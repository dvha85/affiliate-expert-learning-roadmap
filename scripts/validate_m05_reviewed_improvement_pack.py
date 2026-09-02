#!/usr/bin/env python3
"""Validate M05's frozen experiment and human-reviewed ChangeProposal pack."""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def instant(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    experiment = data.get("experiment", {})
    trace = data.get("trace", {})
    outcome = data.get("outcome", {})
    evaluation = data.get("evaluation", {})
    proposal = data.get("change_proposal", {})
    review = data.get("review", {})
    costs = data.get("costs", {})
    for field in ("experiment_id", "main_variable", "hypothesis", "primary_metric", "measurement_context_id", "window_start", "window_end", "stop_rule", "frozen_at"):
        if not experiment.get(field):
            errors.append(f"Experiment missing {field}")
    try:
        if instant(experiment["frozen_at"]) > instant(experiment["window_start"]):
            errors.append("Experiment must be frozen before its window")
        if instant(experiment["window_end"]) < instant(experiment["window_start"]):
            errors.append("Experiment window_end must not precede window_start")
    except (KeyError, ValueError):
        errors.append("Experiment freeze/window timestamps must be ISO-8601")
    if outcome.get("action_record_id") != trace.get("action_record_id") or outcome.get("outcome_id") != trace.get("outcome_id"):
        errors.append("Outcome must link to Trace ActionRecord and Outcome ID")
    if outcome.get("measurement_context_id") != experiment.get("measurement_context_id"):
        errors.append("Outcome must use the frozen MeasurementContext")
    if evaluation.get("outcome_id") != trace.get("outcome_id") or evaluation.get("evaluation_id") != trace.get("evaluation_id"):
        errors.append("Evaluation must link to Outcome")
    if proposal.get("evaluation_id") != trace.get("evaluation_id"):
        errors.append("ChangeProposal must link to Evaluation")
    if proposal.get("production_mutation") is not False:
        errors.append("Outcome/ChangeProposal cannot mutate production")
    if proposal.get("status") not in {"PENDING_REVIEW", "APPROVED", "REJECTED"}:
        errors.append("ChangeProposal needs a reviewable status")
    if review.get("decision") not in {"release", "reject"} or not review.get("reviewer") or not review.get("rollback_target"):
        errors.append("Human review needs reviewer, release/reject decision and rollback target")
    if outcome.get("status") == "inconclusive" and evaluation.get("result") != "INCONCLUSIVE":
        errors.append("inconclusive outcome must remain INCONCLUSIVE in Evaluation")
    if not isinstance(costs.get("content_production_minutes"), (int, float)) or "model_tool_cost" not in costs or not costs.get("net_value_limitation"):
        errors.append("M05 must record production time, model/tool cost and net-value limitation")
    replay = data.get("offline_replay", {})
    if not replay.get("champion_id") or not replay.get("challenger_id"):
        errors.append("M05 needs offline champion–challenger record")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate M05 reviewed-improvement evaluator pack")
    parser.add_argument("--case", type=Path, default=ROOT / "evals/M05-reviewed-improvement/valid-reviewed-improvement.json")
    args = parser.parse_args()
    errors = validate(json.loads(args.case.read_text(encoding="utf-8")))
    if errors:
        print("M05 REVIEWED IMPROVEMENT PACK: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M05 REVIEWED IMPROVEMENT PACK: PASS — synthetic fixture; no self-modification.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
