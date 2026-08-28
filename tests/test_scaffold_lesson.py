import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "scaffold_lesson.py"


class ScaffoldLessonRegressionTests(unittest.TestCase):
    def run_scaffold(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_dry_run_existing_scaffold_is_non_fatal(self) -> None:
        result = self.run_scaffold("--lesson", "0.2", "--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("EXISTS 0.2:", result.stdout)
        self.assertIn("would not overwrite", result.stdout)

    def test_actual_write_still_refuses_existing_scaffold(self) -> None:
        result = self.run_scaffold("--lesson", "0.2")
        self.assertEqual(result.returncode, 3)
        self.assertIn("refusing to overwrite", result.stderr)


if __name__ == "__main__":
    unittest.main()
