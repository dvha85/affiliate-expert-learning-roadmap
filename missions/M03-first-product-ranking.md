---
mission_id: "M03"
title: "Xếp hạng sản phẩm đầu tiên"
status: ready
requires_missions: ["M02"]
bot_version_from: "v0.2"
bot_version_to: "v0.3"
estimated_hours: 4
knowledge:
  required: ["5.11", "27.3"]
  on_demand: []
  reference: []
projects:
  contributes_to: [4]
risk_scope:
  external_side_effects: false
---

# Mission M03 — First Product Ranking (Xếp hạng sản phẩm đầu tiên)

## Ship Target — Mục tiêu bàn giao

Từ learner Bot v0.2, tự xây hai ranking strategy (chiến lược xếp hạng) và dùng dữ liệu để chứng minh vì sao `commission_rate only` có thể đưa ra thứ tự kém hơn một score dùng Expected Value (Giá trị kỳ vọng).

Điểm học quan trọng nhất của M03 là **tự gặp vấn đề trước rồi mới cải tiến**, không chạy sẵn lời giải v0.3 từ reference.

## Starting Bot State — Trạng thái Bot ban đầu

Starting state là learner commit đã PASS M02:

```text
validated Product ingest
→ ProductSnapshot/history foundation
→ storage được nối vào executable
→ chưa có ranking/decision logic
```

Workspace:

```text
lab/learner/affiliate-bot/
```

## Build First — Xây trước

Bước 1 — build naive ranking (xếp hạng đơn giản) trước:

```text
score = commission_rate
```

Chạy và lưu ranking output.

Bước 2 — **chưa mở reference**, tự hỏi:

> Sản phẩm có commission rate cao nhất có nhất thiết tạo expected commission cao nhất không?

Chỉ sau khi đã có before output và câu hỏi thực tế này mới pull Expected Value knowledge.

## Run — Chạy

```bash
cd lab/learner/affiliate-bot
go run ./cmd/bot
go test ./...
```

Bot cần in được ít nhất:

```text
Commission-only ranking:
...
```

Sau Improve, in thêm:

```text
Expected-Value ranking:
...
```

## Observe — Quan sát

Commission Rate (Tỷ lệ hoa hồng) bỏ qua Price (Giá) và Conversion Potential (Khả năng chuyển đổi).

Ví dụ data mẫu cố ý cho phép ranking đổi thứ tự:

```text
commission-only top: A
Expected-Value top: B
```

Nếu ranking không đổi trên data bạn đang dùng, tạo một dataset nhỏ khác đủ để bộc lộ khác biệt và giải thích vì sao.

## Knowledge Pull — Lấy kiến thức đúng lúc

### Required — Bắt buộc cho Mission

- `5.11` — Expected Value (Giá trị kỳ vọng).
  - slice: expected outcome phải kết hợp xác suất/kết quả kinh tế; commission rate đơn lẻ không đủ.
- `27.3` — Ranking (Xếp hạng).
  - slice: score phải deterministic (xác định), so sánh được, có tie-break (quy tắc phá hòa) và giải thích được.

> Không yêu cầu full PASS 5.11/27.3 trước khi viết naive ranking. Knowledge được pull **sau khi before result đã làm lộ vấn đề**.

### On-demand — Khi phát sinh nhu cầu

Các biến để M06 refine (cải tiến) score:

- Demand (Nhu cầu);
- Product–Audience Fit (Mức phù hợp sản phẩm–đối tượng);
- valid-order/refund risk (rủi ro đơn hợp lệ/hoàn trả);
- seller/product quality;
- CVR và các tín hiệu conversion khác.

### Reference — Tham khảo

- advanced statistics/AI ranking cố ý để sau;
- `lab/affiliate-bot/` có reference v0.3, chỉ mở sau learner attempt hoặc khi review.

## Improve — Cải tiến

Thêm strategy thứ hai với baseline formula (công thức nền):

```text
commission-only score
= commission_rate

simple Expected-Value score
= price × commission_rate × conversion_potential
```

Đây **không** phải production Opportunity Score. Nó cố ý đơn giản để tạo context cho Economics/Product Intelligence về sau.

Thêm deterministic tie-break, ví dụ Product ID khi hai score bằng nhau.

## Tests — Kiểm thử

Tests phải chứng minh:

- có ít nhất một dataset mà top product của hai strategy khác nhau;
- cùng input → cùng ranking;
- tie-break deterministic;
- invalid Product không tạo NaN/undefined behavior;
- storage/ingest của M01–M02 vẫn không bị regression (hỏng lại).

## Operate — Vận hành

Chạy sample dataset và xem hai ranking cạnh nhau. Lưu before/after output.

Đây là lúc bạn biến một nguyên tắc lý thuyết:

```text
EXPECTED VALUE > COMMISSION RATE
```

thành behavior của Bot mà bạn trực tiếp quan sát được.

## Failure Case — Tình huống lỗi

Thử Product có invalid conversion potential hoặc malformed data. Validation layer phải chặn dữ liệu trước ranking; ranking không được âm thầm tạo NaN/undefined result.

## Evidence — Bằng chứng

Lưu:

- naive commission-only implementation + output;
- Expected-Value implementation + output;
- test cho ranking đảo thứ tự;
- deterministic tie-break test;
- learner commit;
- một đoạn giải thích tại sao thứ tự thay đổi.

## Explain-back — Giải thích lại

1. Vì sao Commission Rate không phải Expected Value?
2. Price và Conversion Potential làm thay đổi expected outcome như thế nào?
3. Vì sao ranking function phải deterministic ở giai đoạn này?
4. Những biến nào còn thiếu trước khi score đủ dùng cho real recommendation (khuyến nghị thật)?
5. Vì sao M03 vẫn chưa được phép tự execute một business action bên ngoài?

## Mission PASS — Tiêu chí PASS

- [ ] learner tự build commission-only ranking trước
- [ ] đã lưu before output trước khi cải tiến
- [ ] learner tự thêm Expected-Value ranking
- [ ] hai ranking cùng chạy được
- [ ] tests PASS
- [ ] same input tạo deterministic output
- [ ] có ít nhất một before/after ordering difference được giải thích
- [ ] failure case đã được thử
- [ ] hiểu knowledge slices 5.11 và 27.3 đủ cho implementation
- [ ] explain-back đạt
- [ ] evidence đã lưu

## Bot Version Result — Kết quả phiên bản Bot

```text
v0.2 → v0.3 first deterministic decision/ranking behavior
```

## Next Mission — Mission tiếp theo

M04 — Product Watcher (Bot theo dõi thay đổi sản phẩm).