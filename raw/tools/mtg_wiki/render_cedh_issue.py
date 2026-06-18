#!/usr/bin/env python3
"""
Render a parsed cEDH Issue Form (JSON) into a spec-compliant content block .md
and print its target path. Used by the issue-to-PR workflow.

SECURITY (per proposal v0.5): all user-controlled values arrive via a JSON file
(NOT inline in shell), and every value is YAML-safe-serialized (json.dumps for
strings, list literals built explicitly) so a malicious Issue cannot inject
frontmatter keys, break out of the block, or run commands. Output path is
whitelisted to cedh/<subdir>/<sanitized-slug>.md.

Usage:
  python3 render_cedh_issue.py issue.json
    (issue.json = output of stefanbuck/github-issue-parser; fields keyed by id)

Prints the written file path on stdout.  Stdlib only.
"""

import json
import re
import sys
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CEDH = ROOT / "wiki" / "branches" / "strategy" / "cedh"

BLOCK_MAP = {
    "套牌拆解 (cedh-deck)": ("cedh-deck", "decks", "synthesis"),
    "Meta 快照 (cedh-meta)": ("cedh-meta", "meta-snapshots", "synthesis"),
    "决策树 (cedh-decision-tree)": ("cedh-decision-tree", "decision-trees", "decision-tree"),
    "组合技/Stax锁 (cedh-combo)": ("cedh-combo", "combos", "concept"),
    "单卡评估 (cedh-card-eval)": ("cedh-card-eval", "card-evaluations", "concept"),
}
ARCH_OK = {"Turbo", "Stax", "Midrange", "Adaptive"}
PAIR_OK = {"single", "partner", "partner-with", "friends-forever", "background"}
SLUG_RE = re.compile(r"[^a-z0-9-]")


def sanitize_slug(s: str) -> str:
    s = (s or "").strip().lower().replace(" ", "-")
    s = SLUG_RE.sub("", s)            # drop anything not [a-z0-9-]; kills ../ and /
    s = re.sub(r"-+", "-", s).strip("-")
    if not s:
        raise SystemExit("ERROR: slug 为空或非法")
    return s


def yml_str(v: str) -> str:
    """YAML-safe scalar via JSON double-quoting (valid YAML, escapes injection)."""
    return json.dumps(v if v is not None else "", ensure_ascii=False)


def yml_list(items) -> str:
    items = [i for i in (items or []) if str(i).strip()]
    if not items:
        return "[]"
    return "\n" + "\n".join(f"  - {yml_str(str(i).strip())}" for i in items)


def lines_to_list(text):
    return [l.strip() for l in (text or "").splitlines() if l.strip()]


def main(argv=None):
    src = Path((argv or sys.argv[1:])[0])
    data = json.loads(src.read_text(encoding="utf-8"))

    block_label = (data.get("block") or "").strip()
    if block_label not in BLOCK_MAP:
        raise SystemExit(f"ERROR: 未知内容块类型 `{block_label}`")
    block, subdir, ftype = BLOCK_MAP[block_label]

    slug = sanitize_slug(data.get("slug", ""))
    today = datetime.date.today().isoformat()
    as_of = (data.get("as_of") or "").strip() or today
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", as_of):
        as_of = today
    if block == "cedh-meta":
        fname = f"{as_of}-{slug}.md" if not slug.startswith(as_of) else f"{slug}.md"
    else:
        fname = f"{slug}.md"

    out = CEDH / subdir / fname
    # whitelist guard: resolved path must stay under cedh/<subdir>/
    if not str(out.resolve()).startswith(str((CEDH / subdir).resolve()) + "/"):
        raise SystemExit("ERROR: 解析出的路径越界")

    arch = (data.get("archetype") or "").strip()
    arch = arch if arch in ARCH_OK else ""
    pair = (data.get("pair_type") or "").strip()
    pair = pair if pair in PAIR_OK else "single"
    commander = (data.get("commander") or "").strip()
    cards = lines_to_list(data.get("cards_cited"))
    sources = lines_to_list(data.get("sources"))
    title = (data.get("title_name") or slug).strip()
    body = data.get("body") or ""

    fm = [
        "---",
        f"created: {today}",
        f"updated: {today}",
        f"type: {ftype}",
        f"block: {block}",
        "format: cedh",
        f"tags: [cEDH, {block}]",
        f"commander: {yml_str(commander)}",
    ]
    if block == "cedh-deck":
        fm.append(f"pair_type: {pair}")
    fm.append(f"archetype: {yml_str(arch)}")
    fm.append(f"sources: {yml_list(sources)}")
    fm.append(f"as_of: {as_of}")
    fm.append(f"cards_cited: {yml_list(cards)}")
    fm.append("---")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(fm) + f"\n\n# {title}\n\n{body}\n", encoding="utf-8")
    print(out.relative_to(ROOT).as_posix())
    return 0


if __name__ == "__main__":
    sys.exit(main())
