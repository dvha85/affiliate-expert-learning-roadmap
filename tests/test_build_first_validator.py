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


def ready_headings() -> str:
    return "\n\n".join(validator.READY_HEADINGS) + "\n"


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
                '''---\nmission_id: "M00"\nstatus: planned\nrequires_missions: []\nbot_version_from: null\nbot_version_to: "v0.0"\nknowledge:\n  required: ["99.99"]\nprojects:\n  contributes_to: []\n---\n''',
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
                '''---\nmission_id: "M00"\nstatus: planned\nrequires_missions: ["M01"]\nbot_version_from: null\nbot_version_to: "v0.0"\nknowledge:\n  required: []\nprojects:\n  contributes_to: []\n---\n''',
                encoding="utf-8",
            )
            problems = []
            validator.check_missions(root, set(), {"M00": "v0.0"}, problems)
            self.assertTrue(any(p.code == "BUILD005" for p in problems))

    def test_missing_authored_dependency_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "missions").mkdir()
            mission = root / "missions" / "M01-test.md"
            mission.write_text(
                '''---\nmission_id: "M01"\nstatus: planned\nrequires_missions: ["M00"]\nbot_version_from: "v0.0"\nbot_version_to: "v0.1"\nknowledge:\n  required: []\nprojects:\n  contributes_to: []\n---\n''',
                encoding="utf-8",
            )
            problems = []
            validator.check_missions(root, set(), {"M01": "v0.1"}, problems)
            self.assertTrue(any(p.code == "BUILD005" and "chưa có authored" in p.message for p in problems))

    def test_ready_mission_missing_tests_section_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "missions").mkdir()
            headings = [h for h in validator.READY_HEADINGS if h != "## Tests"]
            mission = root / "missions" / "M00-test.md"
            mission.write_text(
                '''---\nmission_id: "M00"\nstatus: ready\nrequires_missions: []\nbot_version_from: null\nbot_version_to: "v0.0"\nknowledge:\n  required: ["0.1"]\nprojects:\n  contributes_to: []\n---\n\n''' + "\n\n".join(headings) + "\n\nlab/learner/affiliate-bot/\n",
                encoding="utf-8",
            )
            problems = []
            validator.check_missions(root, {"0.1"}, {"M00": "v0.0"}, problems)
            self.assertTrue(any(p.code == "BUILD007" and "## Tests" in p.message for p in problems))

    def test_ready_mission_requires_explicit_required_knowledge(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "missions").mkdir()
            mission = root / "missions" / "M00-test.md"
            mission.write_text(
                '''---\nmission_id: "M00"\nstatus: ready\nrequires_missions: []\nbot_version_from: null\nbot_version_to: "v0.0"\nknowledge:\n  required: []\nprojects:\n  contributes_to: []\n---\n\n''' + ready_headings() + "\nlab/learner/affiliate-bot/\n",
                encoding="utf-8",
            )
            problems = []
            validator.check_missions(root, {"0.1"}, {"M00": "v0.0"}, problems)
            self.assertTrue(any(p.code == "BUILD004" and "knowledge.required" in p.message for p in problems))

    def test_lesson_pass_mechanism_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "missions").mkdir()
            mission = root / "missions" / "M00-test.md"
            mission.write_text(
                '''---\nmission_id: "M00"\nstatus: planned\nrequires_missions: []\nbot_version_from: null\nbot_version_to: "v0.0"\nknowledge:\n  required: []\nprojects:\n  contributes_to: []\nlesson_pass: true\n---\n''',
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
                '''---\nmission_id: "M00"\nstatus: planned\nrequires_missions: []\nbot_version_from: null\nbot_version_to: "v0.0"\nknowledge:\n  required: []\nprojects:\n  contributes_to: [15]\n---\n''',
                encoding="utf-8",
            )
            problems = []
            validator.check_missions(root, set(), {"M00": "v0.0"}, problems)
            self.assertTrue(any(p.code == "BUILD009" for p in problems))

    def test_version_from_must_continue_previous_version(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "missions").mkdir()
            (root / "missions" / "M00-test.md").write_text(
                '''---\nmission_id: "M00"\nstatus: planned\nrequires_missions: []\nbot_version_from: null\nbot_version_to: "v0.0"\nknowledge:\n  required: []\nprojects:\n  contributes_to: []\n---\n''', encoding="utf-8"
            )
            (root / "missions" / "M01-test.md").write_text(
                '''---\nmission_id: "M01"\nstatus: planned\nrequires_missions: ["M00"]\nbot_version_from: "v9.9"\nbot_version_to: "v0.1"\nknowledge:\n  required: []\nprojects:\n  contributes_to: []\n---\n''', encoding="utf-8"
            )
            problems = []
            validator.check_missions(root, set(), {"M00": "v0.0", "M01": "v0.1"}, problems)
            self.assertTrue(any(p.code == "BUILD012" and "bot_version_from" in p.message for p in problems))

    def test_project_map_drift_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "BOT-EVOLUTION-ROADMAP.md").write_text("- M00 → Project 1 — Demo\n", encoding="utf-8")
            (root / "missions").mkdir()
            (root / "missions" / "M00-test.md").write_text(
                '''---\nmission_id: "M00"\nstatus: planned\nrequires_missions: []\nbot_version_from: null\nbot_version_to: "v0.0"\nknowledge:\n  required: []\nprojects:\n  contributes_to: []\n---\n''', encoding="utf-8"
            )
            problems = []
            validator.check_missions(root, set(), {"M00": "v0.0"}, problems)
            self.assertTrue(any(p.code == "BUILD013" for p in problems))

    def test_bootstrap_mission_must_name_learner_workspace(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "missions").mkdir()
            mission = root / "missions" / "M00-test.md"
            mission.write_text(
                '''---\nmission_id: "M00"\nstatus: ready\nrequires_missions: []\nbot_version_from: null\nbot_version_to: "v0.0"\nknowledge:\n  required: ["0.1"]\nprojects:\n  contributes_to: []\n---\n\n''' + ready_headings(),
                encoding="utf-8",
            )
            problems = []
            validator.check_missions(root, {"0.1"}, {"M00": "v0.0"}, problems)
            self.assertTrue(any(p.code == "BUILD011" and "learner workspace" in p.message for p in problems))

    def test_missing_bootstrap_bot_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            problems = []
            validator.check_bootstrap(Path(tmp), problems)
            self.assertTrue(any(p.code == "BUILD010" for p in problems))

    def test_learner_reference_go_directive_must_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            reference = root / "lab" / "affiliate-bot"
            learner = root / "lab" / "learner" / "affiliate-bot"
            reference.mkdir(parents=True)
            learner.mkdir(parents=True)
            (reference / "go.mod").write_text("module ref\n\ngo 1.27\n", encoding="utf-8")
            (learner / "go.mod").write_text("module learner\n\ngo 1.26\n", encoding="utf-8")
            problems = []
            validator.check_bootstrap(root, problems)
            self.assertTrue(any(p.code == "BUILD014" for p in problems))

    def test_current_m00_rejects_future_capability_leak(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            learner = root / "lab" / "learner" / "affiliate-bot" / "cmd" / "bot"
            learner.mkdir(parents=True)
            (learner / "main.go").write_text('package main\nimport "encoding/json"\n', encoding="utf-8")
            (root / "PROGRESS.md").write_text("| Current Mission (Mission hiện tại) | **M00 — Demo** |\n", encoding="utf-8")
            problems = []
            validator.check_bootstrap(root, problems)
            self.assertTrue(any(p.code == "BUILD011" and "capability ceiling" in p.message for p in problems))

    def test_language_policy_marker_is_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "LANGUAGE-POLICY.md").write_text("# Language\n", encoding="utf-8")
            problems = []
            validator.check_language_policy(root, problems)
            self.assertTrue(any(p.code == "LANG001" for p in problems))

    def test_core_authority_doc_must_reference_language_policy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "LANGUAGE-POLICY.md").write_text("Tiếng Việt là ngôn ngữ chính thức\n", encoding="utf-8")
            (root / "README.md").write_text("# Repo\n", encoding="utf-8")
            problems = []
            validator.check_language_policy(root, problems)
            self.assertTrue(any(p.code == "LANG001" and p.path == "README.md" for p in problems))


if __name__ == "__main__":
    unittest.main()
