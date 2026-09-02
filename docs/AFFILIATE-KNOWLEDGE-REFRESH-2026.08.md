# Affiliate Knowledge Refresh — 2026.08

> Current-knowledge reference cho [`CURRICULUM.md`](../CURRICULUM.md). Hai syllabus trong `sources/` chỉ là historical provenance; mapping cũ không còn quyết định Part/Chapter/Lesson hiện hành.

**Verified:** 2026-09-02  
**Scope:** Việt Nam + global affiliate/creator commerce, tracking/attribution, search, AI commerce, legal/privacy/tax/compliance.  
**Policy:** xem [`FRESHNESS-POLICY.md`](FRESHNESS-POLICY.md).

## 1. Executive update map

| Khu vực | 2026 operating update | Curriculum mapping | Curriculum action | Volatility |
|---|---|---|---|---|
| TikTok creator quality | PQP → **Promotion Performance Score (PPS)** từ 2026-08-27 | C6–C8; C12–C13 khi dùng làm platform/account signal | reference_update | HIGH |
| TikTok AIGC | AIGC được phép nhưng phải trung thực, không fake product/results/story; disclosure/label theo policy hiện hành | C5–C6, C8, C16 | mission_or_lesson_change | HIGH |
| TikTok originality | Nội dung không nguyên bản/repost thiếu đóng góp hoặc permission có thể vi phạm; có Content Authorization Tool | C6, C8, C16 | mission_or_lesson_change | HIGH |
| TikTok content posting limit | Content Posting Limit có thể ẩn product link sau vi phạm lặp lại | C6/C12 Reference | watch_only | HIGH |
| TikTok creator eligibility | Vietnam creator application currently includes ≥1,000 followers, age ≥18, compliance/identity conditions | C6 Reference | reference_update | HIGH |
| Google Analytics attribution | EVC window tùy chỉnh 1–30 ngày; CTC 1–90 ngày | C7–C10 | contract_hardening | HIGH |
| Google Analytics imports | Có campaign data import validation report để phát hiện campaign thiếu cost/click/impression | C7–C9 | contract_hardening | MEDIUM/HIGH |
| Google Search AI | Search Console có controls/insights cho generative-AI Search và rollout toàn cầu được xác nhận 2026-08-31 | C6–C8 Reference | reference_update | MEDIUM |
| Google site reputation | Enforcement cập nhật từ 2026-08-30; third-party content dùng reputation của host vẫn là policy risk | C6, C16, C19 Reference | reference_update | MEDIUM/HIGH |
| Vietnam e-commerce | Luật TMĐT 122/2025/QH15 + NĐ 248/2026/NĐ-CP hiệu lực 2026-07-01 | C6, C16, C19 | reference_update | HIGH |
| Vietnam privacy | Luật 91/2025/QH15 + NĐ 356/2025/NĐ-CP; hướng dẫn 2026-08-13 làm rõ nhiều hoạt động kinh doanh là xử lý dữ liệu cá nhân | C3, C15–C16, C19 | contract_hardening | HIGH |
| Vietnam advertising | Luật 75/2025/QH15 hiệu lực 2026-01-01; NĐ 342/2025/NĐ-CP hiệu lực 2026-02-15 | C6, C16, C19 | reference_update | HIGH |
| Vietnam tax | NĐ 68/2026/NĐ-CP + NĐ 141/2026/NĐ-CP; một số platform thuộc scope có nghĩa vụ khấu trừ/kê khai/nộp thay | revenue Reference | contract_hardening | HIGH |
| EU AI transparency | Article 50 transparency obligations áp dụng từ 2026-08-02 trong phạm vi luật điều chỉnh | C6, C16, C19 Reference | mission_or_lesson_change | HIGH |
| YouTube commerce | YouTube Shopping Affiliate liệt kê Việt Nam; Amazon integration mới công bố cho eligible U.S. creators | C6–C8 Reference | watch_only | HIGH |
| Shopee Affiliate | Chưa xác nhận material rule/attribution/commission change tháng 8 từ primary source đủ mạnh để đổi Core | platform Reference | watch_only | HIGH |
| Agentic commerce | Google UCP và industry direction cho thấy discovery/checkout dần có agentic layer | C13–C17; Advanced A09 | watch_only | MEDIUM |
| Disclosure/reviews | FTC guidance tiếp tục yêu cầu disclosure rõ, dễ thấy cho material connection | C6, C16, C19 | reference_update | MEDIUM/HIGH |

