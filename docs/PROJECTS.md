# Hệ thống project

## 1. 14 main projects

| # | Project | Phần | Evidence cốt lõi |
|---:|---|---:|---|
| 1 | Affiliate Business Map | 1 | Ecosystem, money flow, role map |
| 2 | Tracking & Attribution Architecture | 3 | Event map, ID strategy, reconciliation |
| 3 | Niche Intelligence | 6 | Niche scorecard và quyết định chọn niche |
| 4 | Product Intelligence | 8 | Dataset, score, ranking, validation |
| 5 | Real Content Portfolio | 9 | Nội dung thật và performance history |
| 6 | Funnel Analysis | 11 | Funnel map, drop-off, bottleneck, actions |
| 7 | Affiliate Data Warehouse | 12 | Schema, history, data quality, metrics |
| 8 | Analytics Dashboard | 13 | Dashboard ra quyết định được |
| 9 | Experiment System | 14 | Tối thiểu 10 experiments có hypothesis |
| 10 | Product Tracker Bot | 15 | Go collector/workflow, history/provenance, reliable alerts |
| 11 | Opportunity Engine | 16 | Rule/score/rank/recommendation + reason/confidence/risk/policy |
| 12 | AI Content Assistant | 17 | Grounded tool workflow, evaluation, prompt-injection controls, human approval |
| 13 | Production Affiliate Bot | 19 | Durable recovery, observability, security, RISK 0/1/2, kill switch, deployment |
| 14 | Affiliate Intelligence Platform | 21 | End-to-end governed action + audit/evaluation/feedback loop |

Số lượng main project vẫn là **14**. Labs và Pass Gates không phải Project #15+.

Mỗi project dùng [`templates/PROJECT-README.md`](../templates/PROJECT-README.md) và cần tối thiểu: scope, deliverables, acceptance criteria, evidence/demo, retrospective và next version.

## 2. Engineering acceptance — Projects 10–14

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

### Project 11 — Opportunity Engine

PASS evidence phải có:

```text
input features
→ score/rank/recommendation
→ reason/evidence/confidence
→ RiskLevel
→ PolicyDecision
```

Decision output không được tự động đồng nghĩa external execution.

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
→ Analyze
→ Recommend / ActionIntent
→ Policy + Risk
→ Auto action OR Human Approval
→ Execute
→ Audit / Trace
→ Measure outcome
→ Evaluate / Learn
↺
```

Acceptance phải bao gồm ít nhất một RISK 0/1 path, một RISK 2 approval path, một failure/retry/recovery case và evidence rằng model output không bypass policy.

## 3. Labs

Labs là work package tích hợp, thường effort `XL`.

| Lab | Vị trí | Vai trò | Project? |
|---|---|---|---|
| Affiliate Lab / orientation practice | Part 0 | Môi trường thực hành, baseline, evidence workflow | Không |
| Platform Policy Monitoring System | Part 5 | Theo dõi policy/rule và impact | Không |

Nếu syllabus chứa thêm lab, thêm theo đúng canonical scope; không tự đổi thành main project.

## 4. Pass Gates

Pass Gate:

- có acceptance criteria riêng;
- có evidence link;
- có thể reuse artifact lesson/project;
- chỉ tính effort incremental cho integration/review/hardening/demo;
- không double-count artifact đã tồn tại.

## 5. Evidence convention

- Lesson evidence: [`artifacts/README.md`](../artifacts/README.md)
- Project scope/acceptance: [`templates/PROJECT-README.md`](../templates/PROJECT-README.md)
- Experiment evidence: [`templates/EXPERIMENT-LOG.md`](../templates/EXPERIMENT-LOG.md)
- Retrospective: [`templates/RETROSPECTIVE.md`](../templates/RETROSPECTIVE.md)

Project/Lab/Pass Gate chỉ hoàn thành khi acceptance criteria và evidence tương ứng tồn tại; file/folder tồn tại không tự động nghĩa complete.
