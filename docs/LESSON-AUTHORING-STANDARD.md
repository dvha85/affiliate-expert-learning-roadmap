# Lesson Authoring Standard

> `templates/LESSON.md` là authoring template; `templates/LESSON-NOTES.md` là evidence note của người học. Hai file phục vụ hai mục đích khác nhau.

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

- `part-XX` và `chapter-YY` dùng zero-padding 2 chữ số;
- filename bắt đầu bằng lesson ID chính xác từ syllabus;
- slug lowercase, dùng dấu `-`, ưu tiên ASCII;
- không đổi lesson ID/title canonical nếu chưa đổi syllabus.

## 2. Metadata bắt buộc

Mỗi lesson phải có YAML front matter:

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

- `planned`: scaffold/chưa viết đủ;
- `draft`: đã có nội dung nhưng chưa đạt authoring Definition of Done;
- `ready`: đủ để learner học và chạy PASS cycle.

`status: ready` **không có nghĩa learner PASS**.

### `effort`

Dùng `S|M|L` theo [`EFFORT-MODEL.md`](EFFORT-MODEL.md). `XL` chủ yếu dành cho LAB/PROJECT/PASS Gate.

### `estimated_minutes`

Planning estimate cụ thể, calibration dần bằng actual time.

### `prerequisites`

Chỉ ghi dependency thật. Không tự động coi lesson trước là prerequisite.

### `source_refs`

Tuân theo [`SOURCE-MAPPING.md`](SOURCE-MAPPING.md). `canonical` phải có `S:` ref; `training`/`research` chỉ ghi ref thực sự dùng.

Current/external facts tuân theo [`FRESHNESS-POLICY.md`](FRESHNESS-POLICY.md):

```yaml
source_refs:
  external:
    - "EXT:TIKTOK:PPS"
last_verified: "2026-08-28"
```

Contract:

- external refs có dữ liệu → `last_verified` bắt buộc là `YYYY-MM-DD`;
- `last_verified` có ngày → phải có external refs;
- `last_verified` là ngày **đã kiểm chứng**, không phải ngày lesson được tạo.

## 3. Heading hierarchy

- Chỉ có **một `#`** cho title lesson.
- Main sections dùng `##`.
- Subsections dùng `###`.
- Sub-subsections dùng `####` khi thật cần.
- Không nhảy từ `##` sang `####` nếu không có `###`.

Bài 0.1 là reference implementation hiện tại cho hierarchy và content contract.

## 4. Quy ước thuật ngữ song ngữ

Curriculum được viết chủ yếu bằng tiếng Việt nhưng phải giúp người học làm quen với thuật ngữ tiếng Anh thực tế dùng trong Affiliate, Marketing, Data và Engineering.

Quy tắc mặc định cho thuật ngữ chuyên ngành beginner-facing:

```text
English Term (Tiếng Việt)
```

Ví dụ:

```text
Conversion Potential (Khả năng chuyển đổi)
Product–Audience Fit (Mức độ phù hợp giữa sản phẩm và đối tượng)
Refund Risk (Rủi ro hoàn tiền/trả hàng)
```

### 4.1. Lần xuất hiện đầu tiên

Ở lần xuất hiện có ý nghĩa đầu tiên trong lesson hoặc section, ưu tiên viết song ngữ.

Ví dụ:

> CVR (Conversion Rate — Tỷ lệ chuyển đổi) là tỷ lệ chuyển đổi từ một bước funnel sang hành động mục tiêu.

Sau khi đã giải thích, có thể dùng `CVR` hoặc `Conversion Rate` ở các đoạn sau nếu ngữ cảnh rõ.

### 4.2. Bảng/list dùng để học hoặc ra quyết định

Nếu bảng/list chứa các tiêu chí người học phải ghi nhớ hoặc sử dụng để phân tích, ưu tiên giữ song ngữ trực tiếp trong bảng/list.

Ví dụ:

```text
Demand (Nhu cầu thị trường)
Conversion Potential (Khả năng chuyển đổi)
Competition (Mức độ cạnh tranh)
```

### 4.3. Code, identifier, protocol và framework

Không dịch tên function, API, identifier, protocol hoặc framework bên trong code.

Ví dụ giữ nguyên:

```text
CalculateOpportunityScore()
ActionIntent
PostgreSQL
Model Context Protocol (MCP)
OpenTelemetry
```

Phần giải thích xung quanh phải dùng tiếng Việt dễ hiểu.

### 4.4. Không dịch máy móc

Bản dịch trong ngoặc là **learner aid**, không nhất thiết là tên chính thức của platform/vendor. Nếu thuật ngữ có nhiều cách dịch, giữ English term để bảo toàn nghĩa và dùng một bản dịch nhất quán trong curriculum.

Glossary dùng chung: [`GLOSSARY-VI.md`](GLOSSARY-VI.md).

Lesson có thuật ngữ reusable chưa có trong glossary nên bổ sung glossary hoặc ít nhất dùng bản dịch nhất quán với các lesson hiện có.

## 5. Minimum content contract

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

## 6. Mapping tới 5 PASS criteria

| PASS criterion | Authoring section tối thiểu |
|---|---|
| Concept | Objectives + Concept + Explanation |
| Example | Example + Real Case |
| Quiz ≥80% | Quiz + Answer key/rubric |
| Practice | Exercise + artifact + DoD |
| Explain-back | Explain-back + expected points |

