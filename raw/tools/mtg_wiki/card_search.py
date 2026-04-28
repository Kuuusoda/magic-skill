#!/usr/bin/env python3
"""
Card search: local index + mtgch API + Scryfall fallback.
Supports exact, fuzzy, prefix matching for EN; mtgch/Scryfall for CN.
"""

import json
import re
from pathlib import Path
from typing import Optional

from utils import (
    DATA_DIR,
    normalize_name,
    detect_language,
    levenshtein,
    mtgch_get,
    scryfall_get,
)

# ── Load indices ───────────────────────────────────────────────────
_name_index: Optional[dict] = None
_prefix_index: Optional[dict] = None


def _load_indices():
    global _name_index, _prefix_index
    if _name_index is None:
        path = DATA_DIR / "card_name_index.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                _name_index = json.load(f)
        else:
            _name_index = {}
    if _prefix_index is None:
        path = DATA_DIR / "card_prefix_index.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                _prefix_index = json.load(f)
        else:
            _prefix_index = {}


# ── Local search ───────────────────────────────────────────────────
def local_exact(name: str) -> Optional[dict]:
    """Exact match by normalized name."""
    _load_indices()
    norm = normalize_name(name)
    # Guard against empty normalized names (e.g. all-special-char input)
    if not norm:
        return None
    return _name_index.get(norm)


def local_fuzzy(name: str, max_dist: int = 2, top_n: int = 5) -> list[dict]:
    """Fuzzy match using Levenshtein distance on normalized names."""
    _load_indices()
    norm = normalize_name(name)
    if len(norm) < 3:
        return []
    candidates = []
    for key, card in _name_index.items():
        dist = levenshtein(norm, key)
        if dist <= max_dist:
            candidates.append((dist, card))
    candidates.sort(key=lambda x: x[0])
    return [c[1] for c in candidates[:top_n]]


def local_prefix(prefix: str, limit: int = 10) -> list[dict]:
    """Prefix autocomplete."""
    _load_indices()
    norm = normalize_name(prefix)
    if len(norm) < 2:
        return []
    keys = _prefix_index.get(norm, [])
    return [_name_index[k] for k in keys[:limit] if k in _name_index]


# ── API search ─────────────────────────────────────────────────────
def mtgch_search(name: str) -> Optional[dict]:
    """Search mtgch API. Returns first matching card or None."""
    r = mtgch_get("/result", {"q": name, "priority_chinese": "true"})
    items = r.get("items", [])
    if not items:
        return None
    # Prefer exact name match
    norm_query = normalize_name(name)
    for item in items:
        if normalize_name(item.get("name", "")) == norm_query:
            return _mtgch_to_card(item)
    # Also check face_name for split/aftermath cards
    for item in items:
        if normalize_name(item.get("face_name", "")) == norm_query:
            return _mtgch_to_card(item)
    # Fall back to first result
    return _mtgch_to_card(items[0])


def scryfall_fuzzy(name: str) -> Optional[dict]:
    """Scryfall fuzzy named search."""
    r = scryfall_get("/cards/named", {"fuzzy": name})
    if r.get("error") or r.get("object") == "error":
        return None
    return _scryfall_to_card(r)


def scryfall_search_cn(name: str) -> Optional[dict]:
    """Scryfall search for Chinese printed name."""
    r = scryfall_get("/cards/search", {
        "q": f'lang:zhs "{name}"',
        "unique": "prints",
    })
    if r.get("error") or r.get("object") == "error":
        return None
    data = r.get("data", [])
    if not data:
        return None
    return _scryfall_to_card(data[0])


# ── Data normalizers ───────────────────────────────────────────────
def _mtgch_to_card(item: dict) -> dict:
    """Normalize mtgch item to our card format."""
    return {
        "oracle_id": item.get("oracle_id"),
        "name": item.get("name", ""),
        "face_name": item.get("face_name"),
        "type_line": item.get("type_line", ""),
        "oracle_text": item.get("oracle_text", ""),
        "mana_cost": item.get("mana_cost", ""),
        "cmc": item.get("cmc"),
        "colors": item.get("colors", []),
        "color_identity": item.get("color_identity", []),
        "keywords": item.get("keywords", []),
        "power": item.get("power"),
        "toughness": item.get("toughness"),
        "loyalty": item.get("loyalty"),
        "legalities": item.get("legalities", {}),
        "rarity": item.get("rarity", ""),
        "set_name": item.get("set_name", ""),
        "set": item.get("set", ""),
        "released_at": item.get("released_at", ""),
        "source": "mtgch",
    }


def _scryfall_to_card(item: dict) -> dict:
    """Normalize Scryfall item to our card format."""
    return {
        "oracle_id": item.get("oracle_id"),
        "name": item.get("name", ""),
        "face_name": item.get("card_faces", [{}])[0].get("name") if item.get("card_faces") else None,
        "type_line": item.get("type_line", ""),
        "oracle_text": item.get("oracle_text", ""),
        "mana_cost": item.get("mana_cost", ""),
        "cmc": item.get("cmc"),
        "colors": item.get("colors", []),
        "color_identity": item.get("color_identity", []),
        "keywords": item.get("keywords", []),
        "power": item.get("power"),
        "toughness": item.get("toughness"),
        "loyalty": item.get("loyalty"),
        "legalities": item.get("legalities", {}),
        "rarity": item.get("rarity", ""),
        "set_name": item.get("set_name", ""),
        "set": item.get("set", ""),
        "released_at": item.get("released_at", ""),
        "printed_name": item.get("printed_name"),
        "printed_text": item.get("printed_text"),
        "printed_type_line": item.get("printed_type_line"),
        "lang": item.get("lang"),
        "image_uris": item.get("image_uris", {}),
        "source": "scryfall",
    }


# ── Unified search ─────────────────────────────────────────────────
def search(name: str, allow_api: bool = True) -> Optional[dict]:
    """
    Unified card search.

    Strategy:
      1. Local exact match (EN only; local index has no CN names)
      2. Local fuzzy match (EN only)
      3. mtgch API (primary for CN; fallback for EN)
      4. Scryfall fallback
    """
    lang = detect_language(name)

    # 1. Local exact (EN only — local index has no Chinese printed_name data)
    if lang == "en":
        result = local_exact(name)
        if result:
            return result

    # 2. Local fuzzy (EN only)
    if lang == "en":
        fuzzy = local_fuzzy(name)
        if fuzzy:
            return fuzzy[0]

    if not allow_api:
        return None

    # 3. mtgch API (best for Chinese; also works for English)
    result = mtgch_search(name)
    if result:
        return result

    # 4. Scryfall fallback
    if lang == "zh":
        result = scryfall_search_cn(name)
    else:
        result = scryfall_fuzzy(name)
    return result


def search_multi(names: list[str], allow_api: bool = True) -> dict[str, Optional[dict]]:
    """Search multiple cards at once."""
    return {name: search(name, allow_api) for name in names}


# ── CLI ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Lightning Bolt"
    result = search(query)
    if result:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Card not found: {query}")
