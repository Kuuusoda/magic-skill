"""知识库加载和检索模块"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Dict, List


class KnowledgeBase:
    """万智牌知识库"""

    def __init__(self, wiki_path: str, raw_path: str, skill_path: str | None = None, agent_path: str | None = None):
        self.wiki_path = Path(wiki_path)
        self.raw_path = Path(raw_path)
        self.skill_path = Path(skill_path) if skill_path else None
        self.agent_path = Path(agent_path) if agent_path else None
        self.documents: List[Dict] = []
        self._load_knowledge_base()

    def _load_knowledge_base(self):
        """加载知识库文档"""
        # 加载 wiki 文档
        if self.wiki_path.exists():
            for md_file in self.wiki_path.rglob("*.md"):
                try:
                    content = md_file.read_text(encoding="utf-8")
                    self.documents.append({
                        "path": str(md_file),
                        "content": content,
                        "type": "wiki"
                    })
                except Exception as e:
                    print(f"加载 {md_file} 失败: {e}")

        # 加载规则文档
        cr_path = self.raw_path / "cr"
        if cr_path.exists():
            for md_file in cr_path.glob("*.md"):
                try:
                    content = md_file.read_text(encoding="utf-8")
                    self.documents.append({
                        "path": str(md_file),
                        "content": content,
                        "type": "rules"
                    })
                except Exception as e:
                    print(f"加载 {md_file} 失败: {e}")

        # 加载项目 skills：机器人不能只依赖模型记忆，必须读当前仓库的技能契约。
        if self.skill_path and self.skill_path.exists():
            skill_files = []
            shared_path = self.skill_path / "_shared"
            if shared_path.exists():
                skill_files.extend(sorted(shared_path.glob("*.md")))
            for skill_dir in sorted(p for p in self.skill_path.iterdir() if p.is_dir() and p.name != "_shared"):
                for name in ("SKILL.md", "SKILL_EN.md"):
                    path = skill_dir / name
                    if path.exists():
                        skill_files.append(path)

            for md_file in skill_files:
                try:
                    content = md_file.read_text(encoding="utf-8")
                    doc_type = "skill-shared" if "_shared" in md_file.parts else "skill"
                    self.documents.append({
                        "path": str(md_file),
                        "content": content,
                        "type": doc_type
                    })
                except Exception as e:
                    print(f"加载 {md_file} 失败: {e}")

        # 加载 agent 定义，便于回答时遵守项目内的协作/查询流程。
        if self.agent_path and self.agent_path.exists():
            for md_file in sorted(self.agent_path.glob("*.md")):
                try:
                    content = md_file.read_text(encoding="utf-8")
                    self.documents.append({
                        "path": str(md_file),
                        "content": content,
                        "type": "agent"
                    })
                except Exception as e:
                    print(f"加载 {md_file} 失败: {e}")

        print(f"知识库加载完成: {len(self.documents)} 个文档")

    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """关键词搜索（改进版：文件名优先 + 中文匹配 + 模糊匹配）"""
        results = []
        query_lower = query.lower()

        for doc in self.documents:
            content_lower = doc["content"].lower()
            path_lower = doc["path"].lower()

            # 文件名匹配（高分）
            filename = Path(doc["path"]).stem.lower()
            name_score = 0
            for kw in query_lower.split():
                if kw in filename:
                    name_score += 10

            # 内容关键词匹配
            keywords = query_lower.split()
            content_score = sum(1 for kw in keywords if kw in content_lower)

            # 中文整词匹配
            if query in doc["content"]:
                content_score += 5

            # 中文部分匹配（取查询中长度>=2的子串）
            chinese_chars = [c for c in query if '\u4e00' <= c <= '\u9fff']
            if len(chinese_chars) >= 2:
                query_str = ''.join(chinese_chars)
                # 尝试 2-4 字的子串
                for length in range(min(4, len(query_str)), 1, -1):
                    for i in range(len(query_str) - length + 1):
                        substr = query_str[i:i+length]
                        if substr in doc["content"]:
                            content_score += 3
                            break

            total_score = name_score + content_score

            if total_score > 0:
                idx = content_lower.find(keywords[0]) if keywords else 0
                if idx < 0:
                    # 用中文子串定位
                    for c in query:
                        if c in content_lower:
                            idx = content_lower.index(c)
                            break
                    if idx < 0:
                        idx = 0
                start = max(0, idx - 200)
                end = min(len(doc["content"]), idx + 800)
                snippet = doc["content"][start:end]

                results.append({
                    "path": doc["path"],
                    "snippet": snippet,
                    "score": total_score,
                    "type": doc["type"]
                })

        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]

    def get_context(self, query: str) -> str:
        """获取查询相关的上下文"""
        results = self.search(query)

        if not results:
            return "未找到相关信息。"

        context_parts = []
        for i, result in enumerate(results, 1):
            context_parts.append(
                f"[文档 {i}] ({result['type']})\n"
                f"路径: {result['path']}\n"
                f"内容:\n{result['snippet']}\n"
            )

        return "\n---\n".join(context_parts)

    def get_skill_context(self) -> str:
        """获取适合放入系统提示的当前项目 skill 摘要。"""
        shared_docs = [d for d in self.documents if d["type"] == "skill-shared"]
        skill_docs = [d for d in self.documents if d["type"] == "skill" and Path(d["path"]).name == "SKILL.md"]

        parts = []
        if shared_docs:
            parts.append("【MTG 公共 skill 契约】")
            for doc in shared_docs:
                parts.append(f"路径: {doc['path']}\n{_clip(doc['content'], 4500)}")

        if skill_docs:
            parts.append("【当前可用 MTG skills】")
            for doc in sorted(skill_docs, key=lambda d: d["path"]):
                meta = _parse_frontmatter(doc["content"])
                name = meta.get("name") or Path(doc["path"]).parent.name
                description = meta.get("description", "")
                overview = _extract_skill_overview(doc["content"])
                parts.append(
                    f"- {name}: {description}\n"
                    f"  路径: {doc['path']}\n"
                    f"{overview}"
                )

        return "\n\n".join(parts) if parts else "未加载项目 skill。"


def _clip(text: str, limit: int) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "\n...[已截断]"


def _parse_frontmatter(content: str) -> Dict[str, str]:
    if not content.startswith("---"):
        return {}
    end = content.find("\n---", 3)
    if end < 0:
        return {}
    meta: Dict[str, str] = {}
    for line in content[3:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    return meta


def _extract_skill_overview(content: str, limit: int = 1800) -> str:
    """保留触发/边界/实体解析等高价值段落，避免把超长 skill 全塞进系统提示。"""
    lines = content.splitlines()
    keep = []
    capture = False
    wanted_headers = (
        "## 触发条件",
        "## 边界",
        "## 执行流程",
        "### Step 0",
        "## Card Lookup",
        "## 牌名",
        "## 实体解析",
    )
    stop_headers = (
        "### Step 1",
        "## 输出",
        "## Performance",
        "## 验证",
    )
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(wanted_headers):
            capture = True
        elif capture and stripped.startswith(stop_headers):
            capture = False
        if capture:
            keep.append(line)

    text = "\n".join(keep).strip()
    if not text:
        text = "\n".join(lines[:80]).strip()
    return _clip(text, limit)


def _project_root() -> Path:
    # knowledge.py 位于 qq-bot/plugins/mtg_bot/knowledge.py
    return Path(__file__).resolve().parents[3]


def _resolve_project_path(value: str | None, default: Path) -> Path:
    if not value:
        return default
    path = Path(value)
    if path.is_absolute():
        return path

    root = _project_root()
    candidates = [
        Path.cwd() / path,
        root / path,
        root / "qq-bot" / path,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()
    return (root / "qq-bot" / path).resolve()


# 全局知识库实例
_kb_instance = None


def get_knowledge_base() -> KnowledgeBase:
    """获取知识库单例"""
    global _kb_instance
    if _kb_instance is None:
        # 从环境变量读取路径
        root = _project_root()
        wiki_path = _resolve_project_path(os.getenv("WIKI_PATH"), root / "wiki")
        raw_path = _resolve_project_path(os.getenv("RAW_PATH"), root / "raw")
        skill_path = _resolve_project_path(os.getenv("SKILL_PATH"), root / "skill")
        agent_path = _resolve_project_path(os.getenv("AGENT_PATH"), root / "agent")
        _kb_instance = KnowledgeBase(str(wiki_path), str(raw_path), str(skill_path), str(agent_path))
    return _kb_instance
