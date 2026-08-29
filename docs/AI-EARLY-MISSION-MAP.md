# AI Early Mission Map — Bản đồ AI tư vấn từ M05 đến M10

Tài liệu này làm rõ cách A1 AI advisory xuất hiện sớm nhưng không làm thay đổi Mission spine hoặc quyền execution.

| Mission | AI use case | Trigger | AI output | Downstream authority |
|---|---|---|---|---|
| M05 | Alert Triage | material product/change alert | priority/summary/cause analysis | rule/human |
| M06 | Product Research | product/review/seller evidence mới | structured features/risks/angles | deterministic Product Intelligence |
| M07 | Content Intelligence support | content/performance evidence mới | content feature/quality analysis | analytics/human |
| M08 | Revenue Investigator | anomaly/reconciliation mismatch | hypotheses/evidence/missing data | reconciliation/analytics |
| M09 | Experiment Copilot | experiment design/result event | hypothesis/interpretation/next test | experiment/statistics policy |
| M10 | Decision Analyst | Decision Fusion needs analysis | AnalysisPacket | Decision/Policy Engine |

## Quy tắc chung

```text
M05–M10 = A1
```

A1 được phép:

- READ;
- ANALYZE;
- EXTRACT;
- SUMMARIZE;
- CLASSIFY;
- RECOMMEND;
- ABSTAIN / REQUEST MORE EVIDENCE.

A1 không được:

- external publish;
- spend money;
- change account/platform settings;
- delete important data;
- bypass experiment budget/policy;
- assign itself execution permission.

## M05 gate

Core reliable alert phải hoạt động deterministic trước. AI triage là enrichment layer.

PASS-level architecture khi M05 được author:

```text
change detection works
+ retry/idempotency works
+ alert exists without AI
+ AI triage can enrich alert
+ invalid/unsupported AI output is rejected
```

## M06 gate

AI extracted feature chỉ trở thành scoring input khi:

1. schema hợp lệ;
2. source/evidence ref tồn tại;
3. field semantics rõ;
4. uncertainty được giữ nếu source mơ hồ.

Không dùng raw LLM score như Product Intelligence truth.

## M08 gate

AI investigation phải tách:

```text
observed facts
hypotheses
missing evidence
recommended checks
```

Không mutate revenue/order ledger từ hypothesis.

## M09 gate

Statistical result là canonical experiment evidence; AI interpretation là analysis layer.

Nếu AI và statistical engine conflict, lưu conflict làm evaluation case thay vì để AI override result.

## M10 gate

M10 tiêu thụ `AnalysisPacket` nhưng tạo `DecisionPacket` qua Decision Fusion. AI assessment chỉ là một evidence channel.

## Chiến lược cost/latency

Không gọi AI theo timer khi không có material change.

```text
Signal/Event
→ materiality gate
→ AI advisory nếu expected information value đáng giá
```

Ghi ít nhất:

- invocation reason;
- model/provider capability class;
- latency;
- cost;
- result status;
- fallback used hay không.

## Knowledge reuse

Các pattern này dùng knowledge hiện có ở Parts 13/14/16/17/18. Không tạo Lesson mới trong migration Agentic Decision Intelligence v1.