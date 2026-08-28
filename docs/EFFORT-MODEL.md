# Effort Model — S / M / L / XL

> Mục tiêu của effort model là lập kế hoạch theo **thời gian để PASS**, không theo số checkbox hoặc độ dài bài viết.

Roadmap có 671 bài học nhưng các bài không có trọng lượng bằng nhau. Một lesson thuật ngữ như `Merchant` không nên được lập lịch ngang với một lesson phải code, phân tích dữ liệu hoặc kiểm chứng policy.

## 1. Đơn vị đo

Effort của lesson bao gồm thời gian cần thiết để hoàn thành đủ chu trình:

```text
LEARN → EXPLAIN → APPLY → TEST → PASS
```

Bao gồm:

- đọc/học concept;
- tự giải thích;
- example/case;
- practice của lesson;
- quiz;
- explain-back;
- ghi evidence/lesson note tối thiểu.

Không đo số từ của lesson. Không PASS nhanh hơn chỉ vì bài viết ngắn.

## 2. Bốn mức effort

| Mức | Khoảng thời gian tham chiếu | Midpoint dùng để planning | Dùng khi |
|---|---:|---:|---|
| **S — Small** | 15–30 phút | **0.375 giờ** | Một concept/thuật ngữ tương đối atomic; example ngắn; micro-practice; quiz/explain-back đơn giản |
| **M — Medium** | 45–75 phút | **1 giờ** | Có case/calculation/research nhỏ; cần tạo artifact ngắn hoặc so sánh/ra quyết định |
| **L — Large** | 1.5–3 giờ | **2.25 giờ** | Có implementation, coding, dataset, phân tích nhiều bước, policy/legal verification hoặc artifact đáng kể |
| **XL — Integration Gate** | thường 4–8 giờ, có thể nhiều buổi | Không dùng midpoint cố định | LAB, PROJECT, PASS Gate, capstone/integration milestone |

`XL` không phải cách gọi một lesson “rất khó”. Nó là work package tích hợp nhiều lesson. Capstone lớn có thể tách thành nhiều XL work package.

## 3. Decision rule để gán effort cho lesson

Dùng rule theo thứ tự dưới đây.

### S — Small

Gán `S` khi lesson chủ yếu là một đơn vị kiến thức atomic và để PASS chỉ cần:

- giải thích concept bằng lời của mình;
- một example nhỏ;
- micro-practice hoặc nhận diện đúng/sai;
- quiz + explain-back ngắn.

Ví dụ loại bài thường rơi vào S: role/entity, thuật ngữ, metric definition, taxonomy, concept nền.

### M — Medium

Nâng lên `M` nếu lesson yêu cầu ít nhất một trong các việc sau:

- tính toán hoặc phân tích một case có nhiều biến;
- research nhỏ và lưu evidence;
- so sánh lựa chọn và giải thích quyết định;
- tạo artifact có thể tái sử dụng;
- nối từ concept sang một quyết định business thực tế.

### L — Large

Nâng lên `L` nếu lesson yêu cầu ít nhất một trong các việc sau:

- code/implementation phải chạy hoặc có test;
- thiết kế schema/architecture/pipeline;
- làm việc với dataset hoặc historical data;
- phân tích nhiều bước cần kiểm chứng;
- kiểm tra policy/legal hiện hành và lưu nguồn/evidence;
- tạo artifact kỹ thuật hoặc analytical deliverable đáng kể.

### XL — Integration Gate

Dùng `XL` cho:

- LAB;
- PROJECT;
- PASS Gate tích hợp nhiều lesson;
- deployment/capstone milestone;
- retrospective/integration có scope nhiều buổi.

LAB/PROJECT/PASS Gate được budget riêng, không biến toàn bộ lesson trong phần thành XL.

## 4. Quy tắc chống double-count

Project và lesson có thể dùng cùng artifact. Vì vậy:

```text
Lesson effort
= thời gian để tạo learning + evidence của lesson

XL gate effort
= chỉ phần integration / review / hardening / demo tăng thêm
```

Không cộng lại toàn bộ thời gian tạo artifact nếu artifact đã được tính trong lesson.

Ví dụ: một schema được tạo trong lesson 38.x và sau đó dùng cho Project 7. Project 7 chỉ tính phần tích hợp, validation, demo và retrospective còn lại.

## 5. Escalation rules

