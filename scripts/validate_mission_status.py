#!/usr/bin/env python3
"""Validate Mission authoring-state projections against canonical Mission front matter.

Mission front matter is the source of truth for authored Mission status. The Mission
spine in missions/README.md is a human-readable projection and must not drift.
Canonical Mission IDs are derived from CURRICULUM.md rather than hard-coded here.
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

FRONT_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
MISSION_ID_RE = re.compile(r"(?m)^mission_id:\s*[\"']?(M\d{2})[\"']?\s*$")
STATUS_RE = re.compile(r"(?m)^status:\s*[\"']?([A-Za-z_-]+)[\"']?\s*$")
CANONICAL_MISSION_RE = re.compile(r"(?m)^\|\s*(M\d{2})\s+—")
README_MISSION_RE = re.compile(r"\b(M\d{2})\b")
FILE_MISSION_RE = re.compile(r"^(M\d{2})-")
ALLOWED_STATUS = {"planned", "draft", "ready"}


@dataclass(frozen=True)
class Problem:
    code: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.code} {self.path}: {self.message}"


def canonical_mission_ids(root: Path, problems: list[Problem]) -> list[str]:
    path = root / "CURRICULUM.md"
    if not path.exists():
        problems.append(Problem("MSTATE001", "CURRICULUM.md", "thiếu canonical curriculum"))
        return []
    ids = CANONICAL_MISSION_RE.findall(path.read_text(encoding="utf-8"))
    if not ids:
        problems.append(Problem("MSTATE002", "CURRICULUM.md", "không tìm thấy Mission spine canonical"))
        return []
    if len(ids) != len(set(ids)):
        problems.append(Problem("MSTATE003", "CURRICULUM.md", "Mission ID bị lặp trong canonical Mission spine"))
    return list(dict.fromkeys(ids))


def read_readme_statuses(root: Path, problems: list[Problem]) -> dict[str, str]:
    path = root / "missions" / "README.md"
    if not path.exists():
        problems.append(Problem("MSTATE004", "missions/README.md", "thiếu Mission index"))
        return {}

    statuses: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.startswith("|"):
            continue
        cells = [cell.strip() for cell in raw.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        match = README_MISSION_RE.search(cells[0])
        if not match:
            continue
        mission_id = match.group(1)
        status = cells[-1].strip().lower()
        if status not in ALLOWED_STATUS:
            problems.append(
                Problem("MSTATE005", "missions/README.md", f"{mission_id} có authoring status không hợp lệ: {status!r}")
            )
            continue
        if mission_id in statuses:
            problems.append(Problem("MSTATE006", "missions/README.md", f"{mission_id} xuất hiện nhiều lần"))
            continue
        statuses[mission_id] = status
    return statuses


def read_front_matter_statuses(root: Path, problems: list[Problem]) -> dict[str, tuple[str, Path]]:
    statuses: dict[str, tuple[str, Path]] = {}
    folder = root / "missions"
    if not folder.exists():
        return statuses

    for path in sorted(folder.glob("M??-*.md")):
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        front = FRONT_RE.match(text)
        if not front:
            problems.append(Problem("MSTATE007", str(rel), "Mission file thiếu front matter"))
            continue
        raw = front.group(1)
        id_match = MISSION_ID_RE.search(raw)
        status_match = STATUS_RE.search(raw)
        if not id_match:
            problems.append(Problem("MSTATE008", str(rel), "Mission front matter thiếu mission_id"))
            continue
        mission_id = id_match.group(1)
        file_match = FILE_MISSION_RE.match(path.name)
        if not file_match or file_match.group(1) != mission_id:
            problems.append(
                Problem("MSTATE009", str(rel), f"mission_id={mission_id} không khớp tên file")
            )
        if not status_match:
            problems.append(Problem("MSTATE010", str(rel), "Mission front matter thiếu status"))
            continue
        status = status_match.group(1).lower()
        if status not in ALLOWED_STATUS:
            problems.append(Problem("MSTATE011", str(rel), f"status không hợp lệ: {status!r}"))
            continue
        if mission_id in statuses:
            problems.append(Problem("MSTATE012", str(rel), f"Mission file trùng mission_id {mission_id}"))
            continue
        statuses[mission_id] = (status, rel)
    return statuses


def validate(root: Path) -> list[Problem]:
    root = root.resolve()
    problems: list[Problem] = []
    canonical_ids = canonical_mission_ids(root, problems)
    readme_statuses = read_readme_statuses(root, problems)
    file_statuses = read_front_matter_statuses(root, problems)

    canonical_set = set(canonical_ids)
    readme_set = set(readme_statuses)
    for mission_id in canonical_ids:
        if mission_id not in readme_statuses:
            problems.append(Problem("MSTATE013", "missions/README.md", f"thiếu row cho {mission_id}"))
    for mission_id in sorted(readme_set - canonical_set):
        problems.append(Problem("MSTATE014", "missions/README.md", f"{mission_id} không tồn tại trong canonical Mission spine"))

    for mission_id, (front_status, rel) in sorted(file_statuses.items()):
        if mission_id not in canonical_set:
            problems.append(Problem("MSTATE015", str(rel), f"{mission_id} không tồn tại trong canonical Mission spine"))
            continue
        projected = readme_statuses.get(mission_id)
        if projected is not None and projected != front_status:
            problems.append(
                Problem(
                    "MSTATE016",
                    "missions/README.md",
                    f"{mission_id} projection={projected!r} nhưng front matter={front_status!r} ở {rel}",
                )
            )

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Kiểm tra Mission authoring-state consistency")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    problems = validate(args.root)
    if problems:
        print(f"MISSION STATUS CI: FAIL ({len(problems)} problem(s))")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print("MISSION STATUS CI: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
