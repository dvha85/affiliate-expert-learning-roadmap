# Mô hình học Build-First — Mission-first, Evidence-gated

## 1. Authority

Build-First là cách thực thi active curriculum trong [`../CURRICULUM.md`](../CURRICULUM.md).

```text
MỤC TIÊU, CORE, MISSION VÀ PASS BOUNDARY
= CURRICULUM.md

CHECKLIST / INDEX HIỆN HÀNH
= ROADMAP.md + roadmap/part-00.md ... part-06.md

VIỆC TIẾP THEO CẦN THỬ VÀ SHIP
= BUILD-FIRST.md + Mission hiện tại

HISTORICAL / RESEARCH INPUT
= sources/ và revision cũ, không phải active authority
```

Active structure hiện có 7 Parts, 21 Chapters, 63 Core micro-lessons và 12 Missions (`M00–M11`). Các con số này là inventory/authoring ceiling hiện tại, không phải invariant phải giữ nếu learner evidence cho thấy cần merge, bỏ hoặc đổi thứ tự.

## 2. Mission-first learning loop

```text
Attempt first trên target quan sát được
→ Run
→ Observe gap/failure
→ Pull tối đa ba micro-lessons
→ Improve implementation/decision
→ Test happy path + failure path
→ Operate trên real evidence hoặc sample được gắn nhãn
→ Measure
→ Compare human vs Bot/baseline
→ Explain back
→ Save technical + business evidence
→ Ship Bot capability tiếp theo
```

Learner phải có lý do cụ thể để cần một concept trước khi học sâu concept đó. Không yêu cầu đọc hết một Part rồi mới code hoặc ra thị trường.

## 3. Bốn thực thể tiến độ

### Mission

Đơn vị tiến độ chính. Mỗi Mission bắt đầu bằng attempt và theo dõi riêng Capability PASS, Reality verified và Operated.

### Core micro-lesson

Knowledge slice ngắn được kéo đúng lúc để sửa gap vừa quan sát. Lesson không phải tuyến tuần tự và không tự thay Mission evidence.

### Bot Version

Trạng thái sản phẩm sau một Mission. Bot Version mô tả capability/authority đã chứng minh, không phải điểm số learner.

### Milestone Gate

Bốn checkpoint tích hợp trên cùng một Bot:

- G1 — First Evidence-Backed Decision (`M00`);
- G2 — Trustworthy Intelligence (`M01–M02`);
- G3 — First Market Learning Loop (`M03–M05`);
- G4 — Governed Production Loop (`M06–M11`).

## 4. Ba chiều tiến độ độc lập

```text
CAPABILITY PASS
= working artifact + tests/failure case + explain-back

REALITY VERIFIED
= đúng cấp Real Evidence Ladder + provenance + timestamp + honest classification

OPERATED
= đủ cycle/window + failure/safety evidence theo Mission

MISSION DONE
= Capability PASS + Reality verified + Operated
```

Learner có thể tiếp tục engineering trong lúc chờ observation window nhưng Mission chưa `DONE`. Sample/synthetic record chỉ là E0; nó không thay observation, publication hay analytics thật.

Kết quả thị trường không cần dương. `zero`, `negative`, `inconclusive` và `not_yet_observable` đều hợp lệ nếu measurement trung thực; missing không được đổi thành zero.

## 5. Real Evidence Ladder

| Cấp | Evidence | Bắt đầu |
|---|---|---|
| E0 | sample/synthetic cho engineering test | pre-M00 |
| E1 | public observation có source/time | M00 |
| E2 | learner tự duyệt và publish thủ công | M03 |
| E3 | analytics/export thật | M04 |
| E4 | Decision → Action → Outcome → reviewed improvement | M05 |
| E5 | bounded governed canary | M10 |
| E6 | production closed-loop evidence | M11 |

Real evidence đến trước autonomy: Bot chưa được external execute trong lúc learner đang học cách thu thập, đánh giá và nối outcome.

## 6. Knowledge pull: Core / Advanced / Reference

### Core

Chỉ pull knowledge cần cho Mission hiện tại hoặc ngay kế tiếp, làm thay đổi artifact/decision và được áp dụng ngay.

### Advanced

Chỉ mở module khi real bottleneck/use case yêu cầu. ML, bandit, RAG, MCP/A2A/multi-agent, high-scale, paid traffic và SaaS không phải Core dependency.

### Reference

Glossary, Go/SQL/HTTP cookbook, schema, platform/legal current facts, provider matrix và deployment recipe không có PASS checkbox riêng. Learner tra cứu khi blocker xuất hiện.

