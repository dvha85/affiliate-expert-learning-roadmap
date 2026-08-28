# Mô hình học Build-First v1

## 1. Authority (nguồn có thẩm quyền)

Build-First là một **execution layer (lớp thực thi việc học)** nằm trên active canonical curriculum (curriculum chuẩn hiện hành).

```text
NHỮNG GÌ CUỐI CÙNG PHẢI BIẾT
= sources/SYLLABUS-v2026.09.md
+ baseline v2026.08 được kế thừa
+ ROADMAP inventory đã chuẩn hóa

TIẾP THEO CẦN XÂY GÌ
= BUILD-FIRST.md + Mission system
```

Build-First không tạo một canonical syllabus revision (bản syllabus chuẩn mới) và không thay đổi 23 Parts / 89 Chapters / 671 lessons / 14 main Projects.

## 2. Vòng học

```text
Ship Target (Mục tiêu bàn giao)
→ Build smallest working slice (Xây phần nhỏ nhất chạy được)
→ Run (Chạy)
→ Observe gap/failure (Quan sát thiếu sót/lỗi)
→ Pull required knowledge (Lấy kiến thức cần thiết)
→ Improve implementation/decision logic (Cải tiến code/logic quyết định)
→ Test (Kiểm thử)
→ Operate (Vận hành)
→ Measure result (Đo kết quả)
→ Explain (Giải thích)
→ Save evidence (Lưu bằng chứng)
→ Ship Bot Version (Bàn giao phiên bản Bot)
```

Người học nên gặp một **lý do cụ thể** để cần một concept (khái niệm) trước khi dành nhiều giờ học concept đó trong trạng thái tách rời thực hành.

## 3. Bốn thực thể

### Lesson (Bài học)

Đơn vị kiến thức chuẩn. Lesson PASS độc lập và dựa trên evidence (bằng chứng).

### Mission (Nhiệm vụ thực hành)

Đơn vị build/run/operate với một ship target có thể quan sát. Một Mission có thể kéo kiến thức từ nhiều Part khác nhau.

### Canonical Project (Dự án chuẩn)

Một trong 14 integration milestones (mốc tích hợp) của curriculum. Mission có thể đóng góp evidence tái sử dụng cho Project, nhưng Mission ID không bao giờ trở thành Project ID.

### Bot Version (Phiên bản Bot)

Trạng thái sản phẩm sau một Mission. Đây không phải điểm số của learner.

## 4. Hai trục tiến độ

```text
PRODUCT PROGRESS (TIẾN ĐỘ SẢN PHẨM)
Mission → Bot Version chạy được → operational evidence (bằng chứng vận hành)

KNOWLEDGE PROGRESS (TIẾN ĐỘ KIẾN THỨC)
Lesson → knowledge evidence → PASS / RETRY
```

Learner có thể ship (bàn giao) một feature nhỏ trong khi nhiều Lesson vẫn chưa PASS. Mission có thể yêu cầu hiểu một **knowledge slice (phần kiến thức cần dùng)** của các Lesson đó trước Mission PASS, nhưng Mission không được tự thay đổi Lesson PASS.

## 5. Ba lớp kiến thức just-in-time (đúng lúc cần)

Mission dùng ba mức:

- **REQUIRED (Bắt buộc cho Mission)** — phải hiểu đủ để giải thích implementation/quyết định của Mission.
- **ON-DEMAND (Khi phát sinh nhu cầu)** — lấy khi implementation hoặc business context làm lộ nhu cầu thực sự.
- **REFERENCE (Tham khảo)** — hữu ích để đào sâu nhưng không phải Mission PASS gate (cổng PASS).

Điểm quan trọng:

```text
REQUIRED FOR MISSION
≠
FULL LESSON PASS
```

Ví dụ M00 có thể cần một phần của 0.1 và 0.2 để hiểu Bot đang phục vụ business flow nào; learner không bắt buộc phải hoàn thành toàn bộ PASS cycle của hai Lesson trước khi chạy dòng code đầu tiên.

Mapping (ánh xạ) Mission ↔ Knowledge được quản lý tập trung để không bulk-edit (sửa hàng loạt) front matter của 671 Lesson.

## 6. Learner workspace và reference implementation

Người học trực tiếp build tại:

```text
lab/learner/affiliate-bot/
```

Bản triển khai tham chiếu hiện tại:

```text
lab/affiliate-bot/
```

Reference implementation (bản tham chiếu) không phải starting state (trạng thái bắt đầu) của learner.

Quy tắc:

```text
learner attempt (tự thử)
→ observe failure/gap
→ knowledge pull
→ improve
→ reference chỉ dùng để đối chiếu khi cần
```

Điều này ngăn Build-First biến thành “đọc lời giải có sẵn”.

## 7. Tiến trình Go-first

Part 15 vẫn là formal Bot Engineering mastery (phạm vi làm chủ Bot Engineering chính thức). Build-First cho phép dùng Go sớm với scope hẹp.

```text
M00: package/main/function + test tối thiểu
M01: struct/JSON/error/validation
M02: SQL/repository/migration/history
M04+: context/scheduling/concurrency
M05+: retry/backoff/idempotency/timeout
sau đó: durable workflow/tool/AI/governance
```

Mastery được chứng minh về sau bằng engineering evidence rộng hơn.

## 8. Build-first không có nghĩa unsafe-first (làm nguy hiểm trước)

```text
BUILD CODE EARLY (viết code sớm)
≠
AUTOMATE REAL BUSINESS EARLY (tự động hóa kinh doanh thật sớm)
```

Các Mission đầu phải giảm external side effects (tác động bên ngoài). Consequential execution (thực thi có hậu quả đáng kể) vẫn phải đi qua deterministic policy/risk boundary (ranh giới chính sách/rủi ro xác định) và Human Approval khi cần.

## 9. Quy tắc capacity (quỹ thời gian)

Build-First thay sequencing (thứ tự học), không thay weekly capacity. Standard vẫn khoảng 9h/tuần; Accelerated vẫn khoảng 11–12h/tuần cho tới khi actual Mission data (dữ liệu thực tế từ Mission) đủ để recalibrate (hiệu chỉnh lại).

## 10. Anti-patterns (cách làm cần tránh)

Không:

- xóa hoặc đổi số Lesson chỉ vì Mission kéo kiến thức xuyên Part;
- tạo Project 15+ từ Mission ID;
- đánh dấu hàng loạt Lesson PASS khi một Mission ship;
- dạy nhiều tháng cú pháp Go trước Bot chạy đầu tiên;
- thêm AI autonomy trước deterministic decision/policy boundary;
- đưa external side effect có hậu quả vào Mission đầu chỉ để Bot trông “nâng cao” hơn;
- mở reference implementation trước khi learner có attempt nếu không có blocker thật;
- tính cùng một implementation nhiều lần thành Lesson artifact + Mission artifact + Project artifact khi đó thực sự là cùng một evidence.

## 11. Trạng thái cuối mong muốn

Curriculum cuối cùng phải tạo cảm giác:

```text
Tôi xây một Affiliate Intelligence Bot thật
→ Bot làm lộ thứ tôi chưa hiểu
→ Tôi học đúng concept đó
→ Tôi cải tiến Bot
→ Tôi vận hành và đo nó
→ Evidence chứng minh cả product progress và knowledge progress
```

## 12. Ngôn ngữ

Tiếng Việt là ngôn ngữ chính thức. English term (thuật ngữ tiếng Anh) được giữ khi cần độ chính xác kỹ thuật và phải có giải thích tiếng Việt khi quan trọng. Xem [`LANGUAGE-POLICY.md`](LANGUAGE-POLICY.md).