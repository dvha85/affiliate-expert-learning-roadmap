# Hợp đồng quyết định của Affiliate Intelligence Bot

Tài liệu này giữ cho chương trình luôn là khóa học xây **Affiliate Intelligence Bot (Bot phân tích và hỗ trợ quyết định Affiliate)**, không trôi thành một khóa agent/automation chung chung chỉ dùng Affiliate làm ví dụ.

Hợp đồng (`contract`) có tính **tích lũy (`cumulative`)**: Mission sớm chỉ điền các field đã có evidence; field chưa đủ bằng chứng phải là `unknown`, `not_yet_observable` hoặc một trạng thái từ chối quyết định (`abstention state`) hợp lệ. Không được bịa dữ liệu để output có vẻ đầy đủ.

## Active v2 maturity map

| Mission | Contract increment v2 |
|---|---|
| M00 | offer/audience/channel/content hypothesis, evidence, disclosure/tracking and human-only Action record; Bot fields may remain unknown |
| M01 | first `MeasurementContext` and outcome snapshot; distinguish zero/missing/pending/inconclusive |
| M02 | smallest deterministic reason, confidence, uncertainty and abstain |
| M03 | append-only history, provenance, freshness and reconciliation |
| M04 | grounded AI explanation with source refs/fallback; no tool/write permission |
| M05 | outcome → evaluation → proposed improvement → test/review/rollback |
| M06–M11 | reliable observation, DecisionPacket, read tools, governed ActionIntent and closed-loop recovery |

The v1 details below remain reference only; their M00–M04 labels do not define
the active execution order. See [`CURRICULUM-MIGRATION-v2.md`](CURRICULUM-MIGRATION-v2.md).

## Câu hỏi cuối cùng Bot phải hỗ trợ

Ở mức production (môi trường vận hành thật), Bot phải có khả năng trả lời có bằng chứng:

```text
Hôm nay nên quảng bá product/offer (sản phẩm/ưu đãi) nào?
Tại sao?
Cho audience/problem (nhóm người/vấn đề) nào?
Content angle (góc nội dung) nào?
Hook / CTA (câu mở / lời kêu gọi hành động) nào?
Channel (kênh) nào?
Khi nào / trong window (khoảng quan sát) nào?
Expected Value / expected affiliate revenue (giá trị kỳ vọng / doanh thu Affiliate kỳ vọng) là bao nhiêu?
Evidence nào hỗ trợ quyết định?
Measurement context (ngữ cảnh đo lường) nào sẽ dùng để đọc outcome?
Confidence (độ tin cậy) là bao nhiêu và theo method nào?
Uncertainty / missing evidence (độ bất định / bằng chứng còn thiếu) là gì?
Compliance / business risk (rủi ro tuân thủ / kinh doanh) là gì?
Recommended state là ACT / WAIT / GET_MORE_DATA / HUMAN_REVIEW / DENY?
Measurement / experiment (phép đo / thí nghiệm) tiếp theo là gì?
```

Bot có quyền **không trả lời một field** nếu evidence chưa đủ. `unknown` tốt hơn một con số hoặc recommendation (khuyến nghị) giả.

## Các field logic chuẩn

| Field | Ý nghĩa | Không được nhầm với |
|---|---|---|
| `product_or_offer` | sản phẩm/offer đang cân nhắc | seller claim chưa kiểm chứng |
| `audience_problem` | nhóm người / nhu cầu mà quyết định phục vụ | demographic chung chung không có evidence |
| `content_angle` | giả thuyết về cách diễn đạt giá trị | quyền publish cuối cùng |
| `hook_cta` | giả thuyết về câu mở / hành động tiếp theo | cam kết chuyển đổi |
| `channel` | nơi artifact/action dự kiến xuất hiện | quyền dùng tool |
| `timing_window` | thời điểm / cửa sổ quan sát | tạo khẩn cấp giả |
| `expected_value` | EV/doanh thu kỳ vọng với assumption rõ | commission rate đơn lẻ |
| `evidence_refs` | nguồn/snapshot/metric hỗ trợ quyết định | văn bản AI tự sinh |
| `measurement_context_ref` | ref tới source/scope/attribution/window/config dùng để diễn giải outcome | chính metric value hoặc attribution truth phổ quát |
| `confidence` | mức tin cậy + method/reason | xác suất chân lý mặc định |
| `uncertainty` | assumption, missing/conflict/staleness | giá trị `0` |
| `risk` | rủi ro tuân thủ/kinh doanh/vận hành | quyền thực thi |
| `recommended_state` | ACT/WAIT/GET_MORE_DATA/HUMAN_REVIEW/DENY | kết quả thực thi |
| `next_measurement` | outcome/experiment cần thu tiếp | tự sửa production âm thầm |

