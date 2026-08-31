# Phần 1 — TRUSTWORTHY DATA & GROUNDED AI

- Timeline: **Evidence-gated; recalibrate after learner pilot**.
- **Chapters:** C3–C5
- **Core:** 9 micro-lessons
- **Missions:** M01–M02
- **Outcome:** Bot giữ lịch sử/provenance đáng tin cậy và AI chỉ enrich một deterministic baseline có fallback.

## Trạng thái authoring

- **Chương 3:** learner-ready — canonical ingest/identity/validation/normalization.
- **Chương 4:** learner-ready — append-only history, delta/freshness, second E1 observation + restart.
- **M01:** learner-ready; Mission chỉ DONE khi Capability + Reality E1 + Operated đều đạt.
- **Chương 5 / M02:** chưa author; chỉ bắt đầu sau khi M01 PASS.

## Attempt trước knowledge pull

1. M01 Checkpoint 1: đưa data xấu/ambiguous qua ingest M00 hiện có, quan sát identity/validation gap rồi mới pull Chương 3.
2. M01 Checkpoint 2: cố ý ghi đè snapshot để quan sát data loss trước khi pull `4.1–4.2`.
3. M01 Checkpoint 3: second E1 observation + restart + raw change report trước khi pull `4.3`.
4. M02: chạy deterministic baseline trước AI, rồi mới thử AI valid/unsupported/unavailable.

## Core checklist

### Chương 3 — Minimal trustworthy ingest

- [ ] **3.1** — [Stable subject identity, observation identity và schema vừa đủ](../lessons/part-01/chapter-03/3.1-subject-observation-identity-schema.md)
- [ ] **3.2** — [Validation contract, clear errors và failure-path tests](../lessons/part-01/chapter-03/3.2-validation-clear-errors-failure-tests.md)
- [ ] **3.3** — [Normalization, provenance và source boundary nhỏ nhất](../lessons/part-01/chapter-03/3.3-normalization-provenance-source-boundary.md)

Chương 3 kết thúc ở:

```text
M00 E1 observation
→ stable subject identity
→ strict validation
→ canonical normalization
→ provenance-preserving observation
```

### Chương 4 — History và change observation

- [ ] **4.1** — [Append-only JSONL và immutable snapshots](../lessons/part-01/chapter-04/4.1-append-only-jsonl-immutable-snapshots.md)
- [ ] **4.2** — [Delta, timestamp, freshness và historical query](../lessons/part-01/chapter-04/4.2-delta-timestamp-freshness-historical-query.md)
- [ ] **4.3** — [Second observation cycle, restart và change report](../lessons/part-01/chapter-04/4.3-second-observation-restart-change-report.md)

Chương 4 phải hoàn thành flow:

```text
overwrite failure
→ immutable append-only history
→ exact duplicate vs conflict
→ preserve valid out-of-order evidence
→ historical query by observed_at
→ delta semantics
→ freshness(as_of, policy)
→ second E1 observation
→ restart proof
→ deterministic change report
```

M01 không yêu cầu thị trường phải thay đổi. `UNCHANGED` là Reality outcome hợp lệ nếu t1/t2 đều là E1 observations thật.

### Chương 5 — Grounded AI advisory

- [ ] **5.1** — Chọn deterministic rule hay AI theo decision value
- [ ] **5.2** — Structured extraction với evidence refs và uncertainty
- [ ] **5.3** — Eval case, invalid-output rejection, fallback, cost và privacy

Chương 5 chưa được pull trước khi M01 PASS. AI không được dùng để bù cho history/evidence contract chưa đáng tin.

## M01 gate trước M02

Trước khi sang M02 phải chứng minh:

```text
Capability
+ Reality E1
+ Operated
```

Tối thiểu:

- canonical ingest chạy đúng;
- stable `subject_id` tách `observation_id`;
- history append-only + durable qua restart;
- duplicate/conflict/out-of-order semantics rõ;
- delta không trộn missing/zero/unchanged;
- freshness dùng explicit `as_of/policy`;
- ít nhất một subject thật có E1 observations tại t1 và t2;
- same history/as_of/policy cho report deterministic;
- M00 behavior không regression;
- S0, không external side effect.

## Part PASS

- [ ] M01–M02 đều có Capability PASS, Reality verified và Operated
- [ ] Stable subject identity không bị trộn với observation identity
- [ ] Snapshot cũ không bị overwrite và query history được
- [ ] Valid out-of-order evidence không bị silently drop
- [ ] Freshness không được invent khi thiếu policy
- [ ] Core product decision vẫn chạy khi AI unavailable
- [ ] Unsupported AI claim không trở thành scoring fact

[← Part trước](part-00.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-02.md)
