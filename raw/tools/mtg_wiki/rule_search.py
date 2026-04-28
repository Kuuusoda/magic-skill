#!/usr/bin/env python3
"""
Rule search: CR/MTR/IPG keyword and rule-number lookup.
Searches local indices, CR markdown files, and wiki concept pages.
"""

import json
import re
from pathlib import Path
from typing import Optional

from utils import DATA_DIR, CR_DIR, WIKI_CONCEPTS_DIR, load_concept_index

# ── Load indices ───────────────────────────────────────────────────
_cr_index: Optional[dict] = None
_concept_index: Optional[dict] = None
_concept_title_map: Optional[dict] = None


def _load_indices():
    global _cr_index, _concept_index, _concept_title_map
    if _cr_index is None:
        path = DATA_DIR / "cr_rule_index.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                _cr_index = json.load(f)
        else:
            _cr_index = {}
    if _concept_index is None:
        _concept_index = load_concept_index()
    if _concept_title_map is None:
        path = DATA_DIR / "concept_title_map.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                _concept_title_map = json.load(f)
        else:
            _concept_title_map = {}


# ── Rule number lookup ─────────────────────────────────────────────
def lookup_cr(rule_num: str) -> Optional[dict]:
    """Lookup a CR rule by number (e.g. '101.4', '704.5a')."""
    _load_indices()
    return _cr_index.get(rule_num)


def lookup_cr_context(rule_num: str, context_lines: int = 3) -> Optional[dict]:
    """Lookup a CR rule with surrounding context lines."""
    info = lookup_cr(rule_num)
    if not info:
        return None
    cr_file = CR_DIR / info["file"]
    if not cr_file.exists():
        return info
    with open(cr_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    start = max(0, info["line"] - 1 - context_lines)
    end = min(len(lines), info["line"] + context_lines)
    return {
        **info,
        "context": "".join(lines[start:end]).strip(),
    }


# ── Keyword search in CR ───────────────────────────────────────────
def search_cr_keyword(keyword: str, max_results: int = 10) -> list[dict]:
    """Search CR files for lines containing keyword (Chinese or English)."""
    results = []
    keyword_lower = keyword.lower()
    if not CR_DIR.exists():
        return results
    for cr_file in sorted(CR_DIR.glob("[0-9].md")):
        with open(cr_file, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                if keyword_lower in line.lower():
                    # Strip HTML tags for readability
                    text = re.sub(r"<[^>]+>", "", line).strip()
                    if text and len(text) > 10:
                        results.append({
                            "file": cr_file.name,
                            "line": lineno,
                            "text": text,
                        })
                    if len(results) >= max_results:
                        return results
    return results


# ── Concept page lookup ────────────────────────────────────────────
def lookup_concept(name: str) -> Optional[dict]:
    """Find a wiki concept page by title or slug."""
    _load_indices()
    slug = _concept_title_map.get(name)
    if not slug:
        # Try normalized match
        for title, s in _concept_title_map.items():
            if name.lower() in title.lower() or title.lower() in name.lower():
                slug = s
                break
    if not slug:
        return None
    info = _concept_index.get(slug)
    if not info:
        return None
    # Load page content
    path = WIKI_CONCEPTS_DIR / f"{slug}.md"
    content = ""
    if path.exists():
        content = path.read_text(encoding="utf-8")
    return {
        "slug": slug,
        "title": info["title"],
        "tags": info.get("tags", []),
        "cr_refs": info.get("cr_refs", []),
        "content": content,
    }


# ── Unified rule search ────────────────────────────────────────────
def search(query: str) -> dict:
    """
    Unified rule search.

    1. If query looks like a rule number (e.g. '101.4', '704.5a'), lookup directly.
    2. Search concept pages by title.
    3. Search CR files for keyword.
    """
    # Rule number pattern
    if re.match(r"^\d+(\.\d+[a-z]?)?$", query.strip()):
        result = lookup_cr_context(query.strip())
        if result:
            return {"type": "rule_number", "results": [result]}

    # Concept lookup
    concept = lookup_concept(query)
    if concept:
        return {"type": "concept", "results": [concept]}

    # CR keyword search
    cr_results = search_cr_keyword(query, max_results=10)
    if cr_results:
        return {"type": "keyword", "results": cr_results}

    return {"type": "none", "results": []}


# ── CLI ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "101.4"
    result = search(query)
    print(json.dumps(result, ensure_ascii=False, indent=2))
