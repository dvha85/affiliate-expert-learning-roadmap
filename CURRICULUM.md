# Chương trình — Affiliate Intelligence Bot hướng kết quả

**Trạng thái:** Chương trình chuẩn đang áp dụng (`active canonical curriculum`)

**Đối tượng:** Người mới bắt đầu, kể cả người chưa từng lập trình

**Sản phẩm xuyên suốt:** Một Affiliate Intelligence Bot (Bot phân tích và hỗ trợ quyết định Affiliate) tiến hóa qua 12 Mission

**Cấu trúc Core (cốt lõi):** 7 Parts · 21 Chapters · 63 micro-lessons

**Tỷ lệ mục tiêu:** khoảng 15% kéo kiến thức (`knowledge pull`) · 85% xây, chạy, đo và cải tiến

Tổng cộng: **7 phần · 21 chương · 63 bài học**.

> Curriculum này thay thế cấu trúc 23 Parts / 89 Chapters / 671 lessons làm nguồn thực thi chính.
> `sources/SYLLABUS-v2026.08.md` và `sources/SYLLABUS-v2026.09.md` chỉ còn là nguồn lịch sử/nghiên cứu, không phải active authority.
> 63 là inventory outcome/knowledge hiện tại, không có nghĩa 63 lesson file đều đã `ready`. M00/Part 0 được biên soạn trước; phần sau chỉ lên `ready` sau review và bằng chứng từ người học.

## 1. Mục tiêu đầu ra

Người hoàn thành Core phải chứng minh bằng artifact (sản phẩm tạo ra) và evidence (bằng chứng) rằng họ có thể:

1. quan sát một workflow Affiliate thật và phân biệt `fact` (sự thật), `estimate` (ước lượng), `assumption` (giả định), `unknown` (chưa biết);
2. xây Bot Go đọc, kiểm tra, lưu lịch sử và theo dõi dữ liệu sản phẩm;
3. xếp hạng cơ hội bằng đường cơ sở tất định (`deterministic baseline`) có giải thích, confidence (độ tin cậy) và khả năng abstain (từ chối quyết định khi chưa đủ bằng chứng);
4. tự xuất bản thủ công nội dung đúng disclosure (công bố quan hệ Affiliate), gắn tracking (theo dõi đo lường) và thu outcome (kết quả quan sát được) thật;
5. liên kết `Decision → Action → Outcome → Evaluation` (Quyết định → Hành động → Kết quả → Đánh giá);
6. chạy thí nghiệm nhỏ và chấp nhận kết quả `inconclusive` (chưa đủ bằng chứng để kết luận);
7. thêm AI advisory (AI tư vấn) có grounding (căn cứ bằng chứng), schema validation, evaluation và deterministic fallback (phương án dự phòng tất định);
8. cho agent thu thập bằng chứng qua tool chỉ-đọc (`read-only`) có permission và audit rõ;
9. tự động hóa hành động rủi ro thấp và bắt buộc approval (phê duyệt) cho hành động có hậu quả;
10. deploy, monitor, recover, dùng kill switch và tạo proposed improvement từ outcome mà không để Bot tự sửa production policy, prompt hoặc weights.

### Hợp đồng câu trả lời của Affiliate Intelligence Bot

Để curriculum không trôi thành khóa agent/automation chung chung, một Bot trưởng thành phải hỗ trợ quyết định có bằng chứng cho các câu hỏi domain sau:

```text
Product/Offer (sản phẩm/ưu đãi) nào?
Tại sao?
Audience/Problem (nhóm người/vấn đề) nào?
Content Angle (góc nội dung) nào?
Hook / CTA (câu mở / lời kêu gọi hành động) nào?
Channel (kênh) nào?
Timing / observation window (thời điểm / cửa sổ quan sát) nào?
Expected Value / expected affiliate revenue (giá trị kỳ vọng / doanh thu kỳ vọng) bao nhiêu?
Evidence refs nào hỗ trợ?
Confidence theo method/reason nào?
Uncertainty / missing evidence là gì?
Compliance / business risk là gì?
Recommended state: ACT / WAIT / GET_MORE_DATA / HUMAN_REVIEW / DENY?
Next measurement / experiment là gì?
```

