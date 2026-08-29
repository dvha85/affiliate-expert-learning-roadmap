# Quy ước ngôn ngữ tiếng Việt

Tài liệu này là chuẩn biên soạn cho toàn bộ nội dung dành cho người học trong repo.

## 1. Ngôn ngữ chính

**Tiếng Việt là ngôn ngữ chính.** Câu, đoạn, heading, bảng mô tả, hướng dẫn, tiêu chí PASS và giải thích phải ưu tiên tiếng Việt tự nhiên, rõ nghĩa.

Không viết một câu tiếng Việt nhưng chèn quá nhiều từ tiếng Anh khi đã có cách diễn đạt tiếng Việt dễ hiểu tương đương.

## 2. Khi nào giữ thuật ngữ tiếng Anh

Giữ thuật ngữ tiếng Anh khi ít nhất một điều đúng:

1. đó là tên chuẩn trong code/schema/API;
2. dịch sang tiếng Việt dễ gây sai nghĩa hoặc mất khả năng tra cứu;
3. learner cần nhận diện đúng thuật ngữ để đọc tài liệu kỹ thuật bên ngoài;
4. đó là enum/state/token mà code đang dùng.

Ví dụ nên giữ:

- `DecisionPacket`;
- `ActionIntent`;
- `idempotency`;
- `fallback`;
- `retry/backoff`;
- `read-only`;
- `schema`;
- `Expected Value (EV)`;
- `CTR`, `CVR`, `EPC`;
- `RISK 0/1/2`, `DENY`;
- `BLOCKED_EXTERNAL`.

## 3. Cách giải thích thuật ngữ

Ở lần xuất hiện quan trọng đầu tiên trong một tài liệu, dùng một trong hai dạng:

```text
thuật ngữ tiếng Việt (`English term`)
```

hoặc:

```text
English term (giải thích tiếng Việt)
```

Ví dụ:

- đường cơ sở tất định (`deterministic baseline`);
- từ chối quyết định (`abstention`);
- dữ liệu chỉ-đọc (`read-only`);
- `fallback` (phương án dự phòng);
- `freshness` (độ mới của dữ liệu);
- `provenance` (nguồn gốc và đường dẫn truy xuất bằng chứng).

Không cần lặp lại phần giải thích ở mọi lần xuất hiện sau nếu ngữ cảnh đã rõ.

## 4. Những phần không dịch

Không dịch hoặc sửa tùy tiện:

- tên file, thư mục và đường dẫn;
- command shell;
- code identifier;
- JSON/YAML key;
- enum/state;
- API field;
- commit SHA;
- tên chính thức của chuẩn/protocol/library/tool khi việc dịch làm mất khả năng tra cứu.

Có thể giải thích bằng tiếng Việt ở prose xung quanh.

## 5. Heading và bảng

Heading dành cho learner phải ưu tiên tiếng Việt.

Không nên:

```text
## Mission progression
## Early-loop target
## Planning bands
```

Nên:

```text
## Tiến triển theo Mission
## Mục tiêu vòng lặp thực tế sớm
## Các dải lập kế hoạch
```

Tên cột bảng cũng theo nguyên tắc tương tự, trừ field/schema name cần giữ nguyên.

## 6. Thuật ngữ Affiliate và Bot

Các thuật ngữ Affiliate/Engineering quan trọng được giữ bằng tiếng Anh khi cần nhưng phải có nghĩa tiếng Việt ở ngữ cảnh học đầu tiên, ví dụ:

- `Audience` (nhóm người mục tiêu);
- `Content Angle` (góc nội dung);
- `Hook` (câu mở thu hút);
- `CTA` / Call to Action (lời kêu gọi hành động);
- `Conversion` (chuyển đổi);
- `Commission` (hoa hồng);
- `Refund Risk` (rủi ro hoàn/huỷ);
- `Compliance Risk` (rủi ro tuân thủ);
- `Expected Value` (giá trị kỳ vọng);
- `Tracking` (theo dõi đo lường);
- `Outcome` (kết quả quan sát được).

## 7. Kiểm tra trước Pull Request

Trước khi merge thay đổi tài liệu dành cho learner, reviewer phải kiểm:

- prose có đang chủ yếu là tiếng Việt không;
- heading/cột bảng có đang dùng tiếng Anh không cần thiết không;
- thuật ngữ chuyên ngành mới đã có giải thích tiếng Việt ở lần xuất hiện quan trọng chưa;
- code/schema/token có bị dịch sai không;
- cùng một thuật ngữ có được dùng nhất quán không.

Quy tắc này áp dụng cho README, CURRICULUM, ROADMAP, Mission, Lesson, docs hướng dẫn và learner workspace. Historical source trong `sources/` được giữ nguyên khi cần bảo toàn provenance; chỉ các tài liệu hướng dẫn bao quanh historical source phải theo quy ước này.
