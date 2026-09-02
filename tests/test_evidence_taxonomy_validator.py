from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_evidence_taxonomy import validate


class EvidenceTaxonomyValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.write(
            "BUILD-FIRST.md",
            """origin / eligibility: real | synthetic\nuse context khi relevant: test | replay\nKhông ép `real | synthetic | test | replay` thành bốn giá trị loại trừ trên cùng một enum.\n`evidence_kind: real | synthetic` khi contract M00 áp dụng\n""",
        )
        self.write(
            "lessons/part-00/chapter-00/0.2-sample-real-fact-estimate-assumption-unknown.md",
            """nó **không phải E1 evidence**\nsource_url: \"<URL công khai bạn thực sự vừa quan sát>\"\nNếu đây chỉ là ví dụ/fixture được dựng để học hoặc test, phải giữ nó là `synthetic`.\nM00 hiện chỉ serialize:\nevidence_kind: real | synthetic\n""",
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write(self, rel: str, content: str) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def codes(self) -> set[str]:
        return {problem.code for problem in validate(self.root)}

    def test_valid_semantics_pass(self) -> None:
        self.assertEqual([], validate(self.root))

    def test_old_single_axis_enum_fails(self) -> None:
        build = (self.root / "BUILD-FIRST.md").read_text(encoding="utf-8")
        build += "\n`evidence_kind: real | test | synthetic | replay`;\n"
        self.write("BUILD-FIRST.md", build)
        self.assertIn("ETAX003", self.codes())

    def test_placeholder_real_url_fails(self) -> None:
        path = "lessons/part-00/chapter-00/0.2-sample-real-fact-estimate-assumption-unknown.md"
        lesson = (self.root / path).read_text(encoding="utf-8")
        lesson += "\nsource_url: https://example.com/product-x\n"
        self.write(path, lesson)
        self.assertIn("ETAX003", self.codes())

    def test_missing_m00_serialized_contract_fails(self) -> None:
        path = "lessons/part-00/chapter-00/0.2-sample-real-fact-estimate-assumption-unknown.md"
        lesson = (self.root / path).read_text(encoding="utf-8").replace(
            "evidence_kind: real | synthetic", "evidence_kind: something-else"
        )
        self.write(path, lesson)
        self.assertIn("ETAX002", self.codes())


if __name__ == "__main__":
    unittest.main()
