# Tiêu chuẩn author Mission

## 1. Mục đích

Mission là đơn vị **build + run + observe + improve + operate + evidence (xây + chạy + quan sát + cải tiến + vận hành + bằng chứng)**. Mission không thay thế canonical Lesson (Bài học chuẩn) hoặc canonical Project (Dự án chuẩn).

## 2. Đặt tên

```text
missions/M00-bot-boots.md
missions/M01-product-ingest.md
```

Mission ID dùng thứ tự `M00`, `M01`, ... và độc lập với Lesson ID.

## 3. Metadata bắt buộc

```yaml
mission_id: "M00"
title: "..."
status: planned|draft|ready
requires_missions: []
bot_version_from: null
bot_version_to: "v0.0"
estimated_hours: 2
knowledge:
  required: []
  on_demand: []
  reference: []
projects:
  contributes_to: []
risk_scope:
  external_side_effects: false
```

## 4. Semantics (ý nghĩa) của knowledge mapping

- `required`: Lesson ID mà learner phải hiểu **đủ phần liên quan** trước Mission PASS.
- `on_demand`: Lesson/concept chỉ pull khi implementation hoặc business context làm lộ nhu cầu.
- `reference`: kiến thức đào sâu, không phải Mission PASS gate.

Quy tắc:

```text
required knowledge for Mission
≠
full Lesson PASS
```

Mission `ready` phải chỉ rõ Lesson ID và knowledge slice (phần kiến thức cần ngay) trong nội dung Mission hoặc central map. Không được dùng `required: []` trong khi body lại nói có kiến thức bắt buộc mà không có canonical mapping.

Mission ↔ Knowledge mapping được quản lý tập trung; không bulk-edit 671 Lesson chỉ để thêm Mission metadata.

## 5. Các section bắt buộc khi `ready`

Để giữ compatibility (tương thích) với validator hiện tại, heading giữ English term và có nghĩa Việt đi kèm:

1. `## Ship Target — Mục tiêu bàn giao`
2. `## Starting Bot State — Trạng thái Bot ban đầu`
3. `## Build First — Xây trước`
4. `## Run — Chạy`
5. `## Observe — Quan sát`
6. `## Knowledge Pull — Lấy kiến thức đúng lúc`
7. `## Improve — Cải tiến`
8. `## Tests — Kiểm thử`
9. `## Operate — Vận hành`
10. `## Failure Case — Tình huống lỗi`
11. `## Evidence — Bằng chứng`
12. `## Explain-back — Giải thích lại`
13. `## Mission PASS — Tiêu chí PASS`
14. `## Bot Version Result — Kết quả phiên bản Bot`
15. `## Next Mission — Mission tiếp theo`

## 6. Quy tắc Build-First

Mission phải đưa learner tới **smallest runnable implementation (phần triển khai nhỏ nhất chạy được)** trước khi có block theory dài. Knowledge được đưa vào vì learner vừa gặp một decision, failure, measurement hoặc design gap cụ thể.

## 7. Learner workspace và reference implementation

Learner build trên workspace riêng. Reference implementation (bản triển khai tham chiếu) không được coi là Starting Bot State của learner.

Với bootstrap hiện tại:

```text
learner workspace:   lab/learner/affiliate-bot/
reference v0.3:      lab/affiliate-bot/
```

Mission phải hướng learner tự thêm capability theo sequence. Reference chỉ dùng để:

- đối chiếu sau một attempt;
- unblock (gỡ kẹt) khi learner đã thử và có evidence về blocker;
- review implementation sau khi feature đã chạy.

Không dùng reference để copy lời giải rồi đánh dấu PASS.

## 8. Tests (kiểm thử) và operation (vận hành)

Độ sâu testing tăng theo scope Mission. Mission đầu có thể chỉ cần unit/behavior test. Mission sau thêm integration, restart/recovery, idempotency, security, policy và approval test khi thực sự cần.

Mọi Mission phải có ít nhất một Failure Case cụ thể.

## 9. Evidence (bằng chứng)

Evidence phải inspectable (có thể kiểm tra), có thể gồm:

- code path + commit SHA;
- test output;
- sample data/output;
- kết quả before/after;
- logs/metrics;
- decision note (ghi chú quyết định);
- screenshot/link khi cần.

Không copy lại cả codebase vào artifact chỉ để tạo thêm evidence.

## 10. Đóng góp vào Project

`projects.contributes_to` chỉ được tham chiếu canonical Projects 1–14. Contribution (đóng góp) không tự động đánh dấu Project PASS.

Central Bot Evolution map và Mission frontmatter phải thống nhất về Project contribution.

## 11. Safety (an toàn)

Mission phải nêu rõ có external side effect (tác động bên ngoài) hay không.

```text
BUILD CODE EARLY (viết code sớm)
≠
AUTOMATE REAL BUSINESS EARLY (tự động hóa kinh doanh thật sớm)
```

Consequential side effect (tác động có hậu quả đáng kể) phải có deterministic policy/risk/approval control phù hợp ở stage được đưa vào.

## 12. Authoring Definition of Done (định nghĩa hoàn tất authoring)

Một Mission chỉ được `ready` khi:

- metadata hợp lệ;
- ship target có thể quan sát;
- starting state có thể tái lập từ learner path/previous learner Mission;
- commands/steps có thể chạy hoặc design-only có lý do rõ;
- required knowledge mapping explicit bằng canonical Lesson ID;
- knowledge slice đủ cụ thể để learner không phải học cả chương không cần thiết;
- tests + failure case tồn tại;
- evidence path được định nghĩa;
- PASS criteria đo được;
- Project contribution đồng bộ với central map;
- Mission không tự thay Lesson PASS;
- committed material không cần secret/credential;
- nội dung tuân thủ [`LANGUAGE-POLICY.md`](LANGUAGE-POLICY.md).