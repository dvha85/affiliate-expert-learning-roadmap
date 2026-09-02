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
data scope / minimisation contract khi có dữ liệu người dùng
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

Nhưng permission least privilege chưa đủ. Một credential có thể chỉ có quyền đọc mà vẫn cho Agent lấy nhiều dữ liệu hơn mục đích cần thiết.

Invariant:

```text
Agent can technically read data
≠ Agent needs that data
```

và:

```text
publicly obtainable
≠ automatically appropriate to collect/store/process
```

## 5. `DataAccessContext` — Ngữ cảnh truy cập dữ liệu

Khi tool/Agent có thể xử lý personal/customer/account data hoặc dữ liệu nhạy cảm theo context, task/session/tool contract phải khai báo tối thiểu phần liên quan:

```yaml
purpose:
data_scope:
personal_data_class:
minimum_data_required:
retention_policy:
downstream_sharing:
redaction_policy:
legal_or_policy_basis_ref:
```

Không phải tool public-product metadata nào cũng cần full shape. Mục tiêu là khiến boundary dữ liệu rõ **khi có rủi ro**, không biến mọi read-only call thành paperwork.

### Purpose limitation — Giới hạn mục đích

Tool chỉ lấy dữ liệu phục vụ task đã khai báo.

Ví dụ:

```text
Task: reconcile campaign clicks
→ cần campaign ID + aggregate click metrics
```

không tự tạo quyền:

```text
→ tải toàn bộ customer profile/contact history
```

Nếu task đổi purpose materially, phải tạo context/authorization mới thay vì silently reuse data.

### Data minimisation — Tối thiểu hóa dữ liệu

Ưu tiên aggregate/pseudonymous/reference data khi đủ cho quyết định.

```text
need campaign outcome
→ campaign-level aggregate
```

ưu tiên hơn:

```text
→ raw user-level identifiers
```

nếu raw identifiers không cần để đạt Mission outcome.

### Retention — Thời hạn lưu

Không giữ raw personal/sensitive data vô thời hạn chỉ vì audit/debug thuận tiện.

Tách:

```text
canonical business evidence cần giữ
vs
raw sensitive payload chỉ dùng tạm cho processing
```

Retention phải phù hợp purpose/current policy và có deletion/expiry behavior khi cần.

### Downstream sharing — Chia sẻ xuống hệ thống khác

Trước khi chuyển dữ liệu sang LLM provider, n8n node, MCP server, external API hoặc logging backend, phải kiểm:

- downstream có thật sự cần data đó không;
- scope nào được chia sẻ;
- có thể redact/tokenize/reference thay raw value không;
- secret/personal data có bị model-visible/log-visible ngoài ý muốn không;
- current policy/legal boundary có cho phép không.

### Redaction — Che dữ liệu

Auditability không đồng nghĩa lưu raw sensitive value. Ưu tiên:

```text
safe ID / hash / reference
+ metadata cần cho trace
```

thay vì full personal data trong prompt/log/trace.

## 6. Prompt Injection Boundary — Ranh giới chống Prompt Injection

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

## 7. Tool Misuse Controls — Kiểm soát lạm dụng công cụ

Trước side-effecting tool call, xác minh:

1. Tool này có được phép trong workflow hiện tại không?
2. Target (đích) được yêu cầu có nằm trong phạm vi cho phép không?
3. Arguments có đúng schema không?
4. Action có nằm trong risk/policy limit không?
5. Approval có bắt buộc không và nếu có thì còn valid không?
6. Action đã execute trước đó chưa?
7. Current context có đủ fresh (mới) để thực thi không?
8. Data scope có phù hợp purpose/minimum necessary không?
9. Downstream destination có được phép nhận data class đó không?

## 8. MCP Governance — Quản trị MCP

MCP tăng interoperability (khả năng liên thông) nhưng **không làm mọi tool trở nên đáng tin**.

Với MCP server/client:

- verify server origin/configuration;
- giới hạn exposed tools/resources;
- coi remote description/result là untrusted data;
- scope credential;
- áp dụng cùng risk/approval policy như native tool;
- áp dụng cùng `DataAccessContext`/minimisation/redaction boundary khi MCP tool xử lý personal/sensitive data;
- ghi server/tool identity và protocol/runtime metadata vào audit trace khi liên quan;
- review protocol/security change qua freshness process.

## 9. Generated Code / Command Execution — Chạy code/lệnh do model sinh

Không cho Agent chạy arbitrary generated shell/code (lệnh/code tùy ý do model sinh) trong privileged production environment.

Nếu thật sự cần code execution:

- isolate/sandbox (cô lập);
- giới hạn filesystem/network/credential access;
- đặt time/resource limits;
- tách read-only analysis và production writes;
- yêu cầu approval cho consequential output/action.

## 10. Secrets — Bí mật hệ thống

Không đặt long-lived secret vào prompt, log hoặc RAG document.

Dùng:

- secret manager/environment injection;
- short-lived token khi có thể;
- scoped credential;
- rotation/revocation;
- redaction (che dữ liệu nhạy cảm) trong log/trace.

Secret minimisation và personal-data minimisation là hai boundary liên quan nhưng không đồng nhất. Một payload có thể không chứa secret nhưng vẫn chứa personal data không cần thiết.

## 11. Audit Requirements — Yêu cầu ghi vết

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
DataAccessContext/ref khi relevant
```

Không lưu sensitive raw data chỉ vì tiện debug. Audit record nên chứng minh **ai/cái gì đã truy cập dữ liệu gì theo purpose nào** mà không mặc định copy toàn bộ payload vào trace.

## 12. Kill Switch and Containment — Dừng khẩn cấp và khoanh vùng

Hệ thống phải hỗ trợ tắt:

- toàn bộ external actions;
- một action category;
- một platform/tool;
- một agent/workflow.

Collection và analysis có thể tiếp tục trong khi execution bị tắt **chỉ trong data-access policy hiện hành**. Kill switch của external actions không cấp quyền thu dữ liệu rộng hơn.

## 13. Evaluation and Red-Team Cases — Đánh giá và tình huống tấn công mô phỏng

Tối thiểu phải thử:

- Product text độc hại yêu cầu Agent bỏ qua rule;
- tool argument injection;
- fake approval content;
- stale approval sau khi Product/price thay đổi;
- duplicate execution sau retry;
- MCP tool description bị compromise/sai;
- credential quá rộng;
- read-only tool trả thừa personal data so với task purpose;
- Agent cố mở rộng query/data scope để “có thêm context” mà không justified;
- downstream LLM/log/MCP destination nhận raw personal data không cần thiết;
- retention/debug artifact giữ raw sensitive data quá scope;
- model đề xuất platform manipulation bị cấm;
- hidden instruction trong retrieved content.

## 14. Anti-patterns — Cách làm cần tránh

Tránh:

- `LLM → privileged tool` không có policy boundary;
- một credential dùng cho mọi integration;
- `read_only = privacy_safe`;
- “public data” = “được phép collect/store vô hạn”;
- gửi full customer/account payload vào model khi aggregate/reference data đủ;
- giữ raw PII trong log/trace để debug lâu dài;
- tin MCP/server metadata như authorization;
- log secret/full personal data;
- coi Prompt Injection chỉ là prompt-writing problem;
- giả định Human Approval có thể bù cho tool permission/data boundary thiết kế kém;
- cho cùng một Agent tự sửa policy đang giới hạn chính nó.
