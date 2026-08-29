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

    def test_old_pass_vocabulary_is_rejected_in_active_authority(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for rel in validator.AUTHORITY_FILES:
                path = root / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("Capability PASS / Reality verified / Operated\n", encoding="utf-8")
            (root / "CURRICULUM.md").write_text("Technical PASS + Evidence PASS\n", encoding="utf-8")
            problems = []
            validator.check_authority(root, problems)
            self.assertTrue(any(p.code == "BUILD018" and p.path == "CURRICULUM.md" for p in problems))

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
            for i in range(12):
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

    def test_dynamic_inventory_mismatch_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "CURRICULUM.md").write_text("Tổng cộng: **1 phần · 1 chương · 1 bài học**.\n", encoding="utf-8")
            (root / "ROADMAP.md").write_text("Tổng cộng: **1 phần · 1 chương · 2 bài học**.\n", encoding="utf-8")
            problems = []
            validator.check_dynamic_inventory_authority(root, problems)
            self.assertTrue(any(p.code == "BUILD015" and "lệch CURRICULUM" in p.message for p in problems))

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

    def test_ready_required_lesson_must_link_to_ready_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "roadmap").mkdir()
            (root / "roadmap" / "part-00.md").write_text(
                "- [ ] **0.1** — [Draft lesson](../lessons/0.1.md)\n", encoding="utf-8"
            )
            (root / "lessons").mkdir()
            (root / "lessons" / "0.1.md").write_text(
                '---\nlesson_id: "0.1"\nstatus: draft\n---\n', encoding="utf-8"
            )
            (root / "missions").mkdir()
            (root / "missions" / "M00-test.md").write_text(
                '''---\nmission_id: "M00"\nstatus: ready\nrequires_missions: []\nbot_version_from: null\nbot_version_to: "v0.0"\nknowledge:\n  required: ["0.1"]\nevidence:\n  minimum_level: "E1"\n  reality_required: true\nsafety_gate: "S0"\n---\n\n'''
                + ready_headings()
                + "\nlab/learner/affiliate-bot/\npublic observations\nhuman ranking trước Bot\nsample không tính Reality\n",
                encoding="utf-8",
            )
            problems = []
            validator.check_missions(root, {"0.1"}, {"M00": "v0.0"}, problems)
            self.assertTrue(any(p.code == "BUILD016" and "status=ready" in p.message for p in problems))

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

    def test_legacy_reference_must_not_claim_current_m02_m03_mapping(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            reference = root / "lab" / "affiliate-bot"
            reference.mkdir(parents=True)
            (reference / "README.md").write_text("reference for bootstrap Missions M00-M03\n", encoding="utf-8")
            problems = []
            validator.check_bootstrap(root, problems)
            self.assertTrue(any(p.code == "BUILD020" for p in problems))

    def test_current_m00_rejects_future_capability_leak(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            learner = root / "lab" / "learner" / "affiliate-bot" / "cmd" / "bot"
            learner.mkdir(parents=True)
            (learner / "main.go").write_text("package main\ntype ActionIntent struct{}\n", encoding="utf-8")
            (root / "PROGRESS.md").write_text("Current Mission: M00\n", encoding="utf-8")
            problems = []
            validator.check_bootstrap(root, problems)
            self.assertTrue(any(p.code == "BUILD011" and "capability ceiling" in p.message for p in problems))

    def test_m00_scaffold_rejects_non_nullable_numeric_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            learner = root / "lab" / "learner" / "affiliate-bot"
            (learner / "internal" / "observation").mkdir(parents=True)
            (learner / "internal" / "decision").mkdir(parents=True)
            (learner / "cmd" / "bot").mkdir(parents=True)
            (learner / "data").mkdir(parents=True)
            (learner / "internal" / "observation" / "observation.go").write_text(
                'package observation\ntype Record struct { Price float64; CommissionRate float64 }\n', encoding="utf-8"
            )
            problems = []
            validator.check_bootstrap(root, problems)
            self.assertTrue(any(p.code == "BUILD019" and "nullable" in p.message for p in problems))

    def test_m00_failure_fixture_cannot_claim_real_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = root / "lab" / "learner" / "affiliate-bot" / "data"
            data.mkdir(parents=True)
            (data / "m00-missing-input.json").write_text('[{"evidence_kind":"real"}]', encoding="utf-8")
            problems = []
            validator.check_bootstrap(root, problems)
            self.assertTrue(any(p.code == "BUILD019" and "giả nhãn real" in p.message for p in problems))

    def test_evidence_metadata_must_match_roadmap(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "ROADMAP.md").write_text("| M00 | ship | E1 |\n", encoding="utf-8")
            (root / "missions").mkdir()
            (root / "missions" / "M00-test.md").write_text(
                '''---\nmission_id: "M00"\nstatus: planned\nrequires_missions: []\nbot_version_from: null\nbot_version_to: "v0.0"\nknowledge:\n  required: []\nevidence:\n  minimum_level: "E0"\n  reality_required: false\nsafety_gate: "S0"\n---\npublic observations\nhuman rank trước Bot\nsample không tính Reality\n''',
                encoding="utf-8",
            )
            problems = []
            validator.check_missions(root, set(), {"M00": "v0.0"}, problems)
            self.assertTrue(any(p.code == "BUILD016" and "phải là E1" in p.message for p in problems))
            self.assertTrue(any(p.code == "BUILD016" and "reality_required: true" in p.message for p in problems))

    def test_m00_requires_real_evidence_and_human_before_bot(self):
        problems = []
        validator.check_mission_semantics(
            "M00",
            "sample ranking only; Bot ranks before human",
            "",
            "missions/M00.md",
            problems,
        )
        self.assertTrue(any(p.code == "BUILD017" and "human judgment" in p.message for p in problems))
        self.assertTrue(any(p.code == "BUILD017" and "sample/synthetic" in p.message for p in problems))

    def test_m03_requires_human_only_publish(self):
        problems = []
        validator.check_mission_semantics(
            "M03",
            "Bot publishes content automatically",
            '  external_side_effects: true\n  execution_actor: "bot"\n',
            "missions/M03.md",
            problems,
        )
        self.assertTrue(any(p.code == "BUILD017" and "human_only" in p.message for p in problems))
        self.assertTrue(any(p.code == "BUILD017" and "manual publish" in p.message for p in problems))

    def test_m04_requires_real_analytics_and_missing_zero_separation(self):
        problems = []
        validator.check_mission_semantics("M04", "synthetic metric demo", "", "missions/M04.md", problems)
        self.assertTrue(any(p.code == "BUILD017" and "analytics/export thật" in p.message for p in problems))

    def test_m05_requires_reviewed_outcome_improvement(self):
        problems = []
        validator.check_mission_semantics("M05", "change score until output looks good", "", "missions/M05.md", problems)
        self.assertTrue(any(p.code == "BUILD017" and "Outcome→Evaluation" in p.message for p in problems))

    def test_language_policy_marker_is_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "LANGUAGE-POLICY.md").write_text("# Language\n", encoding="utf-8")
            problems = []
            validator.check_language_policy(root, problems)
            self.assertTrue(any(p.code == "LANG001" for p in problems))

    def test_ci_authority_doc_must_reference_language_policy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "LANGUAGE-POLICY.md").write_text("Tiếng Việt là ngôn ngữ chính thức\n", encoding="utf-8")
            (root / "docs" / "CURRICULUM-CI.md").write_text("# CI\n", encoding="utf-8")
            problems = []
            validator.check_language_policy(root, problems)
            self.assertTrue(any(p.code == "LANG001" and p.path == "docs/CURRICULUM-CI.md" for p in problems))


if __name__ == "__main__":
    unittest.main()
