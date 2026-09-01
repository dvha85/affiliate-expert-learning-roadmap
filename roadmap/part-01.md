# Phần 1 — TRUSTWORTHY DATA & GROUNDED AI

- Timeline: **Evidence-gated; recalibrate after learner pilot**.
- **Chapters:** C3–C5
- **Core:** 9 micro-lessons
- **Missions:** M01–M02
- **Outcome:** Bot giữ lịch sử/provenance đáng tin cậy và AI chỉ enrich một deterministic baseline có grounding + fallback.

## Trạng thái authoring

- **Chương 3:** learner-ready — canonical ingest/identity/validation/normalization.
- **Chương 4:** learner-ready — append-only history, delta/freshness, second E1 observation + restart.
- **M01:** learner-ready; Mission chỉ DONE khi Capability + Reality E1 + Operated đều đạt.
- **Chương 5:** learner-ready — call/skip AI, grounding, evaluation và deterministic fallback.
- **M02:** learner-ready; Mission chỉ DONE khi Capability + Reality E1 + Operated đều đạt.

## Attempt trước knowledge pull

1. M01 Checkpoint 1: đưa data xấu/ambiguous qua ingest M00 hiện có, quan sát identity/validation gap rồi mới pull Chương 3.
2. M01 Checkpoint 2: cố ý ghi đè snapshot để quan sát data loss trước khi pull `4.1–4.2`.
3. M01 Checkpoint 3: second E1 observation + restart + raw change report trước khi pull `4.3`.
4. M02 Checkpoint 1: human-label eval subset + deterministic baseline trước khi pull `5.1`.
5. M02 Checkpoint 2: chạy untrusted AI replay outputs trước validation rồi mới pull `5.2`.
6. M02 Checkpoint 3: chạy valid/invalid/unsupported/unavailable/injection/skip matrix trước khi pull `5.3`.

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

Chương 4 hoàn thành:

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

- [ ] **5.1** — [Chọn quy tắc tất định hay AI theo giá trị quyết định](../lessons/part-01/chapter-05/5.1-deterministic-rule-hay-ai-theo-decision-value.md)
- [ ] **5.2** — [Trích xuất có cấu trúc với tham chiếu bằng chứng và độ bất định](../lessons/part-01/chapter-05/5.2-structured-extraction-evidence-refs-uncertainty.md)
- [ ] **5.3** — [Đánh giá case, từ chối output sai, fallback, chi phí và riêng tư](../lessons/part-01/chapter-05/5.3-eval-rejection-fallback-cost-privacy.md)

Chương 5 chỉ bắt đầu sau M01 PASS và phải hoàn thành flow:

```text
E1 history
→ human labels before AI
→ deterministic baseline FIRST
→ CALL_AI | SKIP_AI
→ untrusted AI output
→ strict schema validation
→ evidence ref exists?
→ evidence actually supports claim?
→ fact | hypothesis | missing evidence
→ grounded advisory | reject | fallback
→ human-visible analysis
→ no scoring mutation
→ no Action
```

Rule bắt buộc:

```text
structured ≠ grounded
citation/ref exists ≠ claim supported
AI confidence ≠ evidence
AI recommendation ≠ execution permission
```

M02 là **AI Advisor (A1)**, không phải Agent runtime: không tool use, không autonomous loop, không write authority và không Action execution.

Prompt-injection case chỉ PASS khi đồng thời giữ:

```text
authority containment
+
analysis integrity / grounding
```

Tức là injected content không được tăng quyền **và** không được bypass schema/ref/support gate để trở thành grounded fact/scoring input.

M02 chỉ đánh giá analysis/information utility trên E1 eval set. Không được tuyên bố AI tăng conversion/revenue trước khi có outcome evidence ở Mission sau.

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

## M02 gate trước Part 02 / M03

M02 chỉ DONE khi:

```text
Capability
+ Reality E1
+ Operated
```

Tối thiểu:

- deterministic core chạy khi Advisor absent/unavailable;
- explicit `CALL_AI | SKIP_AI` + reason;
- human labels tồn tại trước AI output;
- strict advisory schema;
- evidence-ref validity + claim-support grounding;
- fact/hypothesis/missing tách rõ;
- unsupported claim không mutate Product/history/scoring facts;
- injection không tăng authority và không bypass grounding;
- replay/live execution evidence được phân loại trung thực;
- valid/invalid/unsupported/fallback/injection/skip cases được vận hành;
- no tool/write/external side effect;
- S1 authority ceiling giữ nguyên.

## Part PASS

- [ ] M01–M02 đều có Capability PASS, Reality verified và Operated
- [ ] Stable subject identity không bị trộn với observation identity
- [ ] Snapshot cũ không bị overwrite và query history được
- [ ] Valid out-of-order evidence không bị silently drop
- [ ] Freshness không được invent khi thiếu policy
- [ ] Core product decision vẫn chạy khi AI unavailable
- [ ] Có ít nhất một `SKIP_AI` case hợp lý
- [ ] Evidence ref tồn tại nhưng không support claim vẫn bị chặn
- [ ] Unsupported AI claim không trở thành scoring/history fact
- [ ] Prompt injection không đổi authority và không vượt grounding gates
- [ ] Replay không bị trình bày như live provider evidence
- [ ] M02 không claim business lift từ E1-only evaluation
- [ ] AI không có tool/write/execution authority

[← Part trước](part-00.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-02.md)
