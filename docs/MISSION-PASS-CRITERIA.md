# Tiêu chí Mission PASS

Mission PASS phản ánh **product/evidence progress (tiến độ sản phẩm/bằng chứng)** và độc lập với canonical Lesson PASS.

## Tiêu chí nền

Một Mission chỉ PASS khi toàn bộ tiêu chí liên quan đã đạt:

- [ ] **Feature works (Tính năng chạy đúng)** — ship target có thể demo được.
- [ ] **Bot runs (Bot chạy được)** — run path đã ghi trong Mission hoạt động đúng với scope.
- [ ] **Tests pass (Kiểm thử đạt)** — automated/manual checks cần thiết đều đạt.
- [ ] **Data flows (Dữ liệu đi qua đúng luồng)** — sample/real data đi tới output dự kiến khi Mission có data flow.
- [ ] **Output is inspectable (Đầu ra kiểm tra được)** — learner có thể cho xem kết quả, không chỉ nói “đã xong”.
- [ ] **Failure case tested (Đã thử tình huống lỗi)** — ít nhất một failure/invalid-input scenario phù hợp scope đã được thực hiện.
- [ ] **Required knowledge understood (Hiểu kiến thức bắt buộc)** — learner hiểu **knowledge slice** đủ để giải thích implementation/quyết định của Mission.
- [ ] **Explain-back passes (Giải thích lại đạt)** — learner giải thích được vì sao solution hoạt động và trade-off quan trọng.
- [ ] **Evidence saved (Đã lưu bằng chứng)** — code/result/test evidence được link hoặc lưu lại.

## Tiêu chí engineering theo scope

Chỉ thêm khi Mission thực sự đưa capability đó vào:

- [ ] timeout/cancellation (hết thời gian/hủy);
- [ ] retry/backoff (thử lại/tăng thời gian chờ);
- [ ] idempotency/deduplication (lặp an toàn/chống trùng);
- [ ] persistence/recovery (lưu bền vững/phục hồi);
- [ ] observability (khả năng quan sát);
- [ ] least privilege/secrets handling (quyền tối thiểu/xử lý bí mật);
- [ ] deterministic policy/risk (chính sách/rủi ro xác định);
- [ ] Human Approval (phê duyệt con người);
- [ ] rollback/compensation/kill switch (quay lui/bù lỗi/dừng khẩn cấp);
- [ ] cost/resource checks (kiểm chi phí/tài nguyên).

Không ép M00 phải có control nâng cao chỉ để “đủ checklist”. Criteria tăng theo side effect (tác động bên ngoài) và failure mode (kiểu lỗi) thật.

## Required knowledge không đồng nghĩa full Lesson PASS

```text
Mission required knowledge
= hiểu phần kiến thức cần để build/giải thích Mission

Full Lesson PASS
= Concept + Example + Quiz + Practice artifact + Explain-back
```

Do đó:

```text
Mission PASS
≠
Lesson PASS
```

Mission không bao giờ tự ghi Lesson PASS. Một Mission có thể chỉ cần một slice của Lesson để ship an toàn, trong khi learner vẫn cần hoàn thành PASS cycle đầy đủ của Lesson đó về sau. Ngược lại, Lesson artifact có thể được reuse (tái sử dụng) làm Mission evidence khi thật sự chứng minh cùng yêu cầu.

## Learner workspace và reference

PASS phải dựa trên implementation/evidence mà learner thực sự build/hiểu trong learner workspace. Reference implementation chỉ dùng để đối chiếu hoặc gỡ blocker; copy reference không tự tạo Mission PASS.

## Review decision (quyết định review)

Các trạng thái learner:

- `✅ PASS` — đủ tiêu chí bắt buộc.
- `🟦 Awaiting Review (Chờ review)` — implementation có nhưng evidence/explain-back chưa review xong.
- `⛔ Blocked (Bị chặn)` — có prerequisite bên ngoài hoặc blocker kỹ thuật/business chưa giải quyết.
- `🟨 In Progress (Đang làm)` — còn công việc trong scope.

Không hạ chất lượng PASS chỉ để đạt ngày kế hoạch.