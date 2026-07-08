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


class TestCardResolve(unittest.TestCase):
    def resolve(self, query: str, fmt: str, intent: str):
        return card_resolve.resolve(query, fmt, intent, allow_api=False)

    def test_duel_commander_shorthand_beats_bad_fuzzy(self):
        cases = [
            ("spider99", "Spider-Man 2099, Miguel O'Hara"),
            ("phelia", "Phelia, Exuberant Shepherd"),
            ("kess", "Kess, Dissident Mage"),
            ("niv", "Niv-Mizzet, Parun"),
        ]
        for query, expected in cases:
            with self.subTest(query=query):
                result = self.resolve(query, "duel-commander", "commander")
                self.assertEqual(result["selected"], expected)
                self.assertFalse(result["needs_clarification"])

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
