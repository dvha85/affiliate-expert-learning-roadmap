# Tiêu chuẩn biên soạn micro-lesson

> [Lesson template](../templates/LESSON.md) là contract biên soạn. Curriculum là **Mission-first**: lesson chỉ tồn tại để giải quyết một gap có thể quan sát trong Mission.

## 1. Vai trò của lesson

Một Core lesson phải đồng thời thỏa bốn điều kiện:

1. cần cho một Mission cụ thể;
2. làm thay đổi code, evidence hoặc quyết định ngay;
3. có thể học và áp dụng trong khoảng 20–45 phút;
4. không phải current fact có thể chuyển thành reference ngắn.

Không tách mỗi thuật ngữ thành một lesson. Không viết một chương lý thuyết dài rồi thêm exercise ở cuối.

## 2. Path và metadata

```text
lessons/part-XX/chapter-YY/X.Y-slug.md
```

Front matter bắt buộc:

```yaml
lesson_id: "X.Y"
title: "..."
part: X
chapter: Y
track: core
mission_refs: ["M00"]
practice_first: true
effort: S
estimated_minutes: 30
status: planned
prerequisites: []
source_refs:
  active:
    - "CUR:PX/CY/LX.Y"
  historical: []
  training: []
  research: []
  external: []
last_verified: null
```

`status: ready` chỉ nói nội dung đủ dùng; không có nghĩa learner đã applied hay Mission đã PASS.

## 3. Content contract cho `ready`

Thứ tự section bắt buộc:

1. `Trigger` — gap nào trong Mission khiến bài cần thiết;
2. `Try First` — attempt 5–15 phút trước lời giải;
3. `Observe` — expected/observed/evidence kind;
4. `Minimum Knowledge` — tối đa 1–3 concept;
5. `Apply` — sửa Bot/data/decision đang có;
6. `Test a Failure` — ít nhất một failure mode;
7. `Evidence` — before/after và nguồn;
8. `Checkpoint` — câu hỏi/rubric ngắn;
9. `Explain-back` — vì sao, giới hạn, bước đo tiếp;
10. `Applied / Retry`;
11. `Next Action` — quay lại Mission.

## 4. Quy tắc practice-first

- Attempt phải có output hoặc quyết định quan sát được.
- Không đưa sẵn implementation hoàn chỉnh trước attempt.
- Knowledge chỉ giải thích phần cần để vượt gap hiện tại.
- Mỗi lesson phải áp dụng lại trên đúng case đã quan sát.
- Quiz nhớ thuật ngữ không thể thay code/evidence/decision artifact.
- Cùng evidence có thể dùng cho Lesson và Mission nếu thật sự chứng minh cùng requirement; không sao chép để tăng số artifact.

## 5. Real Evidence Ladder

Lesson gắn Mission có Reality gate phải nêu rõ evidence kind yêu cầu. Không dùng sample để thay URL công khai, public artifact hoặc analytics thật.

Không có click/order không đồng nghĩa học viên FAIL. `0` là outcome hợp lệ nếu hệ thống thật báo 0; missing không được đổi thành 0.

## 6. Freshness và nguồn

Platform policy, pháp luật, tax, API, model/SDK, attribution window và điều kiện tài khoản là current facts. Chúng phải:

- trỏ tới nguồn chính thức/primary khi có thể;
- có external source ID;
- ghi `last_verified: YYYY-MM-DD`;
- được tách khỏi Core khi chỉ là chi tiết platform thay đổi nhanh.

Các file cũ trong `sources/` là historical provenance, không phải active structural authority.

## 7. Definition of Done

Micro-lesson chỉ được chuyển `ready` khi:

- metadata đầy đủ và trỏ tới ít nhất một Mission;
- `practice_first: true`;
- Try First chạy/quan sát được;
- Minimum Knowledge không vượt scope;
- Apply thay đổi một artifact thật;
- failure case, evidence path và explain-back rubric cụ thể;
- không có placeholder;
- link và freshness hợp lệ;
- người mới có thể hiểu hướng dẫn mà không cần đọc reference implementation trước.
