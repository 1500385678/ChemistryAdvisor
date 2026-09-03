# ChemistryAdvisor

> 16-化学-Chemistry 行业 Web 项目 · 内部代号 ChemistryAdvisor

## 项目说明
基于张勇的 36 行业架构,ChemistryAdvisor 是 化学-Chemistry 行业的 Web 端顾问产品。

定位:让化学从"元素周期表背诵"变成"看得见分子、玩得转反应"——可视化、计算化、场景化。

详细规划见 `项目开发计划.md`,技术架构见 `化学顾问开发架构与计划.md`。

## 数据规模 (2026-09-04)

数据层位于 `data/knowledge/`,目前进度:

| 数据文件 | 条目数 | Phase 0 目标 | 进度 | 最近一次更新 |
|---------|--------|-------------|------|------------|
| `elements.json` | 80 | 118 | 67.8% | 2026-09-02 v3 (+20 Pm–Hg) |
| `reaction_types.json` | 20 | 50 | 40.0% | 2026-09-01 v3 (+4 水解/缩合/异构化/歧化) |
| `compounds.json` | 50 | 200 | 25.0% | 2026-09-04 v2 (+25 酸/碱/盐/氧化物/醇/羧酸/酯/多糖) |
| `themes.json` | 10 | — | 主题分类 | 2026-08-24 起草 |

总计:160 条结构化知识条目,Phase 0 整体进度约 42%。

### 化合物库 v2 新增 25 条明细

| 类别 | 新增 |
|------|------|
| 无机酸 | 氢氟酸 HF · 高氯酸 HClO₄ |
| 无机碱 | 氢氧化钙 Ca(OH)₂ · 氢氧化镁 Mg(OH)₂ |
| 无机盐 | 碳酸钠 Na₂CO₃ · 硫酸铜 CuSO₄·5H₂O · 硫酸钠 Na₂SO₄ · 硝酸钾 KNO₃ · 硝酸铵 NH₄NO₃ · 氯化钙 CaCl₂ |
| 无机氧化物 | 氧化钙 CaO · 氧化铁 Fe₂O₃ · 氧化铝 Al₂O₃ · 一氧化碳 CO · 二氧化硫 SO₂ |
| 单质气体 | 氯气 Cl₂ |
| 醇/二醇/三醇/酚 | 异丙醇 · 乙二醇 · 甘油 · 苯酚 |
| 羧酸/酯/单糖/多糖 | 柠檬酸 · 乙酸乙酯 · 果糖 · 淀粉 · 纤维素 |

## 同步
- GitHub: https://github.com/1500385678/ChemistryAdvisor
- Gitee: https://gitee.com/architectzy/ChemistryAdvisor

## 自动化
- 巡检: 每日 02:30 触发,输出 `.Log/巡检-化学-YYYYMMDD.md`(不修改主计划)
- 开发: 每日 03:30 触发,读 `.plan/YYYYMMDD.md` → 产出 1 个小变更 → 推 Gitee + GitHub
