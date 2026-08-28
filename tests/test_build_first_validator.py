from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_build_first", ROOT / "scripts" / "validate_build_first.py")
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


class BuildFirstValidatorTests(unittest.TestCase):
    def test_current_repo_passes(self):
        problems = validator.validate(ROOT)
        self.assertEqual([], problems, "\n".join(str(p) for p in problems))

    def test_missing_authority_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            problems = []
            validator.check_authority(Path(tmp), problems)
            self.assertTrue(any(p.code == "BUILD001" for p in problems))

    def test_broken_spine_sequence_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "docs" / "BOT-EVOLUTION-ROADMAP.md"
            path.parent.mkdir(parents=True)
            path.write_text("| M00 | v0.0 | A |\n| M02 | v0.2 | C |\n", encoding="utf-8")
            problems = []
            validator.check_roadmap_spine(root, problems)
            self.assertTrue(any(p.code == "BUILD003" for p in problems))

    def test_backwards_bot_version_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "docs" / "BOT-EVOLUTION-ROADMAP.md"
            path.parent.mkdir(parents=True)
            rows = []
            for i in range(16):
                version = f"v0.{i}" if i < 4 else f"v{i - 3}.0"
                rows.append(f"| M{i:02d} | {version} | target |")
            rows[3] = "| M03 | v0.1 | backwards |"
            path.write_text("\n".join(rows) + "\n", encoding="utf-8")
            problems = []
            validator.check_roadmap_spine(root, problems)
            self.assertTrue(any(p.code == "BUILD006" for p in problems))

    def test_unknown_lesson_ref_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "missions").mkdir()
            mission = root / "missions" / "M00-test.md"
            mission.write_text(
                '''---\nmission_id: "M00"\nstatus: planned\nrequires_missions: []\nbot_version_to: "v0.0"\nknowledge:\n  required: ["99.99"]\nprojects:\n  contributes_to: []\n---\n''',
                encoding="utf-8",
            )
            problems = []
            validator.check_missions(root, {"0.1"}, {"M00": "v0.0"}, problems)
            self.assertTrue(any(p.code == "BUILD004" for p in problems))

    def test_forward_dependency_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "missions").mkdir()
            mission = root / "missions" / "M00-test.md"
            mission.write_text(
                '''---\nmission_id: "M00"\nstatus: planned\nrequires_missions: ["M01"]\nbot_version_to: "v0.0"\nknowledge:\n  required: []\nprojects:\n  contributes_to: []\n---\n''',
                encoding="utf-8",
            )
            problems = []
            validator.check_missions(root, set(), {"M00": "v0.0"}, problems)
            self.assertTrue(any(p.code == "BUILD005" for p in problems))

    def test_ready_mission_missing_tests_section_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "missions").mkdir()
            headings = [h for h in validator.READY_HEADINGS if h != "## Tests"]
            mission = root / "missions" / "M00-test.md"
            mission.write_text(
                '''---\nmission_id: "M00"\nstatus: ready\nrequires_missions: []\nbot_version_to: "v0.0"\nknowledge:\n  required: []\nprojects:\n  contributes_to: []\n---\n\n''' + "\n\n".join(headings) + "\n",
                encoding="utf-8",
            )
            problems = []
            validator.check_missions(root, set(), {"M00": "v0.0"}, problems)
            self.assertTrue(any(p.code == "BUILD007" and "## Tests" in p.message for p in problems))

    def test_lesson_pass_mechanism_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "missions").mkdir()
            mission = root / "missions" / "M00-test.md"
            mission.write_text(
                '''---\nmission_id: "M00"\nstatus: planned\nrequires_missions: []\nbot_version_to: "v0.0"\nknowledge:\n  required: []\nprojects:\n  contributes_to: []\nlesson_pass: true\n---\n''',
                encoding="utf-8",
            )
            problems = []
            validator.check_missions(root, set(), {"M00": "v0.0"}, problems)
            self.assertTrue(any(p.code == "BUILD008" for p in problems))

    def test_project_15_reference_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "missions").mkdir()
            mission = root / "missions" / "M00-test.md"
            mission.write_text(
                '''---\nmission_id: "M00"\nstatus: planned\nrequires_missions: []\nbot_version_to: "v0.0"\nknowledge:\n  required: []\nprojects:\n  contributes_to: [15]\n---\n''',
                encoding="utf-8",
            )
            problems = []
            validator.check_missions(root, set(), {"M00": "v0.0"}, problems)
            self.assertTrue(any(p.code == "BUILD009" for p in problems))

    def test_missing_bootstrap_bot_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            problems = []
            validator.check_bootstrap(Path(tmp), problems)
            self.assertTrue(any(p.code == "BUILD010" for p in problems))


if __name__ == "__main__":
    unittest.main()
