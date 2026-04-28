#!/usr/bin/env python3
"""
Name translator: EN ↔ CN card name translation.
Uses local indices + Scryfall lang:zhs data.
"""

import json
from pathlib import Path
from typing import Optional

from utils import DATA_DIR, normalize_name, detect_language, scryfall_get

# ── Load / build translation cache ─────────────────────────────────
_translation_cache: Optional[dict] = None  # en_norm -> {cn, oracle_id}


def _load_translation_cache():
    global _translation_cache
    if _translation_cache is not None:
        return
    path = DATA_DIR / "cn_en_mapping.json"
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            _translation_cache = json.load(f)
    else:
        _translation_cache = {}


def _save_translation_cache():
    path = DATA_DIR / "cn_en_mapping.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(_translation_cache or {}, f, ensure_ascii=False, indent=2)


def _scryfall_fetch_cn(en_name: str) -> Optional[str]:
    """Fetch Chinese printed name from Scryfall."""
    r = scryfall_get("/cards/search", {
        "q": f'lang:zhs oracle:"{en_name}"',
        "unique": "prints",
    })
    if r.get("error") or r.get("object") == "error":
        return None
    for card in r.get("data", []):
        pn = card.get("printed_name")
        if pn:
            return pn
    return None


def translate(name: str) -> Optional[dict]:
    """
    Translate a card name between English and Chinese.
    Returns {name, translated_name, lang, oracle_id} or None.
    """
    _load_translation_cache()
    lang = detect_language(name)

    if lang == "en":
        # EN -> CN
        norm = normalize_name(name)
        cached = _translation_cache.get(norm)
        if cached and cached.get("cn"):
            return {
                "name": name,
                "translated_name": cached["cn"],
                "lang": "en",
                "oracle_id": cached.get("oracle_id"),
                "source": "cache",
            }
        # Fetch from Scryfall
        cn_name = _scryfall_fetch_cn(name)
        if cn_name:
            _translation_cache[norm] = {"cn": cn_name, "en": name}
            _save_translation_cache()
            return {
                "name": name,
                "translated_name": cn_name,
                "lang": "en",
                "source": "scryfall",
            }
        return None

    else:
        # CN -> EN: search Scryfall by printed_name
        r = scryfall_get("/cards/search", {
            "q": f'lang:zhs "{name}"',
            "unique": "prints",
        })
        if r.get("error") or r.get("object") == "error":
            return None
        for card in r.get("data", []):
            pn = card.get("printed_name", "")
            if name in pn or pn in name:
                en = card.get("name", "")
                _translation_cache[normalize_name(en)] = {
                    "cn": pn,
                    "en": en,
                    "oracle_id": card.get("oracle_id"),
                }
                _save_translation_cache()
                return {
                    "name": name,
                    "translated_name": en,
                    "lang": "zh",
                    "oracle_id": card.get("oracle_id"),
                    "source": "scryfall",
                }
        return None


# ── CLI ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Lightning Bolt"
    result = translate(query)
    if result:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Translation not found: {query}")
