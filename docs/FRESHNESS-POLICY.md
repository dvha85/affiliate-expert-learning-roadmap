# Freshness Policy

> Mục tiêu: giữ curriculum ổn định về cấu trúc nhưng không để các dữ kiện platform, legal, tax, privacy, API, pricing, Go/runtime và AI/agent behavior trở nên lỗi thời.

**Policy version:** 2026-08-28  
**Applies to:** lesson authoring, source mapping, policy/legal/tax watch, platform docs, API/tool behavior, Go/runtime/SDK/protocol facts và current-market examples.

## 1. Tách canonical knowledge và current facts

Repo có hai lớp tri thức độc lập:

```text
CANONICAL CURRICULUM
= validated normalized roadmap inventory
+ active SYLLABUS-v2026.09 explicit overrides
+ inherited/historical evidence from SYLLABUS-v2026.08

CURRENT KNOWLEDGE OVERLAY
= platform policy / law / tax / privacy / API / software / AI / search / creator-commerce facts được external-verify
```

Đọc [`../sources/CURRICULUM-INDEX-v2026.09.md`](../sources/CURRICULUM-INDEX-v2026.09.md) để hiểu provenance `source_explicit / normalized_from_chapter / normalized_then_overridden`.

Web research không tự động sửa canonical curriculum. Nếu current fact đổi nhưng không cần thay lesson structure, cập nhật current-state override/source register thay vì âm thầm rewrite historical source.

## 2. Volatility classes

### HIGH — review trước khi author và tối đa mỗi 30 ngày

- platform policy, eligibility, commission, attribution window;
- seller/creator program terms;
- legal/tax/privacy/advertising requirements;
- API availability/limits khi ảnh hưởng production;
- AI-generated content rules;
- payment/settlement/current fee behavior;
- security-sensitive agent/tool protocol changes khi ảnh hưởng control boundary.

### MEDIUM — review tối đa mỗi 90 ngày

- search/discovery behavior;
- creator-commerce measurement conventions;
- browser/privacy measurement ecosystem;
- Go/runtime/SDK/library status;
- LLM/agent/tooling capabilities;
- MCP/A2A/workflow/observability capabilities;
- vendor product behavior ảnh hưởng exercise.

### LOW — review tối đa mỗi 12 tháng hoặc khi có evidence thay đổi

- business fundamentals;
- unit economics formulas;
- statistical concepts;
- software architecture principles;
- generic experimentation/reliability/security concepts.

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
    - "EXT:MCP:SDK"
last_verified: "2026-08-28"
```

Quy tắc:

- `external` không rỗng → `last_verified` phải là `YYYY-MM-DD`;
- `last_verified` có ngày → phải có ít nhất một external ref;
- external ref phải resolve được trong current external-source register hoặc được ghi rõ URL/nguồn trong lesson;
- current claim phải phân biệt với author inference/example.

## 5. Source registers

Current external sources hiện được quản lý tối thiểu tại:

- [`AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md`](AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)
- [`BOT-ENGINEERING-REFRESH-2026.08.md`](BOT-ENGINEERING-REFRESH-2026.08.md)

Mỗi source entry nên có:

- stable ID;
- source owner;
- title/topic;
- URL;
- verified date;
- volatility class;
- curriculum mapping;
- factual implication.

Future source registers có thể được thêm theo domain, nhưng stable external IDs không được reuse cho nguồn khác nghĩa.

## 6. Staleness rule khi author lesson

Trước khi chuyển lesson sang `ready`:

1. resolve canonical lesson/provenance;
2. xác định lesson có current claims không;
3. nếu có, kiểm tra external source có còn hoạt động và nội dung còn áp dụng;
4. HIGH >30 ngày → re-check;
5. MEDIUM >90 ngày → re-check;
6. cập nhật ref/date;
7. không copy current policy/version/threshold sang lesson khác mà không mang theo provenance.

CI kiểm metadata contract và source-ID resolution, nhưng không thể tự xác minh nội dung pháp lý/platform còn đúng. Human research vẫn bắt buộc.

## 7. Current-state override pattern

Khi canonical terminology cũ nhưng operating truth thay đổi:

```markdown
> **Current-state override — verified YYYY-MM-DD**
> Historical/canonical context dùng X.
> Current operating truth là Y.
> Lesson dạy Y để vận hành và X để hiểu migration/provenance.
```

Không đổi lesson ID chỉ vì platform rename nếu scope curriculum vẫn giữ nguyên.

## 8. Engineering freshness pattern

Không hard-code version hiện hành vào lesson title nếu concept bền hơn version.

Ví dụ:

```text
canonical lesson:
Go runtime, modules và project structure

freshness layer:
current supported Go release / current MCP SDK / current workflow reference
```

Framework/protocol update thường sửa examples + source register trước; chỉ đổi canonical structure khi có curriculum-level decision rõ ràng.

## 9. Legal/tax disclaimer

Phần legal/tax/privacy trong repo là educational research, không phải tư vấn pháp lý/kế toán/thuế cho tình huống cá nhân cụ thể. Khi quyết định thực tế có rủi ro đáng kể, phải kiểm tra văn bản hiện hành và/hoặc chuyên gia phù hợp.

## 10. Continuous watch loops

Part 22 formalizes maintenance:

- Chương 85 — Platform Watch: HIGH;
- Chương 86 — Legal & Tax Watch: HIGH;
- Chương 87 — Technology Watch: MEDIUM/HIGH tùy topic;
- Chương 88 — Research Practice: hypothesis → evidence → system update.

Freshness không phải một lần update; nó là operating loop của Affiliate Intelligence System.