# Kế hoạch triển khai cá nhân — Curriculum v2 Reality-First

**Cập nhật:** 2026-09-02  
**Baseline đã merge:** `1d33f71`
**Authority:** [CURRICULUM](../CURRICULUM.md),
[ADR-005](ADR-005-REALITY-FIRST-CURRICULUM.md),
[ADR-006](ADR-006-PERSONAL-VALIDATION-AND-PUBLIC-PILOT.md),
[migration guide](CURRICULUM-MIGRATION-v2.md).

Đây là checklist vận hành cho phần còn thiếu của kế hoạch v2, dành cho một
người vận hành repository. Nó phân biệt delivery scaffold, evidence thực hành
cá nhân và learner PASS: fixture/eval **không** được dùng để tuyên bố E1–E4
hay pilot validation tổng quát.

## Quy ước trạng thái

- `[x]` — hoàn tất và đã có trong `main`;
- `[~]` — đã có một phần/scaffold, còn acceptance criteria trong checklist;
- `[ ]` — chưa bắt đầu;
- `BLOCKED_EXTERNAL` là trạng thái trung thực khi learner không có access hoặc
  safe channel; không được thay bằng synthetic evidence.

Personal validation chỉ xác nhận rằng owner đã làm được loop trong bối cảnh
của mình. Nó không đổi `pilot_status` thành `validated`, không đại diện cho
người mới khác và không tự mở quyền hành động bên ngoài.

## Ba loại gate không được gộp

| Gate | Cho phép | Không cho phép |
|---|---|---|
| `AUTHORING_OPEN` | viết contract, code, fixture, replay, dry-run, inactive workflow | claim Reality/PASS, dùng credential live, external side effect |
| `LIVE_ACTIVATION` | chạy capability đúng authority ceiling trên source/account owner kiểm soát | tăng authority cao hơn Mission, đổi blocker thành evidence |
| `PUBLIC_VALIDATION` | claim phù hợp cho learner khác sau pilot độc lập | suy từ personal evidence ra timeline/readiness tổng quát |

`BLOCKED_EXTERNAL` là blocker hợp lệ và có thể mở `AUTHORING_OPEN`; nó không
bao giờ thỏa `LIVE_ACTIVATION`, E1–E6, Mission PASS hay public validation.

## Snapshot hiện tại

- [x] V2 canonical spine: `O00 → M00 → (M01 ∥ M02) → M03 → M04 → M05…`.
- [x] Tag baseline `curriculum-v1-pre-reality-first`, ADR-005, migration rules
  và readiness metadata/validator.
- [x] O00, M00–M05 có Mission/starter/eval/verification scaffold.
- [x] Privacy boundary và redacted-evidence templates/validator.
- [x] M00–M05 v2 đang là `draft`, delivery metadata complete,
  `pilot_status: untested`; learner knowledge path vẫn còn gap cần xử lý ở H1.
- [x] M05 có reviewed-improvement contract/starter/eval; personal validation
  evidence còn trống.

> Không đổi `draft` thành `ready` hay `pilot_status: validated` chỉ vì test/eval
> xanh hoặc personal validation. Trạng thái đó chỉ dành cho pilot/evidence phù
> hợp nếu repository sau này phục vụ người khác.

## Bảng điều khiển công việc hiện tại

| Workstream | Trạng thái | Gate kế tiếp |
|---|---|---|
| CI và privacy checks có thể tin cậy | `BLOCKED` | H1.1 validator CLI |
| Beginner path M00–M05 | `BLOCKED` | H1.2 workspace path + knowledge cards |
| Authority docs personal/public | `IN_PROGRESS` | ADR-006 + H1.3 đồng bộ docs |
| Personal evidence E1–E4 | `NOT_STARTED` | H2 personal validation |
| PR10 authoring | `BLOCKED` | H1 hoàn tất |
| M06 live read-only | `BLOCKED` | E3 thật + Gate PR10-LIVE |
| M10 governed canary | `BLOCKED` | E4 thật + Gate PR12-CANARY |
| M11 production loop | `BLOCKED` | E5 thật + Gate PR13-LIVE |

## Acceptance theo bốn mục tiêu của chương trình

