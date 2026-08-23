#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
md_to_json.py — ChemistryAdvisor 主题 md 解析器

功能:
  1. 解析 _ChemistryLib/0X_xxx/xxx.md 的 frontmatter(5 字段)
  2. 解析 ## 章节 / ### 小节 / 表格
  3. 输出 data/knowledge/themes.json(10 条记录)

使用:
  python3 scripts/md_to_json.py [--lib _ChemistryLib] [--out data/knowledge/themes.json]
"""
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# 5 个 frontmatter 字段
FRONTMATTER_FIELDS = ["类型", "适用角色", "关联技能", "更新日期", "来源"]

# frontmatter 行: `- **字段**：值`
FRONTMATTER_RE = re.compile(r"^- \*\*([^*]+)\*\*\s*[:：]\s*(.+?)\s*$")

# 标题: ## / ###
HEADING_RE = re.compile(r"^(#{2,3})\s+(.+?)\s*$")

# 表格行: | col1 | col2 |
TABLE_ROW_RE = re.compile(r"^\s*\|(.+)\|\s*$")

# 表格分隔行: |---|---|---|
TABLE_SEP_RE = re.compile(r"^\s*\|[\s\-:|]+\|\s*$")


def parse_frontmatter(text: str) -> tuple[dict[str, str], int]:
    """解析 frontmatter(顶部 5 个 `- **字段**：值` 行)。返回 (字段 dict, 消费行数)。"""
    meta: dict[str, str] = {}
    consumed = 0
    for line in text.splitlines():
        if not line.strip():
            consumed += 1
            continue
        m = FRONTMATTER_RE.match(line)
        if not m:
            # frontmatter 结束(遇到非空且非 frontmatter 行)
            break
        key = m.group(1).strip()
        if key in FRONTMATTER_FIELDS:
            meta[key] = m.group(2).strip()
            consumed += 1
        else:
            break
    return meta, consumed


def parse_title(text: str) -> str:
    """解析 H1 标题 `# xxx`。"""
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("# ") and not s.startswith("## "):
            return s[2:].strip()
    return ""


def split_blocks(text: str) -> list[dict[str, Any]]:
    """把 md 正文切成块:heading / table / paragraph。"""
    blocks: list[dict[str, Any]] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()

        # 标题
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            blocks.append({"kind": "heading", "level": level, "title": title})
            i += 1
            continue

        # 表格
        if TABLE_ROW_RE.match(line):
            # 收集连续表格行
            tbl_lines = []
            while i < len(lines) and TABLE_ROW_RE.match(lines[i]):
                tbl_lines.append(lines[i])
                i += 1
            # 至少 3 行(header + sep + 1 row)
            if len(tbl_lines) >= 3 and TABLE_SEP_RE.match(tbl_lines[1]):
                headers = [
                    c.strip() for c in tbl_lines[0].strip("|").split("|")
                ]
                rows = []
                for tl in tbl_lines[2:]:
                    cells = [c.strip() for c in tl.strip("|").split("|")]
                    rows.append(cells)
                blocks.append(
                    {"kind": "table", "headers": headers, "rows": rows}
                )
            continue

        # 跳过水平线 / 空行(段落内空行用于分隔)
        if not s or s == "---":
            i += 1
            continue

        # 段落:累积直到空行 / 标题 / 表格
        para = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            ns = nxt.strip()
            if not ns or ns == "---":
                break
            if HEADING_RE.match(nxt):
                break
            if TABLE_ROW_RE.match(nxt):
                break
            para.append(nxt)
            i += 1
        blocks.append({"kind": "paragraph", "text": "\n".join(para).strip()})
    return blocks


def blocks_to_sections(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """把块序列组织成章节树:每个 ## 是一个 section,内含 ## 下的 ### 和段落/表格。"""
    sections: list[dict[str, Any]] = []
    current_h2: dict[str, Any] | None = None

    for b in blocks:
        if b["kind"] == "heading":
            if b["level"] == 2:
                current_h2 = {
                    "title": b["title"],
                    "level": 2,
                    "subsections": [],
                    "tables": [],
                }
                sections.append(current_h2)
            elif b["level"] == 3 and current_h2 is not None:
                current_h2["subsections"].append(
                    {
                        "title": b["title"],
                        "content": [],
                        "tables": [],
                    }
                )
        elif b["kind"] == "table" and current_h2 is not None:
            # 表归到当前 ## 下;若有当前 ###,归到 ### 下,否则归 ##
            if current_h2["subsections"]:
                current_h2["subsections"][-1]["tables"].append(
                    {"headers": b["headers"], "rows": b["rows"]}
                )
            else:
                current_h2["tables"].append(
                    {"headers": b["headers"], "rows": b["rows"]}
                )
        elif b["kind"] == "paragraph" and current_h2 is not None:
            if current_h2["subsections"]:
                current_h2["subsections"][-1]["content"].append(b["text"])
            # 否则段落附在 ## 的"intro"字段
            else:
                current_h2.setdefault("intro", []).append(b["text"])
    return sections


def parse_one_md(path: Path) -> dict[str, Any]:
    """解析单个 md,返回结构化 dict。"""
    text = path.read_text(encoding="utf-8")
    title = parse_title(text)
    meta, _ = parse_frontmatter(text)
    # 跳过 frontmatter + 顶部水平线,从首个 ## 开始切块
    blocks_all = split_blocks(text)
    # 过滤掉 frontmatter 之前的块(在 split_blocks 里 frontmatter 行不进任何规则,会被当成段落)
    # 实际我们用 parse_frontmatter 已抽掉逻辑,这里按"首个 heading 块开始"
    blocks = []
    seen_heading = False
    for b in blocks_all:
        if not seen_heading:
            if b["kind"] == "heading":
                seen_heading = True
                blocks.append(b)
            # skip 之前所有块
        else:
            blocks.append(b)
    sections = blocks_to_sections(blocks)
    # 派生 name(从目录名)
    name = path.parent.name
    return {
        "name": name,
        "title": title,
        "type": meta.get("类型", ""),
        "role": meta.get("适用角色", ""),
        "skills": meta.get("关联技能", ""),
        "updated": meta.get("更新日期", ""),
        "source": meta.get("来源", ""),
        "section_count": len(sections),
        "sections": sections,
    }


def find_theme_dirs(lib_root: Path) -> list[Path]:
    """找所有 0X_xxx 主题目录。"""
    return sorted([p for p in lib_root.iterdir() if p.is_dir() and re.match(r"^\d{2}_", p.name)])


def main() -> int:
    here = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="ChemistryAdvisor 主题 md 解析器")
    parser.add_argument("--lib", default=str(here.parent), help="_ChemistryLib 父目录(指向 _ChemistryLib)")
    parser.add_argument("--out", default=str(here / "data" / "knowledge" / "themes.json"), help="输出 JSON")
    args = parser.parse_args()

    lib_root = Path(args.lib)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    theme_dirs = find_theme_dirs(lib_root)
    if not theme_dirs:
        print(f"[ERROR] 在 {lib_root} 下未找到任何 0X_xxx 主题目录", file=sys.stderr)
        return 1

    results: list[dict[str, Any]] = []
    for d in theme_dirs:
        # 找目录里唯一的 md
        mds = list(d.glob("*.md"))
        if not mds:
            print(f"[WARN] {d.name} 下无 md,跳过", file=sys.stderr)
            continue
        md = mds[0]
        rec = parse_one_md(md)
        results.append(rec)
        print(f"[OK] {rec['name']:30s} sections={rec['section_count']:2d}")

    out_path.write_text(
        json.dumps(results, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\n[DONE] 写入 {len(results)} 条 → {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
