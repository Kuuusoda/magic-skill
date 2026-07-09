#!/usr/bin/env python3
"""
Lint strategy community content blocks across supported MTG formats.

This generalizes the original cEDH-only lint gate to handle both cEDH and
Duel Commander blocks. It intentionally lints only content-block directories,
not strategy index/source-registry/alias pages or templates with placeholders.

Usage:
  python3 lint_strategy_block.py <file1.md> [file2.md ...]
  python3 lint_strategy_block.py --changed <base_ref>

Exit code: 0 = all pass, 1 = at least one ERROR.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STRATEGY_ROOT = "wiki/branches/strategy"

FORMAT_DIRS = {
    "cedh": "cedh",
    "duel-commander": "duel-commander",
}

# block -> (format, subdir, required type)
BLOCKS = {
    "cedh-deck": ("cedh", "decks", "synthesis"),
    "cedh-meta": ("cedh", "meta-snapshots", "synthesis"),
    "cedh-decision-tree": ("cedh", "decision-trees", "decision-tree"),
    "cedh-combo": ("cedh", "combos", "concept"),
    "cedh-card-eval": ("cedh", "card-evaluations", "concept"),
    "dc-deck": ("duel-commander", "decks", "synthesis"),
    "dc-meta": ("duel-commander", "meta-snapshots", "synthesis"),
    "dc-decision-tree": ("duel-commander", "decision-trees", "decision-tree"),
    "dc-combo": ("duel-commander", "combos", "concept"),
    "dc-card-eval": ("duel-commander", "card-evaluations", "concept"),
    "dc-banlist": ("duel-commander", "banlist", "synthesis"),
}

ARCHETYPE_ENUM = {
    "cedh": {"Turbo", "Stax", "Midrange", "Adaptive", ""},
    "duel-commander": {"Aggro", "Control", "Midrange", "Combo", "Stax", "Voltron", "Tempo", ""},
}
PAIR_ENUM = {"single", "partner", "partner-with", "friends-forever", "background", ""}

EXHAUSTIVE = {"cedh-combo", "cedh-card-eval", "dc-combo", "dc-card-eval"}
SUBSET = {"cedh-deck", "dc-deck"}
EXEMPT = {"cedh-meta", "cedh-decision-tree", "dc-meta", "dc-decision-tree", "dc-banlist"}

BASE_REQUIRED = ["created", "updated", "type", "block", "format", "tags", "sources"]
REQUIRED_BY_BLOCK = {
    "cedh-deck": ["as_of", "commander", "pair_type", "archetype", "cards_cited"],
    "cedh-meta": ["as_of", "cards_cited"],
    "cedh-decision-tree": ["as_of", "cards_cited"],
    "cedh-combo": ["as_of", "cards_cited"],
    "cedh-card-eval": ["as_of", "cards_cited"],
    "dc-deck": [
        "as_of", "banlist_as_of", "rules_as_of", "match_policy",
        "commander", "pair_type", "archetype", "cards_cited",
    ],
    "dc-meta": ["as_of", "banlist_as_of", "rules_as_of", "match_policy", "cards_cited"],
    "dc-decision-tree": ["as_of", "rules_as_of", "cards_cited"],
    "dc-combo": ["as_of", "rules_as_of", "cards_cited"],
    "dc-card-eval": ["as_of", "rules_as_of", "cards_cited"],
    "dc-banlist": [
        "banlist_as_of", "rules_as_of", "banned", "banned_as_commander",
        "generated_by", "source_hash",
    ],
}

DATE_FIELDS = {"created", "updated", "as_of", "banlist_as_of", "rules_as_of"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
BILINGUAL_RE = re.compile(r".+（.+）\s*$")


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, "缺少 YAML frontmatter（文件须以 --- 开头）"
    end = text.find("\n---", 3)
    if end == -1:
        return None, "frontmatter 未闭合（缺第二个 ---）"
    body = text[3:end].strip("\n")
    data, cur_key = {}, None
    for raw in body.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        if re.match(r"^\s+-\s+", line):
            if cur_key is None:
                continue
            item = re.sub(r"^\s+-\s+", "", line)
            item = _strip_comment_and_quotes(item)
            if not isinstance(data.get(cur_key), list):
                data[cur_key] = []
            data[cur_key].append(item)
            continue
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2)
        cur_key = key
        val = _strip_comment_and_quotes(val)
        if val == "":
            data[key] = ""
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [_strip_comment_and_quotes(x) for x in inner.split(",") if x.strip()] if inner else []
        else:
            data[key] = val
    return data, None


def _strip_comment_and_quotes(s):
    s = re.sub(r"\s+#.*$", "", s).strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        s = s[1:-1]
    return s.strip()


def _as_list(value):
    if isinstance(value, list):
        return value
    if value in (None, ""):
        return []
    return [value]


def _tags(fm):
    return {str(t).strip() for t in _as_list(fm.get("tags", [])) if str(t).strip()}


def _is_content_block_path(rel):
    for fmt, fmt_dir in FORMAT_DIRS.items():
        for block, (block_fmt, subdir, _type) in BLOCKS.items():
            if block_fmt != fmt:
                continue
            if rel.startswith(f"{STRATEGY_ROOT}/{fmt_dir}/{subdir}/") and rel.endswith(".md"):
                return True
    return False


def lint_file(path: Path, errors, warns):
    rel = path.relative_to(ROOT).as_posix() if path.is_absolute() else path.as_posix()

    def err(m): errors.append(f"ERROR: {rel}: {m}")
    def warn(m): warns.append(f"WARN: {rel}: {m}")

    if not path.exists():
        err("文件不存在")
        return
    text = path.read_text(encoding="utf-8")
    fm, perr = parse_frontmatter(text)
    if perr:
        err(perr)
        return

    block = fm.get("block", "")
    if block not in BLOCKS:
        err(f"block=`{block}` 不在允许块类型 {sorted(BLOCKS)}")
        return

    expected_format, subdir, want_type = BLOCKS[block]
    required = BASE_REQUIRED + REQUIRED_BY_BLOCK.get(block, [])
    for f in required:
        if f not in fm:
            err(f"frontmatter 缺字段 `{f}`")

    if fm.get("type") != want_type:
        err(f"type=`{fm.get('type')}` 与 block=`{block}` 不符（应为 `{want_type}`）")

    fmt = fm.get("format", "")
    if fmt != expected_format:
        err(f"format=`{fmt}` 与 block=`{block}` 不符（应为 `{expected_format}`）")

    expect_dir = f"{STRATEGY_ROOT}/{FORMAT_DIRS[expected_format]}/{subdir}/"
    if not rel.startswith(expect_dir):
        err(f"文件应落在 `{expect_dir}`，实际 `{rel}`")

    stem = path.stem
    if not SLUG_RE.match(stem) and not DATE_RE.match(stem[:10]):
        err(f"文件名 `{stem}` 应为小写短横线（meta 块可用 YYYY-MM-DD- 前缀）")

    arch = fm.get("archetype", "")
    if arch not in ARCHETYPE_ENUM.get(expected_format, {""}):
        err(f"archetype=`{arch}` 不在 format=`{expected_format}` 的枚举 {sorted(ARCHETYPE_ENUM[expected_format])}")

    if block.endswith("-deck"):
        pt = fm.get("pair_type", "")
        if pt not in PAIR_ENUM:
            err(f"pair_type=`{pt}` 不在枚举 {sorted(PAIR_ENUM)}")

    for df in DATE_FIELDS:
        if df in fm and isinstance(fm[df], str) and fm[df] and not DATE_RE.match(fm[df]):
            err(f"{df}=`{fm[df]}` 应为 YYYY-MM-DD")

    sources = fm.get("sources", [])
    if block in {"cedh-meta", "dc-meta"} and not _as_list(sources):
        if "seed" in _tags(fm):
            warn("Meta seed 允许 sources 为空；正式快照必须补来源")
        else:
            err("Meta 快照必须有 sources（P3 时效数据须标来源）")

    if block == "dc-banlist":
        for field in ("banned", "banned_as_commander"):
            if field in fm and not isinstance(fm[field], list):
                err(f"{field} 必须是 frontmatter list")

    cc = _as_list(fm.get("cards_cited", []))
    if block in EXHAUSTIVE and not cc:
        err(f"block=`{block}` 须穷举 cards_cited（至少 1 张）")
    if block in SUBSET and not cc:
        warn(f"block=`{block}` 建议列核心 cards_cited（代表性子集）")
    for c in cc:
        if c and not BILINGUAL_RE.match(c):
            err(f"cards_cited 项 `{c}` 非「中文（English）」双语格式")

    for link in re.findall(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", text):
        link = link.strip()
        if link.startswith(("http://", "https://")):
            continue
        target = link if link.endswith(".md") else link + ".md"
        candidates = [
            path.parent / target,
            ROOT / "wiki" / target,
            ROOT / STRATEGY_ROOT / target,
        ]
        base = Path(target).name
        found = any(c.exists() for c in candidates) or bool(list((ROOT / "wiki").rglob(base)))
        if not found:
            warn(f"WikiLink `[[{link}]]` 未解析到现有页面")

    body = text[text.find("\n---", 3) + 4:] if text.startswith("---") else text
    cc_norm = {re.sub(r"\s", "", c) for c in cc}
    for mention in set(re.findall(r"([\u4e00-\u9fffA-Za-z][\u4e00-\u9fffA-Za-z0-9·'，、 -]*（[A-Za-z][^）]*）)", body)):
        if re.sub(r"\s", "", mention) not in cc_norm:
            warn(f"正文出现疑似牌名 `{mention.strip()}` 不在 cards_cited（一致性）")


def changed_files(base_ref):
    out = subprocess.run(
        ["git", "diff", "--name-only", f"{base_ref}...HEAD"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    ).stdout
    return [ROOT / l for l in out.splitlines() if _is_content_block_path(l)]


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("files", nargs="*")
    p.add_argument("--changed", metavar="BASE_REF", help="lint strategy content blocks changed vs BASE_REF")
    args = p.parse_args(argv)

    targets = [Path(f) for f in args.files]
    if args.changed:
        targets += changed_files(args.changed)
    if not targets:
        print("no strategy content block files to lint")
        return 0

    errors, warns = [], []
    for t in targets:
        lint_file(t if t.is_absolute() else (ROOT / t), errors, warns)

    for w in warns:
        print(w)
    for e in errors:
        print(e)
    print(f"\n--- strategy lint: {len(targets)} file(s), {len(errors)} error(s), {len(warns)} warning(s) ---")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