| Mục tiêu | Bằng chứng hoàn thành | Trạng thái hiện tại | Workstream |
|---|---|---|---|
| Bot tự động đủ “thông minh” | deterministic fallback + grounded AI + read tools + governed R0/R1 action + abstention/recovery | `PARTIAL`; M06–M11 chưa author/live | PR10–PR13 |
| Dễ bắt đầu cho người mới | clean checkout → O00 ≤20 phút; path nhất quán; blocker/hint actionable; không cần Go/API trước M00 | `BLOCKED`; path và knowledge gap | H1.1–H1.2 |
| Thực hành trước lý thuyết | mỗi Mission thử trước, pull tối đa ba card đúng gap, apply/test/evidence/explain-back | `PARTIAL`; tám card M00/M01/M05 còn thiếu | H1.2 + H2 |
| Cải tiến từ dữ liệu thực tế | E1→E4 cá nhân, preregistered experiment, honest outcome, reviewed change/rollback | `NOT_STARTED`; chưa có personal trace | H2 |

Không đổi trạng thái trong bảng chỉ vì code/test xanh. Mỗi dòng chỉ chuyển khi
evidence ở cột thứ hai có thể truy lại và authority gate tương ứng đạt.

---

## A. Hoàn tất residual PR0–PR2 — migration/readiness

### A1. Projection trạng thái và migration artifacts

- [x] Thêm banner **Curriculum v2 Personal** với trạng thái factual: M00–M05
  có delivery scaffold nhưng chưa pilot validated; M06–M11 đi qua personal
  authoring/live gates riêng.
- [x] Tạo `scripts/migrate_curriculum_v1_to_v2.py --dry-run`, chỉ báo mapping
  và không sửa `PROGRESS.md`/learner evidence.
- [x] Thêm redirect/migration stub rõ ràng cho các Mission v1 để learner mới
  không đi nhầm sequence v1.
- [x] Thêm/ghi rõ vị trí `legacy-v1-M00` hoặc historical reference tương đương
  có link tới artifact v1 được giữ lại.
- [x] Chuyển `PROGRESS.md` upstream thành example/template v1; tạo learner
  state local ignored cho v2 mà vẫn giữ lesson credit/provenance.

**Gate:** migration dry-run không thay file; link/artifact cũ resolve; không
auto-credit Mission PASS.

### A2. CI/repository enforcement

- [ ] (Tuỳ chọn) Xác minh trên GitHub rằng `Curriculum CI` là required status
  check và `main` có branch protection/ruleset nếu repository được cộng tác
  hoặc dùng từ nhiều máy.
- [x] Quy ước một PR chỉ được gọi “delivered” khi `delivery complete` và pilot
  claim có evidence refs; `ready` vẫn chỉ là authoring state.

**Gate:** local CI-equivalent luôn xanh; GitHub protection là lớp bảo vệ bổ
sung, không phải blocker cho personal repository.

## B. PR3 còn thiếu — beginner onboarding và workspace privacy

- [x] Tạo `docs/BEGINNER-START-HERE.md`: browser → first safe output, mô tả
  không cần biết terminal/Go trước M00.
- [x] Thêm hướng dẫn Windows/macOS/Linux có đường xử lý blocker cụ thể.
- [x] Thêm `.devcontainer/devcontainer.json` hoặc nêu rõ supported alternative
  nếu devcontainer không phù hợp với curriculum.
- [x] Tạo `scripts/preflight.py` kiểm tool/workspace và in remediation có thể
  làm theo, không chỉ báo lỗi chung chung.
- [x] Thêm issue template `beginner-blocker` (OS, step, blocker code, không
  yêu cầu secret/PII).
- [x] Tạo workspace initializer sinh learner-local state/evidence paths đã bị
  ignore; không copy private sample vào Git.
- [x] Bổ sung ignore path còn thiếu: `workspace/`, `pilot/raw/`,
  `lab/learner/affiliate-bot/data/local/` và raw analytics/private exports.

**Personal gate:** owner có thể đi từ browser → first safe output theo docs;
không có secret/PII/raw analytics bị commit.

## C. PR4 còn thiếu — contract registry và orientation đầy đủ

### C1. Contract registry

- [x] Tạo `contracts/schemas/`, `contracts/examples/`, `policies/`,
  `evals/packs/`, `evals/cases/`, `evals/expected/`.
- [x] Define/version schemas: Observation, HumanPrediction, BotDecision,
  ActionRecord, MeasurementContext, Outcome, Evaluation, ChangeProposal,
  TraceBundle.
