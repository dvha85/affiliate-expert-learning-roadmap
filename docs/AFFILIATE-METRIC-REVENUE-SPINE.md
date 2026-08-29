# Affiliate Metric & Revenue Spine

Tài liệu này định nghĩa metric/revenue chain dùng xuyên M00–M11. Mục tiêu là giữ Affiliate Intelligence gắn với **measured business reality**, không tối ưu một proxy rời rạc như commission rate.

## 1. Canonical funnel

Dùng event nào source thực sự cung cấp; không bịa event bị thiếu.

```text
Impression / Exposure
→ View
→ Engagement
→ Click
→ Product View
→ Add to Cart
→ Checkout
→ Order
→ Valid Order
→ Final Commission
→ Payment (nếu observable)
```

Một platform có thể chỉ cung cấp subset của chain. Event không observable phải là `unknown`/`not_available`, không đổi thành `0`.

## 2. Minimum revenue model

Ở mức tối thiểu:

```text
Clicks = Exposure × CTR
Orders = Clicks × CVR
Valid Orders = Orders × Valid Order Rate
Expected Affiliate Revenue = Valid Orders × Commission per Valid Order
```

Gộp lại:

```text
Expected Affiliate Revenue
= Exposure
× CTR
× CVR
× Valid Order Rate
× Commission per Valid Order
```

Nếu chưa có exposure và chỉ đang ra quyết định trên một click/opportunity:

```text
Expected Value per Click
= P(Order | Click)
× P(Valid | Order)
× Commission per Valid Order
```

Commission rate chỉ là một input upstream của `Commission per Valid Order`; nó không đủ để quyết định product opportunity.

## 3. Evidence state cho từng factor

Mỗi factor phải có state độc lập:

```text
observed
estimated
assumed
unknown
```

Ví dụ:

| Factor | Value | State | Evidence |
|---|---:|---|---|
| Exposure | 1,200 | observed | platform export, observed_at |
| CTR | 2.5% | observed | 30 clicks / 1,200 exposure |
| CVR | 4% | estimated | small historical sample |
| Valid Order Rate | unknown | unknown | chưa có source |
| Commission/Valid | 80,000 VND | observed | affiliate program terms/export |

Không nhân một chain rồi gọi kết quả là “data-driven” nếu phần lớn factor là assumption mà không ghi rõ.

## 4. Derived metrics

Chỉ tính khi denominator observable và có cùng scope/window:

```text
CTR = Click / Exposure
CVR = Order / Click
Valid Order Rate = Valid Order / Order
Refund/Invalid Rate = Invalid or Refunded Order / Order
EPC = Final Commission / Click
Revenue per Exposure = Final Commission / Exposure
```

Nếu denominator bằng `0`, metric ratio phải theo explicit undefined policy; không tự suy thành `0%` nếu semantics không cho phép.

## 5. Mission progression

| Mission | Metric maturity |
|---|---|
| M00 | commission/price chỉ là baseline scenario; conversion probability vẫn unknown nếu chưa đo |
| M01 | cùng metric có provenance, timestamp, history và freshness |
| M02 | AI có thể giải thích/hypothesize nhưng không overwrite metric truth |
| M03 | pre-register target metric, expected direction và outcome window trước publish |
| M04 | import real exposure/click/order/valid/final commission khi source hỗ trợ; tách test events |
| M05 | chọn bottleneck theo funnel và experiment một thay đổi chính |
| M06 | watcher tự động thu signal đã hiểu với retry/dedup/freshness |
| M07 | DecisionPacket tham chiếu metric window/confidence/missing evidence |
| M08 | read-only tools chỉ lấy missing factor có decision value |
| M09 | ActionIntent giữ expected outcome/cost/risk nhưng chưa có permission |
| M10 | canary đo outcome, intervention, cost và policy block trong bounds |
| M11 | decision → action → outcome → revenue/evaluation trace end-to-end |

## 6. Bottleneck diagnosis

```text
No exposure
→ distribution/channel hypothesis

Exposure but no click
→ audience/angle/hook/CTA hypothesis

Click but no order
→ product–audience fit / landing / offer hypothesis

Order but invalid/refunded
→ product quality / seller quality / expectation / compliance hypothesis

Metrics missing or conflicting
→ measurement/instrumentation hypothesis
```

Không được nhảy tới automation/AI optimization khi measurement layer chưa phân biệt được các bottleneck trên.

## 7. Window and cohort integrity

Mọi comparison phải ghi:

- time window;
- channel/scope;
- product/offer version;
- content/action version;
- test vs real event;
- pending/partial/final status;
- known attribution limits.

Không so hai rate từ scope/window khác nhau mà không ghi limitation.

## 8. Revenue truth states

Order lifecycle phải tách khi source hỗ trợ:

```text
ORDER_PENDING
ORDER_VALID
ORDER_INVALID
ORDER_REFUNDED
COMMISSION_PENDING
COMMISSION_FINAL
COMMISSION_PAID
```

`Order` không đồng nghĩa `revenue`. `Commission pending` không đồng nghĩa `paid`.

## 9. Decision rule

Metric spine phục vụ decision, không thay decision contract.

```text
Evidence + Funnel Metrics + Opportunity Signals
→ Expected Value / bottleneck assessment
→ Affiliate Intelligence Decision
→ Risk / Policy
→ Action or Abstention
→ Outcome
→ Evaluation
```

Nguyên tắc:

> **DATA > OPINION**
>
> **EXPECTED VALUE > COMMISSION RATE**
>
> **MISSING ≠ ZERO**
>
> **ORDER ≠ VALID ORDER ≠ FINAL/PAID COMMISSION**
