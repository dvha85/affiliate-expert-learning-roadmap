# Agent Runtime Standard — Chuẩn môi trường chạy Agent

## 1. Mục tiêu

A2 Agent được phép dùng tool để lấy thêm evidence, nhưng runtime phải enforce permission, budgets, validation và policy boundary thay vì dựa vào prompt.

Agent runtime là **untrusted intelligence worker**, không phải authority layer.

## 2. Runtime loop

```text
Task / Decision Need
→ Build allowed tool surface
→ Model reasoning
→ Tool request
→ Permission + schema validation
→ Tool execution
→ validate result
→ update AnalysisPacket / CandidateEvidence
→ Deterministic Core validation/grounding
→ stop / continue within budget
```

Go hiện là reference/fallback implementation của deterministic validation; implementation khác chỉ được thay sau parity/audit/fail-closed gate theo ADR-004.

## 3. Budgets

Mỗi run cần bounded limits phù hợp:

- max model turns;
- max tool calls;
- max wall-clock time;
- model/tool cost budget;
- max concurrent read calls;
- max retry attempts.

Hết budget phải fail/abstain có kiểm soát, không loop vô hạn.

## 4. Evidence escalation

Agent tool use ưu tiên phục vụ câu hỏi:

```text
what evidence is missing?
```

Không mặc định gọi mọi tool “để chắc”. Tool call phải có reason và được trace/evaluate.

Agent output hoặc tool result **không tự trở thành canonical evidence**. Nó là `CandidateEvidence` cho tới khi Deterministic Core validation và grounding pass.

## 5. Read vs write

M08 mặc định `READ_ONLY` evidence collection. `INTERNAL_WRITE` chỉ khi workflow contract yêu cầu và được allowlist rõ. `EXTERNAL_SIDE_EFFECT` chỉ xuất hiện ở Mission sau và luôn qua ActionIntent + deterministic Policy/Risk cùng approval khi cần.

## 6. Safe Profile bắt buộc từ M08

Canonical capability profile trung lập vendor:

```text
AGENT SAFE PROFILE — M08

Tool surface:
ALLOWLIST ONLY

External write:
DENY

Arbitrary shell / command execution:
DENY BY DEFAULT

Self-modification / skill mutation:
DENY

Production workspace mutation:
DENY

Credential disclosure:
DENY

Persistent memory write:
DENY BY DEFAULT hoặc isolated sandbox có review

Messaging / publish / spend / account change:
DENY

Tool result:
UNTRUSTED UNTIL DETERMINISTIC VALIDATION

Canonical state ownership:
NEVER AGENT-OWNED
```

Hermes Agent hoặc runtime khác chỉ được dùng ở M08 nếu map được profile này thành enforcement thực tế. Feature runtime có sẵn không đồng nghĩa permission được cấp.

Mission sau có thể mở thêm capability theo authority gate, nhưng phải explicit, versioned và auditable; không inherit quyền ngầm từ runtime.

## 7. Provider capability adapter

Core runtime có interface trung lập cho:

- structured output;
- tool discovery/search;
- tool calls;
- reasoning/model invocation;
- pause/resume hooks khi available.

Provider-specific feature được adapter hóa. Không để provider response/tool type thành domain type.

## 8. Tool discovery

Nếu runtime/provider hỗ trợ deferred loading, ưu tiên namespace discovery để giảm tool-schema context và confusion. Nếu không, application có thể pre-filter allowed tools deterministic trước model call.

Discovery chỉ ảnh hưởng tool visibility; **authorization vẫn là deterministic permission check**.

## 9. Error classes

Phân biệt:

- model output invalid;
- tool argument invalid;
- permission denied;
- timeout;
- transient tool failure;
- permanent failure;
- stale result;
- policy denied;
- approval required.

Retry chỉ áp khi safe/idempotent và policy cho phép.

## 10. State

Không trộn:

```text
conversation/session state
knowledge/RAG
workflow durable state
decision/action state
```

Long approval wait không phụ thuộc process memory hoặc Agent session memory.

## 11. Observability

Trace tối thiểu:

- run/decision correlation;
- selected model route;
- discovered/available tools;
- permission decision;
- tool calls + latency/status;
- interruptions/approval;
- token/cost metrics khi available;
- final task status.

## 12. Security

Retrieved content, MCP descriptions/results và tool output là untrusted. Tool selection không được thay đổi authorization policy. Credential scope phải theo least privilege.

Prompt/model instruction không thể tự bật capability bị Safe Profile hoặc Policy deny.

Canonical fail-safe:

```text
Deterministic Policy Authority unavailable / invalid / unverified
→ no consequential execution
```

Không fallback sang Agent judgment hoặc workflow branch để giữ hệ thống chạy.
