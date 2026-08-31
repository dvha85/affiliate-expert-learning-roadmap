---
mission_id: "M01"
title: "Trustworthy History"
status: draft
requires_missions: ["M00"]
bot_version_from: "v0.1"
bot_version_to: "v0.2"
estimated_hours: 12
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
→ append history without overwriting old evidence
→ compare two observation times
→ report change / unchanged / missing / stale / unknown
```

M01 dùng data/store nhỏ nhất đáp ứng behavior. PostgreSQL, repository pattern, concurrency, scheduler hoặc abstraction rộng không phải mục tiêu tự thân.

M01 cố ý tách bốn identity/time concept ngay từ đầu:

```text
subject_id
= đối tượng Product/Offer ổn định cần theo dõi qua thời gian

observation_id
= một lần quan sát cụ thể

observed_at
= khi thế giới/source được quan sát

ingested_at
= khi Bot nhận/lưu observation
```

Không dùng `product_name` thay cho stable identity, và không dùng `observation_id` để đại diện cho Product xuyên thời gian.

## Starting Bot State — Trạng thái Bot ban đầu

Starting state là learner commit đã PASS M00:

- Bot v0.1 chạy/test được;
- có 5 E1 public observations;
- có human ranking, deterministic BotDecision và abstention case;
- M00 `observation.Record` đã tồn tại;
- chưa có stable `subject_id`, strict ingest contract, validated history hoặc change semantics.

Reference không phải starting state. Chương 03 phải **evolve M00 record/code hiện có**, không yêu cầu learner viết parser/schema lại từ trang trắng.

## Try First — Thử trước

### Checkpoint 1 — Đưa input xấu qua ingest M00 hiện có

1. Copy một M00 observation file thành scratch input; chưa refactor trước.
2. Chạy lần lượt các case:
   - valid record;
   - malformed JSON;
   - unknown JSON field;
   - negative price;
   - missing `source_url`;
   - hai observations khác nhau nhưng cùng `product_name`;
   - hai observations của cùng Product ở hai thời điểm nhưng không có stable `subject_id`.
3. Ghi before behavior: parser/validator hiện fail rõ, silently accept hay khiến identity mơ hồ?
4. Viết câu hỏi: “Nếu Product đổi tên hoặc hai Product trùng tên, Bot sẽ biết snapshot nào thuộc cùng subject bằng cách nào?”
5. **Sau attempt mới pull `3.1–3.3`** rồi harden ingest/normalization.

Checkpoint 1 không yêu cầu history store. Output của Chương 03 là một **validated canonical observation** sẵn sàng để Chương 04 lưu append-only.

### Checkpoint 2 — Cố ý ghi đè history

1. Lưu một snapshot cho cùng `subject_id`.
2. Tạo observation thứ hai ở thời điểm khác.
3. Dùng implementation đơn giản ghi đè current record và quan sát evidence nào bị mất.
4. Viết câu hỏi: watcher/decision audit sau này không còn trả lời được điều gì?
5. Sau attempt, pull `4.1–4.2` rồi chuyển sang immutable append-only snapshots.

### Checkpoint 3 — Second observation + restart

1. Ghi observation thật lần hai trên ít nhất một `subject_id` sau một khoảng thời gian đã khai báo.
2. Import snapshot thứ hai bằng command thủ công, rồi restart process.
3. Đọc lại history, so snapshot cũ/mới và phân loại delta.
4. Sau attempt, pull slice cần thiết từ `4.3` để tạo change report có thể lặp lại.

## Canonical ingest contract của M01

Chương 03 phải đưa M00 record tới shape tối thiểu về semantics như sau; exact Go type có thể khác nếu giải thích được:

```yaml
subject_id:
observation_id:
product_name:
source_url:
observed_at:
ingested_at:
access_method: public_manual
evidence_kind: real
price:
currency:
commission_rate:
other_visible_signal:
missing_fields: []
notes:
```

Quy tắc:

- `subject_id` phải ổn định qua nhiều observations của cùng Product/Offer;
- `observation_id` phải xác định một observation cụ thể;
- `observed_at` đến từ observation context, không được thay bằng thời điểm import;
- `ingested_at` mô tả khi Bot nhận record và không được giả làm thời điểm thị trường được quan sát;
- missing giữ `null`/unknown, không đổi thành `0`;
- normalized value không được xóa raw/provenance cần thiết để audit;
- unknown field phải có policy rõ: strict reject ở canonical ingest hoặc explicit quarantine; không silently ignore material field rồi tuyên bố input đã validated.

## Run — Chạy

Exact history command sẽ được chốt khi Chương 04 hoàn tất. Với Chương 03, executable phải có một path có thể chạy/test để chứng minh ingest contract, ví dụ CLI hiện tại hoặc test trực tiếp trên ingest package.

Draft target sau toàn M01:

```bash
cd lab/learner/affiliate-bot
go run ./cmd/bot
go test ./...
```

Expected observable output sau toàn M01:

```text
Bot version: v0.2
Snapshots saved: <n>
Subject: <subject_id>
Previous observed_at: <time>
Current observed_at: <time>
Changes:
  price: unchanged | changed | missing | unknown
  commission: unchanged | changed | missing | unknown
