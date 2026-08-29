# Phần 17 — AI AFFILIATE BOT

- Timeline: **Standard M11–12 · Accelerated M9** — forecast; PASS evidence mới là gate.
- Quy mô: **6 chương / 36 bài**
- Chỉ tick bài khi đã đạt đủ [5 tiêu chí PASS](../docs/PASS-CRITERIA.md).

> AI capability tăng dần theo [`AI-CAPABILITY-LEVELS.md`](../docs/AI-CAPABILITY-LEVELS.md): A1 advisory/read-only có thể xuất hiện từ M05; Part 17 là nơi formalize A2 tool-assisted Agent, grounding, evaluation và state separation. `AI APPEARS EARLY ≠ AI GETS AUTHORITY EARLY`.

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

> Structured output nên normalize về domain contract như `AnalysisPacket`/`DecisionPacket`, không để provider response object trở thành business model. Tool use là production boundary: schema, validation, permissions, side effects, timeout, retry, idempotency, policy decision và audit.

> **M12 tool runtime:** tool nên đăng ký theo namespace/permission/risk ceiling; runtime có thể dùng deferred tool discovery (nạp tool đúng lúc) và bounded programmatic orchestration cho nhiều READ_ONLY calls. Đây là capability pattern trung lập provider; implementation cụ thể thuộc freshness layer. Xem [`TOOL-REGISTRY-STANDARD.md`](../docs/TOOL-REGISTRY-STANDARD.md), [`AGENT-RUNTIME-STANDARD.md`](../docs/AGENT-RUNTIME-STANDARD.md) và [`PROGRAMMATIC-TOOL-ORCHESTRATION.md`](../docs/PROGRAMMATIC-TOOL-ORCHESTRATION.md).

> **MCP 2026 note:** protocol line `2026-07-28` có stateless core, MRTR, header routing, cacheable lists, authorization hardening và extension/Tasks. Stateless transport không thay durable business/workflow state. Xem [`MCP-2026-OPERATING-NOTES.md`](../docs/MCP-2026-OPERATING-NOTES.md).

### Chương 62 — AI Product Understanding

- [ ] **62.1** — Trích xuất Product Features
- [ ] **62.2** — Chuyển Features thành Benefits
- [ ] **62.3** — Xác định Audience và Pain
- [ ] **62.4** — Phân tích Objections
- [ ] **62.5** — Đề xuất và kiểm chứng Content Angles

> AI Product Understanding được phép xuất hiện sớm ở M06 dưới A1 để extract unstructured evidence thành structured features; deterministic score/ranking baseline vẫn ở Decision/Product Intelligence core.

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

> Knowledge ≠ session state ≠ durable workflow state. Signal/Analysis/Decision/Execution state cũng phải tách để audit. Approval wait, retry state và action history không được nhét tùy tiện vào prompt/RAG store.

### Chương 65 — AI & Agent Evaluation

- [ ] **65.1** — Correctness và task success
- [ ] **65.2** — Relevance và tool selection accuracy
- [ ] **65.3** — Hallucination và unsupported claims
- [ ] **65.4** — Policy Safety, prompt injection và tool misuse
- [ ] **65.5** — Brand Consistency và approval quality
- [ ] **65.6** — Performance, latency, cost và human intervention rate

> Evaluation không chỉ hỏi “text có hay không?”. Với Agent phải đo trajectory: tool selection/arguments, tool calls thừa, policy blocks, evidence coverage, confidence calibration, latency/cost và task/outcome success.

### Chương 66 — Human-in-the-loop & Approval Workflow

- [ ] **66.1** — AI Draft, Action Intent và trạng thái workflow
- [ ] **66.2** — Human Review, Risk Level và checklist duyệt
- [ ] **66.3** — Approve/Reject, reason và audit trail
- [ ] **66.4** — Pause/Resume, publish/action boundaries và expiry
- [ ] **66.5** — Performance feedback, evaluation và learning loop

> **Default architecture:** single-agent/tool workflow trước; multi-agent chỉ dùng khi decomposition thật sự có lợi. Human Approval là stateful workflow boundary, không chỉ là “người xem lại text”.

> **Provider-neutral rule:** model routing/tool capability có thể khác nhau giữa provider; domain Decision/Policy core phải giữ interface trung lập và có exit path.

> **2026 freshness note:** AIGC policy là operating constraint. AI workflow phải giữ source grounding, product fidelity, disclosure state, policy checks và Human Approval cho claims/publishing boundary. Current platform/provider/tool capabilities thuộc freshness layer và phải re-verify trước production use.

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