- [x] Encode common semantics: `origin`, provenance/time, `unknown`/missing
  khác observed `0`, idempotency/duplicate và authority/action boundary.
- [x] Thêm schema/example validator vào CI.

### C2. O00 full synthetic trace

- [x] Nâng O00 thành one-command trace:
  `Observation → HumanPrediction → BotDecision → human-approved DRY_RUN →
  Outcome → Evaluation → ChangeProposal(PENDING_REVIEW)`.
- [x] Assert mọi record `origin=synthetic`, external side effect count = 0,
  replay idempotent và ChangeProposal không modify production.
- [x] Cung cấp quickstart ≤60 phút, tách rõ E0 orientation khỏi M00 Reality.

**Gate:** valid trace + failure fixtures (missing/zero, duplicate replay,
attempted production mutation) đều qua expected behavior.

## D. PR5 còn thiếu — harden M00/M01 market loop

### D1. M00 templates và evidence gates

- [x] Thêm `templates/MARKET-BRIEF.md`, `AUDIENCE-OBSERVATION.md`,
  `PUBLISH-READINESS.md`, `ACTION-RECORD.md`.
- [x] Validator/checklist yêu cầu tối thiểu 3 audience/problem observations có
  source, access method và observed_at.
- [x] Freeze hypothesis, exact artifact, tracking ID và outcome window trước
  manual publish; lưu human review reference.
- [x] Check claim/disclosure/rights/PII/channel permission; block paid spend,
  DM, scraping và auto-publish.

### D2. M01 measurement contract

- [x] Thêm `templates/MEASUREMENT-CONTEXT.md` và `OUTCOME-SNAPSHOT.md`, liên
  kết Outcome → ActionRecord → MeasurementContext bằng IDs.
- [x] Viết low-traffic protocol: predeclared window, observed zero khác
  missing/pending/not_yet_observable, attribution limitation và next read time.
- [x] Eval phải fail khi source/window/action linkage không đủ.

**Gate:** learner có safe channel tạo E1→E2 human-only; nếu không, Reality là
`BLOCKED_EXTERNAL`. M01 chỉ dùng analytics/export/outcome thật cho E3.

## E. PR6 còn thiếu — M02 hai implementation profile

- [x] Define Operator/no-code profile (không paid/proprietary prerequisite).
- [x] Define Go builder profile; giữ Go như golden oracle, không entrypoint
  bắt buộc trước M00.
- [x] Cùng consume contract fixtures: valid, missing, observed zero, malformed,
  duplicate, identity conflict, mixed currency, deterministic tie.
- [x] Thêm parity runner; expected output/state/reason phải **100%** giống nhau
  giữa hai profile.
- [x] Thêm `HINTS-M02.md`, checkpoint pack, intentional failing tests và
  Decision Context Card.
- [x] Đọc MarketBrief/evidence reference thật khi có access; sample luôn giữ
  `synthetic`, `price × commission_rate` chỉ là weak scenario.

**Gate:** thiếu audience/offer evidence → abstain; no external action; 3–6
knowledge cards được pull on demand; owner ghi focused time thực tế để cải
tiến personal workflow, không xem 6–8 giờ là promise cho người khác.

## F. PR7 còn thiếu — complete M03/M04 contracts

### F1. M03 history

- [x] Mở rộng append-only history cho Observation, ActionRecord, Outcome và
  MeasurementContext (không chỉ generic snapshot).
- [x] Bổ sung fixtures/test: duplicate exact, identity conflict, out-of-order,
  restart, correction/reconciliation và missing provenance.
- [x] Thêm starter progression, intentional failure và `HINTS-M03.md`.

### F2. M04 grounded advisory

- [x] Eval fixtures cho malformed schema, unknown ref, valid ref nhưng
  unsupported claim, prompt injection, provider unavailable và replay/live
  labeling.
- [x] Log redacted versions/inputs/fallback; live optional phải ghi
  `live_provider_verified: pending` khi chưa có live evidence.
- [x] Encode merge thresholds: schema validity 100%; material unsupported claim
  reject 100%; authorization violation 0; deterministic fallback 100%.

**Gate:** no API key cần cho eval; AI không tool/write/publish/execute và không
mutate deterministic baseline/history.

## G. PR8 — M05 First Reviewed Improvement

