# Mission system

Mission là đơn vị tiến độ chính của curriculum. Một Bot duy nhất tiến hóa qua M00–M11.

~~~text
Mission ≠ Lesson ≠ Milestone ≠ Bot Version
~~~

- Lesson cung cấp knowledge slice đúng lúc.
- Mission ship một capability/evidence step.
- Milestone gom nhiều Mission thành demo.
- Bot Version là trạng thái sản phẩm sau Mission.

## Spine

| Mission | Outcome | Authoring |
|---|---|---|
| [M00](M00-first-evidence-backed-decision.md) | First evidence-backed decision | ready |
| [M01](M01-trustworthy-history.md) | Trustworthy history | draft |
| [M02](M02-grounded-ai-advisor.md) | Grounded AI advisor | draft |
| [M03](M03-first-tracked-manual-publish.md) | First tracked manual publish | draft |
| M04 | Real outcome analytics | planned |
| M05 | First real improvement loop | planned |
| M06 | Reliable automatic watcher | planned |
| M07 | Decision, abstention và memory | planned |
| M08 | Read-only tool agent | planned |
| M09 | Shadow action + durable approval | planned |
| M10 | Limited governed automation | planned |
| M11 | Production closed loop | planned |

`planned` nghĩa là outcome/knowledge/gate đã có trong `CURRICULUM.md`, roadmap và Mission Knowledge Map, nhưng execution file chưa được author/review. Không tự nhảy tới một Mission planned rồi đoán acceptance criteria.

## Trạng thái độc lập

Authoring: planned → draft → ready.

Learner:

- Capability PASS;
- Reality verified;
- Operated;
- DONE khi các chiều bắt buộc đều đạt.

Mission ready không nghĩa learner đã PASS. CI xanh cũng không tạo learner evidence.

## Evidence chain

~~~text
Observation → HumanPrediction → BotDecision
→ Action/ActionIntent → Outcome → Evaluation
→ ChangeProposal → BotVersion
~~~

Early Mission chưa có mọi record; không được dùng synthetic record để giả vờ đã có real outcome.

## Workspace

~~~text
lab/learner/affiliate-bot/   # learner tự build
lab/affiliate-bot/           # reference sau attempt
~~~

Chi tiết: [Mission authoring standard](../docs/MISSION-AUTHORING-STANDARD.md) và [Mission PASS](../docs/MISSION-PASS-CRITERIA.md).
