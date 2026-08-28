---
mission_id: "M01"
title: "Đọc và kiểm tra dữ liệu sản phẩm"
status: ready
requires_missions: ["M00"]
bot_version_from: "v0.0"
bot_version_to: "v0.1"
estimated_hours: 3
knowledge:
  required: ["38.1", "51.1", "52.3", "52.7"]
  on_demand: []
  reference: []
projects:
  contributes_to: []
risk_scope:
  external_side_effects: false
---

# Mission M01 — Product Ingest (Đọc và kiểm tra dữ liệu sản phẩm)

## Ship Target — Mục tiêu bàn giao

Từ learner Bot v0.0, tự xây capability (năng lực) đọc `data/sample-products.json` thành `[]Product`, validate (kiểm tra) business data và trả lỗi rõ ràng khi input sai.

Kết quả M01 không được có ranking hoặc AI.

## Starting Bot State — Trạng thái Bot ban đầu

Starting state là **learner commit đã PASS M00**, không phải reference implementation.

Learner workspace:

```text
lab/learner/affiliate-bot/
```

Trước M01, Bot chỉ khởi động/in status và chưa có Product model hay JSON ingest.

## Build First — Xây trước

Tự tạo phần nhỏ nhất theo thứ tự:

```text
Product struct
→ read file
→ JSON decode
→ validate fields
→ print product count
```

Gợi ý path, không phải bắt buộc copy reference:

```text
internal/product/
internal/ingest/
cmd/bot/
```

Chỉ sau khi đã có attempt, bạn có thể đối chiếu `lab/affiliate-bot/` nếu cần.

## Run — Chạy

```bash
cd lab/learner/affiliate-bot
go run ./cmd/bot
go test ./...
```

Expected capability sau M01:

```text
Affiliate Bot starting...
Loaded products: 2
Bot version: v0.1
Bot status: OK
```

Exact wording có thể khác, nhưng product count phải đến từ file JSON thật chứ không hard-code.

## Observe — Quan sát

JSON parse được chưa có nghĩa business data hợp lệ.

Bot cần phân biệt:

```text
syntax hợp lệ
≠
business data hợp lệ
```

Ví dụ:

- `id` rỗng: JSON hợp lệ nhưng Product không định danh được;
- `price < 0`: JSON hợp lệ nhưng business value vô lý;
- `commission_rate > 1`: parse được nhưng sai semantics;
- unknown field (field lạ): có thể là schema drift cần phát hiện thay vì âm thầm bỏ qua;
- trailing JSON/garbage (dữ liệu dư sau document hợp lệ): phải bị reject thay vì chỉ đọc document đầu tiên rồi bỏ qua phần sau.

## Knowledge Pull — Lấy kiến thức đúng lúc

### Required — Bắt buộc cho Mission

- `38.1` — Core marketplace entities.
  - slice: Product cần identity và field cốt lõi nào.
- `51.1` — Go runtime, modules và project structure.
  - slice: package/type/struct đủ để tổ chức Product model.
- `52.3` — File Import.
  - slice: local file là ProductSource đầu tiên và cách tách read/decode khỏi domain.
- `52.7` — Validation.
  - slice: syntax validation khác business validation.

> Không yêu cầu full PASS bốn Lesson trước khi code M01. Chỉ cần hiểu slice đủ để build và explain-back.

### On-demand — Khi phát sinh nhu cầu

- error wrapping (bọc lỗi) khi lỗi hiện tại khó truy nguyên;
- JSON decoder behavior khi test lộ edge case;
- platform-specific fields chỉ khi có adapter thật.

### Reference — Tham khảo

- Part 12 data model đầy đủ để sau;
- `lab/affiliate-bot/` chỉ đối chiếu sau attempt;
- reference ingest hiện có strict tests cho unknown field, trailing JSON value và trailing garbage để dùng khi review.

## Improve — Cải tiến

Sau happy path đầu tiên, thêm business validation tối thiểu:

- ID/name không rỗng;
- price không âm;
- commission rate trong khoảng hợp lệ;
- conversion potential trong khoảng hợp lệ nếu field được dùng trong sample schema.

Sau đó harden parser (làm bộ đọc chặt chẽ hơn):

- reject unknown field;
- sau lần decode chính, xác nhận input đã tới EOF (hết document), không silently accept trailing content.

Không thêm field platform cụ thể khi chưa có business need.

## Tests — Kiểm thử

Ít nhất cover:

- valid JSON;
- malformed JSON;
- invalid Product;
- unknown field;
- trailing JSON value;
- trailing garbage/content;
- output Product count đúng với sample file.

## Operate — Vận hành

Chạy với:

1. file sample chuẩn;
2. một bản copy tự sửa thành invalid Product;
3. một bản có field lạ;
4. một bản có JSON/document dư sau array hợp lệ.

Quan sát error message có giúp tìm nguyên nhân hay không.

## Failure Case — Tình huống lỗi

Malformed JSON, Product invalid, unknown field hoặc trailing content phải trả error rõ ràng và exit non-success; không silently drop (âm thầm bỏ) record/phần dữ liệu lỗi.

## Evidence — Bằng chứng

Lưu:

- Product model;
- ingest code path;
- sample input/output;
- test output;
- ít nhất một invalid-input output;
- learner commit;
- note: validation nào bảo vệ downstream decision.

## Explain-back — Giải thích lại

1. Vì sao decode thành công chưa đủ để tin dữ liệu?
2. Validation nào là syntax validation, validation nào là business validation?
3. Vì sao trailing content phải bị reject?
4. Vì sao không đưa platform-specific field vào core Product quá sớm?
5. Nếu API sau này trả schema khác, layer nào nên phát hiện?

## Mission PASS — Tiêu chí PASS

- [ ] learner tự build Product model + JSON ingest
- [ ] valid data đi qua đúng luồng
- [ ] invalid data fail rõ ràng
- [ ] unknown field bị reject
- [ ] trailing content bị reject
- [ ] tests PASS
- [ ] output kiểm tra được
- [ ] chưa leak ranking/AI capability vào M01
- [ ] hiểu required knowledge slices
- [ ] explain-back đạt
- [ ] evidence đã lưu

## Bot Version Result — Kết quả phiên bản Bot

```text
v0.0 → v0.1 validated strict Product ingest
```

## Next Mission — Mission tiếp theo

M02 — Product Store & History (Lưu trữ và lịch sử sản phẩm).