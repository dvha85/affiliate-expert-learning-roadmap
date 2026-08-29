# Freshness Policy

> Mục tiêu: giữ outcome và safety boundary của chương trình ổn định, đồng thời không để dữ kiện platform, pháp lý, thuế, privacy, API, pricing, Go/runtime và AI/agent trở nên lỗi thời.

**Policy version:** 2026-08-29
**Applies to:** `CURRICULUM.md`, roadmap, Mission, lesson, source mapping, policy/legal/tax watch, platform docs, API/tool behavior, Go/runtime/SDK/protocol facts và current-market examples.

## 1. Authority và current facts là hai lớp khác nhau

```text
ACTIVE CURRICULUM AUTHORITY
= CURRICULUM.md
+ ROADMAP.md và roadmap/part-00.md ... part-06.md làm normalized index
+ Mission/lesson files làm execution detail

CURRENT KNOWLEDGE OVERLAY
= platform policy / law / tax / privacy / API / software / AI / search / creator-commerce facts được external-verify

HISTORICAL INPUT
= sources/ và các revision cũ, chỉ dùng cho provenance/research
```

[`../CURRICULUM.md`](../CURRICULUM.md) quyết định mục tiêu, cấu trúc Core hiện tại, Mission spine `M00–M11`, Real Evidence Ladder và PASS boundary. File trong `sources/`, kể cả `SYLLABUS-v2026.09.md`, không còn là active authority và không được dùng để khôi phục cấu trúc legacy.

Web research không tự động sửa curriculum. Khi current fact đổi mà outcome/learning sequence vẫn đúng, cập nhật source register, reference card hoặc implementation note. Chỉ thay Core/Mission khi learner evidence hoặc operating risk cho thấy curriculum-level decision cần đổi.

## 2. Volatility classes

### HIGH — kiểm tra trước khi dùng và tối đa mỗi 30 ngày

- platform policy, eligibility, commission, attribution window;
- seller/creator program terms;
- legal/tax/privacy/advertising requirements;
- API availability/limits khi ảnh hưởng production;
- AI-generated content rules;
- payment/settlement/current fee behavior;
- security-sensitive agent/tool protocol changes khi ảnh hưởng control boundary.

### MEDIUM — kiểm tra tối đa mỗi 90 ngày

- search/discovery behavior;
- creator-commerce measurement conventions;
- browser/privacy measurement ecosystem;
- Go/runtime/SDK/library status;
- LLM/agent/tooling capabilities;
- MCP/A2A/workflow/observability capabilities;
- vendor behavior ảnh hưởng exercise.

### LOW — kiểm tra tối đa mỗi 12 tháng hoặc khi có evidence thay đổi

- business fundamentals;
- unit economics formulas;
- statistical concepts;
- software architecture principles;
- generic experimentation/reliability/security concepts.

Thời hạn là thời điểm phải re-check, không phải cam kết nguồn vẫn đúng tới ngày đó. Trước consequential action luôn revalidate dữ kiện HIGH liên quan.

## 3. External source priority

Ưu tiên:

1. government / official legal text;
2. official platform/vendor/help/policy docs;
3. primary standards/specifications;
4. regulator guidance;
5. reputable industry research;
6. secondary source chỉ khi primary source không đủ.

Không dùng blog SEO/affiliate aggregator làm nguồn duy nhất cho current policy/legal claim.

## 4. Lesson và Mission metadata contract

Khi artifact dạy hoặc dùng current fact:

```yaml
source_refs:
  external:
    - "EXT:TIKTOK:PPS"
last_verified: "2026-08-29"
```

Quy tắc:

- `external` không rỗng thì `last_verified` phải là `YYYY-MM-DD`;
- có `last_verified` thì phải có ít nhất một external ref;
- external ref phải resolve trong current source register hoặc có URL/nguồn rõ tại chỗ;
- current claim phải tách khỏi author inference, estimate và example;
- evidence learner thu được cần `source_url`/source ref, `observed_at`, access method, claim kind, confidence/limitation khi relevant;
- sample/synthetic data phải mang nhãn E0 và không được thỏa Reality verified yêu cầu E1+.

Active lesson dùng `source_refs.active: ["CUR:..."]`. `S:`/`T:`/`R:` chỉ được đặt trong historical/training/research lineage khi thực sự dùng; chúng không bao giờ thay active identity từ `CURRICULUM.md` và roadmap.

