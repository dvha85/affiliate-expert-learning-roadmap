# Affiliate Intelligence Decision Contract

Tài liệu này giữ cho chương trình luôn là **Affiliate Intelligence Bot course**, không trôi thành một khóa generic agent/automation chỉ dùng Affiliate làm ví dụ.

Contract là **cumulative**: Mission sớm chỉ điền các field đã có evidence; field chưa đủ bằng chứng phải là `unknown`, `not_yet_observable` hoặc một abstention state hợp lệ. Không được bịa dữ liệu để làm output có vẻ đầy đủ.

## Câu hỏi cuối cùng Bot phải hỗ trợ

Ở mức production, Bot phải có khả năng trả lời có bằng chứng:

```text
Hôm nay nên quảng bá product/offer nào?
Tại sao?
Cho audience/problem nào?
Content angle nào?
Hook / CTA nào?
Channel nào?
Khi nào / trong window nào?
Expected Value / expected affiliate revenue là bao nhiêu?
Evidence nào hỗ trợ quyết định?
Confidence là bao nhiêu và theo method nào?
Uncertainty / missing evidence là gì?
Compliance / business risk là gì?
Recommended state là ACT / WAIT / GET_MORE_DATA / HUMAN_REVIEW / DENY?
Measurement / experiment tiếp theo là gì?
```

Bot có quyền **không trả lời một field** nếu evidence chưa đủ. `unknown` tốt hơn một con số hoặc recommendation giả.

## Canonical logical fields

| Field | Ý nghĩa | Không được nhầm với |
|---|---|---|
| `product_or_offer` | subject được cân nhắc | seller claim không kiểm chứng |
| `audience_problem` | ai / nhu cầu nào decision phục vụ | generic demographic không có evidence |
| `content_angle` | hypothesis về cách diễn đạt value | final publish permission |
| `hook_cta` | hypothesis về opening/next action | guaranteed conversion claim |
| `channel` | nơi artifact/action dự kiến xuất hiện | tool permission |
| `timing_window` | thời điểm/observation window | urgency giả |
| `expected_value` | EV/revenue expectation với assumption rõ | commission rate đơn lẻ |
| `evidence_refs` | source/snapshot/metric hỗ trợ decision | AI prose |
| `confidence` | mức tin cậy + method/reason | xác suất chân lý mặc định |
| `uncertainty` | assumption, missing/conflict/staleness | value `0` |
| `risk` | compliance/business/operational risk | permission to execute |
| `recommended_state` | ACT/WAIT/GET_MORE_DATA/HUMAN_REVIEW/DENY | execution result |
| `next_measurement` | outcome/experiment cần thu tiếp | silent self-modification |

## Product opportunity evidence

Khi evidence trưởng thành, decision có thể cân nhắc các signal domain sau:

- Demand;
- Product–Audience Fit;
- Price;
- Conversion Potential;
- Commission per Order;
- Sales Trend;
- Product Quality;
- Seller Quality;
- Content Potential;
- Competition;
- Refund Risk;
- Compliance Risk.

Không Mission nào bắt buộc phải có đủ 12 signal. Mỗi signal phải mang trạng thái evidence riêng: `observed | estimated | assumed | unknown` cùng provenance/freshness phù hợp.

Nguyên tắc:

> **DATA > OPINION**
>
> **EXPECTED VALUE > COMMISSION RATE**

## Mission maturity map

| Mission | Contract phải trưởng thành thêm |
|---|---|
| M00 | `product_or_offer`, evidence refs, deterministic reason, confidence/weakest assumption, abstain khi evidence không đủ |
| M01 | history, freshness, change/delta và identity làm evidence đáng tin hơn |
| M02 | grounded AI analysis có thể đề xuất audience/angle nhưng unsupported field bị reject/fallback |
| M03 | `audience_problem`, `content_angle`, `hook_cta`, `channel`, `timing_window`, risk/disclosure và human publish decision |
| M04 | outcome thật làm rõ CTR/CVR/order/valid/final commission và cập nhật EV assumptions |
| M05 | `next_measurement` trở thành explicit experiment/change proposal từ bottleneck thật |
| M06 | signal collection tự động nhưng không thay đổi decision authority |
| M07 | canonical `DecisionPacket` gom evidence/confidence/uncertainty/risk/state/expiry |
| M08 | agent chỉ dùng read tools để lấp missing evidence đáng giá |
| M09 | recommendation tạo `ActionIntent`; intent vẫn không phải permission |
| M10 | ACT chỉ được auto-execute trong RISK0/RISK1 bounds đã policy cho phép; RISK2 cần approval |
| M11 | contract chạy end-to-end và nối decision → action → outcome → evaluation → reviewed change |

## Early-mission partial output

Ví dụ M00 có thể hợp lệ như sau:

```text
product_or_offer: Product B
audience_problem: unknown
content_angle: unknown
hook_cta: unknown
channel: unknown
timing_window: unknown
expected_value: scenario_only
confidence: low
uncertainty:
  - conversion probability unknown
  - audience fit not yet measured
recommended_state: GET_MORE_DATA
next_measurement: observe public product evidence and preserve human ranking
```

Output này tốt hơn việc Bot tự bịa audience, hook, CVR hoặc expected revenue.

## Separation of authority

```text
Affiliate Intelligence recommendation
≠ ActionIntent
≠ PolicyDecision
≠ Approval
≠ ExecutionRecord
≠ Outcome
```

Một recommendation rất tự tin không làm tăng quyền của Bot. External side effect vẫn tuân theo risk/policy/approval của Mission hiện tại.

## Outcome closes the contract

Decision chỉ có giá trị học tập khi outcome quay lại đúng decision/action record. Khi dữ liệu hỗ trợ, funnel domain chuẩn là:

```text
Exposure / Impression
→ View / Engagement (nếu channel cung cấp)
→ Click
→ Product View / Add to Cart / Checkout (nếu nguồn cung cấp)
→ Order
→ Valid Order
→ Final Commission
→ Payment (nếu observable)
```

Không được tạo event giả để lấp khoảng trống của platform. Measurement spine chi tiết nằm ở `AFFILIATE-METRIC-REVENUE-SPINE.md` khi tài liệu đó được kích hoạt.

## Definition of integrity

Một Affiliate Intelligence Decision đạt integrity khi:

1. recommendation truy được về evidence;
2. field thiếu được giữ thiếu;
3. estimate/assumption không được trình bày như fact;
4. EV không bị thay bằng commission-rate-only shortcut;
5. confidence có method/reason;
6. risk và permission tách khỏi recommendation quality;
7. Bot có thể abstain;
8. next measurement/experiment được ghi trước khi outcome được dùng để “học”;
9. outcome không tự động rewrite production behavior.
