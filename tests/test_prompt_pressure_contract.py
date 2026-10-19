"""Structural checks for the upgraded daily discipleship research-prompt skill.

These inspect the skill contract, not an LLM's reasoning or factual accuracy.
Run from the repository root:
    python -m unittest discover -s tests -p test_prompt_pressure_contract.py
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "daily-discipleship-research-prompt" / "SKILL.md"


class CriticalResearchPromptContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = SKILL.read_text(encoding="utf-8")

    def assert_markers(self, *markers):
        for marker in markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, self.text)

    def test_original_modes_and_routing_survive(self):
        self.assert_markers(
            "Do **not** perform the research", "PROMPT_ONLY", "SELF_EXECUTE",
            "### TODAY'S RESEARCH QUESTION", "### COPY INTO GENSPARK",
            "NEXT: discipleship-deep-research-executor",
            "## Save progress and make interrupted work resumable",
            "resume checkpoint", "## Plain-language learning requirement"
        )

    def test_four_research_challenges_exist(self):
        self.assert_markers(
            "Challenge the premise", "Steelman the alternative",
            "Set reversal conditions", "Reconsider the conclusion",
            "strongest fair objection", "if no change is warranted"
        )

    def test_adaptive_low_overhead_and_seven_optional_levers(self):
        self.assert_markers(
            "For narrow fact-checks", "do not manufacture an opponent",
            "at most two or three", "Expertise standard", "“Obviously” bait",
            "Audience:", "Weird constraint", "Imaginary bet",
            "Opponent:", "Version 2.0"
        )

    def test_source_and_memory_integrity(self):
        self.assert_markers(
            "independently supported effects", "UNVERIFIED",
            "“yesterday,”", "G2/G3 disciple-making",
            "Do not claim these pressure tactics improve factual accuracy"
        )

    def test_still_requests_full_bounded_report(self):
        self.assert_markers(
            "## Required report artifact", "### EXECUTION PROMPT",
            "### HANDOFF", "What This Research Does Not Prove",
            "Sources with direct links/citations", "PRACTICE INTELLIGENCE"
        )


if __name__ == "__main__":
    unittest.main()
