# Agent Security and Tool Governance — Bảo mật Agent và quản trị công cụ

> Security standard (chuẩn bảo mật) cho Affiliate Bot và AI Agent có khả năng gọi tool (công cụ).

Tiếng Việt là ngôn ngữ chính. English terminology và code/entity identifiers được giữ khi cần độ chính xác kỹ thuật. Xem [`LANGUAGE-POLICY.md`](LANGUAGE-POLICY.md) và [`GLOSSARY-VI.md`](GLOSSARY-VI.md).

## 1. Core principle — Nguyên tắc cốt lõi

```text
MODEL OUTPUT IS UNTRUSTED INPUT
(ĐẦU RA MÔ HÌNH LÀ ĐẦU VÀO KHÔNG ĐƯỢC TIN CẬY MẶC ĐỊNH)
```

Nói cách khác:

```text
Model output (đầu ra mô hình)
≠
Execution permission (quyền thực thi)
```

LLM có thể recommend (đề xuất) action, nhưng production authorization (quyền thực thi trong production) phải đến từ explicit system policy + permission (chính sách và quyền rõ ràng của hệ thống).

## 2. Threat Model — Mô hình đe dọa

Affiliate Agent có thể đọc untrusted content (nội dung không đáng tin mặc định) từ:

- Product description;
- Seller page;
- website;
- review/comment;
- email/message;
- uploaded file;
- API response;
- RAG document;
- MCP resource/tool metadata.

Nội dung này có thể chứa malicious/misleading instructions (chỉ dẫn độc hại/gây hiểu sai) nhằm thay đổi behavior của Agent.

Prompt Injection (tấn công/chỉ dẫn tiêm vào prompt) phải được xử lý giống hostile input (đầu vào thù địch) đi qua Trust Boundary (ranh giới tin cậy), không phải chỉ là lỗi viết prompt.

## 3. Tool categories — Phân loại công cụ

Mỗi tool phải khai báo tối thiểu:

```text
name
purpose
input schema
output schema
read/write
side-effect level
required permission
risk ceiling
timeout/retry behavior
idempotency behavior
approval requirement
audit fields
```

### READ_ONLY (Chỉ đọc)

Ví dụ:

- lấy Product metadata;
- đọc Analytics;
- xem current policy snapshot.

### INTERNAL_WRITE (Ghi nội bộ)

Ví dụ:

- cập nhật internal ranking;
- lưu draft;
- ghi experiment result.

### EXTERNAL_SIDE_EFFECT (Tác động bên ngoài)

Ví dụ:

- publish;
- gửi message;
- thay account configuration;
- spend money.

Tool có external side effect phải mặc định có policy/risk/approval chặt hơn.

## 4. Least Privilege — Quyền tối thiểu cần thiết

Không cấp một universal credential (credential toàn quyền) cho Agent khi capability có thể tách scope.

Ưu tiên:

```text
collector credential → read scope (quyền đọc)
publisher credential → publish scope (quyền xuất bản)
billing credential   → isolated high-risk scope (quyền rủi ro cao tách biệt)
```

Tool access phải được cấp theo workflow/role, không chỉ vì tool tồn tại trong registry.

## 5. Prompt Injection Boundary — Ranh giới chống Prompt Injection

Không coi retrieved content (nội dung truy xuất) là system-level instruction.

Kiến trúc ưu tiên:

```text
UNTRUSTED CONTENT (Nội dung không tin cậy)
→ parser / normalizer
→ data model
→ model reasoning context
→ proposed ActionIntent
→ policy engine
→ permission check
→ approval nếu cần
→ tool execution
```

Control quan trọng:

- tách instruction và data;
- chỉ đưa context cần thiết;
- giới hạn tool set theo task;
- validate tool arguments;
- reject unknown field/target khi phù hợp;
- dùng allowlist (danh sách cho phép) cho sensitive destination;
- không cho retrieved text thay authorization policy;
- consequential side effect phải qua deterministic policy/approval.

## 6. Tool Misuse Controls — Kiểm soát lạm dụng công cụ

Trước side-effecting tool call, xác minh:

1. Tool này có được phép trong workflow hiện tại không?
2. Target (đích) được yêu cầu có nằm trong phạm vi cho phép không?
3. Arguments có đúng schema không?
4. Action có nằm trong risk/policy limit không?
5. Approval có bắt buộc không và nếu có thì còn valid không?
6. Action đã execute trước đó chưa?
7. Current context có đủ fresh (mới) để thực thi không?

## 7. MCP Governance — Quản trị MCP

MCP tăng interoperability (khả năng liên thông) nhưng **không làm mọi tool trở nên đáng tin**.

Với MCP server/client:

- verify server origin/configuration;
- giới hạn exposed tools/resources;
- coi remote description/result là untrusted data;
- scope credential;
- áp dụng cùng risk/approval policy như native tool;
- ghi server/tool identity và protocol/runtime metadata vào audit trace khi liên quan;
- review protocol/security change qua freshness process.

## 8. Generated Code / Command Execution — Chạy code/lệnh do model sinh

Không cho Agent chạy arbitrary generated shell/code (lệnh/code tùy ý do model sinh) trong privileged production environment.

Nếu thật sự cần code execution:

- isolate/sandbox (cô lập);
- giới hạn filesystem/network/credential access;
- đặt time/resource limits;
- tách read-only analysis và production writes;
- yêu cầu approval cho consequential output/action.

## 9. Secrets — Bí mật hệ thống

Không đặt long-lived secret vào prompt, log hoặc RAG document.

Dùng:

- secret manager/environment injection;
- short-lived token khi có thể;
- scoped credential;
- rotation/revocation;
- redaction (che dữ liệu nhạy cảm) trong log/trace.

## 10. Audit Requirements — Yêu cầu ghi vết

Với action quan trọng, lưu:

```text
workflow_id
action_intent_id
model/provider/version khi liên quan
prompt/template version khi liên quan
tool identity
validated arguments hoặc safe hash/reference
policy version
risk level
approval decision
execution result
external correlation id
trace id
timestamps
```

Không lưu sensitive raw data chỉ vì tiện debug.

## 11. Kill Switch and Containment — Dừng khẩn cấp và khoanh vùng

Hệ thống phải hỗ trợ tắt:

- toàn bộ external actions;
- một action category;
- một platform/tool;
- một agent/workflow.

Collection và analysis có thể tiếp tục trong khi execution bị tắt.

## 12. Evaluation and Red-Team Cases — Đánh giá và tình huống tấn công mô phỏng

Tối thiểu phải thử:

- Product text độc hại yêu cầu Agent bỏ qua rule;
- tool argument injection;
- fake approval content;
- stale approval sau khi Product/price thay đổi;
- duplicate execution sau retry;
- MCP tool description bị compromise/sai;
- credential quá rộng;
- model đề xuất platform manipulation bị cấm;
- hidden instruction trong retrieved content.

## 13. Anti-patterns — Cách làm cần tránh

Tránh:

- `LLM → privileged tool` không có policy boundary;
- một credential dùng cho mọi integration;
- tin MCP/server metadata như authorization;
- log secret/full personal data;
- coi Prompt Injection chỉ là prompt-writing problem;
- giả định Human Approval có thể bù cho tool permission thiết kế kém;
- cho cùng một Agent tự sửa policy đang giới hạn chính nó.