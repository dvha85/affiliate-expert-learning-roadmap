# Programmatic Tool Orchestration — Điều phối tool có chương trình và giới hạn

## 1. Mục tiêu

Khi cần đọc nhiều dữ liệu, Agent không nên luôn lặp:

```text
model → tool → model → tool → model → tool
```

Runtime có thể dùng bounded orchestration để loop/branch/parallel read calls rồi đưa aggregate result về reasoning step.

## 2. Pattern

```text
Investigation Plan
→ bounded program
   ├─ product.get_history(...)
   ├─ revenue.get_commission(...)
   ├─ tracking.get_metrics(...)
   └─ platform.get_policy_snapshot(...)
→ validate each result
→ aggregate evidence
→ model reasons once
```

## 3. Scope mặc định

Cho phép tốt nhất với:

- `READ_ONLY` tools;
- bounded/internal computations;
- một số `INTERNAL_WRITE` nếu transaction/idempotency/policy rõ.

Không cho free orchestration của:

- publish;
- spend;
- account/security change;
- destructive delete;
- consequential external messaging.

## 4. Guardrails

Bắt buộc:

- allowlisted tools;
- max calls/concurrency/time/cost;
- schema validation;
- per-tool timeout;
- cancellation;
- deterministic aggregation where practical;
- trace toàn bộ tool trajectory;
- partial-failure handling.

## 5. Parallelism

Parallel read chỉ dùng khi source/tool rate limits và consistency semantics cho phép. More concurrency không đồng nghĩa better latency nếu downstream bị rate-limit.

## 6. Failure handling

Nếu một subset fail:

- classify missing evidence;
- không silently treat missing value as zero/false;
- decide retry/skip/abstain;
- reflect uncertainty trong AnalysisPacket.

## 7. Implementation references

Một số Agent runtime/provider hiện hỗ trợ generated-code/programmatic tool coordination. Repo coi đây là **implementation reference**, không phải domain invariant.

Nếu provider không hỗ trợ, cùng concept có thể triển khai deterministic trong Go workflow layer.

## 8. Evaluation

So sánh với sequential agent loop:

- task success;
- number of model turns;
- tool calls;
- latency;
- cost;
- rate-limit/failure rate;
- evidence completeness.

Chỉ adopt nếu measurement cho thấy value thật.