# Mission index

The active canonical sequence is curriculum v2. `authoring` is not delivery
readiness: see `python scripts/report_readiness.py` and
[migration rules](../docs/CURRICULUM-MIGRATION-v2.md).

## V2 canonical Mission spine

| Mission | Outcome | Authoring |
|---|---|---|
| M00 | First Safe Market Loop — human-only manual publish with disclosure/tracking | planned |
| M01 | First Outcome Snapshot — real measurement, zero/pending/inconclusive allowed | planned |
| M02 | Smallest Deterministic Bot — auditable A0 baseline | planned |
| M03 | Trustworthy History & Measurement — provenance/freshness/reconcile | planned |
| M04 | Grounded AI Advisor — A1, no tools/write/execute | planned |
| M05 | First Reviewed Improvement — outcome → test/review/rollback | planned |
| M06 | Reliable Watcher | planned |
| M07 | Decision and Abstention | planned |
| M08 | Read-only Evidence Agent | planned |
| M09 | Shadow Action and Approval | planned |
| M10 | Governed Canary | planned |
| M11 | Production Closed Loop | planned |

M00 → {M01, M02}; M01 + M02 → M03 → M04 → M05 → M06 … M11. `O00`
is a non-PASS synthetic orientation and intentionally has no Mission file yet.

## V1 baseline/reference delivery

These are retained exactly enough to preserve existing links, learner evidence
and reference behavior. Their `curriculum_version: 1` metadata means they do
not project the v2 rows above; do not use them as a new learner's v2 order.

| V1 file | Historical outcome | Authoring | Delivery |
|---|---|---|---|
| [M00 First Evidence-Backed Decision](M00-first-evidence-backed-decision.md) | maps to v2 M02 knowledge/baseline | ready | incomplete |
| [M01 Trustworthy History](M01-trustworthy-history.md) | maps to v2 M03 history | ready | incomplete |
| [M02 Grounded AI Advisor](M02-grounded-ai-advisor.md) | maps to v2 M04 AI advisor | ready | incomplete |
| [M03 First Tracked Manual Publish](M03-first-tracked-manual-publish.md) | maps to v2 M00 market loop | draft | incomplete |

No v1 `ready` row is evidence that a v2 Mission is delivered. The explicit
old-to-new mapping is maintained in
[CURRICULUM-MIGRATION-v2.md](../docs/CURRICULUM-MIGRATION-v2.md).
