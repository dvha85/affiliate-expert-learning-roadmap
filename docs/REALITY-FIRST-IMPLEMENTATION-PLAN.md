# Kế hoạch triển khai còn lại — Curriculum v2 Reality-First

**Cập nhật:** 2026-09-02  
**Baseline đã merge:** `2ab6656`  
**Authority:** [CURRICULUM](../CURRICULUM.md),
[ADR-005](ADR-005-REALITY-FIRST-CURRICULUM.md),
[migration guide](CURRICULUM-MIGRATION-v2.md).

Đây là checklist vận hành cho phần còn thiếu của kế hoạch v2. Nó phân biệt
delivery scaffold, pilot thật và learner PASS: fixture/eval **không** được dùng
để tuyên bố E1–E4 hay pilot validation.

## Quy ước trạng thái

- `[x]` — hoàn tất và đã có trong `main`;
- `[~]` — đã có một phần/scaffold, còn acceptance criteria trong checklist;
- `[ ]` — chưa bắt đầu;
- `BLOCKED_EXTERNAL` là trạng thái trung thực khi learner không có access hoặc
  safe channel; không được thay bằng synthetic evidence.

## Snapshot hiện tại

- [x] V2 canonical spine: `O00 → M00 → (M01 ∥ M02) → M03 → M04 → M05…`.
- [x] Tag baseline `curriculum-v1-pre-reality-first`, ADR-005, migration rules
  và readiness metadata/validator.
- [x] O00, M00–M05 có Mission/starter/eval/verification scaffold.
- [x] Privacy boundary và redacted-evidence templates/validator.
- [x] M00–M05 v2 đang là `draft`, `delivery complete`, `pilot_status: untested`.
- [x] M05 có reviewed-improvement contract/starter/eval; chưa có pilot evidence thật.

> Không đổi `draft` thành `ready` hay `pilot_status: validated` chỉ vì test/eval
> xanh. Promotion cần starter/eval/verification **và** actual pilot/evidence
> phù hợp với Mission.

---

## A. Hoàn tất residual PR0–PR2 — migration/readiness

### A1. Projection trạng thái và migration artifacts

- [x] Thêm banner **Curriculum v2 Beta** với trạng thái factual: M00–M04 có
  delivery scaffold nhưng chưa pilot validated; M05–M11 planned.
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

- [ ] Xác minh trên GitHub rằng `Curriculum CI` là required status check và
  `main` có branch protection/ruleset; cập nhật audit date trong governance.
- [x] Quy ước một PR chỉ được gọi “delivered” khi `delivery complete` và pilot
  claim có evidence refs; `ready` vẫn chỉ là authoring state.

**Gate:** configuration được kiểm từ GitHub settings/API, không chỉ từ docs.

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

**Pilot gate:** median browser → first safe output ≤20 phút; không có
secret/PII/raw analytics bị commit.

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
knowledge cards được pull on demand; target focused time 6–8 giờ cần pilot xác
thực, không xem là promise.

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

## H. PR9 — pilot và promotion (không thể fake bằng code)

- [x] Tạo pilot kit: consent/session/aggregate templates, privacy boundary và
  validator; kit không chứa dữ liệu pilot hoặc telemetry.
- [ ] Recruit 5–10 learners chưa lập trình; obtain explicit consent, no hidden
  telemetry and no collection of secret/PII/raw account data.
- [ ] Create anonymized pilot record: setup/first-run/build/debug/knowledge/
  retry time, highest hint, blocker code, dropout point, Capability/Reality/
  Operated and focused vs waiting time.
- [ ] Measure time-to-E1/E2/E3/E4 and public-action authority violations.
- [ ] Compare outcomes to promotion thresholds below; publish only aggregate or
  redacted evidence.

| Promotion threshold | Result |
|---|---|
| ≥80% first demo ≤20 minutes | [ ] |
| ≥70% M00 Capability in 4–6 focused hours | [ ] |
| median first E2 ≤8 focused hours | [ ] |
| required lesson median ≤30 min; p90 ≤45 min | [ ] |
| dropout before M00 <20% | [ ] |
| human-only public action 100%; fabricated evidence/secret/PII/safety bypass = 0 | [ ] |
| ≥3 learners complete M05/E4 before production forecast | [ ] |

**Promotion rule:** only after this evidence may timeline forecasts be
recalibrated or a Mission move to `pilot_status: validated`.

## I. PR10–PR13 — locked until PR9 promotion

> Do **not** author these deeply or grant more authority before PR9 passes.

### PR10 — M06 read-only watcher

- [ ] n8n/workflow-as-code layout under `lab/orchestration/n8n/`.
- [ ] Retry, dedup, allowlist, alert and replay fixtures; exported workflows
  `active=false`, no credential.

### PR11 — M07/M08 decision and read-only agent

- [ ] DecisionPacket, abstention/memory/evaluation contract.
- [ ] Allowlisted read-only tool Agent; policy/evidence/freshness boundary.

### PR12 — M09/M10 shadow approval and canary

- [ ] Durable ActionIntent/approval record and shadow mode.
- [ ] Bounded canary, risk/policy gate, audit, kill switch and recovery tests.

### PR13 — M11 production closed loop

- [ ] Production trace, backup/restore, recovery, incident runbook and kill
  switch evidence.
- [ ] No silent self-modification of prompt/policy/weights/workflow.

## Definition of Done — v2 Beta

- [x] M00–M05 each have Mission, lesson mapping, starter, hint ladder, eval
  pack and verification command.
- [x] O00 runs one synthetic end-to-end trace with no side effect.
- [x] M00 is human-only E2; M01 keeps zero/missing semantics; M02 profiles
  have parity; M03 survives restart; M04 meets grounded rejection/fallback
  thresholds; M05 creates only reviewed ChangeProposal.
- [x] README/readiness reports are factual; local CI-equivalent checks are green.
- [ ] Pilot evidence meets PR9 promotion gates.

## Recommended execution order

```text
A + B + C
→ D + E + F
→ G (M05)
→ H (pilot/promotion)
→ I (PR10–PR13, only after pilot)
```

M05 and pilot are the critical path to Beta. PR10–PR13 are deliberately not a
near-term checklist for implementation until learners demonstrate that the
earlier loop is understandable, safe and useful.
