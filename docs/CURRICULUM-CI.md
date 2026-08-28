# Curriculum CI — Hệ thống kiểm tra curriculum

Curriculum CI bảo vệ đồng thời **canonical curriculum (curriculum chuẩn)**, provenance/freshness (nguồn gốc/độ mới), Build-First execution semantics (ngữ nghĩa thực thi), learner/reference code và các invariant (bất biến) quan trọng.

Tiếng Việt là ngôn ngữ chính thức của tài liệu. English term được giữ cho tên code, error code, công nghệ và thuật ngữ kỹ thuật khi cần. Xem [`LANGUAGE-POLICY.md`](LANGUAGE-POLICY.md).

## 1. Chạy kiểm tra local

Từ root repository:

```bash
python scripts/validate_curriculum.py
python scripts/validate_hardening.py
python scripts/validate_build_first.py
python -m unittest discover -s tests -v
```

Reference Bot:

```bash
cd lab/affiliate-bot
test -z "$(gofmt -l .)"
go vet ./...
go test ./...
```

Learner Bot:

```bash
cd lab/learner/affiliate-bot
test -z "$(gofmt -l .)"
go vet ./...
go test ./...
```

Exit code `0` nghĩa là gate tương ứng PASS.

## 2. Layer 1 — Canonical curriculum validator

`scripts/validate_curriculum.py` bảo vệ:

- active canonical v2026.09 + historical v2026.08;
- 23 Parts / 89 Chapters / 671 lessons;
- Go-first Part 15 direction;
- timeline metadata;
- Lesson ID, metadata, lifecycle và headings;
- relative links;
- freshness metadata contract.

Các nhóm lỗi tiêu biểu: `CANON*`, `TECH*`, `ROADMAP*`, `COUNT*`, `TIME*`, `ID*`, `LINK*`, `META*`, `FRESH*`, `STATE*`, `HEAD*`.

## 3. Layer 2 — Curriculum integrity hardening validator

`scripts/validate_hardening.py` bảo vệ:

- external source IDs đối chiếu Affiliate + Bot source registers;
- normalized provenance authority;
- đúng 671 Lesson / 89 Chapter;
- canonical Project 1–14 và vị trí Part;
- authority-document consistency.

Layer này ngăn Build-First làm yếu source/provenance rules đã được harden trước migration.

## 4. Layer 3 — Build-First semantic validator

`scripts/validate_build_first.py` bảo vệ execution architecture mà không định nghĩa lại canonical syllabus.

### BUILD001 — Authority files

Bắt buộc có:

- `BUILD-FIRST.md`;
- `docs/BUILD-FIRST-LEARNING-MODEL.md`;
- `docs/MISSION-AUTHORING-STANDARD.md`;
- `docs/MISSION-PASS-CRITERIA.md`;
- `docs/BOT-EVOLUTION-ROADMAP.md`;
- `docs/MISSION-KNOWLEDGE-MAP.md`;
- `docs/LANGUAGE-POLICY.md`.

### BUILD002 — Mission identity

Mission ID phải hợp lệ/unique và filename đã author phải bắt đầu bằng chính `MXX-` của nó.

### BUILD003 — Mission sequence

Product roadmap phải có đúng `M00` → `M15` theo thứ tự.

Authored Mission files chỉ được tạo thành một **contiguous prefix (prefix liên tục)** bắt đầu từ `M00`. Hiện M00–M03 đã `ready`; M04–M15 vẫn là roadmap target cho tới khi author thật.

### BUILD004 — Knowledge mapping

- explicit Lesson ID trong Mission knowledge metadata phải resolve trong canonical 671 inventory;
- Mission `ready` phải có ít nhất một canonical Lesson ID trong `knowledge.required`;
- `required knowledge for Mission ≠ full Lesson PASS` vẫn được giữ: CI chỉ yêu cầu mapping rõ, không tự đánh dấu Lesson PASS.

### BUILD005 — Dependency graph

Mission dependency phải:

- trỏ về Mission trước;
- tồn tại trong authored prefix;
- không tạo cycle (chu trình vòng).

### BUILD006 — Bot Version progression

Bot Version trong M00–M15 roadmap phải tăng nghiêm ngặt. `bot_version_to` của authored Mission phải khớp roadmap target.

### BUILD007 — Ready Mission contract

Mọi Mission `status: ready` phải chứa các section:

```text
Ship Target — Mục tiêu bàn giao
Starting Bot State — Trạng thái Bot ban đầu
Build First — Xây trước
Run — Chạy
Observe — Quan sát
Knowledge Pull — Lấy kiến thức đúng lúc
Improve — Cải tiến
Tests — Kiểm thử
Operate — Vận hành
Failure Case — Tình huống lỗi
Evidence — Bằng chứng
Explain-back — Giải thích lại
Mission PASS — Tiêu chí PASS
Bot Version Result — Kết quả phiên bản Bot
Next Mission — Mission tiếp theo
```

English heading prefix được giữ để validator/code contract ổn định; nội dung giải thích vẫn dùng tiếng Việt.

### BUILD008 — Learner-state separation

