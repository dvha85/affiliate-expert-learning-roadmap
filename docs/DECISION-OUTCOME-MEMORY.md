# Decision / Outcome Memory — Bộ nhớ quyết định và kết quả

> Đây là business learning memory (bộ nhớ học từ vận hành), **không phải chat history** và không thay Knowledge Base/RAG/workflow state.

## 1. Mục tiêu

Hệ thống phải trả lời được:

```text
Ta đã quyết định gì?
Dựa trên evidence nào?
Confidence/uncertainty khi đó ra sao?
Policy cho phép gì?
Đã thực thi gì?
Outcome sau đó là gì?
Decision đó tốt/xấu ở điểm nào?
```

## 2. State separation

```text
Knowledge Base
≠
Session / Conversation State
≠
Durable Workflow State
≠
Decision / Outcome Memory
```

Decision/Outcome Memory lưu history để evaluation/calibration, không dùng làm nơi chứa mọi prompt/message.

## 3. Logical schema

```yaml
decision:
  decision_id:
  subject:
  created_at:
  decision_type:
  evidence_refs: []
  confidence:
  uncertainty: []
  freshness: {}
  reason_codes: []
  risk_level:
  policy_decision:

action:
  action_intent_id:
  execution_id:
  action_type:
  executed_at:
  result:

outcome:
  observed_at:
  window:
  metrics: {}
  adverse_events: []

evaluation:
  task_success:
  outcome_quality:
  calibration_error:
  notes:
```

Không phải decision nào cũng có action/outcome ngay. Hệ thống phải hỗ trợ pending/unknown outcome.

## 4. Outcome window

Một action có thể cần nhiều window:

```text
1h
24h
7d
30d
```

Chọn theo business effect, không dùng một window cố định cho mọi decision.

## 5. Counterfactual / baseline

Khi có thể, so outcome với:

- previous baseline;
- control/experiment variant;
- expected value forecast;
- no-action historical comparable.

Không claim causality chỉ từ before/after nếu experiment design không hỗ trợ.

## 6. Learning loop

```text
Decision
→ Action
→ Outcome
→ Evaluation
→ Proposed Improvement
→ Offline Test / Experiment
→ Review
→ Deploy
```

**Không**:

```text
Outcome
→ Agent silently rewrites production policy/prompt/weights
```

Agent/learning loop **không tự rewrite production policy/prompt/weights**. Mọi thay đổi production phải qua versioned change + test/evaluation/review phù hợp.

## 7. Những gì có thể học từ memory

- confidence calibration;
- scoring/ranking weight hypotheses;
- model routing quality;
- prompt/workflow improvements;
- alert threshold proposals;
- data/freshness gaps;
- experiment ideas;
- policy false-positive/false-negative review proposals.

Policy authority không được tự sửa chỉ vì model thấy pattern.

## 8. Data quality

Outcome phải có provenance/time window. Missing outcome không được coi như failure/success mặc định.

Đánh dấu:

- `OUTCOME_PENDING`;
- `OUTCOME_UNKNOWN`;
- `OUTCOME_PARTIAL`;
- `OUTCOME_FINAL` khi business definition cho phép.

## 9. Privacy / retention

Không lưu raw personal/sensitive data chỉ vì “memory”. Ưu tiên IDs, aggregate metrics, safe references/hash và retention policy phù hợp.

## 10. Evaluation usage

Decision/Outcome Memory là nguồn cho `AGENT-EVALUATION-STANDARD.md`, nhưng cần tránh leakage: nếu đánh giá model trên case đã nằm trong prompt/memory training-like context thì phải ghi rõ để không đánh giá sai chất lượng generalization.