---
mission_id: "M00"
title: "First Evidence-Backed Decision"
status: ready
requires_missions: []
bot_version_from: null
bot_version_to: "v0.1"
estimated_hours: 10
knowledge:
  required: ["0.1", "0.2", "0.3", "1.1", "1.2", "1.3", "2.1", "2.2", "2.3"]
  on_demand: []
  reference: []
milestones:
  contributes_to: ["G1"]
evidence:
  minimum_level: "E1"
  reality_required: true
safety_gate: "S0"
risk_scope:
  external_side_effects: false
---

# Mission M00 — First Evidence-Backed Decision

## Ship Target — Mục tiêu bàn giao

Từ learner scaffold tối giản, tự hoàn thành ba vòng attempt/pull:

```text
boot + edit + test failure
→ ghi 5 public Product observations
→ human rank trước
→ Bot baseline rank sau
→ compare + abstain khi evidence không đủ
```

Bot v0.1 phải tạo một quyết định đầu tiên có thể kiểm tra và giải thích, đồng thời nói rõ điều gì là fact, estimate, assumption hoặc unknown. M00 không publish, không gọi AI, không dùng tool bên ngoài và không tạo external side effect.

## Starting Bot State — Trạng thái Bot ban đầu

Learner workspace:

```text
lab/learner/affiliate-bot/
```

Starting state là scaffold `pre-v0.1` có thể compile/test, đọc ba observations synthetic, giữ `null` khác `0`, chạy baseline `price × commission_rate` và trả `RANK_SCENARIO`. Nó cố ý chưa có public evidence, human ranking, history hoặc business authority; evidence gate hiện tại chỉ là đường ray tối thiểu cho M00.

Scaffold chạy được để người chưa biết Go quan sát một decision-shaped output trước khi học syntax. Learner không phải viết parser từ trang trắng; công việc M00 là thay evidence, chỉ ra baseline yếu ở đâu rồi thêm một behavior/explanation có test.

Output dành cho learner phải theo [quy ước ngôn ngữ tiếng Việt](../docs/VIETNAMESE-LANGUAGE-STYLE.md): tiếng Việt là chính; enum/state, JSON key và code identifier được giữ nguyên khi cần nhưng phải có diễn giải tiếng Việt ở lần xuất hiện quan trọng.

Reference implementation trong `lab/affiliate-bot/` không phải starting state. Khi bị chặn, dùng [thang gợi ý M00](../lab/learner/affiliate-bot/HINTS-M00.md) từng mức; chỉ mở reference sau khi đã ghi blocker cụ thể.

### Environment preflight

Từ repo root, kiểm tra:

```bash
git --version
go version
git rev-parse --show-toplevel
test -f lab/learner/affiliate-bot/go.mod
cd lab/learner/affiliate-bot
go env GOMOD
go test ./...
```

Nếu Git/Go/module chưa sẵn sàng, dừng và xử lý environment blocker trước. Không tạo folder/source rời ngoài repository để né preflight.

## Try First — Thử trước

M00 có ba checkpoint. Mỗi checkpoint dự kiến 45–90 phút trước khi tính thời gian debug/evidence.

### Checkpoint 1 — Boot, sửa và quan sát test failure

1. Chạy Bot và baseline tests trước khi đọc bài dài:

   ```bash
   cd lab/learner/affiliate-bot
   go run ./cmd/bot
   go test ./...
   ```

2. Đọc output synthetic baseline và test `TestRunShowsSafeStarterStateInVietnamese`; tự thêm một output có ý nghĩa, ví dụ formula version hoặc weakest-assumption label, theo dạng tiếng Việt + thuật ngữ kỹ thuật khi cần.
3. Thêm assertion cho output mới trước để test fail, chạy test và đọc failure message.
4. Sửa behavior/test đúng, chạy lại tới PASS.
5. Ghi điều Bot hiện biết và chưa biết về Affiliate.

