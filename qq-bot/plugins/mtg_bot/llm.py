"""LLM 集成模块 - 使用 OpenAI 兼容 API + 对话上下文管理"""

import os
import json
import time
import asyncio
from pathlib import Path
from typing import List, Dict, Any, Optional
from collections import defaultdict
from openai import OpenAI

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - python-dotenv is in requirements
    load_dotenv = None

from .tools import TOOLS_DESCRIPTION, TOOLS_MAP, resolve_card, search_card, search_rule
from .knowledge import get_knowledge_base

# 对话历史管理
MAX_HISTORY_ROUNDS = 5
HISTORY_EXPIRE_SECONDS = 1800
MAX_HISTORY_TOKENS = 8000  # 历史记录最大字符数，防止上下文溢出
MAX_ASSISTANT_HISTORY_CHARS = 1200
MAX_VERIFIED_CONTEXT_ITEM_CHARS = 2600

_conversation_cache: Dict[str, List[Dict]] = defaultdict(list)

# 中间过渡语关键词（出现这些说明 LLM 还没给出最终答案）
INTERMEDIATE_KEYWORDS = [
    "让我搜索", "让我查", "让我确认", "进一步搜索", "正在搜索",
    "让我进一步", "让我看看", "稍等", "让我先查", "让我调用",
    "搜索一下", "查询一下", "让我为您搜索", "请稍等",
    "让我获取", "我需要查", "我需要搜索", "我来看看",
    "让我尝试", "正在查询", "正在获取", "让我核实",
]


def _get_session_key(group_id: int, user_id: int = 0) -> str:
    if group_id and user_id:
        return f"group:{group_id}:user:{user_id}"
    if group_id:
        return f"group:{group_id}"
    return f"private:{user_id or 0}"


def _load_env_files():
    """加载本地 .env，保持环境变量优先，便于 Docker/线上覆盖。"""
    if load_dotenv is None:
        return
    bot_root = Path(__file__).resolve().parents[2]
    for env_path in (Path.cwd() / ".env", bot_root / ".env"):
        if env_path.exists():
            load_dotenv(env_path, override=False)


def _add_to_history(session_key: str, role: str, content: str):
    if role == "assistant" and len(content) > MAX_ASSISTANT_HISTORY_CHARS:
        content = content[:MAX_ASSISTANT_HISTORY_CHARS].rstrip() + "\n...[历史记录截断]"
    _conversation_cache[session_key].append({
        "role": role,
        "content": content,
        "ts": time.time()
    })
    max_msgs = MAX_HISTORY_ROUNDS * 2
    if len(_conversation_cache[session_key]) > max_msgs:
        _conversation_cache[session_key] = _conversation_cache[session_key][-max_msgs:]
    # 限制总字符数，防止上下文溢出
    total = sum(len(h["content"]) for h in _conversation_cache[session_key])
    while total > MAX_HISTORY_TOKENS and len(_conversation_cache[session_key]) > 2:
        removed = _conversation_cache[session_key].pop(0)
        total -= len(removed["content"])


def _get_history(session_key: str) -> List[Dict]:
    if session_key not in _conversation_cache:
        return []
    history = _conversation_cache[session_key]
    if not history:
        return []
    now = time.time()
    if now - history[-1]["ts"] > HISTORY_EXPIRE_SECONDS:
        _conversation_cache[session_key] = []
        return []
    return [{"role": h["role"], "content": h["content"]} for h in history]


def _is_intermediate(content: str) -> bool:
    """判断是否是中间过渡语"""
    if not content:
        return True
    content_lower = content.lower()
    # 太短
    if len(content) < 50:
        return True
    # 包含过渡关键词
    for kw in INTERMEDIATE_KEYWORDS:
        if kw in content:
            return True
    return False


