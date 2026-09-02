# AI advisory map — M04 đến M07

V2 deliberately keeps M00–M03 free of AI authority: M00 is human-only market
action, M01 is a measurement snapshot, and M02–M03 establish deterministic
baseline/history. AI starts only when it has evidence and a fallback boundary.

| Mission | Use case | AI output | Authority còn lại |
|---|---|---|---|
| M04 | Grounded product/outcome explanation | structured claims + evidence refs + uncertainty | deterministic/history + human |
| M05 | Experiment copilot | hypothesis/interpretation/next measurement | preregistered test + human review |
| M06 | Alert triage | priority/summary/cause hypotheses | deterministic alert path |
| M07 | Decision analysis | AnalysisPacket | deterministic Decision/Policy boundary |

```text
M04–M07 = A1 advisory/read-only
AI output = untrusted input
Decision ≠ Execution
```

## Gate chung

- evidence có source/freshness;
- structured output được validate;
- unsupported claim bị reject;
- confidence có method/reason;
- deterministic fallback chạy khi AI unavailable;
- latency/cost/privacy được ghi;
- model không có tool hoặc external action authority.

## M04 bắt đầu bằng evaluation

Trước provider call thật: human label một case set nhỏ, lưu deterministic
baseline/history, định nghĩa schema/rubric, test missing/stale/conflict/
prompt-injection, rồi mới thử AI adapter. Output nghe hay không phải PASS nếu
không grounded hoặc không tốt hơn baseline trên metric đã định nghĩa.
