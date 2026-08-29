# Bản đồ Mission ↔ Knowledge

Đây là lớp mapping (ánh xạ) just-in-time tập trung. Tài liệu cố ý tránh bulk-edit front matter của 671 Lesson.

## Ý nghĩa ba mức kiến thức

- **REQUIRED (Bắt buộc cho Mission)** — phải hiểu đủ để Mission PASS.
- **ON-DEMAND (Lấy khi phát sinh nhu cầu)** — pull khi implementation/business context làm lộ nhu cầu cụ thể.
- **REFERENCE (Tham khảo)** — hữu ích để đào sâu nhưng không phải Mission PASS gate.

Các Lesson ID explicit phải resolve trong canonical inventory 671 bài. Khi Mission đã `ready`, ưu tiên **Lesson ID cụ thể + knowledge slice** thay vì theme mơ hồ.

```text
REQUIRED FOR MISSION
≠
FULL LESSON PASS
```

## AI capability mapping

```text
M00–M04 → A0 deterministic
M05–M10 → A1 AI advisory/read-only
M11–M12 → A2 tool-assisted Agent
M13–M14 → A3 governed action Agent
M15     → A4 optional multi-agent
```

AI level mô tả quyền kỹ thuật của Bot, không phải learner PASS.

## M00 — Khởi động Affiliate Bot

**REQUIRED**

- `0.1` — Affiliate Expert là gì?
  - slice: affiliate là business system, vai trò Affiliate Expert, hiểu trước khi automate thật.
- `0.2` — Affiliate Bot Engineer là gì?
  - slice: Bot Engineer biến business logic thành hệ thống; deterministic trước AI; Decision ≠ Execution.

**ON-DEMAND**

- Go tối thiểu để đọc `package main`, `func`, slice và test learner workspace.

**REFERENCE**

- Part 15 formal Bot Engineering mastery để sau.

## M01 — Product Ingest

**REQUIRED**

- `38.1` — Core marketplace entities.
  - slice: Product identity và field cốt lõi.
- `51.1` — Go runtime, modules và project structure.
  - slice: struct/type/package đủ để tạo Product model.
- `52.3` — File Import.
  - slice: local file làm data source đầu tiên.
- `52.7` — Validation.
  - slice: syntax validation khác business validation.

**ON-DEMAND**

- Platform-specific fields chỉ khi có adapter thật;
- error wrapping/JSON details khi lỗi thực tế yêu cầu.

## M02 — Product Store & History

**REQUIRED**

- `38.2` — ProductSnapshot và dữ liệu lịch sử.
- `39.1` — Snapshot.
- `51.3` — PostgreSQL, Redis và data access.
  - slice: repository boundary, migration/schema, persistence contract; chưa cần Redis.

**ON-DEMAND**

- PostgreSQL driver/integration wiring khi thực sự bật local DB;
- data lineage/provenance sâu hơn khi có nguồn ngoài.

## M03 — Product Ranking đầu tiên

**REQUIRED**

- `5.11` — Expected Value.
- `27.3` — Ranking.

**ON-DEMAND**

- Demand, Product–Audience Fit, price, CVR, valid-order/refund risk, seller/product quality khi tiến tới M06.

**REFERENCE**

- advanced statistical ranking và AI scoring để sau.

## M04 — Product Watcher

**AI level:** A0.

**REQUIRED themes**

- snapshot/delta semantics;
- scheduler;
- context/cancellation.

**ON-DEMAND**

- bounded concurrency khi collection tuần tự thành bottleneck thật.

## M05 — Reliable Alerts + AI Alert Triage

**AI level:** A1 — advisory/read-only.

**REQUIRED themes**

- rule/threshold;
- timeout;
- retry/backoff;
- idempotency/deduplication;
- structured alert evidence;
- AI summary/classification/urgency chỉ như advisory layer;
- deterministic fallback khi AI unavailable.

**ON-DEMAND**

- `61.5` Structured Output và `65.x` evaluation khi author M05 cần AI output schema/eval cụ thể.

## M06 — Product Intelligence + AI Product Research

**AI level:** A1.

**REQUIRED themes**

- Parts 2, 6, 7, 8: economics + market + customer + product intelligence;
- AI extraction từ unstructured product/review/seller evidence thành structured features;
- source grounding, product fidelity, confidence/uncertainty.

**Rule:** AI có thể extract/explain; deterministic engine vẫn chịu trách nhiệm score/rank baseline.

## M07 — Content Intelligence

**AI level:** A1.

**REQUIRED themes**

- Parts 9–11: content/psychology + traffic context + funnel/conversion;
- content signal extraction/analysis phải giữ provenance và policy state.

## M08 — Revenue & Attribution Intelligence + Investigator

**AI level:** A1.

**REQUIRED themes**

- Parts 2, 3, 11–13: economics, tracking/attribution, funnel, data, analytics;
- anomaly investigation: hypotheses + evidence + missing evidence + confidence;
- AI không sửa transaction/reconciliation truth.

## M09 — Experiment Engine + AI Copilot

**AI level:** A1.

**REQUIRED themes**

- Part 14 experimentation/statistics;
- AI được generate hypothesis/interpret/propose next experiment;
- statistical engine vẫn tính result và uncertainty chính thức;
- Part 18 adaptive experimentation khi learner tiến tới bandit/ML scope.

## M10 — Decision Intelligence & Policy Engine

**AI level:** A1.

**REQUIRED themes**

- Parts 8, 13, 15, 16 và relevant Part 18 signals;
- Rule/Score/Rank/Forecast/Experiment evidence + AI AnalysisPacket → Decision Fusion;
- `DecisionPacket` phải có evidence/confidence/uncertainty/freshness/expiry;
- Decision ≠ Execution;
- RiskLevel + PolicyDecision vẫn là deterministic/governed authority.

## M11 — AI Analysis Assistant

**AI level:** A2.

**REQUIRED themes**

- Part 17: grounding, structured output, LLM workflow, evaluation, state separation;
- model routing theo task/value/risk;
- provider-neutral AI interface;
- analysis trajectory và cost/latency evaluation.

## M12 — Tool-Using Agent

**AI level:** A2.

**REQUIRED themes**

- explicit tool contract;
- tool registry/discovery;
- validation + permissions + risk ceiling;
- MCP khi hữu ích;
- bounded orchestration để lấy missing evidence;
- external side-effect tool không được bypass Policy/Risk.

## M13 — Governed Automation

**AI level:** A3.

**REQUIRED themes**

- ActionIntent;
- RISK 0/1/2;
- durable Human Approval;
- expiry/revalidation;
- audit/idempotency.

## M14 — Production Agentic Bot

**AI level:** A3.

**REQUIRED themes**

- Part 19: recovery, observability, security, least privilege, kill switch, cost;
- agent/tool/decision tracing;
- trajectory evaluation;
- decision latency/cost/failure metrics.

## M15 — Affiliate Intelligence Platform

**AI level:** A4 optional.

**REQUIRED themes**

- Part 21 capstone integration;
- Signal → Analysis → Decision → Action → Outcome → Evaluation closed loop;
- Decision/Outcome memory;
- multi-agent/A2A chỉ khi có independent remote-agent boundary thật.

## Quy tắc refine

Khi Mission được author `ready`, thay theme-level pulls bằng **tập Lesson ID nhỏ nhất thực sự cần cho Mission PASS**, kèm knowledge slice cụ thể. Không thêm hàng trăm mapping dự đoán trước khi có Mission thực tế.