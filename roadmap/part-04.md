# Phần 4 — Intelligence đáng tin cậy và orchestration

- Timeline: **Evidence-gated; reliability and evaluation cases determine completion**.
- **Chapters:** C12–C14
- **Core:** 9 micro-lessons
- **Missions:** M06–M07
- **Outcome:** Signal-to-decision pipeline chịu được duplicate, stale/conflicting evidence; n8n trưởng thành thành orchestration owner còn Deterministic Core giữ canonical signal/decision/policy contracts.

## Hybrid ownership trong Part 04

```text
n8n
= primary watcher/orchestration reference
= trigger + integration + routing + retry workflow + alert delivery

Deterministic Core
= canonical Signal/Decision contracts
= validation + dedup semantics + policy/abstention authority
= Go reference/fallback; visual rule engine có thể compare từ M07

Agent/AI
= optional triage/advisory
= không authorize execution
```

Part này là bước nâng n8n từ read-only learning slice ở M04 thành runtime orchestration thực sự. Tuy nhiên `workflow branch` không được trở thành policy authority.

Implementation principle:

```text
n8n handles plumbing
Deterministic Core handles canonical decision semantics
Go is a reference implementation, not a mandatory human-coding quota
```

## Attempt trước knowledge pull

1. M06: chạy watcher/orchestration với duplicate event và transient failure; lưu before behavior rồi mới thêm reliability.
2. M07: replay stale/missing/conflicting evidence rồi mới thêm `DecisionPacket` và abstention policy.
3. Cố ý dừng/retry orchestration để chứng minh canonical evidence/decision không phụ thuộc vào in-memory workflow state.
4. Sau khi deterministic fixtures/oracle đã ổn định, thử **một visual rule comparison nhỏ** trên cùng input/output contract; không adopt nếu parity hoặc reason trace không rõ.

## Core checklist

### Chương 12 — Reliable signals và alerts

- [ ] **12.1** — Material change, threshold, severity và alert noise
- [ ] **12.2** — Retry, backoff, idempotency và deduplication
- [ ] **12.3** — Queue/recovery boundary, logs, metrics và correlation

Implementation reference ưu tiên:

```text
schedule/webhook
→ n8n workflow
→ source/collector
→ Deterministic Core validation + dedup contract
→ SignalPacket
→ route/alert
```

`n8n execution succeeded` không có nghĩa signal hợp lệ; deterministic domain validation vẫn là gate.

M06 không yêu cầu tự viết Go scheduler/retry/alert nếu n8n giải quyết use case rõ hơn và behavior vẫn audit được.

### Chương 13 — Decision contracts

- [ ] **13.1** — SignalPacket → AnalysisPacket → DecisionPacket → ActionIntent
- [ ] **13.2** — Evidence, confidence, uncertainty, freshness và expiry
- [ ] **13.3** — Risk/policy boundary: WAIT, GET_MORE_DATA và HUMAN_REVIEW

Ownership bắt buộc:

```text
Deterministic Core creates/validates DecisionPacket
→ n8n routes DecisionPacket
→ Agent may advise
→ Deterministic Policy Authority owns final state
```

Implementation của Deterministic Policy Authority có thể là Go reference hoặc một reviewed visual rule engine đã PASS parity/fail-closed gate.

### Chương 14 — Decision evaluation

- [ ] **14.1** — Deterministic baseline, eval dataset và success rubric
- [ ] **14.2** — Unsupported, stale, missing và conflicting-evidence cases
- [ ] **14.3** — Decision utility, latency, cost và human intervention rate

M07 là **first meaningful visual-rule comparison** cho Core path. Candidate hiện tại: DecisionRules hoặc equivalent deterministic rule engine.

Comparison tối thiểu:

```text
same canonical fixtures
→ Go/reference result
→ visual rule result
→ parity diff
→ reason/trace review
```

Visual rule engine không được adopt nếu:

- same input/version cho result không deterministic;
- `unknown`/missing bị ép thành value;
- rule version/rollback không audit được;
- runtime/API failure không fail closed;
- AI-generated rule được publish mà không review.

Evaluation phải tách:

- domain decision quality;
- deterministic implementation parity/reliability;
- orchestration reliability;
- Agent/AI advisory quality nếu dùng.

Không gộp các failure class thành một metric mơ hồ.

## Orchestration reliability contract

M06 phải chứng minh tối thiểu:

```text
duplicate trigger
→ no duplicate canonical signal/action

transient integration failure
→ retry/backoff hoặc explicit failure

process/workflow restart
→ no loss of canonical evidence

same event replay
→ deterministic/idempotent result
```

Correlation ID phải nối được:

```text
workflow execution
→ source fetch/import
→ canonical evidence/signal
→ DecisionPacket
→ alert/result
```

## Fail-safe rules

```text
n8n unavailable
→ watcher/orchestration degraded
→ canonical history remains valid

Agent unavailable
→ deterministic DecisionPacket path remains

Deterministic Policy Authority unavailable / invalid / unverified
→ no consequential downstream execution
```

Không fallback sang n8n IF/Switch hoặc Agent judgment để giữ workflow chạy.

Part 04 chưa cấp external action authority ngoài alert/read-only operational effects được Mission cho phép.

## Part PASS

- [ ] M06–M07 đều có Capability PASS, Reality verified và Operated
- [ ] Duplicate/retry không tạo alert hoặc canonical record trùng
- [ ] Stale/missing/conflicting evidence dẫn tới trạng thái an toàn
- [ ] DecisionPacket có evidence/confidence/freshness/expiry
- [ ] Có baseline và eval report, không chỉ demo happy path
- [ ] n8n route/orchestrate nhưng không sở hữu Product truth hoặc final policy authority
- [ ] Orchestration restart/failure không corrupt canonical evidence
- [ ] Deterministic path vẫn hoạt động khi Agent unavailable
- [ ] Nếu dùng visual rule candidate: parity/reason/version/fail-closed gate PASS trước adoption
- [ ] Go vẫn có thể giữ vai trò reference/fallback mà learner không phải tự viết mọi orchestration plumbing

[← Part trước](part-03.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-05.md)
