# AI Capability Levels — Cấp năng lực AI A0–A4

Tài liệu này chuẩn hóa mức quyền của AI trong Build-First để **AI xuất hiện đúng lúc nhưng authority tăng dần theo evidence và risk controls**.

## A0 — Deterministic Only (Chỉ logic xác định)

Phù hợp M00–M04.

Cho phép:

- parsing/validation;
- snapshot/history;
- deterministic scoring/ranking;
- scheduler/change detection.

Không cần model call để ship core capability.

## A1 — AI Advisory / Read-Only (AI tư vấn / chỉ đọc)

Phù hợp từ M05 đến M10.

Cho phép:

- summarize (tóm tắt);
- classify (phân loại);
- extract structured facts (trích xuất dữ kiện có cấu trúc);
- correlate evidence (liên kết bằng chứng);
- generate hypothesis (tạo giả thuyết);
- explain anomaly/ranking/experiment;
- recommend investigation hoặc decision candidate.

Không cho phép AI tự external execute. Output phải có structured contract, evidence và confidence khi dùng cho quyết định.

## A2 — Tool-Assisted Agent (Agent dùng công cụ)

Phù hợp M11–M12.

Agent được phép gọi tool theo registry/contract. Mỗi tool phải có:

- schema;
- read/write category;
- permission;
- risk ceiling;
- timeout/retry/idempotency behavior;
- approval requirement;
- audit fields.

Tool result và remote description vẫn là untrusted input. Model không được tự mở rộng quyền tool.

## A3 — Governed Action Agent (Agent hành động có kiểm soát)

Phù hợp M13–M14.

Agent có thể tạo `ActionIntent` nhưng execution authority thuộc Policy/Risk Engine.

```text
ActionIntent
→ PolicyDecision
→ RiskLevel
   ├─ RISK 0 → auto
   ├─ RISK 1 → auto + mandatory audit
   └─ RISK 2 → durable Human Approval → revalidate → execute/reject
```

Bắt buộc có audit, idempotency, expiry/revalidation và kill switch cho side-effect scope phù hợp.

## A4 — Optional Multi-Agent (Đa Agent tùy chọn)

Chỉ cân nhắc ở M15 nếu có independent agent/service boundary thật, ví dụ Product Intelligence Agent và Revenue Agent được deploy/quản trị độc lập.

Không dùng multi-agent chỉ để workflow trông nâng cao hơn. Trong cùng Go application, interface/function/workflow nội bộ thường đơn giản và dễ audit hơn.

A2A hoặc agent-to-agent protocol là optional implementation choice; không phải dependency mặc định.

## Quy tắc nâng cấp level

Không nâng AI level chỉ vì model/framework mới xuất hiện. Chỉ nâng khi:

1. business value rõ;
2. deterministic baseline tồn tại;
3. failure modes đã biết;
4. evidence/evaluation đủ;
5. permission/risk boundary đã thiết kế;
6. fallback và operational cost chấp nhận được.

## Ma trận quyền

| Capability | A0 | A1 | A2 | A3 | A4 |
|---|:---:|:---:|:---:|:---:|:---:|
| deterministic compute | ✓ | ✓ | ✓ | ✓ | ✓ |
| AI analysis | — | ✓ | ✓ | ✓ | ✓ |
| read tool | — | giới hạn | ✓ | ✓ | ✓ |
| internal write | — | — | policy | policy | policy |
| external side effect | — | — | intent only / policy | governed | governed |
| Human Approval | — | — | khi tool yêu cầu | bắt buộc cho RISK2 | bắt buộc cho RISK2 |
| multi-agent | — | — | — | không mặc định | optional |

## Invariant

```text
CAPABILITY LEVEL
≠
LEARNER PASS
```

Level mô tả quyền kỹ thuật của bot, không phải điểm số learner.