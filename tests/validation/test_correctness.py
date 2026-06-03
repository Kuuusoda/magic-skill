#!/usr/bin/env python3
"""
Correctness regression tests for mtg-judge-zh validation.py

Ensures the new validation rules do NOT falsely reject valid outputs
from normal, successful analyses. Prevents overfitting of the validation
system to edge cases at the expense of standard use cases.

Run: python3 -m pytest tests/validation/test_correctness.py -v
     or: python3 tests/validation/test_correctness.py
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

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
    validate_full_pipeline,
    ValidationResult,
)


def v(result: ValidationResult) -> tuple[list[str], list[str]]:
    return result.errors, result.warnings


# ═══════════════════════════════════════════════════════════════
# 1. Standard valid outputs must PASS
# ═══════════════════════════════════════════════════════════════


class TestStandardValidOutputs(unittest.TestCase):
    """Verify that normal, valid agent outputs are accepted."""

    def test_typical_query_plan(self):
        """A standard interaction question about protection."""
        data = {
            "cards": ["闪电击", "幽灵选手"],
            "rule_keywords": ["protection", "702.16", "damage"],
            "question_type": "interaction",
            "needs_rulings": False,
            "needs_strategy": False,
        }
        errors, warnings = v(validate_query_plan(data))
        self.assertEqual(len(errors), 0, f"Valid query plan rejected: {errors}")
        self.assertEqual(len(warnings), 0)

    def test_typical_card_info_lightning_bolt(self):
        """Standard Lightning Bolt card info."""
        data = {
            "input_name": "闪电击",
            "english_name": "Lightning Bolt",
            "scryfall_id": "f58dba4f-1abb-47a3-a684-29c32bab95c0",
            "oracle_text": "Lightning Bolt deals 3 damage to any target.",
            "mana_cost": "{R}",
            "type_line": "Instant",
            "power_toughness": None,
            "error": None,
        }
        errors, warnings = v(validate_card_info(data))
        self.assertEqual(len(errors), 0)
        self.assertEqual(len(warnings), 0)

    def test_typical_card_info_creature(self):
        """Standard creature card with power/toughness."""
        data = {
            "input_name": "幽灵选手",
            "english_name": "Burrenton Forge-Tender",
            "scryfall_id": "abc-123",
            "oracle_text": "Protection from red. ...",
            "mana_cost": "{W}",
            "type_line": "Creature — Kithkin Wizard",
            "power_toughness": "1/1",
            "error": None,
        }
        errors, warnings = v(validate_card_info(data))
        self.assertEqual(len(errors), 0)

    def test_typical_rule_info_cr(self):
        """Standard CR rule lookup result."""
        data = {
            "keyword": "protection",
            "matches": [
                {
                    "rule_number": "702.16a",
                    "rule_text": "Protection is a static ability...",
                    "source_file": "raw/cr/7.md",
                    "source_type": "cr_rule",
                },
                {
                    "rule_number": "702.16b",
                    "rule_text": "A permanent or player with protection...",
                    "source_file": "raw/cr/7.md",
                    "source_type": "cr_rule",
                },
            ],
        }
        errors, warnings = v(validate_rule_info(data))
        self.assertEqual(len(errors), 0)
        self.assertEqual(len(warnings), 0)

    def test_typical_rule_info_wiki(self):
        """Standard wiki concept lookup result."""
        data = {
            "keyword": "legendary",
            "matches": [
                {
                    "rule_number": "N/A",
                    "rule_text": "Legendary is a supertype...",
                    "source_file": "wiki/concepts/legendary.md",
                    "source_type": "wiki_concept",
                }
            ],
        }
        errors, warnings = v(validate_rule_info(data))
        self.assertEqual(len(errors), 0)

    def test_typical_analysis_no_assumptions(self):
        """Standard analysis with no assumptions — should not warn."""
        evidence = {
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
                    "keyword": "protection",
                    "matches": [
                        {
                            "rule_number": "702.16a",
                            "rule_text": "...",
                            "source_file": "raw/cr/7.md",
                            "source_type": "cr_rule",
                        }
                    ],
                }
            ],
        }
        data = {
            "conclusion": "Lightning Bolt cannot deal damage.",
            "reasoning": "Because 702.16a states that protection prevents damage...",
            "confidence": "certain",
            "cited_rules": ["702.16a"],
            "cited_cards": ["Lightning Bolt"],
            "needs_more_evidence": None,
        }
        errors, warnings = v(validate_analysis(data, evidence=evidence))
        self.assertEqual(len(errors), 0, f"Valid analysis rejected: {errors}")
        self.assertEqual(len(warnings), 0, f"Unexpected warnings: {warnings}")

    def test_typical_analysis_with_evidence_based_assumptions(self):
        """Analysis with evidence-based assumptions — should not warn."""
        evidence = {
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
                            "rule_number": "120.1a",
                            "rule_text": "...",
                            "source_file": "raw/cr/1.md",
                            "source_type": "cr_rule",
                        }
                    ],
                }
            ],
        }
        data = {
            "conclusion": "Can deal damage.",
            "reasoning": "Lightning Bolt is a red instant. It deals damage.",
            "confidence": "certain",
            "cited_rules": ["120.1a"],
            "cited_cards": ["Lightning Bolt"],
            "assumptions": [
                {
                    "assumption": "Lightning Bolt is a red spell",
                    "evidence_based": True,
                    "note": "Confirmed by card type_line",
                }
            ],
            "needs_more_evidence": None,
        }
        errors, warnings = v(validate_analysis(data, evidence=evidence))
        self.assertEqual(len(errors), 0)
        self.assertEqual(len(warnings), 0)

    def test_typical_verdict_pass(self):
        """Standard PASS verdict."""
        data = {
            "status": "PASS",
            "card_check": "PASS",
            "rule_check": "PASS",
            "evidence_check": "PASS",
            "citation_check": "PASS",
            "notes": "All checks passed. Analysis is sound.",
        }
        errors, warnings = v(validate_verdict(data))
        self.assertEqual(len(errors), 0)
        self.assertEqual(len(warnings), 0)

    def test_typical_verdict_warn(self):
        """Standard WARN verdict (some minor concern)."""
        data = {
            "status": "WARN",
            "card_check": "PASS",
            "rule_check": "PASS",
            "evidence_check": "WARN",
            "citation_check": "PASS",
            "notes": "Evidence mostly sufficient but one ruling is old.",
        }
        errors, warnings = v(validate_verdict(data))
        self.assertEqual(len(errors), 0)

    def test_typical_verdict_block(self):
        """Standard BLOCK verdict."""
        data = {
            "status": "BLOCK",
            "card_check": "FAIL",
            "rule_check": "PASS",
            "evidence_check": "FAIL",
            "citation_check": "PASS",
            "notes": "Card lookup failed for one card.",
        }
        errors, warnings = v(validate_verdict(data))
        self.assertEqual(len(errors), 0)


# ═══════════════════════════════════════════════════════════════
# 2. Regression: new checks should not break normal cases
# ═══════════════════════════════════════════════════════════════


class TestRegressionNoOverfitting(unittest.TestCase):
    """Ensure new validation rules don't falsely flag normal outputs."""

    def test_wiki_na_rule_number_not_flagged(self):
        """Wiki sources use 'N/A' as rule_number — should be accepted."""
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
        data = {
            "conclusion": "test",
            "reasoning": "test",
            "confidence": "certain",
            "cited_rules": ["N/A"],
            "cited_cards": [],
            "needs_more_evidence": None,
        }
        errors, _ = v(validate_analysis(data, evidence=evidence))
        self.assertEqual(len(errors), 0, "Wiki 'N/A' rule_number should be accepted")

    def test_wiki_decision_tree_source_accepted(self):
        """Wiki decision tree sources should be accepted."""
        data = {
            "keyword": "blood moon",
            "matches": [
                {
                    "rule_number": "wiki-decision-tree",
                    "rule_text": "Blood Moon sets land subtype...",
                    "source_file": "wiki/branches/referee/decision-trees/lands.md",
                    "source_type": "wiki_decision_tree",
                }
            ],
        }
        errors, _ = v(validate_rule_info(data))
        self.assertEqual(len(errors), 0)

    def test_wiki_framework_source_accepted(self):
        """Wiki framework sources should be accepted."""
        data = {
            "keyword": "layer system",
            "matches": [
                {
                    "rule_number": "wiki-framework",
                    "rule_text": "Layer 4 handles type-changing...",
                    "source_file": "wiki/branches/referee/frameworks/layer-system.md",
                    "source_type": "wiki_framework",
                }
            ],
        }
        errors, _ = v(validate_rule_info(data))
        self.assertEqual(len(errors), 0)

    def test_old_ruling_not_rejected(self):
        """Old rulings should not be automatically rejected.

        The validation script should NOT check ruling freshness.
        That check belongs in the skill logic, not in schema validation.
        """
        data = {
            "scryfall_id": "abc",
            "rulings": [
                {
                    "published_at": "2002-01-01",
                    "comment": "Very old ruling.",
                    "source": "wotc",
                }
            ],
        }
        from validation import validate_ruling_info
        errors, _ = v(validate_ruling_info(data))
        self.assertEqual(len(errors), 0, "Old rulings should not be rejected by validator")

    def test_confidence_likely_no_assumptions_ok(self):
        """confidence=likely with no assumptions should pass cleanly."""
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
                            "rule_number": "120.1a",
                            "rule_text": "...",
                            "source_file": "raw/cr/1.md",
                            "source_type": "cr_rule",
                        }
                    ],
                }
            ],
        }
        data = {
            "conclusion": "Probably can deal damage.",
            "reasoning": "Most likely yes, but depends on protection subtype.",
            "confidence": "likely",
            "cited_rules": ["120.1a"],
            "cited_cards": ["Lightning Bolt"],
            "needs_more_evidence": None,
        }
        errors, warnings = v(validate_analysis(data, evidence=evidence))
        self.assertEqual(len(errors), 0)
        self.assertEqual(len(warnings), 0)

    def test_confidence_uncertain_no_citations_ok(self):
        """confidence=uncertain with no cited rules/cards should pass."""
        data = {
            "conclusion": "Unclear without more info.",
            "reasoning": "Need to know the protection subtype.",
            "confidence": "uncertain",
            "cited_rules": [],
            "cited_cards": [],
            "needs_more_evidence": {
                "rules": ["protection subtype"],
                "reason": "Need to determine which color/type of protection.",
            },
        }
        errors, warnings = v(validate_analysis(data, evidence=None))
        self.assertEqual(len(errors), 0)
        self.assertEqual(len(warnings), 0)

    def test_multiple_cards_all_valid(self):
        """Evidence with multiple valid cards should pass."""
        evidence = {
            "cards": [
                {
                    "input_name": "闪电击",
                    "english_name": "Lightning Bolt",
                    "scryfall_id": "abc1",
                    "oracle_text": "Deals 3.",
                    "mana_cost": "{R}",
                    "type_line": "Instant",
                },
                {
                    "input_name": "幽灵选手",
                    "english_name": "Burrenton Forge-Tender",
                    "scryfall_id": "abc2",
                    "oracle_text": "Protection from red.",
                    "mana_cost": "{W}",
                    "type_line": "Creature — Kithkin Wizard",
                },
            ],
            "rules": [],
            "rulings": [],
        }
        errors, _ = v(validate_evidence_package(evidence))
        self.assertEqual(len(errors), 0)

    def test_card_with_empty_strings_not_null(self):
        """Card with empty string mana_cost should be valid (some lands have no mana cost)."""
        data = {
            "input_name": "海岛",
            "english_name": "Island",
            "scryfall_id": "abc",
            "oracle_text": "({T}: Add {U}.)",
            "mana_cost": "",
            "type_line": "Basic Land — Island",
            "error": None,
        }
        errors, _ = v(validate_card_info(data))
        self.assertEqual(len(errors), 0, "Empty mana_cost is valid for lands")


