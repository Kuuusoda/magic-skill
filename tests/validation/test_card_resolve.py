#!/usr/bin/env python3
"""Regression tests for card_resolve.py entity disambiguation."""

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

import card_resolve
import format_meta_evidence


class TestCardResolve(unittest.TestCase):
    def resolve(self, query: str, fmt: str, intent: str):
        return card_resolve.resolve(query, fmt, intent, allow_api=False)

    def test_duel_commander_shorthand_beats_bad_fuzzy(self):
        cases = [
            ("2099", "Spider-Man 2099"),
            ("spider99", "Spider-Man 2099"),
            ("phelia", "Phelia, Exuberant Shepherd"),
            ("kess", "Kess, Dissident Mage"),
            ("niv", "Niv-Mizzet, Parun"),
        ]
        for query, expected in cases:
            with self.subTest(query=query):
                result = self.resolve(query, "duel-commander", "commander")
                self.assertEqual(result["selected"], expected)
                self.assertFalse(result["needs_clarification"])

    def test_duel_commander_2099_has_meta_evidence(self):
        result = card_resolve.resolve(
            "2099",
            "duel-commander",
            "commander",
            allow_api=False,
            require_meta_evidence=True,
        )
        self.assertEqual(result["selected"], "Spider-Man 2099")
        self.assertFalse(result["needs_clarification"])
        self.assertTrue(result["meta_evidence_found"])
        top = result["candidates"][0]
        self.assertEqual(top["name"], "Spider-Man 2099")
        self.assertIn("meta_evidence", top)
        self.assertNotIn("Miguel O'Hara", top["name"])

    def test_format_meta_evidence_lookup(self):
        result = format_meta_evidence.resolve_meta_evidence("blue farm", "cedh", "deck")
        self.assertTrue(result["evidence_found"])
        self.assertEqual(result["matches"][0]["name"], "Blue Farm (Tymna the Weaver / Kraum, Ludevic's Opus)")

    def test_cedh_deck_and_combo_shorthand(self):
        cases = [
            ("blue farm", "Blue Farm (Tymna the Weaver / Kraum, Ludevic's Opus)", "deck"),
            ("tnt", "Tymna the Weaver / Thrasios, Triton Hero", "commander"),
            ("rogsi", "Rograkh, Son of Rohgahh / Silas Renn, Seeker Adept", "commander"),
            ("thoracle", "Thassa's Oracle", "combo"),
            ("breach", "Underworld Breach", "combo"),
        ]
        for query, expected, intent in cases:
            with self.subTest(query=query):
                result = self.resolve(query, "cedh", intent)
                self.assertEqual(result["selected"], expected)
                self.assertFalse(result["needs_clarification"])

    def test_modern_archetype_shorthand(self):
        cases = [
            ("frog", "Dimir Frog"),
            ("energy", "Boros Energy"),
            ("belcher", "Tameshi Belcher"),
            ("amulet", "Amulet Titan"),
        ]
        for query, expected in cases:
            with self.subTest(query=query):
                result = self.resolve(query, "modern", "deck")
                self.assertEqual(result["selected"], expected)
                self.assertFalse(result["needs_clarification"])

    def test_interaction_components(self):
        result = self.resolve("oracle consultation", "judge", "interaction")
        self.assertEqual(result["selected"], "Thassa's Oracle + Demonic Consultation")
        self.assertEqual(result["components"], ["Thassa's Oracle", "Demonic Consultation"])
        self.assertFalse(result["needs_clarification"])

        result = self.resolve("breach LED", "judge", "interaction")
        self.assertEqual(result["selected"], "Underworld Breach + Lion's Eye Diamond")
        self.assertEqual(result["components"], ["Underworld Breach", "Lion's Eye Diamond"])
        self.assertFalse(result["needs_clarification"])


if __name__ == "__main__":
    unittest.main()
