# Autonomy and Approval Model — Mô hình tự chủ và phê duyệt

> Governance standard (chuẩn quản trị) cho Bot có thể tự hành động trong phạm vi cho phép, trong khi con người giữ quyền duyệt các consequential actions (hành động có hậu quả đáng kể).

Tiếng Việt là ngôn ngữ chính. Các entity/code identifier như `ActionIntent`, `PolicyDecision`, `ApprovalRequest` giữ nguyên tiếng Anh để dùng thống nhất trong code/schema; phần giải thích dùng tiếng Việt. Xem [`LANGUAGE-POLICY.md`](LANGUAGE-POLICY.md) và [`GLOSSARY-VI.md`](GLOSSARY-VI.md).

## 1. Goal — Mục tiêu

Hệ thống đích không phải **fully manual (hoàn toàn thủ công)** và cũng không phải **unconstrained autonomy (tự chủ không giới hạn)**.

Mục tiêu là:

```text
Observe (Quan sát)
→ Analyze (Phân tích)
→ tạo ActionIntent (Ý định hành động)
→ classify RiskLevel (Phân loại mức rủi ro)
→ PolicyDecision (Quyết định chính sách)
→ tự execute HOẶC request Human Approval
→ Audit (Ghi vết)
→ Measure result (Đo kết quả)
```

Con người không babysit (canh) từng bước cơ học; con người giữ quyền ở quyết định/tình huống có hậu quả đáng kể.

## 2. Core entities — Các thực thể cốt lõi

### ActionIntent (Ý định hành động)

Mô tả action Bot **muốn** thực hiện trước khi hệ thống cho phép execution.

Minimum fields (trường tối thiểu):

```text
id
intent_type
requested_by
reason
inputs
expected_effect
risk_level
created_at
expires_at
idempotency_key
```

`ActionIntent` không phải quyền thực thi. Nó chỉ là đề xuất có cấu trúc để Policy Engine đánh giá.

### RiskLevel (Mức rủi ro)

```text
RISK 0 — routine / reversible / internal
         thường lệ / đảo ngược được / nội bộ

RISK 1 — controlled side effect + mandatory audit
         tác động có kiểm soát + bắt buộc ghi vết

RISK 2 — consequential + Human Approval required
         hậu quả đáng kể + bắt buộc con người duyệt
```

### PolicyDecision (Quyết định chính sách)

```text
ALLOW
ALLOW_WITH_AUDIT
REQUIRE_APPROVAL
DENY
```

Record (ghi lại) policy version và explanation/reason (giải thích/lý do) để quyết định có thể audit.

### ApprovalRequest (Yêu cầu phê duyệt)

Phải đủ context (ngữ cảnh) để người duyệt ra quyết định nhanh:

- điều gì sẽ xảy ra;
- vì sao Bot đề xuất;
- evidence/source provenance (bằng chứng/nguồn gốc dữ liệu);
- expected benefit (lợi ích kỳ vọng);
- risk/downside (rủi ro/mặt trái);
- expiry (hết hạn);
- exact side effect (tác động chính xác);
- rollback/compensation path (đường quay lui/bù lỗi) nếu có.

### ApprovalDecision (Quyết định phê duyệt)

```text
APPROVE
REJECT
EXPIRE
CANCEL
```

Lưu decision time, actor và reason.

### ExecutionRecord (Bản ghi thực thi)

Ghi tối thiểu:

- ActionIntent;
- PolicyDecision;
- ApprovalDecision nếu có;
- execution attempt(s) (các lần thử thực thi);
- external request/result IDs;
- idempotency key;
- final state;
- error/compensation;
- measured result.

## 3. Ví dụ RiskLevel

### RISK 0

Thường là internal/read-only actions (hành động nội bộ/chỉ đọc):

- thu thập Product data;
- refresh snapshot;
- tính metrics;
- cập nhật ranking cache;
- tạo internal report;
- detect anomaly (phát hiện bất thường);
- tạo alert (cảnh báo).

### RISK 1

Ví dụ có thể được policy cho tự chạy nhưng bắt buộc audit:

- đổi internal Product priority;
- bật/tắt watcher;
- tạo draft;
- điều chỉnh bounded experiment configuration (cấu hình thử nghiệm trong giới hạn);
- cập nhật internal recommendation state.