`Curriculum action` dùng bốn giá trị chuẩn:

```text
reference_update
contract_hardening
mission_or_lesson_change
watch_only
```

Current fact không tự tạo Core checkbox. Chỉ `contract_hardening` hoặc `mission_or_lesson_change` mới được xem xét sửa learner-facing acceptance criteria, và vẫn phải giữ Mission outcome/authority boundary.

## 2. TikTok Shop Vietnam — current-state overrides

### EXT:TIKTOK:PPS

- **Source:** TikTok Shop Academy — Promotion Performance Score / Latest Policies Updates
- **URL:** https://seller-vn.tiktok.com/university/course?content_id=4242906912278289&lang=en&learning_id=1534569199585041
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C6–C8; C12–C13 khi dùng làm platform/account signal; platform Reference
- **Curriculum action:** reference_update

Current operating fact:

- TikTok states **PPS replaces PQP as the active score from 2026-08-27**.
- PPS là score 0–5 dựa đều trên Product Selection và Content Quality/policy compliance theo published description.
- TikTok recommends aiming for **4.5+**; below **3.0** may affect content visibility.

Boundary bắt buộc:

```text
PPS observed
≠ Product Quality fact
≠ Content Quality ground truth
≠ Affiliate Intelligence Bot score
≠ cross-platform comparable metric
```

**Curriculum decision:** không map PPS thành M00 Product truth và không thêm field bắt buộc vào M00 schema. Nếu learner dùng TikTok ở M03+, PPS chỉ là platform-derived observation có source, `observed_at`, scope/account context và limitation.

### EXT:TIKTOK:AIGC

- **Source:** TikTok Shop Academy — AI-Generated Content (AIGC)
- **URL:** https://seller-vn.tiktok.com/university/essay?knowledge_id=6832782790018833&lang=en
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C5–C6, C8, C16; AI/compliance Reference
- **Curriculum action:** mission_or_lesson_change

Current operating fact:

- AIGC được phép nếu tuân TikTok Shop Content Policy và Community Guidelines.
- AI-generated product visuals phải giữ product fidelity; không thêm feature không tồn tại.
- Không dùng AI/filter/edit để tạo fake results hoặc misleading before/after effect.
- Disclosure/label phải theo current platform guidance khi applicable.

**Curriculum implication:** AI-assisted content phải được đánh giá theo **truthfulness + product fidelity + provenance + disclosure + policy safety**, không chỉ generation quality.

### EXT:TIKTOK:UNORIGINAL-CONTENT

- **Source:** TikTok Shop Academy — Unoriginal Content
- **URL:** https://seller-vn.tiktok.com/university/essay?knowledge_id=6837791128880898&lang=en
- **Published:** 2026-08-24
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C6, C8, C16; content/compliance Reference
- **Curriculum action:** mission_or_lesson_change

TikTok Shop Vietnam prohibits unoriginal content in shoppable videos/LIVE, including examples such as reuse without meaningful contribution, direct mirroring, or merging others' content without permission.

**Curriculum implication:** `content_origin`, originality/contribution và rights/authorization state cần xuất hiện trong M03 compliance artifact khi relevant.

### EXT:TIKTOK:CONTENT-AUTHORIZATION

- **Source:** TikTok Shop Academy — Content Authorization Tool guidance
- **URL:** https://seller-vn.tiktok.com/university/essay?identity=1&knowledge_id=5667844449044231&role=1
- **Published:** 2026-08-20
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C6, C16; content-rights Reference
- **Curriculum action:** reference_update

TikTok provides a tool for requesting/granting authorization to repost another creator's TikTok Shop content. Authorization state là evidence riêng; không suy permission chỉ vì asset public.

