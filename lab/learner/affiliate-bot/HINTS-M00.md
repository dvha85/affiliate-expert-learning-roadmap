# Thang gợi ý M00 — chỉ mở từng mức sau khi đã thử

Mục tiêu của thang gợi ý (`hint ladder`) là gỡ đúng blocker (điểm chặn), không đưa một lời giải để sao chép. Sau mỗi mức, quay lại chạy Bot/test trước khi mở mức tiếp theo.

## Blocker A — Không biết bắt đầu sửa ở đâu

### Gợi ý 1

Chạy ba input đã chuẩn bị và so dòng `Trạng thái quyết định (Decision state)`:

~~~bash
go run ./cmd/bot
go run ./cmd/bot data/m00-missing-input.json
go run ./cmd/bot data/m00-conflicting-input.json
~~~

Tìm bốn state trong `internal/decision/ranking.go`. Từ chối quyết định (`abstain`) là tên hành vi; state cụ thể ở M00 là `GET_MORE_DATA` hoặc `HUMAN_REVIEW`.

### Gợi ý 2

Muốn đổi output, sửa hàm `run` trong `cmd/bot/main.go`. Hàm đã nhận `io.Writer`, vì vậy test có thể truyền `bytes.Buffer` và kiểm bằng `strings.Contains`.

### Gợi ý 3

Copy test `TestRunShowsSafeStarterStateInVietnamese`, đổi tên test và thêm một marker có ý nghĩa bằng tiếng Việt, ví dụ `Phiên bản công thức (Formula version): commission-per-order/v1`. Làm test fail trước, thêm output sau, rồi chạy lại tới PASS.

Không dịch enum/state, JSON key hoặc code identifier. Ví dụ giữ nguyên `RANK_SCENARIO`, `evidence_kind`, `commission_rate`, nhưng giải thích bằng tiếng Việt ở phần người học đọc thấy.

## Blocker B — Không biết ghi public observation thế nào

### Gợi ý 1

Copy `data/m00-observations.json` thành file riêng. Với từng record thật, dùng đúng các field:

~~~json
{
  "observation_id": "OBS-...",
  "product_name": "...",
  "source_url": "https://...",
  "observed_at": "2026-08-29T10:00:00+07:00",
  "access_method": "public_manual",
  "evidence_kind": "real",
  "price": 0,
  "currency": "VND",
  "commission_rate": null,
  "other_visible_signal": "...",
  "missing_fields": ["commission_rate"],
  "notes": "..."
}
~~~

Số `0` chỉ dùng nếu nguồn thật hiển thị 0. Không thấy số thì dùng `null` và ghi tên field vào `missing_fields`. `commission_rate` dùng số thập phân (`10%` → `0.10`); chỉ so score khi cùng currency.

### Gợi ý 2

`internal/observation/observation.go` dùng `*float64`: JSON `null`/field vắng thành `nil`, còn JSON `0` vẫn là một value có thật. Đừng đổi pointer về `float64` nếu bạn chưa có cách khác giữ `missing != 0`.

### Gợi ý 3

Nếu Bot trả `GET_MORE_DATA`, đọc từng dòng `Bằng chứng còn thiếu (Missing evidence)`. Không bịa field để đạt `RECOMMEND`; giữ state này và ghi bằng chứng tiếp theo cần lấy vẫn là một kết quả M00 hợp lệ.

## Blocker C — Không biết viết so sánh người với Bot

### Gợi ý 1

Trước khi chạy Bot trên file thật, dùng `templates/PUBLIC-OBSERVATION.md` để đóng băng xếp hạng của con người (`human ranking`), lý do (`reason`), bằng chứng mạnh nhất (`strongest evidence`) và giả định yếu nhất (`weakest assumption`).

### Gợi ý 2

Bot baseline chỉ biết `price × commission_rate`. Con người có thể biết mức phù hợp sản phẩm (`product fit`) nhưng phải đánh dấu phần đó là fact, estimate hay assumption.

### Gợi ý 3

So sánh đạt khi chỉ ra ít nhất một bất đồng hoặc một trường hợp đồng ý kèm lý do. Không cần sửa formula để ép Bot giống human.

## Khi vẫn bị chặn

Ghi command, toàn bộ error, điều đã thử và mức gợi ý đã dùng vào artifact M00. Lúc đó mới mở `lab/affiliate-bot/` để học một pattern kỹ thuật; reference hiện là snapshot legacy, không phải lời giải đúng mission mới.
