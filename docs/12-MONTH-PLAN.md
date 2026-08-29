# Hồ sơ 12 tháng — dự báo theo giờ tập trung

> Evidence (bằng chứng) là gate; calendar (lịch) không phải tiêu chí PASS. Hồ sơ này chỉ là **khung lập kế hoạch (`planning envelope`)** và phải được dự báo lại từ số liệu thực tế của người học.

## Nguyên tắc lập kế hoạch

Không khóa Mission vào một tháng cố định. Dùng **khung giờ tập trung + thời gian chờ bên ngoài tách riêng**:

- khoảng 5–8 giờ tập trung/tuần;
- thời gian chờ account/platform/outcome được ghi riêng, không tính như giờ học;
- safety/evidence gate không bị nén để giữ lịch;
- người học có thể tiếp tục phần kỹ thuật được Mission cho phép trong lúc Reality gate đang chờ;
- sau M00–M05 phải dự báo lại từ thời gian build/debug/business/review thực tế.

## Mục tiêu vòng lặp thực tế sớm

Mục tiêu sư phạm là đưa người học tới **hành động thị trường thật có tracking đầu tiên do người thực hiện (M03)** đủ sớm để curriculum nhận reality feedback (phản hồi từ thực tế), thay vì để nhiều tháng trôi qua chỉ với hạ tầng.

Ước lượng Mission hiện tại:

| Mission | Giờ tập trung danh nghĩa | Kết quả |
|---|---:|---|
| M00 | ~10h | quyết định đầu tiên dựa trên evidence |
| M01 | ~12h | history đáng tin cậy |
| M02 | ~12h | AI advisor có grounding |
| M03 | ~14h | lần publish có tracking đầu tiên do người thực hiện |
| **M00→M03** | **~48h** | hành động thị trường thật có tracking đầu tiên |

Với 5–8 giờ tập trung/tuần, ~48h tương đương khoảng **6–10 tuần làm việc tập trung**, chưa tính blocker/thời gian chờ bên ngoài. Vì vậy “M03 vào tháng 5” không còn là mục tiêu mặc định.

Nếu người học bị chặn bởi account/platform/quyền truy cập thực tế, ghi `BLOCKED_EXTERNAL` và dự báo lại; không dùng sample thay cho E2.

## Các dải lập kế hoạch

| Dải | Mission | Mục đích |
|---|---|---|
| B1 | M00 | khởi động + evidence công khai thật + quyết định đầu tiên |
| B2 | M01–M02 | dữ liệu đáng tin + AI có grounding, giữ fallback tất định |
| B3 | M03 | publish có tracking do người thực hiện càng sớm càng hợp lý sau khi đủ điều kiện |
| B4 | M04–M05 | analytics outcome thật + cải tiến đầu tiên đã review |
| B5 | M06–M07 | watcher đáng tin cậy + `DecisionPacket`/memory |
| B6 | M08 | agent thu evidence chỉ-đọc |
| B7 | M09–M10 | shadow approval → tự động hóa giới hạn có quản trị |
| B8 | M11 | vòng production khép kín + diễn tập recovery |

Lịch 12 tháng là **khung trên để lập kế hoạch**, không phải lý do kéo dài một Mission đã PASS hoặc trì hoãn hành động thực tế khi các điều kiện tiên quyết đã đủ.

## Các điểm dự báo lại

Dự báo lại sau:

1. M00 — vì đây là số liệu setup/build/evidence đầu tiên của người mới hoàn toàn;
2. M03 — vì người học đã có hành động công khai có tracking đầu tiên;
3. M05 — vì đã có vòng học từ thị trường khép kín đầu tiên;
4. M07 — vì workload reliability/decision đã quan sát được;
5. M10 — trước vòng production khép kín.

Mỗi lần dự báo lại phải tách:

```text
giờ tập trung cho build/debug/business/review
+
ngày chờ/blocker bên ngoài
```

Không cộng hai loại trên thành một con số “giờ học”.

Xem thêm [`EFFORT-MODEL.md`](EFFORT-MODEL.md) và [`AFFILIATE-METRIC-REVENUE-SPINE.md`](AFFILIATE-METRIC-REVENUE-SPINE.md).
