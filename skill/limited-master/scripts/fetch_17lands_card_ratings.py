#!/usr/bin/env python3
"""Fetch and summarize 17Lands card ratings data for Limited."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ENDPOINT = "https://www.17lands.com/card_ratings/data"

METRICS = {
    "gih": "win_rate",
    "win_rate": "win_rate",
    "oh": "opening_hand_win_rate",
    "opening_hand": "opening_hand_win_rate",
    "drawn": "drawn_win_rate",
    "iwd": "drawn_improvement_win_rate",
    "improvement": "drawn_improvement_win_rate",
    "alsa": "avg_seen",
    "avg_seen": "avg_seen",
    "ata": "avg_pick",
    "avg_pick": "avg_pick",
    "play_rate": "play_rate",
    "games": "game_count",
}

RATE_FIELDS = {
    "play_rate",
    "win_rate",
    "opening_hand_win_rate",
    "drawn_win_rate",
    "drawn_improvement_win_rate",
}

DEFAULT_COLUMNS = [
    "name",
    "color",
    "rarity",
    "game_count",
    "play_rate",
    "win_rate",
    "opening_hand_win_rate",
    "drawn_win_rate",
    "drawn_improvement_win_rate",
    "avg_seen",
    "avg_pick",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch 17Lands /card_ratings/data and print a Limited card table."
    )
    parser.add_argument("--expansion", required=True, help="Set code, e.g. TDM, EOE, FIN.")
    parser.add_argument(
        "--format",
        default="PremierDraft",
        help="17Lands format, e.g. PremierDraft, TradDraft, Sealed. Default: PremierDraft.",
    )
    parser.add_argument(
        "--colors",
        help="Optional 17Lands colors filter passed to the API, e.g. WU or BR.",
    )
    parser.add_argument(
        "--user-group",
        help="Optional 17Lands user_group filter passed through as-is.",
    )
    parser.add_argument(
        "--rarity",
        nargs="*",
        help="Local rarity filter: common uncommon rare mythic.",
    )
    parser.add_argument(
        "--color",
        help="Local color filter. Use W/U/B/R/G; C matches colorless.",
    )
    parser.add_argument("--name", help="Local case-insensitive card name substring filter.")
    parser.add_argument(
        "--min-games",
        type=int,
        default=100,
        help="Minimum game_count to include. Default: 100.",
    )
    parser.add_argument(
        "--sort",
        default="gih",
        choices=sorted(METRICS),
        help="Sort metric. Common: gih, oh, drawn, iwd, alsa, ata, play_rate, games.",
    )
    parser.add_argument(
        "--ascending",
        action="store_true",
        help="Sort ascending. Useful for ALSA/ATA when looking for earliest-picked cards.",
    )
    parser.add_argument("--top", type=int, default=20, help="Rows to print. Default: 20.")
    parser.add_argument(
        "--output",
        help="Optional output path. Extension controls format: .json, .csv, or .md.",
    )
    parser.add_argument("--endpoint", default=ENDPOINT, help=argparse.SUPPRESS)
    parser.add_argument("--timeout", type=int, default=30, help="HTTP timeout seconds.")
    return parser.parse_args()


def build_url(args: argparse.Namespace) -> str:
    params = {
        "expansion": args.expansion,
        "format": args.format,
    }
    if args.colors is not None:
        params["colors"] = args.colors
    if args.user_group is not None:
        params["user_group"] = args.user_group
    return args.endpoint + "?" + urllib.parse.urlencode(params)


def fetch_json(url: str, timeout: int) -> list[dict[str, Any]]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "limited-master/1.0 (+https://www.17lands.com)",
            "Accept": "application/json,text/plain,*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        text = response.read().decode("utf-8")
    text = text.strip()
    if not text.startswith("["):
        raise RuntimeError(
            "17Lands did not return JSON. The endpoint may have changed; "
            "open https://www.17lands.com/card_data manually and verify filters."
        )
    data = json.loads(text)
    if not isinstance(data, list):
        raise RuntimeError("Unexpected 17Lands response shape; expected a JSON list.")
    return data


def normalize_rarity(value: str | None) -> str:
    return (value or "").strip().lower()


def include_row(row: dict[str, Any], args: argparse.Namespace) -> bool:
    if args.min_games and (row.get("game_count") or 0) < args.min_games:
        return False
    if args.rarity:
        wanted = {normalize_rarity(r) for r in args.rarity}
        if normalize_rarity(row.get("rarity")) not in wanted:
            return False
    if args.color:
        wanted = args.color.upper()
        color = (row.get("color") or "").upper()
        if wanted == "C":
            if color:
                return False
        elif wanted not in color:
            return False
    if args.name and args.name.lower() not in (row.get("name") or "").lower():
        return False
    return True


def sort_rows(rows: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    metric = METRICS[args.sort]
    present = [row for row in rows if row.get(metric) is not None]
    missing = [row for row in rows if row.get(metric) is None]

    return sorted(present, key=lambda row: row.get(metric), reverse=not args.ascending) + missing


def fmt_value(field: str, value: Any) -> str:
    if value is None:
        return ""
    if field in RATE_FIELDS:
        try:
            return f"{float(value) * 100:.1f}%"
        except (TypeError, ValueError):
            return str(value)
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def markdown_table(rows: list[dict[str, Any]], columns: list[str] = DEFAULT_COLUMNS) -> str:
    headers = {
        "name": "Name",
        "color": "Color",
        "rarity": "Rarity",
        "game_count": "Games",
        "play_rate": "Play Rate",
        "win_rate": "GIH WR",
        "opening_hand_win_rate": "OH WR",
        "drawn_win_rate": "Drawn WR",
        "drawn_improvement_win_rate": "IWD",
        "avg_seen": "ALSA",
        "avg_pick": "ATA",
    }
    lines = []
    lines.append("| " + " | ".join(headers.get(c, c) for c in columns) + " |")
    lines.append("| " + " | ".join("---" for _ in columns) + " |")
    for row in rows:
        lines.append("| " + " | ".join(fmt_value(c, row.get(c)) for c in columns) + " |")
    return "\n".join(lines)


def write_output(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix.lower() == ".json":
        path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    elif path.suffix.lower() == ".csv":
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=DEFAULT_COLUMNS, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
    elif path.suffix.lower() in {".md", ".markdown"}:
        path.write_text(markdown_table(rows) + "\n", encoding="utf-8")
    else:
        raise RuntimeError("Output extension must be .json, .csv, or .md")


def main() -> int:
    args = parse_args()
    url = build_url(args)
    try:
        data = fetch_json(url, args.timeout)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        print(f"Tried: {url}", file=sys.stderr)
        return 1

    rows = [row for row in data if include_row(row, args)]
    rows = sort_rows(rows, args)
    if args.top > 0:
        rows = rows[: args.top]

    if args.output:
        write_output(Path(args.output), rows)

    print(f"Source: {url}")
    print(f"Rows: {len(rows)}")
    print(markdown_table(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
