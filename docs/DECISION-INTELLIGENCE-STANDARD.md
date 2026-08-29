# Decision Intelligence Standard — Chuẩn trí tuệ quyết định

> Áp dụng trọng tâm ở M10/Project 11. Mục tiêu là hợp nhất evidence từ nhiều nguồn thành quyết định có thể kiểm tra, thay vì để một model hoặc một score đơn lẻ quyết định.

## 1. Decision Fusion

```text
Rule Engine
+ Scoring / Ranking
+ Forecast / ML
+ Anomaly Signals
+ Experiment Evidence
+ AI AnalysisPacket
→ Decision Fusion
→ DecisionPacket
```

Không source nào được tự động có quyền override tất cả source khác nếu policy không quy định rõ.

## 2. Decision classes

Decision hợp lệ có thể là:

- `RECOMMEND`;
- `DO_NOT_RECOMMEND`;
- `WAIT`;
- `GET_MORE_DATA`;
- `HUMAN_REVIEW`;
- `CREATE_ACTION_INTENT`.

Không ép hệ thống luôn phải chọn một action khi evidence chưa đủ.

## 3. Evidence hierarchy

Ưu tiên theo source authority và freshness, không theo “AI nói tự tin”.

Ví dụ:

```text
validated transaction/order fact
> verified current platform/product fact
> deterministic derived metric
> experiment/forecast/model estimate
> AI interpretation/hypothesis
```

Hierarchy cụ thể phải do domain/policy định nghĩa.

## 4. Conflict handling

Khi evidence conflict:

```text
conflict detected
→ record conflict
→ assess freshness/source authority
→ request missing evidence nếu có
→ lower confidence hoặc WAIT/HUMAN_REVIEW
```

Không để model tự hòa giải conflict bằng cách tạo fact mới.

## 5. DecisionPacket requirements

M10+ phải dùng contract tại `DECISION-CONTRACTS.md`. Tối thiểu:

- evidence refs;
- deterministic scores/rules relevant;
- AI assessment nếu dùng;
- confidence;
- uncertainty;
- missing evidence;
- freshness;
- expiry/next recheck;
- reason codes;
- RiskLevel;
- PolicyDecision.

## 6. Confidence gating

Confidence không phải execution permission.

```text
high confidence + RISK2
≠
auto execute
```

Decision routing có thể dùng confidence để chọn `GET_MORE_DATA`, `HUMAN_REVIEW` hoặc mức reasoning model, nhưng external action authority vẫn ở Policy/Risk.

## 7. Freshness gating

Decision phải re-evaluate khi critical evidence quá cũ hoặc decision expired.

Critical facts thường gồm:

- price;
- commission;
- inventory/availability;
- seller/product eligibility;
- policy state;
- experiment/revenue data window.

## 8. Model routing

AI task được route theo complexity/value/risk, không dùng model mạnh nhất mặc định. Routing standard xem `MODEL-ROUTING-STANDARD.md`.

## 9. Observability

Mỗi decision nên log/trace tối thiểu:

- decision_id;
- trigger;
- evidence refs;
- model route nếu có;
- latency;
- cost;
- confidence/uncertainty;
- policy result;
- outcome link khi có.

## 10. Acceptance baseline

Decision Intelligence feature chưa đạt nếu chỉ demo một output đẹp. Phải có:

- deterministic baseline;
- conflict/missing-evidence case;
- stale-evidence case;
- explainable DecisionPacket;
- policy separation;
- evaluation evidence.