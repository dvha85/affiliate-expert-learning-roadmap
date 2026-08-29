# AI Advisory Patterns — Mẫu AI tư vấn/chỉ đọc

> Áp dụng AI Capability Level A1. AI được phân tích, trích xuất, giải thích và đề xuất nhưng **không có external execution authority**.

## 1. Pattern chung

```text
Deterministic Signal / Data
→ Evidence Package
→ AI Advisory Analysis
→ Structured AnalysisPacket
→ Deterministic Consumer / Human
```

Mọi pattern A1 phải có:

- deterministic input/provenance;
- structured output;
- evidence refs;
- confidence + uncertainty khi output ảnh hưởng quyết định;
- explicit missing evidence;
- deterministic fallback/degraded mode;
- latency/cost measurement;
- không external side effect.

## 2. Alert Triage — M06

```text
Change Detector
→ Rule/Threshold
→ Alert Candidates
→ AI Triage
   ├─ summarize
   ├─ classify
   ├─ correlate related signals
   ├─ estimate urgency
   └─ explain likely cause
→ Priority Alert Queue
```

Output gợi ý:

```yaml
alert_id:
summary:
category:
urgency:
evidence_refs: []
possible_causes: []
confidence:
uncertainty: []
```

AI không được:

- thay threshold mà không qua change/review flow;
- tự suppress alert quan trọng nếu deterministic policy yêu cầu giữ;
- execute product/content/account action.

Fallback:

```text
AI unavailable
→ deterministic alert vẫn được phát/lưu
→ analysis_status = unavailable
```

## 3. Product Research — M02

AI xử lý dữ liệu phi cấu trúc như description, review, seller text, policy notes, customer comments rồi normalize thành structured evidence.

```text
Unstructured Evidence
→ AI Extraction
→ Structured Product Intelligence
→ validation/provenance
→ deterministic scoring/ranking
```

Output gợi ý:

```yaml
product_id:
audiences: []
pain_points: []
benefits: []
objections: []
content_angles: []
risk_signals: []
seller_signals: []
evidence_refs: []
confidence:
uncertainty: []
```

Rule:

```text
AI EXTRACTS / EXPLAINS
≠
AI INVENTS PRODUCT TRUTH
```

Product claims phải trace được về source. AI-generated feature không có evidence không được trở thành scoring fact.

## 4. Outcome / Attribution Investigation — M04

Trigger bằng anomaly hoặc reconciliation mismatch.

```text
Revenue/Attribution Signal
→ collect tracking/order/refund/commission/product history
→ AI Investigator
→ ranked hypotheses + evidence + missing evidence
```

Output:

```yaml
incident_id:
hypotheses:
  - cause:
    evidence_refs: []
    confidence:
alternative_hypotheses: []
missing_evidence: []
recommended_checks: []
```

AI không được rewrite order/commission ledger truth. Transaction reconciliation vẫn deterministic/data-driven.

## 5. Experiment Copilot — M05

AI đứng quanh statistical engine, không thay statistical engine.

```text
Context
→ AI propose hypothesis/variants
→ Experiment Engine runs
→ Statistics computes result
→ AI interprets result/confounders
→ proposes next experiment
```

Cho phép:

- hypothesis generation;
- variant ideation;
- interpretation;
- confounder checklist;
- next-experiment proposal.

Không cho phép:

- đổi primary metric sau khi thấy result mà không ghi protocol change;
- gọi result “winner” trái statistical/evidence gate;
- tự tăng budget/action scope vượt experiment policy.

## 6. Confidence và abstention

AI phải được phép **abstain (không kết luận)**.

```text
insufficient evidence
→ missing_evidence
→ WAIT / GET_MORE_DATA / HUMAN_REVIEW
```

Không ép model luôn phải chọn một cause/product/variant.

## 7. Evaluation tối thiểu

A1 feature cần đo:

- structured-output validity;
- evidence coverage;
- unsupported-claim rate;
- classification/extraction correctness;
- latency p50/p95;
- cost / task;
- fallback success;
- human usefulness khi có review.

## 8. Security

Input từ product/review/web/platform là untrusted content. AI advisory output cũng là untrusted input cho downstream system. Không cho content được retrieval thay đổi permission/policy.
