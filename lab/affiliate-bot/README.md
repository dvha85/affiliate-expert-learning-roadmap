# Affiliate Bot — legacy engineering reference snapshot v0.3

> Snapshot này được viết cho mission sequence cũ. Nó **không** phải lời giải M00–M03 hiện hành: M02 hiện là Grounded AI Advisor và M03 là Human Tracked Publish. Dùng code ở đây để đối chiếu từng pattern ingest/history/ranking sau attempt, không dùng version/mapping cũ làm learner progress.

Đây **không phải learner workspace**.

Người học trực tiếp build tại:

```text
lab/learner/affiliate-bot/
```

## Khi nào nên mở reference

Quy tắc mặc định:

```text
TỰ THỬ BUILD
→ RUN / OBSERVE
→ PULL KNOWLEDGE
→ IMPROVE / TEST
→ mở reference để đối chiếu khi cần
```

Reference dùng để:

- review design sau learner attempt (lần thử);
- gỡ blocker khi đã có lỗi/evidence cụ thể;
- so sánh implementation và trade-off;
- bảo vệ curriculum bằng executable tests.

Không copy toàn bộ reference sang learner workspace rồi coi đó là Mission PASS.

## Chạy bản tham chiếu

```bash
cd lab/affiliate-bot
go run ./cmd/bot
```

Có thể truyền custom input (đầu vào tùy chỉnh):

```bash
go run ./cmd/bot path/to/products.json
```

## Kiểm thử

```bash
go test ./...
```

## Scope kỹ thuật của snapshot v0.3

- validated JSON product ingest (đọc và kiểm tra Product JSON);
- Product domain validation (kiểm tra dữ liệu nghiệp vụ Product);
- storage boundary (ranh giới lưu trữ) + in-memory snapshot history cho test nhanh;
- PostgreSQL schema/migration path trong `migrations/001_init.sql`;
- executable flow lưu ProductSnapshot vào Repository;
- commission-only ranking (xếp hạng chỉ theo tỷ lệ hoa hồng);
- Expected-Value ranking (xếp hạng theo Giá trị kỳ vọng đơn giản);
- deterministic tie-breaking (phá hòa xác định).

Không có external API, credential, AI, publishing hoặc money-moving side effect (tác động di chuyển tiền) trong bootstrap reference.

## Persistence pattern trong snapshot

Snapshot có PostgreSQL migration contract (hợp đồng schema), trong khi unit test dùng in-memory Repository để feedback nhanh. Trong curriculum hiện hành, M01 bắt đầu bằng append-only file history; SQL/Repository chỉ pull on-demand khi requirement thật cần.

PostgreSQL driver/integration environment được thêm khi operational value (giá trị vận hành) đủ lớn; không để M00/M01 hoặc PR tài liệu phải phụ thuộc database service chỉ để chạy CI nhanh.

## Expected sample behavior (hành vi mẫu mong đợi)

Dataset cố ý chứng minh sản phẩm có Commission Rate (Tỷ lệ hoa hồng) cao nhất không nhất thiết có simple Expected Value (Giá trị kỳ vọng đơn giản) cao nhất:

```text
commission-only top: A
Expected-Value top: B
```

Reference này thể hiện một ranking pattern có thể đối chiếu trong M00 hoặc khi đánh giá baseline sau này:

```text
Build naive ranking
→ Observe weakness
→ Pull Knowledge
→ Improve formula
→ Compare before/after
```

Nhưng learner phải tự tạo before/after trong learner workspace trước khi dùng reference làm lời giải đối chiếu.
