#!/usr/bin/env python3
"""Validate the canonical Reality-First v2 lesson projection."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "lessons" / "V2-LESSON-MAP.json"
LESSON_ROOT = ROOT / "lessons"


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
        fail("V2-LESSON-MAP.json must declare curriculum_version=2")

    rules = data.get("rules", {})
    if rules.get("lesson_id_is_reading_order") is not False:
        fail("lesson IDs must not be treated as reading order in v2")
    if rules.get("legacy_front_matter_may_define_v2_readiness") is not False:
        fail("legacy front matter must not define v2 readiness")

    lessons = data.get("lessons", {})
    indexed = lesson_index()
    missing = sorted(set(lessons) - set(indexed))
    if missing:
        fail(f"mapped lesson files missing: {missing}")

    for lesson_id, meta in lessons.items():
        refs = meta.get("v2_mission_refs")
        if not isinstance(refs, list) or not refs:
            fail(f"{lesson_id}: v2_mission_refs must be a non-empty list")
        if meta.get("hard_prerequisites") != []:
            fail(f"{lesson_id}: hard lesson-chain prerequisites are not allowed in v2 projection")

        path = indexed[lesson_id]
        text = path.read_text(encoding="utf-8")
        generation = meta.get("body_generation")
        if generation == "v1":
            if meta.get("legacy_front_matter_retained") is not True:
                fail(f"{lesson_id}: v1 body must explicitly retain legacy front matter")
        elif generation == "v2":
            if not re.search(r"^curriculum_version:\s*2\s*$", text, re.MULTILINE):
                fail(f"{lesson_id}: v2-authored lesson must declare curriculum_version: 2")
        else:
            fail(f"{lesson_id}: body_generation must be v1 or v2")

    expected = {
        "6.1": ["M00"], "6.2": ["M00"], "6.3": ["M00"], "7.1": ["M00"],
        "7.2": ["M01"],
        "3.1": ["M03"], "3.2": ["M03"], "3.3": ["M03"],
        "4.1": ["M03"], "4.2": ["M03"], "4.3": ["M03"],
        "8.1": ["M04"], "8.2": ["M04"], "8.3": ["M04"],
    }
    for lesson_id, refs in expected.items():
        actual = lessons[lesson_id]["v2_mission_refs"]
        if actual != refs:
            fail(f"{lesson_id}: expected v2_mission_refs={refs}, got {actual}")

    for legacy_ai in ("5.1", "5.2", "5.3"):
        if lessons[legacy_ai].get("v2_role") != "reference":
            fail(f"{legacy_ai}: legacy AI lesson must be reference, not active M04 sequence")

    m00 = (ROOT / "missions" / "M00-first-safe-market-loop.md").read_text(encoding="utf-8")
    if 'on_demand: ["6.1", "6.2", "6.3", "7.1"]' not in m00:
        fail("M00 must pull 6.1, 6.2, 6.3 and 7.1 on demand")
    if "Decision ≠ Approval ≠ Execution" not in m00:
        fail("M00 must state Decision ≠ Approval ≠ Execution")

    m04 = (ROOT / "missions" / "M04-grounded-ai-advisor.md").read_text(encoding="utf-8")
    if 'on_demand: ["8.1", "8.2", "8.3"]' not in m04:
        fail("M04 must use Chapter 8 as the active v2 grounded-advisory sequence")
    if 'reference: ["5.1", "5.2", "5.3"]' not in m04:
        fail("M04 must retain 5.1-5.3 as reference only")

    print(f"PASS: v2 lesson projection is consistent ({len(lessons)} mapped lessons)")


def main() -> int:
    try:
        validate()
    except (AssertionError, json.JSONDecodeError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