`measurement_context_ref` chỉ bắt đầu có ý nghĩa khi Mission có measurement thật. M00–M03 có thể giữ `unknown` hoặc mới chỉ pre-register expected window/tracking identity. Không backfill một context giả vào Mission sớm.

## Bằng chứng về cơ hội sản phẩm

Khi evidence trưởng thành, quyết định có thể cân nhắc các tín hiệu (`signal`) domain sau:

- Demand (nhu cầu);
- Product–Audience Fit (độ phù hợp sản phẩm–nhóm người);
- Price (giá);
- Conversion Potential (tiềm năng chuyển đổi);
- Commission per Order (hoa hồng trên đơn);
- Sales Trend (xu hướng bán);
- Product Quality (chất lượng sản phẩm);
- Seller Quality (chất lượng người bán);
- Content Potential (tiềm năng nội dung);
- Competition (mức cạnh tranh);
- Refund Risk (rủi ro hoàn/huỷ);
- Compliance Risk (rủi ro tuân thủ).

Không Mission nào bắt buộc phải có đủ 12 signal. Mỗi signal phải mang trạng thái evidence riêng: `observed | estimated | assumed | unknown`, cùng provenance (nguồn gốc) và freshness (độ mới) phù hợp.

Platform-derived score như creator quality/account score có thể là signal quan sát được, nhưng không tự trở thành `Product Quality`, `Seller Quality`, conversion truth hoặc Bot score nếu không có contract/evidence chứng minh semantics đó.

Nguyên tắc:

> **DATA > OPINION — Dữ liệu quan trọng hơn ý kiến.**
>
> **EXPECTED VALUE > COMMISSION RATE — Giá trị kỳ vọng quan trọng hơn tỷ lệ hoa hồng đơn lẻ.**

## V1 baseline maturity detail

| Mission | Hợp đồng phải trưởng thành thêm |
|---|---|
| M00 | `product_or_offer`, evidence refs, lý do tất định, confidence/giả định yếu nhất, abstain khi evidence không đủ |
| M01 | history, freshness, change/delta và identity làm evidence đáng tin hơn |
| M02 | phân tích AI có grounding (căn cứ bằng chứng) có thể đề xuất audience/angle nhưng field không được hỗ trợ phải reject/fallback |
| M03 | `audience_problem`, `content_angle`, `hook_cta`, `channel`, `timing_window`, risk/disclosure; pre-register target metric/window/tracking identity; human publish |
| M04 | outcome thật làm rõ CTR/CVR/order/valid/final commission; tạo `MeasurementContext` và reconcile source/attribution/config trước khi cập nhật assumption của EV |
| M05 | `next_measurement` trở thành experiment/change proposal rõ ràng từ bottleneck thật; comparison giữ measurement-context compatibility/limitations |
| M06 | thu tín hiệu tự động nhưng không tự tăng quyền quyết định |
| M07 | `DecisionPacket` chuẩn gom evidence/confidence/uncertainty/risk/state/expiry và measurement-context refs khi relevant |
| M08 | agent chỉ dùng read tools để lấp missing evidence/context đáng giá |
| M09 | recommendation tạo `ActionIntent`; intent vẫn không phải permission |
| M10 | ACT chỉ được tự chạy trong giới hạn RISK0/RISK1 đã được policy cho phép; RISK2 cần approval |
| M11 | contract chạy đầu-cuối và nối decision → action → outcome → measurement context → evaluation → reviewed change |

