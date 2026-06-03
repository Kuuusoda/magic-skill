#!/usr/bin/env python3
"""
Scryfall rulings lookup.

Pulls the official WotC rulings for a card via Scryfall's
`/cards/{scryfall_id}/rulings` endpoint and caches the result locally.

Use cases:
  - Judge rule research: the rulings text often clarifies card-specific
    interactions that the Comprehensive Rules describe only in general
    terms (e.g. "How does <triggered ability> interact with <replacement
    effect> on this card?").
  - Card primer / article writing: include WotC's canonical rulings
    alongside Oracle text without paraphrasing.

Lookup order:
  1. Resolve input → scryfall_id (mtgch local index for CN, oracle index
     or mtgch local index for EN, or pass through if input is already a UUID).
  2. Local rulings cache (data/scryfall_rulings/<scryfall_id>.json), TTL 90d.
  3. Scryfall /cards/{id}/rulings (network), cache on success.

Usage:
  python3 scryfall_rulings.py "Lightning Bolt"
  python3 scryfall_rulings.py "闪电击"
  python3 scryfall_rulings.py "f58dba4f-1abb-47a3-a684-29c32bab95c0"
  python3 scryfall_rulings.py "Lumra, Bellow of the Woods" --refresh
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from typing import Optional

from utils import DATA_DIR, detect_language, scryfall_get
import mtgch_name_index

RULINGS_DIR = DATA_DIR / "scryfall_rulings"
RULINGS_DIR.mkdir(exist_ok=True)

CACHE_TTL_SECONDS = 90 * 86400  # 90 days
_UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I)


# ── Card → scryfall_id resolver ─────────────────────────────────────
def _resolve_to_id(query: str) -> Optional[dict]:
    """Resolve an EN/CN name or UUID to a (scryfall_id, en, cn) record.

    Returns dict with keys: scryfall_id, name (EN), cn (CN if known).
    """
    q = (query or "").strip()
    if not q:
        return None

    # Direct UUID pass-through.
    if _UUID_RE.match(q):
        rec = mtgch_name_index.lookup(q)
        if rec:
            return {
                "scryfall_id": rec.get("scryfall_id") or q,
                "name": rec.get("en", ""),
                "cn": rec.get("cn", ""),
            }
        return {"scryfall_id": q, "name": "", "cn": ""}

    # Bridge via local mtgch name index (handles both EN and CN).
    rec = mtgch_name_index.lookup(q)
    if rec and rec.get("scryfall_id"):
        return {
            "scryfall_id": rec["scryfall_id"],
            "name": rec.get("en", ""),
            "cn": rec.get("cn", ""),
        }

    # Scryfall fallback for cards not in the local index (very new / odd).
    if detect_language(q) == "zh":
        r = scryfall_get(
            "/cards/search", {"q": f'lang:zhs "{q}"', "unique": "prints"}
        )
        for card in r.get("data", []) or []:
            pn = card.get("printed_name", "")
            if q in pn or pn in q:
                return {
                    "scryfall_id": card.get("id") or card.get("oracle_id"),
                    "name": card.get("name", ""),
                    "cn": pn,
                }
        return None

    r = scryfall_get("/cards/named", {"fuzzy": q})
    if r.get("object") == "card":
        return {
            "scryfall_id": r.get("id") or r.get("oracle_id"),
            "name": r.get("name", ""),
            "cn": "",
        }
    return None


# ── Rulings cache I/O ───────────────────────────────────────────────
def _cache_path(scryfall_id: str) -> Path:
    return RULINGS_DIR / f"{scryfall_id}.json"


def _read_cache(scryfall_id: str) -> Optional[dict]:
    path = _cache_path(scryfall_id)
    if not path.exists():
        return None
    if time.time() - path.stat().st_mtime > CACHE_TTL_SECONDS:
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def _write_cache(scryfall_id: str, payload: dict) -> None:
    try:
        with open(_cache_path(scryfall_id), "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


# ── Scryfall fetch ──────────────────────────────────────────────────
def _fetch_rulings(scryfall_id: str) -> Optional[list[dict]]:
    """Call Scryfall /cards/{id}/rulings; return list or None on error."""
    r = scryfall_get(f"/cards/{scryfall_id}/rulings")
    if r.get("error") or r.get("object") == "error":
        return None
    if r.get("object") != "list":
        return None
    rulings = []
    for entry in r.get("data", []) or []:
        rulings.append(
            {
                "published_at": entry.get("published_at", ""),
                "comment": entry.get("comment", ""),
                "source": entry.get("source", "wotc"),
            }
        )
    return rulings


# ── Public API ──────────────────────────────────────────────────────
def get_rulings(query: str, refresh: bool = False) -> Optional[dict]:
    """Return a structured rulings payload for the given card.

    Response shape:
      {
        "card": {"name", "cn", "scryfall_id"},
        "rulings": [{"published_at", "comment", "source"}, ...],
        "source": "cache" | "scryfall",
        "fetched_at": ISO date,
      }
    Returns None only if the card itself cannot be resolved.
    """
    card = _resolve_to_id(query)
    if not card or not card.get("scryfall_id"):
        return None

    sid = card["scryfall_id"]

    if not refresh:
        cached = _read_cache(sid)
        if cached is not None:
            cached["source"] = "cache"
            return cached

    rulings = _fetch_rulings(sid)
    if rulings is None:
        return None

    payload = {
        "card": {
            "name": card.get("name", ""),
            "cn": card.get("cn", ""),
            "scryfall_id": sid,
        },
        "rulings": rulings,
        "source": "scryfall",
        "fetched_at": time.strftime("%Y-%m-%d"),
    }
    _write_cache(sid, payload)
    return payload


# ── CLI ─────────────────────────────────────────────────────────────
def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Fetch Scryfall rulings for a card.")
    parser.add_argument("query", help="EN name, CN name, or scryfall_id (UUID)")
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Skip the local cache and refetch from Scryfall.",
    )
    parser.add_argument(
        "--format",
        choices=("json", "text"),
        default="json",
        help="Output format (default json).",
    )
    args = parser.parse_args(argv)

    result = get_rulings(args.query, refresh=args.refresh)
    if result is None:
        print(f"No rulings found / card not resolvable: {args.query}", file=sys.stderr)
        return 1

    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    # Plain-text rendering for quick scanning.
    card = result["card"]
    label = f"{card.get('cn') or ''} ({card['name']})".strip()
    print(f"{label}  [{card['scryfall_id']}]")
    print(f"source: {result['source']}  fetched_at: {result.get('fetched_at', '-')}")
    rulings = result.get("rulings", [])
    if not rulings:
        print("(no rulings recorded)")
        return 0
    for i, r in enumerate(rulings, 1):
        print(f"\n[{i}] {r.get('published_at', '?')}")
        print(r.get("comment", "").strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
