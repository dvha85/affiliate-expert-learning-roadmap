# Manual Affiliate Loop — Business Grounding cho M00–M06

> **Vai trò:** lane thực hành Affiliate thủ công chạy song song với Build-First Missions.
>
> **Không phải:** Mission mới, Project mới, điều kiện để tự động tick Lesson PASS, hay quyền thực thi business action sớm.

## 1. Vì sao lane này tồn tại?

Build-First giúp learner có software chạy được sớm. Nhưng một Affiliate Bot chỉ hữu ích khi learner biết **business signal nào đáng đo, assumption nào đang yếu và quyết định nào chưa nên tự động hóa**.

Vì vậy từ M00 đến M06, learner chạy hai vòng lặp song song:

```text
SOFTWARE LANE
Build → Run → Observe → Pull Knowledge → Improve → Test → Save Evidence

BUSINESS LANE
Observe manually → Record evidence → Make a human judgment → Explain why
→ Compare with bot → Find disagreement/uncertainty → Improve model/data
```

Hai lane gặp nhau tại **evidence**, không gặp nhau bằng cách cho Bot quyền hành động sớm.

## 2. Safety boundary

Trong M00–M06, Manual Affiliate Loop ưu tiên **read-only observation và offline analysis**.

Không yêu cầu learner:

- publish content;
- spend advertising budget;
- thay đổi account/platform settings;
- gửi message cho customer/seller;
- đặt hàng hoặc tạo transaction;
- cho Bot tự thực thi external side effect.

Nếu một nguồn dữ liệu yêu cầu login, payment hoặc thay đổi trạng thái account thì learner có thể dùng sample/public data thay thế và ghi rõ provenance.

`Decision ≠ Execution` vẫn là invariant.

## 3. Evidence contract tối thiểu

Mỗi observation dùng cho Bot nên ghi ít nhất:

| Field | Ý nghĩa |
|---|---|
| `observed_at` | thời điểm quan sát |
| `source` | URL/public page/sample dataset/manual note |
| `fact_or_assumption` | `fact`, `estimate`, `assumption` hoặc `unknown` |
| `value` | giá trị quan sát/ước lượng |
| `confidence` | `low`, `medium`, `high` |
| `reason` | vì sao learner tin/không tin signal này |

Không biến estimate thành fact chỉ vì nó đã được nhập vào code.

## 4. M00–M06 progression

### M00 — Bot Boots: nhìn business trước khi Bot quyết định

Mục tiêu manual:

- chọn 3 sản phẩm công khai hoặc 3 sample products;
- ghi tên, giá và nguồn;
- viết 1 câu: “Tôi chưa đủ dữ liệu để kết luận sản phẩm nào tốt nhất vì …”.

Điểm học: Bot boot thành công **không đồng nghĩa** Bot hiểu Affiliate.

### M01 — Product Ingest: dữ liệu nhập vào có nghĩa gì?

Với 3–5 sản phẩm, learner ghi thủ công khi có thể:

- product name;
- price;
- commission/rate nếu nguồn công khai cung cấp;
- seller/platform;
- rating/review/sales signal nếu có;
- source + observed_at.

Sau đó so với schema/parser của M01:

- field nào là fact?
- field nào thiếu?
- field nào dễ stale?
- parser đang kiểm syntax hay business truth?

### M02 — Product History: snapshot có giá trị khi nào?

Quan sát lại cùng tập sản phẩm ở một thời điểm khác hoặc dùng hai sample snapshots.

Learner xác định:

- field nào thay đổi;
- field nào không biết có thay đổi hay không;
- vì sao overwrite snapshot cũ sẽ làm mất evidence;
- dữ liệu nào cần timestamp/provenance.

Điểm học: history là nền cho trend/alert/attribution, không chỉ là bài tập database.

### M03 — Product Ranking: human judgment trước score

Trước khi chạy ranking model:

1. learner tự xếp hạng 3–5 sản phẩm;
2. ghi lý do cho thứ tự đó;
3. đánh dấu từng lý do là `fact`, `estimate`, `assumption` hoặc `unknown`;
4. sau đó mới chạy bot ranking;
5. ghi ít nhất một điểm Bot đồng ý hoặc bất đồng với human ranking.

Không sửa formula chỉ để ép Bot khớp intuition. Bất đồng là evidence để học.

### M04 — Product Watcher: signal nào thật sự đáng alert?

Khi M04 được author `ready`, learner dùng manual observations để xác định trước:

- thay đổi nào đáng quan tâm;
- threshold nào mới chỉ là hypothesis;
- alert nào có nguy cơ noise;
- signal nào cần history trước khi kết luận.

Tài liệu này **không làm M04 ready**.

### M05 — Reliable Alerts + AI Advisory

Khi M05 được author `ready`, learner lấy một số manual cases đã biết outcome/context để hỏi:

- deterministic rule có alert đúng không?
- AI advisory giải thích gì thêm?
- model output có dẫn nguồn/evidence không?
- khi AI khác deterministic rule, human cần xem gì?

`MODEL OUTPUT = UNTRUSTED INPUT`; AI ở đây không có execution authority.

Tài liệu này **không làm M05 ready**.

### M06 — Product Intelligence

Khi M06 được author `ready`, learner bắt đầu thay các assumption yếu bằng evidence tốt hơn về:

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

Mục tiêu không phải “có thật nhiều feature”, mà là biết **signal nào có provenance, confidence và decision value**.

Tài liệu này **không làm M06 ready**.

## 5. Human vs Bot comparison note

Template ngắn sau mỗi Mission có ranking/decision:

```text
Manual judgment:
Bot output:
Agreement:
Disagreement:
Strongest evidence:
Weakest assumption:
What I would measure next:
Would I allow execution from this decision? Why/why not?
```

## 6. Nguyên tắc pedagogy

```text
DO NOT:
software output → assume business truth

DO:
manual observation
→ evidence + provenance
→ human judgment
→ deterministic model
→ compare
→ measure disagreement/uncertainty
→ improve data/model
→ only later automate governed execution
```

Manual Affiliate Loop không cạnh tranh với Build-First. Nó đảm bảo thứ được build ngày càng gần **Affiliate Intelligence** thay vì chỉ ngày càng nhiều code.