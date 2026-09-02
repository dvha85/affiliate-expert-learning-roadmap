---
mission_id: "M01"
title: "Trustworthy History"
status: ready
curriculum_version: 1
release_kind: "bot"
requires_missions: ["M00"]
bot_version_from: "v0.1"
bot_version_to: "v0.2"
estimated_hours: 12
delivery:
  starter_paths:
    - "lab/learner/affiliate-bot/"
  eval_pack: null
  verification_commands:
    - "cd lab/learner/affiliate-bot && go test ./..."
knowledge:
  required: ["3.1", "3.2", "3.3", "4.1", "4.2", "4.3"]
  on_demand: []
  reference: []
milestones:
  contributes_to: ["G2"]
evidence:
  minimum_level: "E1"
  reality_required: true
safety_gate: "S0"
risk_scope:
  external_side_effects: false
---

# Mission M01 — Trustworthy History

## Ship Target — Mục tiêu bàn giao

Nâng Bot v0.1 thành v0.2 có thể:

```text
read M00 observations
→ identify stable subject vs individual observation
→ validate/normalize without inventing missing values
→ create immutable snapshots
→ append durable history without overwriting old evidence
→ query same subject across observed_at
→ compare two observations
→ report changed / unchanged / missing / unknown
→ classify freshness only from explicit as_of + policy
```

M01 dùng storage nhỏ nhất đáp ứng behavior. Canonical learner path là **append-only JSONL file**. PostgreSQL, repository pattern, concurrency, scheduler hoặc watcher không phải mục tiêu tự thân.

M01 giữ bốn identity/time concept tách biệt:

```text
subject_id
= Product/Offer ổn định cần theo dõi qua thời gian

observation_id
= một lần quan sát cụ thể

observed_at
= khi source/world được quan sát

ingested_at
= khi Bot nhận/lưu observation
```

Không dùng `product_name` thay stable identity và không dùng `observation_id` làm Product identity xuyên thời gian.

## Starting Bot State — Trạng thái Bot ban đầu

Learner workspace:

```text
lab/learner/affiliate-bot/
```

Starting state là learner commit đã PASS M00:

- Bot v0.1 chạy/test được;
- có 5 E1 public observations;
- có deterministic BotDecision + abstention;
- M00 observation record và parser/validation tối thiểu đã tồn tại;
- chưa có stable `subject_id`, canonical M01 ingest contract, immutable durable history, delta/freshness semantics hoặc restart proof.

Reference không phải starting state. Chương 03 là knowledge/application slice của **M01 Checkpoint 1**, không phải prerequisite xảy ra trước khi M01 bắt đầu.

## Try First — Thử trước

### Checkpoint 1 — Ingest contract

Bắt đầu từ M00 record hiện có, chưa giả định Chương 03 đã được apply:

```text
M00 record
→ bad-input/identity attempt
→ 3.1–3.3
→ canonical validated observation
```

Sau khi Checkpoint 1 + Chương 03 được applied, learner mới có canonical observation đủ điều kiện để bước vào Checkpoint 2/history work.

### Checkpoint 2 — Cố ý overwrite để thấy data loss

1. Chọn một canonical observation của `subject_id` thật tại `t1`.
2. Lưu nó bằng cách đơn giản nhất như một current JSON record.
3. Tạo observation thứ hai của cùng `subject_id` tại `t2`.
4. Ghi đè current record bằng observation `t2`.
5. Trước khi đọc 4.1–4.2, ghi chính xác evidence nào đã mất và câu hỏi audit nào không còn trả lời được.

Ví dụ:

```text
Tôi còn biết current price.
Tôi không còn chứng minh được price tại t1 là gì.
Tôi không còn biết change xảy ra giữa hai observations nào.
```

**Sau attempt mới pull `4.1–4.2`.**

### Checkpoint 3 — Second E1 observation + restart

1. Với ít nhất một `subject_id` thật từ M00/M01, tạo observation E1 lần hai tại `t2`, có `observed_at` khác `t1`.
2. Append snapshot thứ hai vào durable history.
3. Dừng process và chạy lại.
4. Query history sau restart; xác minh cả `t1` và `t2` còn tồn tại.
5. Compare theo `observed_at`, tạo change report.
6. Chạy lại report trên cùng history để kiểm deterministic.
7. **Sau attempt mới pull `4.3`** để harden second-cycle/restart/report behavior.