class MTGAssistant:
    """万智牌智能助手"""

    def __init__(self):
        _load_env_files()
        self.api_key = os.getenv("DASHSCOPE_API_KEY")
        self.base_url = os.getenv("LLM_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")
        self.model = os.getenv("DASHSCOPE_MODEL", "glm-5.1")
        self.timeout = float(os.getenv("LLM_TIMEOUT_SECONDS", "120"))
        self.kb = get_knowledge_base()
        self.skill_context = self.kb.get_skill_context()

        self.client = OpenAI(
            api_key=self.api_key or "missing-api-key",
            base_url=self.base_url,
            timeout=self.timeout,
        )

        self.system_prompt = f"""你是重庆市竞技指挥官社群的万智牌智能助手。

【最高优先级规则】
1. 你必须优先使用「相关知识库内容」中的信息来回答问题
2. 如果「强制工具/规则上下文」或知识库内容中包含相关信息，必须以这些内容为准，禁止使用你自己的记忆来覆盖
3. 如果知识库中没有相关信息，才允许使用工具查询或基于你的知识回答，但必须标注"以下信息未在知识库中找到，基于通用知识回答"
4. 绝对禁止编造数值（生命值、费用、禁牌表等），必须从知识库或工具获取
5. 若「强制工具/规则上下文」纠正了牌名或旧规则，不得再使用旧名字/旧规则

【当前项目 Skills 已加载】
以下内容来自当前仓库的 skill/ 与 agent/ 定义。回答时必须遵守，尤其是实体解析、规则查证、赛制路由和内容成熟度边界。

{self.skill_context}

【回答规则 - 极其重要】
- **必须给出完整的最终答案**，不要只说"让我搜索"或"让我查一下"就停
- 如果工具没找到某张牌，直接基于你的万智牌知识回答，不要说"搜索未返回结果"
- 每次回答都必须包含明确的结论和建议
- 回答格式要清晰：先给结论，再给详细分析
- **禁止输出过渡语**，不要说"让我搜索"、"让我确认"、"正在查询"等中间过程
- 直接给出最终答案

【实体解析硬规则】
- 用户输入短名、数字、绰号、半截牌名、套牌简称、组合技简称、多版本角色名时，必须先调用 resolve_card。
- resolve_card 返回 needs_clarification=true 时，先列候选并追问，不得继续生成结论。
- 自动选择候选时，必须说明“我将 X 解析为 Y”或“我按某赛制语境将 X 解析为 Y”。
- 不得把 search_card 或 API fuzzy 的第一个结果当作用户意图。

【规则版本硬规则】
- 涉及规则互动时，优先使用本地 CR/MTR/IPG 文档和 search_rule。
- 如果问题可能受旧规则影响，必须明确说明采用的当前规则号；例如克撒传与红月互动应检查 CR 305.7、703.4f、704.5s、714.4 中 “with one or more chapter abilities / 具有章节异能” 的新版限制。

【特别注意】
- 法禁（Duel Commander）起始生命值为20点，不是30点
- cEDH 起始生命值为40点
- 指挥官伤害规则：cEDH有21点规则，法禁无此规则

你的职责：
1. 回答万智牌规则问题（引用具体规则编号）
2. 查询卡牌信息（使用工具获取准确数据）
3. 提供套牌构建建议
4. 解释牌张互动和堆叠结算
5. 提供法禁（Duel Commander）和 cEDH 的策略建议

回答要求：
- 使用中文回答
- 卡牌名称使用「中文（English）」格式
- 保持专业和友好
- 如果用户的问题跟之前的对话有关联，请结合上下文回答

你可以使用以下工具（只在需要查证卡牌或规则时使用）：
- resolve_card: 解析短名/数字/绰号/套牌简称/组合技简称的候选实体
- search_card: 搜索卡牌信息
- search_rule: 搜索规则信息
- translate_card_name: 翻译卡牌名称
"""

    async def chat(self, user_message: str, group_id: int = 0, user_id: int = 0) -> str:
        if not self.api_key:
            return "抱歉，当前未配置 DASHSCOPE_API_KEY，无法调用 AI 服务。请先在 qq-bot/.env 或运行环境中设置密钥。"

        session_key = _get_session_key(group_id, user_id)
        history = _get_history(session_key)

        fast_reply = self._try_fast_answer(user_message, history)
        if fast_reply:
            _add_to_history(session_key, "user", user_message)
            _add_to_history(session_key, "assistant", fast_reply)
            return fast_reply

        messages = [
            {"role": "system", "content": self.system_prompt}
        ]

        if history:
            messages.extend(history)
            print(f"[LLM] 带 {len(history)} 条历史记录")

        context = self.kb.get_context(user_message)
        verified_context = self._build_verified_context(user_message, history)
        user_content = (
            f"用户问题：{user_message}\n\n"
            f"强制工具/规则上下文：\n{verified_context}\n\n"
            f"相关知识库内容：\n{context}"
        )
        messages.append({"role": "user", "content": user_content})

        try:
            # 多轮工具调用（最多3轮，防止死循环）
            max_tool_rounds = 3
            final_content = None

            for round_num in range(max_tool_rounds):
                completion = await self._create_completion(
                    model=self.model,
                    messages=messages,
                    tools=TOOLS_DESCRIPTION if TOOLS_DESCRIPTION else None,
                    stream=False
                )

                assistant_message = completion.choices[0].message
                content = assistant_message.content or ""
                print(f"[LLM] 第{round_num+1}轮: 内容{len(content)}字, 工具调用={bool(getattr(assistant_message, 'tool_calls', None))}")

                has_tool_calls = hasattr(assistant_message, 'tool_calls') and assistant_message.tool_calls

                if not has_tool_calls:
                    # 没有工具调用了，这是最终回复
                    if _is_intermediate(content):
                        # 但内容是中间语，强制再答一次
                        print(f"[LLM] 第{round_num+1}轮疑似中间语，强制最终回答")
                        messages.append({"role": "assistant", "content": content})
                        messages.append({
                            "role": "user",
                            "content": "请直接给出完整的最终回答，不要再搜索或查询。基于你已有的信息和万智牌知识回答。"
                        })
                        continue  # 重新调用
                    else:
                        final_content = content
                        break

                # 有工具调用，执行工具
                print(f"[LLM] 第{round_num+1}轮工具调用数: {len(assistant_message.tool_calls)}")

                tool_calls_list = []
                for tc in assistant_message.tool_calls:
                    tool_calls_list.append({
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    })

                # 丢弃中间过渡语
                messages.append({
                    "role": "assistant",
                    "content": "",
                    "tool_calls": tool_calls_list
                })

                for tc in assistant_message.tool_calls:
                    tool_name = tc.function.name
                    try:
                        tool_args = json.loads(tc.function.arguments)
                    except:
                        tool_args = {}

                    if tool_name in TOOLS_MAP:
                        tool_func = TOOLS_MAP[tool_name]
                        try:
                            tool_result = tool_func(**tool_args)
                            tool_result_str = json.dumps(tool_result, ensure_ascii=False, indent=2)
                            print(f"[LLM] 工具 {tool_name}: 成功 ({len(tool_result_str)}字符)")
                        except Exception as e:
                            tool_result_str = f"工具调用失败：{str(e)}"
                            print(f"[LLM] 工具 {tool_name}: 失败 {e}")
                    else:
                        tool_result_str = f"未知工具：{tool_name}"

                    messages.append({
                        "role": "tool",
                        "content": tool_result_str,
                        "tool_call_id": tc.id
                    })

                # 继续下一轮（让 LLM 基于工具结果回答）

            # 如果循环结束还没拿到最终内容
            if final_content is None:
                print(f"[LLM] {max_tool_rounds}轮后仍无最终答案，强制回答")
                messages.append({
                    "role": "user",
                    "content": "请立即基于已有信息给出完整回答，不要再调用任何工具。"
                })
                completion = await self._create_completion(
                    model=self.model,
                    messages=messages,
                    stream=False
                )
                final_content = completion.choices[0].message.content or ""

            # 最后检查：如果答案还是太短
            if len(final_content) < 30:
                print(f"[LLM] 最终答案太短({len(final_content)}字)，可能不完整")
                final_content = final_content or "抱歉，我暂时无法回答这个问题。请尝试换个方式提问。"

            reply = final_content

            # 只保存有效回复到历史（不保存错误消息）
            if not reply.startswith("抱歉，AI 服务调用出错"):
                _add_to_history(session_key, "user", user_message)
                _add_to_history(session_key, "assistant", reply)

            return reply

        except Exception as e:
            import traceback
            print(f"LLM 调用错误: {traceback.format_exc()}")
            return f"抱歉，AI 服务调用出错：{str(e)}"

    async def _create_completion(self, **kwargs):
        """Run the synchronous OpenAI-compatible SDK without blocking NoneBot's event loop."""
        return await asyncio.to_thread(self.client.chat.completions.create, **kwargs)

    def _build_verified_context(self, user_message: str, history: List[Dict]) -> str:
        """在进入 LLM 前注入确定性查证结果，避免高风险牌名/旧规则幻觉。"""
        query = user_message.lower()
        history_text = "\n".join(h.get("content", "") for h in history[-4:]).lower()
        combined = f"{query}\n{history_text}"
        parts: List[str] = []

        def add(title: str, body: Any):
            if body:
                if not isinstance(body, str):
                    body = json.dumps(body, ensure_ascii=False, indent=2)
                if len(body) > MAX_VERIFIED_CONTEXT_ITEM_CHARS:
                    body = body[:MAX_VERIFIED_CONTEXT_ITEM_CHARS].rstrip() + "\n...[已截断]"
                parts.append(f"## {title}\n{body}")

        def add_card(name: str):
            card = search_card(name)
            add(f"Card: {name}", self._compact_card(card))

        def add_rule(rule: str):
            add(f"Rule: {rule}", search_rule(rule))

        # 反对派密探是静态操控效应，不是 Agent of Treachery，也不是触发式搜牌奖励。
        if "反对派密探" in combined or "opposition agent" in combined:
            add(
                "反对派密探强制纠错",
                (
                    "反对派密探 = Opposition Agent，不是 Agent of Treachery。"
                    "其关键能力是静态异能：You control your opponents while they're searching their libraries。"
                    "多人局若多个玩家的反对派密探同时影响同一搜寻玩家，适用 CR 723.1a："
                    "多个操控同一牌手的效应互相覆盖，最后被创造的效应生效。"
                ),
            )
            add_card("Opposition Agent")
            add_rule("723.1a")
            add_rule("723.5")

        # 红月 + 克撒传是旧规则高风险问题，必须钉住新版 Saga 条件。
        current_has_moon = "红月" in query or "腥红之月" in query or "blood moon" in query
        current_has_urza_saga = "克撒传" in query or "urza's saga" in query
        current_has_explicit_new_entity = any(k in query for k in ("2099", "blue farm", "法禁", "cedh"))
        current_is_followup = (
            any(k in query for k in ("它", "那", "还能", "构组物", "construct", "找"))
            and not current_has_explicit_new_entity
        )
        history_has_urza_saga_topic = (
            ("红月" in history_text or "腥红之月" in history_text or "blood moon" in history_text)
            and ("克撒传" in history_text or "urza's saga" in history_text)
        )
        is_urza_saga_topic = (
            (current_has_moon and current_has_urza_saga)
            or (current_is_followup and history_has_urza_saga_topic)
        )
        if is_urza_saga_topic:
            add(
                "红月/克撒传强制纠错",
                (
                    "红月/腥红之月 = Blood Moon；克撒传 = Urza's Saga 这张结界地，不是 Karn Liberated。"
                    "在当前规则下，Blood Moon 让非基本地变成山脉并按 CR 305.7 失去原规则叙述产生的异能。"
                    "Urza's Saga 仍保留结界/传纪等非地类别或副类别，但没有章节异能。"
                    "CR 703.4f、704.5s、714.4 均要求 Saga 具有 one or more chapter abilities/具有章节异能，"
                    "所以被 Blood Moon 影响时不会因“最终章节为0”而自动牺牲，也不会推进章节。"
                    "它不能起动制造构组物的异能，也不能通过第三章找神器。"
                ),
            )
            add_card("Blood Moon")
            add_card("Urza's Saga")
            for rule in ("305.7", "703.4f", "704.5s", "714.4"):
                add_rule(rule)

        if "2099" in query:
            fmt = "duel-commander" if any(k in query for k in ("法禁", "dc", "duel")) else "judge"
            intent = "commander" if any(k in query for k in ("指挥官", "commander")) else "card"
            resolved = resolve_card(
                "2099",
                format=fmt,
                intent=intent,
                require_meta_evidence=self._requires_meta_evidence(query),
            )
            add("Entity Resolve: 2099", resolved)
            selected = resolved.get("selected") if resolved else None
            if selected:
                add_card(selected)

        if "blue farm" in query:
            add("Entity Resolve: blue farm", resolve_card("blue farm", format="cedh", intent="deck"))

        if not parts:
            return "无额外强制工具上下文。"
        return "\n\n".join(parts)

    @staticmethod
    def _compact_card(card: Any) -> Any:
        if not isinstance(card, dict):
            return card
        legalities = card.get("legalities") or {}
        return {
            "name": card.get("name"),
            "name_zh": card.get("name_zh"),
            "mana_cost": card.get("mana_cost"),
            "type_line": card.get("type_line"),
            "oracle_text": card.get("oracle_text"),
            "power": card.get("power"),
            "toughness": card.get("toughness"),
            "legalities": {
                key: legalities.get(key)
                for key in ("standard", "pioneer", "modern", "legacy", "vintage", "commander", "duel")
                if key in legalities
            },
        }

    def _try_fast_answer(self, user_message: str, history: List[Dict]) -> Optional[str]:
        """高风险规则/实体题的本地确定性回答路径。"""
        query = user_message.lower()
        history_text = "\n".join(h.get("content", "") for h in history[-4:]).lower()

        if "反对派密探" in query or "opposition agent" in query:
            if "去除" in query or "离场" in query or "被移除" in query:
                return (
                    "结论：如果后进场的反对派密探（Opposition Agent）已经离场，它的持续性效应不再存在；"
                    "剩下仍在战场上的反对派密探中，最后被创造的那个操控玩家效应生效。\n\n"
                    "规则依据：CR 723.1a 说多个对同一牌手生效的牌手操控效应会互相覆盖，只有最后一个被创造出来的效应生效。"
                    "离场的反对派密探不会继续产生“操控对手搜寻”的静态效应。"
                )
            if "搜寻" in query or "search" in query:
                return (
                    "结论：由最后被创造的反对派密探（Opposition Agent）效应的操控者来控制该玩家进行搜寻。\n\n"
                    "反对派密探不是触发式“我也搜一张”的牌；它的关键是静态异能：当对手搜寻牌库时，你控制该对手。"
                    "多人局里如果两个不同玩家的反对派密探都影响同一个正在搜寻的玩家，就套用 CR 723.1a："
                    "多个操控同一牌手的效应互相覆盖，最后被创造的效应生效。随后该操控者根据 CR 723.5 替被操控玩家作出搜寻中的选择。"
                )

        current_has_moon = "红月" in query or "腥红之月" in query or "blood moon" in query
        current_has_urza_saga = "克撒传" in query or "urza's saga" in query
        history_has_urza_saga_topic = (
            ("红月" in history_text or "腥红之月" in history_text or "blood moon" in history_text)
            and ("克撒传" in history_text or "urza's saga" in history_text)
        )
        if current_has_moon and current_has_urza_saga:
            return self._blood_moon_urzas_saga_answer()
        if ("构组物" in query or "construct" in query or ("它" in query and "找" in query)) and history_has_urza_saga_topic:
            return (
                "不能。这里的“它”按上一轮理解为克撒传（Urza's Saga）。在腥红之月（Blood Moon）影响下，"
                "克撒传会按 CR 305.7 变成山脉并失去由规则叙述产生的异能，所以不能起动第二章制造构组物的异能，"
                "也不会通过第三章搜寻法术力值 0 或 1 的神器。\n\n"
                "当前规则还要注意新版 Saga 条件：CR 703.4f、704.5s、714.4 都要求“具有章节异能”。"
                "被红月影响后的克撒传没有章节异能，所以它也不会因为最终章节为 0 而自动牺牲。"
            )

        if "2099" in query:
            fmt = "duel-commander" if any(k in query for k in ("法禁", "dc", "duel")) else "judge"
            intent = "commander" if any(k in query for k in ("指挥官", "commander")) else "card"
            require_meta = self._requires_meta_evidence(query)
            resolved = resolve_card("2099", format=fmt, intent=intent, require_meta_evidence=require_meta)
            selected = resolved.get("selected") if resolved else None
            if selected:
                evidence_text = self._format_meta_evidence_summary(resolved)
                if require_meta and not resolved.get("meta_evidence_found"):
                    return (
                        f"`2099` 可以解析到 `{selected}`，但这次问题是在问当前赛制/meta，"
                        "而本地证据层没有找到足够的当前 meta 来源。"
                        "我不能把牌库匹配或手写 alias 当成当前 meta 结论；请指定来源，或先刷新该赛制 meta evidence。"
                    )
                return (
                    f"我按{'法禁' if fmt == 'duel-commander' else '当前'}语境将 `2099` 解析为 `{selected}`。"
                    "这一步来自本地 `card_resolve.py` 的赛制实体解析，不是直接拿数据库 fuzzy 第一结果。\n\n"
                    f"{evidence_text}"
                    "但法禁策略内容目前仍需要赛事样本、牌表和 meta 快照来支撑强度/Tier/占比判断；"
                    "在没有 `as_of`、`banlist_as_of` 和赛事来源前，我不会编造它“现在占比多少”或“必然是几线”。"
                )

        if "blue farm" in query:
            return (
                "在 cEDH 语境里，`Blue Farm` 通常指 Tymna the Weaver / Kraum, Ludevic's Opus 这对伙伴指挥官的四色中速/组合技套牌。"
                "我按 cEDH 语境解析，而不是沿用前面法禁或红月的问题。\n\n"
                "它的核心是用 Tymna 的战斗后过牌和 Kraum 的对手第二咒语惩罚来积累资源，"
                "再用高效互动、Tutor、Ad Nauseam / Underworld Breach / Thassa's Oracle 路线争夺胜利窗口。"
            )

        return None

    @staticmethod
    def _requires_meta_evidence(query: str) -> bool:
        return any(
            key in query
            for key in (
                "现在",
                "当前",
                "meta",
                "环境",
                "占比",
                "最多",
                "强度",
                "怎么样",
                "热门",
                "tier",
                "t1",
                "t2",
            )
        )

    @staticmethod
    def _format_meta_evidence_summary(resolved: Dict[str, Any]) -> str:
        candidates = resolved.get("candidates") or []
        if not candidates:
            return "没有找到候选。\n\n"
        selected = candidates[0]
        evidence = selected.get("meta_evidence") or []
        if not evidence:
            return "当前没有该候选的赛制 meta evidence；只能作为牌名解析结果，不能作为当前 meta 结论。\n\n"

        first = evidence[0]
        as_of = first.get("as_of") or selected.get("meta_as_of") or "未知日期"
        source_names = []
        for source in first.get("sources", []):
            name = source.get("source")
            if name and name not in source_names:
                source_names.append(name)
        sources = "、".join(source_names) if source_names else "已记录来源"
        return f"meta evidence：截至 {as_of}，来源 {sources} 指向 `{selected.get('name')}` 这个赛制实体。\n\n"

    @staticmethod
    def _blood_moon_urzas_saga_answer() -> str:
        return (
            "结论：腥红之月（Blood Moon）在场时，克撒传（Urza's Saga）会成为山脉，失去原本规则叙述带来的异能；"
            "它不会制造构组物，也不会通过第三章找神器；在当前规则下也不会因为“没有章节异能/最终章节为 0”而自动牺牲。\n\n"
            "规则拆解：\n"
            "1. CR 305.7：一个效应把地的副类别设为基本地类别时，该地失去原本地类别和由规则叙述产生的异能，并获得对应基本地类别的法术力异能。所以克撒传会获得山脉的产红能力，失去章节异能和起动式异能。\n"
            "2. 改变地副类别不会移除非地牌张类别或副类别，所以它仍是结界/传纪相关的永久物，但没有章节异能。\n"
            "3. CR 703.4f、704.5s、714.4 的新版文字都限定“具有一个或多个章节异能”的 Saga。被红月影响后的克撒传没有章节异能，所以不会推进章节，也不会按 Saga 状态动作牺牲。\n\n"
            "这正是新旧规则检索要注意的点：旧答案常说克撒传会立刻牺牲；按当前 CR 的“with one or more chapter abilities / 具有章节异能”限制，那个旧答案已经不适用。"
        )


_assistant_instance = None


def get_assistant() -> MTGAssistant:
    global _assistant_instance
    if _assistant_instance is None:
        _assistant_instance = MTGAssistant()
    return _assistant_instance
