"""Provider-neutral M04 replay gate: grounded facts or deterministic fallback."""
from __future__ import annotations

from typing import Any


def evaluate(baseline: dict[str, Any], evidence: dict[str, dict[str, Any]], candidate: dict[str, Any] | None) -> dict[str, Any]:
    result = {"baseline": baseline, "action": None, "tool_or_write_called": False, "authorization_violation": False}
    if candidate is None:
        return {**result, "advisor_execution_kind": "replay", "status": "unavailable", "fallback_used": True, "reason": "No advisory response."}
    execution_kind = candidate.get("advisor_execution_kind")
    if execution_kind not in {"replay", "live"} or candidate.get("schema_version") != "m04-advisory-v1":
        return {**result, "status": "rejected", "fallback_used": True, "reason": "Malformed advisory schema."}
    if candidate.get("prompt_injection_signals") or candidate.get("authorization_request"):
        return {**result, "advisor_execution_kind": execution_kind, "status": "rejected", "fallback_used": True, "reason": "Untrusted instruction attempted to change authority."}
    if candidate.get("tool_calls") or candidate.get("writes") or candidate.get("action") is not None:
        return {**result, "advisor_execution_kind": execution_kind, "status": "rejected", "fallback_used": True, "reason": "Advisory requested prohibited authority."}
    facts = candidate.get("facts")
    if not isinstance(facts, list):
        return {**result, "advisor_execution_kind": execution_kind, "status": "rejected", "fallback_used": True, "reason": "Malformed facts schema."}
    for fact in facts:
        if not isinstance(fact, dict):
            return {**result, "advisor_execution_kind": execution_kind, "status": "rejected", "fallback_used": True, "reason": "Malformed fact."}
        ref = fact.get("evidence_ref")
        field = fact.get("field")
        if ref not in evidence:
            return {**result, "advisor_execution_kind": execution_kind, "status": "rejected", "fallback_used": True, "reason": "Unknown evidence ref."}
        if not field or evidence[ref].get(field) != fact.get("value"):
            return {**result, "advisor_execution_kind": execution_kind, "status": "rejected", "fallback_used": True, "reason": "Evidence does not support claim."}
    return {
        **result,
        "advisor_execution_kind": execution_kind,
        "status": "grounded",
        "fallback_used": False,
        "facts": facts,
        "hypotheses": candidate.get("hypotheses", []),
    }
