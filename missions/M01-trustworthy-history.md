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
read observations
→ validate/normalize
→ create immutable snapshots
→ append history without overwriting old evidence
→ compare two observation times
→ report change / unchanged / missing / stale / unknown
```

M01 dùng data/store nhỏ nhất đáp ứng behavior. PostgreSQL, abstraction hoặc concurrency không phải mục tiêu tự thân.

## Starting Bot State — Trạng thái Bot ban đầu

Starting state là learner commit đã PASS M00:

- Bot v0.1 chạy/test được;
- có 5 E1 public observations;
- có human ranking, deterministic BotDecision và abstention case;
- chưa có validated history hoặc change semantics.

Reference không phải starting state.

## Try First — Thử trước

### Checkpoint 1 — Đưa input xấu qua parser tối giản

1. Tạo Product/Observation struct tối thiểu từ record M00.
2. Đọc file thật trước khi thiết kế schema rộng.
3. Thử valid, malformed, unknown field, negative value và missing source.
4. Lưu before behavior: parser đang fail rõ hay silently accept?
5. Sau attempt, pull `3.1–3.3` rồi harden ingest/normalization.

### Checkpoint 2 — Cố ý ghi đè history

1. Lưu một snapshot cho cùng Product.
2. Tạo observation thứ hai ở thời điểm khác.
3. Dùng implementation đơn giản ghi đè current record và quan sát evidence nào bị mất.
4. Viết câu hỏi: watcher/decision audit sau này không còn trả lời được điều gì?
5. Sau attempt, pull `4.1–4.2` rồi chuyển sang immutable append-only snapshots.

### Checkpoint 3 — Second observation + restart

1. Ghi observation thật lần hai trên cùng subject sau một khoảng thời gian đã khai báo.
2. Import snapshot thứ hai bằng command thủ công, rồi restart process.
3. Đọc lại history, so snapshot cũ/mới và phân loại delta.
4. Sau attempt, pull slice cần thiết từ `4.3` để tạo change report có thể lặp lại.

## Run — Chạy

Exact command sẽ được chốt khi Mission lên `ready`; draft target tối thiểu:

```bash
cd lab/learner/affiliate-bot
go run ./cmd/bot
go test ./...
```

Expected observable output:

```text
Bot version: v0.2
Snapshots saved: <n>
Subject: <id>
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
- evidence bị mất trong overwrite attempt;
- field thay đổi thật, không đổi, thiếu hoặc không so sánh được;
- difference giữa Product identity và Observation/Snapshot;
- gap nào thực sự cần storage/query control; scheduler/retry vẫn để M06.

## Knowledge Pull — Lấy kiến thức đúng lúc

### Checkpoint 1

- `3.1` — Product struct, JSON/file import và schema vừa đủ;
- `3.2` — validation, clear errors và failure-path tests;
- `3.3` — source adapter boundary, normalization và provenance.

### Checkpoint 2

- `4.1` — immutable snapshots và persistence tối thiểu;
- `4.2` — delta, timestamp, freshness và historical query.

### Checkpoint 3

- `4.3` — second observation cycle, restart và change report.

Khi author `ready`, các lesson phải cung cấp file/append-only implementation trước. SQL/repository chỉ ở slice bắt buộc nếu concrete Mission test thật cần chúng.

## Improve — Cải tiến

- reject invalid/malformed observations rõ ràng;
- preserve raw/source reference và normalized value;
- tạo immutable Snapshot có identity + `observed_at`;
- append thay vì overwrite;
- compare cùng subject qua hai timestamps;
- không coi field missing là `0` hoặc unchanged;
- thêm freshness classification;
- nối history path vào executable, không để package dead code.

## Tests — Kiểm thử

Draft acceptance tests:

- valid real observation đi qua ingest;
- malformed/unknown/invalid field fail rõ;
- snapshot input mutation không sửa history cũ;
- second snapshot không overwrite first snapshot;
- duplicate snapshot xử lý deterministic;
- out-of-order timestamp được reject hoặc đánh dấu;
- missing khác zero/unchanged;
- delta change/unchanged/missing đúng;
- restart vẫn đọc lại được history theo persistence scope đã chọn;
- second observation tạo change report deterministic;
- M00 ranking/abstention không regression.

