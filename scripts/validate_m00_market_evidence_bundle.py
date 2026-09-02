#!/usr/bin/env python3
"""Check M00's three-observation and human-only evidence-bundle contract."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def markdown_values(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("-") or ":" not in line:
            continue
        key, value = line[1:].split(":", 1)
        values[key.strip().lower()] = value.strip()
    return values


def validate(bundle: Path, fixture: bool = True) -> list[str]:
    errors: list[str] = []
    brief = markdown_values(bundle / "MARKET-BRIEF.md")
    readiness = markdown_values(bundle / "PUBLISH-READINESS.md")
    action = markdown_values(bundle / "ACTION-RECORD.md")
    try:
        observations = json.loads((bundle / "audience-observations.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalid audience-observations.json: {exc}"]
    for field in ("brief_id", "frozen_at", "audience_problem_hypothesis", "exact_artifact_ref", "tracking_id", "outcome_window_start", "outcome_window_end"):
        if not brief.get(field):
            errors.append(f"MarketBrief missing {field}")
    if len(observations) < 3:
        errors.append("M00 requires at least three audience/problem observations")
    for index, observation in enumerate(observations, start=1):
        for field in ("observation_id", "source_url", "access_method", "observed_at", "audience_problem"):
            if not observation.get(field):
                errors.append(f"observation {index} missing {field}")
        if observation.get("access_method") != "public_manual":
            errors.append(f"observation {index} must use public_manual")
        expected_kind = "synthetic" if fixture else "real"
        if observation.get("evidence_kind") != expected_kind:
            errors.append(f"observation {index} must be {expected_kind} in this mode")
    for field in ("brief_id", "exact_artifact_ref", "tracking_id", "outcome_window", "human_reviewer"):
        if not readiness.get(field):
            errors.append(f"PublishReadiness missing {field}")
    for field in ("claim check", "disclosure check", "rights/permission check", "pii check", "owned/allowed channel check"):
        if readiness.get(field) != "pass":
            errors.append(f"PublishReadiness must pass {field}")
    for field in ("paid spend", "dm/outreach", "scraping", "bot/ai auto-publish"):
        if readiness.get(field) != "no":
            errors.append(f"PublishReadiness must prohibit {field}")
    for field in ("action_record_id", "brief_id", "tracking_id", "measurement_context_id", "outcome_window_start", "outcome_window_end"):
        if not action.get(field):
            errors.append(f"ActionRecord missing {field}")
    if action.get("execution_actor") != "human_only" or action.get("action") != "manual publish":
        errors.append("M00 ActionRecord must be human_only manual publish")
    if action.get("bot/ai publish or external execution") != "no":
        errors.append("M00 must prohibit Bot/AI publish or external execution")
    if brief.get("brief_id") and action.get("brief_id") != brief.get("brief_id"):
        errors.append("ActionRecord must reference the frozen MarketBrief")
    if fixture and action.get("external_side_effect") != "false":
        errors.append("fixture must not claim an external side effect")
    if not fixture and action.get("external_side_effect") != "true":
        errors.append("real manual publish must record external_side_effect: true")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a M00 market evidence bundle")
    parser.add_argument("--bundle", type=Path, default=Path(__file__).resolve().parents[1] / "evals/M00-market-evidence-bundle")
    parser.add_argument("--real", action="store_true", help="require real observations and a real human action record")
    args = parser.parse_args()
    errors = validate(args.bundle, fixture=not args.real)
    if errors:
        print("M00 MARKET EVIDENCE BUNDLE: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    kind = "real bundle" if args.real else "synthetic structural fixture"
    print(f"M00 MARKET EVIDENCE BUNDLE: PASS — {kind}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
