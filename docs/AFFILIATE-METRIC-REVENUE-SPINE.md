# Trục chỉ số và doanh thu Affiliate

Tài liệu này định nghĩa chuỗi chỉ số/doanh thu (`metric/revenue chain`) dùng xuyên M00–M11. Mục tiêu là giữ Affiliate Intelligence gắn với **thực tế kinh doanh đã đo được (`measured business reality`)**, không tối ưu một chỉ số thay thế (`proxy`) rời rạc như commission rate.

## 1. Phễu chuẩn (`canonical funnel`)

Chỉ dùng event mà nguồn thực sự cung cấp; không bịa event bị thiếu.

```text
Impression / Exposure (lượt hiển thị)
→ View (xem)
→ Engagement (tương tác)
→ Click (nhấp)
→ Product View (xem sản phẩm)
→ Add to Cart (thêm giỏ)
→ Checkout (thanh toán)
→ Order (đơn hàng)
→ Valid Order (đơn hợp lệ)
→ Final Commission (hoa hồng cuối cùng)
→ Payment (tiền được thanh toán, nếu quan sát được)
```

Một platform có thể chỉ cung cấp một phần của chuỗi. Event không quan sát được phải là `unknown`/`not_available`, không đổi thành `0`.

## 2. Mô hình doanh thu tối thiểu

Ở mức tối thiểu:

```text
Clicks = Exposure × CTR
Orders = Clicks × CVR
Valid Orders = Orders × Valid Order Rate
Expected Affiliate Revenue = Valid Orders × Commission per Valid Order
```

Tức là:

```text
Doanh thu Affiliate kỳ vọng
= Lượt hiển thị
× CTR
× CVR
× Tỷ lệ đơn hợp lệ
× Hoa hồng trên mỗi đơn hợp lệ
```

Nếu chưa có exposure và chỉ đang ra quyết định trên một click/opportunity:

```text
Expected Value per Click (giá trị kỳ vọng trên mỗi click)
= P(Order | Click)
× P(Valid | Order)
× Commission per Valid Order
```

Commission rate chỉ là một input ở thượng nguồn của `Commission per Valid Order`; nó không đủ để quyết định cơ hội sản phẩm.

## 3. Trạng thái bằng chứng cho từng yếu tố

Mỗi factor (yếu tố) phải có trạng thái độc lập:

```text
observed   # đã quan sát
estimated  # đã ước lượng
assumed    # đang giả định
unknown    # chưa biết
```

Ví dụ:

| Yếu tố | Giá trị | Trạng thái | Bằng chứng |
|---|---:|---|---|
| Exposure | 1,200 | observed | platform export, observed_at |
| CTR | 2.5% | observed | 30 clicks / 1,200 exposure |
| CVR | 4% | estimated | mẫu lịch sử nhỏ |
| Valid Order Rate | unknown | unknown | chưa có source |
| Commission/Valid | 80,000 VND | observed | điều khoản/export chương trình Affiliate |

Không nhân một chuỗi rồi gọi kết quả là “data-driven” nếu phần lớn factor là assumption mà không ghi rõ.

## 4. Chỉ số suy ra (`derived metrics`)

Chỉ tính khi mẫu số quan sát được và có cùng phạm vi/cửa sổ:

```text
CTR = Click / Exposure
CVR = Order / Click
Valid Order Rate = Valid Order / Order
Refund/Invalid Rate = Invalid or Refunded Order / Order
EPC = Final Commission / Click
Revenue per Exposure = Final Commission / Exposure
```

Nếu mẫu số bằng `0`, tỷ lệ phải tuân theo policy xử lý undefined đã định; không tự suy thành `0%` nếu semantics không cho phép.

## 5. `MeasurementContext` — ngữ cảnh đo lường bắt buộc từ M04

Tên metric và value chưa đủ để diễn giải outcome. Từ M04, analytics/outcome quan trọng phải reference một `MeasurementContext` (ngữ cảnh đo lường) hoặc equivalent canonical record.

Shape logic tối thiểu:

```yaml
measurement_context_id:
reporting_source:
reporting_scope:
tracking_id:
campaign_id:
attribution_model:
attribution_lookback_window:
reporting_timezone:
configuration_observed_at:
import_validation_status:
data_freshness:
limitations: []
```

Không phải source nào cũng expose mọi field. Field không có phải giữ `unknown`/`not_available`; không được invent attribution config.

### Invariant so sánh

```text
same metric name
+ different attribution/source/scope/window context
≠ directly comparable measurement
```

Ví dụ:

```text
TikTok reports 8 conversions
Google Analytics reports 5 conversions
```

không tạo quyền chọn số thuận lợi hơn. Flow đúng là:

```text
compare source + event definition + tracking identity
+ attribution model/window + timezone + data freshness
→ reconcile / explain limitation
→ canonical interpretation
```

### Import success khác measurement completeness

```text
file/API import succeeded
≠ payload semantically complete
≠ attribution context known
≠ canonical outcome accepted
```

Khi nguồn/import tool cung cấp validation status, giữ nó trong `MeasurementContext`. Thiếu cost/click/impression hoặc mismatch campaign ID phải là data-quality evidence, không được bị workflow success che mất.

