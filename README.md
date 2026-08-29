# Affiliate Intelligence Bot — Learning Roadmap

Chương trình dành cho người mới xây **một Affiliate Intelligence Bot tiến hóa dần từ quyết định dựa trên bằng chứng tới tự động hóa có kiểm soát**.

## Bắt đầu trong 5 phút

Chưa cần đọc hết curriculum. Trước khi chạy starter, kiểm tra workstation và chắc chắn terminal đang đứng trong đúng repo:

~~~bash
git --version
go version
git rev-parse --show-toplevel
test -f lab/learner/affiliate-bot/go.mod
~~~

Nếu `go version` báo `command not found`, hoặc `git rev-parse` / `test -f` fail, **chưa chạy lệnh Bot tiếp**. Sửa environment/repo path trước; đây là preflight, không phải lesson hay PASS gate.

Khi bốn lệnh trên đều ổn:

~~~bash
cd lab/learner/affiliate-bot
go env GOMOD
go run ./cmd/bot
go test ./...
~~~

Bạn phải thấy `Bot version: pre-v0.1` và `Decision state: RANK_SCENARIO`. Sau đó mở [Mission M00](missions/M00-first-evidence-backed-decision.md), thực hiện Checkpoint 1 và chỉ kéo micro-lesson khi đã thấy một gap/failure cụ thể. Nếu bị chặn, dùng [Hint ladder M00](lab/learner/affiliate-bot/HINTS-M00.md) từng mức.

Nếu bạn chưa truy cập được public product evidence thật, ghi blocker là `BLOCKED_EXTERNAL`/pending và tiếp tục phần engineering có thể làm bằng sample. **Không đổi sample thành “real” chỉ để vượt gate.**

Sau lần chạy đầu, dùng [canonical curriculum](CURRICULUM.md) để hiểu outcome/ranh giới, [Build-First](BUILD-FIRST.md) để hiểu execution model và [Progress](PROGRESS.md) để lưu tiến độ.

~~~text
TRY ON REAL EVIDENCE
→ RUN / OBSERVE
→ PULL 1–3 KNOWLEDGE SLICES
→ IMPROVE / TEST
→ COMPARE HUMAN VS BOT
→ SAVE EVIDENCE
→ SHIP NEXT BOT VERSION
~~~

## Cấu trúc active

- **Active canonical:** [CURRICULUM.md](CURRICULUM.md).
- **Execution spine:** 12 Mission, M00–M11.
- **Core knowledge:** 7 Part · 21 Chapter · 63 micro-lesson.
- **Milestone:** 4 gate trên cùng một Bot, không phải nhiều project rời.
- **Advanced:** chỉ mở khi bottleneck thực tế yêu cầu.
- **Historical/reference:** các file trong sources/ và revision cũ không còn quyết định cấu trúc active.

Số lượng 7/21/63 là inventory hiện tại, **không phải invariant cần bảo vệ**. Curriculum được phép giảm, gộp hoặc thay đổi khi learner evidence chứng minh cấu trúc khác tốt hơn.

## “Thông minh” và “tự động” nghĩa là gì?

Bot thông minh không đồng nghĩa “gọi LLM”. Bot phải:

- dùng evidence có nguồn và thời điểm;
- phân biệt fact, estimate, assumption, unknown;
- có deterministic baseline trước AI;
- biết confidence/uncertainty và biết abstain;
- nối Decision → Action → Outcome → Evaluation;
- đề xuất cải tiến nhưng không tự sửa production behavior âm thầm.

Authority tăng theo gate:

~~~text
A0 deterministic decision
→ A1 grounded AI advisory
→ A2 read-only tool agent
→ A3 shadow/approval
→ limited governed automation
~~~

Public publish, spend, account change, delete và consequential communication luôn đi qua policy/risk/approval phù hợp.

## Thực tế xuất hiện khi nào?

- M00: quan sát sản phẩm công khai và human-vs-bot comparison.
- M01: snapshot thật lần hai.
- M02: AI đọc evidence công khai thật.
- M03: người học tự duyệt và publish một nội dung có tracking.
- M04: analytics thật; giá trị 0 vẫn là outcome hợp lệ.
- M05: vòng cải tiến thị trường đầu tiên.
- M06+: tự động quan sát read-only, rồi mới tăng authority.

Order/revenue không phải điều kiện PASS vì nằm ngoài quyền kiểm soát. Integrity của measurement mới là gate.

## Workspace

~~~text
lab/learner/affiliate-bot/   # nơi người học tự build
lab/affiliate-bot/           # reference để đối chiếu sau attempt
~~~

Không copy reference rồi coi là PASS.

## Trạng thái hiện tại

Đây là clean-slate curriculum revision. Người học chưa bắt đầu; [Progress](PROGRESS.md) vẫn ở M00.

- M00 và 9 micro-lesson Part 0: `ready`;
- M01–M03: Mission draft để review sau learner evidence;
- M04–M11 và lesson Part 1–6: planned inventory, chưa giả vờ là nội dung sẵn sàng học.

Việc author dần là có chủ đích: pilot M00 trước, dùng actual blocker/time/evidence để gộp, bỏ hoặc sửa các lesson sau. Authoring readiness được theo dõi tách biệt với learner progress.

## Kiểm tra repository

~~~bash
python scripts/validate_curriculum.py
python scripts/validate_authority.py
python scripts/validate_hardening.py
python scripts/validate_build_first.py
python scripts/validate_agentic_architecture.py
python -m unittest discover -s tests -v
~~~

Go checks cho cả learner và reference workspace vẫn là merge gate.