Freshness: current | stale | unknown
```

## Observe — Quan sát

Learner phải lưu:

- parser/validation behavior trước và sau hardening;
- identity ambiguity trước khi có `subject_id`;
- distinction giữa `subject_id`, `observation_id`, `observed_at`, `ingested_at`;
- raw/provenance nào được giữ qua normalization;
- evidence bị mất trong overwrite attempt;
- field thay đổi thật, không đổi, thiếu hoặc không so sánh được;
- gap nào thực sự cần storage/query control; scheduler/retry vẫn để M06.

## Knowledge Pull — Lấy kiến thức đúng lúc

### Checkpoint 1

- `3.1` — evolve M00 record: stable subject identity, observation identity, timestamps và schema vừa đủ;
- `3.2` — validation contract, clear errors, unknown/malformed/invalid field và failure-path tests;
- `3.3` — normalization/provenance và source boundary nhỏ nhất cho public/manual ingest.

Chương 03 không build history store, watcher, database hay AI. Nó kết thúc ở canonical validated observation.

### Checkpoint 2

- `4.1` — immutable snapshots và persistence tối thiểu;
- `4.2` — delta, timestamp, freshness và historical query.

### Checkpoint 3

- `4.3` — second observation cycle, restart và change report.

Khi author Chương 04, ưu tiên file/append-only implementation trước. SQL/repository chỉ ở slice bắt buộc nếu concrete Mission test thật cần chúng.

## Improve — Cải tiến

Sau Chương 03:

- evolve M00 record thay vì duplicate schema;
- thêm stable subject identity;
- reject malformed/invalid observations rõ ràng;
- xử lý unknown field theo explicit policy;
- preserve source/raw context và normalized value;
- giữ `observed_at` khác `ingested_at`;
- không coi missing là `0`;
- nối ingest path vào executable/test thật, không để package dead code.

Sau Chương 04:

- tạo immutable Snapshot có identity + `observed_at`;
- append thay vì overwrite;
- compare cùng `subject_id` qua hai timestamps;
- thêm freshness classification từ explicit `as_of`/policy;
- preserve valid out-of-order evidence thay vì silently drop.

## Tests — Kiểm thử

### Chương 03 acceptance slice

- valid M00/E1 observation đi qua canonical ingest;
- malformed JSON fail rõ;
- unknown field không bị silently ignored theo cách làm mất contract;
- invalid negative/out-of-domain numeric value fail rõ;
- missing source/identity fail rõ;
- `subject_id` và `observation_id` không bị dùng lẫn;
- same `subject_id` có thể có nhiều `observation_id`;
- same product name không tự động chứng minh same subject;
- missing giữ khác observed zero;
- `observed_at` và `ingested_at` được phân biệt;
- normalization không biến seller/source claim thành measured business fact;
- M00 ranking/abstention không regression.

### Chương 04 / final M01 acceptance slice

- snapshot input mutation không sửa history cũ;
- second snapshot không overwrite first snapshot;
- exact duplicate xử lý idempotent/deterministic;
- cùng `observation_id` nhưng content khác phải conflict/review, không silently replace;
- valid out-of-order observation được preserve và đánh dấu/order đúng theo `observed_at`, hoặc nếu implementation tạm thời chưa hỗ trợ thì capability không được tuyên bố DONE;
- missing khác zero/unchanged;
- delta change/unchanged/missing đúng;
- restart vẫn đọc lại được history theo persistence scope đã chọn;
- second observation tạo change report deterministic.

## Reality Check — Kiểm chứng thực tế

**Minimum:** E1.

Chương 03 có thể dùng lại 5 E1 observations từ M00 để harden ingest; chưa cần chờ observation lần hai để lesson 3.1–3.3 được applied.

Final M01 Reality minimum:

```text
ít nhất 1 subject thật
+ observation E1 tại t1
+ observation E1 tại t2
+ cùng stable subject_id
+ observed_at khác nhau
```

Recommended: lặp lại trên nhiều subject nếu thuận tiện, nhưng không ép learner đợi cả 5 Product thay đổi chỉ để PASS history semantics.

- raw/public source có thể không thay đổi; `unchanged` là outcome hợp lệ;
- nếu source biến mất/không truy cập được, lưu missing/access failure thay vì tạo giá trị;
- sample snapshots chỉ chứng minh edge cases, không thay second E1 observation.

M01 không yêu cầu source thật sự đổi giá/commission. Reality gate kiểm lịch sử quan sát trung thực, không kiểm learner may mắn gặp change.

## Operate — Vận hành

Final M01 tối thiểu:

1. ingest hai observation times cho cùng subject;
2. restart process và xác minh history theo persistence scope đã chọn;
3. chạy một no-change cycle;
4. chạy một changed/missing fixture cycle;
5. chạy lại cùng hai snapshots để chứng minh report deterministic.

Nếu store hiện tại không survive restart, capability chưa đạt `Operated`.

## Failure Case — Tình huống lỗi

- malformed/unknown field;
- source/subject/observation identity rỗng;
- invalid timestamp;
- same name nhưng different subject;
- exact duplicate;
- same observation ID nhưng conflicting content;
- out-of-order valid observation;
- partial record;
- store failure;
- truncated/corrupt history file hoặc restart không đọc lại được;
- learner code vô tình mutate snapshot cũ.

Không được silently drop record, silently relabel evidence hoặc overwrite evidence cũ.

## Safety Gate — Cổng an toàn

**S0 — Evidence/Data.**

Authority ceiling vẫn là public/manual read + local processing. M01 không tự scrape, login, publish, message, spend hoặc thay platform state.

Nếu learner sau này dùng source adapter ngoài manual file, adapter phải có access method/permission rõ và vẫn read-only. Restricted/private scraping là `DENY`.

## Evidence — Bằng chứng

Lưu dưới `artifacts/missions/M01/`:

### Chương 03

- before ingest behavior;
- identity ambiguity note;
- canonical observation shape sau hardening;
- valid + malformed + unknown-field + invalid-domain outputs/tests;
- `subject_id` vs `observation_id` example;
- `observed_at` vs `ingested_at` example;
- normalization/provenance note;
- final Chương 03 test output.

### Chương 04 / final M01

- overwrite/data-loss attempt;
- t1/t2 E1 Observation records;
- immutable Snapshot/history artifact;
- delta/freshness output;
- happy/failure/restart test output;
- restart/persistence note;
- learner commit và storage trade-off note.

Evidence chain:

```text
Public Observation(E1)
→ Canonical Validated Observation
→ Snapshot(t1)
→ Snapshot(t2)
→ Signal-like Delta
→ no external Action
```

## Explain-back — Giải thích lại

Sau Chương 03 learner phải giải thích được:

1. Vì sao Product/subject khác Observation?
2. Vì sao `product_name` không phải stable identity đủ mạnh?
3. Vì sao `observation_id` không thể dùng thay `subject_id`?
4. `observed_at` khác `ingested_at` ở điểm nào và nhầm chúng gây lỗi gì?
5. Validation khác normalization thế nào?
6. Vì sao normalization không được invent missing data hoặc nâng seller claim thành fact?
7. Vì sao M01 chưa cần database/watcher/concurrency?

Final M01 bổ sung:

8. Overwrite làm mất audit nào?
9. Vì sao missing khác zero hoặc unchanged?
10. Store tối giản đáp ứng gì và chưa đáp ứng gì?
11. Provenance/freshness ảnh hưởng decision thế nào?
12. Next measurement nào cần cho grounded AI ở M02?

## Mission PASS — Tiêu chí PASS

M01 vẫn `draft` cho tới khi Chương 04 được author/review; hoàn thành Chương 03 chưa đồng nghĩa M01 DONE.

### Capability

- [ ] Chương 03 ingest/validation/normalization contract chạy đúng
- [ ] stable subject identity tách khỏi observation identity
- [ ] observed time tách khỏi ingest time
- [ ] history immutable và append-only sau Chương 04
- [ ] delta/freshness semantics đúng sau Chương 04
- [ ] executable thực sự dùng ingest/history path
- [ ] happy/failure/restart tests đạt
- [ ] M00 behavior không regression
- [ ] required knowledge được pull sau attempt và explain-back đạt

### Reality

- [ ] M00 E1 evidence được ingest trung thực trong Chương 03
- [ ] final M01 có ít nhất một subject với t1/t2 E1 observations
- [ ] source/observed_at/access method được giữ
- [ ] missing/unchanged/zero không bị trộn
- [ ] sample chỉ dùng cho edge/failure cases

### Operated

- [ ] chạy đủ t1/t2, restart, no-change và failure cycles
- [ ] không overwrite hoặc silently drop evidence
- [ ] S0 đạt, không external side effect

## Bot Version Result — Kết quả phiên bản Bot

Chỉ bump version sau khi **toàn M01** đạt Capability + Reality + Operated:

```text
v0.1 first evidence decision
→ v0.2 trustworthy observation history
```

Hoàn thành riêng Chương 03 chỉ tạo **M01 ingest checkpoint**, chưa phải Bot v0.2.

Authority ceiling không đổi: public/manual read + local deterministic processing.

## Next Mission — Mission tiếp theo

M02 — Grounded AI Advisor: chỉ bắt đầu sau khi M01 PASS; deterministic baseline/history phải tồn tại trước AI.