Đây là **hợp đồng tích lũy (`cumulative contract`)**. Mission sớm chỉ điền field đã có evidence; field chưa đủ phải giữ `unknown`, `not_yet_observable` hoặc abstain. Không được bịa audience, CVR, expected revenue, risk hoặc recommendation để làm output trông đầy đủ.

Ý nghĩa field chuẩn, các tín hiệu cơ hội sản phẩm và mức trưởng thành M00→M11 nằm tại [`docs/AFFILIATE-INTELLIGENCE-DECISION-CONTRACT.md`](docs/AFFILIATE-INTELLIGENCE-DECISION-CONTRACT.md).

Nguyên tắc xuyên suốt:

> **DATA > OPINION — Dữ liệu quan trọng hơn ý kiến.**
>
> **EXPECTED VALUE > COMMISSION RATE — Giá trị kỳ vọng quan trọng hơn tỷ lệ hoa hồng đơn lẻ.**

## 2. Mission-first — mô hình học bắt buộc

Mỗi Mission đi theo cùng một vòng lặp:

```text
TỰ THỬ TRƯỚC
→ CHẠY
→ QUAN SÁT MỘT GAP CỤ THỂ
→ KÉO TỐI ĐA 1–3 MICRO-LESSON MỖI LẦN
→ CẢI TIẾN
→ TEST HAPPY PATH VÀ FAILURE PATH
→ VẬN HÀNH TRÊN DỮ LIỆU THẬT HOẶC SAMPLE ĐƯỢC GẮN NHÃN RÕ
→ LƯU BẰNG CHỨNG KỸ THUẬT + KINH DOANH
→ GIẢI THÍCH LẠI
→ PHÁT HÀNH NĂNG LỰC BOT TIẾP THEO
```

Không yêu cầu người học đọc hết một Part rồi mới được build. Lesson là mảnh kiến thức được kéo đúng lúc; evidence của Mission mới là đơn vị tiến độ chính.

### Ba chiều tiến độ độc lập

Mỗi Mission theo dõi riêng:

- **Capability PASS (đạt năng lực):** artifact chạy được, test/failure case đạt và người học giải thích được implementation;
- **Reality verified (thực tế đã kiểm chứng):** evidence đúng cấp, có provenance/timestamp và không đánh tráo sample thành dữ liệu thật;
- **Operated (đã vận hành):** capability đã chạy qua số cycle, failure/recovery case và safety gate mà Mission yêu cầu.

Mission chỉ `DONE` khi cả ba chiều bắt buộc đều đạt. Người học có thể tiếp tục phần engineering trong lúc chờ observation window, nhưng không được tuyên bố Reality đã verified hoặc Mission đã DONE.

## 3. Thang bằng chứng thực tế (`Real Evidence Ladder`)

| Cấp | Bằng chứng | Mission đầu tiên |
|---|---|---|
| E0 | Sample/synthetic, chỉ dùng cho engineering test | bộ khung pre-M00 |
| E1 | Quan sát nguồn công khai thật, có source và thời gian | M00 |
| E2 | Hành động thật do người thực hiện: nội dung được publish thủ công | M03 |
| E3 | Analytics/export thật: impression/click/order, kể cả giá trị `0` | M04 |
| E4 | Decision → Action → Outcome và cải tiến đã review liên kết được | M05 |
| E5 | Canary giới hạn có quản trị, có policy, audit và kill-switch evidence | M10 |
| E6 | Bằng chứng vòng production khép kín | M11 |

Quy tắc:

- sample data không thể thỏa business-evidence gate;
- không có conversion không phải là FAIL;
- `0` chỉ hợp lệ khi source thật báo `0`; missing data không được đổi thành `0`;
- external publish ban đầu luôn do con người thực hiện;
- outcome có thể `positive`, `negative`, `zero`, `inconclusive` hoặc `not_yet_observable`;
- Bot không tự tăng authority chỉ vì model confidence cao.

## 4. Cấu trúc Core

