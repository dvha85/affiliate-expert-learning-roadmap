#!/usr/bin/env python3
"""Validate the portable v2 contract registry using only the standard library."""
from __future__ import annotations

import argparse
import json
from copy import deepcopy
from pathlib import Path
from typing import Any

SCHEMAS = (
    "observation",
    "human-prediction",
    "bot-decision",
    "action-record",
    "measurement-context",
    "outcome",
    "evaluation",
    "change-proposal",
    "trace-bundle",
    "experiment",
)
RECORD_TO_SCHEMA = {
    "observation": "observation",
    "human_prediction": "human-prediction",
    "bot_decision": "bot-decision",
    "action_record": "action-record",
    "measurement_context": "measurement-context",
    "outcome": "outcome",
    "evaluation": "evaluation",
    "change_proposal": "change-proposal",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def require_fields(value: dict[str, Any], schema: dict[str, Any], label: str, errors: list[str]) -> None:
    for field in schema.get("required", []):
        if field not in value:
            errors.append(f"{label}: missing required field {field}")


def validate_trace(trace: dict[str, Any], schemas: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    require_fields(trace, schemas["trace-bundle"], "TraceBundle", errors)
    if trace.get("origin") != "synthetic":
        errors.append("O00 TraceBundle origin must be synthetic")
    if trace.get("external_side_effect_count") != 0:
        errors.append("O00 external_side_effect_count must be 0")
    if trace.get("replay_new_record_count") != 0:
        errors.append("O00 duplicate replay must create 0 records")
    records = trace.get("records")
    if not isinstance(records, dict):
        return errors + ["TraceBundle records must be an object"]
    for record_name, schema_name in RECORD_TO_SCHEMA.items():
        record = records.get(record_name)
        if not isinstance(record, dict):
            errors.append(f"TraceBundle missing {record_name}")
            continue
        require_fields(record, schemas[schema_name], record_name, errors)
        if record.get("origin") != "synthetic":
            errors.append(f"{record_name} origin must be synthetic in O00")
    observation = records.get("observation", {})
    decision = records.get("bot_decision", {})
    action = records.get("action_record", {})
    outcome = records.get("outcome", {})
    evaluation = records.get("evaluation", {})
    proposal = records.get("change_proposal", {})
    if isinstance(decision, dict) and decision.get("action") is not None:
        errors.append("O00 BotDecision action must be null")
    if isinstance(action, dict) and (action.get("mode") != "DRY_RUN" or action.get("external_side_effect") is not False):
        errors.append("O00 ActionRecord must be a human-approved DRY_RUN without side effect")
    if isinstance(outcome, dict) and outcome.get("value_state") in {"missing", "unknown", "not_yet_observable"} and outcome.get("observed_value") == 0:
        errors.append("missing/unknown/not_yet_observable outcome must not become observed zero")
    if isinstance(outcome, dict) and outcome.get("action_record_id") != action.get("action_record_id"):
        errors.append("Outcome must reference ActionRecord")
    if isinstance(evaluation, dict) and evaluation.get("outcome_id") != outcome.get("outcome_id"):
        errors.append("Evaluation must reference Outcome")
    if isinstance(proposal, dict):
        if proposal.get("evaluation_id") != evaluation.get("evaluation_id"):
            errors.append("ChangeProposal must reference Evaluation")
        if proposal.get("status") != "PENDING_REVIEW" or proposal.get("production_mutation") is not False:
            errors.append("O00 ChangeProposal must be PENDING_REVIEW and cannot mutate production")
    if isinstance(observation, dict) and observation.get("value_state") == "observed" and not observation.get("provenance_ref"):
        errors.append("observed O00 values would require provenance")
    return errors


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    schema_dir = root / "contracts/schemas"
    schemas: dict[str, dict[str, Any]] = {}
    for name in SCHEMAS:
        path = schema_dir / f"{name}.schema.json"
        if not path.exists():
            errors.append(f"missing schema {path.relative_to(root)}")
            continue
        try:
            data = load_json(path)
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON schema {name}: {exc.msg}")
            continue
        if data.get("$schema") != "https://json-schema.org/draft/2020-12/schema" or not data.get("title"):
            errors.append(f"schema {name} must declare draft and title")
        schemas[name] = data
    policy = root / "policies/v2-authority-policy.json"
    if not policy.exists():
        errors.append("missing v2 authority policy")
    if len(schemas) != len(SCHEMAS):
        return errors
    trace_path = root / "contracts/examples/o00-trace.json"
    if not trace_path.exists():
        return errors + ["missing O00 trace example"]
    trace = load_json(trace_path)
    errors.extend(validate_trace(trace, schemas))
    invalid_cases = {
        "o00-missing-to-zero.json": lambda copy: copy["records"]["outcome"].update({"value_state": "missing", "observed_value": 0}),
        "o00-duplicate-replay.json": lambda copy: copy.update({"replay_new_record_count": 1}),
        "o00-production-mutation.json": lambda copy: copy["records"]["change_proposal"].update({"production_mutation": True}),
    }
    for filename, mutate in invalid_cases.items():
        if not (root / "evals/cases" / filename).exists():
            errors.append(f"missing invalid case declaration {filename}")
            continue
        broken = deepcopy(trace)
        mutate(broken)
        if not validate_trace(broken, schemas):
            errors.append(f"invalid O00 case {filename} was accepted")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate v2 contracts and the O00 synthetic trace")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if errors:
        print("CONTRACT REGISTRY: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("CONTRACT REGISTRY: PASS — O00 is synthetic, idempotent and non-actionable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
