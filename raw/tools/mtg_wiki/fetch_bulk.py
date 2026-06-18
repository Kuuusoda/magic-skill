#!/usr/bin/env python3
"""
Fetch a Scryfall bulk-data file.

Scryfall bulk download URIs are NOT stable: you must first query
https://api.scryfall.com/bulk-data, find the entry by `type`, and use its
`download_uri` (which embeds a timestamp and changes on each refresh). The
entry's `updated_at` is the right value to key an actions/cache on.

Usage:
  python3 fetch_bulk.py oracle_cards            # -> prints output path
  python3 fetch_bulk.py all_cards -o /tmp/all.json
  python3 fetch_bulk.py oracle_cards --print-meta   # only print updated_at + uri (no download)

Bulk types: oracle_cards | all_cards | default_cards | unique_artwork | rulings | ...

This script uses only the Python standard library (no extra deps) so it runs
unchanged on a GitHub Actions runner.
"""

import argparse
import json
import sys
import urllib.request
from pathlib import Path

BULK_INDEX_URL = "https://api.scryfall.com/bulk-data"
UA = "mtg-wiki-skill/1.0 (+github community contribution CI)"


def _open(url: str, timeout: int = 60):
    """Return an OPEN urllib response; caller is responsible for closing it."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    return urllib.request.urlopen(req, timeout=timeout)


def resolve_bulk(bulk_type: str) -> dict:
    """Return the bulk-data entry dict for the given type (has download_uri, updated_at, size)."""
    with _open(BULK_INDEX_URL) as resp:
        index = json.load(resp)
    for entry in index.get("data", []):
        if entry.get("type") == bulk_type:
            return entry
    available = ", ".join(e.get("type", "?") for e in index.get("data", []))
    raise SystemExit(f"bulk type '{bulk_type}' not found. Available: {available}")


def download(uri: str, out_path: Path, timeout: int = 600) -> Path:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with _open(uri, timeout=timeout) as resp, open(out_path, "wb") as f:
        # stream to disk; bulk files can be hundreds of MB to multiple GB
        while True:
            chunk = resp.read(1 << 20)  # 1 MiB
            if not chunk:
                break
            f.write(chunk)
    return out_path


def main(argv=None):
    p = argparse.ArgumentParser(description="Fetch a Scryfall bulk-data file.")
    p.add_argument("bulk_type", help="oracle_cards | all_cards | default_cards | rulings | ...")
    p.add_argument("-o", "--out", help="output path (default: ./<type>-<updated_at>.json)")
    p.add_argument("--print-meta", action="store_true",
                   help="only print type/updated_at/size/download_uri as JSON, do not download")
    args = p.parse_args(argv)

    entry = resolve_bulk(args.bulk_type)
    meta = {
        "type": entry.get("type"),
        "updated_at": entry.get("updated_at"),
        "size": entry.get("size"),
        "download_uri": entry.get("download_uri"),
    }
    if args.print_meta:
        print(json.dumps(meta, ensure_ascii=False))
        return 0

    stamp = (entry.get("updated_at") or "")[:10]
    out = Path(args.out) if args.out else Path(f"{args.bulk_type}-{stamp}.json")
    download(entry["download_uri"], out)
    # emit the path on stdout so a workflow step can capture it
    print(str(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
