# ChemistryAdvisor

> 16-化学-Chemistry 行业 Web 项目 · 内部代号 ChemistryAdvisor

## 项目说明
基于张勇的 36 行业架构,ChemistryAdvisor 是 化学-Chemistry 行业的 Web 端顾问产品。

定位:让化学从"元素周期表背诵"变成"看得见分子、玩得转反应"——可视化、计算化、场景化。

详细规划见 `项目开发计划.md`,技术架构见 `化学顾问开发架构与计划.md`。

## 数据规模 (2026-09-03)

数据层位于 `data/knowledge/`,目前进度:

| 数据文件 | 条目数 | Phase 0 目标 | 进度 | 最近一次更新 |
|---------|--------|-------------|------|------------|
| `elements.json` | 80 | 118 | 67.8% | 2026-09-02 v3 (+20 Pm–Hg) |
| `reaction_types.json` | 20 | 50 | 40.0% | 2026-09-01 v3 (+4 水解/缩合/异构化/歧化) |
| `compounds.json` | 25 | 200 | 12.5% | 2026-08-27 v1 |
| `themes.json` | 10 | — | 主题分类 | 2026-08-24 起草 |

总计:135 条结构化知识条目,Phase 0 整体进度约 35%。

## 同步
- GitHub: https://github.com/1500385678/ChemistryAdvisor
- Gitee: https://gitee.com/architectzy/ChemistryAdvisor

## 自动化
- 巡检: 每日 02:30 触发,输出 `.Log/巡检-化学-YYYYMMDD.md`(不修改主计划)
- 开发: 每日 03:30 触发,读 `.plan/YYYYMMDD.md` → 产出 1 个小变更 → 推 Gitee + GitHub