## 5. Source registers

Current external sources được quản lý tối thiểu tại:

- [`AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md`](AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)
- [`BOT-ENGINEERING-REFRESH-2026.08.md`](BOT-ENGINEERING-REFRESH-2026.08.md)

Mỗi source entry nên có:

- stable ID;
- source owner;
- title/topic và URL;
- verified date;
- volatility class;
- Core/Mission/Advanced/Reference mapping hiện hành;
- factual implication và giới hạn áp dụng.

Stable external ID không được reuse cho nguồn khác nghĩa. Khi thay nguồn, giữ compatibility alias hoặc migration note rõ.

## 6. Freshness gate trước khi author hoặc operate

Trước khi chuyển lesson/Mission sang `ready`, hoặc trước khi dùng current fact trong một run thật:

1. resolve scope từ [`../CURRICULUM.md`](../CURRICULUM.md) và Mission hiện tại;
2. xác định claim nào volatile và claim nào là learner observation;
3. kiểm tra nguồn còn hoạt động và còn áp dụng cho đúng quốc gia/account/context;
4. HIGH quá 30 ngày hoặc MEDIUM quá 90 ngày thì re-check;
5. cập nhật ref/date và lưu changed meaning nếu có;
6. test happy path lẫn stale/missing/conflicting path;
7. không copy policy/version/threshold sang nơi khác mà bỏ provenance;
8. trước publish, spend, account change hoặc external execution, revalidate policy và evidence liên quan.

CI kiểm contract, link và source-ID resolution. CI không thể xác nhận một quy định pháp lý hay platform rule vẫn đúng; human research vẫn bắt buộc.

## 7. Current-state override pattern

Khi historical terminology khác operating truth:

```markdown
> **Current-state note — verified YYYY-MM-DD**
> Historical source dùng X để giải thích provenance.
> Operating truth hiện tại là Y trong context Z.
> Mission áp dụng Y; nếu context khác phải re-check.
```

Không đổi lesson ID chỉ vì platform rename nếu learning outcome vẫn giữ nguyên. Ngược lại, không giữ một lesson chỉ để bảo toàn ID khi learner evidence cho thấy lesson thừa hoặc đặt sai thời điểm.

## 8. Engineering freshness pattern

Không hard-code current version vào Core lesson title nếu concept bền hơn version.

```text
Core micro-lesson:
runtime, cancellation, schema validation hoặc tool permission cần để ship Mission

Reference/freshness layer:
current supported Go release, provider SDK, MCP spec hoặc workflow product
```

Framework/protocol update thường sửa example, adapter và source register. Nó chỉ làm đổi Core khi behavior/risk thực sự thay learning outcome hoặc PASS gate.

## 9. Real Evidence Ladder và freshness

Freshness là một phần của Reality verified:

- E1 public observation phải có URL/source và `observed_at`;
- E2 manual publish phải lưu disclosure/policy check tại thời điểm publish;
- E3 analytics/export phải giữ observation window và phân biệt missing với zero;
- E4+ phải nối Decision → Action → Outcome bằng evidence chưa hết hạn cho quyết định đó;
- E5/E6 phải revalidate policy, approval và action target ngay trước execute.

Kết quả `zero`, `negative` hoặc `inconclusive` vẫn hợp lệ. Dữ liệu stale hoặc không rõ nguồn không được nâng thành business truth bằng model confidence.

## 10. Legal/tax disclaimer

Phần legal/tax/privacy trong repo là educational research, không phải tư vấn pháp lý, kế toán hay thuế cho tình huống cá nhân. Trước quyết định có rủi ro đáng kể, phải kiểm tra văn bản hiện hành và/hoặc chuyên gia phù hợp.

## 11. Continuous watch loop

Freshness là operating loop xuyên suốt bốn Milestone Gate, không phải một Part học một lần:

```text
Observe source or policy change
→ record provenance and verified_at
→ assess affected Mission/decision/action
→ update reference/adapter/test
→ run regression and safety checks
→ review before release
```

M11 phải chứng minh production observation, recovery và outcome review. Platform/legal/technology watch tiếp tục sau Core như Reference operating practice; chúng không tạo thêm checkbox chỉ để tăng inventory.
