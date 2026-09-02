from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.init_learner_workspace import FILES, initialize
from scripts.migrate_curriculum_v1_to_v2 import report


class MigrationAndWorkspaceTests(unittest.TestCase):
    def test_migration_report_is_dry_run_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs/CURRICULUM-MIGRATION-v2.md").write_text("# guide\n", encoding="utf-8")
            output = report(root)
            self.assertIn("DRY RUN ONLY", output)
            self.assertFalse((root / "workspace").exists())

    def test_workspace_initializer_creates_only_missing_local_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "workspace"
            created = initialize(root)
            self.assertEqual({path.relative_to(root).as_posix() for path in created}, set(FILES))
            progress = root / "PROGRESS.md"
            progress.write_text("keep me", encoding="utf-8")
            self.assertNotIn(progress, initialize(root))
            self.assertEqual(progress.read_text(encoding="utf-8"), "keep me")
