# Lesson Authoring Standard

> Chuẩn này áp dụng cho lesson mới từ Step 5 trở đi. `templates/LESSON.md` là authoring template; `templates/LESSON-NOTES.md` là evidence note của người học. Hai file phục vụ hai mục đích khác nhau.

## 1. Naming và path

Lesson file:

```text
lessons/part-XX/chapter-YY/X.Y-slug-kebab-case.md
```

Ví dụ:

```text
lessons/part-00/chapter-00/0.2-affiliate-bot-engineer-la-gi.md
lessons/part-12/chapter-38/38.4-affiliate-link-click-order-commission.md
```

Quy tắc:

- `part-XX` và `chapter-YY` dùng zero-padding 2 chữ số.
- Filename bắt đầu bằng lesson ID chính xác từ syllabus.
- Slug lowercase, dùng dấu `-`, ưu tiên ASCII để link/path ổn định.
- Không đổi lesson ID/title canonical nếu chưa đổi syllabus.

## 2. Metadata bắt buộc

Mỗi authored lesson phải có YAML front matter:

```yaml
lesson_id: "X.Y"
title: "Tên bài"
part: X
chapter: Y
effort: M
estimated_minutes: 60
status: planned
prerequisites: []
source_refs:
  canonical:
    - "S:PX/CY/LX.Y"
  training: []
  research: []
  external: []
last_verified: null
```

### `status`

Allowed:

- `planned`: scaffold/chưa viết đủ.
- `draft`: đã có nội dung nhưng chưa đạt authoring Definition of Done.
- `ready`: lesson content đã đủ để người học học và làm PASS cycle.

`status: ready` **không có nghĩa người học PASS**.

### `effort`

Dùng `S|M|L` theo [`EFFORT-MODEL.md`](EFFORT-MODEL.md). `XL` chủ yếu dành cho LAB/PROJECT/PASS Gate.

### `estimated_minutes`

Một estimate cụ thể nằm trong hoặc hợp lý với effort class. Đây là planning value và sẽ được calibration bằng actual time.

### `prerequisites`

Chỉ ghi dependency thật. Không tự động coi lesson trước là prerequisite.

Ví dụ:

```yaml
prerequisites:
  - "0.1"
  - "concept: basic affiliate flow"
```

### `source_refs`

Tuân theo [`SOURCE-MAPPING.md`](SOURCE-MAPPING.md). `canonical` phải có `S:` ref. `training`/`research` chỉ ghi ref thực sự dùng.

## 3. Heading hierarchy

- Chỉ có **một `#`** cho title lesson.
- Main sections dùng `##`.
- Subsections dùng `###`.
- Sub-subsections dùng `####` khi thật cần.
- Không nhảy từ `##` sang `####` nếu không có `###`.

Bài 0.1 hiện có nhiều section dùng `#`; Step 9 sẽ migrate mà không mất nội dung.

## 4. Minimum content contract

Lesson `ready` phải có:

1. Mục tiêu học tập đo được.
2. Prerequisites.
3. Source refs.
4. Concept cốt lõi.
5. Giải thích sâu.
6. Ví dụ minh họa.
7. Case thực tế/tình huống quyết định.
8. Misconceptions/failure modes.
9. Exercise + artifact path + DoD.
10. Quiz.
11. Answer key hoặc scoring rubric.
12. Explain-back.
13. 5 tiêu chí PASS.
14. Knowledge Base update.
15. Tóm tắt ngắn.
16. Tài liệu nguồn thực sự dùng.
17. Next action.

Không bắt buộc mọi section dài ngang nhau. S lesson phải gọn; L lesson có thể sâu hơn.

## 5. Mapping tới 5 PASS criteria

| PASS criterion | Authoring section tối thiểu |
|---|---|
| Concept | Objectives + Concept + Explanation |
| Example | Example + Real Case |
| Quiz ≥80% | Quiz + Answer key/rubric |
| Practice | Exercise + artifact + DoD |
| Explain-back | Explain-back + expected points |

Lesson không được `ready` nếu thiếu bất kỳ hàng nào.

## 6. Quiz và rubric

### Quiz size guideline

- S: 3–5 câu.
- M: 5–10 câu.
- L: 8–15 câu hoặc assessment tương đương.

### Quiz quality

