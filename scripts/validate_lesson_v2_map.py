#!/usr/bin/env python3
"""Validate the retained numeric lesson map as a reference/provenance layer.

The active learner order is mission-based under curriculum/. This validator must
not make legacy numeric IDs or old Mission pull lists authoritative again.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "lessons" / "V2-LESSON-MAP.json"
LESSON_ROOT = ROOT / "lessons"
ACTIVE_LEARNER_ROOT = ROOT / "curriculum"


def fail(message: str) -> None:
    raise AssertionError(message)


def load_map() -> dict:
    return json.loads(MAP_PATH.read_text(encoding="utf-8"))


def lesson_index() -> dict[str, Path]:
    result: dict[str, Path] = {}
    pattern = re.compile(r'^lesson_id:\s*["\']?([^"\'\n]+)', re.MULTILINE)
    for path in LESSON_ROOT.glob("part-*/chapter-*/*.md"):
        text = path.read_text(encoding="utf-8")
        match = pattern.search(text)
        if not match:
            continue
        lesson_id = match.group(1).strip()
        if lesson_id in result:
            fail(f"duplicate lesson_id {lesson_id}: {result[lesson_id]} and {path}")
        result[lesson_id] = path
    return result


def validate() -> None:
    data = load_map()
    if data.get("curriculum_version") != 2:
        fail("V2-LESSON-MAP.json must declare curriculum_version=2 while retained")

    rules = data.get("rules", {})
    if rules.get("lesson_id_is_reading_order") is not False:
        fail("retained numeric lesson IDs must not be treated as learner reading order")
    if rules.get("legacy_front_matter_may_define_v2_readiness") is not False:
        fail("legacy front matter must not define current readiness")

    if not (ACTIVE_LEARNER_ROOT / "README.md").exists():
        fail("curriculum/README.md must define the active mission-based learner path")
    for required in (
        ACTIVE_LEARNER_ROOT / "BOOT" / "BOOT.1-run-change-test.md",
        ACTIVE_LEARNER_ROOT / "M00" / "M00.1-affiliate-intelligence-objective.md",
        ACTIVE_LEARNER_ROOT / "M00" / "M00.2-evidence-uncertainty.md",
        ACTIVE_LEARNER_ROOT / "M00" / "M00.3-decision-approval-execution.md",
    ):
        if not required.exists():
            fail(f"active learner card missing: {required.relative_to(ROOT)}")

    lessons = data.get("lessons", {})
    indexed = lesson_index()
    missing = sorted(set(lessons) - set(indexed))
    if missing:
        fail(f"mapped reference lesson files missing: {missing}")

    for lesson_id, meta in lessons.items():
        refs = meta.get("v2_mission_refs")
        if not isinstance(refs, list) or not refs:
            fail(f"{lesson_id}: retained v2_mission_refs must be a non-empty provenance list")
        if meta.get("hard_prerequisites") != []:
            fail(f"{lesson_id}: hard legacy lesson-chain prerequisites are not allowed")

        path = indexed[lesson_id]
        text = path.read_text(encoding="utf-8")
        generation = meta.get("body_generation")
        if generation == "v1":
            if meta.get("legacy_front_matter_retained") is not True:
                fail(f"{lesson_id}: v1 body must explicitly retain legacy front matter")
        elif generation == "v2":
            if not re.search(r"^curriculum_version:\s*2\s*$", text, re.MULTILINE):
                fail(f"{lesson_id}: v2-authored reference lesson must declare curriculum_version: 2")
        else:
            fail(f"{lesson_id}: body_generation must be v1 or v2")

    m00 = (ROOT / "missions" / "M00-first-safe-market-loop.md").read_text(encoding="utf-8")
    if "Decision ≠ Approval ≠ Execution" not in m00:
        fail("M00 must retain the Decision ≠ Approval ≠ Execution authority boundary")
    if "NO external execution" not in m00:
        fail("M00 must remain non-executing under the mission-first reset")
    if "on_demand: [\"6.1\", \"6.2\", \"6.3\", \"7.1\"]" in m00:
        fail("M00 must not restore the retired numeric lesson pull list as learner authority")

    print(
        "PASS: retained numeric lesson map is reference-only; "
        f"{len(lessons)} mapped legacy/reference lessons remain traceable"
    )


def main() -> int:
    try:
        validate()
    except (AssertionError, json.JSONDecodeError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
