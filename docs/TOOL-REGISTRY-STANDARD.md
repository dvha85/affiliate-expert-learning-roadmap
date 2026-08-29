# Tool Registry Standard — Chuẩn đăng ký công cụ

> Áp dụng từ A2/M12. Tool tồn tại không đồng nghĩa Agent được quyền dùng trong mọi workflow.

## 1. Namespace

Ưu tiên nhóm tool theo domain:

```text
product.*
market.*
content.*
tracking.*
revenue.*
experiment.*
policy.*
platform.*
```

Namespace giúp tool discovery (khám phá tool), giảm schema surface và dễ áp permission/risk policy.

## 2. Metadata bắt buộc

Mỗi tool cần contract tương đương:

```yaml
name:
namespace:
purpose:
input_schema:
output_schema:
permission: READ_ONLY | INTERNAL_WRITE | EXTERNAL_SIDE_EFFECT
risk_ceiling: RISK_0 | RISK_1 | RISK_2
timeout:
retry_policy:
idempotency:
requires_approval:
audit_fields: []
```

## 3. Permission

- `READ_ONLY`: đọc/collect/query;
- `INTERNAL_WRITE`: ghi state nội bộ có kiểm soát;
- `EXTERNAL_SIDE_EFFECT`: publish/send/spend/change/delete hoặc tác động ngoài hệ thống.

Model không được tự nâng permission hoặc risk ceiling.

## 4. Deferred discovery

Khi tool surface lớn, runtime có thể chỉ load namespace/tool cần cho task thay vì gửi toàn bộ schema vào model context.

```text
Task
→ Tool Search / Discovery
→ load relevant namespace
→ validate allowed tools
→ invoke
```

Đây là capability tùy provider/runtime. Core registry phải hoạt động độc lập với một implementation cụ thể.

## 5. Tool result

Tool output cũng là untrusted input. Trước khi vào domain/Decision core cần:

- schema validation;
- provenance/source identity;
- timestamp/freshness;
- error classification;
- sensitive-data filtering khi relevant.

## 6. External side effects

External tool không được tự do tham gia programmatic/batch orchestration nếu không có explicit policy.

```text
Agent proposes
→ ActionIntent
→ Policy/Risk
→ approval nếu cần
→ Executor/tool
```

## 7. Tool identity và audit

Audit nên có:

- tool name/version/namespace;
- server/provider identity khi relevant;
- validated arguments hoặc safe hash/reference;
- permission/risk level;
- policy/approval result;
- external correlation ID;
- latency/result/error.

## 8. Adoption rule

Không thêm MCP/tool framework chỉ vì integration có thể dùng nó. REST/webhook/native SDK/file import vẫn đúng khi đơn giản, an toàn và dễ vận hành hơn.