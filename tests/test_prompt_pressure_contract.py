"""Structural contract tests for the daily research prompt skill.

These tests check required instructions, not whether any LLM follows them.
Run: python -m unittest tests/test_prompt_pressure_contract.py
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "daily-discipleship-research-prompt" / "SKILL.md"


class PromptPressureContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t = SKILL.read_text(encoding="utf-8")

    def test_original_modes_and_handoff_survive(self):
        for term in ("PROMPT_ONLY", "SELF_EXECUTE", "NEXT: discipleship-deep-research-executor",
                     "Do **not** perform the research", "CONTEXT", "provisional",
                     "resume checkpoint"):
            with self.subTest(term=term):
                self.assertIn(term.lower(), self.t.lower())

    def test_seven_levers_and_selective_usage(self):
        for term in ("High expertise", 'Obviously', "Imagined audience",
                     "Odd creative constraint", "Imaginary bet", "Invented opponent",
                     "Version 2.0", "**two or three**"):
            with self.subTest(term=term):
                self.assertIn(term, self.t)

    def test_adversarial_checks(self):
        for term in ("Challenge the premise", "Steelman one competing view",
                     "Decision test", "Substantive revision pass",
                     "independently supported effect", "UNVERIFIED"):
            with self.subTest(term=term):
                self.assertIn(term, self.t)

    def test_integrity_boundaries(self):
        for term in ("false memory", "Do not state these tactics have been proven",
                     "not just this skill", "PROMPT_ONLY or SELF_EXECUTE"):
            with self.subTest(term=term):
                self.assertIn(term, self.t)


if __name__ == "__main__":
    unittest.main()
