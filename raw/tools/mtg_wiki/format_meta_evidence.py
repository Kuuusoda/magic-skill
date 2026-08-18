#!/usr/bin/env python3
"""Format-specific metagame evidence lookup for entity resolution.

This module is deliberately small and deterministic:
- It reads curated, reviewable evidence from raw/data/format_meta_evidence/*.json.
- It does not decide card legality or card text.
- It gives card_resolve.py a format/meta signal that is stronger than fuzzy
  card search but weaker than a future live data ingestion pipeline.
"""

from __future__ import annotations

import argparse
import json
from datetime import date, datetime
from pathlib import Path
from typing import Any

from utils import PROJECT_ROOT, normalize_name


META_EVIDENCE_DIR = PROJECT_ROOT / "raw" / "data" / "format_meta_evidence"
STALE_AFTER_DAYS = 180


def load_format_evidence(fmt: str) -> dict[str, Any]:
    path = META_EVIDENCE_DIR / f"{fmt}.json"
    if not path.exists():
        return {"format": fmt, "as_of": "", "sources": [], "entities": []}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {"format": fmt, "as_of": "", "sources": [], "entities": []}


def resolve_meta_evidence(query: str, fmt: str, intent: str = "", candidates: list[str] | None = None) -> dict[str, Any]:
    data = load_format_evidence(fmt)
    qnorm = normalize_name(query)
    candidate_norms = {normalize_name(c) for c in (candidates or []) if c}
    matches = []

    for entity in data.get("entities", []):
        match = match_entity(entity, qnorm, intent, candidate_norms)
        if match:
            matches.append(match)

    matches.sort(key=lambda m: (m["score"], len(m.get("evidence", []))), reverse=True)
    return {
        "query": query,
        "format": fmt,
        "intent": intent,
        "as_of": data.get("as_of", ""),
        "stale": is_stale(data.get("as_of", "")),
        "sources": data.get("sources", []),
        "evidence_found": bool(matches),
        "matches": matches,
    }


def match_entity(entity: dict[str, Any], qnorm: str, intent: str, candidate_norms: set[str]) -> dict[str, Any] | None:
    name = entity.get("name", "")
    entity_norm = normalize_name(name)
    aliases = [normalize_name(a) for a in entity.get("aliases", [])]
    intents = set(entity.get("intents", []))
    matched_by = []
    score = 0.0

    if qnorm and qnorm == entity_norm:
        matched_by.append("exact_meta_name")
        score += 90
    if qnorm and qnorm in aliases:
        matched_by.append("meta_alias")
        score += 120
    if entity_norm in candidate_norms:
        matched_by.append("candidate_name")
        score += 80
    if aliases and aliases_set_intersects(aliases, candidate_norms):
        matched_by.append("candidate_alias")
        score += 70

    if not matched_by:
        return None

    if intent and intent in intents:
        matched_by.append("intent_match")
        score += 10

    confidence = entity.get("confidence", "medium")
    if confidence == "high":
        score += 15
    elif confidence == "low":
        score -= 15

    evidence = entity.get("evidence", [])
    score += min(len(evidence), 3) * 5

    return {
        "name": name,
        "entity": entity.get("entity", "card"),
        "score": score,
        "matched_by": matched_by,
        "confidence": confidence,
        "observed_at": entity.get("observed_at", ""),
        "aliases": entity.get("aliases", []),
        "evidence": evidence,
    }


def aliases_set_intersects(aliases: list[str], candidate_norms: set[str]) -> bool:
    return bool(set(aliases) & candidate_norms)


def is_stale(as_of: str) -> bool:
    if not as_of:
        return True
    try:
        as_of_date = datetime.strptime(as_of, "%Y-%m-%d").date()
    except ValueError:
        return True
    return (date.today() - as_of_date).days > STALE_AFTER_DAYS


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--format", default="duel-commander", choices=["duel-commander", "cedh", "modern"])
    parser.add_argument("--intent", default="")
    parser.add_argument("--candidate", action="append", default=[], help="Known candidate name to check against meta evidence.")
    args = parser.parse_args(argv)
    result = resolve_meta_evidence(args.query, args.format, args.intent, args.candidate)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
