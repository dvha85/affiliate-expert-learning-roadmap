# Agent HITL Runtime — Human-in-the-loop bền vững

> HITL (Human-in-the-loop — con người trong vòng kiểm soát) là workflow boundary có state, không chỉ là “AI viết rồi người đọc lại”.

## 1. Flow chuẩn

```text
DecisionPacket
→ ActionIntent
→ persist canonical action state
→ Policy Engine
→ persist PolicyDecision
→ RiskLevel
   ├─ RISK 0 → execute theo policy
   ├─ RISK 1 → execute + mandatory audit
   └─ RISK 2
       → create + persist ApprovalRequest
       → orchestrator PAUSE/WAIT
       → human approve/reject/expire/cancel
       → persist ApprovalDecision
       → reload canonical state
       → revalidate
       → policy/risk re-check
       → execute hoặc terminate
       → persist ExecutionRecord
```

## 2. Canonical state phải persist ngoài runtime history

Invariant bắt buộc:

```text
n8n execution state/history
≠ canonical Action / Approval / Execution state
```

Canonical store/domain contract phải lưu tối thiểu:

- decision ID và DecisionPacket reference/version;
- ActionIntent + version;
- PolicyDecision/risk result + policy version;
- ApprovalRequest;
- ApprovalDecision actor/time/reason;
- expiry;
- safe evidence/context references;
- idempotency key;
- canonical action state;
- ExecutionRecord/result;
- audit timestamps/correlation ID.

Orchestrator có thể lưu `workflow_execution_id`, workflow version và runtime status để correlation/debug, nhưng **không được là nguồn duy nhất** để chứng minh approval, authorization hoặc execution outcome.

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

Lưu actor/time/reason vào canonical action state.

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

Runtime/provider có thể hỗ trợ serialize/pause/resume trực tiếp, n8n có thể wait/resume workflow, hoặc Go workflow layer có thể điều phối state. Đây là implementation detail.

Business state machine phải đọc lại **canonical persisted state** trước resume. Workflow memory/history không được thay canonical authorization record.

## 7. Failure / restart

Test ít nhất:

- process/orchestrator restart trong lúc chờ approval;
- workflow execution history không còn nhưng canonical approval/action state vẫn đọc được;
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

## 9. Runtime ownership

```text
Go/domain store
= canonical Decision / ActionIntent / Policy / Approval / Execution records

n8n/orchestrator
= route, wait, resume, retry, integration execution

Agent
= analyze/propose within permission
```

```text
orchestrator says "success"
≠ business action is canonically authorized/successful
```

## 10. Metrics

Theo dõi:

- approval-required rate;
- approve/reject rate;
- approval latency;
- expired/cancelled requests;
- revalidation failures;
- duplicate-prevention events;
- runtime-recovery events;
- human intervention rate;
- outcome sau approved actions.
