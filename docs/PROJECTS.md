# Hệ thống project

## 1. 14 main projects

| # | Project | Phần | Evidence cốt lõi |
|---:|---|---:|---|
| 1 | Affiliate Business Map | 1 | Ecosystem, money flow, role map |
| 2 | Tracking & Attribution Architecture | 3 | Event map, ID strategy, reconciliation |
| 3 | Niche Intelligence | 6 | Niche scorecard và quyết định chọn niche |
| 4 | Product Intelligence | 8 | Dataset, score, ranking, validation |
| 5 | Real Content Portfolio | 9 | Nội dung thật và performance history |
| 6 | Funnel Analysis | 11 | Funnel map, drop-off, bottleneck, actions |
| 7 | Affiliate Data Warehouse | 12 | Schema, history, data quality, metrics |
| 8 | Analytics Dashboard | 13 | Dashboard ra quyết định được |
| 9 | Experiment System | 14 | Tối thiểu 10 experiments có hypothesis |
| 10 | Product Tracker Bot | 15 | Collector, scheduler, history, alerts |
| 11 | Opportunity Engine | 16 | Rule, score, rank, recommendation |
| 12 | AI Content Assistant | 17 | Grounded drafts, evaluation, human approval |
| 13 | Production Affiliate Bot | 19 | Monitoring, reliability, security, deployment |
| 14 | Affiliate Intelligence Platform | 21 | End-to-end capstone và feedback loop |

Số lượng main project vẫn là **14**. Labs và Pass Gates bên dưới là integration checkpoints, không phải Project #15+.

Mỗi project dùng [`templates/PROJECT-README.md`](../templates/PROJECT-README.md) và cần tối thiểu: scope, deliverables, acceptance criteria, evidence/demo, retrospective và next version.

## 2. Labs

Labs là work package tích hợp, thường effort `XL`, dùng để nối nhiều lesson thành một hệ thống hoặc kiểm tra khả năng vận hành thực tế.

Inventory sẽ được mở rộng theo syllabus khi author từng Part. Lab đã được xác định rõ trong roadmap hiện tại gồm:

| Lab | Vị trí | Vai trò | Project? |
|---|---|---|---|
| Affiliate Lab / orientation practice | Part 0 | Tạo môi trường thực hành, baseline và workflow học | Không |
| Platform Policy Monitoring System | Part 5 | Theo dõi thay đổi policy/rule và impact | Không |

Nếu syllabus chứa thêm lab ở Part khác, thêm vào bảng này theo đúng tên/scope canonical; không tự đổi thành main project.

## 3. Pass Gates

Pass Gate là checkpoint tích hợp để xác nhận năng lực trước khi chuyển stage lớn.

Một Pass Gate:

- có acceptance criteria riêng;
- có evidence link;
- có thể reuse artifact đã tạo trong lesson/project;
- chỉ tính effort incremental cho integration/review/hardening/demo;
- không nhân đôi toàn bộ effort của artifact đã tồn tại.

Pass Gate không làm thay đổi số lượng 14 main projects.

## 4. Evidence convention

- Lesson evidence: xem [`artifacts/README.md`](../artifacts/README.md).
- Project scope/acceptance: [`templates/PROJECT-README.md`](../templates/PROJECT-README.md).
- Experiment evidence: [`templates/EXPERIMENT-LOG.md`](../templates/EXPERIMENT-LOG.md).
- Retrospective: [`templates/RETROSPECTIVE.md`](../templates/RETROSPECTIVE.md).

Project/Lab/Pass Gate chỉ được coi là hoàn thành khi acceptance criteria và evidence tương ứng tồn tại; file/folder tồn tại không tự động nghĩa là complete.
