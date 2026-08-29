# Confidence & Uncertainty — Độ tin cậy và bất định

## 1. Mục tiêu

Không dùng một con số confidence để che giấu việc thiếu dữ liệu. Decision Intelligence phải biểu diễn rõ:

```text
what we know
what we infer
what we do not know
what evidence conflicts
```

## 2. Confidence không phải probability truth

Model self-reported confidence không được hiểu tự động là xác suất quyết định đúng.

Confidence nên là field đã normalize theo task/evaluation hoặc ít nhất là indicator để routing/review.

## 3. Uncertainty classes

Gợi ý phân loại:

- `DATA_MISSING` — thiếu dữ liệu;
- `DATA_STALE` — dữ liệu cũ;
- `SOURCE_CONFLICT` — nguồn mâu thuẫn;
- `MODEL_DISAGREEMENT` — model/algorithm khác nhau;
- `LOW_SAMPLE` — sample nhỏ;
- `REGIME_CHANGE` — platform/policy/market regime thay đổi;
- `UNKNOWN` — chưa xác định nguyên nhân.

## 4. Abstention

System phải cho phép:

```text
WAIT
GET_MORE_DATA
HUMAN_REVIEW
```

Abstention tốt hơn fabricated certainty.

## 5. Confidence calibration

Khi có outcome history, đánh giá:

- high-confidence decisions có thật sự đúng nhiều hơn không;
- calibration error;
- confidence theo task type;
- confidence theo model/provider route;
- confidence khi data stale/missing.

## 6. Routing examples

```text
confidence high + evidence fresh + low risk
→ recommendation may proceed to policy

confidence low + missing read evidence
→ fetch permitted data

source conflict material
→ human review hoặc wait

RISK2
→ approval bất kể model confidence cao
```

## 7. Evidence requirement

Mỗi confidence có ảnh hưởng DecisionPacket cần trace được về:

- evidence set;
- evaluation/calibration method nếu có;
- model/algorithm producing assessment;
- timestamp/data window.

## 8. Anti-patterns

Không:

- hard-code `confidence: 0.9` chỉ để schema đầy đủ;
- dùng verbal certainty thay evidence;
- cho LLM tự xác nhận confidence rồi auto execute;
- bỏ uncertainty khỏi UI/approval packet vì “gây khó hiểu”.