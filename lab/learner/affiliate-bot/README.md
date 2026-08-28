# Affiliate Bot — workspace của người học

Đây là workspace (không gian làm việc) mà người học trực tiếp sửa trong chuỗi Mission M00 → M03 và các Mission tiếp theo.

## Trạng thái khởi đầu

Workspace trong repository chỉ chứa năng lực tối thiểu của M00:

```text
khởi động chương trình
→ in Bot version
→ in Bot status
→ exit cleanly
```

Nó **không có sẵn**:

- Product model;
- JSON ingest (đọc dữ liệu JSON);
- validation (kiểm tra dữ liệu);
- storage/history (lưu trữ/lịch sử);
- ranking (xếp hạng);
- Expected Value (Giá trị kỳ vọng).

Những capability (năng lực) đó phải được người học tự thêm qua M01 → M03.

## Chạy M00

```bash
cd lab/learner/affiliate-bot
go run ./cmd/bot
go test ./...
```

## Dữ liệu mẫu

`data/sample-products.json` được đặt sẵn để M01 có input (đầu vào) ổn định. M00 không sử dụng file này.

## Reference implementation (bản triển khai tham chiếu)

Bản tham chiếu hiện nằm ở:

```text
lab/affiliate-bot/
```

Quy tắc học:

```text
TỰ THỬ BUILD
→ RUN / OBSERVE
→ PULL KNOWLEDGE
→ FIX / TEST
→ chỉ mở reference khi cần đối chiếu hoặc sau khi đã có một attempt (lần thử)
```

Không copy toàn bộ reference vào learner workspace rồi coi đó là Mission PASS. PASS phải dựa trên code/evidence mà người học thực sự hiểu và giải thích được.

## Nguyên tắc an toàn

```text
BUILD CODE EARLY (viết code sớm)
≠
AUTOMATE REAL BUSINESS EARLY (tự động hóa hoạt động kinh doanh thật quá sớm)
```

M00–M03 chỉ dùng dữ liệu mẫu/local và không có external side effect (tác động bên ngoài), không publish, không tiêu tiền và không thay đổi tài khoản nền tảng.