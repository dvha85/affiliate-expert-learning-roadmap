# Decision Contracts — Hợp đồng dữ liệu cho quyết định

Tài liệu này định nghĩa bốn contract (hợp đồng dữ liệu) xuyên suốt Decision Intelligence. Các ví dụ là logical schema, không bắt buộc một format serialize duy nhất.

```text
SignalPacket
→ AnalysisPacket
→ DecisionPacket
→ ActionIntent
```

## 1. SignalPacket

Mô tả một fact/change đã được deterministic system phát hiện.

Trường tối thiểu:

```yaml
signal_id:
subject:
signal_type:
observed_at:
source_refs: []
freshness:
values: {}
```

Yêu cầu:

- source/provenance phải truy được;
- timestamp rõ;
- không nhét model conclusion vào phần fact;
- dữ liệu stale phải được đánh dấu thay vì coi như current.

## 2. AnalysisPacket

Mô tả phân tích của rule/statistics/AI analyst.

```yaml
analysis_id:
subject:
summary:
evidence_refs: []
possible_causes: []
missing_evidence: []
confidence:
uncertainty: []
recommended_investigation: []
model_metadata: {}
```

`model_metadata` chỉ lưu khi relevant và không được chứa secret.

Quy tắc:

```text
CLAIM WITHOUT EVIDENCE
→ unsupported
```

Nếu AI không tìm thấy evidence, phải trả `missing_evidence` hoặc uncertainty thay vì bịa nguồn.

## 3. DecisionPacket

Đây là contract chính của M10+.

```yaml
decision_id:
subject:
decision_type:
created_at:
expires_at:
next_recheck_at:

deterministic:
  scores: {}
  rules: []
  ranking: {}

ai_assessment:
  recommendation:
  confidence:
  uncertainty: []

evidence_refs: []
missing_evidence: []

freshness: {}

recommended_action:
risk_level:
policy_decision:
reason_codes: []
```

### Trường bắt buộc về nghĩa

- **evidence_refs** — quyết định dựa trên dữ liệu nào;
- **confidence** — mức tin cậy của assessment, không phải xác suất đúng tuyệt đối;
- **uncertainty** — điều chưa biết hoặc evidence xung đột;
- **freshness** — tuổi/độ mới của facts quan trọng;
- **expires_at** — thời điểm decision không còn được execute mà không re-evaluate;
- **risk_level** — phân loại rủi ro theo policy;
- **policy_decision** — ALLOW / ALLOW_WITH_AUDIT / REQUIRE_APPROVAL / DENY hoặc equivalent contract hiện hành.

## 4. ActionIntent

Mô tả hành động được đề xuất trước khi thực thi.

```yaml
intent_id:
decision_id:
intent_type:
target:
inputs: {}
reason:
expected_effect:
risk_level:
created_at:
expires_at:
idempotency_key:
```

ActionIntent **không** đồng nghĩa execution permission.

```text
DecisionPacket
→ ActionIntent
→ Policy/Risk re-check
→ Approval nếu cần
→ Executor
```

## 5. State separation

Không trộn bốn loại dữ liệu:

```text
Fact/Signal
≠
Analysis
≠
Decision
≠
Execution Record
```

Điều này giúp audit được câu hỏi:

- hệ thống đã thấy gì;
- AI/rule đã phân tích gì;
- quyết định cuối là gì;
- policy cho phép gì;
- executor thực sự đã làm gì;
- outcome sau đó ra sao.

## 6. Revalidation

Trước external execution, revalidate các facts có thể đổi như:

- price;
- commission;
- inventory/availability;
- product/seller eligibility;
- policy version;
- approval expiry;
- action duplication/idempotency state.

Nếu context thay đổi material, DecisionPacket cũ phải hết hiệu lực hoặc tạo decision mới.

## 7. Provider neutrality

Không dùng provider-specific response object làm domain contract. Adapter phải normalize về các contract trên trước khi đi vào Decision/Policy core.