RISK 1 phải có policy bounds (giới hạn chính sách) rõ ràng, không phải “Bot thích thì làm”.

### RISK 2

Thường cần Human Approval:

- publish nội dung ra ngoài;
- spend money (tiêu tiền);
- thay account/platform settings;
- xóa dữ liệu quan trọng;
- gửi consequential external communication;
- thay production/security configuration;
- action có material legal/compliance impact.

Risk classification chính xác phụ thuộc policy/scope và có thể thay đổi theo context.

## 4. Approval workflow — Workflow phê duyệt

```text
ActionIntent
→ Policy Engine
→ REQUIRE_APPROVAL
→ persist workflow state
→ create ApprovalRequest
→ notify human
→ wait durably (chờ bền vững)
   ├── APPROVE → resume → revalidate → execute
   ├── REJECT  → terminate
   ├── EXPIRE  → terminate / re-plan
   └── CANCEL  → terminate
→ audit final state
```

Diễn giải:

```text
Ý định hành động
→ Bộ máy chính sách
→ Yêu cầu phê duyệt
→ Lưu state workflow
→ Tạo yêu cầu phê duyệt
→ Báo cho người duyệt
→ Chờ bền vững
→ Duyệt / Từ chối / Hết hạn / Hủy
→ Ghi vết trạng thái cuối
```

## 5. Revalidation before execution — Kiểm lại trước thực thi

Approval không có nghĩa “được phép thực thi mãi mãi”. Ngay trước execution phải re-check:

- approval chưa hết hạn;
- Product/price/commission còn current (hiện hành);
- policy version còn áp dụng;
- action chưa chạy rồi;
- credential/permission còn hợp lệ;
- external target còn tồn tại;
- risk không tăng lên.

Nếu material context (ngữ cảnh quan trọng) đã thay đổi, tạo ApprovalRequest mới thay vì dùng approval cũ.

## 6. Idempotency — Tính lặp an toàn

Mọi side-effecting action (hành động tạo tác động bên ngoài) phải có idempotency strategy.

Idempotency nghĩa là retry cùng operation không âm thầm tạo thêm external side effect trùng lặp ngoài ý muốn.

Ví dụ key:

```text
publish:<content-id>:<version>
alert:<event-id>:<channel>
workflow:<workflow-id>:<step>
```

Retry không được biến một intent thành nhiều lần publish/spend/send ngoài dự kiến.

## 7. Kill Switch — Công tắc dừng khẩn cấp

Production autonomous system cần tối thiểu:

- global execution disable (tắt mọi execution);
- action-type disable (tắt một loại action);
- platform/tool disable;
- emergency credential revocation path;
- khả năng tiếp tục collection/analysis trong khi side effect bị tắt.

Behavior ưu tiên:

```text
ANALYZE may continue
ACT can be disabled independently

PHÂN TÍCH có thể tiếp tục
HÀNH ĐỘNG có thể bị tắt độc lập
```

## 8. Human experience principle — Nguyên tắc trải nghiệm người vận hành

Operator nên review **decision (quyết định)**, không babysit từng mechanical step (bước cơ học).

Approval tốt phải có concise decision packet (gói quyết định ngắn, đủ thông tin), không bắt người duyệt đọc raw logs để hiểu Bot đang muốn làm gì.

## 9. Metrics — Chỉ số vận hành

Theo dõi tối thiểu:

- auto-execution rate;
- approval-required rate;
- approval acceptance/rejection rate;
- approval latency;
- expired requests;
- duplicate-prevention events;
- policy blocks;
- rollback/compensation rate;
- human intervention rate;
- outcome sau approved action so với auto action.

Các metric này dùng để tối ưu mức tự chủ mà không làm mất control.

## 10. Anti-patterns — Cách làm cần tránh

Không:

- để LLM tự assign risk và tự approve high-risk action của chính nó;
- dùng chat message làm approval record duy nhất;
- giữ approval state chỉ trong process memory;
- execute sau approval khi critical facts đã thay đổi đáng kể;
- retry side effect khi chưa có idempotency;
- để kill switch phụ thuộc vào chính agent workflow đang lỗi;
- classify mọi thứ thành RISK 2 khiến con người trở thành bottleneck.