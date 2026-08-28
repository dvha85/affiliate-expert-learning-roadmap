# Phần 17 — AI AFFILIATE BOT

- Timeline: **Standard M11–12 · Accelerated M9** — forecast; PASS evidence mới là gate.
- Quy mô: **6 chương / 36 bài**
- Chỉ tick bài khi đã đạt đủ [5 tiêu chí PASS](../docs/PASS-CRITERIA.md).

## Checklist bài học

### Chương 61 — LLM Foundation

- [ ] **61.1** — LLM
- [ ] **61.2** — Token
- [ ] **61.3** — Context
- [ ] **61.4** — Prompt
- [ ] **61.5** — Structured Output
- [ ] **61.6** — Tool Engineering, Tool Calling và MCP
- [ ] **61.7** — Hallucination
- [ ] **61.8** — Evaluation
- [ ] **61.9** — Cost

> Tool use phải được xem như một production boundary: schema, validation, permissions, side effects, timeout, retry, idempotency, policy decision và audit. MCP là interoperability concept quan trọng; không bắt buộc dùng cho mọi integration nếu REST/webhook/native API đơn giản hơn.

### Chương 62 — AI Product Understanding

- [ ] **62.1** — Trích xuất Product Features
- [ ] **62.2** — Chuyển Features thành Benefits
- [ ] **62.3** — Xác định Audience và Pain
- [ ] **62.4** — Phân tích Objections
- [ ] **62.5** — Đề xuất và kiểm chứng Content Angles

### Chương 63 — AI Content Engine

- [ ] **63.1** — GenerateHooks()
- [ ] **63.2** — GenerateScript()
- [ ] **63.3** — GenerateComparison()
- [ ] **63.4** — GenerateReview()
- [ ] **63.5** — GenerateCTA() và content safety

### Chương 64 — Knowledge Base, RAG & State

- [ ] **64.1** — Knowledge Base và knowledge boundary
- [ ] **64.2** — Embeddings
- [ ] **64.3** — Vector Search
- [ ] **64.4** — Retrieval
- [ ] **64.5** — RAG
- [ ] **64.6** — Source Grounding, session state và workflow state

> Knowledge ≠ session state ≠ durable workflow state. Approval wait, retry state và action history không được nhét tùy tiện vào prompt/RAG store.

### Chương 65 — AI & Agent Evaluation

- [ ] **65.1** — Correctness và task success
- [ ] **65.2** — Relevance và tool selection accuracy
- [ ] **65.3** — Hallucination và unsupported claims
- [ ] **65.4** — Policy Safety, prompt injection và tool misuse
- [ ] **65.5** — Brand Consistency và approval quality
- [ ] **65.6** — Performance, latency, cost và human intervention rate

> Evaluation không chỉ hỏi “text có hay không?”. Với agent phải đo cả trajectory: chọn đúng tool không, argument đúng không, có gọi tool thừa không, policy có chặn đúng không và task có hoàn thành thật không.

### Chương 66 — Human-in-the-loop & Approval Workflow

- [ ] **66.1** — AI Draft, Action Intent và trạng thái workflow
- [ ] **66.2** — Human Review, Risk Level và checklist duyệt
- [ ] **66.3** — Approve/Reject, reason và audit trail
- [ ] **66.4** — Pause/Resume, publish/action boundaries và expiry
- [ ] **66.5** — Performance feedback, evaluation và learning loop

> **Default architecture:** single-agent/tool workflow trước; multi-agent chỉ dùng khi decomposition thật sự có lợi. Human approval phải là stateful workflow boundary chứ không chỉ là “người xem lại text”.

> **2026 freshness note:** AIGC policy is an operating constraint, not an optional ethics appendix. AI workflows must preserve source grounding, product fidelity, disclosure state, policy checks and human approval for claims/publishing boundaries. Current platform rules belong in the freshness layer and must be re-verified before production use.

## Cổng thực hành

- [ ] **PROJECT 12 — AI Content Assistant**
- [ ] Có artifact/evidence được lưu trong repo hoặc liên kết từ Issue
- [ ] Viết retrospective: kết quả, sai lệch, điều học được, bước tiếp theo

## Hoàn thành phần

- [ ] Tất cả bài học đã PASS
- [ ] Project/Lab/Pass Gate (nếu có) đã hoàn tất
- [ ] Knowledge Base đã cập nhật
- [ ] Đã chọn bài đầu tiên của phần tiếp theo

[← Roadmap tổng](../ROADMAP.md)
