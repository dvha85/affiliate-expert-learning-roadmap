# Data Freshness for Decisions — Độ mới dữ liệu cho quyết định

## 1. Mục tiêu

Một DecisionPacket đúng tại thời điểm T có thể sai vài phút/giờ sau nếu price, commission, stock, eligibility hoặc policy thay đổi.

Vì vậy:

```text
CORRECT ANALYSIS
+
STALE DATA
=
UNSAFE DECISION
```

## 2. Freshness metadata

Decision-relevant fact nên mang:

```yaml
observed_at:
source_ref:
age_seconds:
freshness_class:
```

`freshness_class` có thể là `FRESH`, `AGING`, `STALE`, `UNKNOWN` theo domain rule.

## 3. Decision freshness map

DecisionPacket nên tổng hợp critical facts:

```yaml
freshness:
  product_price:
  commission:
  availability:
  seller_quality:
  platform_policy:
  conversion_window:
```

Không dùng một freshness score chung nếu critical facts có cadence rất khác nhau.

## 4. Expiry

Decision có:

- `created_at`;
- `expires_at`;
- `next_recheck_at` khi relevant.

Sau expiry:

```text
DO NOT EXECUTE OLD DECISION
→ refresh critical evidence
→ rebuild/revalidate DecisionPacket
```

## 5. Revalidation before action

RISK 1/2 hoặc external side effect cần recheck critical state trước execution:

- target còn tồn tại;
- price/commission còn trong accepted range;
- product/seller còn eligible;
- policy version còn valid;
- approval chưa expire;
- action chưa execute/idempotency key chưa complete.

## 6. Regime changes

Platform policy, creator score definition, tracking/attribution rule hoặc marketplace schema thay đổi có thể làm historical series không còn comparable.

Đánh dấu regime/effective date thay vì giả định metric giữ nguyên nghĩa qua thời gian.

## 7. Missing freshness

Unknown timestamp/source age phải được coi là uncertainty, không mặc định fresh.

## 8. Metrics

Theo dõi:

- stale-decision blocks;
- refresh-before-execute count;
- decision expired before action;
- stale evidence discovered after outcome;
- data-source lag;
- re-evaluation latency.

## 9. Integration với repo freshness policy

`docs/FRESHNESS-POLICY.md` quản current facts của curriculum. File này áp dụng cùng tư duy freshness vào **runtime business decisions**. Hai lớp khác mục đích nhưng cùng nguyên tắc: thông tin biến động phải có source + verified/observed time + recheck policy.