Sau attempt mới pull `0.1–0.3`.

### Checkpoint 2 — Ghi public observations trước khi thiết kế schema hoàn hảo

1. Chọn 5 sản phẩm công khai để M00 và G1 dùng cùng một gate.
2. Ghi thủ công observation tối thiểu:

   ```yaml
   observation_id:
   product_name:
   observed_at:
   source_url:
   access_method: public_manual
   evidence_kind: real
   price:
   currency:
   commission_rate:
   other_visible_signal:
   missing_fields: []
   notes:
   ```

3. Không điền một field chỉ vì muốn đủ schema. Nếu commission/rating/sales không công khai, giữ `unknown` và ghi nguồn không cung cấp. Dùng decimal cho rate (`10%` → `0.10`) và chỉ so price-based score trong cùng currency.
4. Copy starter file thành input riêng, thay bằng public observations và cho Bot đọc file đó; không sửa nhãn `synthetic` thành `real` nếu record vẫn là sample.
5. Chạy file thật. Nếu state là `GET_MORE_DATA`, đọc lý do; không bịa field để ép Bot recommend. Full ingest/schema validation để M01.

Sau attempt mới pull `1.1–1.3`.

### Checkpoint 3 — Human rank trước, Bot rank sau

1. Trước khi chạy ranking, tự xếp hạng 5 observations.
2. Với mỗi thứ hạng, ghi reason, strongest evidence và weakest assumption.
3. Chạy baseline ranking đơn giản đã có, xác nhận deterministic và giải thích limitation của commission-per-order.
4. Cải tiến reason/formula-version output bằng test có sẵn, nhưng giữ baseline dễ hiểu.
5. Chạy Bot, lưu output, rồi so với human ranking.
6. Chạy input missing/conflicting có sẵn và giải thích vì sao Bot trả `GET_MORE_DATA` hoặc `HUMAN_REVIEW`.

Sau attempt mới pull `2.1–2.3`.

## Run — Chạy

Lệnh tối thiểu:

```bash
cd lab/learner/affiliate-bot
go run ./cmd/bot path/to/your-public-observations.json
go test ./...
```

Câu chữ chính xác không bắt buộc, nhưng output cuối phải ưu tiên tiếng Việt và cho thấy tối thiểu:

```text
Phiên bản Bot (Bot version): v0.1
Loại bằng chứng (Evidence kind): real (...)
Số quan sát (Observations) đã nạp: 5
Tham chiếu xếp hạng của con người (Human ranking reference): saved
Xếp hạng đường cơ sở của Bot (Bot baseline ranking):
  <hạng + sản phẩm + điểm/lý do>
Trạng thái quyết định (Decision state): RANK_SCENARIO | RECOMMEND | GET_MORE_DATA | HUMAN_REVIEW
Bằng chứng còn thiếu (Missing evidence):
```

Các token máy đọc như `RANK_SCENARIO`, `RECOMMEND`, `GET_MORE_DATA`, `HUMAN_REVIEW`, JSON key và code identifier không được dịch hoặc đổi tùy tiện.

Bot không được hard-code product count/ranking chỉ để khớp expected output.

## Observe — Quan sát

Ghi riêng cho từng checkpoint:

- expected behavior;
- observed output/failure;
- evidence kind;
- gap làm learner phải pull knowledge;
- change đã áp dụng sau khi học;
- điều vẫn chưa đủ để kết luận.

Các câu hỏi bắt buộc:

1. Chương trình chạy được có đồng nghĩa hiểu Affiliate không?
2. Public page có field nào là fact quan sát được và field nào chỉ là estimate?
3. Parser/ranking deterministic có biến assumption thành truth không?
4. Bot và human bất đồng ở đâu?
5. Khi nào Bot nên abstain bằng `GET_MORE_DATA` hoặc `HUMAN_REVIEW`?

## Knowledge Pull — Lấy kiến thức đúng lúc

