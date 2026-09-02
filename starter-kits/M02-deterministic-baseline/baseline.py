"""Small, auditable M02 deterministic decision baseline; no AI/tools/network."""
from __future__ import annotations

from typing import Any

FORMULA_VERSION = "m02-price-times-commission-v0.1"


def evaluate(observations: list[dict[str, Any]]) -> dict[str, Any]:
    """Rank only fully evidenced numeric rows; otherwise abstain safely."""
    missing: list[str] = []
    scored: list[dict[str, Any]] = []
    for index, row in enumerate(observations):
        subject = str(row.get("subject_id") or f"row-{index + 1}")
        required = ("source_url", "observed_at", "price", "commission_rate")
        absent = [field for field in required if row.get(field) is None or row.get(field) == ""]
        if absent:
            missing.append(f"{subject}: {', '.join(absent)}")
            continue
        price = row["price"]
        commission_rate = row["commission_rate"]
        if not isinstance(price, (int, float)) or not isinstance(commission_rate, (int, float)):
            missing.append(f"{subject}: numeric price/commission_rate")
            continue
        scored.append({"subject_id": subject, "score": price * commission_rate})

    base = {
        "formula_version": FORMULA_VERSION,
        "ai_or_tool_called": False,
        "action": None,
        "evidence_kinds": sorted({str(row.get("evidence_kind", "unknown")) for row in observations}),
    }
    if missing:
        return {
            **base,
            "recommended_state": "GET_MORE_DATA",
            "reason": "Required evidence is missing or invalid; no ranking is emitted.",
            "missing_evidence": sorted(missing),
            "ranking": [],
        }
    ranked = sorted(scored, key=lambda item: (-item["score"], item["subject_id"]))
    return {
        **base,
        "recommended_state": "RANK_SCENARIO",
        "reason": "Deterministic price × commission_rate scenario; not execution permission.",
        "missing_evidence": [],
        "ranking": ranked,
    }
