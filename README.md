# Affiliate Intelligence Bot — lộ trình học và xây hệ thống có kiểm soát

Mục tiêu của repo là giúp người mới xây một **Affiliate Intelligence Bot tiến hóa dần tới tự động hóa cao nhưng vẫn kiểm soát được**.

Nội dung learner-facing ưu tiên tiếng Việt; xem [`docs/VIETNAMESE-LANGUAGE-STYLE.md`](docs/VIETNAMESE-LANGUAGE-STYLE.md).

## Bắt đầu ở đâu?

1. Đọc [`CURRICULUM.md`](CURRICULUM.md) — nguồn chuẩn về Mission sequence, evidence và authority.
2. Mở [`curriculum/README.md`](curriculum/README.md) — learner path hiện hành.
3. Nếu đã hoàn thành pilot Bài 0.1 trước reset, giữ credit ở [`BOOT.1`](curriculum/BOOT/BOOT.1-run-change-test.md); không cần học lại.
4. Bắt đầu M00 mới tại [`M00.1`](curriculum/M00/M00.1-affiliate-intelligence-objective.md).

## Bot tiến hóa như thế nào?

```text
real evidence
→ deterministic advice
→ trustworthy history/replay
→ human action + measurement
→ grounded AI
→ automatic read-only
→ read-only evidence agent
→ shadow action
→ durable human approval
→ bounded auto-action
→ governed production closed loop
```

## Control model

```text
Evidence
→ DecisionPacket
→ ActionIntent
→ deterministic Policy / Risk
→ Human Approval khi cần
→ Controlled Execution
→ Audit
→ Outcome
→ Evaluation
```

Nguyên tắc bắt buộc:

```text
AI confidence != execution permission
Decision != Approval != Execution
Tool result != trusted evidence
```

## Reality-First, không Publish-First

M00 bắt đầu bằng observation thị trường thật nhưng **không yêu cầu publish**. Publish/action thật xuất hiện sau khi learner đã có deterministic baseline và history đủ audit.

## Technology

Go, n8n, AgentRuntime, MCP, rule engine, Temporal, OPA, Langfuse… là implementation/reference options. Tool chỉ được adopt khi giải quyết bottleneck thật và không làm đổi authority ceiling.

```text
DETERMINISTIC CORE FIRST != CODE FIRST
```

## Legacy/reference

Numeric lesson IDs cũ trong `lessons/`, các syllabus trong `sources/` và migration artifacts cũ chỉ còn vai trò reference/provenance trong giai đoạn cleanup. Learner mới không dùng chúng để xác định thứ tự học.

Snapshot đầy đủ trước curriculum reset:

```text
archive/pre-curriculum-reset-2026-09-03
```

## Repository checks

CI vẫn bảo vệ contracts, evidence semantics, privacy, authority và retained reference implementations trong thời gian migration. Repo hardening sẽ tiếp tục tách CI thành các nhóm dễ chẩn đoán hơn.
