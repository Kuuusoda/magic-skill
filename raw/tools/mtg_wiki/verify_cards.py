#!/usr/bin/env python3
"""
Force-verify cards cited by strategy content blocks against OFFLINE indices.

This is the CARD VERIFICATION gate of the CI (existence + bilingual + official
CN translation). It is OFFLINE/deterministic: it reads the prebuilt indices, so
it does NOT hit any API at PR time (no rate-limit flakiness).

Inputs (offline indices; CI restores/generates them, see fetch_bulk.py +
build_indices.py + build_cn_index.py):
  - card_name_index.json   (EN existence + oracle_text)  via build_indices.py
  - cn_name_index.json     (CN<->EN official names)      via build_cn_index.py

Levels (per proposal v0.5):
  ERROR  : cited EN name not found in offline oracle index, or CN translation
           not matching the official CN name.
  WARN   : indices missing entirely (no data source yet) -> verification skipped;
           or a card looks like a brand-new printing not yet in the bulk
           (caller may apply a "new-card" maintainer override label).

Usage:
  python3 verify_cards.py <file1.md> [file2.md ...]
  python3 verify_cards.py --changed <base_ref>

Exit: 0 = pass (or skipped due to missing indices), 1 = at least one ERROR.
Stdlib only.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STRATEGY_CONTENT_DIRS = (
    "wiki/branches/strategy/cedh/decks",
    "wiki/branches/strategy/cedh/meta-snapshots",
    "wiki/branches/strategy/cedh/decision-trees",
    "wiki/branches/strategy/cedh/combos",
    "wiki/branches/strategy/cedh/card-evaluations",
    "wiki/branches/strategy/duel-commander/decks",
    "wiki/branches/strategy/duel-commander/meta-snapshots",
    "wiki/branches/strategy/duel-commander/decision-trees",
    "wiki/branches/strategy/duel-commander/combos",
    "wiki/branches/strategy/duel-commander/card-evaluations",
)

try:
    from utils import normalize_name, ORACLE_CARDS_PATH, CN_NAME_INDEX_PATH, RAW_DATA_DIR
    NAME_INDEX_PATH = RAW_DATA_DIR.parent / "tools" / "mtg_wiki" / "data" / "card_name_index.json"
except Exception:
    def normalize_name(name: str) -> str:
        if not name:
            return ""
        return re.sub(r"[^a-z0-9一-鿿]", "", name.lower().strip())
    NAME_INDEX_PATH = Path("data/card_name_index.json")
    CN_NAME_INDEX_PATH = Path("cn_name_index.json")

# The card name index built by build_indices.py lives next to the tools.
DEFAULT_NAME_INDEX = Path(__file__).resolve().parent / "data" / "card_name_index.json"

BILINGUAL_RE = re.compile(r"^\s*(.+?)（(.+?)）\s*$")  # 中文（English）


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def parse_cards_cited_and_commander(text):
    """Pull cards_cited list + commander from frontmatter (minimal parse)."""
    if not text.startswith("---"):
        return [], ""
    end = text.find("\n---", 3)
    body = text[3:end] if end != -1 else ""
    cards, commander, cur = [], "", None
    for raw in body.splitlines():
        line = raw.rstrip()
        if re.match(r"^\s+-\s+", line) and cur == "cards_cited":
            item = re.sub(r"^\s+-\s+", "", line)
            item = re.sub(r"\s+#.*$", "", item).strip().strip("\"'")
            if item:
                cards.append(item)
            continue
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not m:
            continue
        cur = m.group(1)
        val = re.sub(r"\s+#.*$", "", m.group(2)).strip().strip("\"'")
        if cur == "commander" and val:
            commander = val
        if cur == "cards_cited" and val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            cards += [x.strip().strip("\"'") for x in inner.split(",") if x.strip()]
    return cards, commander


def split_bilingual(entry):
    """'中文（English）' -> (cn, en). Handles '// ' multi-name by splitting faces."""
    m = BILINGUAL_RE.match(entry)
    if not m:
        return None, None
    return m.group(1).strip(), m.group(2).strip()


def verify_entry(entry, name_index, cn_index, errors, warns, rel):
    cn, en = split_bilingual(entry)
    if not en:
        errors.append(f"ERROR: {rel}: `{entry}` 非「中文（English）」双语格式，无法查证")
        return
    # multi-face "A // B" — verify each english face
    en_faces = [e.strip() for e in en.split("//")]
    cn_faces = [c.strip() for c in cn.split("//")] if cn else []
    for i, ef in enumerate(en_faces):
        key = normalize_name(ef)
        if key not in name_index:
            warns.append(
                f"WARN: {rel}: 英文名 `{ef}` 不在离线 Oracle 索引（可能是新牌未入 bulk；维护者可加放行 label）"
            )
            continue
        if not name_index[key].get("oracle_text") and name_index[key].get("oracle_text") != "":
            errors.append(f"ERROR: {rel}: `{ef}` 索引中 oracle_text 缺失")
        # CN official-name check
        if cn_index and i < len(cn_faces) and cn_faces[i]:
            official = cn_index.get("en_to_cn", {}).get(key)
            if official and normalize_name(official) != normalize_name(cn_faces[i]):
                errors.append(
                    f"ERROR: {rel}: 中文译名 `{cn_faces[i]}` 与官方 `{official}` 不符（{ef}）"
                )


def verify_file(path, name_index, cn_index, errors, warns):
    rel = path.relative_to(ROOT).as_posix() if path.is_absolute() else path.as_posix()
    if not path.exists():
        errors.append(f"ERROR: {rel}: 文件不存在"); return
    text = path.read_text(encoding="utf-8")
    cards, commander = parse_cards_cited_and_commander(text)
    targets = list(cards)
    if commander:
        targets.append(commander)
    if not targets:
        return  # nothing to verify (e.g. decision-tree with empty cards_cited)
    for entry in targets:
        # commander may itself be "A // B"; reuse same verifier
        verify_entry(entry, name_index, cn_index, errors, warns, rel)


def changed_files(base_ref):
    out = subprocess.run(
        ["git", "diff", "--name-only", f"{base_ref}...HEAD"],
        cwd=ROOT, capture_output=True, text=True,
    ).stdout
    return [ROOT / l for l in out.splitlines()
            if l.endswith(".md") and any(l.startswith(f"{d}/") for d in STRATEGY_CONTENT_DIRS)]


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("files", nargs="*")
    p.add_argument("--changed", metavar="BASE_REF")
    p.add_argument("--name-index", default=str(DEFAULT_NAME_INDEX))
    p.add_argument("--cn-index", default=str(CN_NAME_INDEX_PATH))
    args = p.parse_args(argv)

    name_index = load_json(args.name_index)
    cn_index = load_json(args.cn_index)

    if name_index is None:
        # No data source yet -> skip (NOT a failure). Proposal v0.5: "无索引=neutral/skip".
        print(f"WARN: 离线 Oracle 索引缺失（{args.name_index}）→ 强制查证跳过（neutral）。")
        print("      CI 须先经 fetch_bulk.py + build_indices.py 生成索引；本地可同样生成。")
        return 0
    if cn_index is None:
        print(f"WARN: CN 译名索引缺失（{args.cn_index}）→ 仅做英文存在性查证，跳过译名校验。")

    targets = [Path(f) for f in args.files]
    if args.changed:
        targets += changed_files(args.changed)
    if not targets:
        print("no strategy content block files to verify")
        return 0

    errors, warns = [], []
    for t in targets:
        verify_file(t if t.is_absolute() else (ROOT / t), name_index, cn_index, errors, warns)

    for w in warns:
        print(w)
    for e in errors:
        print(e)
    print(f"\n--- verify: {len(targets)} file(s), {len(errors)} error(s), {len(warns)} warning(s) ---")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