### EXT:TIKTOK:CONTENT-POSTING-LIMIT

- **Source:** TikTok Shop Academy — TikTok Shop Content Posting Limit
- **URL:** https://seller-vn.tiktok.com/university/essay?knowledge_id=5393782430680848&lang=en
- **Published:** 2026-08-24
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C6/C12 platform Reference
- **Curriculum action:** watch_only

Content Posting Limit có thể giới hạn shoppable posting sau repeated low-quality/non-interactive/misleading/repetitive behavior; product links có thể bị hidden sau khi limit reached. Đây là current platform operational fact, chưa phải lý do tạo Core lesson hoặc Bot optimization target.

### EXT:TIKTOK:CREATOR-ELIGIBILITY-VN

- **Source:** TikTok Shop Academy — How to Become a TikTok Shop Creator
- **URL:** https://seller-vn.tiktok.com/university/essay?knowledge_id=6837793229817601
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C6; platform Reference
- **Curriculum action:** reference_update

As of verification, published Vietnam requirements include at least **1,000 followers**, age **18+**, identity/compliance conditions and continuing account-health requirements. Re-check before a real learner action.

### EXT:TIKTOK:POLICY-UPDATES

- **Source:** TikTok Shop Academy — Latest Policies Updates
- **URL:** https://seller-vn.tiktok.com/university/course?content_id=4242906912278289&lang=en&learning_id=1534569199585041
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C6, C16; platform freshness Reference
- **Curriculum action:** reference_update

Use this as one official watch source for creator/seller policy migration. It documents the August 2026 PPS rollout and other operational changes.

## 3. Vietnam e-commerce, legal, privacy and tax — 2026 baseline

> Educational research only. Lesson author/operator phải verify exact provision/source áp dụng cho đúng scope; đây không phải legal/tax advice.

### EXT:VN:ECOM-LAW-122-2025

- **Source:** Chính phủ/Công báo — Luật Thương mại điện tử số 122/2025/QH15
- **URL:** https://vanban.chinhphu.vn/?docid=216503&pageid=27160
- **Effective:** 2026-07-01
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C6, C16, C19; legal Reference

### EXT:VN:ECOM-ND248-2026

- **Source:** Chính phủ — Nghị định 248/2026/NĐ-CP
- **URL:** https://vanban.chinhphu.vn/?docid=218747&orggroupid=2&pageid=27160
- **Effective:** 2026-07-01
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C6, C16, C19; legal Reference

### EXT:VN:PDPL-91-2025

- **Source:** Chính phủ/Công báo — Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15
- **URL:** https://vanban.chinhphu.vn/?classid=1&docid=214590&pageid=27160&typegroup=
- **Effective:** 2026-01-01
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C3, C15–C16, C19; privacy Reference

### EXT:VN:PDPL-ND356-2025

- **Source:** Chính phủ — Nghị định 356/2025/NĐ-CP
- **URL:** https://vanban.chinhphu.vn/?classid=1&docid=216387&pageid=27160
- **Effective:** 2026-01-01
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C3, C15–C16, C19; privacy Reference

### EXT:VN:PDPL-BCA-GUIDANCE-2026-08

- **Source:** Bộ Công an — hướng dẫn doanh nghiệp phòng ngừa vi phạm pháp luật về bảo vệ dữ liệu cá nhân
- **URL:** https://bocongan.gov.vn/bai-viet/cong-an-nghe-an-canh-bao-huong-dan-doanh-nghiep-phong-ngua-nguy-co-vi-pham-phap-luat-ve-bao-ve-du-lieu-ca-nhan-trong-hoat-dong-san-xuat-kinh-doanh-1786591676
- **Published:** 2026-08-13
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C15–C16, C19; privacy/data-governance Reference
- **Curriculum action:** contract_hardening

Guidance explains that processing includes a broad set of operations; examples include customer lists, sales software, customer-audience advertising and transferring data to delivery providers. Operating implication for Bot/Agent: **permission to access data is not enough; purpose, minimum necessary data, retention and downstream sharing matter**.

