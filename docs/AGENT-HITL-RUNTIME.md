# Agent HITL Runtime — Human-in-the-loop bền vững

> HITL (Human-in-the-loop — con người trong vòng kiểm soát) là workflow boundary có state, không chỉ là “AI viết rồi người đọc lại”.

## 1. Flow chuẩn

```text
DecisionPacket
→ ActionIntent
→ Policy Engine
→ RiskLevel
   ├─ RISK 0 → execute theo policy
   ├─ RISK 1 → execute + mandatory audit
   └─ RISK 2
       → persist workflow/action state
       → create ApprovalRequest
       → PAUSE
       → human approve/reject/expire/cancel
       → reload state
       → revalidate
       → policy/risk re-check
       → execute hoặc terminate
```

## 2. State phải persist

Không giữ approval wait chỉ trong process memory.

Lưu tối thiểu:

- workflow/run ID;
- decision ID;
- ActionIntent;
- policy/risk result;
- ApprovalRequest;
- expiry;
- safe evidence references;
- idempotency key;
- current state;
- audit timestamps.

## 3. ApprovalRequest

Người duyệt cần một decision packet ngắn nhưng đủ:

- bot muốn làm gì;
- vì sao;
- evidence chính;
- confidence/uncertainty;
- expected benefit;
- downside/risk;
- exact external side effect;
- expiry;
- rollback/compensation path nếu có.

Mục tiêu là duyệt **decision**, không bắt con người đọc raw logs.

## 4. Approval decisions

```text
APPROVE
REJECT
EXPIRE
CANCEL
```

Lưu actor/time/reason theo scope phù hợp.

## 5. Revalidation bắt buộc

Approval không phải permission vĩnh viễn.

Trước execute lại kiểm:

- approval chưa hết hạn;
- DecisionPacket chưa hết hạn;
- product/price/commission/eligibility còn phù hợp;
- policy version còn valid;
- risk không tăng;
- credential/permission còn hợp lệ;
- target còn tồn tại;
- idempotency/action state chưa complete.

Nếu material context đổi:

```text
DO NOT EXECUTE OLD APPROVAL
→ create/recompute DecisionPacket
→ request approval mới nếu vẫn RISK2
```

## 6. Resume semantics

Runtime/provider có thể hỗ trợ serialize/pause/resume trực tiếp, hoặc Go workflow layer tự persist state. Đây là implementation detail; business state machine phải nhất quán.

## 7. Failure / restart

Test ít nhất:

- process restart trong lúc chờ approval;
- duplicate approve callback;
- approval đến sau expiry;
- target thay đổi sau approval;
- tool timeout sau approval;
- retry executor không tạo duplicate side effect;
- kill switch bật trước resume.

## 8. Kill switch

Kill switch phải có thể chặn execution dù approval đã tồn tại.

```text
ANALYZE may continue
ACT can be disabled independently
```

## 9. Current implementation reference

Freshness register `BOT-ENGINEERING-REFRESH-2026.08.md` ghi current Agent runtime reference cho pattern interrupt → serialize run state → approve/reject → resume.

Đó chỉ là implementation reference:

```text
SDK approval mechanism
≠
Business Policy/Risk authority
```

## 10. Metrics

Theo dõi:

- approval-required rate;
- approve/reject rate;
- approval latency;
- expired/cancelled requests;
- revalidation failures;
- duplicate-prevention events;
- human intervention rate;
- outcome sau approved actions.