| Part | Chương | Bài Core | Mission | Kết quả năng lực |
|---|---:|---:|---|---|
| [P0 — Quyết định đầu tiên dựa trên bằng chứng](roadmap/part-00.md) | C0–C2 | 9 | M00 | Bot chạy được, dùng evidence thật và tạo quyết định đầu tiên |
| [P1 — Dữ liệu đáng tin và AI có grounding](roadmap/part-01.md) | C3–C5 | 9 | M01–M02 | History dữ liệu đáng tin cậy và AI advisory có grounding/fallback |
| [P2 — Vòng thị trường có tracking đầu tiên](roadmap/part-02.md) | C6–C8 | 9 | M03–M04 | Nội dung thật, tracking thật và so sánh outcome người với AI |
| [P3 — Cải tiến dựa trên outcome](roadmap/part-03.md) | C9–C11 | 9 | M05 | Một thay đổi có hypothesis, outcome và rollback path |
| [P4 — Intelligence và quyết định đáng tin cậy](roadmap/part-04.md) | C12–C14 | 9 | M06–M07 | Dịch vụ signal-to-decision đáng tin có evaluation |
| [P5 — Tool Agent và tự động hóa có quản trị](roadmap/part-05.md) | C15–C17 | 9 | M08–M10 | Agent dùng tool chỉ-đọc và workflow hành động có quản trị |
| [P6 — Vòng production khép kín](roadmap/part-06.md) | C18–C20 | 9 | M11 | Bot production có recovery, safety và vòng học từ outcome |

## 5. Trục Mission và kéo kiến thức

| Mission | Mục tiêu thử/phát hành | Kiến thức kéo vào |
|---|---|---|
| M00 — Quyết định đầu tiên dựa trên bằng chứng | Chạy Bot, thu 5 public observations, người xếp hạng trước và giải thích Bot ranking | 0.1–2.3, theo ba vòng attempt/pull |
| M01 — History đáng tin cậy | Tự build ingest/validation, lưu ít nhất hai snapshot thật và phát hiện thay đổi | 3.1–4.3 |
| M02 — AI Advisor có grounding | Thêm AI advisory trên deterministic baseline; invalid AI output phải fallback | 5.1–5.3 |
| M03 — Người publish nội dung có tracking | Người học tự duyệt và publish một micro-content có disclosure/tracking | 6.1–7.1 |
| M04 — Phân tích outcome thật | Import outcome thật, reconcile và so human baseline với AI-assisted variant | 7.2–8.3 |
| M05 — Cải tiến thật đầu tiên | Chạy một experiment; tạo proposed change, offline test, review và version mới | 9.1–11.3 |
| M06 — Watcher tự động đáng tin cậy | Watcher/alert chạy được qua retry, duplicate và recovery case | 12.1–12.3 |
| M07 — Quyết định và abstention | `DecisionPacket` xử lý đúng stale, missing và conflicting evidence | 13.1–14.3 |
| M08 — Agent thu evidence chỉ-đọc | Agent dùng explicit tools để lấy missing evidence, không có external side effect | 15.1–15.3 |
| M09 — Hành động chạy bóng và approval | Tạo `ActionIntent`, durable approval và shadow/dry-run execution | 16.1–16.3, 17.1 |
| M10 — Tự động hóa giới hạn có quản trị | Chạy bounded RISK0/RISK1 canary; RISK2 vẫn cần durable approval | 17.2–17.3, reuse C16 |
| M11 — Vòng production khép kín | Deploy, chạy qua observation window, recovery drill và outcome review | 18.1–20.3 |

Mỗi Mission phải làm trưởng thành thêm một phần của Affiliate Intelligence Decision Contract; automation capability không được thay thế domain reasoning. Mission file phải đưa người học tới attempt trước khi trỏ tới giải thích dài. Reference implementation chỉ được mở sau attempt hoặc khi người học chủ động dùng hint ladder.

## 6. Các cổng mốc (`Milestone Gates`)

### G1 — Quyết định đầu tiên dựa trên bằng chứng — M00

- Bot chạy, test và tạo output kiểm tra được;
- có E1 evidence từ ít nhất 5 product observations;
- human judgment tồn tại trước Bot ranking;
- decision có reason, confidence và weakest assumption.

### G2 — Intelligence đáng tin cậy — M01–M02

- validation và history không overwrite evidence;
- change detection dùng provenance/freshness;
- deterministic capability vẫn chạy khi AI unavailable;
- AI claim không có evidence ref không được đi vào scoring fact.

### G3 — Vòng học thị trường đầu tiên — M03–M05

- có ít nhất một publication thủ công, đúng compliance và có tracking;
- có outcome thật sau một observation window đã khai báo;
- missing khác zero và inconclusive được giữ nguyên;
- có một improvement từ hypothesis đến reviewed release hoặc documented rejection.

### G4 — Vòng production có quản trị — M06–M11