### EXT:VN:AD-LAW-75-2025

- **Source:** Chính phủ — Luật 75/2025/QH15 sửa đổi, bổ sung Luật Quảng cáo
- **URL:** https://vanban.chinhphu.vn/?classid=1&docid=214561&pageid=27160&typegroupid=3ypegroupid%3D3
- **Effective:** 2026-01-01
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C6, C16, C19; legal/compliance Reference

### EXT:VN:AD-ND342-2025

- **Source:** Chính phủ — Nghị định 342/2025/NĐ-CP
- **URL:** https://vanban.chinhphu.vn/?classid=1&docid=216403&orggroupid=2&pageid=27160
- **Effective:** 2026-02-15
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C6, C16, C19; legal/compliance Reference

### EXT:VN:TAX-ND68-2026

- **Source:** Chính phủ — Nghị định 68/2026/NĐ-CP
- **URL:** https://vanban.chinhphu.vn/?classid=1&docid=217111&orggroupid=2&pageid=27160
- **Effective:** 2026-03-05
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** outcome/revenue Reference; not a Core PASS gate

### EXT:VN:TAX-ND141-2026

- **Source:** Chính phủ — Nghị định 141/2026/NĐ-CP sửa đổi Nghị định 68/2026/NĐ-CP
- **URL:** https://vanban.chinhphu.vn/?docid=217960&orggroupid=2&pageid=27160
- **Effective:** 2026-01-01 (the official metadata states this effective date)
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** outcome/revenue Reference; not a Core PASS gate

### EXT:VN:TAX-PLATFORM-WITHHOLDING-GUIDANCE-2026

- **Source:** Cổng TTĐT Chính phủ — Hướng dẫn khai thuế, khấu trừ thuế với hoạt động kinh doanh trên nền tảng thương mại điện tử
- **URL:** https://xaydungchinhsach.chinhphu.vn/huong-dan-khai-thue-khau-tru-thue-voi-hoat-dong-kinh-doanh-tren-nen-tang-thuong-mai-dien-tu-119260309150311529.htm
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** revenue/payment reconciliation Reference
- **Curriculum action:** contract_hardening

The guidance states that platform operators in the defined scope with online ordering and payment functions have withholding/declaration/payment-on-behalf duties under the cited framework. Curriculum must not convert this into one universal Affiliate tax rate. When source exposes it, preserve `tax_withheld`/withholding evidence separately from gross commission and net payout.

**Curriculum implication:** C6/C16/C19 and channel-specific artifacts must not hard-code legal threshold, tax rate, procedure or platform duty from memory. Verify current source, jurisdiction and scope at use time.

## 4. Tracking & attribution in the privacy era

### EXT:GOOGLE:PRIVACY-SANDBOX-2025

- **Source:** Privacy Sandbox — News & Updates
- **URL:** https://privacysandbox.com/news/?by-type=announcements
- **Verified:** 2026-09-02
- **Volatility:** MEDIUM/HIGH
- **Maps to:** C7–C10; Advanced A02
- **Curriculum action:** watch_only

Do not teach a deterministic story that browser/privacy changes follow one fixed cookie-deprecation schedule. The durable model is:

```text
first-party identifiers
+ consent
+ server-side events where justified
+ platform conversion APIs
+ reconciliation
+ privacy-aware aggregate/modeled measurement
+ data ownership
```

### EXT:GOOGLE:GA-CONVERSION-WINDOWS-2026-08

- **Source:** Google Analytics Help — What's new in Google Analytics, 2026-08-11
- **URL:** https://support.google.com/analytics/answer/9164320?hl=en
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C7–C10; measurement Reference
- **Curriculum action:** contract_hardening

Google Analytics now supports custom integer lookback windows:

- engaged-view conversions: **1–30 days**;
- click-through conversions: **1–90 days**.

Operating implication:

```text
metric value without attribution configuration
= incomplete measurement evidence
```

Comparisons must preserve attribution model/window and configuration timestamp/scope when relevant.