## Reality Check — Kiểm chứng thực tế

**Minimum:** E1.

- dùng lại cùng public subjects từ M00;
- lấy observation thứ hai có `observed_at` khác;
- raw/public source có thể không thay đổi; “unchanged” là outcome hợp lệ;
- nếu source biến mất/không truy cập được, lưu missing/access failure thay vì tạo giá trị;
- sample snapshots chỉ chứng minh edge cases, không thay second E1 observation.

M01 không yêu cầu source phải thật sự đổi giá/commission. Reality gate kiểm lịch sử quan sát trung thực, không kiểm learner may mắn gặp change.

## Operate — Vận hành

Tối thiểu:

1. ingest hai observation times cho cùng subject;
2. restart process và xác minh history theo persistence scope đã chọn;
3. chạy một no-change cycle;
4. chạy một changed/missing fixture cycle;
5. chạy lại cùng hai snapshots để chứng minh report deterministic.

Nếu store hiện tại không survive restart, Mission author phải hoặc bổ sung minimal durable store, hoặc ghi rõ capability chưa đạt `Operated`.

## Failure Case — Tình huống lỗi

- malformed/unknown field;
- source/identity rỗng;
- zero/invalid timestamp;
- duplicate snapshot;
- out-of-order observation;
- partial record;
- store failure;
- truncated/corrupt history file hoặc restart không đọc lại được;
- learner code vô tình mutate snapshot cũ.

Không được silently drop record hoặc overwrite evidence.

## Safety Gate — Cổng an toàn

**S0 — Evidence/Data.**

Authority ceiling vẫn là public/manual read + local processing. M01 không tự scrape, login, publish, message, spend hoặc thay platform state.

Nếu learner dùng source adapter ngoài manual file, adapter phải có access method/permission rõ và vẫn read-only. Restricted/private scraping là `DENY`.

## Evidence — Bằng chứng

Lưu dưới `artifacts/missions/M01/`:

- before parser behavior + hardened behavior;
- overwrite/data-loss attempt;
- two E1 Observation records;
- immutable Snapshot/history artifact;
- delta/freshness output;
- happy/failure/restart test output;
- restart/persistence note;
- learner commit và storage trade-off note.

Evidence chain:

```text
Observation(E1, t1)
→ Snapshot(t1)
→ Observation(E1, t2)
→ Snapshot(t2)
→ Signal-like Delta
→ no external Action
```

## Explain-back — Giải thích lại

Learner phải trỏ vào code/evidence của mình để giải thích:

1. Vì sao current Product và historical Snapshot khác nhau?
2. Overwrite làm mất quyết định/audit nào?
3. Vì sao missing khác zero hoặc unchanged?
4. Provenance/freshness ảnh hưởng ranking thế nào?
5. Store tối giản hiện tại đáp ứng gì và chưa đáp ứng gì?
6. Vì sao M01 chưa cần production watcher/concurrency?
7. Next measurement nào cần cho grounded AI ở M02?

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] ingest/validation/normalization chạy đúng
- [ ] history immutable và append-only
- [ ] delta/freshness semantics đúng
- [ ] executable thực sự dùng history path
- [ ] happy/failure/restart tests đạt
- [ ] M00 behavior không regression
- [ ] required knowledge được pull sau attempt và explain-back đạt

### Reality

- [ ] có second E1 observations trên cùng public subjects
- [ ] source/observed_at/access method được giữ
- [ ] missing/unchanged/zero không bị trộn
- [ ] sample chỉ dùng cho edge/failure cases

### Operated

- [ ] chạy đủ t1/t2, restart, no-change và failure cycles
- [ ] không overwrite hoặc silently drop evidence
- [ ] S0 đạt, không external side effect

## Bot Version Result — Kết quả phiên bản Bot

```text
v0.1 first evidence decision
→ v0.2 trustworthy observation history
```

Authority ceiling không đổi: public/manual read + local deterministic processing.

## Next Mission — Mission tiếp theo

M02 — Grounded AI Advisor: chạy deterministic baseline trước, rồi kiểm AI valid, unsupported, malformed và unavailable trên cùng E1 evidence.
