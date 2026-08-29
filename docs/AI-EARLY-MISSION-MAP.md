# AI advisory map — M02 đến M07

AI xuất hiện sau human/deterministic baseline và trước tool/action authority.

| Mission | Use case | AI output | Authority còn lại |
|---|---|---|---|
| M02 | Grounded product research | structured claims + evidence refs + uncertainty | deterministic score/human |
| M03 | Content draft/critique | draft + claim/evidence map | human review và manual publish |
| M04 | Outcome investigation | hypotheses + missing evidence | analytics/reconciliation |
| M05 | Experiment copilot | hypothesis/interpretation/next measurement | preregistered experiment + human |
| M06 | Alert triage | priority/summary/cause hypotheses | deterministic alert path |
| M07 | Decision analysis | AnalysisPacket | deterministic Decision/Policy boundary |

~~~text
M02–M07 = A1 advisory/read-only
AI output = untrusted input
Decision ≠ Execution
~~~

## Gate chung

- evidence có source/freshness;
- structured output được validate;
- unsupported claim bị reject;
- confidence có method/reason;
- deterministic fallback chạy khi AI unavailable;
- latency/cost/privacy được ghi;
- model không có tool hoặc external action authority.

## M02 bắt đầu bằng evaluation

Trước provider call thật:

1. human label một case set nhỏ;
2. lưu deterministic baseline;
3. định nghĩa schema/rubric;
4. test missing/stale/conflict/prompt-injection;
5. chỉ sau đó mới thử AI adapter.

M03–M07 tái sử dụng cùng evaluation/evidence contract và thêm metric phù hợp use case. Output nghe hay không phải PASS nếu không grounded hoặc không tốt hơn baseline trên metric đã định nghĩa.