- [x] Author `missions/M05-first-reviewed-improvement.md`, starter, hints,
  contract fixtures/eval pack và CI command.
- [x] Define Experiment/Evaluation/ChangeProposal contracts and TraceBundle
  linkage from Decision → Action → Outcome → Evaluation.
- [x] Freeze one main variable, hypothesis, primary metric, MeasurementContext,
  outcome window và stop rule before outcome.
- [x] Treat insufficient traffic as `INCONCLUSIVE`, not positive/negative proof.
- [x] Record content-production time, model/tool cost và net value limitation.
- [x] Implement offline replay/champion–challenger, human release/reject and
  rollback records.
- [x] Enforce: Outcome creates ChangeProposal only; it cannot self-modify
  prompt/rule/policy/workflow.

**Gate:** M05 establishes E4 only with a real linked trace and human review.
Negative/inconclusive outcome can pass if the measurement is honest.

## H. PR9 — sửa blocker rồi chạy personal validation

### H1. Trust repair — bắt buộc trước PR10 authoring

#### H1.1 Validator CLI và CI

- [ ] Thêm `if __name__ == "__main__": raise SystemExit(main())` cho
  `validate_m00_market_loop_pack.py` và `validate_privacy_boundary.py`.
- [ ] Thêm subprocess tests: missing input/missing repository phải exit khác 0;
  valid fixture phải có output PASS và exit 0.
- [ ] Quyết định `validate_runtime_architecture.py`: thêm CLI + CI nếu còn dùng,
  hoặc archive/remove khỏi active checks để tránh validator chết nhưng tồn tại.
- [ ] Chạy toàn bộ Python validators, unit tests và Go checks sau khi sửa.

**Gate H1.1:** command invalid phải fail thật; GitHub/local CI không được xanh
do validator CLI không chạy.

#### H1.2 Beginner path và knowledge-on-demand

- [ ] Chuẩn hóa toàn bộ learner-local path thành `workspace/artifacts/local/`;
  initializer, M00/M01 Mission và starter command phải dùng cùng path.
- [ ] Author/rewrite các knowledge cards đang được M00/M01/M05 gọi:
  `6.1`, `6.2`, `7.1`, `7.2`, `7.3`, `9.1`, `10.1`, `11.1`.
- [ ] Mỗi card giữ Try First → Observe → Minimum Knowledge → Apply → Failure →
  Evidence → Explain-back và target 20–45 phút.
- [ ] Readiness report phải hiển thị riêng `delivery metadata complete` và
  `learner path complete`; unresolved knowledge ID không được ẩn.
- [ ] Thêm validator/test bắt missing knowledge file khi Mission được đưa vào
  personal execution hoặc promoted `ready`.

**Gate H1.2:** owner đi từ O00 tới từng knowledge link của M00–M05 mà không gặp
dead link, path tự tạo hoặc yêu cầu đọc legacy v1 để tiếp tục.

#### H1.3 Authority và status vocabulary

- [x] Ghi ADR-006 tách Personal Development khỏi Public Curriculum Validation.
- [ ] Đồng bộ ADR-002, ADR-005, migration, effort/calibration, mission authoring,
  `pilot/README.md` và PR template với ba gate ở đầu tài liệu này.
- [ ] Giữ `pilot_status: untested` và không dùng personal evidence để claim
  beginner readiness, timeline hay cohort success.
- [ ] Đổi wording mơ hồ `delivery complete` thành đúng lớp trạng thái ở mọi
  learner-facing summary.

**Gate H1.3:** không active authority doc nào nói cohort pilot là prerequisite
cho personal authoring; không doc nào cho personal evidence thay public pilot.

### H2. Personal validation loop — E1 đến E4

- [x] Có template consent/session/aggregate, privacy boundary và validator;
  trong personal mode chúng chỉ là tuỳ chọn để ghi nhận redacted.
- [ ] Chạy O00 sạch từ checkout mới; ghi actual setup/first-run time và blocker.
- [ ] M00: freeze brief/version trước action, có E1 public observations, human
  review và E2 manual publish; nếu block thì ghi `BLOCKED_EXTERNAL` và dừng
  mọi live progression phụ thuộc E2.
- [ ] M01: tạo E3 read-only snapshot thật, giữ zero/missing/pending riêng.
- [ ] M02: chạy Operator + Go parity trên fixture và permitted E1 reference;
  output chỉ advisory/abstain, không action.
