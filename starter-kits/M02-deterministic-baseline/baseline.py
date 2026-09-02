"""Small, auditable M02 deterministic decision baseline; no AI/tools/network."""
from __future__ import annotations

from typing import Any

FORMULA_VERSION = "m02-price-times-commission-v0.1"
REQUIRED_FIELDS = ("subject_id", "observation_id", "source_url", "observed_at", "price", "currency", "commission_rate")


def response(state: str, reason: str, evidence_kinds: set[str], missing: list[str] | None = None, ranking: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    return {
        "formula_version": FORMULA_VERSION,
        "ai_or_tool_called": False,
        "action": None,
        "evidence_kinds": sorted(evidence_kinds),
        "recommended_state": state,
        "reason": reason,
        "missing_evidence": sorted(missing or []),
        "ranking": ranking or [],
    }


def evaluate(observations: list[dict[str, Any]]) -> dict[str, Any]:
    """Rank only fully evidenced single-currency rows; otherwise abstain/review."""
    missing: list[str] = []
    scored: list[dict[str, Any]] = []
    seen_observations: set[str] = set()
    subject_identity: dict[str, str] = {}
    currencies: set[str] = set()
    evidence_kinds = {str(row.get("evidence_kind", "unknown")) for row in observations}
    for index, row in enumerate(observations):
        subject = str(row.get("subject_id") or f"row-{index + 1}")
        observation_id = str(row.get("observation_id") or "")
        if observation_id and observation_id in seen_observations:
            return response("HUMAN_REVIEW", "Duplicate observation_id requires human review.", evidence_kinds, [f"{observation_id}: duplicate observation_id"])
        seen_observations.add(observation_id)
        identity = str(row.get("identity_key") or subject)
        prior_identity = subject_identity.get(subject)
        if prior_identity is not None and prior_identity != identity:
            return response("HUMAN_REVIEW", "Identity conflict requires human review.", evidence_kinds, [f"{subject}: conflicting identity_key"])
        subject_identity[subject] = identity
        absent = [field for field in REQUIRED_FIELDS if row.get(field) is None or row.get(field) == ""]
        if absent:
            missing.append(f"{subject}: {', '.join(absent)}")
            continue
        price = row["price"]
        commission_rate = row["commission_rate"]
        if not isinstance(price, (int, float)) or not isinstance(commission_rate, (int, float)):
            missing.append(f"{subject}: numeric price/commission_rate")
            continue
        if row.get("evidence_kind") not in {"real", "synthetic"}:
            missing.append(f"{subject}: evidence_kind real or synthetic")
            continue
        currencies.add(str(row["currency"]))
        scored.append({"subject_id": subject, "score": price * commission_rate})
    if missing:
        return response("GET_MORE_DATA", "Required evidence is missing or invalid; no ranking is emitted.", evidence_kinds, missing)
    if len(currencies) > 1:
        return response("HUMAN_REVIEW", "Mixed currency requires human review.", evidence_kinds, ["currency: mixed comparison scope"])
    ranked = sorted(scored, key=lambda item: (-item["score"], item["subject_id"]))
    return response("RANK_SCENARIO", "Deterministic price × commission_rate scenario; not execution permission.", evidence_kinds, ranking=ranked)
