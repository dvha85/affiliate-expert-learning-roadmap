#!/usr/bin/env python3
"""Guard the tracked PR9 template against fabricated pilot completion claims."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def validate(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    if data.get("pilot_status") != "not_started":
        errors.append("tracked pilot template must remain not_started until human review")
    if data.get("hidden_telemetry") is not False or data.get("consent_required") is not True:
        errors.append("pilot template must require consent and prohibit hidden telemetry")
    if data.get("participant_count") is not None:
        errors.append("tracked template must not claim participants")
    serialized = json.dumps(data).lower()
    if "@" in serialized or "api_key" in serialized or "password" in serialized:
        errors.append("pilot template must not contain identifying/secret fields")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the tracked PR9 pilot template")
    parser.add_argument("--template", type=Path, default=Path(__file__).resolve().parents[1] / "pilot/aggregate-template.json")
    args = parser.parse_args()
    errors = validate(args.template)
    if errors:
        print("PILOT TEMPLATE: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PILOT TEMPLATE: PASS — no participant/pilot claim is fabricated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
