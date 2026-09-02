from __future__ import annotations

import tempfile
import unittest
import subprocess
import sys
from pathlib import Path

from scripts.validate_privacy_boundary import REQUIRED_FILES, validate


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_privacy_boundary.py"


class PrivacyBoundaryValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for rel in REQUIRED_FILES:
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Resource\n", encoding="utf-8")
        (self.root / ".gitignore").write_text(
            ".env\nworkspace/\nworkspace/artifacts/local/\nworkspace/artifacts/private/\nworkspace/artifacts/missions/*/private/\nworkspace/artifacts/missions/*/raw/\nlab/learner/affiliate-bot/data/local/\nraw-analytics/\nprivate-exports/\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_valid_fixture_passes(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_ignore_marker_fails(self):
        (self.root / ".gitignore").write_text(".env\n", encoding="utf-8")
        self.assertTrue(any(problem.code == "PRIV002" for problem in validate(self.root)))

    def test_plaintext_secret_in_artifact_fails(self):
        artifact = self.root / "artifacts" / "missions" / "M00" / "notes.md"
        artifact.parent.mkdir(parents=True)
        artifact.write_text("api_key: abc123\n", encoding="utf-8")
        self.assertTrue(any(problem.code == "PRIV003" for problem in validate(self.root)))

    def test_cli_valid_fixture_passes(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.root)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PRIVACY BOUNDARY: PASS", result.stdout)

    def test_cli_missing_repository_fails(self):
        missing = self.root / "missing-repository"
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(missing)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("PRIVACY BOUNDARY: FAIL", result.stdout)