- [ ] M03: append/query/restart/reconcile history với E3 reference thật.
- [ ] M04: freeze baseline, chạy grounded/rejected/fallback cases; live provider
  vẫn optional và không có tool/write authority.
- [ ] M05: preregister one-variable experiment trước outcome; tạo linked E4
  trace và self-review release/reject/rollback sau outcome. Thiếu traffic phải
  giữ `INCONCLUSIVE`.
- [ ] Ghi focused setup/build/debug/knowledge/review/retry tách external waiting;
  raw evidence ở ignored workspace, chỉ publish summary đã redact.
- [ ] Owner viết retrospective: điều gì hữu ích, blocker nào lặp lại, knowledge
  nào đến sai lúc và capability nào có đủ lý do để author tiếp.

| Personal evidence gate | Result |
|---|---|
| O00 và toàn bộ trusted local CI-equivalent xanh | [ ] |
| M00 có E1→E2 thật, human-only | [ ] |
| M01/M03 có E3 thật, trace/provenance/freshness đúng | [ ] |
| M05 có E4 thật hoặc progression live dừng ở `BLOCKED_EXTERNAL` | [ ] |
| Không secret/PII commit, fabricated evidence, auto-publish hay safety bypass | [ ] |
| Owner đã review limitations và rollback trước khi tăng authority | [ ] |

Personal evidence không đổi `pilot_status: validated`. Nếu H2 bị block, owner
vẫn có thể mở authoring-only PR sau H1 nhưng không được kích hoạt live gate.

## I. PR10–PR13 — authoring và live activation tách riêng

### PR10 — M06 Reliable Watcher

#### PR10-AUTHORING

- [ ] Author M06 Mission/starter/hints/eval/verification bundle.
- [ ] Tạo n8n/workflow-as-code layout dưới `lab/orchestration/n8n/`.
- [ ] Retry, timeout, dedup, allowlist, alert, restart và replay fixtures.
- [ ] Exported workflow luôn `active=false`, không credential, không write tool.

**Gate PR10-AUTHORING:** H1 complete; O00/contracts/evals/Go checks xanh. E3 bị
block vẫn được author/replay nhưng Mission giữ Reality pending/blocked.

#### PR10-LIVE — M06 read-only activation

- [ ] Có E3 source/measurement context thật thuộc account/source owner được phép
  đọc; access method và current policy đã review.
- [ ] Credential chỉ ở local runtime/secret store; least privilege read-only.
- [ ] Chạy ít nhất ba scheduled cycles gồm no-change, observed change và một
  failure/recovery; duplicate/retry không tạo record sai.
- [ ] Canonical history không phụ thuộc n8n execution log và không biến missing
  thành zero.

**Gate PR10-LIVE:** E3 thật + read-only permission + recovery evidence. Chỉ
fixture/replay hoặc `BLOCKED_EXTERNAL` không đủ.

### PR11 — M07 Decision + M08 Read-only Evidence Agent

#### PR11-AUTHORING

- [ ] Author M07/M08 Mission bundles và DecisionPacket/evaluation contracts.
- [ ] Tool Registry allowlist với schema, purpose, minimum data, timeout, risk
  ceiling và audit.
- [ ] Tối thiểu 10 DecisionPacket cases gồm stale/missing/conflict/injection/
  tool-denied; tất cả fail-closed hoặc abstain đúng expected state.
- [ ] Agent không có write/publish/spend/account-change/execute tool.

**Gate PR11-AUTHORING:** PR10 replay/recovery tests pass và deterministic path
vẫn hoạt động khi Agent/n8n unavailable.

#### PR11-LIVE — M08 read-only tool activation

- [ ] M06 có real operated history và owner audit ít nhất một full read cycle.
- [ ] Read tool chỉ lấy field cần cho declared decision; excess personal data bị
  minimise/redact/reject và không vào trace mặc định.
- [ ] CandidateEvidence phải qua deterministic validation/grounding trước khi
  trở thành canonical evidence.
- [ ] Ghi tool selection, args đã redact, permission result, latency/cost,
  evidence refs và fallback.

**Gate PR11-LIVE:** real read-only trajectory + zero unauthorized tool/write
attempt; live Agent không làm mất deterministic fallback.

### PR12 — M09 Shadow Approval + M10 Governed Canary

#### PR12-SHADOW — không external execution

