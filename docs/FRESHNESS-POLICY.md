# Freshness Policy

> Mục tiêu: giữ curriculum ổn định về cấu trúc nhưng không để các dữ kiện platform, legal, tax, privacy, API, pricing và AI behavior trở nên lỗi thời.

**Policy version:** 2026-08-28  
**Applies to:** lesson authoring, source mapping, policy watch, legal/tax watch, platform docs, API/tool behavior và current-market examples.

## 1. Tách canonical knowledge và current facts

Repo có hai lớp tri thức độc lập:

```text
CANONICAL CURRICULUM
= Part / Chapter / Lesson / Project / LAB / PASS Gate từ SYLLABUS v2026.08

CURRENT KNOWLEDGE OVERLAY
= platform policy / law / tax / privacy / API / AI / search / creator-commerce facts được external-verify
```

Web research không tự động sửa canonical syllabus.

Nếu một thuật ngữ trong syllabus đã lỗi thời nhưng lesson ID/title vẫn là canonical provenance, giữ ID/title và thêm **current-state override** trong lesson/roadmap note.

Ví dụ:

```text
14.2 — Promotion Quality Points (canonical title)
Current state 2026-08-27+: TikTok Shop dùng Promotion Performance Score (PPS)
```

## 2. Volatility classes

### HIGH — review trước khi author và tối đa mỗi 30 ngày

- platform policy, eligibility, commission, attribution window;
- seller/creator program terms;
- legal/tax/privacy/advertising requirements;
- API availability/limits;
- AI-generated content rules;
- payment/settlement/current fee behavior.

### MEDIUM — review tối đa mỗi 90 ngày

- search/discovery behavior;
- creator-commerce measurement conventions;
- browser/privacy measurement ecosystem;
- LLM/agent/tooling capabilities;
- vendor product behavior ảnh hưởng exercise.

### LOW — review tối đa mỗi 12 tháng hoặc khi có evidence thay đổi

- business fundamentals;
- unit economics formulas;
- statistical concepts;
- software architecture principles;
- generic experimentation concepts.

## 3. External source priority

Ưu tiên:

1. government / official legal text;
2. official platform/vendor/help/policy docs;
3. primary standards/specifications;
4. regulator guidance;
5. reputable industry research;
6. secondary source chỉ khi primary source không đủ.

Không dùng blog SEO/affiliate aggregator làm nguồn duy nhất cho current policy/legal claim.

## 4. Lesson metadata contract

Khi lesson có current facts:

```yaml
source_refs:
  external:
    - "EXT:TIKTOK:PPS"
    - "EXT:VN:PDPL-2025"
last_verified: "2026-08-28"
```

Quy tắc:

- `external` không rỗng → `last_verified` phải là `YYYY-MM-DD`;
- `last_verified` có ngày → phải có ít nhất một external ref;
- external ref phải resolve được trong current external-source register hoặc được ghi rõ URL/nguồn trong lesson;
- current claim phải phân biệt với author inference/example.

## 5. Source register

Current external sources được ghi trong:

- [`AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md`](AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)

Mỗi source entry nên có:

- stable ID;
- source owner;
- title/topic;
- URL;
- verified date;
- volatility class;
- curriculum mapping;
- factual implication.

## 6. Staleness rule khi author lesson

Trước khi chuyển lesson sang `ready`:

1. xác định lesson có current claims không;
2. nếu có, kiểm tra external source có còn hoạt động và nội dung có còn áp dụng;
3. nếu source thuộc HIGH và `last_verified` >30 ngày, re-check;
4. nếu MEDIUM và >90 ngày, re-check;
5. cập nhật source/ref/date;
6. không copy một con số/current policy sang lesson khác mà không mang theo provenance.

CI kiểm tra **metadata contract**, nhưng không thể tự xác minh nội dung pháp lý/platform còn đúng. Human review vẫn bắt buộc.

## 7. Current-state override pattern

Khi canonical title cũ nhưng khái niệm hiện hành đổi:

```markdown
> **Current-state override — verified YYYY-MM-DD**
> Canonical syllabus dùng thuật ngữ X để giữ provenance.
> Hiện tại platform/regulation dùng Y.
> Lesson phải dạy Y là operating truth và X là migration/history context.
```

Không đổi lesson ID chỉ vì rename platform terminology.

## 8. Legal/tax disclaimer

Phần legal/tax/privacy trong repo là **educational research**.

Không trình bày như tư vấn pháp lý, kế toán hoặc thuế cho một tình huống cá nhân cụ thể. Khi quyết định thực tế có rủi ro đáng kể, learner phải kiểm tra văn bản hiện hành và/hoặc chuyên gia phù hợp.

## 9. Continuous watch loops

Part 22 formalizes maintenance:

- Chương 85 — Platform Watch: HIGH volatility;
- Chương 86 — Legal & Tax Watch: HIGH volatility;
- Chương 87 — Technology Watch: MEDIUM volatility;
- Chương 88 — Research Practice: biến thay đổi thành hypothesis → evidence → system update.

Freshness không phải một lần update; nó là operating loop của Affiliate Intelligence System.
