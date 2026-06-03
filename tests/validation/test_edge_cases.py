#!/usr/bin/env python3
"""
Edge-case test suite for mtg-judge-zh validation.py

Tests robustness against malformed inputs, missing fields, type errors,
invalid enums, empty values, cross-reference failures, and boundary conditions.

Run: python3 -m pytest tests/validation/test_edge_cases.py -v
     or: python3 tests/validation/test_edge_cases.py
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

# Add the tools directory to path
sys.path.insert(
    0,
    str(
        Path(__file__).parent.parent.parent
        / "raw"
        / "tools"
        / "mtg_wiki"
    ),
)

from validation import (
    validate_analysis,
    validate_card_info,
    validate_evidence_package,
    validate_query_plan,
    validate_rule_info,
    validate_verdict,
    ValidationResult,
)


# ──────────────────────────────────────────────────────────────
# Helper utilities
# ──────────────────────────────────────────────────────────────


def v(result: ValidationResult) -> tuple[list[str], list[str]]:
    """Unpack errors and warnings from a ValidationResult."""
    return result.errors, result.warnings


# ═══════════════════════════════════════════════════════════════
# 1. QueryPlan edge cases
# ═══════════════════════════════════════════════════════════════


class TestQueryPlanEdgeCases(unittest.TestCase):
    """Edge cases for QueryPlan validation."""

    def test_valid_minimal(self):
        data = {
            "cards": ["闪电击"],
            "rule_keywords": ["damage"],
            "question_type": "rule",
            "needs_rulings": False,
            "needs_strategy": False,
        }
        errors, warnings = v(validate_query_plan(data))
        self.assertEqual(len(errors), 0, f"Unexpected errors: {errors}")

    def test_missing_cards(self):
        data = {
            "rule_keywords": ["damage"],
            "question_type": "rule",
            "needs_rulings": False,
            "needs_strategy": False,
        }
        errors, _ = v(validate_query_plan(data))
        self.assertTrue(any("cards" in e for e in errors))

    def test_missing_question_type(self):
        data = {
            "cards": ["闪电击"],
            "rule_keywords": ["damage"],
            "needs_rulings": False,
            "needs_strategy": False,
        }
        errors, _ = v(validate_query_plan(data))
        self.assertTrue(any("question_type" in e for e in errors))

    def test_invalid_question_type(self):
        data = {
            "cards": ["闪电击"],
            "rule_keywords": ["damage"],
            "question_type": "invalid_type",
            "needs_rulings": False,
            "needs_strategy": False,
        }
        errors, _ = v(validate_query_plan(data))
        self.assertTrue(any("invalid value" in e for e in errors))

    def test_cards_is_string_not_array(self):
        data = {
            "cards": "闪电击",
            "rule_keywords": ["damage"],
            "question_type": "rule",
            "needs_rulings": False,
            "needs_strategy": False,
        }
        errors, _ = v(validate_query_plan(data))
        self.assertTrue(any("cards" in e and "list" in e for e in errors))

    def test_needs_rulings_is_string(self):
        data = {
            "cards": ["闪电击"],
            "rule_keywords": ["damage"],
            "question_type": "rule",
            "needs_rulings": "false",
            "needs_strategy": False,
        }
        errors, _ = v(validate_query_plan(data))
        self.assertTrue(any("needs_rulings" in e for e in errors))

    def test_empty_cards_for_interaction(self):
        data = {
            "cards": [],
            "rule_keywords": ["damage"],
            "question_type": "interaction",
            "needs_rulings": False,
            "needs_strategy": False,
        }
        errors, warnings = v(validate_query_plan(data))
        self.assertEqual(len(errors), 0)
        self.assertTrue(any("empty cards" in w.lower() for w in warnings))

    def test_rule_keywords_contains_empty_string(self):
        data = {
            "cards": ["闪电击"],
            "rule_keywords": ["damage", ""],
            "question_type": "rule",
            "needs_rulings": False,
            "needs_strategy": False,
        }
        errors, _ = v(validate_query_plan(data))
        self.assertTrue(any("empty" in e for e in errors))

    def test_empty_object(self):
        errors, _ = v(validate_query_plan({}))
        self.assertGreater(len(errors), 0)


# ═══════════════════════════════════════════════════════════════
# 2. CardInfo edge cases
# ═══════════════════════════════════════════════════════════════


class TestCardInfoEdgeCases(unittest.TestCase):
    """Edge cases for CardInfo validation."""

    def test_valid_card(self):
        data = {
            "input_name": "闪电击",
            "english_name": "Lightning Bolt",
            "scryfall_id": "abc-123",
            "oracle_text": "Deals 3 damage.",
            "mana_cost": "{R}",
            "type_line": "Instant",
            "power_toughness": None,
            "error": None,
        }
        errors, _ = v(validate_card_info(data))
        self.assertEqual(len(errors), 0, f"Unexpected errors: {errors}")

    def test_missing_oracle_text_with_error(self):
        """If error is set, missing oracle_text should NOT error."""
        data = {
            "input_name": "未知牌",
            "english_name": None,
            "scryfall_id": None,
            "oracle_text": None,
            "mana_cost": None,
            "type_line": None,
            "error": "Card not found",
        }
        errors, _ = v(validate_card_info(data))
        self.assertEqual(len(errors), 0, f"Should not error when error field is set: {errors}")

    def test_missing_oracle_text_without_error(self):
        """If error is NOT set, missing oracle_text MUST error."""
        data = {
            "input_name": "闪电击",
            "english_name": "Lightning Bolt",
            "scryfall_id": "abc-123",
            "oracle_text": None,
            "mana_cost": "{R}",
            "type_line": "Instant",
            "error": None,
        }
        errors, _ = v(validate_card_info(data))
        self.assertTrue(any("oracle_text" in e for e in errors))

    def test_empty_oracle_text_without_error(self):
        """Empty oracle_text should be treated as missing."""
        data = {
            "input_name": "闪电击",
            "english_name": "Lightning Bolt",
            "scryfall_id": "abc-123",
            "oracle_text": "",
            "mana_cost": "{R}",
            "type_line": "Instant",
            "error": None,
        }
        errors, _ = v(validate_card_info(data))
        self.assertTrue(any("oracle_text" in e for e in errors))

    def test_missing_scryfall_id(self):
        data = {
            "input_name": "闪电击",
            "english_name": "Lightning Bolt",
            "scryfall_id": None,
            "oracle_text": "Deals 3 damage.",
            "mana_cost": "{R}",
            "type_line": "Instant",
            "error": None,
        }
        errors, _ = v(validate_card_info(data))
        self.assertTrue(any("scryfall_id" in e for e in errors))

    def test_missing_english_name(self):
        data = {
            "input_name": "闪电击",
            "english_name": None,
            "scryfall_id": "abc-123",
            "oracle_text": "Deals 3 damage.",
            "mana_cost": "{R}",
            "type_line": "Instant",
            "error": None,
        }
        errors, _ = v(validate_card_info(data))
        self.assertTrue(any("english_name" in e for e in errors))

    def test_missing_type_line(self):
        data = {
            "input_name": "闪电击",
            "english_name": "Lightning Bolt",
            "scryfall_id": "abc-123",
            "oracle_text": "Deals 3 damage.",
            "mana_cost": "{R}",
            "type_line": None,
            "error": None,
        }
        errors, _ = v(validate_card_info(data))
        self.assertTrue(any("type_line" in e for e in errors))

    def test_card_with_error_but_has_fields_warns(self):
        """If error is set but fields are present, should warn."""
        data = {
            "input_name": "闪电击",
            "english_name": "Lightning Bolt",
            "scryfall_id": "abc-123",
            "oracle_text": "Deals 3 damage.",
            "mana_cost": "{R}",
            "type_line": "Instant",
            "error": "Some error",
        }
        errors, warnings = v(validate_card_info(data))
        self.assertEqual(len(errors), 0)
        self.assertGreater(len(warnings), 0)

    def test_empty_object(self):
        errors, _ = v(validate_card_info({}))
        self.assertGreater(len(errors), 0)

    def test_not_an_object(self):
        errors, _ = v(validate_card_info("not an object"))
        self.assertGreater(len(errors), 0)


# ═══════════════════════════════════════════════════════════════
# 3. RuleInfo edge cases
# ═══════════════════════════════════════════════════════════════


class TestRuleInfoEdgeCases(unittest.TestCase):
    """Edge cases for RuleInfo validation."""

    def test_valid_rule(self):
        data = {
            "keyword": "protection",
            "matches": [
                {
                    "rule_number": "702.16a",
                    "rule_text": "Protection...",
                    "source_file": "raw/cr/7.md",
                    "source_type": "cr_rule",
                }
            ],
        }
        errors, _ = v(validate_rule_info(data))
        self.assertEqual(len(errors), 0, f"Unexpected errors: {errors}")

    def test_valid_wiki_source(self):
        data = {
            "keyword": "protection",
            "matches": [
                {
                    "rule_number": "N/A",
                    "rule_text": "Protection means...",
                    "source_file": "wiki/concepts/protection.md",
                    "source_type": "wiki_concept",
                }
            ],
        }
        errors, _ = v(validate_rule_info(data))
        self.assertEqual(len(errors), 0, f"Unexpected errors: {errors}")

    def test_invalid_source_type(self):
        data = {
            "keyword": "test",
            "matches": [
                {
                    "rule_number": "702.16a",
                    "rule_text": "test",
                    "source_file": "raw/cr/7.md",
                    "source_type": "invalid_type",
                }
            ],
        }
        errors, _ = v(validate_rule_info(data))
        self.assertTrue(any("invalid_type" in e for e in errors))

    def test_cr_rule_without_raw_prefix(self):
        data = {
            "keyword": "test",
            "matches": [
                {
                    "rule_number": "702.16a",
                    "rule_text": "test",
                    "source_file": "wiki/concepts/test.md",
                    "source_type": "cr_rule",
                }
            ],
        }
        errors, _ = v(validate_rule_info(data))
        self.assertTrue(any("raw/" in e for e in errors))

    def test_empty_matches(self):
        """Empty matches array should not error (just no rules found)."""
        data = {"keyword": "test", "matches": []}
        errors, _ = v(validate_rule_info(data))
        self.assertEqual(len(errors), 0)

    def test_missing_match_fields(self):
        data = {
            "keyword": "test",
            "matches": [{"rule_number": "702.16a"}],
        }
        errors, _ = v(validate_rule_info(data))
        self.assertTrue(any("rule_text" in e for e in errors))
        self.assertTrue(any("source_file" in e for e in errors))
        self.assertTrue(any("source_type" in e for e in errors))

    def test_multiple_matches_one_invalid(self):
        data = {
            "keyword": "test",
            "matches": [
                {
                    "rule_number": "702.16a",
                    "rule_text": "valid",
                    "source_file": "raw/cr/7.md",
                    "source_type": "cr_rule",
                },
                {
                    "rule_number": "702.16b",
                    "rule_text": "invalid source type",
                    "source_file": "raw/cr/7.md",
                    "source_type": "bad_type",
                },
            ],
        }
        errors, _ = v(validate_rule_info(data))
        self.assertEqual(len(errors), 1)
        self.assertTrue(any("bad_type" in e for e in errors))

    def test_wiki_decision_tree_accepted(self):
        data = {
            "keyword": "test",
            "matches": [
                {
                    "rule_number": "wiki-decision-tree",
                    "rule_text": "test",
                    "source_file": "wiki/branches/referee/decision-trees/lands.md",
                    "source_type": "wiki_decision_tree",
                }
            ],
        }
        errors, _ = v(validate_rule_info(data))
        self.assertEqual(len(errors), 0)


# ═══════════════════════════════════════════════════════════════
# 4. Analysis edge cases
# ═══════════════════════════════════════════════════════════════


class TestAnalysisEdgeCases(unittest.TestCase):
    """Edge cases for Analysis validation."""

    def setUp(self):
        self.evidence = {
            "cards": [
                {
                    "input_name": "闪电击",
                    "english_name": "Lightning Bolt",
                    "scryfall_id": "abc",
                    "oracle_text": "Deals 3 damage.",
                    "mana_cost": "{R}",
                    "type_line": "Instant",
                }
            ],
            "rules": [
                {
                    "keyword": "damage",
                    "matches": [
                        {
                            "rule_number": "702.16a",
                            "rule_text": "Protection...",
                            "source_file": "raw/cr/7.md",
                            "source_type": "cr_rule",
                        }
                    ],
                }
            ],
        }

    def test_valid_analysis(self):
        data = {
            "conclusion": "Can deal damage",
            "reasoning": "Because protection...",
            "confidence": "certain",
            "cited_rules": ["702.16a"],
            "cited_cards": ["Lightning Bolt"],
            "needs_more_evidence": None,
        }
        errors, _ = v(validate_analysis(data, evidence=self.evidence))
        self.assertEqual(len(errors), 0, f"Unexpected errors: {errors}")

    def test_missing_conclusion(self):
        data = {
            "reasoning": "Because...",
            "confidence": "certain",
            "cited_rules": [],
            "cited_cards": [],
        }
        errors, _ = v(validate_analysis(data))
        self.assertTrue(any("conclusion" in e for e in errors))

    def test_invalid_confidence(self):
        data = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "maybe",
            "cited_rules": [],
            "cited_cards": [],
        }
        errors, _ = v(validate_analysis(data))
        self.assertTrue(any("confidence" in e for e in errors))

    def test_cited_rule_not_in_evidence(self):
        data = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "certain",
            "cited_rules": ["999.99"],
            "cited_cards": ["Lightning Bolt"],
            "needs_more_evidence": None,
        }
        errors, _ = v(validate_analysis(data, evidence=self.evidence))
        self.assertTrue(any("999.99" in e for e in errors))

    def test_cited_card_not_in_evidence(self):
        data = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "certain",
            "cited_rules": ["702.16a"],
            "cited_cards": ["Nonexistent Card"],
            "needs_more_evidence": None,
        }
        errors, _ = v(validate_analysis(data, evidence=self.evidence))
        self.assertTrue(any("Nonexistent Card" in e for e in errors))

    def test_confidence_certain_with_unverified_assumption_warns(self):
        data = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "certain",
            "cited_rules": ["702.16a"],
            "cited_cards": ["Lightning Bolt"],
            "assumptions": [
                {"assumption": "Protection is red", "evidence_based": False}
            ],
            "needs_more_evidence": None,
        }
        errors, warnings = v(validate_analysis(data, evidence=self.evidence))
        self.assertEqual(len(errors), 0)
        self.assertTrue(any("evidence-based" in w.lower() for w in warnings))

    def test_confidence_certain_with_evidence_based_assumption_no_warn(self):
        data = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "certain",
            "cited_rules": ["702.16a"],
            "cited_cards": ["Lightning Bolt"],
            "assumptions": [
                {"assumption": "Lightning Bolt deals damage", "evidence_based": True}
            ],
            "needs_more_evidence": None,
        }
        errors, warnings = v(validate_analysis(data, evidence=self.evidence))
        self.assertEqual(len(errors), 0)
        self.assertEqual(len(warnings), 0)

    def test_confidence_likely_with_unverified_assumption_no_warn(self):
        """Only confidence=certain triggers the assumption warning."""
        data = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "likely",
            "cited_rules": ["702.16a"],
            "cited_cards": ["Lightning Bolt"],
            "assumptions": [
                {"assumption": "Some guess", "evidence_based": False}
            ],
            "needs_more_evidence": None,
        }
        errors, warnings = v(validate_analysis(data, evidence=self.evidence))
        self.assertEqual(len(errors), 0)
        self.assertEqual(len(warnings), 0)

    def test_no_evidence_skips_citation_check(self):
        """Without evidence, citation checks should be skipped."""
        data = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "certain",
            "cited_rules": ["999.99"],
            "cited_cards": ["Nonexistent"],
            "needs_more_evidence": None,
        }
        errors, _ = v(validate_analysis(data, evidence=None))
        # Should not error about missing citations since no evidence provided
        self.assertEqual(len(errors), 0)

    def test_empty_cited_rules_and_cards(self):
        data = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "uncertain",
            "cited_rules": [],
            "cited_cards": [],
            "needs_more_evidence": None,
        }
        errors, _ = v(validate_analysis(data, evidence=self.evidence))
        self.assertEqual(len(errors), 0)

    def test_invalid_assumption_schema(self):
        data = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "certain",
            "cited_rules": [],
            "cited_cards": [],
            "assumptions": [{"assumption": "test"}],  # missing evidence_based
            "needs_more_evidence": None,
        }
        errors, _ = v(validate_analysis(data))
        self.assertTrue(any("evidence_based" in e for e in errors))

    def test_needs_more_evidence_with_invalid_schema(self):
        data = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "certain",
            "cited_rules": [],
            "cited_cards": [],
            "needs_more_evidence": {"reason": "missing rules"},  # missing "rules"
        }
        errors, _ = v(validate_analysis(data))
        self.assertTrue(any("rules" in e for e in errors))


# ═══════════════════════════════════════════════════════════════
# 5. Verdict edge cases
# ═══════════════════════════════════════════════════════════════


class TestVerdictEdgeCases(unittest.TestCase):
    """Edge cases for Verdict validation."""

    def test_valid_pass_verdict(self):
        data = {
            "status": "PASS",
            "card_check": "PASS",
            "rule_check": "PASS",
            "evidence_check": "PASS",
            "citation_check": "PASS",
            "notes": "All good",
        }
        errors, _ = v(validate_verdict(data))
        self.assertEqual(len(errors), 0)

    def test_card_check_fail_but_status_pass_warns(self):
        """FAIL checks should have status=BLOCK."""
        data = {
            "status": "PASS",
            "card_check": "FAIL",
            "rule_check": "PASS",
            "evidence_check": "PASS",
            "citation_check": "PASS",
            "notes": "Inconsistent",
        }
        errors, warnings = v(validate_verdict(data))
        self.assertEqual(len(errors), 0)
        self.assertTrue(any("FAIL" in w and "BLOCK" in w for w in warnings))

    def test_evidence_check_fail_but_status_pass_warns(self):
        data = {
            "status": "PASS",
            "card_check": "PASS",
            "rule_check": "PASS",
            "evidence_check": "FAIL",
            "citation_check": "PASS",
            "notes": "Inconsistent",
        }
        errors, warnings = v(validate_verdict(data))
        self.assertTrue(any("FAIL" in w for w in warnings))

    def test_all_pass_but_status_block_warns(self):
        data = {
            "status": "BLOCK",
            "card_check": "PASS",
            "rule_check": "PASS",
            "evidence_check": "PASS",
            "citation_check": "PASS",
            "notes": "Why blocked?",
        }
        errors, warnings = v(validate_verdict(data))
        # This is unusual but not necessarily wrong, so no hard error
        # But could be a warning in future versions

    def test_invalid_status(self):
        data = {
            "status": "OK",
            "card_check": "PASS",
            "rule_check": "PASS",
            "evidence_check": "PASS",
            "citation_check": "PASS",
            "notes": "test",
        }
        errors, _ = v(validate_verdict(data))
        self.assertTrue(any("status" in e for e in errors))

    def test_invalid_evidence_check(self):
        data = {
            "status": "PASS",
            "card_check": "PASS",
            "rule_check": "PASS",
            "evidence_check": "NOPE",
            "citation_check": "PASS",
            "notes": "test",
        }
        errors, _ = v(validate_verdict(data))
        self.assertTrue(any("evidence_check" in e for e in errors))

    def test_missing_field(self):
        data = {
            "status": "PASS",
            "card_check": "PASS",
            "rule_check": "PASS",
            "evidence_check": "PASS",
            # missing citation_check
            "notes": "test",
        }
        errors, _ = v(validate_verdict(data))
        self.assertTrue(any("citation_check" in e for e in errors))


# ═══════════════════════════════════════════════════════════════
# 6. Evidence package edge cases
# ═══════════════════════════════════════════════════════════════


class TestEvidencePackageEdgeCases(unittest.TestCase):
    """Edge cases for Evidence package validation."""

    def test_valid_package(self):
        evidence = {
            "cards": [
                {
                    "input_name": "闪电击",
                    "english_name": "Lightning Bolt",
                    "scryfall_id": "abc",
                    "oracle_text": "Deals 3.",
                    "mana_cost": "{R}",
                    "type_line": "Instant",
                }
            ],
            "rules": [
                {
                    "keyword": "damage",
                    "matches": [
                        {
                            "rule_number": "702.16a",
                            "rule_text": "Protection...",
                            "source_file": "raw/cr/7.md",
                            "source_type": "cr_rule",
                        }
                    ],
                }
            ],
            "rulings": [
                {
                    "scryfall_id": "abc",
                    "rulings": [
                        {"published_at": "2021-06-18", "comment": "test", "source": "wotc"}
                    ],
                }
            ],
        }
        errors, _ = v(validate_evidence_package(evidence))
        self.assertEqual(len(errors), 0, f"Unexpected errors: {errors}")

    def test_ruling_scryfall_id_not_in_cards_warns(self):
        evidence = {
            "cards": [
                {
                    "input_name": "闪电击",
                    "english_name": "Lightning Bolt",
                    "scryfall_id": "abc",
                    "oracle_text": "Deals 3.",
                    "mana_cost": "{R}",
                    "type_line": "Instant",
                }
            ],
            "rules": [],
            "rulings": [
                {
                    "scryfall_id": "xyz-different",
                    "rulings": [
                        {"published_at": "2021-06-18", "comment": "test", "source": "wotc"}
                    ],
                }
            ],
        }
        errors, warnings = v(validate_evidence_package(evidence))
        self.assertEqual(len(errors), 0)
        self.assertTrue(any("xyz-different" in w for w in warnings))

    def test_card_with_error_in_package(self):
        evidence = {
            "cards": [
                {
                    "input_name": "未知牌",
                    "english_name": None,
                    "scryfall_id": None,
                    "oracle_text": None,
                    "mana_cost": None,
                    "type_line": None,
                    "error": "Card not found",
                }
            ],
            "rules": [],
            "rulings": [],
        }
        errors, _ = v(validate_evidence_package(evidence))
        self.assertEqual(len(errors), 0)  # Error cards should not fail validation

    def test_empty_package(self):
        evidence = {"cards": [], "rules": [], "rulings": []}
        errors, _ = v(validate_evidence_package(evidence))
        self.assertEqual(len(errors), 0)

    def test_not_a_dict(self):
        errors, _ = v(validate_evidence_package("not a dict"))
        self.assertGreater(len(errors), 0)


# ═══════════════════════════════════════════════════════════════
# 7. Complex / integration edge cases
# ═══════════════════════════════════════════════════════════════


class TestComplexEdgeCases(unittest.TestCase):
    """Complex scenarios and integration tests."""

    def test_multiple_cards_one_with_error(self):
        """Package with one valid card and one error card."""
        evidence = {
            "cards": [
                {
                    "input_name": "闪电击",
                    "english_name": "Lightning Bolt",
                    "scryfall_id": "abc",
                    "oracle_text": "Deals 3.",
                    "mana_cost": "{R}",
                    "type_line": "Instant",
                },
                {
                    "input_name": "未知牌",
                    "english_name": None,
                    "scryfall_id": None,
                    "oracle_text": None,
                    "mana_cost": None,
                    "type_line": None,
                    "error": "Not found",
                },
            ],
            "rules": [],
            "rulings": [],
        }
        errors, _ = v(validate_evidence_package(evidence))
        self.assertEqual(len(errors), 0)

    def test_analysis_cites_card_from_error_entry(self):
        """Analysis should not cite a card that failed lookup."""
        evidence = {
            "cards": [
                {
                    "input_name": "闪电击",
                    "english_name": "Lightning Bolt",
                    "scryfall_id": "abc",
                    "oracle_text": "Deals 3.",
                    "mana_cost": "{R}",
                    "type_line": "Instant",
                },
                {
                    "input_name": "未知牌",
                    "english_name": None,
                    "scryfall_id": None,
                    "oracle_text": None,
                    "error": "Not found",
                },
            ],
            "rules": [],
        }
        analysis = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "certain",
            "cited_rules": [],
            "cited_cards": ["Lightning Bolt"],  # Valid
            "needs_more_evidence": None,
        }
        errors, _ = v(validate_analysis(analysis, evidence=evidence))
        self.assertEqual(len(errors), 0)

    def test_multiple_rules_same_rule_number(self):
        """Evidence can have the same rule number from different keywords."""
        evidence = {
            "cards": [],
            "rules": [
                {
                    "keyword": "protection",
                    "matches": [
                        {
                            "rule_number": "702.16a",
                            "rule_text": "...",
                            "source_file": "raw/cr/7.md",
                            "source_type": "cr_rule",
                        }
                    ],
                },
                {
                    "keyword": "protection from",
                    "matches": [
                        {
                            "rule_number": "702.16a",
                            "rule_text": "...",
                            "source_file": "raw/cr/7.md",
                            "source_type": "cr_rule",
                        }
                    ],
                },
            ],
        }
        analysis = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "certain",
            "cited_rules": ["702.16a"],
            "cited_cards": [],
            "needs_more_evidence": None,
        }
        errors, _ = v(validate_analysis(analysis, evidence=evidence))
        self.assertEqual(len(errors), 0)

    def test_wiki_na_rule_number_accepted(self):
        """Wiki sources often have rule_number='N/A'."""
        evidence = {
            "cards": [],
            "rules": [
                {
                    "keyword": "legendary",
                    "matches": [
                        {
                            "rule_number": "N/A",
                            "rule_text": "Legendary rule...",
                            "source_file": "wiki/concepts/legendary.md",
                            "source_type": "wiki_concept",
                        }
                    ],
                }
            ],
        }
        analysis = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "certain",
            "cited_rules": ["N/A"],
            "cited_cards": [],
            "needs_more_evidence": None,
        }
        errors, _ = v(validate_analysis(analysis, evidence=evidence))
        self.assertEqual(len(errors), 0)


# ═══════════════════════════════════════════════════════════════
# Run
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    unittest.main(verbosity=2)