Mission không được chứa cơ chế tự tuyên bố canonical Lesson PASS.

```text
Mission PASS ≠ Lesson PASS
```

### BUILD009 — Canonical Projects only

`projects.contributes_to` chỉ được tham chiếu Project 1–14. Mission ID không tạo Project 15+.

### BUILD010 — Learner + reference bootstrap files

CI yêu cầu cả hai workspace tối thiểu tồn tại:

```text
lab/affiliate-bot/                 reference implementation
lab/learner/affiliate-bot/         learner workspace
```

Điều này ngăn tài liệu tuyên bố Build-First runnable trong khi một trong hai code path bị mất.

### BUILD011 — Learner/reference separation + capability ceiling

Bootstrap Mission M00–M03 phải chỉ rõ learner workspace và không được dùng `cd lab/affiliate-bot` làm Run/Build path.

Validator còn đọc **Current Mission** từ `PROGRESS.md` để áp capability ceiling (trần năng lực) cho learner workspace:

```text
Current M00 → chưa được có Product ingest / store / ranking
Current M01 → được có Product ingest; chưa được có store / ranking
Current M02 → được có ingest + store; chưa được có ranking
Current M03 → được có ranking
```

Nhờ đó starter không leak lời giải của Mission sau, nhưng learner workspace vẫn được phép tiến hóa khi `PROGRESS.md` chuyển Mission.

### BUILD012 — Bot Version continuity

- M00 phải có `bot_version_from: null`;
- Mission sau phải có `bot_version_from` đúng bằng `bot_version_to` của Mission ngay trước.

Ví dụ:

```text
M00 to v0.0
M01 from v0.0 → to v0.1
M02 from v0.1 → to v0.2
```

### BUILD013 — Project map consistency

`projects.contributes_to` trong Mission frontmatter phải khớp central mapping tại `docs/BOT-EVOLUTION-ROADMAP.md`.

Guard này ngăn drift kiểu Mission nói đóng góp Project 4 nhưng central roadmap quên ghi.

### BUILD014 — Go runtime consistency

Go directive của learner và reference module phải cùng một line.

CI không hard-code vĩnh viễn `1.27`; current Go version vẫn thuộc freshness process. Guard chỉ ngăn learner/reference vô tình chạy hai runtime line khác nhau.

### LANG001 — Language Policy authority

- `docs/LANGUAGE-POLICY.md` phải tuyên bố tiếng Việt là ngôn ngữ chính thức;
- các authority docs cốt lõi phải tham chiếu Language Policy.

Guard này **không** dùng tỷ lệ từ tiếng Việt/tiếng Anh máy móc, vì code block, API name và technical term cần được giữ tiếng Anh chính xác.

## 5. Executable Go gates

GitHub Actions chạy cho **cả reference và learner modules**:

```text
gofmt check
→ go vet ./...
→ go test ./...
```

Reference Bot chứng minh curriculum có một implementation chạy/test được để đối chiếu.

Learner Bot chứng minh active learner workspace không bị hỏng khi người học tiến hóa qua Mission.

Fast CI hiện **không** bắt buộc PostgreSQL service. M02 dạy persistence boundary + migration contract, còn fast tests dùng in-memory Repository. Integration infrastructure chỉ thêm khi operational value đủ lớn.

## 6. Regression / mutation tests

`tests/test_build_first_validator.py` bảo vệ ít nhất:

- current repo sạch;
- authority file bị thiếu;
- M00–M15 sequence bị hỏng;
- Bot Version đi lùi;
- unknown Lesson ref;
- forward dependency;
- dependency trỏ tới authored Mission không tồn tại;
- ready Mission thiếu section;
- ready Mission thiếu required canonical knowledge;
- lesson-PASS mutation mechanism;
- Project 15 reference;
- `bot_version_from` không nối tiếp version trước;
- central Project map lệch Mission frontmatter;
- bootstrap Mission không dùng learner workspace;
- learner/reference Go directive lệch nhau;
- current learner workspace vượt capability ceiling;
- Language Policy marker/reference bị mất.

Các regression tests của curriculum/hardening/scaffolder trước đó tiếp tục chạy.

## 7. GitHub Actions merge rule

Workflow `.github/workflows/curriculum-ci.yml` chạy với mọi Pull Request và mọi push vào `main`.

```text
canonical validator
→ hardening validator
→ Build-First semantic validator
→ Python regression tests
→ reference: gofmt + vet + test
→ learner:   gofmt + vet + test
```

**Quy tắc quy trình:** không merge khi bất kỳ gate nào fail.

Để GitHub tự cưỡng chế quy tắc này ở cấp repository, branch protection/ruleset của `main` cần require Pull Request và required status check tương ứng. Xem [`REPOSITORY-GOVERNANCE.md`](REPOSITORY-GOVERNANCE.md).

## 8. State rule — CI không phải learner PASS

CI chỉ xác minh cấu trúc/code/invariant của repository.

```text
CI PASS
≠
Mission PASS
≠
Lesson PASS
≠
Project PASS
```

Không được dùng một GitHub Actions run xanh để tự cập nhật learner achievement.