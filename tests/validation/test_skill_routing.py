#!/usr/bin/env python3
"""Static routing checks for project MTG skills.

This does not pretend to simulate an LLM router. It guards the contract that
each project skill has at least one routing regression case and that the
frontmatter description carries enough trigger language for those cases.
"""

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = ROOT / "tests" / "routing" / "mtg_skill_routing_cases.json"
SKILL_ROOT = ROOT / "skill"
SHARED_CONTRACT = "skill/_shared/mtg-common.md"


def parse_skill_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise AssertionError(f"{path}: missing frontmatter")
    end = text.find("\n---", 3)
    if end == -1:
        raise AssertionError(f"{path}: unclosed frontmatter")
    data = {}
    for line in text[3:end].splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line.strip())
        if match:
            data[match.group(1)] = match.group(2).strip().strip("\"'")
    return data


def project_skills() -> dict:
    skills = {}
    for path in sorted(SKILL_ROOT.glob("*/SKILL.md")):
        fm = parse_skill_frontmatter(path)
        name = fm.get("name")
        desc = fm.get("description", "")
        if not name:
            raise AssertionError(f"{path}: missing name")
        skills[name] = {"path": path, "description": desc}
    return skills


def score_description(description: str, signals: list[str]) -> int:
    haystack = description.casefold()
    return sum(1 for signal in signals if signal.casefold() in haystack)


class SkillRoutingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skills = project_skills()
        cls.cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))["cases"]

    def test_every_case_targets_existing_skill(self):
        for case in self.cases:
            self.assertIn(
                case["expected_skill"],
                self.skills,
                f"{case['id']}: expected skill does not exist",
            )

    def test_every_project_skill_has_a_routing_case(self):
        covered = {case["expected_skill"] for case in self.cases}
        ignored = {"_shared"}
        uncovered = sorted(set(self.skills) - covered - ignored)
        self.assertFalse(uncovered, f"Project skills without routing cases: {uncovered}")

    def test_expected_skill_description_has_route_signals(self):
        for case in self.cases:
            skill = self.skills[case["expected_skill"]]
            score = score_description(skill["description"], case["signals"])
            self.assertGreater(
                score,
                0,
                f"{case['id']}: {case['expected_skill']} description lacks routing signals {case['signals']}",
            )

    def test_expected_skill_scores_highest_for_case_signals(self):
        for case in self.cases:
            scores = {
                name: score_description(skill["description"], case["signals"])
                for name, skill in self.skills.items()
            }
            expected = case["expected_skill"]
            best_score = max(scores.values())
            self.assertEqual(
                scores[expected],
                best_score,
                f"{case['id']}: expected {expected} score {scores[expected]} below best {best_score}: {scores}",
            )

    def test_shared_contract_is_configured_and_injected_for_judge_subagents(self):
        config = json.loads((ROOT / "opencode.json").read_text(encoding="utf-8"))
        self.assertIn(SHARED_CONTRACT, config.get("instructions", []))

        judge_path = self.skills["mtg-judge-zh"]["path"]
        judge_body = judge_path.read_text(encoding="utf-8")
        self.assertIn(
            SHARED_CONTRACT,
            judge_body,
            "mtg-judge-zh must explicitly pass L2 shared contract into subagent prompts",
        )


if __name__ == "__main__":
    unittest.main()