## Output từng phần ở Mission sớm

Ví dụ M00 có thể hợp lệ như sau:

```text
product_or_offer: Product B
audience_problem: unknown
content_angle: unknown
hook_cta: unknown
channel: unknown
timing_window: unknown
expected_value: scenario_only
measurement_context_ref: unknown
confidence: low
uncertainty:
  - conversion probability unknown
  - audience fit not yet measured
recommended_state: GET_MORE_DATA
next_measurement: observe public product evidence and preserve human ranking
```

Output này tốt hơn việc Bot tự bịa audience, hook, CVR, attribution context hoặc expected revenue.

## Measurement context không phải metric value

Khi M04+ có outcome, một value phải truy được về ngữ cảnh đo lường. Canonical fields chi tiết nằm trong [`AFFILIATE-METRIC-REVENUE-SPINE.md`](AFFILIATE-METRIC-REVENUE-SPINE.md), nhưng mental model là:

```text
Metric/Outcome
+ reporting source/scope
+ tracking/campaign identity
+ attribution model/window nếu known
+ reporting timezone/config observed_at nếu relevant
+ freshness/import validation
+ limitations
→ interpretable evidence
```

Invariant:

```text
same metric label
+ different measurement context
≠ automatically comparable truth
```

Nếu TikTok, Shopee, YouTube/merchant export và analytics tool cho số khác nhau, Bot phải preserve/reconcile context; không được chọn số hỗ trợ recommendation ban đầu nhất.

## Tách biệt quyền hành động

```text
Khuyến nghị Affiliate Intelligence
≠ ActionIntent
≠ PolicyDecision
≠ Approval
≠ ExecutionRecord
≠ Outcome
```

Một recommendation rất tự tin không làm tăng quyền của Bot. Tác động ra bên ngoài (`external side effect`) vẫn tuân theo risk/policy/approval của Mission hiện tại.

## Outcome khép kín hợp đồng

Decision chỉ có giá trị học tập khi outcome quay lại đúng decision/action record. Khi dữ liệu hỗ trợ, funnel (phễu) domain chuẩn là:

```text
Exposure / Impression (lượt hiển thị)
→ View / Engagement (xem / tương tác, nếu channel cung cấp)
→ Click (nhấp)
→ Product View / Add to Cart / Checkout (nếu nguồn cung cấp)
→ Order (đơn hàng)
→ Valid Order (đơn hợp lệ)
→ Final Commission (hoa hồng cuối cùng)
→ Payment / Net Payout (thanh toán/tiền thực nhận, nếu quan sát được)
```

Không được tạo event giả để lấp khoảng trống của platform. Gross/final/paid/net payout phải tách khi source expose adjustment/withholding; không suy nghĩa vụ thuế từ một metric thiếu scope.

Measurement spine (trục đo lường) chi tiết nằm ở [`AFFILIATE-METRIC-REVENUE-SPINE.md`](AFFILIATE-METRIC-REVENUE-SPINE.md).

## Định nghĩa tính toàn vẹn

Một Affiliate Intelligence Decision đạt integrity (tính toàn vẹn) khi:

1. recommendation truy được về evidence;
2. field thiếu được giữ thiếu;
3. estimate/assumption không được trình bày như fact;
4. EV không bị thay bằng shortcut chỉ nhìn commission rate;
5. metric/outcome quan trọng ở M04+ truy được về measurement context đủ để diễn giải hoặc ghi rõ context còn thiếu;
6. hai metric khác source/window/attribution context không bị coi là trực tiếp tương đương nếu chưa reconcile;
7. confidence có method/reason;
8. risk và permission tách khỏi chất lượng recommendation;
9. Bot có thể abstain;
10. next measurement/experiment được ghi trước khi outcome được dùng để “học”;
11. outcome không tự động viết lại hành vi production.
