#!/usr/bin/env python3
"""
Build the CN<->EN official name index from a Scryfall bulk file.

WHY all_cards (not default_cards/oracle_cards):
  - oracle_cards has one English entry per oracle_id, NO printed_name.
  - default_cards keeps one printing per card, English-preferred → filtering
    lang==zhs yields almost nothing.
  - all_cards contains EVERY printing in EVERY language, so the Simplified
    Chinese (lang=="zhs") printings with `printed_name` live there.

Field shape (verified against live Scryfall):
  a zhs card object has:  lang=="zhs", name (EN), printed_name (CN), oracle_id
  double-faced / split cards carry per-face names under `card_faces`
  (each face has name + printed_name); top-level printed_name may be absent.

Output: cn_name_index.json — a single committed source of truth:
  {
    "by_oracle_id": { "<oracle_id>": {"en": "...", "cn": "..."} },
    "en_to_cn":     { "<normalized EN>": "<CN>" },
    "cn_to_en":     { "<normalized CN>": "<EN>" },
    "meta": {"source_updated_at": "...", "count": N}
  }

Usage:
  python3 build_cn_index.py all-cards-YYYYMMDD.json
  python3 build_cn_index.py all-cards.json -o ../../data/cn_name_index.json --updated-at 2026-06-17

Stdlib only (runs unchanged on a CI runner). For multi-GB all_cards, this
streams via ijson if available, else falls back to json.load (more memory).
"""

import argparse
import json
import sys
from pathlib import Path

# normalize_name is the same normalization card_search uses, so EN/CN keys match lookups.
try:
    from utils import normalize_name, CN_NAME_INDEX_PATH
except Exception:  # allow running outside the package dir
    import re

    def normalize_name(name: str) -> str:
        if not name:
            return ""
        lowered = name.lower().strip()
        return re.sub(r"[^a-z0-9一-鿿]", "", lowered)

    CN_NAME_INDEX_PATH = Path("cn_name_index.json")


def _iter_cards(path: Path):
    """Yield card dicts from a Scryfall bulk JSON array, streaming if ijson is present."""
    try:
        import ijson  # optional; avoids loading multi-GB all_cards into memory
        with open(path, "rb") as f:
            yield from ijson.items(f, "item")
        return
    except ImportError:
        pass
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    yield from data


def _faces_pairs(card: dict):
    """Yield (en, cn) name pairs for a zhs card, handling single + multi-face cards."""
    en_top = card.get("name")
    cn_top = card.get("printed_name")
    if cn_top:
        # single-faced (or top-level combined name present)
        yield en_top, cn_top
        return
    faces = card.get("card_faces") or []
    en_parts, cn_parts = [], []
    for face in faces:
        fe, fc = face.get("name"), face.get("printed_name")
        if fe and fc:
            en_parts.append(fe)
            cn_parts.append(fc)
            yield fe, fc  # also index each face individually
    if en_parts and cn_parts:
        # combined "A // B" form (matches how split/MDFC names appear)
        yield " // ".join(en_parts), " // ".join(cn_parts)


def build(bulk_path: Path, updated_at: str = "") -> dict:
    by_oracle_id = {}
    en_to_cn = {}
    cn_to_en = {}
    seen = 0
    for card in _iter_cards(bulk_path):
        if card.get("lang") != "zhs":
            continue
        oid = card.get("oracle_id")
        got_pair = False
        for en, cn in _faces_pairs(card):
            if not en or not cn:
                continue
            got_pair = True
            en_to_cn.setdefault(normalize_name(en), cn)
            cn_to_en.setdefault(normalize_name(cn), en)
        if got_pair and oid and oid not in by_oracle_id:
            # store the primary (top-level) EN/CN for the oracle id
            en_main = card.get("name", "")
            cn_main = card.get("printed_name") or " // ".join(
                f.get("printed_name", "") for f in (card.get("card_faces") or [])
            ).strip(" /")
            by_oracle_id[oid] = {"en": en_main, "cn": cn_main}
            seen += 1
    return {
        "by_oracle_id": by_oracle_id,
        "en_to_cn": en_to_cn,
        "cn_to_en": cn_to_en,
        "meta": {"source_updated_at": updated_at, "count": seen},
    }


def main(argv=None):
    p = argparse.ArgumentParser(description="Build CN<->EN name index from Scryfall all_cards bulk.")
    p.add_argument("bulk_path", help="path to Scryfall all_cards bulk JSON")
    p.add_argument("-o", "--out", help=f"output path (default: {CN_NAME_INDEX_PATH})")
    p.add_argument("--updated-at", default="", help="bulk updated_at to record in meta")
    args = p.parse_args(argv)

    bulk = Path(args.bulk_path)
    if not bulk.exists():
        raise SystemExit(f"bulk file not found: {bulk}")
    out = Path(args.out) if args.out else Path(CN_NAME_INDEX_PATH)
    index = build(bulk, args.updated_at)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"CN<->EN index: {index['meta']['count']} zhs cards → {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
