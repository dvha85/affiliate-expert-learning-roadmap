# Phần 19 — PRODUCTION, SECURITY & AUTOMATION

- Timeline: **Standard M13–14 · Accelerated M10–11** — forecast; PASS evidence mới là gate.
- Quy mô: **5 chương / 32 bài**
- Chỉ tick bài khi đã đạt đủ [5 tiêu chí PASS](../docs/PASS-CRITERIA.md).

> Part 19 đưa A3 governed action Agent vào production. Production readiness không chỉ là service uptime; phải chứng minh durable HITL, decision/tool/action tracing, agent evaluation và Decision→Outcome learning có kiểm soát.

## Checklist bài học

### Chương 73 — Production Engineering & Observability

- [ ] **73.1** — Structured Logging
- [ ] **73.2** — Metrics
- [ ] **73.3** — Monitoring
- [ ] **73.4** — Health Check
- [ ] **73.5** — Distributed Tracing và agent/tool spans
- [ ] **73.6** — Alerting và operational SLOs

> Production observability phải truy ngược được `trigger → Signal → Analysis → Decision → tool/action → Policy/Approval → Execution → Outcome`; không chỉ CPU, HTTP status và DB latency.

Agent/decision metrics cần mở rộng theo [`AGENT-EVALUATION-STANDARD.md`](../docs/AGENT-EVALUATION-STANDARD.md), gồm task success, tool selection/arguments, unsupported claims, policy blocks, confidence calibration, decision latency, cost và outcome khi phù hợp.

### Chương 74 — Reliability & Durable Execution

- [ ] **74.1** — Retry và Backoff
- [ ] **74.2** — Timeout và Cancellation
- [ ] **74.3** — Circuit Breaker
- [ ] **74.4** — Queue, Workflow State và recovery boundary
- [ ] **74.5** — Idempotency, Deduplication và exactly-once illusion
- [ ] **74.6** — Checkpoint/Resume, Compensation và Disaster Recovery

> Workflow có Human Approval hoặc long-running external wait phải survive process restart. Durable state là reliability concern, không phải chỉ UX feature.

M13/M14 phải test durable HITL theo [`AGENT-HITL-RUNTIME.md`](../docs/AGENT-HITL-RUNTIME.md): process restart khi chờ approval, duplicate approval callback, expiry, revalidation failure, retry executor và kill switch trước resume.

### Chương 75 — Security & Agent Tool Security

- [ ] **75.1** — API Key và credential boundary
- [ ] **75.2** — Secret Management
- [ ] **75.3** — OAuth
- [ ] **75.4** — Authentication
- [ ] **75.5** — Authorization, least privilege và tool permissions
- [ ] **75.6** — Encryption, data boundary và sandbox/isolation concepts
- [ ] **75.7** — Audit Log, prompt injection và tool misuse investigation

> Agent không được có “god mode”. Untrusted content từ website/product/review/email/API/RAG/MCP có thể trở thành instruction injection; permission + policy + isolation phải giới hạn impact ngay cả khi model bị đánh lừa.

Decision/Outcome Memory không phải lý do để giữ raw sensitive data vô hạn. Chỉ lưu data/reference cần cho audit/evaluation với retention phù hợp.

### Chương 76 — Automation & Agent Governance

- [ ] **76.1** — Ranh giới automation hợp lệ và Action Intent
- [ ] **76.2** — Cấm fake traffic, engagement, review và order
- [ ] **76.3** — Cấm spam, platform manipulation và policy evasion
- [ ] **76.4** — RISK 0: auto execute cho collection, analysis và reporting
- [ ] **76.5** — RISK 1: auto execute + mandatory audit cho controlled actions
- [ ] **76.6** — RISK 2: Approval Queue, pause/resume, audit và kill switch

> Risk classification phải được bảo vệ bởi deterministic policy/rules; LLM có thể đề xuất nhưng không là authority duy nhất cho consequential actions.

RISK2 flow bắt buộc:

```text
DecisionPacket
→ ActionIntent
→ Policy/Risk
→ persist state
→ Human Approval
→ resume
→ revalidate freshness/target/policy/idempotency
→ execute hoặc terminate
```

Approval cũ không được execute nếu material context đổi hoặc decision/approval đã expire.

### Chương 77 — Deployment

- [ ] **77.1** — Docker và Go binary packaging
- [ ] **77.2** — Environment và configuration
- [ ] **77.3** — CI/CD
- [ ] **77.4** — Database Migration
- [ ] **77.5** — Cloud và runtime selection
- [ ] **77.6** — Backup và restore verification
- [ ] **77.7** — Cost Monitoring

> Agent production cost phải theo dõi model calls, tool calls, retries, decision latency và cost per analysis/decision; không chỉ compute/server bill.

## Decision / Outcome Learning

M14 phải chuẩn bị history theo [`DECISION-OUTCOME-MEMORY.md`](../docs/DECISION-OUTCOME-MEMORY.md):

```text
Decision
→ Action
→ Outcome
→ Evaluation
→ Proposed Improvement
→ Offline Test / Experiment
→ Review
→ Deploy
```

Cấm pattern:

```text
Outcome
→ Agent silently rewrites production policy/prompt/weights
```

Learning output chỉ là proposed change cho tới khi qua test/evaluation/review/deploy gate.

> **2026 freshness note:** automation governance phải bao gồm provenance, disclosure, AIGC/product-fidelity checks, data/privacy boundaries, Human Approval và kill switch. “Agentic” capability không loại bỏ accountability cho platform/legal requirements hiện hành.

## Cổng thực hành

- [ ] **PROJECT 13 — Production Affiliate Bot**
- [ ] Có artifact/evidence được lưu trong repo hoặc liên kết từ Issue
- [ ] Viết retrospective: kết quả, sai lệch, điều học được, bước tiếp theo

## Hoàn thành phần

- [ ] Tất cả bài học đã PASS
- [ ] Project/Lab/Pass Gate (nếu có) đã hoàn tất
- [ ] Knowledge Base đã cập nhật
- [ ] Đã chọn bài đầu tiên của phần tiếp theo

[← Roadmap tổng](../ROADMAP.md)
