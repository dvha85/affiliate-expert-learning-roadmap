# Roadmap — Affiliate Intelligence Bot có kiểm soát

> Sequence authority: [`CURRICULUM.md`](CURRICULUM.md). Learner-facing lesson order: [`curriculum/README.md`](curriculum/README.md).

Tổng cộng: **7 phần · 21 chương · 63 bài học**.

> Con số trên hiện chỉ giữ **reference knowledge inventory** để provenance/validator cũ còn hoạt động trong quá trình cleanup. Learner mới không học tuần tự theo 63 numeric IDs.

## Learner progression hiện hành

```text
BOOT.1 (nếu cần)
→ M00 real evidence
→ M01 deterministic Bot
→ M02 trustworthy history/replay
→ M03 human action + measurement
→ M04 grounded AI
→ M05 reviewed improvement
→ M06 automatic read-only
→ M07 read-only Agent
→ M08 shadow ActionIntent
→ M09 durable approval + executor
→ M10 bounded auto-action
→ M11 production closed loop
```

## Mission roadmap

| Mission | Product outcome | Reality | Authority |
|---|---|---|---|
| M00 | First Real Evidence Packet + Human DecisionPacket | E1 | human/read-only |
| M01 | Smallest Deterministic Bot v0.1 | E0 + E1 support | A0 deterministic |
| M02 | Trustworthy History + Replay v0.2 | E1/E3-ready | A0 deterministic |
| M03 | First Tracked Human Action + outcome context | E2→E3 | human executes |
| M04 | Grounded AI Advisor | E3 | A1 advisory |
| M05 | Reviewed Improvement | E4 | A1 propose only |
| M06 | Reliable Automatic Watcher | E4 | automatic read-only |
| M07 | Read-only Evidence Agent | E4 | A2-RO |
| M08 | Shadow ActionIntent + Policy | E4 | A3-shadow |
| M09 | Durable Approval + Controlled Executor | E4/E5-ready | approval-gated |
| M10 | Governed Canary | E5 | bounded RISK0/RISK1 auto |
| M11 | Production Closed Loop | E6 | governed production |

## Reference knowledge inventory

Các Part dưới đây vẫn index numeric knowledge IDs cũ trong giai đoạn cleanup. Chúng là **reference**, không phải reading order.

| Phần | Trọng tâm reference | Chương | Bài | Missions | Trạng thái |
|---|---|---:|---:|---|---|
| [Phần 0](roadmap/part-00.md) | evidence/domain foundations | 0–2 | 9 | M00–M01 | reference |
| [Phần 1](roadmap/part-01.md) | baseline/history foundations | 3–5 | 9 | M01–M02 | reference |
| [Phần 2](roadmap/part-02.md) | measurement/grounded AI | 6–8 | 9 | M02–M04 | reference |
| [Phần 3](roadmap/part-03.md) | reviewed improvement | 9–11 | 9 | M05 | reference |
| [Phần 4](roadmap/part-04.md) | reliable decisions/watchers | 12–14 | 9 | M06 | reference |
| [Phần 5](roadmap/part-05.md) | governed tools/actions | 15–17 | 9 | M07–M10 | reference |
| [Phần 6](roadmap/part-06.md) | production closed loop | 18–20 | 9 | M11 | reference |

## Implementation rule

```text
DETERMINISTIC CORE FIRST != CODE FIRST
NO-CODE WHEN AUDITABLE
AGENT ONLY WHEN IT ADDS MEASURED VALUE
AUTOMATION ONLY AFTER POLICY + AUDIT + RECOVERY
```

Go, n8n, AgentRuntime, MCP, Temporal, OPA, rule engines and observability backends remain implementation/reference choices, not learner authority.
