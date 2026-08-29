# Agent Evaluation Standard — Chuẩn đánh giá AI Agent

> Evaluation (đánh giá) của Agent không chỉ chấm câu trả lời cuối. Phải đánh giá **trajectory (quỹ đạo thực thi)** từ evidence → reasoning → tool → decision → policy → outcome.

## 1. Mục tiêu

Một Agent có output nghe hợp lý vẫn có thể kém nếu:

- chọn sai tool;
- gọi tool thừa;
- truyền argument sai;
- bỏ qua evidence quan trọng;
- dùng dữ liệu stale;
- tạo unsupported claim;
- bị policy chặn đúng nhưng vẫn cố gọi lại;
- latency/cost quá cao;
- quyết định cuối không cải thiện outcome.

## 2. Evaluation layers

```text
INPUT / EVIDENCE QUALITY
→ ANALYSIS QUALITY
→ TOOL TRAJECTORY
→ DECISION QUALITY
→ POLICY / SAFETY
→ EXECUTION QUALITY
→ BUSINESS OUTCOME
```

Không phải Mission nào cũng có đủ các layer; áp dụng theo capability/risk scope.

## 3. Core metrics

### Task / output

- `task_success` — task có hoàn tất đúng mục tiêu không;
- `structured_output_validity` — output có đúng schema không;
- `relevance` — output có trả đúng vấn đề không;
- `unsupported_claim_rate` — tỷ lệ claim không có evidence;
- `evidence_coverage` — evidence quan trọng có được sử dụng/đề cập không.

### Tool trajectory

- `tool_selection_accuracy` — chọn đúng tool không;
- `tool_argument_accuracy` — arguments đúng schema/semantics không;
- `unnecessary_tool_calls` — tool calls thừa;
- `tool_failure_recovery` — xử lý timeout/transient/permanent failure đúng không;
- `permission_denial_behavior` — bị deny thì có dừng/route đúng không.

### Decision

- `decision_accuracy_or_utility` — decision phù hợp truth/outcome thế nào;
- `confidence_calibration` — confidence có tương xứng outcome không;
- `stale_evidence_rate` — decision dùng evidence hết hạn/stale bao nhiêu;
- `abstention_quality` — khi thiếu evidence có WAIT/GET_MORE_DATA đúng lúc không;
- `decision_latency` — từ trigger đến DecisionPacket.

### Safety / governance

- `policy_block_accuracy` — policy chặn/cho đúng không;
- `risk_classification_quality` — RiskLevel theo expected policy;
- `approval_quality` — approval packet có đủ context để con người quyết định không;
- `prompt_injection_resistance` — untrusted content có thay authorization/tool behavior không;
- `duplicate_side_effect_prevention` — retry có tạo side effect trùng không.

### Operations / economics

- `cost_per_analysis`;
- `cost_per_decision`;
- latency p50/p95;
- model escalation rate;
- human intervention rate;
- retries/timeouts;
- availability/fallback success.

### Outcome

Khi có business outcome:

- revenue/commission delta;
- CTR/CVR/order/valid-order delta;
- refund/invalid-order impact;
- decision value vs baseline;
- `revenue_per_decision` hoặc metric phù hợp scope.

Không tối ưu một metric nếu làm xấu compliance/risk hoặc metric business chính.

## 4. Evaluation dataset

Tạo test/eval cases từ:

- known good/bad historical cases;
- synthetic boundary/failure cases;
- prompt injection/tool misuse cases;
- stale/missing/conflicting evidence;
- permission denied;
- tool timeout;
- RISK2 approval path;
- decision/outcome cases có ground truth đủ tốt.

Không dùng production personal/sensitive raw data nếu không cần.

## 5. Offline vs online evaluation

### Offline

Dùng trước deploy/change:

- replay known cases;
- compare model/prompt/router versions;
- check schema/tool/safety;
- estimate cost/latency.

### Online

Sau deploy có guardrails:

- task success;
- human intervention;
- policy blocks;
- decision/outcome linkage;
- cost/latency;
- drift/freshness failures.

## 6. Baseline-first

Mọi AI/Agent improvement nên so với baseline:

```text
deterministic baseline
hoặc
previous approved model/workflow
```

Không kết luận “tốt hơn” chỉ vì demo trông thông minh hơn.

## 7. Versioning

Evaluation record nên biết:

- workflow/prompt version;
- provider/model capability class/version khi relevant;
- tool registry version;
- policy version;
- data/eval dataset version;
- timestamp.

## 8. PASS principle

```text
AI OUTPUT EXISTS
≠
AGENT WORKS
```

Agent feature chỉ được coi là mature khi có evaluation evidence phù hợp với risk/cost của capability đó.