## Canonical history contract

### Canonical learner store

M01 dùng:

```text
data/history.jsonl
```

Mỗi dòng là **một immutable snapshot** độc lập:

```json
{"subject_id":"product-a","observation_id":"obs-a-1","observed_at":"...","ingested_at":"..."}
{"subject_id":"product-a","observation_id":"obs-a-2","observed_at":"...","ingested_at":"..."}
```

Không update dòng cũ tại chỗ để “sửa lịch sử”. Nếu observation cũ sai, giữ record gốc và tạo correction/review artifact theo implementation nhỏ nhất có thể audit.

### Snapshot immutability

Sau khi append thành công:

```text
caller mutate object in memory
≠ historical record silently changes
```

Store phải lưu một serialized/copy value, không giữ alias cho object có thể mutate.

### Duplicate/conflict semantics

M01 phân biệt ba trường hợp:

```text
same observation_id + same canonical content
→ EXACT_DUPLICATE
→ idempotent / already_seen

same observation_id + different canonical content
→ CONFLICT
→ HUMAN_REVIEW / reject conflicting append

same subject_id + same observed_at + conflicting material values
→ CONFLICT
→ HUMAN_REVIEW
```

Không silently replace snapshot cũ.

### Out-of-order observations

Phân biệt:

```text
invalid observed_at
→ reject/quarantine
```

với:

```text
valid evidence đến muộn
observed_at < latest observed_at
→ preserve evidence
→ mark out_of_order = true nếu cần
→ query/order lịch sử theo observed_at
```

Arrival order (`ingested_at`) không được giả làm world-time order (`observed_at`).

## Delta contract

Delta chỉ so observations của **cùng `subject_id`**.

Per-field state tối thiểu:

```text
CHANGED
UNCHANGED
MISSING_CURRENT
MISSING_PREVIOUS
UNKNOWN
NOT_COMPARABLE
```

Ví dụ:

```text
previous price = 299000
current price = 299000
→ UNCHANGED

previous price = 299000
current price = 259000
→ CHANGED

previous price = 299000
current price = null
→ MISSING_CURRENT
```

Không được:

```text
null → 0
null → unchanged
```

Mixed currency hoặc semantic-unit mismatch phải `NOT_COMPARABLE`/review, không tính numeric delta giả.

## Freshness contract

M01 không dùng fixed global TTL như “7 ngày luôn stale”. Freshness phải có explicit inputs:

```text
observed_at
+ as_of
+ policy/max_age cho field/decision scope
```

Mental model:

```text
ClassifyFreshness(observed_at, as_of, max_age)
```

Rules:

- `as_of` phải được truyền rõ trong test/report thay vì gọi `time.Now()` rải rác;
- nếu không có policy phù hợp: `UNKNOWN`;
- nếu `as_of < observed_at`: input/time context invalid;
- freshness là property tương đối với decision scope, không phải thuộc tính vĩnh viễn của snapshot.

## Run — Chạy

Chương 04 phải nối history path vào executable/test thật. Exact CLI có thể khác nếu learner giải thích được, nhưng phải quan sát được tương đương:

```bash
cd lab/learner/affiliate-bot
go test ./...
```

Và một executable path cho history/report, ví dụ:

```bash
go run ./cmd/bot history data/history.jsonl <subject_id>
```

Expected observable information:

```text
Bot version: v0.2
History store: data/history.jsonl
Subject: <subject_id>
Snapshots: <n>
Previous observed_at: <time>
Current observed_at: <time>
Delta:
  price: CHANGED | UNCHANGED | MISSING_CURRENT | MISSING_PREVIOUS | UNKNOWN | NOT_COMPARABLE
  commission_rate: ...
Freshness as_of: <time>
Freshness: CURRENT | STALE | UNKNOWN
```

Tên command/format không phải contract máy bắt buộc; semantics và evidence mới là gate.

## Observe — Quan sát

Learner phải lưu:

