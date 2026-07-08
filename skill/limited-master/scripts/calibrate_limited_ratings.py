#!/usr/bin/env python3
"""Compare Limited ratings against an external reference and summarize gaps."""

from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calibrate a Limited card-rating table against a reference table."
    )
    parser.add_argument("--ours", required=True, help="Our ratings file: .json or .csv.")
    parser.add_argument("--reference", required=True, help="Reference ratings file: .json or .csv.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument("--name-field", default="display_name", help="Our card-name field.")
    parser.add_argument("--rating-field", default="rating", help="Our rating field.")
    parser.add_argument("--ref-name-field", default="name", help="Reference card-name field.")
    parser.add_argument("--ref-rating-field", default="cfb_rating", help="Reference rating field.")
    parser.add_argument("--threshold", type=float, default=1.0, help="Major disagreement threshold.")
    return parser.parse_args()


def load_table(path: Path) -> list[dict[str, Any]]:
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise RuntimeError(f"{path} must contain a JSON list.")
        return data
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8") as handle:
            return list(csv.DictReader(handle))
    raise RuntimeError("Input files must be .json or .csv")


def norm_name(value: Any) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower()
    text = text.replace("’", "'").replace("`", "'").replace("´", "'")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def as_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def group_summary(rows: list[dict[str, Any]], field: str) -> list[tuple[str, list[dict[str, Any]]]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[str(row.get(field) or "")].append(row)
    return sorted(groups.items(), key=lambda item: (-len(item[1]), item[0]))


def fmt(value: float | None) -> str:
    if value is None:
        return ""
    return f"{value:.2f}".rstrip("0").rstrip(".")


def build_report(
    ours: list[dict[str, Any]],
    refs: list[dict[str, Any]],
    args: argparse.Namespace,
) -> str:
    ref_by_name = {norm_name(row.get(args.ref_name_field)): row for row in refs}
    matched = []
    missing = []

    for row in ours:
        our_rating = as_float(row.get(args.rating_field))
        ref = ref_by_name.get(norm_name(row.get(args.name_field)))
        ref_rating = as_float(ref.get(args.ref_rating_field)) if ref else None
        if ref is None or our_rating is None or ref_rating is None:
            missing.append(row)
            continue
        delta = our_rating - ref_rating
        combined = dict(row)
        combined["_reference_rating"] = ref_rating
        combined["_reference_raw"] = ref.get("cfb_raw") or ref.get("raw") or ""
        combined["_delta"] = delta
        combined["_abs_delta"] = abs(delta)
        matched.append(combined)

    major_over = sorted(
        [row for row in matched if row["_delta"] >= args.threshold],
        key=lambda row: row["_delta"],
        reverse=True,
    )
    major_under = sorted(
        [row for row in matched if row["_delta"] <= -args.threshold],
        key=lambda row: row["_delta"],
    )

    lines = ["# Limited Rating Calibration Report", ""]
    lines.append(f"- Our rows: {len(ours)}")
    lines.append(f"- Reference rows: {len(refs)}")
    lines.append(f"- Matched rows: {len(matched)}")
    lines.append(f"- Missing or unscored rows: {len(missing)}")
    if matched:
        lines.append(f"- Mean delta ours-reference: {statistics.mean(row['_delta'] for row in matched):+.2f}")
        lines.append(f"- Mean absolute delta: {statistics.mean(row['_abs_delta'] for row in matched):.2f}")
        for threshold in (0.25, 0.5, 0.75, 1.0):
            count = sum(1 for row in matched if row["_abs_delta"] <= threshold)
            lines.append(f"- Within {threshold:.2f}: {count}/{len(matched)}")

    lines += ["", "## Major Overratings", ""]
    lines.append("| Card | Ours | Reference | Delta | Raw | Note |")
    lines.append("|---|---:|---:|---:|---|---|")
    for row in major_over[:40]:
        lines.append(
            f"| {row.get(args.name_field, '')} | {fmt(as_float(row.get(args.rating_field)))} | "
            f"{fmt(row['_reference_rating'])} | {row['_delta']:+.2f} | "
            f"{str(row.get('_reference_raw', '')).replace('|', '/')} | "
            f"{str(row.get('note', '')).replace('|', '/')} |"
        )

    lines += ["", "## Major Underratings", ""]
    lines.append("| Card | Ours | Reference | Delta | Raw | Note |")
    lines.append("|---|---:|---:|---:|---|---|")
    for row in major_under[:40]:
        lines.append(
            f"| {row.get(args.name_field, '')} | {fmt(as_float(row.get(args.rating_field)))} | "
            f"{fmt(row['_reference_rating'])} | {row['_delta']:+.2f} | "
            f"{str(row.get('_reference_raw', '')).replace('|', '/')} | "
            f"{str(row.get('note', '')).replace('|', '/')} |"
        )

    for field in ("rarity", "colors"):
        if not any(field in row for row in matched):
            continue
        lines += ["", f"## By {field}", ""]
        lines.append("| Group | Count | Mean Delta | Mean Abs Delta | Over | Under |")
        lines.append("|---|---:|---:|---:|---:|---:|")
        for group, rows in group_summary(matched, field):
            lines.append(
                f"| {group or '(blank)'} | {len(rows)} | "
                f"{statistics.mean(row['_delta'] for row in rows):+.2f} | "
                f"{statistics.mean(row['_abs_delta'] for row in rows):.2f} | "
                f"{sum(1 for row in rows if row['_delta'] >= args.threshold)} | "
                f"{sum(1 for row in rows if row['_delta'] <= -args.threshold)} |"
            )

    lines += ["", "## Calibration Prompts", ""]
    lines.append("- For each overrating, ask: did we mistake ceiling for baseline, ignore mana cost, or overvalue narrow synergy?")
    lines.append("- For each underrating, ask: did we miss repeatable advantage, immediate board impact, cheap snowballing, or format-level fixing?")
    lines.append("- Rewrite future notes so every 3.0+ card explains why it is better than replaceable filler.")
    lines.append("- Use range or split ratings for cards whose value changes by archetype instead of forcing everything into a single middle score.")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    ours = load_table(Path(args.ours))
    refs = load_table(Path(args.reference))
    report = build_report(ours, refs, args)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
