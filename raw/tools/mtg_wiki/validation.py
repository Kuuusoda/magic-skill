#!/usr/bin/env python3
"""
Hard-coded JSON validation for mtg-judge-zh skill outputs.

Validates agent outputs against schemas, checks evidence consistency,
verifies citation integrity, and validates ruling freshness.

No external dependencies — uses only Python standard library.

Usage:
  python3 validation.py --schema query-plan < query_plan.json
  python3 validation.py --schema card-info < card_info.json
  python3 validation.py --schema rule-info < rule_info.json
  python3 validation.py --schema analysis --evidence evidence.json < analysis.json
  python3 validation.py --schema verdict < verdict.json
  python3 validation.py --evidence-package evidence.json
  python3 validation.py --full-pipeline query.json cards.json rules.json analysis.json verdict.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Optional

# ── Schema definitions (hard-coded, synchronized with .claude/schemas/*.json) ──

QUERY_PLAN_SCHEMA = {
    "required": ["cards", "rule_keywords", "question_type", "needs_rulings", "needs_strategy"],
    "types": {
        "cards": list,
        "rule_keywords": list,
        "question_type": str,
        "needs_rulings": bool,
        "needs_strategy": bool,
    },
    "enums": {
        "question_type": ["interaction", "rule", "policy", "format"],
    },
    "item_types": {
        "cards": str,
        "rule_keywords": str,
    },
}

CARD_INFO_SCHEMA = {
    "required": ["input_name", "english_name", "oracle_text", "mana_cost", "type_line"],
    "types": {
        "input_name": str,
        "english_name": (str, type(None)),
        "scryfall_id": (str, type(None)),
        "oracle_text": (str, type(None)),
        "mana_cost": (str, type(None)),
        "type_line": (str, type(None)),
        "power_toughness": (str, type(None)),
        "error": (str, type(None)),
    },
}

RULE_MATCH_SCHEMA = {
    "required": ["rule_number", "rule_text", "source_file", "source_type"],
    "types": {
        "rule_number": str,
        "rule_text": str,
        "source_file": str,
        "source_type": str,
    },
    "enums": {
        "source_type": ["wiki_concept", "wiki_decision_tree", "wiki_framework", "cr_rule", "mtr_rule", "ipg_rule"],
    },
}

RULE_INFO_SCHEMA = {
    "required": ["keyword", "matches"],
    "types": {
        "keyword": str,
        "matches": list,
    },
}

ANALYSIS_SCHEMA = {
    "required": ["conclusion", "reasoning", "confidence", "cited_rules", "cited_cards"],
    "types": {
        "conclusion": str,
        "reasoning": str,
        "confidence": str,
        "cited_rules": list,
        "cited_cards": list,
        "assumptions": (list, type(None)),
        "needs_more_evidence": (dict, type(None)),
    },
    "enums": {
        "confidence": ["certain", "likely", "uncertain"],
    },
    "item_types": {
        "cited_rules": str,
        "cited_cards": str,
    },
}

ASSUMPTION_SCHEMA = {
    "required": ["assumption", "evidence_based"],
    "types": {
        "assumption": str,
        "evidence_based": bool,
        "note": (str, type(None)),
    },
}

NEEDS_MORE_EVIDENCE_SCHEMA = {
    "required": ["rules", "reason"],
    "types": {
        "rules": list,
        "reason": str,
    },
    "item_types": {
        "rules": str,
    },
}

VERDICT_SCHEMA = {
    "required": ["status", "card_check", "rule_check", "evidence_check", "citation_check", "notes"],
    "types": {
        "status": str,
        "card_check": str,
        "rule_check": str,
        "evidence_check": str,
        "citation_check": str,
        "notes": str,
    },
    "enums": {
        "status": ["PASS", "WARN", "BLOCK"],
        "card_check": ["PASS", "FAIL"],
        "rule_check": ["PASS", "FAIL"],
        "evidence_check": ["PASS", "WARN", "FAIL"],
        "citation_check": ["PASS", "FAIL"],
    },
}

# ── Validation result ──


class ValidationResult:
    """Collects validation errors."""

    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def add_error(self, msg: str) -> None:
        self.errors.append(msg)

    def add_warning(self, msg: str) -> None:
        self.warnings.append(msg)

    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def has_warnings(self) -> bool:
        return len(self.warnings) > 0

    def summary(self) -> str:
        lines = []
        if self.errors:
            lines.append(f"ERRORS ({len(self.errors)}):")
            for e in self.errors:
                lines.append(f"  [E] {e}")
        if self.warnings:
            lines.append(f"WARNINGS ({len(self.warnings)}):")
            for w in self.warnings:
                lines.append(f"  [W] {w}")
        if not lines:
            lines.append("VALIDATION PASSED")
        return "\n".join(lines)


# ── Generic schema validator ──


def _check_type(path: str, value: Any, expected: type | tuple[type, ...], result: ValidationResult) -> bool:
    """Check if value matches expected type(s)."""
    if isinstance(expected, tuple):
        if not isinstance(value, expected):
            type_names = " or ".join(t.__name__ for t in expected)
            result.add_error(f"{path}: expected {type_names}, got {type(value).__name__}")
            return False
    else:
        if not isinstance(value, expected):
            result.add_error(f"{path}: expected {expected.__name__}, got {type(value).__name__}")
            return False
    return True


def validate_object(
    obj: dict,
    schema: dict,
    result: ValidationResult,
    path: str = "root",
) -> None:
    """Validate a dict object against a schema definition."""
    if not isinstance(obj, dict):
        result.add_error(f"{path}: expected object, got {type(obj).__name__}")
        return

    # Check required fields
    for field in schema.get("required", []):
        if field not in obj:
            result.add_error(f"{path}: missing required field '{field}'")

    # Check types
    for field, expected_type in schema.get("types", {}).items():
        if field in obj:
            _check_type(f"{path}.{field}", obj[field], expected_type, result)

    # Check enums
    for field, allowed in schema.get("enums", {}).items():
        if field in obj and obj[field] not in allowed:
            result.add_error(
                f"{path}.{field}: invalid value '{obj[field]}', must be one of {allowed}"
            )

    # Check array item types
    for field, item_type in schema.get("item_types", {}).items():
        if field in obj and isinstance(obj[field], list):
            for i, item in enumerate(obj[field]):
                if not isinstance(item, item_type):
                    result.add_error(
                        f"{path}.{field}[{i}]: expected {item_type.__name__}, got {type(item).__name__}"
                    )


# ── Domain-specific validators ──


def validate_query_plan(data: dict, result: Optional[ValidationResult] = None) -> ValidationResult:
    """Validate a QueryPlan output."""
    result = result or ValidationResult()
    validate_object(data, QUERY_PLAN_SCHEMA, result)

    # Additional checks
    if "cards" in data and isinstance(data["cards"], list):
        if len(data["cards"]) == 0 and data.get("question_type") == "interaction":
            result.add_warning("interaction question has empty cards list")

    if "rule_keywords" in data and isinstance(data["rule_keywords"], list):
        for i, kw in enumerate(data["rule_keywords"]):
            if not isinstance(kw, str) or not kw.strip():
                result.add_error(f"rule_keywords[{i}]: empty or invalid keyword")

    return result


def validate_card_info(data: dict, result: Optional[ValidationResult] = None) -> ValidationResult:
    """Validate a CardInfo output."""
    result = result or ValidationResult()
    validate_object(data, CARD_INFO_SCHEMA, result)

    # Guard against non-dict input
    if not isinstance(data, dict):
        return result

    # Content checks (hard checks from SKILL.md)
    if data.get("error") is None:
        if not data.get("oracle_text"):
            result.add_error("oracle_text is empty or null for a resolved card")
        if not data.get("scryfall_id"):
            result.add_error("scryfall_id is empty or null for a resolved card")
        if not data.get("english_name"):
            result.add_error("english_name is empty or null for a resolved card")
        if not data.get("type_line"):
            result.add_error("type_line is empty or null for a resolved card")
    else:
        # If error is present, warn about missing fields but don't error
        for field in ["oracle_text", "scryfall_id", "english_name", "type_line"]:
            if data.get(field):
                result.add_warning(f"card has error='{data['error']}' but {field} is not empty")

    return result


def validate_rule_info(data: dict, result: Optional[ValidationResult] = None) -> ValidationResult:
    """Validate a RuleInfo output."""
    result = result or ValidationResult()
    validate_object(data, RULE_INFO_SCHEMA, result)

    matches = data.get("matches", [])
    if not isinstance(matches, list):
        return result

    for i, match in enumerate(matches):
        match_result = ValidationResult()
        validate_object(match, RULE_MATCH_SCHEMA, match_result, path=f"matches[{i}]")
        result.errors.extend(match_result.errors)
        result.warnings.extend(match_result.warnings)

        # Content checks from SKILL.md
        if isinstance(match, dict):
            source_type = match.get("source_type", "")
            source_file = match.get("source_file", "")

            # Note: enum validation in validate_object already catches invalid source_type
            # We only add the cr_rule source_file check here
            if source_type == "cr_rule" and not source_file.startswith("raw/"):
                result.add_error(
                    f"matches[{i}]: cr_rule must have source_file starting with 'raw/', got '{source_file}'"
                )

    return result


def validate_ruling_info(data: dict, result: Optional[ValidationResult] = None) -> ValidationResult:
    """Validate a RulingInfo output."""
    result = result or ValidationResult()

    if not isinstance(data, dict):
        result.add_error("root: expected object")
        return result

    if "scryfall_id" not in data:
        result.add_error("root: missing 'scryfall_id'")

    rulings = data.get("rulings", [])
    if not isinstance(rulings, list):
        result.add_error("rulings: expected array")
        return result

    for i, r in enumerate(rulings):
        if not isinstance(r, dict):
            result.add_error(f"rulings[{i}]: expected object")
            continue
        if "published_at" not in r:
            result.add_error(f"rulings[{i}]: missing 'published_at'")
        if "comment" not in r:
            result.add_error(f"rulings[{i}]: missing 'comment'")
        # Check date format
        date = r.get("published_at", "")
        if date and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(date)):
            result.add_warning(f"rulings[{i}]: unusual date format '{date}'")

    return result


def validate_analysis(
    data: dict,
    evidence: Optional[dict] = None,
    result: Optional[ValidationResult] = None,
) -> ValidationResult:
    """Validate an Analysis output. Optionally checks citations against evidence."""
    result = result or ValidationResult()
    validate_object(data, ANALYSIS_SCHEMA, result)

    # Validate assumptions if present
    assumptions = data.get("assumptions")
    if isinstance(assumptions, list):
        for i, asm in enumerate(assumptions):
            if isinstance(asm, dict):
                asm_result = ValidationResult()
                validate_object(asm, ASSUMPTION_SCHEMA, asm_result, path=f"assumptions[{i}]")
                result.errors.extend(asm_result.errors)
                result.warnings.extend(asm_result.warnings)

    # Validate needs_more_evidence if present
    nme = data.get("needs_more_evidence")
    if isinstance(nme, dict):
        nme_result = ValidationResult()
        validate_object(nme, NEEDS_MORE_EVIDENCE_SCHEMA, nme_result, path="needs_more_evidence")
        result.errors.extend(nme_result.errors)
        result.warnings.extend(nme_result.warnings)

    # Citation checks (if evidence is provided)
    if evidence:
        # Collect available rules
        available_rules: set[str] = set()
        for rule_info in evidence.get("rules", []):
            if isinstance(rule_info, dict):
                for match in rule_info.get("matches", []):
                    if isinstance(match, dict):
                        available_rules.add(match.get("rule_number", ""))

        # Collect available cards
        available_cards: set[str] = set()
        for card in evidence.get("cards", []):
            if isinstance(card, dict):
                available_cards.add(card.get("english_name", ""))

        # Check cited_rules
        for rule_num in data.get("cited_rules", []):
            if rule_num and rule_num not in available_rules:
                result.add_error(
                    f"cited_rules: '{rule_num}' not found in evidence.rules"
                )

        # Check cited_cards
        for card_name in data.get("cited_cards", []):
            if card_name and card_name not in available_cards:
                result.add_error(
                    f"cited_cards: '{card_name}' not found in evidence.cards"
                )

    # Soft check: unverified assumptions with confidence=certain
    confidence = data.get("confidence", "")
    if confidence == "certain" and isinstance(assumptions, list):
        for asm in assumptions:
            if isinstance(asm, dict) and asm.get("evidence_based") is False:
                result.add_warning(
                    f"confidence='certain' but assumption '{asm.get('assumption', '')}' is not evidence-based"
                )

    return result


def validate_verdict(data: dict, result: Optional[ValidationResult] = None) -> ValidationResult:
    """Validate a Verdict output."""
    result = result or ValidationResult()
    validate_object(data, VERDICT_SCHEMA, result)

    # Consistency checks
    status = data.get("status", "")
    checks = ["card_check", "rule_check", "citation_check"]
    for check in checks:
        if data.get(check) == "FAIL" and status != "BLOCK":
            result.add_warning(
                f"{check}=FAIL but status={status} (should be BLOCK)"
            )

    evidence_check = data.get("evidence_check", "")
    if evidence_check == "FAIL" and status not in ("BLOCK", "WARN"):
        result.add_warning(
            f"evidence_check=FAIL but status={status} (should be BLOCK or WARN)"
        )

    return result


# ── Evidence package validator ──


def validate_evidence_package(
    evidence: dict,
    result: Optional[ValidationResult] = None,
) -> ValidationResult:
    """Validate a complete evidence package (cards + rules + rulings)."""
    result = result or ValidationResult()

    if not isinstance(evidence, dict):
        result.add_error("evidence: expected object")
        return result

    # Validate cards
    cards = evidence.get("cards", [])
    if not isinstance(cards, list):
        result.add_error("evidence.cards: expected array")
    else:
        for i, card in enumerate(cards):
            if isinstance(card, dict):
                card_result = validate_card_info(card)
                for e in card_result.errors:
                    result.add_error(f"evidence.cards[{i}]: {e}")
                for w in card_result.warnings:
                    result.add_warning(f"evidence.cards[{i}]: {w}")

    # Validate rules
    rules = evidence.get("rules", [])
    if not isinstance(rules, list):
        result.add_error("evidence.rules: expected array")
    else:
        for i, rule in enumerate(rules):
            if isinstance(rule, dict):
                rule_result = validate_rule_info(rule)
                for e in rule_result.errors:
                    result.add_error(f"evidence.rules[{i}]: {e}")
                for w in rule_result.warnings:
                    result.add_warning(f"evidence.rules[{i}]: {w}")

    # Validate rulings
    rulings = evidence.get("rulings", [])
    if not isinstance(rulings, list):
        result.add_error("evidence.rulings: expected array")
    else:
        for i, ruling in enumerate(rulings):
            if isinstance(ruling, dict):
                ruling_result = validate_ruling_info(ruling)
                for e in ruling_result.errors:
                    result.add_error(f"evidence.rulings[{i}]: {e}")
                for w in ruling_result.warnings:
                    result.add_warning(f"evidence.rulings[{i}]: {w}")

    # Cross-reference: check that every card's scryfall_id in rulings matches a card
    card_ids = set()
    for card in cards:
        if isinstance(card, dict) and card.get("scryfall_id"):
            card_ids.add(card["scryfall_id"])

    for ruling in rulings:
        if isinstance(ruling, dict):
            rid = ruling.get("scryfall_id", "")
            if rid and rid not in card_ids:
                result.add_warning(
                    f"ruling scryfall_id '{rid}' does not match any card in evidence.cards"
                )

    return result


# ── Full pipeline validator ──


def validate_full_pipeline(
    query_plan: dict,
    cards: list[dict],
    rules: list[dict],
    analysis: dict,
    verdict: dict,
    rulings: Optional[list[dict]] = None,
) -> ValidationResult:
    """Run the complete validation pipeline across all steps."""
    result = ValidationResult()

    # Step 1: QueryPlan
    qp_result = validate_query_plan(query_plan)
    result.errors.extend(f"[QueryPlan] {e}" for e in qp_result.errors)
    result.warnings.extend(f"[QueryPlan] {w}" for w in qp_result.warnings)

    # Step 2: Evidence package
    evidence = {
        "cards": cards,
        "rules": rules,
        "rulings": rulings or [],
    }
    ev_result = validate_evidence_package(evidence)
    result.errors.extend(f"[Evidence] {e}" for e in ev_result.errors)
    result.warnings.extend(f"[Evidence] {w}" for w in ev_result.warnings)

    # Step 3: Analysis (with citation check)
    an_result = validate_analysis(analysis, evidence=evidence)
    result.errors.extend(f"[Analysis] {e}" for e in an_result.errors)
    result.warnings.extend(f"[Analysis] {w}" for w in an_result.warnings)

    # Step 4: Verdict
    vd_result = validate_verdict(verdict)
    result.errors.extend(f"[Verdict] {e}" for e in vd_result.errors)
    result.warnings.extend(f"[Verdict] {w}" for w in vd_result.warnings)

    # Pipeline consistency checks
    # QueryPlan.cards vs evidence.cards: allow duplicates in query_plan (e.g. same card mentioned twice)
    qp_cards = query_plan.get("cards", [])
    unique_qp_cards = len(set(qp_cards)) if qp_cards else 0
    if unique_qp_cards != len(cards):
        result.add_warning(
            f"[Pipeline] QueryPlan has {unique_qp_cards} unique cards but evidence has {len(cards)}"
        )

    # QueryPlan.rule_keywords vs evidence.rules: rules may be fewer (some keywords yield nothing)
    # but should not be more (can't have more rule results than keywords searched)
    qp_keywords = query_plan.get("rule_keywords", [])
    if len(rules) > len(qp_keywords):
        result.add_warning(
            f"[Pipeline] Evidence has {len(rules)} rules but QueryPlan only had {len(qp_keywords)} keywords"
        )

    # Verdict status should align with actual errors found
    if result.errors and verdict.get("status") == "PASS":
        result.add_warning(
            f"[Pipeline] Validation found {len(result.errors)} errors but verdict.status=PASS"
        )

    return result


# ── CLI ──


def load_json(path_or_stdin: str) -> Any:
    """Load JSON from file path or stdin (if path is '-')."""
    if path_or_stdin == "-":
        return json.load(sys.stdin)
    with open(path_or_stdin, "r", encoding="utf-8") as f:
        return json.load(f)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Validate mtg-judge-zh agent outputs")
    parser.add_argument(
        "--schema",
        choices=["query-plan", "card-info", "rule-info", "analysis", "verdict", "ruling-info"],
        help="Schema to validate against",
    )
    parser.add_argument(
        "--evidence",
        metavar="PATH",
        help="Evidence package JSON for citation validation (used with --schema analysis)",
    )
    parser.add_argument(
        "--evidence-package",
        metavar="PATH",
        help="Validate a complete evidence package",
    )
    parser.add_argument(
        "--full-pipeline",
        nargs=5,
        metavar="PATH",
        help="Run full pipeline validation: query_plan cards rules analysis verdict",
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="-",
        help="Input JSON file (default: stdin)",
    )
    args = parser.parse_args(argv)

    result = ValidationResult()

    if args.full_pipeline:
        try:
            query_plan = load_json(args.full_pipeline[0])
            cards = load_json(args.full_pipeline[1])
            rules = load_json(args.full_pipeline[2])
            analysis = load_json(args.full_pipeline[3])
            verdict = load_json(args.full_pipeline[4])
            # Ensure cards and rules are lists
            if isinstance(cards, dict):
                cards = [cards]
            if isinstance(rules, dict):
                rules = [rules]
            result = validate_full_pipeline(query_plan, cards, rules, analysis, verdict)
        except Exception as e:
            result.add_error(f"Failed to load pipeline inputs: {e}")

    elif args.evidence_package:
        try:
            evidence = load_json(args.evidence_package)
            result = validate_evidence_package(evidence)
        except Exception as e:
            result.add_error(f"Failed to load evidence package: {e}")

    elif args.schema:
        try:
            data = load_json(args.input)
        except json.JSONDecodeError as e:
            print(f"JSON parse error: {e}", file=sys.stderr)
            return 2
        except Exception as e:
            print(f"Failed to load input: {e}", file=sys.stderr)
            return 2

        evidence = None
        if args.evidence and args.schema == "analysis":
            try:
                evidence = load_json(args.evidence)
            except Exception as e:
                result.add_warning(f"Failed to load evidence for citation check: {e}")

        validators = {
            "query-plan": validate_query_plan,
            "card-info": validate_card_info,
            "rule-info": validate_rule_info,
            "analysis": lambda d: validate_analysis(d, evidence=evidence),
            "verdict": validate_verdict,
            "ruling-info": validate_ruling_info,
        }
        result = validators[args.schema](data)

    else:
        parser.print_help()
        return 1

    print(result.summary())
    return 0 if result.is_valid() else 1


if __name__ == "__main__":
    sys.exit(main())
