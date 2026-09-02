# Phần 0 — Quyết định đầu tiên dựa trên bằng chứng

> **V1 inventory/reference detail.** In canonical v2, P0 supports M00 First
> Safe Market Loop (human-only E1→E2). The Bot-first wording and M00 file links
> below are not a new learner's execution order; remapping is tracked in
> [`../docs/CURRICULUM-MIGRATION-v2.md`](../docs/CURRICULUM-MIGRATION-v2.md).

- Timeline: **Evidence-gated; recalibrate after learner pilot**.
- **Chapters:** C0–C2
- **Core:** 9 micro-lessons
- **Mission:** M00
- **Outcome:** Bot chạy được, đọc evidence thật và tạo quyết định đầu tiên có thể giải thích.

## Cách dùng Part 00

Part 00 là một Mission-first learning flow, không phải một reading list phải đọc hết trước khi làm.

```text
attempt
→ observe a concrete gap
→ pull 1–3 micro-lessons
→ apply ngay vào artifact vừa chạy
→ test / failure case
→ lưu evidence
```

`estimated_minutes` trong lesson là **ngân sách tối đa cho một lượt học sâu + practice/remediation của lesson**, không phải thời gian bắt buộc phải đọc liên tục và cũng không được cộng cơ học vào `M00 estimated_hours` như một workload riêng. Fast path là chỉ kéo phần kiến thức giải quyết gap hiện tại; phần giải thích sâu dùng khi learner bị chặn hoặc cần remediation.

Mục tiêu vẫn là khoảng **15% knowledge pull / 85% build-run-measure-improve** ở cấp chương trình.

## Attempt trước knowledge pull

1. M00 cycle 1: chạy starter Bot, tự sửa một behavior, làm test fail rồi khôi phục PASS.
2. M00 cycle 2: quan sát 5 sản phẩm công khai và ghi source/time trước khi thiết kế “schema hoàn hảo”.
3. M00 cycle 3: human rank trước, chạy naive Bot ranking sau và giữ agreement/disagreement + information gap làm evidence.

## Contract clarification cho M00

### Evidence taxonomy vs serialized enum

Bài 0.2 dùng taxonomy khái niệm rộng:

```text
real | test | synthetic | replay
```

để phân biệt nguồn gốc/vai trò của evidence.

Nhưng **M00 JSON schema hiện chỉ serialize**:

```text
evidence_kind: real | synthetic
```

`test` và `replay` ở Part 00 là cách mô tả role/use context, **không phải legal enum value của `evidence_kind` trong learner Bot M00**. Không thêm enum mới chỉ để khớp taxonomy khái niệm.

### Raw Bot, HumanPrediction và final Decision là ba artifact khác nhau

Giữ separation sau:

```text
HumanPrediction
- được freeze trước khi xem Bot ranking

Raw Bot output
- chỉ phụ thuộc evidence input + code/formula version
- không cần nhận human ranking làm scoring input

Final reviewed Decision artifact
- reference HumanPrediction
- reference raw Bot output
- thêm reason / confidence / uncertainty / missing evidence / next measurement
```

`human_ranking_ref` thuộc evidence/decision bundle để chứng minh human-first, không được dùng để làm Bot ranking “khớp người”.

### Finalization của M00

Không đổi starter thành `v0.1` chỉ vì đã học xong Bài 2.3. Trình tự đúng là:

```text
Capability PASS
+ Reality verified E1
+ Operated
→ freeze M00 evidence bundle
→ final reviewed Decision artifact
→ pre-v0.1 → v0.1
```

Nếu một gate còn pending, learner có thể tiếp tục phần engineering phù hợp nhưng không được tuyên bố M00 DONE hoặc Reality verified.

## Core checklist

### Chương 0 — Bot đầu tiên và evidence discipline

- [ ] **0.1** — [Chạy, sửa và kiểm thử Bot đầu tiên](../lessons/part-00/chapter-00/0.1-chay-sua-va-kiem-thu-bot-dau-tien.md)
- [ ] **0.2** — [Phân biệt loại bằng chứng và loại khẳng định](../lessons/part-00/chapter-00/0.2-sample-real-fact-estimate-assumption-unknown.md)
- [ ] **0.3** — [Observe failure, lưu evidence và explain-back](../lessons/part-00/chapter-00/0.3-observe-failure-evidence-explain-back.md)

### Chương 1 — Quan sát Affiliate thật đầu tiên

- [ ] **1.1** — [Ghi 5 product observations với source và observed_at](../lessons/part-00/chapter-01/1.1-ghi-nam-product-observations.md)
- [ ] **1.2** — [Actors, money flow, commission, validation và refund](../lessons/part-00/chapter-01/1.2-actors-money-flow-commission-refund.md)
- [ ] **1.3** — [Provenance, freshness, missing field và giới hạn kết luận](../lessons/part-00/chapter-01/1.3-provenance-freshness-missing-limits.md)

### Chương 2 — Human-vs-Bot decision đầu tiên

- [ ] **2.1** — [Human ranking trước code: reason, strongest evidence và weakest assumption](../lessons/part-00/chapter-02/2.1-human-ranking-truoc-code.md)
- [ ] **2.2** — [Naive score, Expected Value và before/after comparison](../lessons/part-00/chapter-02/2.2-naive-score-expected-value-before-after.md)
- [ ] **2.3** — [Explainable decision, confidence, uncertainty và abstain](../lessons/part-00/chapter-02/2.3-explainable-decision-confidence-uncertainty-abstain.md)

## Part PASS

- [ ] M00 có Capability PASS, Reality verified cấp E1 và Operated
- [ ] Không dùng sample/synthetic record để tuyên bố market truth
- [ ] Có human-vs-Bot comparison truy được về frozen HumanPrediction và raw Bot baseline
- [ ] Nếu có disagreement, disagreement được giữ và giải thích; **không manufacture disagreement để PASS**
- [ ] Nếu không có disagreement, giải thích ít nhất một agreement và một shared missing-evidence/information gap mà cả human lẫn Bot chưa giải quyết được
- [ ] Final reviewed Decision có reason, confidence/reason, uncertainty/missing evidence và next measurement
- [ ] Learner nói được điều Bot biết, không biết và chưa được phép làm
- [ ] M00 vẫn giữ S0: public/manual read + local deterministic compute; không có external side effect

[← Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-01.md)
