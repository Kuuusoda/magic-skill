#!/usr/bin/env python3
"""
Build local search indices for mtg-judge Skill.

Outputs:
  data/card_name_index.json      — normalized EN name → card summary
  data/card_prefix_index.json    — prefix → list of normalized names
  data/concept_index.json        — concept slug → metadata
  data/concept_title_map.json    — Chinese/English title → slug
  data/cr_rule_index.json        — rule number → {file, line, text}

Usage:
  python3 build_indices.py
"""

import json
import re
from pathlib import Path
from utils import (
    ORACLE_CARDS_PATH,
    WIKI_CONCEPTS_DIR,
    CR_DIR,
    DATA_DIR,
    normalize_name,
)


def build_card_indices():
    """Build card name index and prefix index from oracle-cards-lite.json."""
    print("Loading oracle cards...")
    with open(ORACLE_CARDS_PATH, "r", encoding="utf-8") as f:
        cards = json.load(f)

    name_index = {}
    prefix_index: dict[str, list[str]] = {}

    for card in cards:
        name = card.get("name", "")
        if not name:
            continue
        norm = normalize_name(name)
        name_index[norm] = {
            "oracle_id": card.get("oracle_id"),
            "name": name,
            "type_line": card.get("type_line", ""),
            "oracle_text": card.get("oracle_text", ""),
            "mana_cost": card.get("mana_cost", ""),
            "cmc": card.get("cmc"),
            "colors": card.get("colors", []),
            "color_identity": card.get("color_identity", []),
            "keywords": card.get("keywords", []),
            "power": card.get("power"),
            "toughness": card.get("toughness"),
            "loyalty": card.get("loyalty"),
            "legalities": card.get("legalities", {}),
            "rarity": card.get("rarity", ""),
            "set_name": card.get("set_name", ""),
            "set": card.get("set", ""),
            "released_at": card.get("released_at", ""),
        }

        # Prefix index: first 3 chars up to full name
        for i in range(3, len(norm) + 1):
            prefix = norm[:i]
            if prefix not in prefix_index:
                prefix_index[prefix] = []
            if len(prefix_index[prefix]) < 20:  # cap per prefix
                prefix_index[prefix].append(norm)

    out_name = DATA_DIR / "card_name_index.json"
    out_prefix = DATA_DIR / "card_prefix_index.json"
    with open(out_name, "w", encoding="utf-8") as f:
        json.dump(name_index, f, ensure_ascii=False, indent=2)
    with open(out_prefix, "w", encoding="utf-8") as f:
        json.dump(prefix_index, f, ensure_ascii=False, indent=2)

    print(f"  Card name index: {len(name_index)} cards → {out_name.name}")
    print(f"  Prefix index: {len(prefix_index)} prefixes → {out_prefix.name}")


def build_concept_indices():
    """Build concept index and title-to-slug map from wiki/concepts."""
    print("Scanning wiki/concepts...")
    concept_index = {}
    title_map = {}  # title (CN or EN) -> slug

    if not WIKI_CONCEPTS_DIR.exists():
        print("  No concepts dir found.")
        return

    for p in WIKI_CONCEPTS_DIR.glob("*.md"):
        slug = p.stem
        content = p.read_text(encoding="utf-8")

        # Parse frontmatter
        tags = []
        if content.startswith("---"):
            end = content.find("---", 3)
            if end != -1:
                fm = content[3:end].strip()
                for line in fm.splitlines():
                    if line.startswith("tags:"):
                        tags = [
                            t.strip().strip('"').strip("'")
                            for t in line.split(":", 1)[1].strip(" []").split(",")
                            if t.strip()
                        ]

        # Extract title from first H1
        title = slug
        m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if m:
            title = m.group(1).strip()

        # Extract CR refs
        cr_refs = list(
            set(re.findall(r"CR\s+(\d+(?:\.\d+[a-z]?)?)", content, re.IGNORECASE))
        )
        # Extract MTR refs
        mtr_refs = list(
            set(re.findall(r"MTR\s+(\d+(?:\.\d+)?)", content, re.IGNORECASE))
        )
        # Extract IPG refs
        ipg_refs = list(
            set(re.findall(r"IPG\s+(\d+(?:\.\d+)?)", content, re.IGNORECASE))
        )

        concept_index[slug] = {
            "title": title,
            "tags": tags,
            "cr_refs": cr_refs,
            "mtr_refs": mtr_refs,
            "ipg_refs": ipg_refs,
        }
        title_map[title] = slug
        title_map[slug] = slug  # slug also maps to itself

        # If title contains parenthetical English, also map the Chinese part
        if "（" in title and "）" in title:
            cn_part = title.split("（")[0].strip()
            title_map[cn_part] = slug

    out_concept = DATA_DIR / "concept_index.json"
    out_title = DATA_DIR / "concept_title_map.json"
    with open(out_concept, "w", encoding="utf-8") as f:
        json.dump(concept_index, f, ensure_ascii=False, indent=2)
    with open(out_title, "w", encoding="utf-8") as f:
        json.dump(title_map, f, ensure_ascii=False, indent=2)

    print(f"  Concept index: {len(concept_index)} concepts → {out_concept.name}")
    print(f"  Title map: {len(title_map)} entries → {out_title.name}")


def build_cr_rule_index():
    """Build rule number → {file, line, text} index from CR markdown files."""
    print("Indexing CR rules...")
    rule_index = {}

    if not CR_DIR.exists():
        print("  No CR dir found.")
        return

    cr_files = sorted(CR_DIR.glob("[0-9].md"))
    for cr_file in cr_files:
        with open(cr_file, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                line = line.rstrip("\n")
                # Match <b id='crXXX-Y'>XXX.Y.</b> or <b>XXX.Y</b> patterns
                m = re.search(
                    r"<b\s+id=['\"]cr(\d+(?:\.\d+[a-z]?)?)['\"]>\s*\1\.\s*</b>",
                    line,
                    re.IGNORECASE,
                )
                if not m:
                    # Fallback: match plain <b>100.1.</b> style
                    m = re.search(
                        r"<b>\s*(\d+(?:\.\d+[a-z]?)?)\.\s*</b>", line
                    )
                if m:
                    rule_num = m.group(1)
                    # Extract text after the tag, strip HTML
                    text = re.sub(r"<[^>]+>", "", line).strip()
                    if text:
                        rule_index[rule_num] = {
                            "file": cr_file.name,
                            "line": lineno,
                            "text": text,
                        }

    out_rules = DATA_DIR / "cr_rule_index.json"
    with open(out_rules, "w", encoding="utf-8") as f:
        json.dump(rule_index, f, ensure_ascii=False, indent=2)

    print(f"  CR rule index: {len(rule_index)} rules → {out_rules.name}")


def main():
    print("Building mtg-judge local indices...")
    print(f"Output dir: {DATA_DIR}")
    print()
    build_card_indices()
    build_concept_indices()
    build_cr_rule_index()
    print()
    print("Done.")


if __name__ == "__main__":
    main()