### EXT:GOOGLE:GA-CAMPAIGN-IMPORT-VALIDATION-2026-08

- **Source:** Google Analytics Help — What's new in Google Analytics, 2026-08-10
- **URL:** https://support.google.com/analytics/answer/9164320?hl=en
- **Verified:** 2026-09-02
- **Volatility:** MEDIUM/HIGH
- **Maps to:** C7–C9; analytics import Reference
- **Curriculum action:** contract_hardening

Campaign data import validation report helps identify imported/non-Google campaign records lacking useful data such as cost, clicks or impressions. Import success does not imply measurement completeness.

## 5. Search/discovery is generative and multimodal

### EXT:GOOGLE:GENAI-SEARCH-GUIDE

- **Source:** Google Search Central — Optimizing for generative AI features
- **URL:** https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- **Verified:** 2026-09-02
- **Volatility:** MEDIUM
- **Maps to:** C6–C8; channel Reference
- **Curriculum action:** reference_update

Core SEO best practices remain relevant for AI Overviews/AI Mode. Do not teach “AEO/GEO” as a magical replacement for SEO; emphasize useful original content, machine-readable/product information, page experience, multimedia, source quality and measurable visibility.

### EXT:GOOGLE:GENAI-SEARCH-CONSOLE

- **Source:** Google — New opportunities, control and insights for website owners
- **URL:** https://blog.google/products-and-platforms/products/search/new-controls-website-owners/
- **Updated:** 2026-08-31
- **Verified:** 2026-09-02
- **Volatility:** MEDIUM
- **Maps to:** C6–C8; channel analytics Reference
- **Curriculum action:** reference_update

Google states that website-owner controls and Search Console insights for generative-AI Search features have rolled out globally as of 2026-08-31. Insights include impressions and page/country information. Treat generative-AI visibility as a measurable source-specific signal; do not mechanically merge it with traditional organic metrics when scope differs.

### EXT:GOOGLE:SITE-REPUTATION-2026-08

- **Source:** Google Search Central — Update to the Site Reputation Policy
- **URL:** https://developers.google.com/search/blog/2026/08/update-site-reputation-policy
- **Published:** 2026-08-28
- **Effective enforcement change:** 2026-08-30
- **Verified:** 2026-09-02
- **Volatility:** MEDIUM/HIGH
- **Maps to:** C6, C16, C19; search/compliance Reference
- **Curriculum action:** reference_update

Google continues to target third-party content published on a trusted site primarily to exploit that site's reputation. EEA enforcement behavior differs from outside EEA after 2026-08-30, but the durable curriculum lesson is simpler: **site-reputation exploitation is a compliance/business-risk pattern, not a sustainable Affiliate shortcut**.

## 6. YouTube Shopping Affiliate and Shopee watch

### EXT:YOUTUBE:SHOPPING-AFFILIATE-VN

- **Source:** YouTube Help — YouTube Shopping affiliate overview & eligibility
- **URL:** https://support.google.com/youtube/answer/13376398?hl=vi
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C6–C8; platform Reference
- **Curriculum action:** reference_update

YouTube lists **Vietnam** among markets where eligible creators can participate in YouTube Shopping Affiliate. Use as a channel option in M03–M05, not as a new Core lesson.

### EXT:YOUTUBE:AMAZON-AFFILIATE-US-2026-08

- **Source:** YouTube Official Blog — YouTube Shopping / Amazon creator affiliate integration
- **URL:** https://blog.youtube/news-and-events/youtube-shopping-amazon-creator-affiliates/
- **Published:** 2026-08-27
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** platform watch
- **Curriculum action:** watch_only

Current announcement scope is eligible U.S. creators. Do not generalize it to Vietnam eligibility or alter Core.

### EXT:SHOPEE:AFFILIATE-WATCH-2026-08

- **Source status:** official/primary-source watch
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** platform Reference
- **Curriculum action:** watch_only

No material August 2026 Shopee Affiliate Vietnam rule/commission/attribution change has been confirmed from a primary source strongly enough to justify a Core or Mission change. Secondary reports must not be promoted to curriculum truth without primary verification.

