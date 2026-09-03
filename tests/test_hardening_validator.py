from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_hardening", ROOT / "scripts" / "validate_hardening.py")
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


class HardeningValidatorTests(unittest.TestCase):
    def test_current_repo_passes(self):
        problems = validator.validate(ROOT)
        self.assertEqual([], problems, "\n".join(str(p) for p in problems))

    def test_unknown_external_ref_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "lessons" / "part-00").mkdir(parents=True)
            for rel in validator.REGISTER_PATHS:
                path = root / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("# Register\n## EXT:KNOWN:SOURCE\n", encoding="utf-8")
            lesson = root / "lessons" / "part-00" / "x.md"
            lesson.write_text("source_refs:\n  external:\n    - EXT:UNKNOWN:SOURCE\n", encoding="utf-8")
            problems = []
            ids = validator.collect_registry_ids(root, problems)
            validator.check_external_refs(root, ids, problems)
            self.assertTrue(any(p.code == "FRESH004" for p in problems))

    def test_current_affiliate_register_rejects_legacy_part_mapping(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "docs" / "AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md"
            path.parent.mkdir(parents=True)
            path.write_text("CURRICULUM.md\nMaps to: P22/C87\n", encoding="utf-8")
            problems = []
            validator.check_active_register_mapping(root, problems)
            self.assertTrue(any(p.code == "STALE002" for p in problems))

    def test_missing_canonical_model_marker_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "CURRICULUM.md").write_text(
                "# Curriculum\nMission spine\nReal Evidence Ladder\n",
                encoding="utf-8",
            )
            problems = []
            validator.check_canonical_model(root, problems)
            self.assertTrue(any(p.code == "AUTH003" and "Reference knowledge inventory" in p.message for p in problems))

    def test_duplicate_active_lesson_id_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            part = root / "roadmap" / "part-00.md"
            part.parent.mkdir(parents=True)
            part.write_text(
                "### Chương 0 — Demo\n- [ ] **0.1** — One\n- [ ] **0.1** — Duplicate\n",
                encoding="utf-8",
            )
            problems = []
            validator.collect_roadmap_inventory(root, problems)
            self.assertTrue(any(p.code == "PROV003" for p in problems))

    def test_duplicate_active_chapter_id_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            roadmap = root / "roadmap"
            roadmap.mkdir()
            (roadmap / "part-00.md").write_text("### Chương 0 — One\n", encoding="utf-8")
            (roadmap / "part-01.md").write_text("### Chương 0 — Duplicate\n", encoding="utf-8")
            problems = []
            validator.collect_roadmap_inventory(root, problems)
            self.assertTrue(any(p.code == "PROV004" for p in problems))

    def test_active_authority_doc_must_link_root_canonical(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# README\n", encoding="utf-8")
            problems = []
            validator.check_authority_docs(root, problems)
            self.assertTrue(any(p.code == "AUTH001" and p.path == "README.md" and "CURRICULUM.md" in p.message for p in problems))

    def test_stale_active_inventory_reference_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("Active inventory\nParts: 23\nChapters: 89\nLessons: 671\n", encoding="utf-8")
            problems = []
            validator.check_stale_active_references(root, problems)
            self.assertTrue(any(p.code == "STALE001" and p.path == "README.md" for p in problems))

    def test_sources_are_ignored_by_stale_active_guard(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "sources" / "README.md"
            source.parent.mkdir()
            source.write_text("Historical inventory: 23 Parts / 89 Chapters / 671 Lessons.\n", encoding="utf-8")
            problems = []
            validator.check_stale_active_references(root, problems)
            self.assertEqual([], problems)

    def test_explicit_historical_comparison_is_not_stale(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "CURRICULUM.md").write_text(
                "Curriculum này thay thế cấu trúc cũ 23 Parts / 89 Chapters / 671 Lessons.\n",
                encoding="utf-8",
            )
            problems = []
            validator.check_stale_active_references(root, problems)
            self.assertEqual([], problems)

    def test_allowlisted_historical_doc_is_ignored_by_stale_guard(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rel = Path("docs/ADR-001-GO-FIRST-BOT-STACK.md")
            path = root / rel
            path.parent.mkdir(parents=True)
            path.write_text("Historical inventory: 23 Parts / 89 Chapters / 671 Lessons.\n", encoding="utf-8")
            problems = []
            validator.check_stale_active_references(root, problems)
            self.assertEqual([], problems)


if __name__ == "__main__":
    unittest.main()
