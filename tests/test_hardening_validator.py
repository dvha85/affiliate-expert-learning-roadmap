from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_hardening", ROOT / "scripts" / "validate_hardening.py")
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
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

    def test_missing_provenance_marker_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "sources" / "CURRICULUM-INDEX-v2026.09.md"
            path.parent.mkdir(parents=True)
            path.write_text("# incomplete index\nsource_explicit\n", encoding="utf-8")
            problems = []
            validator.check_provenance_index(root, set(), problems)
            self.assertTrue(any(p.code == "PROV005" for p in problems))

    def test_wrong_project_part_is_rejected(self):
        locations = {project: [part] for project, part in validator.EXPECTED_PROJECT_PART.items()}
        locations[10] = [16]
        problems = []
        validator.check_projects(locations, problems)
        self.assertTrue(any(p.code == "PROJECT002" for p in problems))


if __name__ == "__main__":
    unittest.main()