## 7. Agentic commerce

### EXT:GOOGLE:UCP-2026

- **Source:** Google — Universal Commerce Protocol / agentic commerce
- **URL:** https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/
- **Verified:** 2026-09-02
- **Volatility:** MEDIUM
- **Maps to:** C13–C17; Advanced A09
- **Curriculum action:** watch_only

### EXT:GOOGLE:UCP-UPDATES-2026

- **Source:** Google — UCP updates
- **URL:** https://blog.google/products-and-platforms/products/shopping/ucp-updates/
- **Verified:** 2026-09-02
- **Volatility:** MEDIUM
- **Maps to:** C13–C17; Advanced A09; production Reference
- **Curriculum action:** watch_only

Operating direction:

```text
content/search/conversation
→ AI discovery & comparison
→ product/merchant data
→ recommendation/agent action
→ cart/checkout or merchant handoff
→ measurement & attribution
```

This strengthens the need for machine-readable product truth, freshness, permission, auditable intent and attribution continuity. It does **not** prove traditional affiliate links are obsolete and does not justify raising Bot authority.

## 8. AI transparency and global disclosure

### EXT:EU:AI-ACT-ARTICLE50-2026

- **Source:** European Commission — Guidelines on transparency obligations for providers and deployers of AI systems
- **URL:** https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems
- **Published:** 2026-07-20
- **Applicable from:** 2026-08-02
- **Verified:** 2026-09-02
- **Volatility:** HIGH
- **Maps to:** C6, C16, C19; legal/AI-transparency Reference
- **Curriculum action:** mission_or_lesson_change

Article 50 transparency obligations apply from 2026-08-02 within their legal scope. Requirements differ by provider/deployer/content/use case and include specified transparency/marking/labelling obligations. Curriculum must be **jurisdiction-aware**; `platform allows publish` is not equivalent to `all legal obligations are satisfied`.

### EXT:FTC:ENDORSEMENTS

- **Source:** U.S. Federal Trade Commission — Endorsement Guides FAQ
- **URL:** https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking
- **Verified:** 2026-09-02
- **Volatility:** MEDIUM
- **Maps to:** C6, C16, C19; compliance Reference
- **Curriculum action:** reference_update

FTC guidance treats affiliate commission relationships as material connections that should be disclosed clearly and conspicuously. For global-facing content, verify applicable jurisdiction and platform rules instead of copying one disclosure pattern everywhere.

## 9. Current facts không tự quyết định curriculum structure

Research above does **not** justify:

- thêm/xóa Part/Chapter chỉ để phản ứng với một trend 2026;
- biến từng platform update thành Core lesson bắt buộc;
- đưa PPS vào M00 như Product truth;
- replacing foundational tracking/economics concepts;
- declaring SEO dead hoặc AEO/GEO là replacement;
- declaring affiliate links dead;
- treating AI automation as autonomous publishing without review;
- hard-coding current platform/legal/tax thresholds as permanent truths.

Correct operating model:

```text
OUTCOME-DRIVEN CORE
+
FRESH CURRENT FACTS
+
EXPLICIT UPDATE/WATCH DECISION
+
LEARNER OUTCOME + CONTINUOUS WATCH
=
AFFILIATE INTELLIGENCE CURRICULUM
```

## 10. Authoring priority after this refresh

1. **C7–C10:** add measurement/attribution configuration context; source success ≠ measurement completeness.
2. **M03/C6:** add AIGC provenance, originality/authorization, jurisdiction and current-policy gates before moving M03 to `ready`.
3. **C15–C19:** extend least privilege into data minimisation, purpose, retention and downstream-sharing boundaries.
4. **C1:** keep M00 simple; platform score may be observed as a visible signal but must not become Product truth or permanent schema requirement.
5. **C20:** production review may consume current-fact feeds but may not silently rewrite policy/prompt/formula/weights.
6. **Reference freshness cadence:** recurring review; when no material update exists, record `watch_only`/`no_material_change` instead of manufacturing curriculum work.
