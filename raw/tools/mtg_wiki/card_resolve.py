#!/usr/bin/env python3
"""
Resolve ambiguous MTG card/deck/archetype shorthand into ranked candidates.

This is intentionally different from card_search.py:
- card_search.py returns details for one assumed card.
- card_resolve.py returns candidates, scores, reasons, warnings, and whether
  clarification is needed before a skill answers.

Usage:
  python3 raw/tools/mtg_wiki/card_resolve.py "kess" --format duel-commander --intent commander
  python3 raw/tools/mtg_wiki/card_resolve.py "blue farm" --format cedh --intent deck
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import card_search
from utils import PROJECT_ROOT, normalize_name, mtgch_get, scryfall_get


SHORT_QUERY_LEN = 4

FORMAT_DIRS = {
    "duel-commander": [
        PROJECT_ROOT / "wiki" / "branches" / "strategy" / "duel-commander",
        PROJECT_ROOT / "wiki" / "concepts" / "duel-commander.md",
    ],
    "cedh": [
        PROJECT_ROOT / "wiki" / "branches" / "strategy" / "cedh",
        PROJECT_ROOT / "wiki" / "concepts",
        PROJECT_ROOT / "wiki" / "synthesis",
        PROJECT_ROOT / "output",
    ],
    "modern": [
        PROJECT_ROOT / "wiki" / "branches" / "strategy",
    ],
    "judge": [
        PROJECT_ROOT / "wiki" / "concepts",
        PROJECT_ROOT / "wiki" / "synthesis",
        PROJECT_ROOT / "wiki" / "branches" / "referee",
    ],
}

BUILTIN_ALIASES: dict[str, dict[str, Any]] = {
    # Duel Commander / commander shorthand observed in local tests.
    "2099": {"name": "Spider-Man 2099, Miguel O'Hara", "formats": ["duel-commander"], "intents": ["commander", "deck", "card"]},
    "spider99": {"name": "Spider-Man 2099, Miguel O'Hara", "formats": ["duel-commander"], "intents": ["commander", "deck", "card"]},
    "phelia": {"name": "Phelia, Exuberant Shepherd", "formats": ["duel-commander", "modern"], "intents": ["commander", "deck", "card"]},
    "kess": {"name": "Kess, Dissident Mage", "formats": ["duel-commander", "cedh"], "intents": ["commander", "deck", "card"]},
    "niv": {"name": "Niv-Mizzet, Parun", "formats": ["duel-commander"], "intents": ["commander", "deck", "card"]},
    "tivit": {"name": "Tivit, Seller of Secrets", "formats": ["cedh", "duel-commander"], "intents": ["commander", "deck", "card"]},
    "squee": {"name": "Slimefoot and Squee", "formats": ["duel-commander", "commander"], "intents": ["commander", "deck"]},
    "slimefoot": {"name": "Slimefoot and Squee", "formats": ["duel-commander", "commander"], "intents": ["commander", "deck"]},
    # cEDH deck/combo shorthand.
    "blue farm": {"entity": "deck", "name": "Blue Farm (Tymna the Weaver / Kraum, Ludevic's Opus)", "formats": ["cedh"], "intents": ["deck"]},
    "tymna/kraum": {"entity": "deck", "name": "Blue Farm (Tymna the Weaver / Kraum, Ludevic's Opus)", "formats": ["cedh"], "intents": ["deck", "commander"]},
    "tnt": {"entity": "deck", "name": "Tymna the Weaver / Thrasios, Triton Hero", "formats": ["cedh"], "intents": ["deck", "commander"]},
    "rogsi": {"entity": "deck", "name": "Rograkh, Son of Rohgahh / Silas Renn, Seeker Adept", "formats": ["cedh"], "intents": ["deck", "commander"]},
    "thoracle": {"entity": "combo", "name": "Thassa's Oracle", "formats": ["cedh", "judge"], "intents": ["combo", "card", "interaction"]},
    "oracle": {"entity": "combo", "name": "Thassa's Oracle", "formats": ["cedh", "judge"], "intents": ["combo", "card", "interaction"]},
    "consultation": {"name": "Demonic Consultation", "formats": ["cedh", "judge"], "intents": ["combo", "card", "interaction"]},
    "demonic consultation": {"name": "Demonic Consultation", "formats": ["cedh", "judge"], "intents": ["combo", "card", "interaction"]},
    "breach": {"entity": "combo", "name": "Underworld Breach", "formats": ["cedh", "judge", "modern"], "intents": ["combo", "card", "interaction"]},
    "led": {"name": "Lion's Eye Diamond", "formats": ["cedh", "judge"], "intents": ["combo", "card", "interaction"]},
    # Modern archetype shorthand.
    "frog": {"entity": "deck", "name": "Dimir Frog", "formats": ["modern"], "intents": ["deck", "archetype"]},
    "energy": {"entity": "deck", "name": "Boros Energy", "formats": ["modern"], "intents": ["deck", "archetype"]},
    "belcher": {"entity": "deck", "name": "Tameshi Belcher", "formats": ["modern"], "intents": ["deck", "archetype"]},
    "amulet": {"entity": "deck", "name": "Amulet Titan", "formats": ["modern"], "intents": ["deck", "archetype"]},
}


@dataclass
class Candidate:
    name: str
    entity: str = "card"
    score: float = 0.0
    reasons: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    details: dict[str, Any] | None = None
    wiki_hits: list[str] = field(default_factory=list)

    def add(self, points: float, reason: str):
        self.score += points
        if reason not in self.reasons:
            self.reasons.append(reason)

    def warn(self, warning: str):
        if warning not in self.warnings:
            self.warnings.append(warning)


def merge_candidate(candidates: dict[str, Candidate], name: str, entity: str = "card") -> Candidate:
    key = normalize_name(name)
    if key not in candidates:
        candidates[key] = Candidate(name=name, entity=entity)
    elif entity != "card" and candidates[key].entity == "card":
        candidates[key].entity = entity
    return candidates[key]


def load_external_aliases() -> dict[str, dict[str, Any]]:
    """Load optional format alias JSON files. Missing files are fine."""
    aliases = dict(BUILTIN_ALIASES)
    for path in [
        PROJECT_ROOT / "raw" / "data" / "format_aliases" / "duel-commander.json",
        PROJECT_ROOT / "raw" / "data" / "format_aliases" / "cedh.json",
        PROJECT_ROOT / "raw" / "data" / "format_aliases" / "modern.json",
    ]:
        if not path.exists():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for alias, value in data.get("aliases", data).items():
            if isinstance(value, str):
                aliases[normalize_name(alias)] = {"name": value}
            elif isinstance(value, dict):
                aliases[normalize_name(alias)] = value
    return {normalize_name(k): v for k, v in aliases.items()}


def alias_candidates(query: str, fmt: str, intent: str, candidates: dict[str, Candidate]):
    aliases = load_external_aliases()
    norm = normalize_name(query)
    info = aliases.get(norm)
    if not info:
        contained_alias_candidates(norm, aliases, fmt, intent, candidates)
        return
    add_alias_candidate(info, candidates, fmt, intent, "exact_alias", 100)


def contained_alias_candidates(norm_query: str, aliases: dict[str, dict[str, Any]], fmt: str, intent: str, candidates: dict[str, Candidate]):
    """Find aliases inside compound interaction queries like 'breach LED'."""
    if len(norm_query) < 5:
        return
    for alias_norm, info in aliases.items():
        if len(alias_norm) < 3:
            continue
        if alias_norm in norm_query:
            add_alias_candidate(info, candidates, fmt, intent, "contained_alias", 70)


def add_alias_candidate(info: dict[str, Any], candidates: dict[str, Candidate], fmt: str, intent: str, reason: str, points: float):
    name = info.get("preferred") or info.get("name")
    if not name:
        return
    cand = merge_candidate(candidates, name, info.get("entity", "card"))
    cand.add(points, reason)
    if fmt in info.get("formats", []) or not info.get("formats"):
        cand.add(15, "format_alias_match")
    if intent in info.get("intents", []) or not info.get("intents"):
        cand.add(10, "intent_alias_match")


def paths_for_format(fmt: str) -> list[Path]:
    return FORMAT_DIRS.get(fmt, FORMAT_DIRS["judge"])


def wiki_context_candidates(query: str, fmt: str, intent: str, candidates: dict[str, Candidate], limit: int = 20):
    norm_query = normalize_name(query)
    if len(norm_query) < 3:
        return
    seen_files = 0
    for root in paths_for_format(fmt):
        if not root.exists():
            continue
        files = [root] if root.is_file() else list(root.rglob("*.md"))
        for path in files:
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            if norm_query not in normalize_name(text):
                continue
            seen_files += 1
            rel = path.relative_to(PROJECT_ROOT).as_posix()
            # Extract likely English card/deck names around query mentions.
            names = extract_names_from_text(text, query)
            if not names:
                title = extract_title(text) or path.stem.replace("-", " ").title()
                names = [title]
            for name in names[:6]:
                cand = merge_candidate(candidates, name, infer_entity_from_path(path, fmt, intent))
                cand.add(35 if "commander:" in text[:1000] else 18, "wiki_context_hit")
                if rel not in cand.wiki_hits:
                    cand.wiki_hits.append(rel)
            if seen_files >= limit:
                return


def extract_title(text: str) -> str | None:
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else None


def extract_names_from_text(text: str, query: str) -> list[str]:
    """Heuristic extraction of English names from frontmatter/body lines near query."""
    names: list[str] = []
    qnorm = normalize_name(query)
    for line in text.splitlines():
        if qnorm not in normalize_name(line):
            continue
        # Bold markdown names.
        for m in re.findall(r"\*\*([^*\n]+)\*\*", line):
            if looks_like_name(m):
                names.append(clean_display_name(m))
        # Wiki link display/path.
        for m in re.findall(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", line):
            label = m[1] or m[0]
            if looks_like_name(label):
                names.append(clean_display_name(label))
        # Plain English proper-name spans.
        for m in re.findall(r"\b([A-Z][A-Za-z'’.-]+(?:,? [A-Z][A-Za-z'’.-]+){0,5})\b", line):
            if looks_like_name(m):
                names.append(clean_display_name(m))
    # Stable de-dupe.
    out = []
    seen = set()
    for name in names:
        key = normalize_name(name)
        if key and key not in seen:
            seen.add(key)
            out.append(name)
    return out


def clean_display_name(name: str) -> str:
    return re.sub(r"\s+", " ", name).strip(" -—:：，,。")


def looks_like_name(value: str) -> bool:
    value = clean_display_name(value)
    if not value or len(value) < 3:
        return False
    if value.lower() in {"duel commander", "magic", "modern", "cedh"}:
        return False
    return bool(re.search(r"[A-Za-z]", value))


def infer_entity_from_path(path: Path, fmt: str, intent: str) -> str:
    p = path.as_posix()
    if "decks" in p or intent in {"deck", "archetype"}:
        return "deck"
    if "combos" in p or intent == "combo":
        return "combo"
    return "card"


def api_candidates(query: str, candidates: dict[str, Candidate]):
    """Add mtgch and Scryfall search candidates without trusting first result."""
    try:
        r = mtgch_get("/result", {"q": query, "priority_chinese": "true"})
        for item in r.get("items", [])[:8]:
            name = item.get("name") or item.get("face_name")
            if not name:
                continue
            cand = merge_candidate(candidates, name)
            cand.add(12, "mtgch_candidate")
            cand.details = cand.details or normalize_mtgch(item)
    except Exception:
        pass

    try:
        r = scryfall_get("/cards/search", {"q": query, "unique": "cards"})
        for item in r.get("data", [])[:8]:
            name = item.get("name")
            if not name:
                continue
            cand = merge_candidate(candidates, name)
            cand.add(10, "scryfall_candidate")
            cand.details = cand.details or normalize_scryfall(item)
    except Exception:
        pass

    # Fuzzy named is often useful, but low authority for short/ambiguous terms.
    try:
        fuzzy = card_search.scryfall_fuzzy(query)
        if fuzzy:
            cand = merge_candidate(candidates, fuzzy["name"])
            cand.add(8, "scryfall_fuzzy")
            cand.details = cand.details or fuzzy
    except Exception:
        pass


def normalize_mtgch(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "name": item.get("name"),
        "type_line": item.get("type_line"),
        "oracle_text": item.get("oracle_text"),
        "mana_cost": item.get("mana_cost"),
        "color_identity": item.get("color_identity", []),
        "legalities": item.get("legalities", {}),
        "source": "mtgch",
    }


def normalize_scryfall(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "name": item.get("name"),
        "type_line": item.get("type_line"),
        "oracle_text": item.get("oracle_text"),
        "mana_cost": item.get("mana_cost"),
        "color_identity": item.get("color_identity", []),
        "legalities": item.get("legalities", {}),
        "source": "scryfall",
    }


def enrich_and_score(candidates: dict[str, Candidate], query: str, fmt: str, intent: str, allow_api: bool = True):
    qnorm = normalize_name(query)
    short_query = len(qnorm) <= SHORT_QUERY_LEN
    for cand in candidates.values():
        if allow_api and cand.details is None and cand.entity == "card":
            try:
                cand.details = card_search.search(cand.name)
            except Exception:
                cand.details = None
        details = cand.details or {}
        type_line = details.get("type_line", "") or ""
        legalities = details.get("legalities", {}) or {}
        cnorm = normalize_name(cand.name)

        if cnorm == qnorm:
            cand.add(45, "exact_name")
        elif cnorm.startswith(qnorm) and len(qnorm) >= 3:
            cand.add(20, "name_prefix")
        elif qnorm and qnorm in cnorm:
            cand.add(14, "name_contains")

        if is_legendary_candidate(type_line):
            cand.add(30 if intent in {"commander", "deck"} else 8, "legendary_candidate")
        elif intent == "commander" and cand.entity == "card":
            cand.add(-35, "not_likely_commander")
            cand.warn("not_legendary_for_commander_intent")

        if fmt == "duel-commander":
            if legalities.get("duel") == "legal":
                cand.add(20, "duel_legal")
            elif legalities:
                cand.add(-30, "not_duel_legal_or_unknown")
                cand.warn("duel_legality_not_confirmed")
        elif fmt == "cedh":
            if legalities.get("commander") == "legal":
                cand.add(15, "commander_legal")
        elif fmt == "modern":
            if cand.entity == "deck":
                cand.add(35, "modern_archetype_context")
            elif legalities.get("modern") == "legal":
                cand.add(8, "modern_legal_card")

        if cand.entity in {"deck", "combo", "archetype"} and intent in {"deck", "combo", "archetype"}:
            cand.add(40, "entity_matches_intent")

        if short_query and "exact_alias" not in cand.reasons:
            cand.add(-10, "short_query_noise")
            cand.warn("short_query_without_alias")


def is_legendary_candidate(type_line: str) -> bool:
    return "Legendary" in type_line and ("Creature" in type_line or "Planeswalker" in type_line)


def resolve(query: str, fmt: str, intent: str, limit: int = 5, allow_api: bool = True) -> dict[str, Any]:
    candidates: dict[str, Candidate] = {}
    alias_candidates(query, fmt, intent, candidates)
    wiki_context_candidates(query, fmt, intent, candidates)
    if allow_api and should_expand_with_api(candidates):
        api_candidates(query, candidates)
    enrich_and_score(candidates, query, fmt, intent, allow_api=allow_api)

    ranked = sorted(candidates.values(), key=lambda c: c.score, reverse=True)
    top = ranked[:limit]
    components = [c.name for c in top if ("exact_alias" in c.reasons or "contained_alias" in c.reasons)]
    if intent == "interaction" and len(components) >= 2:
        selected = " + ".join(components)
    else:
        selected = top[0].name if top else None
    needs_clarification = True
    if top:
        if intent == "interaction" and len(components) >= 2:
            needs_clarification = False
        if top[0].score >= 75 and (len(top) == 1 or top[0].score - top[1].score >= 15):
            needs_clarification = False
        # Deck/archetype aliases are often exact enough.
        if "exact_alias" in top[0].reasons and top[0].score >= 80:
            needs_clarification = False

    return {
        "query": query,
        "format": fmt,
        "intent": intent,
        "selected": selected,
        "components": components if components else [],
        "needs_clarification": needs_clarification,
        "candidates": [candidate_to_dict(c) for c in top],
    }


def should_expand_with_api(candidates: dict[str, Candidate]) -> bool:
    """Avoid slow/noisy API expansion when alias/wiki context is already decisive."""
    if not candidates:
        return True
    best = max(candidates.values(), key=lambda c: c.score)
    if "exact_alias" in best.reasons and best.score >= 100:
        return False
    if best.entity in {"deck", "combo", "archetype"} and best.score >= 55:
        return False
    return True


def candidate_to_dict(cand: Candidate) -> dict[str, Any]:
    out = {
        "name": cand.name,
        "entity": cand.entity,
        "score": round(cand.score, 2),
        "reasons": cand.reasons,
        "warnings": cand.warnings,
    }
    if cand.wiki_hits:
        out["wiki_hits"] = cand.wiki_hits[:5]
    if cand.details:
        out["type_line"] = cand.details.get("type_line")
        out["legalities"] = {
            k: v for k, v in (cand.details.get("legalities") or {}).items()
            if k in {"duel", "commander", "modern", "legacy", "vintage"}
        }
        out["source"] = cand.details.get("source")
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--format", default="judge", choices=["judge", "cedh", "duel-commander", "modern"])
    parser.add_argument("--intent", default="card")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--no-api", action="store_true", help="Do not call external APIs; use aliases/wiki context only.")
    args = parser.parse_args(argv)
    result = resolve(args.query, args.format, args.intent, args.limit, allow_api=not args.no_api)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
