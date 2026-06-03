#!/usr/bin/env python3
"""
Local index for mtgch's static card_names.json.

Why this exists:
  card_search.py / name_translator.py used to hit mtgch + Scryfall over the
  network for every Chinese query (rate-limited, slow). The static file
  https://mtgch.com/static/card_names.json contains 33k+ unique cards with
  the official Chinese translation, so we can serve EN↔CN lookups locally
  in O(1) after building the index once.

Row format from upstream (35,745 rows of 5 columns each):
    [english_name, chinese_name, image_url, scryfall_id, mtgch_oracle_id]

Notes:
  - Same English name appears multiple times across printings (different
    scryfall_ids). We pick the row with an image as the canonical record.
  - Split / DFC cards are encoded with a single '/' (e.g. "Wear/Tear").
    We index both the merged form and each face separately. '//' is rare
    and part of the actual name (e.g. "SP//dr"), so we never split on it.

CLI usage:
    python3 mtgch_name_index.py --update            # download + (re)build
    python3 mtgch_name_index.py --update --force    # force re-download
    python3 mtgch_name_index.py --stats             # report index sizes
    python3 mtgch_name_index.py "Lightning Bolt"    # lookup
    python3 mtgch_name_index.py "闪电击"             # lookup
"""

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional

from utils import DATA_DIR, detect_language, normalize_name

MTGCH_NAMES_URL = "https://mtgch.com/static/card_names.json"
USER_AGENT = "mtg-judge-skill/1.0 (mtgch-name-index)"

RAW_PATH = DATA_DIR / "mtgch_card_names_raw.json"
META_PATH = DATA_DIR / "mtgch_card_names_meta.json"
INDEX_PATH = DATA_DIR / "mtgch_name_index.json"

_UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
    re.IGNORECASE,
)


def _load_meta() -> dict:
    if not META_PATH.exists():
        return {}
    try:
        with open(META_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save_meta(meta: dict) -> None:
    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)


