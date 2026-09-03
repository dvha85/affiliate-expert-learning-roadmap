# Bot evolution roadmap — governed autonomy

> Sequence authority: [`CURRICULUM.md`](../CURRICULUM.md). Reality-First không đồng nghĩa Publish-First: M00 tạo market evidence trước, Bot v0.1 xuất hiện ở M01, external action đầu tiên ở M03.

| Mission | Bot version | Part | Product outcome | Reality | AI / authority |
|---|---|---|---|---|---|
| M00 | pre-bot | P0 | First Real Evidence Packet + Human DecisionPacket | E1 | A0 human/read-only; no external action |
| M01 | v0.1 | P1 | Smallest Deterministic Bot | E1 support | A0 deterministic; no action |
| M02 | v0.2 | P1 | Trustworthy History + Replay | E1 | A0 deterministic |
| M03 | v0.3 | P2 | First Tracked Human Action + Outcome Context | E2→E3 | A0 decision/measurement; human executes, Bot no execution |
| M04 | v0.4 | P2 | Grounded AI Advisor with fallback | E3 | A1 advisory; no tools/write |
| M05 | v0.5 | P3 | First Reviewed Improvement | E4 | A1 propose only |
| M06 | v1.0 | P4 | Reliable Automatic Watcher | E4 | A0 core + A1 triage; automatic read-only |
| M07 | v1.1 | P5 | Read-only Evidence Agent | E4 | A2-RO read-only tools |
| M08 | v1.2 | P5 | Shadow ActionIntent + Policy | E4 | A3-shadow; no production side effect |
| M09 | v1.3 | P5 | Durable Approval + Controlled Executor | E4/E5-ready | A3-limited approval-only subset; no bounded auto yet |
| M10 | v1.4 | P5 | Governed Canary | E5 | A3-limited; bounded RISK0/RISK1 auto, RISK2 approval |
| M11 | v2.0 | P6 | Production Closed Loop | E6 | A3-production governed production |

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
- M06 chỉ tự động hóa read-only watcher; Agent tự chọn read tool chỉ bắt đầu ở M07/A2-RO.
- M08 chỉ shadow/dry-run `ActionIntent`; M09 mới nối durable approval với controlled executor và vẫn không cho bounded auto-action.
- M10 mới mở bounded automatic execution cho allowlisted RISK0/RISK1; RISK2 vẫn cần durable human approval + revalidation.
- `ActionIntent` không phải execution permission.
- M10/M11 phải có policy, audit, idempotency, recovery và kill switch.

## Replaceability

Go, visual deterministic rules, n8n và AgentRuntime là implementation choices. Thay runtime không được đổi canonical evidence, decision, policy, approval hoặc audit semantics.

## Optional advanced work

A4 multi-agent chỉ là advanced option sau khi M11 khi decomposition có measured benefit; không phải Core Mission.
