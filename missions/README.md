# Mission index — canonical execution spine

Learner order is defined by `CURRICULUM.md` and this Mission spine. Numeric legacy lesson IDs do not define the learning order.

| Mission | Outcome | Authority | Status |
|---|---|---|---|
| O00 | Safe synthetic walkthrough, no PASS | no side effect | orientation |
| [M00](M00-first-safe-market-loop.md) | First Real Evidence Packet + Human DecisionPacket | human/read-only | draft |
| M01 | Smallest Deterministic Bot v0.1 | A0 deterministic | reset target |
| M02 | Trustworthy History + Replay v0.2 | A0 deterministic | reset target |
| M03 | First Tracked Human Action + outcome context | human executes | reset target |
| [M04](M04-grounded-ai-advisor.md) | Grounded AI Advisor | A1 advisory | draft/remap |
| [M05](M05-first-reviewed-improvement.md) | Reviewed Improvement | A1 propose only | draft/remap |
| M06 | Reliable Automatic Watcher | automatic read-only | planned |
| M07 | Read-only Evidence Agent | A2-RO | planned |
| M08 | Shadow ActionIntent + Policy | A3-shadow | planned |
| M09 | Durable Approval + Controlled Executor | approval-gated | planned |
| M10 | Governed Canary | bounded RISK0/RISK1 auto | planned |
| M11 | Production Closed Loop | governed production | planned |

Canonical progression:

```text
O00 → M00 → M01 → M02 → M03 → M04 → M05 → M06 → M07 → M08 → M09 → M10 → M11
```

M00 is intentionally **Reality-First but not Publish-First**. External publish/action begins at M03 after deterministic advice/history exist.

## Legacy files

Files whose names/outcomes belong to the prior spine are reference-only until removed in cleanup. They do not override the table above. Full pre-reset state is preserved at:

```text
archive/pre-curriculum-reset-2026-09-03
```
