# Mô hình khối lượng học — Core hướng outcome

Số lượng lesson không phải mô hình workload (khối lượng công việc). Core hiện có 63 micro-lesson nhưng phần lớn thời gian phải nằm ở build, debug, quan sát kinh doanh, cửa sổ outcome, review và retry.

## Khung lập kế hoạch ban đầu

~~~text
Thời gian tập trung của người học: khoảng 240–360 giờ
Thời gian chờ outcome: ghi riêng, không tính như giờ làm tập trung
Độ tin cậy của forecast: thấp cho tới khi có pilot M00–M05
~~~

| Gate | Mission | Dự báo giờ tập trung |
|---|---|---:|
| G1 — Quyết định đầu tiên dựa trên evidence | M00 | 12–24 |
| G2 — Dữ liệu đáng tin + AI có grounding | M01–M02 | 35–60 |
| G3 — Vòng học thị trường đầu tiên | M03–M05 | 55–90 |
| G4 — Vòng production có quản trị | M06–M11 | 120–186 |
| **Tổng** | | **222–360** |

Dùng 240–360 giờ làm planning envelope (khung lập kế hoạch) để có khoảng review/integration tối thiểu. Đây là forecast (dự báo), không phải lời hứa.

## Ước lượng danh nghĩa của các Mission đã draft

Các Mission đang author/draft có ước lượng hẹp hơn Gate envelope và hữu ích cho kế hoạch gần hạn:

| Mission | Giờ tập trung danh nghĩa | Ghi chú |
|---|---:|---|
| M00 | ~10h | ready / mục tiêu pilot |
| M01 | ~12h | draft |
| M02 | ~12h | draft |
| M03 | ~14h | draft |
| **M00→M03** | **~48h** | hành động thị trường có tracking đầu tiên do người thực hiện nếu không có blocker bên ngoài |

Các ước lượng này **không ghi đè Gate envelope** và chưa đủ evidence để coi là thời lượng chuẩn. Chúng chỉ ngăn calendar profile vô tình kéo bốn Mission đầu dài hơn nhiều so với chính thiết kế Mission.

Hàm ý lập kế hoạch:

```text
giờ tập trung quyết định nhịp gần hạn
thời gian chờ bên ngoài quyết định độ trễ lịch
tháng trên lịch không quyết định PASS
```

Sau pilot, actuals (số liệu thực tế) được ưu tiên hơn nominal estimate.

## Micro-lesson

- S: 20–30 phút kéo kiến thức + áp dụng nhỏ;
- M: 30–45 phút;
- L: 45–75 phút, chỉ khi không thể chia mà vẫn giữ được decision context.

Thời gian lesson phải gồm TRY/OBSERVE/APPLY/TEST, không chỉ thời gian đọc.

## Số liệu thực tế theo Mission

Ghi riêng:

- build;
- debug;
- operate (vận hành);
- knowledge pull (kéo kiến thức);
- review/retry;
- quan sát/hành động kinh doanh;
- chờ outcome bên ngoài.

Không đếm hai lần (`double-count`). Waiting time có thể kéo dài calendar nhưng không được biến thành “giờ học”.

## Mục tiêu phản hồi thực tế đầu tiên

M03 là hành động thị trường thật có tracking đầu tiên do người thực hiện. Curriculum nên đưa learner tới đó ngay khi prerequisite/evidence của M00–M02 đủ; không trì hoãn chỉ để khớp lịch 12/15 tháng.

Ở mức danh nghĩa ~48 giờ tập trung:

- 4 h/tuần → khoảng 12 tuần;
- 5 h/tuần → khoảng 10 tuần;
- 6 h/tuần → khoảng 8 tuần;
- 8 h/tuần → khoảng 6 tuần.

Đây chỉ là phép tính hỗ trợ lập kế hoạch, không phải lời hứa. Blocker và outcome waiting được cộng vào calendar riêng.

## Quy tắc dự báo lại

Sau M00–M05:

1. lấy median actual/planned theo learner;
2. tách setup, coding, business work, debug và review;
3. xác định blocker ngoài tầm kiểm soát;
4. chỉ áp hệ số cho Mission tương tự;
5. giữ nguyên evidence/safety gate và kéo dài timeline nếu cần.

Nên dự báo lại sớm sau M00 và M03 để phát hiện overhead của người mới hoàn toàn và friction (ma sát) thị trường thật trước khi dự báo phần còn lại.

Không dùng dữ liệu một learner để tuyên bố duration phổ quát. Dữ liệu một người chỉ là calibration (hiệu chỉnh) sơ bộ.
