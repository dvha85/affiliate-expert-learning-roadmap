"""Provider-neutral M04 replay gate: grounded facts or deterministic fallback."""
from __future__ import annotations

from typing import Any


def evaluate(baseline: dict[str, Any], evidence: dict[str, dict[str, Any]], candidate: dict[str, Any] | None) -> dict[str, Any]:
    result = {"baseline": baseline, "action": None, "tool_or_write_called": False}
    if candidate is None:
        return {**result, "status": "unavailable", "fallback_used": True, "reason": "No advisory response."}
    if candidate.get("tool_calls") or candidate.get("writes") or candidate.get("action") is not None:
        return {**result, "status": "rejected", "fallback_used": True, "reason": "Advisory requested prohibited authority."}
    facts = candidate.get("facts")
    if not isinstance(facts, list):
        return {**result, "status": "rejected", "fallback_used": True, "reason": "Malformed facts schema."}
    for fact in facts:
        if not isinstance(fact, dict):
            return {**result, "status": "rejected", "fallback_used": True, "reason": "Malformed fact."}
        ref = fact.get("evidence_ref")
        field = fact.get("field")
        if ref not in evidence:
            return {**result, "status": "rejected", "fallback_used": True, "reason": "Unknown evidence ref."}
        if not field or evidence[ref].get(field) != fact.get("value"):
            return {**result, "status": "rejected", "fallback_used": True, "reason": "Evidence does not support claim."}
    return {
        **result,
        "status": "grounded",
        "fallback_used": False,
        "facts": facts,
        "hypotheses": candidate.get("hypotheses", []),
    }