Điểm quan trọng:

```text
REQUIRED FOR A MISSION ATTEMPT
≠
READ AN ENTIRE SUBJECT FIRST
```

## 7. Learner workspace và reference implementation

Người học trực tiếp build tại:

```text
lab/learner/affiliate-bot/
```

Bản triển khai tham chiếu:

```text
lab/affiliate-bot/
```

Reference không phải starting state.

```text
learner attempt
→ observe failure/gap
→ use hint ladder / pull knowledge
→ improve
→ reference chỉ để đối chiếu sau attempt hoặc khi blocker thật
```

Copy reference rồi chạy test xanh không thỏa Capability PASS hay explain-back.

## 8. Go-first theo đúng thời điểm

Go được học qua capability, không qua một khối syntax dài trước khi Bot chạy:

```text
M00: package/main/function, edit-run-test và output tối thiểu
M01: struct/JSON/error/validation, repository, snapshot và SQL tối thiểu
M02: provider-neutral interface, schema validation, fake provider và eval cases
M03: content artifact, disclosure/tracking metadata; human tự publish
M04: import/reconcile analytics, missing-vs-zero và historical update
M05: experiment record, versioned proposal, offline test và rollback
M06: context/schedule/concurrency, retry/backoff/idempotency và recovery
M07: Signal/Analysis/Decision contracts, freshness/confidence/abstain
M08: tool registry, read-only permission, validation và audit
M09: ActionIntent, durable approval, expiry và shadow execution
M10: policy executor, revalidation, bounded canary và kill switch
M11: deploy, observe, recover và outcome review
```

Khi learner gặp blocker nền tảng, dùng Reference cookbook hoặc hint thay vì chèn cả một Part lý thuyết vào trước Mission.

## 9. Practice-first không phải unsafe-first

```text
BUILD AND MEASURE EARLY
≠
GRANT BOT AUTHORITY EARLY
```

- M00–M02: observe/decide/advice, không Bot external action;
- M03: learner tự review và publish thủ công;
- M04–M08: analytics, improvement, watcher, decision và read-only tools;
- M09: shadow/dry-run + durable approval;
- M10: bounded RISK0/RISK1 canary; RISK2 vẫn approval;
- M11: production loop vẫn giữ policy, revalidation, idempotency, audit và kill switch.

Model confidence không bao giờ tự cấp permission.

## 10. Capacity và recalibration

Không hứa timeline chỉ từ content estimate. Theo dõi cho từng Mission:

- build/debug/operate/knowledge/retry hours;
- thời gian chờ observation window tách khỏi active effort;
- blocker, hint/reference đã dùng và dropout point;
- Capability PASS date, Reality verified date và Operated date riêng.

Estimate là forecast cho tới khi có ít nhất hai absolute beginners hoàn thành `M00–M04`. Sau pilot, được phép gộp/bỏ/đổi lesson hoặc Mission nếu evidence cho thấy learner flow tốt hơn; không hạ PASS criteria chỉ để khớp lịch.

## 11. Anti-patterns

Không:

- giữ lesson/Part chỉ để bảo toàn số lượng;
- biến knowledge inventory lịch sử thành prerequisite tuần tự;
- dạy nhiều tuần cú pháp Go trước Bot đầu tiên;
- gọi sample output là market validation;
- đưa AI trước deterministic baseline hoặc dùng AI claim không evidence làm fact;
- đưa external side effect có hậu quả vào Mission đầu để Bot trông “nâng cao”;
- mở reference solution trước attempt mà không có blocker;
- đánh dấu Mission `DONE` chỉ từ CI hoặc Capability PASS;
- tính cùng một artifact nhiều lần để tạo cảm giác tiến độ;
- cho outcome history tự sửa production prompt/policy/weights/code.

## 12. Trạng thái cuối mong muốn

```text
Tôi thử xây và chạy một Affiliate Intelligence Bot
→ Bot và thị trường làm lộ điều tôi chưa biết
→ Tôi kéo đúng knowledge slice
→ Tôi cải tiến rồi kiểm thử
→ Tôi vận hành với authority phù hợp
→ Evidence thật chứng minh điều gì tốt hơn, xấu hơn hoặc chưa kết luận được
→ Bot đề xuất cải tiến tiếp theo mà không tự vượt policy
```

Tiếng Việt là ngôn ngữ chính. English term được giữ khi cần độ chính xác và giải thích nghĩa khi quan trọng; xem [`LANGUAGE-POLICY.md`](LANGUAGE-POLICY.md).
