"""化学 Web 后端 API。

化学行业 Web 项目 Phase 1 后端骨架(2026-09-19 9/19 W4 第 5 日 T2 兑现):
- 终结 26 工作日 0 代码 commit 周期(8/23 → 9/19)
- 提供 /health 健康检查端点
- 提供 /api/v1 知识库基础路由(预留 Phase 1 化学计算器/反应查询接入)

启动方式:
    pip install -r backend/requirements.txt
    uvicorn backend.main:app --reload --port 8000
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Chemistry Web API",
    description="化学行业 Web 项目后端 API · Phase 1 MVP",
    version="0.1.0",
)

# 允许前端开发服务器跨域访问(Phase 1 Vite 默认 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev
        "http://127.0.0.1:5173",
        "http://localhost:3000",  # 备用
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 知识库数据目录(Phase 0 已沉淀的 JSON 数据)
DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "knowledge"


class HealthResponse(BaseModel):
    """健康检查响应。"""

    status: str
    version: str
    knowledge_files: list[str]


@app.get("/health", response_model=HealthResponse, tags=["meta"])
async def health() -> HealthResponse:
    """健康检查 + 知识库文件清单。

    Returns:
        HealthResponse: 服务状态 + 版本 + 知识库文件列表。
    """
    files: list[str] = []
    if DATA_DIR.exists():
        files = sorted(p.name for p in DATA_DIR.glob("*.json"))
    return HealthResponse(
        status="ok",
        version=app.version,
        knowledge_files=files,
    )


@app.get("/api/v1/knowledge/{name}", tags=["knowledge"])
async def get_knowledge(name: str) -> dict[str, Any]:
    """读取知识库 JSON 文件。

    Phase 1 阶段暂不做权限/RBAC,数据为 Phase 0 已落地的公开化学数据。
    name 取值(无后缀):elements / compounds / reaction_types / themes。

    Args:
        name: 知识库名称。

    Returns:
        dict: 知识库内容。

    Raises:
        HTTPException: 文件不存在或读取失败。
    """
    # 安全:仅允许字母数字下划线,防路径穿越
    if not name.replace("_", "").isalnum():
        raise HTTPException(status_code=400, detail="invalid name")

    target = DATA_DIR / f"{name}.json"
    if not target.exists():
        raise HTTPException(status_code=404, detail=f"{name} not found")

    import json

    try:
        with target.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError) as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


if __name__ == "__main__":  # pragma: no cover
    import uvicorn

    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)