- Bài về **policy/legal/platform rule đang thay đổi**: tối thiểu `M`; nếu phải research nhiều nguồn hoặc impact analysis thì `L`.
- Bài có **code phải chạy/test**: tối thiểu `L`.
- Bài chỉ đọc định nghĩa nhưng PASS yêu cầu build artifact đáng kể: không được giữ `S`; nâng theo work thực tế.
- Nếu actual time vượt upper bound của class lặp lại từ 2 lần trở lên, re-estimate lesson/class thay vì coi đó là lỗi của người học.
- Khi có actual data, ưu tiên actual median của các lesson tương tự hơn midpoint mặc định.

## 6. Metadata contract cho lesson tương lai

Canonical lesson template ở Step 5 sẽ dùng tối thiểu:

```yaml
lesson_id: "X.Y"
effort: S # S | M | L
estimated_minutes: 30
status: planned
```

`XL` chủ yếu nằm ở LAB/PROJECT/PASS Gate metadata, không mặc định gán cho lesson thường.

Lesson note nên lưu thêm actual time để sau này calibration:

```text
Expected effort: M
Actual time: 70 phút
Variance: +10 phút so với midpoint/range tham chiếu
```

## 7. Baseline planning v0.1 cho 671 lesson

Bảng dưới đây là **planning allocation**, chưa phải final per-lesson tagging. Nó được dùng làm đầu vào cho Step 2 để kiểm tra tính khả thi của timeline. Khi lesson được author theo Step 5, `effort` thực tế của từng lesson sẽ thay thế baseline này.

| Part | S slots | M slots | L slots | Lesson hours range | Midpoint hours |
|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 5 | 0 | 5.5–9.8 | 7.6 |
| 1 | 30 | 4 | 0 | 10.5–20.0 | 15.2 |
| 2 | 24 | 10 | 0 | 13.5–24.5 | 19.0 |
| 3 | 24 | 8 | 1 | 13.5–25.0 | 19.2 |
| 4 | 22 | 6 | 0 | 10.0–18.5 | 14.2 |
| 5 | 40 | 9 | 1 | 18.2–34.2 | 26.2 |
| 6 | 18 | 8 | 0 | 10.5–19.0 | 14.8 |
| 7 | 15 | 6 | 0 | 8.2–15.0 | 11.6 |
| 8 | 28 | 10 | 2 | 17.5–32.5 | 25.0 |
| 9 | 32 | 11 | 1 | 17.8–32.8 | 25.2 |
| 10 | 18 | 6 | 0 | 9.0–16.5 | 12.8 |
| 11 | 8 | 6 | 0 | 6.5–11.5 | 9.0 |
| 12 | 10 | 10 | 3 | 14.5–26.5 | 20.5 |
| 13 | 11 | 9 | 3 | 14.0–25.8 | 19.9 |
| 14 | 15 | 10 | 3 | 15.8–29.0 | 22.4 |
| 15 | 18 | 18 | 6 | 27.0–49.5 | 38.2 |
| 16 | 9 | 10 | 4 | 15.8–29.0 | 22.4 |
| 17 | 16 | 15 | 5 | 22.8–41.8 | 32.2 |
| 18 | 16 | 14 | 5 | 22.0–40.5 | 31.2 |
| 19 | 12 | 14 | 6 | 22.5–41.5 | 32.0 |
| 20 | 18 | 12 | 2 | 16.5–30.0 | 23.2 |
| 21 | 5 | 7 | 5 | 14.0–26.2 | 20.1 |
| 22 | 10 | 8 | 2 | 11.5–21.0 | 16.2 |
| **Tổng** | **406** | **216** | **49** | **337–620** | **478.5** |

Kiểm tra count:

```text
406 S + 216 M + 49 L = 671 lessons
```

Midpoint lesson workload hiện tại khoảng **478.5 giờ**, chưa cộng budget tăng thêm cho XL integration gates. Đây là lý do timeline phải được tính theo giờ thay vì lấy `671 / số tháng`.

## 8. Cách Step 2 sử dụng effort model

Step 2 phải:

1. lấy midpoint/range theo Part làm baseline;
2. thêm weekly review và XL integration budget;
3. không double-count project artifacts;
4. so với capacity thực tế theo tuần;
5. chỉ sau đó mới phân bổ tháng/tuần.

Không dùng cách:

```text
113 bài / 4 tuần = 28 bài/tuần
```

mà không xét S/M/L/Lab/Project.

## 9. Calibration sau khi bắt đầu học

Mỗi Chủ nhật có thể ghi actual time của các lesson đã PASS. Sau tối thiểu 8–12 lesson cùng class:

- tính median actual time;
- so với range mặc định;
- điều chỉnh estimate cho các lesson tương tự nếu cần;
- giữ lịch như forecast sống, không coi estimate ban đầu là cam kết cứng.

Mục tiêu của effort model là tạo **kỳ vọng thời gian trung thực**, không tạo thêm bureaucracy.