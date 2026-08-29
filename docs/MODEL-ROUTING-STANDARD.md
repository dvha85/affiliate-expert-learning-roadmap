# Model Routing Standard — Chuẩn định tuyến mô hình

## 1. Nguyên tắc

Không dùng model mạnh/đắt nhất cho mọi task.

```text
Task
→ classify complexity/value/risk
→ select capability class
→ execute
→ evaluate latency/cost/quality
```

## 2. Capability classes

### FAST

Dùng cho:

- extraction;
- classification;
- summarization;
- routine triage.

Mục tiêu: latency/cost thấp, schema validity cao.

### STANDARD

Dùng cho:

- investigation có nhiều evidence;
- ambiguous classification;
- experiment interpretation;
- multi-document synthesis.

### REASONING

Dùng khi:

- evidence xung đột;
- decision có Expected Value cao;
- investigation phức tạp;
- cần multi-step reasoning mà deterministic pipeline chưa đủ.

## 3. Không route policy authority

```text
Model Routing
≠
Policy Routing
```

RiskLevel/PolicyDecision không được chuyển cho “model mạnh hơn” để thay deterministic policy.

## 4. Router inputs

Router có thể dùng:

- task type;
- evidence volume;
- ambiguity/conflict;
- expected decision value;
- latency budget;
- cost budget;
- privacy/data constraints;
- provider availability;
- evaluation history.

## 5. Fallback

Mỗi route cần:

- provider/model unavailable path;
- timeout path;
- invalid structured-output path;
- downgrade/upgrade rule;
- deterministic fallback khi task core cho phép.

## 6. Escalation

```text
FAST fails quality/schema
→ STANDARD

STANDARD finds material conflict
→ REASONING hoặc HUMAN_REVIEW
```

Không loop model escalation vô hạn. Đặt max attempts/cost/time budget.

## 7. Provider neutrality

Routing target là capability class, không phải hard-coded permanent model name trong domain core.

Exact provider/model mapping nằm config/freshness layer.

## 8. Metrics

Theo dõi:

- route distribution;
- task success per route;
- schema failure;
- latency p50/p95;
- cost/task;
- escalation rate;
- human intervention rate;
- outcome quality/calibration.

## 9. Adoption rule

Chỉ thay default route khi evaluation evidence chứng minh cải thiện cost/latency/quality hoặc reliability. Không đổi vì benchmark marketing đơn lẻ.