- [ ] Author M09/M10 Mission bundles, ActionIntent, PolicyDecision, Approval,
  ExecutionRecord và canary contracts.
- [ ] Durable approve/reject/expire/cancel; exact intent/version/context binding.
- [ ] Test restart, duplicate callback, stale approval, changed context,
  unavailable policy authority và kill switch.
- [ ] Shadow executor chỉ tạo expected ExecutionRecord, không side effect.

**Gate PR12-SHADOW:** PR11 audit pass; mọi path thiếu policy/approval/context
đều no-execution; replay/restart không tạo side effect trùng.

#### PR12-CANARY — M10 limited live activation

- [ ] Có E4 thật từ M05; `BLOCKED_EXTERNAL` hoặc synthetic trace không đủ.
- [ ] Khai báo chính xác action allowlist, target/account, RISK class, time
  window, rate/resource/cost cap, success/abort threshold và owner.
- [ ] RISK0/RISK1 chỉ auto-execute trong allowlist sau deterministic policy;
  RISK2 luôn durable human approval + context revalidation.
- [ ] Có idempotency/dedup, dry-run comparison, audit, manual arm/disarm, kill
  switch tại executor, rollback/compensation và recovery drill.
- [ ] Chạy canary qua declared window; zero unauthorized action, duplicate side
  effect, cap violation và safety bypass.

**Gate PR12-CANARY:** chỉ real bounded canary đủ contract mới tạo E5. Replay
chỉ chứng minh Capability, không mở production.

### PR13 — M11 Production Closed Loop

#### PR13-AUTHORING

- [ ] Author M11 Mission/starter/eval/runbook và end-to-end TraceBundle.
- [ ] Production config/secrets boundary, monitoring, cost/SLO, backup/restore,
  incident response và kill-switch runbook.
- [ ] Enforce no silent self-modification of prompt/policy/weights/workflow/data
  scope; outcome chỉ tạo reviewed ChangeProposal.

**Gate PR13-AUTHORING:** PR12 shadow/canary fixtures pass; authoring không tự
kích hoạt production workflow.

#### PR13-LIVE — M11 production activation

- [ ] Có E5 real canary được owner review; không dùng `canary/replay` như hai
  lựa chọn tương đương.
- [ ] Chạy ít nhất hai end-to-end cycles, gồm một failure/recovery cycle, với
  correlation xuyên evidence → decision → policy/approval → execution → outcome.
- [ ] Backup/restore, duplicate replay, stale approval, Agent/n8n/core failure và
  kill-switch drill đều có evidence.
- [ ] RISK0/RISK1 automation giữ exact allowlist/caps; RISK2 vẫn human approval.
- [ ] Outcome/Evaluation tạo proposal; release/reject/rollback luôn versioned và
  do owner review.

**Gate PR13-LIVE:** E6 chỉ đạt sau operated production window + recovery +
reviewed learning loop. Zero incident trong replay không thay production proof.

## Definition of Done — v2 Beta

- [x] M00–M05 each have Mission, lesson mapping, starter, hint ladder, eval
  pack and verification command.
- [x] O00 runs one synthetic end-to-end trace with no side effect.
- [x] M00 is human-only E2; M01 keeps zero/missing semantics; M02 profiles
  have parity; M03 survives restart; M04 meets grounded rejection/fallback
  thresholds; M05 creates only reviewed ChangeProposal.
- [x] README/readiness reports are factual; local CI-equivalent checks are green.
- [ ] H1 trust repair hoàn tất và personal validation records đạt H2 tới mức
  evidence thực tế owner có thể truy lại; `pilot_status` vẫn `untested`.
- [ ] Authoring/live/public gates được báo riêng; blocker không xuất hiện như
  evidence hoặc quyền activation.

## Recommended execution order

```text
A + B + C
→ D + E + F
→ G (M05)
→ H1 (trust repair)
→ H2 (personal validation E1–E4)
→ PR10/PR11 authoring + read-only live gates
→ PR12 shadow → E5 bounded canary
→ PR13 authoring → E6 production loop
```

H1 là blocker trước mọi PR mới. Cohort 5–10 người không còn chặn personal
authoring, nhưng Reality/E3–E6 vẫn chặn live activation. Public readiness chỉ
được claim sau independent pilot; personal evidence không được nâng cấp thành
cohort evidence bằng wording hoặc metadata.