# ═══════════════════════════════════════════════════════════════
# 3. Full pipeline with realistic data
# ═══════════════════════════════════════════════════════════════


class TestFullPipelineRegression(unittest.TestCase):
    """End-to-end pipeline tests with realistic judge question data."""

    def test_lightning_bolt_vs_protection_pipeline(self):
        """Full pipeline for: 'Can Lightning Bolt damage a creature with protection from red?'"""
        query_plan = {
            "cards": ["闪电击", "幽灵选手"],
            "rule_keywords": ["protection", "702.16", "damage"],
            "question_type": "interaction",
            "needs_rulings": False,
            "needs_strategy": False,
        }
        cards = [
            {
                "input_name": "闪电击",
                "english_name": "Lightning Bolt",
                "scryfall_id": "f58dba4f-1abb-47a3-a684-29c32bab95c0",
                "oracle_text": "Lightning Bolt deals 3 damage to any target.",
                "mana_cost": "{R}",
                "type_line": "Instant",
                "error": None,
            },
            {
                "input_name": "幽灵选手",
                "english_name": "Burrenton Forge-Tender",
                "scryfall_id": "some-id",
                "oracle_text": "Protection from red. ...",
                "mana_cost": "{W}",
                "type_line": "Creature — Kithkin Wizard",
                "error": None,
            },
        ]
        rules = [
            {
                "keyword": "protection",
                "matches": [
                    {
                        "rule_number": "702.16a",
                        "rule_text": "Protection is a static ability...",
                        "source_file": "raw/cr/7.md",
                        "source_type": "cr_rule",
                    },
                    {
                        "rule_number": "702.16b",
                        "rule_text": "A permanent or player with protection...",
                        "source_file": "raw/cr/7.md",
                        "source_type": "cr_rule",
                    },
                ],
            }
        ]
        analysis = {
            "conclusion": "Lightning Bolt cannot deal damage to a creature with protection from red.",
            "reasoning": "702.16b states that damage is prevented. Since Lightning Bolt is red and deals damage, protection from red prevents it.",
            "confidence": "certain",
            "cited_rules": ["702.16a", "702.16b"],
            "cited_cards": ["Lightning Bolt", "Burrenton Forge-Tender"],
            "assumptions": [
                {
                    "assumption": "Burrenton Forge-Tender has protection from red",
                    "evidence_based": True,
                    "note": "Confirmed by oracle_text",
                }
            ],
            "needs_more_evidence": None,
        }
        verdict = {
            "status": "PASS",
            "card_check": "PASS",
            "rule_check": "PASS",
            "evidence_check": "PASS",
            "citation_check": "PASS",
            "notes": "All checks passed. Conclusion is directly supported by CR 702.16.",
        }
        result = validate_full_pipeline(query_plan, cards, rules, analysis, verdict)
        self.assertTrue(result.is_valid(), f"Pipeline failed: {result.errors}")
        self.assertEqual(len(result.warnings), 0, f"Unexpected warnings: {result.warnings}")

    def test_trample_mechanic_rule_pipeline(self):
        """Full pipeline for: 'How does trample work?' (rule explanation, no cards)"""
        query_plan = {
            "cards": [],
            "rule_keywords": ["trample", "702.19", "combat damage"],
            "question_type": "rule",
            "needs_rulings": False,
            "needs_strategy": False,
        }
        cards = []
        rules = [
            {
                "keyword": "trample",
                "matches": [
                    {
                        "rule_number": "702.19a",
                        "rule_text": "Trample is a static ability...",
                        "source_file": "raw/cr/7.md",
                        "source_type": "cr_rule",
                    },
                    {
                        "rule_number": "702.19b",
                        "rule_text": "The controller of an attacking creature...",
                        "source_file": "raw/cr/7.md",
                        "source_type": "cr_rule",
                    },
                ],
            }
        ]
        analysis = {
            "conclusion": "Trample allows excess combat damage to be dealt to the defending player.",
            "reasoning": "702.19b explains the damage assignment order for trample. When a creature with trample is blocked, the attacking player must assign lethal damage to all blockers before assigning excess damage to the defending player or planeswalker.",
            "confidence": "certain",
            "cited_rules": ["702.19a", "702.19b"],
            "cited_cards": [],
            "needs_more_evidence": None,
        }
        verdict = {
            "status": "PASS",
            "card_check": "PASS",
            "rule_check": "PASS",
            "evidence_check": "PASS",
            "citation_check": "PASS",
            "notes": "Standard rule explanation with full CR support.",
        }
        result = validate_full_pipeline(query_plan, cards, rules, analysis, verdict)
        self.assertTrue(result.is_valid(), f"Pipeline failed: {result.errors}")
        self.assertEqual(len(result.warnings), 0, f"Unexpected warnings: {result.warnings}")

    def test_legend_rule_pipeline(self):
        """Full pipeline for: 'What happens if I control two legendaries with the same name?'"""
        query_plan = {
            "cards": ["卡恩", "卡恩"],
            "rule_keywords": ["legendary", "704.5j", "legend rule"],
            "question_type": "rule",
            "needs_rulings": False,
            "needs_strategy": False,
        }
        cards = [
            {
                "input_name": "卡恩",
                "english_name": "Karn, the Great Creator",
                "scryfall_id": "abc",
                "oracle_text": "...",
                "mana_cost": "{4}",
                "type_line": "Legendary Planeswalker — Karn",
                "error": None,
            }
        ]
        rules = [
            {
                "keyword": "legendary",
                "matches": [
                    {
                        "rule_number": "704.5j",
                        "rule_text": "If two or more legendary permanents with the same name...",
                        "source_file": "raw/cr/7.md",
                        "source_type": "cr_rule",
                    },
                    {
                        "rule_number": "N/A",
                        "rule_text": "The legend rule is a state-based action...",
                        "source_file": "wiki/concepts/legend-rule.md",
                        "source_type": "wiki_concept",
                    },
                ],
            }
        ]
        analysis = {
            "conclusion": "You choose one to keep and put the rest into their owners' graveyards.",
            "reasoning": "704.5j (the legend rule) is a state-based action. When you control two legendary permanents with the same name, you must choose one and sacrifice the others.",
            "confidence": "certain",
            "cited_rules": ["704.5j", "N/A"],
            "cited_cards": ["Karn, the Great Creator"],
            "needs_more_evidence": None,
        }
        verdict = {
            "status": "PASS",
            "card_check": "PASS",
            "rule_check": "PASS",
            "evidence_check": "PASS",
            "citation_check": "PASS",
            "notes": "Direct rule explanation.",
        }
        result = validate_full_pipeline(query_plan, cards, rules, analysis, verdict)
        self.assertTrue(result.is_valid(), f"Pipeline failed: {result.errors}")
        self.assertEqual(len(result.warnings), 0, f"Unexpected warnings: {result.warnings}")


# ═══════════════════════════════════════════════════════════════
# Run
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    unittest.main(verbosity=2)
