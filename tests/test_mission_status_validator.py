from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_mission_status import validate


class MissionStatusValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.write(
            "CURRICULUM.md",
            """# Curriculum\n\n| Mission | Mục tiêu |\n|---|---|\n| M00 — First | target |\n| M01 — Second | target |\n""",
        )
        self.write(
            "missions/README.md",
            """# Missions\n\n| Mission | Outcome | Authoring |\n|---|---|---|\n| [M00](M00-first.md) | First | ready |\n| M01 | Second | planned |\n""",
        )
        self.write(
            "missions/M00-first.md",
            """---\nmission_id: \"M00\"\nstatus: ready\n---\n\n# M00\n""",
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write(self, rel: str, content: str) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def codes(self) -> set[str]:
        return {problem.code for problem in validate(self.root)}

    def test_valid_projection_passes(self) -> None:
        self.assertEqual([], validate(self.root))

    def test_readme_status_must_match_front_matter(self) -> None:
        readme = (self.root / "missions/README.md").read_text(encoding="utf-8").replace(
            "| [M00](M00-first.md) | First | ready |",
            "| [M00](M00-first.md) | First | draft |",
        )
        self.write("missions/README.md", readme)
        self.assertIn("MSTATE016", self.codes())

    def test_canonical_mission_requires_readme_row(self) -> None:
        readme = (self.root / "missions/README.md").read_text(encoding="utf-8").replace(
            "| M01 | Second | planned |\n", ""
        )
        self.write("missions/README.md", readme)
        self.assertIn("MSTATE013", self.codes())

    def test_filename_must_match_mission_id(self) -> None:
        self.write(
            "missions/M01-wrong.md",
            """---\nmission_id: \"M00\"\nstatus: ready\n---\n\n# Wrong\n""",
        )
        self.assertIn("MSTATE009", self.codes())


if __name__ == "__main__":
    unittest.main()