- overwrite failure trước append-only;
- count/history trước và sau append;
- distinction giữa `observed_at` order và `ingested_at` order;
- exact duplicate vs conflict;
- changed/unchanged/missing/not-comparable delta;
- freshness với explicit `as_of/policy`;
- restart proof;
- M00 decision/ranking regression status.

## Knowledge Pull — Lấy kiến thức đúng lúc

### Sau Checkpoint 1

- `3.1` — stable subject/observation identity và schema vừa đủ;
- `3.2` — validation contract và failure-path tests;
- `3.3` — normalization/provenance/source boundary.

### Sau Checkpoint 2

- `4.1` — append-only JSONL, immutable snapshot, idempotent duplicate và conflict;
- `4.2` — historical query, delta semantics, observed vs ingest time, freshness từ explicit policy.

### Sau Checkpoint 3

- `4.3` — second E1 observation cycle, restart proof, deterministic change report và M01 finalization.

Không kéo SQL, watcher, retry scheduler, message queue hay AI vào M01.

## Improve — Cải tiến

Sau Chương 03:

- stable subject identity;
- strict validated canonical observation;
- provenance/raw context preserved;
- `observed_at != ingested_at`.

Sau Chương 04:

- append immutable JSONL snapshots;
- exact duplicate idempotent;
- conflict không overwrite;
- valid late/out-of-order evidence được preserve;
- history query order theo `observed_at`;
- delta không trộn missing/zero/unchanged;
- freshness dùng explicit `as_of/policy`;
- history survive restart;
- change report deterministic.

## Tests — Kiểm thử

### Chương 03 acceptance slice

- valid E1 observation đi qua canonical ingest;
- malformed/unknown/invalid field fail rõ theo policy;
- stable subject identity tách observation identity;
- missing khác observed zero;
- `observed_at` khác `ingested_at`;
- normalization không invent data;
- M00 behavior không regression.

### Chương 04 / final M01 acceptance slice

- first append tạo snapshot;
- second snapshot không overwrite first;
- input mutation sau append không sửa snapshot đã lưu;
- exact duplicate là idempotent/deterministic;
- same observation ID + conflicting content bị conflict/review;
- same subject + same observed_at + conflicting material value bị conflict/review;
- valid out-of-order evidence được preserve và query đúng theo `observed_at`;
- invalid timestamp fail rõ;
- missing khác zero/unchanged;
- mixed currency/units không bị tính delta numeric giả;
- freshness `CURRENT/STALE/UNKNOWN` chỉ từ explicit `as_of/policy`;
- corrupt/truncated JSONL fail rõ hoặc quarantine rõ, không silently bỏ dòng;
- restart đọc lại history;
- same history + same as_of + same policy tạo same report;
- second E1 observation tạo report;
- M00 ranking/abstention không regression.

## Reality Check — Kiểm chứng thực tế

**Minimum:** E1.

Final M01 Reality minimum:

```text
ít nhất 1 subject thật
+ E1 observation tại t1
+ E1 observation tại t2
+ cùng stable subject_id
+ observed_at khác nhau
```

Recommended: lặp lại nhiều subject nếu thuận tiện, nhưng không ép learner đợi cả 5 Product thay đổi.

`UNCHANGED` là outcome hợp lệ. M01 kiểm history semantics, không yêu cầu thị trường phải thay đổi.

Nếu source không còn truy cập được tại t2, lưu access/missing evidence trung thực; không tạo lại last known value rồi gọi đó là observation mới.

Sample/synthetic chỉ dùng edge/failure tests, không thay second E1 observation.

## Operate — Vận hành

Tối thiểu:

1. ingest/append `t1` và `t2` cho cùng subject;
2. restart và đọc lại cả hai snapshots;
3. một no-change case;
4. một changed hoặc missing fixture case;
5. exact duplicate replay;
6. conflict case;
7. valid out-of-order case;
8. rerun cùng history/as_of/policy để chứng minh deterministic report.

Nếu store không survive restart hoặc evidence cũ bị overwrite, M01 chưa đạt `Operated`.

## Failure Case — Tình huống lỗi

