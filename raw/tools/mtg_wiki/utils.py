"""
mtg-judge utilities: HTTP client, rate limiter, cache manager, config.
"""

import json
import os
import re
import time
import hashlib
from pathlib import Path
from typing import Any, Optional
from urllib import request, error, parse

# ── Paths ──────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_DIR / "data"
CACHE_DIR = BASE_DIR / "cache"
DATA_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)

# Project root: utils.py is at raw/tools/mtg_wiki/utils.py
PROJECT_ROOT = Path(__file__).resolve().parents[3]

ORACLE_CARDS_PATH = PROJECT_ROOT / "raw" / "data" / "oracle-cards-lite.json"
WIKI_CONCEPTS_DIR = PROJECT_ROOT / "wiki" / "concepts"
CR_DIR = PROJECT_ROOT / "raw" / "cr"

# ── API Config ─────────────────────────────────────────────────────
MTGCH_BASE = "https://mtgch.com/api/v1"
SCRYFALL_BASE = "https://api.scryfall.com"

MTGCH_DELAY = 0.2   # seconds between mtgch requests
SCRYFALL_DELAY = 0.1  # seconds between scryfall requests

DEFAULT_CACHE_TTL_DAYS = 30

# ── Rate Limiter ───────────────────────────────────────────────────
class RateLimiter:
    def __init__(self, delay: float):
        self.delay = delay
        self._last = 0.0

    def wait(self):
        now = time.time()
        elapsed = now - self._last
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        self._last = time.time()

_mtch_limiter = RateLimiter(MTGCH_DELAY)
_scryfall_limiter = RateLimiter(SCRYFALL_DELAY)

# ── Cache Manager ──────────────────────────────────────────────────
class CacheManager:
    def __init__(self, cache_dir: Path = CACHE_DIR, ttl_days: int = DEFAULT_CACHE_TTL_DAYS):
        self.cache_dir = cache_dir
        self.ttl = ttl_days * 86400

    def _key(self, url: str) -> str:
        return hashlib.sha256(url.encode()).hexdigest()[:32] + ".json"

    def _path(self, url: str) -> Path:
        return self.cache_dir / self._key(url)

    def get(self, url: str) -> Optional[dict]:
        path = self._path(url)
        if not path.exists():
            return None
        if time.time() - path.stat().st_mtime > self.ttl:
            path.unlink(missing_ok=True)
            return None
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None

    def set(self, url: str, data: dict):
        path = self._path(url)
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

_cache = CacheManager()

# ── HTTP Client ────────────────────────────────────────────────────
def http_get(url: str, headers: Optional[dict] = None, rate_limiter: Optional[RateLimiter] = None, use_cache: bool = True) -> dict:
    """GET with rate limiting, caching, and JSON parsing. Returns {} on failure."""
    if use_cache:
        cached = _cache.get(url)
        if cached is not None:
            return cached

    if rate_limiter:
        rate_limiter.wait()

    req = request.Request(url, headers=headers or {"User-Agent": "mtg-judge-skill/1.0"})
    try:
        with request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if use_cache:
                _cache.set(url, data)
            return data
    except error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore") if hasattr(e, "read") else ""
        return {"error": True, "status": e.code, "body": body, "url": url}
    except Exception as e:
        return {"error": True, "message": str(e), "url": url}


def mtgch_get(endpoint: str, params: Optional[dict] = None) -> dict:
    """Call mtgch API. endpoint should start with '/'."""
    url = MTGCH_BASE + endpoint
    if params:
        url += "?" + parse.urlencode(params)
    return http_get(url, rate_limiter=_mtch_limiter)


SCRYFALL_HEADERS = {
    "User-Agent": "mtg-judge-skill/1.0 (github.com/mtg-judge)",
    "Accept": "application/json",
}


def scryfall_get(endpoint: str, params: Optional[dict] = None) -> dict:
    """Call Scryfall API. endpoint should start with '/'."""
    url = SCRYFALL_BASE + endpoint
    if params:
        url += "?" + parse.urlencode(params)
    return http_get(url, headers=SCRYFALL_HEADERS, rate_limiter=_scryfall_limiter)

# ── String Helpers ─────────────────────────────────────────────────
def normalize_name(name: str) -> str:
    """Lowercase, strip, remove accents for fuzzy matching.
    Preserves CJK characters for Chinese name matching."""
    if not name:
        return ""
    lowered = name.lower().strip()
    # Keep a-z, 0-9, and CJK characters (一-鿿)
    return re.sub(r"[^a-z0-9一-鿿]", "", lowered)


def detect_language(text: str) -> str:
    """'zh' if >50% CJK chars, else 'en'."""
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    total = len(text.strip())
    return "zh" if total > 0 and cjk / total > 0.5 else "en"


def levenshtein(a: str, b: str) -> int:
    """Compute Levenshtein distance."""
    if len(a) < len(b):
        return levenshtein(b, a)
    if len(b) == 0:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a):
        curr = [i + 1]
        for j, cb in enumerate(b):
            curr.append(min(
                curr[-1] + 1,
                prev[j + 1] + 1,
                prev[j] + (0 if ca == cb else 1)
            ))
        prev = curr
    return prev[-1]

# ── Wiki Concept Index Loader ──────────────────────────────────────
_cached_concept_index: Optional[dict] = None

def load_concept_index() -> dict:
    """Load concept slug -> {title, tags, cr_refs} mapping from wiki/concepts."""
    global _cached_concept_index
    if _cached_concept_index is not None:
        return _cached_concept_index

    idx: dict[str, dict] = {}
    if not WIKI_CONCEPTS_DIR.exists():
        _cached_concept_index = idx
        return idx

    for p in WIKI_CONCEPTS_DIR.glob("*.md"):
        slug = p.stem
        title = slug
        tags = []
        cr_refs = []
        try:
            with open(p, "r", encoding="utf-8") as f:
                content = f.read()
            # Simple frontmatter parse
            if content.startswith("---"):
                end = content.find("---", 3)
                if end != -1:
                    fm = content[3:end].strip()
                    for line in fm.splitlines():
                        if line.startswith("tags:"):
                            tags = [t.strip() for t in line.split(":", 1)[1].strip(" []").split(",") if t.strip()]
            # Extract title from first H1
            m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            if m:
                title = m.group(1).strip()
            # Extract CR refs like CR 101.4, CR 704.5
            cr_refs = list(set(re.findall(r"CR\s+(\d+(?:\.\d+[a-z]?)?)", content, re.IGNORECASE)))
        except Exception:
            pass
        idx[slug] = {"title": title, "tags": tags, "cr_refs": cr_refs, "path": str(p)}
    _cached_concept_index = idx
    return idx
