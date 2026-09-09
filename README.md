# ChemistryAdvisor

> 16-化学-Chemistry 行业 Web 项目 · 内部代号 ChemistryAdvisor

## 项目说明
基于张勇的 36 行业架构,ChemistryAdvisor 是 化学-Chemistry 行业的 Web 端顾问产品。

定位:让化学从"元素周期表背诵"变成"看得见分子、玩得转反应"——可视化、计算化、场景化。

详细规划见 `项目开发计划.md`,技术架构见 `化学顾问开发架构与计划.md`。

## 数据规模 (2026-09-10)

数据层位于 `data/knowledge/`,目前进度(2026-09-10 03:30 巡检快照,compounds v3 落地后):

| 数据文件 | 条目数 | Phase 0 目标 | 进度 | 最近一次更新 |
|---------|--------|-------------|------|------------|
| `elements.json` | 80 | 118 | 67.8% | 2026-09-02 v3 (+20 Pm–Hg) |
| `reaction_types.json` | 20 | 50 | 40.0% | 2026-09-01 v3 (+4 水解/缩合/异构化/歧化) |
| `compounds.json` | 75 | 200 | 37.5% | 2026-09-10 v3 (+25 有机主链:烯烃/炔烃/卤代烃/醚/胺/氨基酸/酰胺/腈/硝基) |
| `themes.json` | 10 | — | 主题分类 | 2026-08-24 起草 |

总计:185 条结构化知识条目,Phase 0 整体进度约 23%(75 化合物 + 20 反应 + 0 概念 / 200 化合物 + 50 反应 + 200 概念)。
延期口径(96af917 §1 2,化合物 100/反应 30/元素 100/概念 50):完成度 **62.5%**(175/280)。

> **Phase 0 状态 (2026-09-10)**:deadline 延期至 9/14 24:00(96af917 §1 1),距今 4 工作日,详见 `项目开发计划.md` §五 · Phase 0 收官声明。

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

### 化合物库 v3 新增 25 条明细(2026-09-10)

**有机化学主链补全**:补足烷烃→烯烃→炔烃→卤代烃→醚→胺→氨基酸→酰胺→腈→硝基 共 10 个新类别(类别 20→30)

| 类别 | 新增 |
|------|------|
| 烷烃 | 乙烷 C₂H₆ · 丙烷 C₃H₈ · 正丁烷 C₄H₁₀ |
| 烯烃 | 乙烯 C₂H₄ · 丙烯 C₃H₆ |
| 二烯烃 | 1,3-丁二烯 C₄H₆ |
| 炔烃 | 乙炔 C₂H₂ · 丙炔 C₃H₄ |
| 卤代烃 | 氯仿 CHCl₃ · 四氯化碳 CCl₄ |
| 醚 | 乙醚 · 四氢呋喃 THF |
| 胺 | 甲胺 · 苯胺 |
| 氨基酸 | 甘氨酸 · 丙氨酸 |
| 酰胺 | 尿素 CH₄N₂O |
| 腈 | 乙腈 CH₃CN |
| 硝基化合物 | 硝基苯 C₆H₅NO₂ |
| 醇/羧酸/酯/芳香烃/酮/醛(扩 1) | 正丁醇 · 甲酸 · 乙酸甲酯 · 甲苯 · 环己酮 · 苯甲醛 |

## 同步
- GitHub: https://github.com/1500385678/ChemistryAdvisor
- Gitee: https://gitee.com/architectzy/ChemistryAdvisor

### git 同步状态 (2026-09-08 03:30 T4 闭环)

| 远程 | 状态 | commit 落后 | tracking |
|------|------|------------|----------|
| `github/main` | ✅ 已配 tracking(2026-09-08)+ 已推 | 0 | `[github/main]` |
| `gitee/main` | ✅ 已同步 | 0 | `[gitee/main]` |

> 2026-09-08 终结 13 巡检日 GitHub 半挂(9/6 `df2b9f1` commit message 写"已配 upstream"但实际未配 tracking + 未 push,9/6→9/8 持续累积到 8 commit 落后)。本次 T4 闭环:`git branch --set-upstream-to=github/main` + `git push github main` 推 8 commit + `git push gitee main` 推 2 commit,commit message 标签 → git 状态事实。

## 自动化
- 巡检: 每日 02:30 触发,输出 `.Log/巡检-化学-YYYYMMDD.md`(不修改主计划)
- 开发: 每日 03:30 触发,读 `.plan/YYYYMMDD.md` → 产出 1 个小变更 → 推 Gitee + GitHub

## 开发节奏 · T1-T5 角色分工

> 落地于 2026-09-05 双计划分工决断(详见 `项目开发计划.md` §一 · 主计划声明 + `.plan/20260905.md` §一)。本节明确 5 个角色的职责边界,便于每日 T1-T5 自动派单与 commit 复盘。

| 角色 | 职责 | 频率 | 落地位置 |
|------|------|------|----------|
| **T1 · 计划** | `.plan/YYYYMMDD.md` 起草 / 主计划 checkbox 维护 / Phase 收口清单 | 每日 | `项目开发计划.md` / `.plan/` |
| **T2 · 改bug** | README / 文档修正 / 配置修复 / 小修小补 | 每日 | `README.md` / 根目录配置 |
| **T3 · 加API** | 化合物/反应/元素等数据资产增量 + 库扩 v2/v3/v4 | 每周 2-3 次 | `data/knowledge/*.json` |
| **T4 · 优化/release** | git upstream 配 + push 落地 / 双计划同步声明 / 巡检→开发闭环 | 每日 | `README.md` / 主计划 / `git push` |
| **T5 · 推release** | 元素/化合物等数据资产扩 v3/v4 + 节奏化落地 | 每周 2-3 次 | `data/knowledge/*.json` |

### 当前节奏快照(2026-09-06)

- **T1**(9/5 重启):推 `.plan/20260905.md` + 主计划 §五 .plan 治理 checkbox
- **T2**(9/3):推 `eae2b7b docs(readme)` 补数据规模表
- **T3**(9/4):推 `051a79e feat(data)` compounds v2 50 条
- **T5**(9/2):推 `c1f8df7 feat(data)` elements v3 80 条
- **T4**(9/6 今日):推 `双计划同步声明` + 配 git upstream 终结 11 巡检日半挂

### 数据资产进度(2026-09-06)

| 资产 | 进度 | 距 Phase 0 目标 |
|------|------|----------------|
| `elements.json` | 80 / 118 | 67.8%(差 38) |
| `compounds.json` | 50 / 200 | 25.0%(差 150) |
| `reaction_types.json` | 20 / 50 | 40.0%(差 30) |
| `themes.json` | 10 | 主题分类骨架 |

> Phase 0 deadline: 2026-09-07 24:00 · 距今 22h
