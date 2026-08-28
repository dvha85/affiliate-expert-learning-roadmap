from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_curriculum import validate


class CurriculumValidatorMutationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.make_valid_fixture()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write(self, rel: str, content: str) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def lesson(self, lesson_id: str, status: str, title: str) -> str:
        return f'''---
lesson_id: "{lesson_id}"
title: "{title}"
part: 0
chapter: 0
effort: M
estimated_minutes: 60
status: {status}
prerequisites: []
source_refs:
  canonical:
    - "S:P0/C0/L{lesson_id}"
  training: []
  research: []
  external: []
last_verified: null
---

# Bài {lesson_id} — {title}

## 1. Mục tiêu

Nội dung kiểm thử.
'''

    def make_valid_fixture(self) -> None:
        self.write("ROADMAP.md", '''# Roadmap tổng

Tổng cộng: **1 phần · 1 chương · 2 bài học**.

| Phần | Trọng tâm | Chương | Bài | Trạng thái |
|---|---|---:|---:|---|
| [Phần 0](roadmap/part-00.md) | TEST | 0 | 2 | ⬜ |
''')
        self.write("roadmap/part-00.md", '''# Phần 0 — TEST

- Timeline: **Standard M1 · Accelerated M1** — forecast; PASS evidence mới là gate.

### Chương 0 — Test chapter

- [ ] **0.1** — [Ready lesson](../lessons/part-00/chapter-00/0.1-ready-lesson.md)
- [ ] **0.2** — Planned lesson
''')
        self.write("lessons/part-00/chapter-00/0.1-ready-lesson.md", self.lesson("0.1", "ready", "Ready lesson"))
        self.write("lessons/part-00/chapter-00/0.2-planned-lesson.md", self.lesson("0.2", "planned", "Planned lesson"))

    def codes(self) -> set[str]:
        return {p.code for p in validate(self.root)}

    def test_valid_fixture_passes(self) -> None:
        self.assertEqual([], validate(self.root))

    def test_broken_relative_link_fails(self) -> None:
        self.write("docs/broken.md", "# Broken\n\n[missing](not-there.md)\n")
        self.assertIn("LINK001", self.codes())

    def test_root_markdown_link_is_checked(self) -> None:
        self.write("CONTRIBUTING.md", "# Contributing\n\n[missing](missing-root-target.md)\n")
        self.assertIn("LINK001", self.codes())

    def test_source_markdown_link_is_checked(self) -> None:
        self.write("sources/README.md", "# Sources\n\n[missing](missing-source.md)\n")
        self.assertIn("LINK001", self.codes())

    def test_count_mismatch_fails(self) -> None:
        roadmap = (self.root / "ROADMAP.md").read_text(encoding="utf-8").replace("| 0 | 2 |", "| 0 | 3 |")
        self.write("ROADMAP.md", roadmap)
        self.assertIn("COUNT002", self.codes())

    def test_duplicate_lesson_id_fails(self) -> None:
        part = (self.root / "roadmap/part-00.md").read_text(encoding="utf-8") + "\n- [ ] **0.1** — Duplicate\n"
        self.write("roadmap/part-00.md", part)
        self.assertIn("ID001", self.codes())

    def test_missing_metadata_fails(self) -> None:
        content = self.lesson("0.2", "planned", "Planned lesson").replace("effort: M\n", "")
        self.write("lessons/part-00/chapter-00/0.2-planned-lesson.md", content)
        self.assertIn("META002", self.codes())

    def test_missing_normalized_timeline_fails(self) -> None:
        part = (self.root / "roadmap/part-00.md").read_text(encoding="utf-8").replace(
            "- Timeline: **Standard M1 · Accelerated M1** — forecast; PASS evidence mới là gate.\n\n", ""
        )
        self.write("roadmap/part-00.md", part)
        self.assertIn("TIME001", self.codes())

    def test_external_ref_requires_last_verified(self) -> None:
        content = self.lesson("0.2", "planned", "Planned lesson").replace(
            "  external: []\nlast_verified: null",
            '  external:\n    - "EXT:TEST:CURRENT"\nlast_verified: null',
        )
        self.write("lessons/part-00/chapter-00/0.2-planned-lesson.md", content)
        self.assertIn("FRESH001", self.codes())

    def test_last_verified_requires_external_ref(self) -> None:
        content = self.lesson("0.2", "planned", "Planned lesson").replace(
            "last_verified: null", 'last_verified: "2026-08-28"'
        )
        self.write("lessons/part-00/chapter-00/0.2-planned-lesson.md", content)
        self.assertIn("FRESH002", self.codes())

    def test_last_verified_requires_iso_date(self) -> None:
        content = self.lesson("0.2", "planned", "Planned lesson").replace(
            "  external: []\nlast_verified: null",
            '  external:\n    - "EXT:TEST:CURRENT"\nlast_verified: "28/08/2026"',
        )
        self.write("lessons/part-00/chapter-00/0.2-planned-lesson.md", content)
        self.assertIn("FRESH003", self.codes())


if __name__ == "__main__":
    unittest.main()
