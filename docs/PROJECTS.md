# Hệ thống project

## 1. 14 main projects

| # | Project | Phần | Evidence cốt lõi |
|---:|---|---:|---|
| 1 | Affiliate Business Map | 1 | Ecosystem, money flow, role map |
| 2 | Tracking & Attribution Architecture | 3 | Event map, ID strategy, reconciliation |
| 3 | Niche Intelligence | 6 | Niche scorecard và quyết định chọn niche |
| 4 | Product Intelligence | 8 | Dataset, score, ranking, validation; grounded AI enrichment khi dùng |
| 5 | Real Content Portfolio | 9 | Nội dung thật và performance history |
| 6 | Funnel Analysis | 11 | Funnel map, drop-off, bottleneck, actions |
| 7 | Affiliate Data Warehouse | 12 | Schema, history, data quality, metrics |
| 8 | Analytics Dashboard | 13 | Dashboard ra quyết định được |
| 9 | Experiment System | 14 | Tối thiểu 10 experiments có hypothesis; AI copilot không thay statistical evidence |
| 10 | Product Tracker Bot | 15 | Go collector/workflow, history/provenance, reliable alerts + optional A1 triage |
| 11 | Opportunity Engine | 16 | Rule/score/rank/recommendation + evidence/confidence/uncertainty/freshness/risk/policy |
| 12 | AI Content Assistant | 17 | Grounded tool workflow, evaluation, prompt-injection controls, human approval |
| 13 | Production Affiliate Bot | 19 | Durable recovery, observability, security, RISK 0/1/2, kill switch, deployment |
| 14 | Affiliate Intelligence Platform | 21 | End-to-end governed action + audit/evaluation/feedback loop |

Số lượng main project vẫn là **14**. Labs và Pass Gates không phải Project #15+.

Mỗi project dùng [`templates/PROJECT-README.md`](../templates/PROJECT-README.md) và cần tối thiểu: scope, deliverables, acceptance criteria, evidence/demo, retrospective và next version.

A1 AI advisory patterns xem [`AI-ADVISORY-PATTERNS.md`](AI-ADVISORY-PATTERNS.md). AI output tồn tại **không tự động là Project evidence**; phải chứng minh grounding, schema validity, fallback và evaluation phù hợp.

## 2. AI advisory evidence cho Projects 4/7/9/10

### Project 4 — Product Intelligence

Nếu dùng AI Product Research, evidence phải cho thấy:

- unstructured source → structured extraction;
- mỗi fact/claim quan trọng có source/evidence ref;
- unsupported AI claim không đi vào scoring fact;
- uncertainty/missing evidence được giữ;
- deterministic score/ranking baseline vẫn chạy khi AI unavailable;
- ít nhất một extraction/evidence-quality evaluation case.

### Project 7 — Affiliate Data Warehouse

Nếu lưu AI analysis/revenue investigation:

- tách observed facts khỏi hypotheses;
- không ghi hypothesis đè transaction/reconciliation truth;
- AnalysisPacket có model/evidence metadata khi relevant;
- raw sensitive data không bị lưu chỉ để phục vụ prompt/evaluation.

### Project 9 — Experiment System

Nếu dùng AI Experiment Copilot:

- hypothesis/variant proposal phải lưu như proposal;
- primary metric/statistical result do Experiment Engine tính;
- AI interpretation tách khỏi measured result;
- conflict giữa AI interpretation và statistics phải trở thành evaluation/learning evidence;
- AI không được tự tăng experiment budget/action scope vượt policy.

### Project 10 — Product Tracker Bot

PASS core vẫn phải hoạt động không cần AI. Nếu thêm Alert Triage A1:

- deterministic alert được tạo trước AI enrichment;
- AI output có structured schema + evidence refs;
- AI unavailable vẫn giữ alert pipeline chạy;
- không để AI âm thầm suppress alert mà deterministic policy yêu cầu giữ;
- đo latency/cost và ít nhất một unsupported/invalid-output case.

## 3. Engineering acceptance — Projects 10–14

### Project 10 — Product Tracker Bot

PASS evidence phải cho thấy tối thiểu:

- Go implementation hoặc executable artifact theo primary track;
- collector/adapters có validation + provenance;
- bounded concurrency hoặc chứng minh không cần concurrency;
- timeout/cancellation;
- retry strategy + idempotency/dedup khi phù hợp;
- snapshot/history;
- alerting;
- basic logs/metrics;
- compliance/data-access boundary.

AI triage chỉ là enrichment A1, không thay các core gate trên.

### Project 11 — Opportunity Engine

PASS evidence phải có:

```text
input features / evidence
→ score/rank/recommendation
→ DecisionPacket
   evidence
   confidence
   uncertainty
   freshness/expiry
→ RiskLevel
→ PolicyDecision
```

Decision output không được tự động đồng nghĩa external execution. AI AnalysisPacket nếu có chỉ là một evidence channel trong Decision Fusion.

### Project 12 — AI Content Assistant

PASS evidence phải có:

- grounded/source-aware generation;
- explicit tool contracts nếu dùng tools/MCP;
- tool/input/output validation;
- evaluation cases;
- prompt-injection/tool-misuse test case;
- human approval boundary cho publish/consequential claims;
- audit/evidence của approve/reject.

### Project 13 — Production Affiliate Bot

PASS evidence phải chứng minh:

- process restart/recovery strategy;
- durable state cho long wait/approval khi workflow có nhu cầu;
- retry/backoff/timeout/idempotency;
- secrets/least privilege/tool permissions;
- service/workflow/tool/action tracing hoặc correlation;
- RISK 0/1/2 policy behavior;
- approval queue cho RISK 2;
- kill switch/containment;
- backup/restore hoặc recovery verification;
- cost/operational monitoring.

### Project 14 — Affiliate Intelligence Platform

Capstone phải demo được một closed loop:

```text
Observe / Collect
→ Signal
→ Analyze
→ DecisionPacket / ActionIntent
→ Policy + Risk
→ Auto action OR Human Approval
→ Execute
→ Audit / Trace
→ Measure outcome
→ Evaluate / Learn
↺
```

Acceptance phải bao gồm ít nhất một RISK 0/1 path, một RISK 2 approval path, một failure/retry/recovery case và evidence rằng model output không bypass policy.

## 4. Labs

Labs là work package tích hợp, thường effort `XL`.

| Lab | Vị trí | Vai trò | Project? |
|---|---|---|---|
| Affiliate Lab / orientation practice | Part 0 | Môi trường thực hành, baseline, evidence workflow | Không |
| Platform Policy Monitoring System | Part 5 | Theo dõi policy/rule và impact | Không |

Nếu syllabus chứa thêm lab, thêm theo đúng canonical scope; không tự đổi thành main project.

## 5. Pass Gates

Pass Gate:

- có acceptance criteria riêng;
- có evidence link;
- có thể reuse artifact lesson/project;
- chỉ tính effort incremental cho integration/review/hardening/demo;
- không double-count artifact đã tồn tại.

## 6. Evidence convention

- Lesson evidence: [`artifacts/README.md`](../artifacts/README.md)
- Project scope/acceptance: [`templates/PROJECT-README.md`](../templates/PROJECT-README.md)
- Experiment evidence: [`templates/EXPERIMENT-LOG.md`](../templates/EXPERIMENT-LOG.md)
- Retrospective: [`templates/RETROSPECTIVE.md`](../templates/RETROSPECTIVE.md)

Project/Lab/Pass Gate chỉ hoàn thành khi acceptance criteria và evidence tương ứng tồn tại; file/folder tồn tại không tự động nghĩa complete.