Không chỉ hỏi định nghĩa. Nên có ít nhất một câu áp dụng/diagnostic/decision nếu scope lesson cho phép.

### Answer key

Bắt buộc với multiple choice/numeric/closed answer.

### Scoring rubric

Bắt buộc với case/tự luận/code/design khi không có một đáp án duy nhất.

Rubric phải chỉ rõ:

- tiêu chí chấm;
- điểm/weight;
- PASS threshold;
- lỗi nào là blocking misconception.

PASS quiz mặc định ≥80% theo [`PASS-CRITERIA.md`](PASS-CRITERIA.md).

## 7. Artifact và practice

Artifact phải là evidence có thể inspect được, ví dụ:

- markdown analysis;
- spreadsheet/data output;
- code/test;
- architecture/schema;
- dashboard screenshot/link;
- policy comparison with sources;
- experiment record;
- decision memo.

Không dùng “đã đọc”, “đã xem video”, “đã hiểu” làm artifact.

Với S lesson, artifact có thể là micro-artifact 5–15 phút. Không ép S thành M chỉ vì template dài.

## 8. External verification policy

External verification là bắt buộc khi lesson đưa claim có thể thay đổi theo thời gian, đặc biệt:

- platform policy/rules;
- commission/attribution window hiện hành;
- API availability/limits;
- legal/tax requirement;
- privacy/compliance regulation;
- pricing/fees/current product behavior;
- current software/library behavior nếu ảnh hưởng exercise.

### Ưu tiên nguồn

1. official platform/government/vendor docs;
2. primary standards/specifications;
3. reputable secondary sources nếu primary không đủ.

### Metadata

Khi có current verification:

```yaml
source_refs:
  external:
    - "official:<source-name-or-url-reference>"
last_verified: "YYYY-MM-DD"
```

Trong lesson phải phân biệt:

- canonical curriculum concept;
- current verified fact;
- author inference/example.

Không biến dữ kiện hiện hành thành “sự thật vĩnh viễn” chỉ vì có trong source 2026.08.

## 9. Authoring status Definition of Done

### `planned`

- metadata cơ bản có thể tồn tại;
- placeholder được phép;
- không được xem là lesson để học chính thức.

### `draft`

- phần lớn nội dung đã viết;
- có thể còn TODO, thiếu rubric/verification/review;
- không được quảng bá là hoàn chỉnh.

### `ready`

Chỉ dùng khi:

- metadata hợp lệ;
- source refs đúng;
- heading hierarchy chuẩn;
- objectives measurable;
- đủ Concept/Example/Quiz/Practice/Explain-back;
- answer key/rubric đầy đủ;
- artifact path rõ;
- current claims đã verify khi cần;
- không còn placeholder/TODO;
- links nội bộ hợp lý.

## 10. Compatibility với bài 0.1

Bài 0.1 hiện đã có nội dung đủ phong phú để migrate sang template mà không cần cắt bỏ substantive content. Khi Step 9 migrate:

- thêm YAML metadata;
- chuẩn hóa `#` → `##` cho main sections;
- thêm `source_refs` theo contract;
- gán effort/estimated_minutes;
- tách rõ authoring status;
- giữ nguyên objectives, explanations, case A/B, exercise, quiz 10 câu, answer key, explain-back, PASS và KB content;
- không đổi nội dung chỉ để khớp template nếu nội dung hiện tại đã tốt hơn minimum contract.

Template là **minimum contract**, không phải giới hạn chiều sâu.

## 11. Authoring workflow

```text
1. Read canonical lesson in S
2. Read SOURCE-MAPPING row
3. Resolve prerequisites + execution context
4. Assign S/M/L + estimated minutes
5. Author concept/example/case
6. Design artifact
7. Design quiz + answer key/rubric
8. Design explain-back
9. Verify current facts if needed
10. Check 5 PASS coverage
11. Set status=ready only when DoD passes
```

## 12. Anti-patterns

Không:

- tạo hàng trăm file placeholder rồi coi curriculum đã authored;
- dùng `LESSON-NOTES.md` làm lesson authoring template;
- để quiz không có answer key/rubric;
- gắn source supplement không thực sự hỗ trợ lesson;
- đưa policy/legal facts cũ mà không verification;
- ép mọi lesson có độ dài như nhau;
- tick roadmap vì lesson file tồn tại;
- nhầm `status: ready` với learner PASS.