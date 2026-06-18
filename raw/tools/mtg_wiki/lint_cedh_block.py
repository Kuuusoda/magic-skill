#!/usr/bin/env python3
"""
Lint a cEDH community content block (format / path / naming / frontmatter / WikiLink / cards_cited).

This is the FORMAT gate of the CI (it does NOT do card existence/oracle checks —
that is verify_cards.py). Stdlib-only so it runs unchanged on a CI runner.

Usage:
  python3 lint_cedh_block.py <file1.md> [file2.md ...]
  python3 lint_cedh_block.py --changed <base_ref>      # lint files changed vs base (CI)

Exit code: 0 = all pass, 1 = at least one ERROR (warnings alone do not fail).
Output: structured report lines  "<level>: <file>: <message>"  (ERROR / WARN).
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

# repo root: this file is raw/tools/mtg_wiki/lint_cedh_block.py
ROOT = Path(__file__).resolve().parents[3]
CEDH_DIR = "wiki/branches/strategy/cedh"
TEMPLATES_DIR = "wiki/branches/strategy/_templates"

# block -> (subdir, required type)
BLOCKS = {
    "cedh-deck": ("decks", "synthesis"),
    "cedh-meta": ("meta-snapshots", "synthesis"),
    "cedh-decision-tree": ("decision-trees", "decision-tree"),
    "cedh-combo": ("combos", "concept"),
    "cedh-card-eval": ("card-evaluations", "concept"),
}
ARCHETYPE_ENUM = {"cedh": {"Turbo", "Stax", "Midrange", "Adaptive", ""}}
PAIR_ENUM = {"single", "partner", "partner-with", "friends-forever", "background", ""}
# cards_cited strength per block:穷举 / 子集 / 豁免(warning only)
EXHAUSTIVE = {"cedh-combo", "cedh-card-eval"}
SUBSET = {"cedh-deck"}
EXEMPT = {"cedh-meta", "cedh-decision-tree"}

REQUIRED_FIELDS = ["created", "updated", "type", "block", "format", "tags", "sources", "as_of"]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# bilingual card "中文（English）" — full-width parens, CN before EN
BILINGUAL_RE = re.compile(r".+（.+）\s*$")


def parse_frontmatter(text):
    """Minimal YAML-ish frontmatter parser for the block contract.
    Returns (dict, error_or_None). Supports scalars, inline [..] lists, and
    block '- ' lists. Strips inline '# comments' and surrounding quotes."""
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
        if re.match(r"^\s+-\s+", line):  # block list item
            if cur_key is None:
                continue
            item = re.sub(r"^\s+-\s+", "", line)
            item = _strip_comment_and_quotes(item)
            if not isinstance(data.get(cur_key), list):
                data[cur_key] = []  # coerce prior "" scalar to a block list
            data[cur_key].append(item)
            continue
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2)
        cur_key = key
        val = _strip_comment_and_quotes(val)
        if val == "":
            data[key] = ""  # may become a block list if items follow
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [_strip_comment_and_quotes(x) for x in inner.split(",") if x.strip()] if inner else []
        else:
            data[key] = val
    return data, None


def _strip_comment_and_quotes(s):
    # strip an inline comment that is not inside quotes/parens (heuristic: only if preceded by space)
    s = re.sub(r"\s+#.*$", "", s).strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        s = s[1:-1]
    return s.strip()


def lint_file(path: Path, errors, warns):
    rel = path.relative_to(ROOT).as_posix() if path.is_absolute() else path.as_posix()

    def err(m): errors.append(f"ERROR: {rel}: {m}")
    def warn(m): warns.append(f"WARN: {rel}: {m}")

    if not path.exists():
        err("文件不存在"); return
    text = path.read_text(encoding="utf-8")
    fm, perr = parse_frontmatter(text)
    if perr:
        err(perr); return

    # required fields
    for f in REQUIRED_FIELDS:
        if f not in fm:
            err(f"frontmatter 缺字段 `{f}`")

    block = fm.get("block", "")
    if block not in BLOCKS:
        err(f"block=`{block}` 不在允许的 5 类 {list(BLOCKS)}"); 
    else:
        subdir, want_type = BLOCKS[block]
        # type<->block mapping
        if fm.get("type") != want_type:
            err(f"type=`{fm.get('type')}` 与 block=`{block}` 不符（应为 `{want_type}`）")
        # directory placement
        expect_dir = f"{CEDH_DIR}/{subdir}/"
        if not rel.startswith(expect_dir):
            err(f"文件应落在 `{expect_dir}`，实际 `{rel}`")
        # filename slug
        stem = path.stem
        if not SLUG_RE.match(stem) and not DATE_RE.match(stem[:10]):
            err(f"文件名 `{stem}` 应为小写短横线（meta 块可用 YYYY-MM-DD- 前缀）")

    # format / archetype enum
    fmt = fm.get("format", "")
    if fmt != "cedh":
        err(f"format=`{fmt}` 本分支应为 `cedh`")
    arch = fm.get("archetype", "")
    if arch not in ARCHETYPE_ENUM.get(fmt, {""}):
        err(f"archetype=`{arch}` 不在 format=`{fmt}` 的枚举 {sorted(ARCHETYPE_ENUM.get(fmt, set()))}")

    # pair_type (deck only)
    if block == "cedh-deck":
        pt = fm.get("pair_type", "")
        if pt not in PAIR_ENUM:
            err(f"pair_type=`{pt}` 不在枚举 {sorted(PAIR_ENUM)}")

    # dates
    for df in ("created", "updated", "as_of"):
        if df in fm and isinstance(fm[df], str) and fm[df] and not DATE_RE.match(fm[df]):
            err(f"{df}=`{fm[df]}` 应为 YYYY-MM-DD")

    # sources for time-sensitive blocks
    if block == "cedh-meta":
        src = fm.get("sources", [])
        if not (isinstance(src, list) and len(src) > 0):
            err("Meta 快照必须有 sources（P3 时效数据须标来源）")

    # cards_cited strength
    cc = fm.get("cards_cited", [])
    if not isinstance(cc, list):
        cc = [cc] if cc else []
    if block in EXHAUSTIVE and len(cc) == 0:
        err(f"block=`{block}` 须穷举 cards_cited（至少 1 张）")
    if block in SUBSET and len(cc) == 0:
        warn(f"block=`{block}` 建议列核心 cards_cited（代表性子集）")
    # bilingual format of each cited card
    for c in cc:
        if c and not BILINGUAL_RE.match(c):
            err(f"cards_cited 项 `{c}` 非「中文（English）」双语格式")

    # WikiLink / path existence
    for link in re.findall(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", text):
        link = link.strip()
        if link.startswith(("http://", "https://")):
            continue
        # resolve relative to file dir AND to wiki root by slug
        cand = []
        target = link if link.endswith(".md") else link + ".md"
        cand.append((path.parent / target))
        cand.append(ROOT / "wiki" / target)
        # bare slug -> search wiki/** basename
        base = Path(target).name
        found = any(c.exists() for c in cand) or bool(list((ROOT / "wiki").rglob(base)))
        if not found:
            warn(f"WikiLink `[[{link}]]` 未解析到现有页面")

    # consistency: 正文牌名 ⊆ cards_cited (warning) — detect bilingual mentions in body.
    # match a card-like token: a run of CN/letters immediately before （English）, not the
    # whole preceding sentence (stop at spaces/punctuation).
    body = text[text.find("\n---", 3) + 4:] if text.startswith("---") else text
    cc_norm = {re.sub(r"\s", "", c) for c in cc}
    for mention in set(re.findall(r"([\u4e00-\u9fffA-Za-z][\u4e00-\u9fff·'A-Za-z]*（[A-Za-z][^）]*）)", body)):
        if re.sub(r"\s", "", mention) not in cc_norm:
            warn(f"正文出现疑似牌名 `{mention.strip()}` 不在 cards_cited（一致性）")


def changed_files(base_ref):
    out = subprocess.run(
        ["git", "diff", "--name-only", f"{base_ref}...HEAD"],
        cwd=ROOT, capture_output=True, text=True,
    ).stdout
    files = []
    for line in out.splitlines():
        if line.startswith(f"{CEDH_DIR}/") and line.endswith(".md"):
            files.append(ROOT / line)
    return files


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("files", nargs="*")
    p.add_argument("--changed", metavar="BASE_REF", help="lint cedh blocks changed vs BASE_REF")
    args = p.parse_args(argv)

    targets = [Path(f) for f in args.files]
    if args.changed:
        targets += changed_files(args.changed)
    if not targets:
        print("no cedh block files to lint")
        return 0

    errors, warns = [], []
    for t in targets:
        lint_file(t if t.is_absolute() else (ROOT / t), errors, warns)

    for w in warns:
        print(w)
    for e in errors:
        print(e)
    print(f"\n--- lint: {len(targets)} file(s), {len(errors)} error(s), {len(warns)} warning(s) ---")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
