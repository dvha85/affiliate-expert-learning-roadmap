#!/usr/bin/env python3
"""Kiểm các điểm neo tối thiểu của quy ước ngôn ngữ tiếng Việt.

Validator này cố ý không tự động phán đoán ngôn ngữ tự nhiên của toàn bộ prose.
Nó chỉ ngăn các regression dễ nhận biết: mất style guide, mất liên kết quy ước,
hoặc quay lại một số heading tiếng Anh đã từng xuất hiện trong learner-facing docs.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
STYLE = ROOT / "docs" / "VIETNAMESE-LANGUAGE-STYLE.md"

REQUIRED_LINKS = {
    ROOT / "README.md": "docs/VIETNAMESE-LANGUAGE-STYLE.md",
    ROOT / "CURRICULUM.md": "docs/VIETNAMESE-LANGUAGE-STYLE.md",
    ROOT / "CONTRIBUTING.md": "docs/VIETNAMESE-LANGUAGE-STYLE.md",
}

LEARNER_FACING = [
    ROOT / "README.md",
    ROOT / "CURRICULUM.md",
    ROOT / "lab" / "learner" / "affiliate-bot" / "README.md",
    ROOT / "docs" / "AFFILIATE-INTELLIGENCE-DECISION-CONTRACT.md",
    ROOT / "docs" / "BOT-EVOLUTION-ROADMAP.md",
    ROOT / "docs" / "12-MONTH-PLAN.md",
    ROOT / "docs" / "15-MONTH-PLAN.md",
    ROOT / "docs" / "AFFILIATE-METRIC-REVENUE-SPINE.md",
    ROOT / "docs" / "EFFORT-MODEL.md",
    ROOT / "docs" / "MANUAL-AFFILIATE-LOOP.md",
    ROOT / "sources" / "README.md",
]

FORBIDDEN_HEADINGS = {
    "## Active authority hiện tại",
    "## Mission spine",
    "## Affiliate Intelligence spine",
    "## Early-loop target",
    "## Planning bands",
    "## Mission bands",
    "## Calendar use",
    "## Suggested reforecast checkpoints",
    "## Canonical funnel",
    "## Minimum revenue model",
    "## Derived metrics",
    "## Mission progression",
    "## Bottleneck diagnosis",
    "## Revenue truth states",
    "## Definition of integrity",
    "## Separation of authority",
    "## Early-mission partial output",
}


def main() -> int:
    problems: list[str] = []

    if not STYLE.exists():
        problems.append("LANG001 docs/VIETNAMESE-LANGUAGE-STYLE.md: thiếu style guide tiếng Việt")

    for path, marker in REQUIRED_LINKS.items():
        if not path.exists():
            problems.append(f"LANG002 {path.relative_to(ROOT)}: thiếu file bắt buộc")
            continue
        text = path.read_text(encoding="utf-8")
        if marker not in text:
            problems.append(
                f"LANG003 {path.relative_to(ROOT)}: phải liên kết tới quy ước ngôn ngữ"
            )

    for path in LEARNER_FACING:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in FORBIDDEN_HEADINGS:
            if heading in text:
                problems.append(
                    f"LANG004 {path.relative_to(ROOT)}: heading tiếng Anh cũ quay lại: {heading!r}"
                )

    if problems:
        print("Kiểm tra quy ước ngôn ngữ thất bại:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("Kiểm tra quy ước ngôn ngữ đạt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
