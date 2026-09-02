#!/usr/bin/env python3
"""Guard evidence-origin/use-context semantics and the M00 real-evidence example."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Problem:
    code: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.code} {self.path}: {self.message}"


BUILD_FIRST = Path("BUILD-FIRST.md")
LESSON_02 = Path("lessons/part-00/chapter-00/0.2-sample-real-fact-estimate-assumption-unknown.md")

BUILD_REQUIRED = {
    "origin / eligibility: real | synthetic",
    "use context khi relevant: test | replay",
    "`evidence_kind: real | synthetic` khi contract M00 áp dụng",
    "Không ép `real | synthetic | test | replay` thành bốn giá trị loại trừ trên cùng một enum.",
}

BUILD_FORBIDDEN = {
    "Mỗi evidence phải ghi rõ `real`, `test`, `synthetic` hoặc `replay`.",
    "`evidence_kind: real | test | synthetic | replay`;",
}

LESSON_REQUIRED = {
    "nó **không phải E1 evidence**",
    'source_url: "<URL công khai bạn thực sự vừa quan sát>"',
    "Nếu đây chỉ là ví dụ/fixture được dựng để học hoặc test, phải giữ nó là `synthetic`.",
    "M00 hiện chỉ serialize:",
    "evidence_kind: real | synthetic",
}

LESSON_FORBIDDEN = {
    "source_url: https://example.com/product-x",
}


def check_file(
    root: Path,
    rel: Path,
    required: set[str],
    forbidden: set[str],
    problems: list[Problem],
) -> None:
    path = root / rel
    if not path.exists():
        problems.append(Problem("ETAX001", str(rel), "thiếu file bắt buộc"))
        return
    text = path.read_text(encoding="utf-8")
    for marker in sorted(required):
        if marker not in text:
            problems.append(Problem("ETAX002", str(rel), f"thiếu semantic marker {marker!r}"))
    for marker in sorted(forbidden):
        if marker in text:
            problems.append(Problem("ETAX003", str(rel), f"semantic regression quay lại: {marker!r}"))


def validate(root: Path) -> list[Problem]:
    root = root.resolve()
    problems: list[Problem] = []
    check_file(root, BUILD_FIRST, BUILD_REQUIRED, BUILD_FORBIDDEN, problems)
    check_file(root, LESSON_02, LESSON_REQUIRED, LESSON_FORBIDDEN, problems)
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Kiểm evidence taxonomy origin/use-context consistency")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    problems = validate(args.root)
    if problems:
        print(f"EVIDENCE TAXONOMY CI: FAIL ({len(problems)} problem(s))")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print("EVIDENCE TAXONOMY CI: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