Lesson không được `ready` nếu thiếu bất kỳ hàng nào.

## 7. Quiz và rubric

### Quiz size guideline

- S: 3–5 câu.
- M: 5–10 câu.
- L: 8–15 câu hoặc assessment tương đương.

Không chỉ hỏi định nghĩa; nên có ít nhất một câu áp dụng/diagnostic/decision nếu scope cho phép.

Answer key bắt buộc với multiple choice/numeric/closed answer. Scoring rubric bắt buộc với case/tự luận/code/design khi không có một đáp án duy nhất.

Rubric phải chỉ rõ:

- tiêu chí chấm;
- điểm/weight;
- PASS threshold;
- blocking misconception.

PASS quiz mặc định ≥80% theo [`PASS-CRITERIA.md`](PASS-CRITERIA.md).

## 8. Artifact và practice

Artifact phải là evidence inspect được, ví dụ:

- markdown analysis;
- spreadsheet/data output;
- code/test;
- architecture/schema;
- dashboard screenshot/link;
- policy comparison with sources;
- experiment record;
- decision memo.

Không dùng “đã đọc”, “đã xem video”, “đã hiểu” làm artifact.

## 9. External verification & freshness

External verification bắt buộc với claim có thể thay đổi theo thời gian, đặc biệt:

- platform policy/rules;
- creator/seller eligibility;
- commission/attribution window;
- payment/settlement behavior;
- API availability/limits;
- legal/tax requirement;
- privacy/compliance regulation;
- pricing/fees/current product behavior;
- AI/AIGC policy;
- search/discovery platform behavior khi lesson phụ thuộc vào current implementation.

Nguồn ưu tiên:

1. government / official legal text;
2. official platform/vendor/help/policy docs;
3. primary standards/specifications;
4. regulator guidance;
5. reputable industry research;
6. secondary source khi primary không đủ.

### Volatility cadence

Theo [`FRESHNESS-POLICY.md`](FRESHNESS-POLICY.md):

- HIGH: re-check trước authoring và tối đa 30 ngày;
- MEDIUM: tối đa 90 ngày;
- LOW: tối đa 12 tháng hoặc khi có evidence thay đổi.

Current source register: [`AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md`](AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md).

### Current-state override

Nếu canonical title giữ thuật ngữ lịch sử nhưng platform đã đổi tên/logic, **không tự ý renumber/rename syllabus**. Dùng:

```markdown
> **Current-state override — verified YYYY-MM-DD**
> Canonical syllabus giữ X để bảo toàn provenance.
> Current operating truth là Y.
```

Ví dụ hiện tại: `14.2 — Promotion Quality Points` giữ canonical title, nhưng TikTok Shop dùng **Promotion Performance Score (PPS)** làm active score từ 2026-08-27.

Trong lesson phải phân biệt:

- canonical curriculum concept;
- current verified fact;
- author inference/example.

## 10. Authoring status Definition of Done

### `planned`

- metadata cơ bản có thể tồn tại;
- placeholder được phép;
- không được xem là lesson học chính thức.

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
- thuật ngữ chuyên ngành beginner-facing có learner aid song ngữ khi phù hợp;
- đủ Concept/Example/Quiz/Practice/Explain-back;
- answer key/rubric đầy đủ;
- artifact path rõ;
- current claims đã verify theo freshness policy;
- không còn placeholder/TODO;
- links nội bộ hợp lý.

## 11. Reference implementation — bài 0.1

Bài `0.1 — Affiliate Expert là gì?` là reference implementation `ready`:

- YAML metadata đầy đủ;
- heading hierarchy chuẩn;
- canonical/source mapping rõ;
- effort estimate;
- beginner-facing terminology theo chuẩn song ngữ;
- objectives, concept, explanations, case A/B;
- exercise, quiz 10 câu, answer key;
- explain-back, PASS, Knowledge Base update;
- không có current platform/legal fact cần external verification.

Template là **minimum contract**, không phải giới hạn chiều sâu.

## 12. Authoring workflow

```text
1. Read canonical lesson in S
2. Read SOURCE-MAPPING row
3. Resolve prerequisites + execution context
4. Assign S/M/L + estimated minutes
5. Identify volatility/current-fact needs
6. Author concept/example/case
7. Add bilingual learner aids for specialized terms
8. Design artifact
9. Design quiz + answer key/rubric
10. Verify current facts + register external refs
11. Design explain-back
12. Check 5 PASS coverage
13. Run Curriculum CI
14. Set status=ready only when DoD passes
```

## 13. Anti-patterns

Không:

- tạo hàng trăm file placeholder rồi coi curriculum đã authored;
- dùng `LESSON-NOTES.md` làm lesson authoring template;
- để quiz không có answer key/rubric;
- gắn source supplement không thực sự hỗ trợ lesson;
- đưa policy/legal facts cũ mà không verification;
- hard-code current platform thresholds như sự thật vĩnh viễn;
- dùng SEO/affiliate aggregator làm nguồn duy nhất cho current policy/legal claim;
- ép mọi lesson có độ dài như nhau;
- để beginner-facing lesson dùng dày đặc specialized English terms mà không có learner aid/glossary;
- tick roadmap vì lesson file tồn tại;
- nhầm `status: ready` với learner PASS.