### Sau Checkpoint 1

- `0.1` — chạy, sửa và kiểm thử Bot đầu tiên;
- `0.2` — sample/real evidence và fact/estimate/assumption/unknown;
- `0.3` — observe failure, lưu evidence và explain-back.

Chỉ pull phần giúp hoàn thành vòng `edit → run → fail → fix → test → explain`.

### Sau Checkpoint 2

- `1.1` — ghi Product observations có source và `observed_at`;
- `1.2` — actors, money flow, commission, validation và refund;
- `1.3` — provenance, freshness, missing fields và giới hạn kết luận.

Không yêu cầu learner học mọi platform field trước khi schema tối giản chạy được.

### Sau Checkpoint 3

- `2.1` — human ranking trước code;
- `2.2` — naive score, Expected Value và before/after comparison;
- `2.3` — explainable decision, confidence, uncertainty và abstain.

Nếu Expected Value cần một input chưa được đo như conversion potential, giá trị đó phải là `estimate`/`assumption`, có confidence/reason và không được gọi là measured CVR.

## Improve — Cải tiến

Áp dụng knowledge vào đúng artifact vừa chạy:

1. dùng đúng canonical M00 fields và giữ `null` khác observed `0`;
2. tách human prediction khỏi Bot output;
3. thêm formula/version hoặc weakest-assumption marker bằng test-first;
4. giữ deterministic tie-break đã có và chứng minh bằng test;
5. thêm reason/missing evidence vào decision artifact;
6. giải thích abstention state đã chạy; full validation/normalization để M01.

Không thêm database, scheduler, AI provider hoặc Agent runtime ở M00.

## Tests — Kiểm thử

Automated/manual checks tối thiểu:

- Bot boot và output version đúng;
- output learner-facing ưu tiên tiếng Việt nhưng giữ nguyên semantic token cần thiết;
- một test đã được cố ý làm fail và sau đó phục hồi PASS;
- observations được đọc, không hard-code count;
- malformed JSON fail rõ;
- same input tạo same ranking;
- tie-break deterministic;
- assumption không được serialize/display như measured fact;
- insufficient/missing evidence tạo `GET_MORE_DATA`;
- duplicate/conflicting identity tạo `HUMAN_REVIEW`;
- mixed currency tạo `HUMAN_REVIEW` thay vì so score trực tiếp;
- sample input không được gắn `evidence_kind: real`.

## Reality Check — Kiểm chứng thực tế

**Minimum:** E1.

- đúng 5 public observations cho evidence set đầu tiên; record thiếu field vẫn được giữ trung thực và có thể làm Bot abstain;
- `source_url` là URL/public page cụ thể;
- `observed_at` có timezone hoặc format nhất quán;
- `access_method` là `public_manual`;
- field thiếu được giữ là unknown/missing;
- raw page có thể thay đổi, vì vậy observation là snapshot tại thời điểm ghi.

Sample/synthetic records được phép cho unit/failure tests nhưng không tính Reality verified. Nếu public source không truy cập được, Capability có thể tiếp tục bằng fixture nhưng Reality ở trạng thái `BLOCKED_EXTERNAL`/pending; không đánh dấu M00 DONE.

M00 không có outcome window kinh doanh vì chưa có external action.

## Operate — Vận hành

Chạy ít nhất ba cycle:

1. sample fixture để kiểm engineering path;
2. public observations hợp lệ để tạo ranking/decision;
3. missing/conflicting evidence để tạo abstention.

Chạy lại cùng input để chứng minh output deterministic. Lưu command, input version và output cho từng cycle.

## Failure Case — Tình huống lỗi

Thử ít nhất:

- source_url rỗng hoặc timestamp sai;
- malformed JSON;
- price/commission ngoài domain hợp lý khi field tồn tại;
- duplicate product identity;
- mixed/missing currency;
- key scoring input unknown;
- sample record bị gắn nhãn real;
- human ranking được tạo sau Bot output.