## 6. Mức trưởng thành theo Mission

| Mission | Mức trưởng thành của metric |
|---|---|
| M00 | pre-register tracking/window trước human publish; commission/conversion vẫn unknown nếu chưa đo |
| M01 | import outcome snapshot thật; tách test event, zero, missing, pending và tạo `MeasurementContext` |
| M02 | deterministic baseline chỉ dùng evidence/context đã có |
| M03 | metric có provenance, timestamp, append-only history, freshness và reconcile |
| M04 | AI có thể giải thích/đặt giả thuyết nhưng không ghi đè metric truth |
| M05 | chọn bottleneck theo funnel; experiment chỉ so outcome có measurement context tương thích hoặc limitation rõ |
| M06 | watcher tự động thu signal đã hiểu với retry/dedup/freshness |
| M07 | `DecisionPacket` tham chiếu metric window/context/confidence/missing evidence |
| M08 | read-only tool chỉ lấy missing factor/context có giá trị cho quyết định |
| M09 | `ActionIntent` giữ expected outcome/cost/risk nhưng chưa có permission |
| M10 | canary đo outcome, intervention, cost và policy block trong giới hạn |
| M11 | trace decision → action → outcome → revenue/evaluation đầu-cuối, gồm measurement context khi relevant |

## 7. Chẩn đoán nút thắt (`bottleneck diagnosis`)

```text
Không có exposure
→ giả thuyết distribution/channel

Có exposure nhưng không click
→ giả thuyết audience/angle/hook/CTA

Có click nhưng không order
→ giả thuyết product–audience fit / landing / offer

Có order nhưng invalid/refunded
→ giả thuyết product quality / seller quality / expectation / compliance

Metric thiếu hoặc xung đột
→ giả thuyết measurement/instrumentation/attribution context
```

Không được nhảy tới automation/AI optimization khi lớp đo lường chưa phân biệt được các bottleneck trên.

## 8. Tính toàn vẹn của cửa sổ, cohort và attribution

Mọi comparison phải ghi hoặc reference:

- time window (cửa sổ thời gian);
- channel/scope (kênh/phạm vi);
- product/offer version;
- content/action version;
- test event khác real event;
- trạng thái pending/partial/final;
- reporting source;
- attribution model/lookback window nếu source có;
- timezone/config timestamp khi ảnh hưởng kỳ báo cáo;
- data freshness/import validation;
- giới hạn attribution đã biết.

Không so hai rate từ scope/window/attribution context khác nhau mà không ghi limitation.

## 9. Trạng thái sự thật của doanh thu

Vòng đời đơn hàng/commission phải tách khi nguồn hỗ trợ:

```text
ORDER_PENDING
ORDER_VALID
ORDER_INVALID
ORDER_REFUNDED
COMMISSION_PENDING
COMMISSION_FINAL
COMMISSION_PAID
```

`Order` không đồng nghĩa với `revenue`. `Commission pending` không đồng nghĩa với `paid`.

Khi payment/export thật sự expose adjustment hoặc withholding, lưu riêng:

```yaml
gross_commission:
platform_adjustment:
tax_withheld:
net_payout:
payout_evidence_ref:
```

Boundary:

```text
gross commission
≠ final commission
≠ net payout
```

`tax_withheld` chỉ là observed financial evidence khi source cung cấp. Repo không hard-code một mức thuế Affiliate phổ quát và không suy nghĩa vụ thuế cá nhân chỉ từ một platform field.

## 10. Reconciliation state

Khi nhiều source cùng nói về một outcome, canonical record nên giữ reconciliation state thay vì overwrite:

```text
UNRECONCILED
MATCHED
EXPLAINED_DIFFERENCE
CONFLICTING
INSUFFICIENT_CONTEXT
```

Ví dụ một platform report và analytics tool khác nhau có thể vẫn hợp lệ nếu attribution window/event definition khác. `EXPLAINED_DIFFERENCE` tốt hơn ép hai số thành một.

## 11. Quy tắc ra quyết định

Metric spine phục vụ decision, không thay decision contract.

```text
Evidence + Funnel Metrics + MeasurementContext + Opportunity Signals
→ Expected Value / đánh giá bottleneck
→ Affiliate Intelligence Decision
→ Risk / Policy
→ Action hoặc Abstention
→ Outcome
→ Evaluation
```

Nguyên tắc:

> **DATA > OPINION — Dữ liệu quan trọng hơn ý kiến.**
>
> **EXPECTED VALUE > COMMISSION RATE — Giá trị kỳ vọng quan trọng hơn tỷ lệ hoa hồng đơn lẻ.**
>
> **MISSING ≠ ZERO — Thiếu dữ liệu không phải số 0.**
>
> **METRIC VALUE WITHOUT CONTEXT ≠ COMPARABLE TRUTH — Giá trị chỉ số thiếu ngữ cảnh không phải sự thật có thể so sánh trực tiếp.**
>
> **ORDER ≠ VALID ORDER ≠ FINAL/PAID COMMISSION ≠ NET PAYOUT — Đơn hàng không đồng nghĩa đơn hợp lệ, hoa hồng cuối/đã trả hay tiền thực nhận sau adjustment/withholding.**
