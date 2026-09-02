from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_vietnamese_headings import validate


class VietnameseHeadingValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.write("roadmap/part-00.md", "# Phần 0 — Quyết định đầu tiên dựa trên bằng chứng\n")
        self.write("roadmap/part-01.md", "# Phần 1 — Dữ liệu đáng tin cậy và AI có căn cứ bằng chứng\n")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write(self, rel: str, content: str) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def codes(self) -> set[str]:
        return {problem.code for problem in validate(self.root)}

    def test_vietnamese_first_titles_pass(self) -> None:
        self.assertEqual([], validate(self.root))

    def test_all_caps_english_part_title_fails(self) -> None:
        self.write("roadmap/part-00.md", "# Phần 0 — FIRST EVIDENCE-BACKED DECISION\n")
        self.assertIn("VHEAD003", self.codes())

    def test_mixed_technical_terms_are_not_banned(self) -> None:
        self.write("roadmap/part-00.md", "# Phần 0 — Tool Agent và tự động hóa Hybrid có quản trị\n")
        self.assertNotIn("VHEAD003", self.codes())


if __name__ == "__main__":
    unittest.main()
