# Chemistry Web Backend

化学行业 Web 项目 Phase 1 后端骨架(2026-09-19 落地,`feat(backend): FastAPI + /health endpoint`)。

终结 26 工作日 0 代码 commit 周期(2026-08-23 → 2026-09-19,W1-W4)。

## 目录

```
backend/
├── main.py            # FastAPI 应用入口
├── requirements.txt   # 依赖
└── README.md          # 本文件
```

## 启动

```bash
# 创建虚拟环境(可选,推荐)
python3 -m venv backend/.venv
source backend/.venv/bin/activate

# 安装依赖
pip install -r backend/requirements.txt

# 启动服务(开发模式,自动 reload)
uvicorn backend.main:app --reload --port 8000

# 或直接运行
python3 backend/main.py
```

启动后访问:

- `http://localhost:8000/health` — 健康检查 + 知识库文件清单
- `http://localhost:8000/docs` — Swagger UI 交互式 API 文档
- `http://localhost:8000/api/v1/knowledge/elements` — 读取元素库 JSON
- `http://localhost:8000/api/v1/knowledge/compounds` — 读取化合物库 JSON
- `http://localhost:8000/api/v1/knowledge/reaction_types` — 读取反应类型库 JSON
- `http://localhost:8000/api/v1/knowledge/themes` — 读取主题库 JSON

## 端点

### `GET /health`

健康检查。返回服务状态、版本号、当前可见的知识库 JSON 文件清单。

### `GET /api/v1/knowledge/{name}`

读取 Phase 0 已落地的知识库 JSON 文件。

`name` 取值(无 `.json` 后缀):

| name | 文件 | Phase 0 状态 |
|------|------|---------------|
| `elements` | `data/knowledge/elements.json` | 80/118 元素(67.8% 原 / 80% 延期) |
| `compounds` | `data/knowledge/compounds.json` | 75/200 化合物(37.5% 原 / 75% 延期) |
| `reaction_types` | `data/knowledge/reaction_types.json` | 30/50 类型(60% 原 / **100% 延期 ✓**) |
| `themes` | `data/knowledge/themes.json` | 10/50 主题(20% 原 / 20% 延期) |

## Phase 1 接入规划

- [ ] 化学计算器:分子量/摩尔/配平/pH/缓冲(分模块) → `POST /api/v1/calc/*`
- [ ] 反应查询页:按类型/条件浏览 + 详情展示 → `GET /api/v1/reactions/*`
- [ ] 分子 3D 可视化:输入 SMILES → 3D 模型(RDKit 服务端预计算)

## 关联文档

- 项目主计划:`../项目开发计划.md` §六 Phase 1 MVP
- 项目架构:`../化学顾问开发架构与计划.md`
- 上次巡检:`../.Log/巡检-化学-20260918.md` §三 T2 强制项