Bot phải fail rõ, reject evidence label sai hoặc abstain phù hợp; không âm thầm biến dữ liệu thiếu thành `0`.

## Safety Gate — Cổng an toàn

**S0 — Evidence/Data. Authority ceiling: read/manual local compute only.**

Cho phép:

- xem public pages thủ công;
- ghi local evidence;
- deterministic compute/ranking;
- local file/test output.

Không cho phép:

- login/private/restricted scraping;
- publish/send/spend/order/account change;
- fake click/order/engagement;
- lưu dữ liệu cá nhân không cần thiết;
- coi public observation là permission để Bot hành động.

`risk_scope.external_side_effects` phải luôn là `false` ở M00.

## Evidence — Bằng chứng

Lưu dưới `artifacts/missions/M00/` hoặc link tương đương:

- environment preflight;
- baseline và learner-changed Bot output;
- test failure output + final PASS output;
- 5 public Observation records;
- human ranking có timestamp trước Bot run;
- baseline BotDecision output + formula/version;
- human-vs-Bot comparison;
- abstention case;
- learner commit;
- note: điều Bot biết, không biết và chưa được phép làm.

Evidence chain của M00:

```text
Observation(E1)
→ HumanPrediction
→ BotDecision(RANK_SCENARIO | RECOMMEND | GET_MORE_DATA | HUMAN_REVIEW)
→ no Action in scope
```

## Explain-back — Giải thích lại

Review đạt khi learner trả lời đúng, nêu quan hệ nhân quả và trỏ được vào evidence/code của mình:

1. Vì sao Bot boot chưa phải Affiliate intelligence?
2. Field nào trong observations là fact, estimate, assumption hoặc unknown? Vì sao?
3. Vì sao human judgment phải được ghi trước Bot ranking?
4. Baseline formula bỏ sót điều gì và limitation đó ảnh hưởng quyết định ra sao?
5. Vì sao deterministic formula không làm assumption trở thành fact?
6. Case nào Bot phải abstain và cần đo thêm gì?
7. Vì sao M00 không được publish hoặc gọi AI/Agent?
8. Bước đo thực tế tiếp theo nào làm quyết định tốt hơn?

Không đạt nếu learner chỉ đọc lại định nghĩa mà không giải thích được output/failure/evidence của chính mình.

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] Environment preflight đạt
- [ ] learner đã tự sửa một behavior của Bot
- [ ] đã quan sát test failure và khôi phục final PASS
- [ ] Bot đọc observation records và tạo baseline ranking deterministic
- [ ] malformed JSON fail rõ
- [ ] insufficient evidence tạo `GET_MORE_DATA`; conflict tạo `HUMAN_REVIEW`
- [ ] human-vs-Bot comparison kiểm tra được
- [ ] required lessons `0.1–2.3` đã được pull sau đúng attempt và áp dụng
- [ ] explain-back đạt

### Reality

- [ ] có 5 E1 public observations với source_url/observed_at/access_method
- [ ] sample/synthetic không bị trình bày như market truth
- [ ] human ranking tồn tại trước Bot output
- [ ] strongest evidence, weakest assumption và missing evidence được lưu

### Operated

- [ ] đã chạy sample, real-evidence và abstention cycle
- [ ] cùng input tạo cùng output
- [ ] command/input/output/version evidence đã lưu
- [ ] S0 đạt và không có external side effect

## Bot Version Result — Kết quả phiên bản Bot

```text
pre-v0.1 scaffold
→ v0.1 evidence-backed deterministic decision Bot
```

Authority ceiling sau M00:

```text
public/manual read + local deterministic compute only
```

## Next Mission — Mission tiếp theo

M01 — Trustworthy History: learner sẽ quan sát dữ liệu thay đổi theo thời gian, thử làm mất history rồi xây validated append-only snapshots thay vì coi current value là toàn bộ truth.
