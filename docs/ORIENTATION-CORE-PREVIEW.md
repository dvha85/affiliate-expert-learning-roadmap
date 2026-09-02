# M00 Core Now / Preview

> **V2 migration note:** this preview is being replaced by O00, a safe
> synthetic end-to-end walkthrough with no PASS and no external side effect.
> Do not use it to move a learner past M00. The active sequence is in
> [`../CURRICULUM.md`](../CURRICULUM.md).

M00 không có orientation lecture riêng. Người học chạy starter Bot trước rồi kéo chín micro-lessons Part 0 qua ba cycle.

## Cycle 1 — Bot chạy và test thật

**Core now:** 0.1–0.3.

- chạy/sửa behavior;
- quan sát test failure;
- phân biệt software evidence với market evidence;
- lưu before/failure/change/after.

## Cycle 2 — Public evidence

**Core now:** 1.1–1.3.

- ghi 5 public observations;
- source, observed_at, access method;
- fact/estimate/assumption/unknown;
- provenance/freshness/missing.

## Cycle 3 — Decision đầu tiên

**Core now:** 2.1–2.3.

- human ranking trước Bot;
- deterministic baseline;
- Expected Value ở mức tối thiểu;
- reason/confidence/uncertainty;
- RANK_SCENARIO/RECOMMEND/GET_MORE_DATA/HUMAN_REVIEW; `WAIT` chỉ được chuẩn hóa ở DecisionPacket sau.

## Preview — nhận diện, chưa mastery

Người học chỉ cần biết các capability sẽ xuất hiện sau:

- M01: validation/history;
- M02: grounded AI/evaluation;
- M03–M05: publish thủ công, analytics và improvement;
- M06–M07: reliability/DecisionPacket;
- M08–M10: tools/policy/approval;
- M11: production/recovery/closed loop.

Không cần học MCP, durable workflow, observability, distributed system hoặc multi-agent trước M00. Preview không tạo quiz/PASS gate và không được dùng để trì hoãn public evidence đầu tiên.
