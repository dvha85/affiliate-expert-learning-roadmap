#!/usr/bin/env python3
"""Fail if historical sources regain active curriculum authority."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    required = {
        ROOT / "CURRICULUM.md": ["Active canonical curriculum", "Mission spine"],
        ROOT / "sources" / "README.md": ["historical/research archive", "CURRICULUM.md"],
        ROOT / "sources" / "SYLLABUS-v2026.09.md": ["HISTORICAL ONLY", "KHÔNG CÒN LÀ NGUỒN CHUẨN"],
        ROOT / "sources" / "CURRICULUM-INDEX-v2026.09.md": ["HISTORICAL ONLY"],
    }

    problems: list[str] = []
    for path, markers in required.items():
        if not path.exists():
            problems.append(f"missing: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                problems.append(f"{path.relative_to(ROOT)} missing authority marker: {marker}")

    historical = [
        ROOT / "sources" / "SYLLABUS-v2026.09.md",
        ROOT / "sources" / "CURRICULUM-INDEX-v2026.09.md",
    ]
    forbidden = ["Active canonical revision", "active canonical manifest"]
    for path in historical:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in forbidden:
            if phrase in text:
                problems.append(f"{path.relative_to(ROOT)} reclaims active authority via: {phrase}")

    if problems:
        print("Canonical authority validation: FAIL")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("Canonical authority validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
