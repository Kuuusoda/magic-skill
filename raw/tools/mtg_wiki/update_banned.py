#!/usr/bin/env python3
"""
Extract banned/restricted cards from oracle-cards-lite.json and update
wiki/concepts/banned-and-restricted.md with current lists.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).resolve().parents[3]
ORACLE_PATH = PROJECT_ROOT / "raw" / "data" / "oracle-cards-lite.json"
BANNED_MD = PROJECT_ROOT / "wiki" / "concepts" / "banned-and-restricted.md"

# Formats we care about (skip obscure ones)
FORMAT_NAMES = {
    "standard": "标准 (Standard)",
    "pioneer": "先驱 (Pioneer)",
    "modern": "摩登 (Modern)",
    "legacy": "薪传 (Legacy)",
    "vintage": "特选 (Vintage)",
    "commander": "指挥官 (Commander)",
    "pauper": "纯铁 (Pauper)",
    "historic": "史迹 (Historic)",
    "timeless": "永恒 (Timeless)",
    "explorer": "探索 (Explorer)",
    "alchemy": "炼金 (Alchemy)",
    "brawl": "斗士 (Brawl)",
}

def main():
    print("Loading cards...")
    if not ORACLE_PATH.exists():
        print(f"❌ oracle-cards-lite.json 不存在: {ORACLE_PATH}", file=sys.stderr)
        sys.exit(1)

    with open(ORACLE_PATH, "r", encoding="utf-8") as f:
        cards = json.load(f)
    print(f"  Loaded {len(cards)} cards")

    # Extract banned/restricted
    banned_by_format = defaultdict(list)
    restricted_by_format = defaultdict(list)

    for card in cards:
        name = card.get("name", "")
        legalities = card.get("legalities", {})
        if not legalities:
            continue
        for fmt, status in legalities.items():
            if status == "banned":
                banned_by_format[fmt].append(name)
            elif status == "restricted":
                restricted_by_format[fmt].append(name)

    # Sort names within each format
    for fmt in banned_by_format:
        banned_by_format[fmt].sort()
    for fmt in restricted_by_format:
        restricted_by_format[fmt].sort()

    # Format counts
    banner_total = sum(len(v) for v in banned_by_format.values())
    restricted_total = sum(len(v) for v in restricted_by_format.values())
    print(f"\nExtracting banned/restricted...")
    print(f"  Banned: {banner_total}, Restricted: {restricted_total}")

    # Check if there were changes from previous run
    # by loading the old data section from the md file
    old_section = ""
    if BANNED_MD.exists():
        content = BANNED_MD.read_text(encoding="utf-8")
        marker = "<!-- AUTO-BANNED-DATA-START -->"
        end_marker = "<!-- AUTO-BANNED-DATA-END -->"
        if marker in content and end_marker in content:
            start = content.index(marker)
            end = content.index(end_marker) + len(end_marker)
            old_section = content[start:end]

    # Build new data section
    lines = ["<!-- AUTO-BANNED-DATA-START -->", ""]
    lines.append(f"> 自动生成于 {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append(f"> 数据来源: Scryfall Oracle Cards")
    lines.append(f"> 禁牌总数: {banner_total} | 限牌总数: {restricted_total}")
    lines.append("")

    # Sorted formats for consistent output
    all_formats = sorted(set(list(banned_by_format.keys()) + list(restricted_by_format.keys())))

    for fmt in all_formats:
        fmt_display = FORMAT_NAMES.get(fmt, fmt)
        banned = banned_by_format.get(fmt, [])
        restricted = restricted_by_format.get(fmt, [])

        if not banned and not restricted:
            continue

        lines.append(f"### {fmt_display}")
        lines.append("")

        if banned:
            lines.append(f"**禁牌 ({len(banned)} 张):**")
            lines.append("")
            for name in banned:
                lines.append(f"- {name}")
            lines.append("")

        if restricted:
            lines.append(f"**限牌 ({len(restricted)} 张):**")
            lines.append("")
            for name in restricted:
                lines.append(f"- {name}")
            lines.append("")

    lines.append("<!-- AUTO-BANNED-DATA-END -->")
    new_section = "\n".join(lines)

    # Compare with old
    if new_section == old_section:
        print("  No changes.")
        # Still update the updated field in frontmatter
        return update_frontmatter_date()

    print("  Changes detected, updating file...")

    # Read full file and replace or append the data section
    if BANNED_MD.exists():
        content = BANNED_MD.read_text(encoding="utf-8")
        marker = "<!-- AUTO-BANNED-DATA-START -->"
        end_marker = "<!-- AUTO-BANNED-DATA-END -->"

        if marker in content and end_marker in content:
            start = content.index(marker)
            end = content.index(end_marker) + len(end_marker)
            new_content = content[:start] + new_section + content[end:]
        else:
            # Append after the existing content
            new_content = content.rstrip() + "\n\n---\n\n" + new_section + "\n"
    else:
        # Create new file with frontmatter
        new_content = f"""---
created: 2026-06-15
updated: 2026-06-15
type: concept
tags: [万智牌, 赛制, 规则, 禁限牌表]
sources: [scryfall-oracle-cards]
---

# 禁限牌表（Banned & Restricted Lists）

{new_section}
"""

    BANNED_MD.write_text(new_content, encoding="utf-8")
    print(f"Written to {BANNED_MD}")


def update_frontmatter_date():
    """Update the 'updated' field in frontmatter."""
    if not BANNED_MD.exists():
        return
    content = BANNED_MD.read_text(encoding="utf-8")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    import re
    content = re.sub(r"(updated:\s*)\S+", rf"\g<1>{today}", content)
    BANNED_MD.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
