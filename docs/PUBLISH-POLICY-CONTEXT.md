# Publish Policy Context — Ngữ cảnh policy trước publish

Tài liệu này định nghĩa contract tối thiểu để M03+ kiểm một public content artifact trước khi human publish hoặc trước khi một Mission sau cân nhắc external execution. Nó không thay legal advice và không biến platform policy thành permanent Core truth.

## 1. Mục tiêu

Một artifact không được coi là publish-ready chỉ vì:

```text
claim có evidence
+ link hoạt động
```

Publish readiness còn phụ thuộc vào current platform/legal context, content origin, product fidelity, rights/originality và disclosure.

Mental model:

```text
Content artifact
+ evidence-supported claims
+ PolicyContext
+ human review
→ READY_FOR_HUMAN | BLOCKED | HUMAN_REVIEW
```

## 2. Logical shape

```yaml
policy_context_id:
platform:
channel_scope:
jurisdiction_scope:

policy_source:
policy_scope:
policy_verified_at:
review_result: current | stale | unknown

content_origin:
  human | ai_assisted | ai_generated | reused | mixed

ai_disclosure_status:
  required_present | not_required | unknown

product_fidelity_status:
  supported | needs_review | failed | not_applicable

originality_status:
  original | transformed | reused_authorized | unknown

asset_rights_status:
  owned | licensed | authorized | not_applicable | unknown
reuse_authorization_ref:

affiliate_disclosure_required:
affiliate_disclosure_text:
affiliate_disclosure_placement:

limitations: []
```

Không phải platform/jurisdiction nào cũng cần mọi field. `unknown` tốt hơn invent rule.

## 3. Content origin không phải quality score

```text
AI-generated
≠ automatically bad

Human-written
≠ automatically compliant

Reused public asset
≠ automatically permitted
```

`content_origin` chỉ ghi provenance. Quality/compliance phải review riêng.

## 4. Product fidelity

AI/editing không được làm claim hoặc hình ảnh sản phẩm mạnh hơn evidence.

Các failure class cần chặn hoặc đưa về human review:

- thêm feature/benefit không tồn tại trong evidence;
- thay đổi màu/chất liệu/kích thước/fit theo cách gây hiểu sai;
- tạo fake before/after/result;
- synthetic testimonial/review được trình bày như trải nghiệm thật;
- AI-generated scene khiến người xem tưởng Product đã được dùng/test theo cách chưa xảy ra.

Invariant:

```text
AI rendering quality
≠ product truth
```

## 5. Originality và rights

Nếu artifact reuse nội dung/asset của người khác, phải giữ rights/authorization evidence khi applicable.

```text
asset is public
≠ permission to repost/commercially reuse
```

Nếu permission/originality state không rõ và platform/policy yêu cầu, publish readiness phải `BLOCKED` hoặc `HUMAN_REVIEW`.

## 6. Jurisdiction-aware compliance

Platform cho phép publish không chứng minh mọi nghĩa vụ pháp lý đã thỏa.

```text
platform policy passed
≠ universal legal compliance
```

`jurisdiction_scope` cần được khai báo khi content/audience/action có legal relevance. Nếu current legal requirement không chắc hoặc source stale:

```text
unknown/stale consequential requirement
→ BLOCKED / HUMAN_REVIEW
```

Không copy một disclosure/AI-label rule của EU/US sang Việt Nam hoặc ngược lại nếu chưa xác định applicability.

## 7. Disclosure separation

Affiliate disclosure và AI-content disclosure là hai câu hỏi khác nhau.

```text
affiliate relationship disclosure
≠ AI-generated-content disclosure
```

Có thể cần một, cả hai hoặc không cái nào tùy context. Mỗi quyết định phải trace được về source/scope/current verification.

## 8. Tracking và privacy boundary

Tracking link/UTM không được nhét personal data chỉ vì field kỹ thuật cho phép.

```text
tracking identity
→ content/campaign/action identity
```

không phải:

```text
tracking identity
→ raw customer email / phone / unrelated personal data
```

Data governance chi tiết thuộc tool/privacy contract ở Mission sau; M03 tối thiểu phải reject obvious PII leakage trong public URL/content/log.

## 9. M03 blocking matrix

| Case | Expected |
|---|---|
| unsupported product claim | `BLOCKED` |
| AI invents product feature/result | `BLOCKED` |
| required disclosure missing | `BLOCKED` |
| required AI label unknown/missing | `BLOCKED` hoặc `HUMAN_REVIEW` theo current source |
| reused asset + rights unknown | `BLOCKED`/`HUMAN_REVIEW` |
| policy source stale/unknown | `BLOCKED` |
| jurisdiction applicability unresolved for material requirement | `HUMAN_REVIEW`/`BLOCKED` |
| tracking URL leaks PII/secret | `BLOCKED` |
| platform-derived score looks good but claims unsupported | `BLOCKED`; score không override evidence |

## 10. Authority invariant

M03 vẫn giữ:

```text
Bot/AI
→ analyze / validate / recommend readiness

Human
→ exact-artifact review
→ manual publish
```

PolicyContext không cấp publish authority cho Agent/n8n/Bot.

## 11. Current-fact integration

Current platform/legal facts phải resolve qua [`FRESHNESS-POLICY.md`](FRESHNESS-POLICY.md) và current source register như [`AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md`](AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md).

Contract này giữ semantics bền:

```text
source + scope + verified_at
+ origin/fidelity/rights/disclosure/jurisdiction
→ reviewable publish context
```

Tên policy, threshold, UI field hoặc platform score có thể đổi mà không cần đổi Core lesson ID.