def download(force: bool = False) -> tuple[bool, str]:
    """Fetch the static card_names.json, honouring ETag / Last-Modified.

    Returns (changed, message). `changed` is True iff the local raw file
    was rewritten with fresh content.
    """
    meta = _load_meta()
    headers = {"User-Agent": USER_AGENT}
    if not force and RAW_PATH.exists():
        if etag := meta.get("etag"):
            headers["If-None-Match"] = etag
        if lm := meta.get("last_modified"):
            headers["If-Modified-Since"] = lm

    req = urllib.request.Request(MTGCH_NAMES_URL, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = resp.read()
            # Sanity-check JSON before overwriting cache
            decoded = json.loads(payload.decode("utf-8"))
            with open(RAW_PATH, "wb") as f:
                f.write(payload)
            meta = {
                "etag": resp.headers.get("ETag", ""),
                "last_modified": resp.headers.get("Last-Modified", ""),
                "content_length": len(payload),
                "row_count": len(decoded),
            }
            _save_meta(meta)
            return True, (
                f"Downloaded {len(payload):,} bytes, {len(decoded):,} rows "
                f"(Last-Modified: {meta['last_modified'] or 'n/a'})"
            )
    except urllib.error.HTTPError as e:
        if e.code == 304:
            return False, "Not modified — local cache is current."
        return False, f"HTTPError {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        return False, f"URLError: {e.reason}"
    except Exception as e:
        return False, f"Download failed: {e}"


def _split_faces(en: str, cn: str) -> list[tuple[str, str]]:
    """Yield (merged, face1, face2, ...) name pairs for a row.

    mtgch joins the two faces of a split / DFC card with a single '/'.
    '//' is part of the printed name (e.g. "SP//dr") and never separates
    faces, so we only split when '/' is present without '//'.
    """
    pairs: list[tuple[str, str]] = [(en, cn)]
    if "/" in en and "//" not in en and "/" in cn:
        en_parts = [p.strip() for p in en.split("/")]
        cn_parts = [p.strip() for p in cn.split("/")]
        if len(en_parts) == len(cn_parts):
            for ep, cp in zip(en_parts, cn_parts):
                if ep and cp:
                    pairs.append((ep, cp))
    return pairs


def build() -> dict:
    """Build the four-way index from the cached raw file.

    Each scryfall_id can show up in several rows of card_names.json:
    one per face plus an optional merged "Face A/Face B" row. We
    consolidate them so we can index every face (and the merged form)
    separately while sharing scryfall_id / image / mtgch_id.
    """
    if not RAW_PATH.exists():
        raise FileNotFoundError(
            f"Raw mtgch data missing at {RAW_PATH}. Run `--update` first."
        )
    with open(RAW_PATH, "r", encoding="utf-8") as f:
        rows = json.load(f)

    # Per-sid aggregator: image / mtgch_id (first non-empty wins) and a
    # face dict keyed by normalized English so we don't double-count
    # punctuation variants of the same printed name.
    info: dict[str, dict] = {}
    for row in rows:
        if not isinstance(row, list) or len(row) != 5:
            continue
        en, cn, img, sid, mid = row
        if not sid:
            continue
        slot = info.setdefault(
            sid,
            {"image": "", "mtgch_id": "", "faces": {}, "merged": None},
        )
        if img and not slot["image"]:
            slot["image"] = img
        if mid and not slot["mtgch_id"]:
            slot["mtgch_id"] = mid

        pairs = _split_faces(en, cn)
        if len(pairs) > 1:
            # First pair is the merged form; remember it once.
            if slot["merged"] is None:
                slot["merged"] = pairs[0]
            face_pairs = pairs[1:]
        else:
            face_pairs = pairs

        for face_en, face_cn in face_pairs:
            key = normalize_name(face_en)
            if key:
                slot["faces"].setdefault(key, {"en": face_en, "cn": face_cn})

    by_en: dict[str, dict] = {}
    by_cn: dict[str, dict] = {}
    by_scryfall: dict[str, dict] = {}
    by_mtgch: dict[str, dict] = {}

    for sid, slot in info.items():
        image = slot["image"]
        mid = slot["mtgch_id"]
        face_records: list[dict] = []
        for face in slot["faces"].values():
            rec = {
                "en": face["en"],
                "cn": face["cn"],
                "scryfall_id": sid,
                "mtgch_id": mid,
                "image": image,
            }
            if slot["merged"]:
                rec["merged_en"] = slot["merged"][0]
                rec["merged_cn"] = slot["merged"][1]
            face_records.append(rec)
            en_norm = normalize_name(face["en"])
            cn_norm = normalize_name(face["cn"])
            if en_norm:
                by_en.setdefault(en_norm, rec)
            if cn_norm:
                by_cn.setdefault(cn_norm, rec)

        # Choose the canonical record for sid / mtgch_id lookups.
        # Merged form (if present) wins, otherwise the first face.
        if slot["merged"]:
            m_en, m_cn = slot["merged"]
            canonical = {
                "en": m_en,
                "cn": m_cn,
                "scryfall_id": sid,
                "mtgch_id": mid,
                "image": image,
                "faces": [{"en": r["en"], "cn": r["cn"]} for r in face_records],
            }
            by_en.setdefault(normalize_name(m_en), canonical)
            by_cn.setdefault(normalize_name(m_cn), canonical)
        elif face_records:
            canonical = face_records[0]
        else:
            continue

        by_scryfall[sid] = canonical
        if mid:
            by_mtgch.setdefault(mid, canonical)

    index = {
        "by_en": by_en,
        "by_cn": by_cn,
        "by_scryfall": by_scryfall,
        "by_mtgch": by_mtgch,
    }
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        # Compact form — index is dict-of-dicts, no need for pretty indent
        json.dump(index, f, ensure_ascii=False, separators=(",", ":"))
    return index


_cached_index: Optional[dict] = None


def load() -> dict:
    """Load the index from disk (cached in-process)."""
    global _cached_index
    if _cached_index is None:
        if INDEX_PATH.exists():
            with open(INDEX_PATH, "r", encoding="utf-8") as f:
                _cached_index = json.load(f)
        else:
            _cached_index = {
                "by_en": {},
                "by_cn": {},
                "by_scryfall": {},
                "by_mtgch": {},
            }
    return _cached_index


def update(force: bool = False) -> dict:
    """Download fresh data when changed, then (re)build the index."""
    changed, msg = download(force=force)
    print(msg)
    global _cached_index
    if changed or not INDEX_PATH.exists():
        print("Building index...")
        _cached_index = None
        idx = build()
        print(
            f"  by_en: {len(idx['by_en']):,}  "
            f"by_cn: {len(idx['by_cn']):,}  "
            f"by_scryfall: {len(idx['by_scryfall']):,}  "
            f"by_mtgch: {len(idx['by_mtgch']):,}"
        )
        return idx
    return load()


def lookup(query: str) -> Optional[dict]:
    """Find a card record by EN / CN / scryfall_id / mtgch_id.

    Returns the canonical record (or None if not found). Language is
    detected by character ratio; CJK input checks the CN index first,
    otherwise the EN index is tried first.
    """
    if not query:
        return None
    idx = load()
    q = query.strip()
    if _UUID_RE.match(q):
        key = q.lower()
        return idx["by_scryfall"].get(key) or idx["by_mtgch"].get(key)
    norm = normalize_name(q)
    if not norm:
        return None
    if detect_language(q) == "zh":
        return idx["by_cn"].get(norm) or idx["by_en"].get(norm)
    return idx["by_en"].get(norm) or idx["by_cn"].get(norm)


def _print_stats() -> None:
    idx = load()
    meta = _load_meta()
    print(f"Raw cache: {RAW_PATH} ({'present' if RAW_PATH.exists() else 'missing'})")
    print(f"  Last-Modified: {meta.get('last_modified', 'n/a')}")
    print(f"  ETag:          {meta.get('etag', 'n/a')}")
    print(f"  Size:          {meta.get('content_length', 0):,} bytes")
    print(f"  Row count:     {meta.get('row_count', 0):,}")
    print(f"Index: {INDEX_PATH} ({'present' if INDEX_PATH.exists() else 'missing'})")
    for k in ("by_en", "by_cn", "by_scryfall", "by_mtgch"):
        print(f"  {k}: {len(idx.get(k, {})):,}")


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 0
    if argv[0] in ("--update", "-u"):
        force = "--force" in argv or "-f" in argv
        update(force=force)
        return 0
    if argv[0] in ("--stats", "-s"):
        _print_stats()
        return 0
    if argv[0] in ("--help", "-h"):
        print(__doc__)
        return 0
    query = " ".join(argv)
    result = lookup(query)
    if result:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    print(f"not found: {query}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
