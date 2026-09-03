# Bot evolution roadmap — governed autonomy

> Sequence authority: [`CURRICULUM.md`](../CURRICULUM.md). Reality-First không đồng nghĩa Publish-First: M00 tạo market evidence trước, Bot v0.1 xuất hiện ở M01, external action đầu tiên ở M03.

| Mission | Bot version | Part | Product outcome | Reality | AI / authority |
|---|---|---|---|---|---|
| M00 | pre-bot | P0 | First Real Evidence Packet + Human DecisionPacket | E1 | human/read-only; no external action |
| M01 | v0.1 | P1 | Smallest Deterministic Bot | E1 support | A0 deterministic; no action |
| M02 | v0.2 | P1 | Trustworthy History + Replay | E1 | A0 deterministic |
| M03 | v0.3 | P2 | First Tracked Human Action + Outcome Context | E2→E3 | human executes; Bot no execution |
| M04 | v0.4 | P2 | Grounded AI Advisor with fallback | E3 | A1 advisory; no tools/write |
| M05 | v0.5 | P3 | First Reviewed Improvement | E4 | A1 propose only |
| M06 | v1.0 | P4 | Reliable Automatic Watcher | E4 | automatic read-only |
| M07 | v1.1 | P5 | Read-only Evidence Agent | E4 | A2-RO |
| M08 | v1.2 | P5 | Shadow ActionIntent + Policy | E4 | A3-shadow |
| M09 | v1.3 | P5 | Durable Approval + Controlled Executor | E4/E5-ready | approval-gated action |
| M10 | v1.4 | P5 | Governed Canary | E5 | bounded RISK0/RISK1 auto; RISK2 approval |
| M11 | v2.0 | P6 | Production Closed Loop | E6 | governed production |

```text
O00 synthetic walkthrough (not PASS)
→ M00 real evidence
→ M01 deterministic Bot
→ M02 history/replay
→ M03 human action + outcome
→ M04 grounded AI
→ M05 reviewed improvement
→ M06 automatic read-only
→ M07 read-only Agent
→ M08 shadow action
→ M09 approved action
→ M10 bounded auto-action
→ M11 production closed loop
```

## Version rules

- `pre-bot` nghĩa là chưa phát hành Bot; M00 tạo evidence/context.
- M01 là release v0.1 đầu tiên và phải deterministic/audit được.
- M03 có external action nhưng actor vẫn là human; version chỉ ghi nhận Bot/context đã hỗ trợ trace/measurement, không phải Bot được cấp execution authority.
- AI xuất hiện ở M04 và vẫn không thay deterministic evidence/policy boundary.
- Agent/tool authority chỉ tăng sau evidence/safety gate tương ứng.
- `ActionIntent` không phải execution permission.
- M10/M11 phải có policy, audit, idempotency, recovery và kill switch.

## Replaceability

Go, visual deterministic rules, n8n và AgentRuntime là implementation choices. Thay runtime không được đổi canonical evidence, decision, policy, approval hoặc audit semantics.

## Optional advanced work

A4 multi-agent chỉ là advanced option sau M11 khi decomposition có measured benefit; không phải Core Mission.