- malformed/unknown field;
- missing subject/observation/source;
- invalid timestamp;
- exact duplicate;
- same observation ID conflicting content;
- same subject/time conflicting value;
- out-of-order valid observation;
- partial record;
- mixed currency/semantic unit;
- append/write failure;
- corrupt/truncated history line;
- learner mutate object sau append;
- freshness policy absent;
- `as_of` trước `observed_at`.

Không silently drop record, overwrite evidence hoặc invent current value.

## Safety Gate — Cổng an toàn

**S0 — Evidence/Data.**

Authority ceiling vẫn là public/manual read + local processing. M01 không scrape tự động, login, publish, message, spend hoặc thay platform state.

`data/history.jsonl` là local learner artifact, không phải permission để watcher tự thu data. Automated collection thuộc Mission sau.

## Evidence — Bằng chứng

Lưu dưới `workspace/artifacts/missions/M01/`:

- Chương 03 ingest artifacts;
- overwrite/data-loss attempt;
- t1/t2 E1 observations;
- append-only `history.jsonl` hoặc equivalent artifact;
- duplicate/conflict/out-of-order outputs;
- delta/freshness report với `as_of/policy`;
- restart proof;
- happy/failure tests;
- deterministic rerun evidence;
- M00 regression test;
- storage trade-off note;
- learner commit.

Evidence chain:

```text
Public Observation(E1)
→ Canonical Validated Observation
→ immutable Snapshot(t1)
→ immutable Snapshot(t2)
→ historical query
→ Delta/Freshness Signal
→ no external Action
```

## Explain-back — Giải thích lại

Learner phải trỏ vào code/evidence của mình để giải thích:

1. `subject_id` khác `observation_id` thế nào?
2. `observed_at` khác `ingested_at` thế nào?
3. Overwrite làm mất audit nào?
4. Vì sao append-only giúp audit nhưng không tự làm data đúng?
5. Exact duplicate khác conflict thế nào?
6. Vì sao valid out-of-order observation nên được preserve?
7. Vì sao query change phải order theo `observed_at`?
8. `missing`, `zero`, `unchanged` và `not comparable` khác nhau thế nào?
9. Freshness cần những input/policy nào?
10. Vì sao không dùng một TTL 7 ngày cho mọi field?
11. JSONL đáp ứng gì và chưa đáp ứng gì?
12. Vì sao M01 chưa cần watcher/concurrency/database?
13. M01 history làm grounded AI ở M02 đáng tin hơn ở điểm nào?

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] Chương 03 ingest/validation/normalization contract chạy đúng
- [ ] stable subject identity tách observation identity
- [ ] observed time tách ingest time
- [ ] history immutable + append-only + durable qua restart
- [ ] duplicate/conflict/out-of-order semantics đúng
- [ ] historical query + delta semantics đúng
- [ ] freshness dùng explicit `as_of/policy`
- [ ] executable/test thực sự dùng history path
- [ ] happy/failure/restart tests đạt
- [ ] M00 behavior không regression
- [ ] `3.1–4.3` được pull sau đúng attempt và explain-back đạt

### Reality

- [ ] có ít nhất một subject với t1/t2 E1 observations
- [ ] source/observed_at/access method được giữ
- [ ] second observation không được giả bằng copy last-known value
- [ ] `UNCHANGED` được chấp nhận như outcome thật
- [ ] missing/unchanged/zero không bị trộn
- [ ] sample chỉ dùng edge/failure cases

### Operated

- [ ] chạy t1/t2 + restart
- [ ] chạy no-change + changed/missing fixture
- [ ] chạy duplicate + conflict + out-of-order
- [ ] cùng history/as_of/policy tạo cùng report
- [ ] không overwrite hoặc silently drop evidence
- [ ] S0 đạt, không external side effect

## Bot Version Result — Kết quả phiên bản Bot

Chỉ bump sau khi **Capability + Reality + Operated** đều đạt:

```text
v0.1 first evidence decision
→ v0.2 trustworthy observation history
```

Authority ceiling không đổi:

```text
public/manual read + local deterministic processing
```

## Next Mission — Mission tiếp theo

M02 — Grounded AI Advisor chỉ bắt đầu sau M01 PASS. Deterministic baseline + trustworthy history phải tồn tại trước AI.
