"""Regression checks for metadata/registry failures; synthetic files only."""
from pathlib import Path
import tempfile
import unittest
import check_skills

class SkillValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "skills/example/SKILL.md"
        self.skill.parent.mkdir(parents=True)
        self.skill.write_text('---\nname: example\ndescription: "A useful skill: with detail"\n---\nBody\n')
        self.config = self.root / "config/assistant.yaml"
        self.config.parent.mkdir()
        self.config.write_text('shared_skills: [example]\ndiscipleship_skills: []\nevidence_labels: [HYPOTHESIS]\n')
        (self.root / "AGENTS.md").write_text('## Evidence taxonomy\n\n- '+chr(96)+'HYPOTHESIS'+chr(96)+' - tentative.\n\n## Next\n')
    def errors(self):
        return check_skills.validate(self.root)[1]
    def test_valid_metadata_and_registry(self):
        self.assertEqual(self.errors(), [])
    def test_unquoted_colon_is_rejected(self):
        self.skill.write_text('---\nname: example\ndescription: A skill: with detail\n---\n')
        self.assertTrue(self.errors())
    def test_directory_mismatch_is_rejected(self):
        self.skill.write_text('---\nname: another\ndescription: Test\n---\n')
        self.assertTrue(any('directory mismatch' in e for e in self.errors()))
    def test_description_delimiter_text_is_valid(self):
        self.skill.write_text('---\nname: example\ndescription: "Use --- as a separator"\n---\n')
        self.assertEqual(self.errors(), [])
    def test_missing_closing_delimiter_is_rejected(self):
        self.skill.write_text('---\nname: example\ndescription: Test\n')
        self.assertTrue(any('unclosed' in e for e in self.errors()))
    def test_missing_registered_skill_is_rejected(self):
        self.config.write_text('shared_skills: []\ndiscipleship_skills: []\nevidence_labels: [HYPOTHESIS]\n')
        self.assertTrue(any('registry mismatch' in e for e in self.errors()))
    def test_duplicate_registry_name_is_rejected(self):
        self.config.write_text('shared_skills: [example]\ndiscipleship_skills: [example]\nevidence_labels: [HYPOTHESIS]\n')
        self.assertTrue(any('duplicate skill' in e for e in self.errors()))
    def test_taxonomy_drift_is_rejected(self):
        self.config.write_text('shared_skills: [example]\ndiscipleship_skills: []\nevidence_labels: [DOCUMENTED_EVIDENCE]\n')
        self.assertTrue(any('evidence labels' in e for e in self.errors()))
    def test_empty_skill_tree_is_rejected(self):
        self.skill.unlink()
        self.assertTrue(any('no skills' in e for e in self.errors()))

if __name__ == "__main__":
    unittest.main()