- Signal/Analysis/Decision/Action contract có trace;
- agent tool có schema, permission và audit;
- RISK2 không thể execute nếu thiếu durable approval và revalidation;
- production bot có recovery, kill switch và Decision↔Outcome learning tạo proposed change thay vì silent self-modification.

## 7. Core / Advanced / Reference

### Core — cốt lõi

63 micro-lesson trong 7 Part là toàn bộ phạm vi bắt buộc. Một lesson chỉ được ở Core khi:

1. cần để PASS Mission hiện tại hoặc ngay kế tiếp;
2. làm thay đổi implementation hoặc business decision;
3. có artifact, test hoặc evidence áp dụng ngay;
4. không thể thay bằng một reference card ngắn.

### Module nâng cao (`Advanced`) — không tính Core/PASS

| ID | Module |
|---|---|
| A01 | API theo platform và production adapter |
| A02 | Server-side tracking, webhook và identity resolution |
| A03 | Data warehouse, dashboard và BI nâng cao |
| A04 | Experiment nâng cao và statistical power |
| A05 | Time-series, anomaly detection và forecasting |
| A06 | Machine Learning và Learning-to-Rank |
| A07 | Explore–Exploit và Multi-Armed Bandit |
| A08 | RAG, embedding và vector retrieval |
| A09 | MCP, A2A và multi-agent orchestration |
| A10 | Distributed workflow và vận hành quy mô lớn |
| A11 | Paid traffic và tối ưu portfolio đa kênh |
| A12 | SaaS productization, multi-tenancy và billing |

Advanced module chỉ được mở khi người học đã có Core evidence và một bottleneck/use case thật. Không module nào được dùng để trì hoãn real market loop đầu tiên.

### Reference — tài liệu tham chiếu, không có checkbox bài học

Reference gồm:

- glossary (bảng thuật ngữ);
- Go/SQL/HTTP/testing cookbook;
- JSON schema và decision contract;
- platform playbook có `verified_at`;
- legal/tax/current-policy source register;
- provider capability matrix;
- deployment recipe;
- security và troubleshooting checklist.

Thông tin platform, pháp lý, thuế, model/SDK và current version phải đi qua freshness policy. Chúng không trở thành Core lesson chỉ vì quan trọng.

## 8. Định nghĩa hoàn thành chương trình (`Definition of Done`)

Core chỉ hoàn tất khi:

- M00–M11 đều có Capability PASS, Reality verified và Operated theo contract của Mission;
- bốn Milestone Gate có artifact/demo và retrospective;
- người học có ít nhất một real tracked market loop, kể cả outcome bằng `0` hoặc `inconclusive`;
- Affiliate Intelligence Decision Contract được điền bằng evidence hoặc explicit abstention, không bằng fabricated completeness;
- AI capability có deterministic baseline, eval case và fallback;
- agent không bypass tool permission, policy, approval hoặc kill switch;
- một trace nối được trigger → evidence → decision → action → outcome → evaluation;
- outcome learning chỉ tạo proposed improvement qua test/review;
- người học giải thích được điều Bot biết, không biết và chưa được phép làm.

## 9. Thứ tự authority

Khi tài liệu mâu thuẫn, thứ tự authority là:

1. `CURRICULUM.md` — mục tiêu, cấu trúc Core, Mission spine và PASS boundary;
2. `ROADMAP.md` cùng `roadmap/part-00.md` đến `part-06.md` — normalized checklist/index;
3. Mission và active lesson files — execution detail;
4. operating standards trong `docs/` — contract, safety và quality detail;
5. `sources/` — historical/research input, không phải active implementation authority.

Chi tiết quyết định kiến trúc nằm tại [`docs/ADR-002-OUTCOME-DRIVEN-CURRICULUM.md`](docs/ADR-002-OUTCOME-DRIVEN-CURRICULUM.md).

## 10. Quy ước ngôn ngữ

Nội dung dành cho người học dùng tiếng Việt làm ngôn ngữ chính. Thuật ngữ tiếng Anh chuyên ngành được giữ khi cần chính xác hoặc cần khớp code/schema, nhưng phải có giải thích tiếng Việt ở lần xuất hiện quan trọng. Xem [`docs/VIETNAMESE-LANGUAGE-STYLE.md`](docs/VIETNAMESE-LANGUAGE-STYLE.md).
