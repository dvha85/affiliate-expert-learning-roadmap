#!/usr/bin/env python3
"""Validate explicit Mission delivery/readiness metadata.

Authoring state (planned/draft/ready) is intentionally distinct from delivery
readiness.  This guard makes missing starters, eval packs and pilot evidence
visible during the v1 -> v2 migration without turning historical material into
a false release claim.
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

FRONT_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
MISSION_ID_RE = re.compile(r'(?m)^mission_id:\s*["\']?(M\d{2})["\']?\s*$')
STATUS_RE = re.compile(r'(?m)^status:\s*["\']?([A-Za-z_-]+)["\']?\s*$')
VERSION_RE = re.compile(r'(?m)^curriculum_version:\s*(\d+)\s*$')
KIND_RE = re.compile(r'(?m)^release_kind:\s*["\']?([A-Za-z_]+)["\']?\s*$')
DELIVERY_RE = re.compile(r'(?ms)^delivery:\s*\n((?:^[ \t]+.*(?:\n|$))*)')
DELIVERY_KEY_RE = re.compile(r'(?m)^  ([A-Za-z_]+):(?:\s*(.*))?$')
LIST_ITEM_RE = re.compile(r'^    -\s*["\']?(.*?)["\']?\s*$')

ALLOWED_KINDS = {"market_artifact", "bot"}
ALLOWED_PILOT_STATES = {"untested", "validated"}
DELIVERY_KEYS = {
    "starter_paths",
    "eval_pack",
    "verification_commands",
    "pilot_status",
    "pilot_evidence_refs",
}


@dataclass(frozen=True)
class Problem:
    code: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.code} {self.path}: {self.message}"


@dataclass(frozen=True)
class Readiness:
    mission_id: str
    path: Path
    status: str
    curriculum_version: int
    release_kind: str
    starter_paths: tuple[str, ...]
    eval_pack: str | None
    verification_commands: tuple[str, ...]
    pilot_status: str
    pilot_evidence_refs: tuple[str, ...]

    @property
    def delivery_complete(self) -> bool:
        return bool(self.starter_paths and self.eval_pack and self.verification_commands)


def quoted_or_null(value: str) -> str | None:
    value = value.strip()
    if value in {"", "null", "Null", "NULL", "~"}:
        return None
    return value.strip('"\'')


def parse_delivery(raw: str) -> tuple[dict[str, object], list[str]]:
    """Parse the intentionally small YAML subset used by Mission front matter."""
    values: dict[str, object] = {}
    errors: list[str] = []
    current: str | None = None
    for line in raw.splitlines():
        key_match = DELIVERY_KEY_RE.match(line)
        if key_match:
            current = key_match.group(1)
            inline = key_match.group(2).strip()
            if inline == "[]":
                values[current] = []
            elif inline:
                values[current] = quoted_or_null(inline)
            else:
                values[current] = []
            continue
        item_match = LIST_ITEM_RE.match(line)
        if item_match and current:
            existing = values.get(current)
            if not isinstance(existing, list):
                errors.append(f"{current} không thể vừa scalar vừa list")
                continue
            existing.append(item_match.group(1).strip('"\''))
    return values, errors


def parse_mission(root: Path, path: Path, problems: list[Problem]) -> Readiness | None:
    rel = path.relative_to(root)
    front_match = FRONT_RE.match(path.read_text(encoding="utf-8"))
    if not front_match:
        problems.append(Problem("READY001", str(rel), "thiếu YAML front matter"))
        return None
    front = front_match.group(1)
    id_match = MISSION_ID_RE.search(front)
    status_match = STATUS_RE.search(front)
    version_match = VERSION_RE.search(front)
    kind_match = KIND_RE.search(front)
    delivery_match = DELIVERY_RE.search(front)
    if not id_match:
        problems.append(Problem("READY002", str(rel), "thiếu mission_id"))
        return None
    mission_id = id_match.group(1)
    if not status_match:
        problems.append(Problem("READY002", str(rel), "thiếu status"))
    if not version_match or int(version_match.group(1)) < 1:
        problems.append(Problem("READY003", str(rel), "curriculum_version phải là số nguyên dương"))
    if not kind_match or kind_match.group(1) not in ALLOWED_KINDS:
        problems.append(Problem("READY004", str(rel), "release_kind phải là market_artifact hoặc bot"))
    if not delivery_match:
        problems.append(Problem("READY005", str(rel), "thiếu delivery metadata"))
        return None
    delivery, parse_errors = parse_delivery(delivery_match.group(1))
    for error in parse_errors:
        problems.append(Problem("READY006", str(rel), error))
    missing = sorted(DELIVERY_KEYS - set(delivery))
    if missing:
        problems.append(Problem("READY007", str(rel), f"delivery thiếu field: {', '.join(missing)}"))
        return None

    starter_paths = delivery["starter_paths"]
    commands = delivery["verification_commands"]
    evidence_refs = delivery["pilot_evidence_refs"]
    if not all(isinstance(item, str) and item for item in starter_paths):
        problems.append(Problem("READY008", str(rel), "starter_paths phải là list string không rỗng"))
    if not all(isinstance(item, str) and item for item in commands):
        problems.append(Problem("READY008", str(rel), "verification_commands phải là list string không rỗng"))
    if not all(isinstance(item, str) and item for item in evidence_refs):
        problems.append(Problem("READY008", str(rel), "pilot_evidence_refs phải là list string không rỗng"))
    pilot_status = delivery["pilot_status"]
    if not isinstance(pilot_status, str) or pilot_status not in ALLOWED_PILOT_STATES:
        problems.append(Problem("READY009", str(rel), "pilot_status phải là untested hoặc validated"))
    eval_pack = delivery["eval_pack"]
    if eval_pack is not None and not isinstance(eval_pack, str):
        problems.append(Problem("READY010", str(rel), "eval_pack phải là path hoặc null"))

    for declared in starter_paths:
        candidate = root / declared
        if not candidate.exists():
            problems.append(Problem("READY011", str(rel), f"starter path không tồn tại: {declared}"))
    if isinstance(eval_pack, str) and not (root / eval_pack).exists():
        problems.append(Problem("READY012", str(rel), f"eval_pack không tồn tại: {eval_pack}"))
    if pilot_status == "validated" and not evidence_refs:
        problems.append(Problem("READY013", str(rel), "pilot validated phải có pilot_evidence_refs"))

    if problems and any(problem.path == str(rel) for problem in problems):
        return None
    return Readiness(
        mission_id=mission_id,
        path=rel,
        status=status_match.group(1) if status_match else "unknown",
        curriculum_version=int(version_match.group(1)),
        release_kind=kind_match.group(1),
        starter_paths=tuple(starter_paths),
        eval_pack=eval_pack,
        verification_commands=tuple(commands),
        pilot_status=pilot_status,
        pilot_evidence_refs=tuple(evidence_refs),
    )


def collect(root: Path) -> tuple[list[Readiness], list[Problem]]:
    problems: list[Problem] = []
    records: list[Readiness] = []
    for path in sorted((root / "missions").glob("M??-*.md")):
        record = parse_mission(root, path, problems)
        if record:
            records.append(record)
    return records, problems


def validate(root: Path, strict: bool = False) -> list[Problem]:
    records, problems = collect(root.resolve())
    if strict:
        for record in records:
            if record.status == "ready" and not record.delivery_complete:
                problems.append(
                    Problem(
                        "READY014",
                        str(record.path),
                        "status=ready nhưng chưa có starter + eval_pack + verification_commands",
                    )
                )
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Kiểm readiness metadata của Mission")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--strict", action="store_true", help="fail nếu Mission ready chưa đủ delivery bundle")
    args = parser.parse_args()
    records, problems = collect(args.root.resolve())
    if args.strict:
        for record in records:
            if record.status == "ready" and not record.delivery_complete:
                problems.append(Problem("READY014", str(record.path), "status=ready nhưng chưa có starter + eval_pack + verification_commands"))
    if problems:
        print(f"READINESS METADATA: FAIL ({len(problems)} problem(s))")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print("READINESS METADATA: PASS")
    for record in records:
        delivery = "DELIVERY_COMPLETE" if record.delivery_complete else "DELIVERY_INCOMPLETE"
        print(f"- {record.mission_id} v{record.curriculum_version} {record.release_kind}: {delivery}; pilot={record.pilot_status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
