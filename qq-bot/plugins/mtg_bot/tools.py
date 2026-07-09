"""工具模块 - 封装现有的万智牌查询工具"""

import sys
import os
from pathlib import Path
from typing import Any, Dict, Optional

# 添加 raw/tools 到 Python 路径（多个候选路径）
# tools.py 位于 qq-bot/plugins/mtg_bot/tools.py
# parent x4 = magic/ → magic/raw/tools/mtg_wiki (开发环境)
# Docker 中直接使用 /app/raw/tools/mtg_wiki
_candidates = [
    Path(__file__).resolve().parent.parent.parent.parent / "raw" / "tools" / "mtg_wiki",  # magic/raw/tools/mtg_wiki
    Path("/app/raw/tools/mtg_wiki"),  # Docker 容器
]
for _p in _candidates:
    if _p.exists():
        sys.path.insert(0, str(_p))
        break


def search_card(query: str) -> Optional[Dict[str, Any]]:
    """搜索卡牌信息

    Args:
        query: 卡牌名称（中文或英文）

    Returns:
        卡牌信息字典，如果未找到则返回 None
    """
    try:
        import card_search

        result = card_search.search(query)

        if not result:
            return None

        # card_search.search() 返回的是单个卡牌 dict（包含 name, oracle_text 等）
        # 不是 list，直接处理
        if isinstance(result, dict):
            # 检查是否是"未找到"的返回
            if result.get('type') == 'none' or not result.get('name'):
                return None

            return {
                "name": result.get("name", ""),
                "name_zh": result.get("printed_name", ""),
                "mana_cost": result.get("mana_cost", ""),
                "type_line": result.get("type_line", ""),
                "oracle_text": result.get("oracle_text", ""),
                "power": result.get("power", ""),
                "toughness": result.get("toughness", ""),
                "colors": result.get("colors", []),
                "rarity": result.get("rarity", ""),
                "set": result.get("set", ""),
                "legalities": result.get("legalities", {}),
            }

        return None

    except ImportError:
        print("警告: card_search 模块未找到")
        return None
    except Exception as e:
        print(f"搜索卡牌时出错: {e}")
        import traceback
        traceback.print_exc()
        return None


def resolve_card(
    query: str,
    format: str = "judge",
    intent: str = "card",
    require_meta_evidence: bool = False,
) -> Optional[Dict[str, Any]]:
    """解析短名/数字/绰号/套牌简称，返回候选列表和是否需要追问。

    Args:
        query: 用户输入的牌名、简称、套牌名或组合技片段
        format: judge / cedh / duel-commander / modern
        intent: card / commander / deck / combo / interaction / archetype

    Returns:
        card_resolve.py 的结构化解析结果
    """
    try:
        import card_resolve

        allowed_formats = {"judge", "cedh", "duel-commander", "modern"}
        fmt = format if format in allowed_formats else "judge"
        return card_resolve.resolve(query, fmt, intent or "card", require_meta_evidence=require_meta_evidence)
    except ImportError:
        print("警告: card_resolve 模块未找到")
        return None
    except Exception as e:
        print(f"解析牌名时出错: {e}")
        return None


def search_rule(query: str) -> Optional[str]:
    """搜索规则信息

    Args:
        query: 规则关键词或规则编号

    Returns:
        规则文本，如果未找到则返回 None
    """
    try:
        import rule_search

        result = rule_search.search(query)

        if not result:
            return None

        # rule_search.search() 返回 dict: {'type': 'keyword'|'cr'|'none', 'results': [...]}
        if isinstance(result, dict):
            rtype = result.get('type', 'none')
            results = result.get('results', [])
            if not results:
                return None

            # 格式化结果
            parts = []
            for r in results[:5]:
                parts.append(f"[{r.get('file','')}:L{r.get('line','')}] {r.get('text','')}")
            return '\n'.join(parts)

        return str(result) if result else None

    except ImportError:
        print("警告: rule_search 模块未找到")
        return None
    except Exception as e:
        print(f"搜索规则时出错: {e}")
        return None


def translate_card_name(name: str) -> Optional[str]:
    """翻译卡牌名称

    Args:
        name: 卡牌名称（中文或英文）

    Returns:
        翻译后的名称，如果未找到则返回 None
    """
    try:
        import name_translator

        result = name_translator.translate(name)

        if not result:
            return None

        # name_translator.translate() 返回 dict: {name, translated_name, lang, ...}
        if isinstance(result, dict):
            return result.get("translated_name") or result.get("name")

        return str(result)

    except ImportError:
        print("警告: name_translator 模块未找到")
        return None
    except Exception as e:
        print(f"翻译卡牌名称时出错: {e}")
        return None


# 工具描述（用于 LLM function calling）
TOOLS_DESCRIPTION = [
    {
        "type": "function",
        "function": {
            "name": "resolve_card",
            "description": "解析万智牌短名、数字、绰号、半截牌名、套牌简称或组合技简称；返回候选、分数、是否需要追问。遇到 2099、blue farm、breach LED、frog 这类输入时必须先用它，而不是直接 search_card。",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "用户输入的牌名、简称、套牌名或组合技片段"
                    },
                    "format": {
                        "type": "string",
                        "enum": ["judge", "cedh", "duel-commander", "modern"],
                        "description": "问题语境，默认 judge"
                    },
                    "intent": {
                        "type": "string",
                        "description": "用户意图，例如 card、commander、deck、combo、interaction、archetype"
                    },
                    "require_meta_evidence": {
                        "type": "boolean",
                        "description": "当用户询问当前 meta、占比、强度或赛制环境时设为 true；若候选没有该赛制 meta 证据，则必须追问或降级回答"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_card",
            "description": "搜索万智牌卡牌信息，包括卡牌名称、法术力费用、类型、规则文本等",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "卡牌名称（中文或英文）"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_rule",
            "description": "搜索万智牌规则信息，包括规则文本和解释",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "规则关键词或规则编号（如 702.12）"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "translate_card_name",
            "description": "翻译万智牌卡牌名称（中英文互译）",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "卡牌名称（中文或英文）"
                    }
                },
                "required": ["name"]
            }
        }
    }
]


# 工具函数映射
TOOLS_MAP = {
    "resolve_card": resolve_card,
    "search_card": search_card,
    "search_rule": search_rule,
    "translate_card_name": translate_card_name,
}
