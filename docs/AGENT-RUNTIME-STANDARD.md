# Agent Runtime Standard — Chuẩn môi trường chạy Agent

## 1. Mục tiêu

A2 Agent được phép dùng tool để lấy thêm evidence, nhưng runtime phải enforce permission, budgets, validation và policy boundary thay vì dựa vào prompt.

## 2. Runtime loop

```text
Task / Decision Need
→ Build allowed tool surface
→ Model reasoning
→ Tool request
→ Permission + schema validation
→ Tool execution
→ validate result
→ update AnalysisPacket / Decision evidence
→ stop / continue within budget
```

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

## 5. Read vs write

M08 ưu tiên READ_ONLY evidence collection. INTERNAL_WRITE chỉ khi workflow contract yêu cầu. EXTERNAL_SIDE_EFFECT chỉ xuất hiện ở Mission sau và luôn qua ActionIntent + Policy/Risk cùng approval khi cần.

## 6. Provider capability adapter

Core runtime có interface trung lập cho:

- structured output;
- tool discovery/search;
- tool calls;
- reasoning/model invocation;
- pause/resume hooks khi available.

Provider-specific feature được adapter hóa. Không để provider response/tool type thành domain type.

## 7. Tool discovery

Nếu runtime/provider hỗ trợ deferred loading, ưu tiên namespace discovery để giảm tool-schema context và confusion. Nếu không, application có thể pre-filter allowed tools deterministic trước model call.

## 8. Error classes

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

## 9. State

Không trộn:

```text
conversation/session state
knowledge/RAG
workflow durable state
decision/action state
```

Long approval wait không phụ thuộc process memory.

## 10. Observability

Trace tối thiểu:

- run/decision correlation;
- selected model route;
- discovered/available tools;
- tool calls + latency/status;
- interruptions/approval;
- token/cost metrics khi available;
- final task status.

## 11. Security

Retrieved content, MCP descriptions/results và tool output là untrusted. Tool selection không được thay đổi authorization policy. Credential scope phải theo least privilege.
