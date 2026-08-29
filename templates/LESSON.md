---
lesson_id: "X.Y"
title: "Tên micro-lesson"
part: X
chapter: Y
track: core # core | advanced | reference
mission_refs: ["MXX"]
practice_first: true
effort: S # S | M | L
estimated_minutes: 30
status: planned # planned | draft | ready
prerequisites: []
source_refs:
  active:
    - "CUR:PX/CY/LX.Y"
  historical: []
  training: []
  research: []
  external: []
last_verified: null
---

# Bài X.Y — Tên micro-lesson

> **Track:** `core` · **Mission:** `MXX` · **Thời lượng dự kiến:** 30 phút
> Bài này được kéo vào sau một attempt trong Mission. Không đọc trước chỉ để “hoàn thành lý thuyết”.

## 1. Trigger — Vì sao cần bài này ngay bây giờ?

Mô tả output, failure, decision gap hoặc câu hỏi thực tế vừa xuất hiện trong Mission.

```text
Attempt đã làm:
Điều vừa quan sát:
Câu hỏi cần trả lời:
```

## 2. Try First — Thử trước trong 5–15 phút

Cho một nhiệm vụ nhỏ có thể chạy, quan sát hoặc ra quyết định trước khi giải thích concept.

- Input/evidence sử dụng: ...
- Hành động: ...
- Output cần lưu: ...

Không đưa sẵn lời giải hoàn chỉnh ở bước này.

## 3. Observe — Ghi điều thực sự xảy ra

Người học ghi:

- expected (đã kỳ vọng gì);
- observed (đã thấy gì);
- khác biệt hoặc failure;
- evidence kind: `real | test | synthetic | replay`.

Không được trình bày sample/synthetic như bằng chứng thị trường thật.

## 4. Minimum Knowledge — Kiến thức tối thiểu

Giải thích tối đa 1–3 concept cần để xử lý đúng gap vừa thấy:

1. concept là gì;
2. dùng để ra quyết định nào;
3. failure mode hoặc trade-off quan trọng;
4. điều chưa cần học ở Mission hiện tại.

Với dữ kiện platform, luật, giá, API hoặc model có thể thay đổi, phải dùng nguồn hiện hành và `last_verified`.

## 5. Apply — Áp dụng ngay vào Bot hoặc business evidence

Yêu cầu người học sửa code/data/decision record đang có, rồi chạy lại trên đúng case đã quan sát.

```text
Before:
Change:
After:
Why the result changed:
```

## 6. Test a Failure — Kiểm thử một tình huống lỗi

Tạo ít nhất một invalid, stale, missing, conflicting hoặc failure case phù hợp scope.

- Bot phải làm gì?
- Bot phải từ chối/abstain khi nào?
- Điều gì tuyệt đối không được xảy ra?

## 7. Evidence — Bằng chứng áp dụng

Lưu evidence vào artifact của Mission đang chạy, không tạo tài liệu trùng nếu cùng output đã chứng minh requirement.

Evidence tối thiểu:

- attempt trước khi đọc;
- output/failure đã quan sát;
- thay đổi đã áp dụng;
- before/after hoặc baseline comparison;
- test cuối;
- source/time/evidence kind khi dùng dữ liệu business.

## 8. Checkpoint — Tự kiểm tra nhanh

1. ...?
2. ...?
3. Với case ..., bạn sẽ làm gì và vì sao?

<details>
<summary><strong>Đáp án/rubric</strong></summary>

- Ý bắt buộc 1: ...
- Ý bắt buộc 2: ...
- Blocking misconception: ...

</details>

## 9. Explain-back — Giải thích lại

Không nhìn tài liệu, trả lời:

> “Vì sao thay đổi vừa làm tốt hơn baseline, bằng chứng nào hỗ trợ, và khi nào kết luận này không còn đúng?”

Rubric:

- đúng concept;
- chỉ ra quan hệ nhân quả hoặc giới hạn suy luận;
- liên hệ trực tiếp với code/evidence;
- nêu failure/trade-off;
- nói được bước đo tiếp theo.

## 10. Applied / Retry — Kết quả

Knowledge slice chỉ được coi là **applied** trong Mission khi:

- [ ] đã TRY trước khi đọc phần giải thích;
- [ ] đã APPLY vào Bot hoặc evidence thật;
- [ ] happy path và failure case đều được quan sát;
- [ ] evidence đúng loại được lưu;
- [ ] explain-back không có blocking misconception.

Thiếu bất kỳ mục nào thì ghi `RETRY`; việc đọc xong không tạo PASS.

## 11. Next Action — Hành động tiếp theo

Quay lại Mission, thực hiện checkpoint tiếp theo. Chỉ mở micro-lesson khác khi output/failure/decision mới tạo ra nhu cầu.
