#!/usr/bin/env python3
"""Conversation smoke tests for the MTG assistant with project skills loaded."""

from __future__ import annotations

import asyncio
import os
import time
from typing import Callable

from test_bootstrap import setup_test_env

setup_test_env()

from mtg_bot.llm import MTGAssistant, _conversation_cache, _get_session_key
from mtg_bot.tools import resolve_card, search_rule


def check(name: str, condition: bool, detail: str = "") -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"  {status}  {name}{('  ' + detail) if detail else ''}")
    return condition


def contains_all(text: str, needles: list[str]) -> bool:
    return all(n.lower() in text.lower() for n in needles)


def contains_any(text: str, needles: list[str]) -> bool:
    return any(n.lower() in text.lower() for n in needles)


def run_static_checks() -> bool:
    print("=" * 60)
    print("静态工具/知识检查")
    print("=" * 60)
    ok = True

    r = resolve_card("2099", format="duel-commander", intent="commander")
    ok &= check(
        "法禁 2099 解析到 Spider-Man 2099",
        r is not None and r.get("selected") == "Spider-Man 2099" and not r.get("needs_clarification"),
        str(r)[:180],
    )

    r = resolve_card("blue farm", format="cedh", intent="deck")
    ok &= check(
        "cEDH blue farm 解析到 Tymna/Kraum",
        r is not None and "Tymna" in (r.get("selected") or "") and "Kraum" in (r.get("selected") or ""),
        str(r)[:180],
    )

    r = resolve_card("breach LED", format="judge", intent="interaction")
    ok &= check(
        "多组件互动解析出两个组件",
        r is not None and len(r.get("components", [])) >= 2,
        str(r)[:180],
    )

    rules = search_rule("723.1a")
    ok &= check("CR 723.1a 可检索", rules is not None and "Multiple player-controlling effects" in rules, str(rules)[:120])

    rules = search_rule("714.4")
    ok &= check("CR 714.4 新版 Saga 条件可检索", rules is not None and "one or more chapter abilities" in rules, str(rules)[:120])

    return bool(ok)


async def ask(
    assistant: MTGAssistant,
    question: str,
    validators: list[tuple[str, Callable[[str], bool]]],
    group_id: int,
    user_id: int,
) -> bool:
    print()
    print("-" * 60)
    print("用户:", question)
    start = time.time()
    answer = await asyncio.wait_for(assistant.chat(question, group_id=group_id, user_id=user_id), timeout=120)
    elapsed = time.time() - start
    print(f"耗时: {elapsed:.1f}s | 回复长度: {len(answer)}")
    print(answer[:900].replace("\n\n", "\n"))

    ok = True
    for name, validator in validators:
        ok &= check(name, validator(answer), answer[:120])
    return bool(ok)


async def run_llm_checks() -> bool:
    if not os.getenv("DASHSCOPE_API_KEY"):
        print()
        print("跳过 LLM 连续问答：未配置 DASHSCOPE_API_KEY")
        return True

    print()
    print("=" * 60)
    print("LLM 连续问答检查")
    print("=" * 60)

    assistant = MTGAssistant()
    group_id = 20260709
    user_id = 398103524
    _conversation_cache.pop(_get_session_key(group_id, user_id), None)

    cases = [
        (
            "4人游戏场上有两张反对派密探，这时候有一位不控制反对派密探的玩家执行搜寻牌库的操作，要怎么处理",
            [
                ("引用/命中控制玩家规则", lambda a: "723" in a or "操控" in a),
                ("说明最后创建的效应生效", lambda a: contains_any(a, ["最后", "后创建", "last", "覆盖"])),
            ],
        ),
        (
            "如果后进场的那张反对派密探被去除了呢？",
            [
                ("沿用上轮反对派密探上下文", lambda a: contains_any(a, ["反对派密探", "Opposition Agent", "剩下", "另一张"])),
                ("说明仍按当前存在的控制效应处理", lambda a: contains_any(a, ["继续", "剩下", "生效", "操控"])),
            ],
        ),
        (
            "红月和克撒传是如何互动的",
            [
                ("说明变山并失去能力", lambda a: contains_any(a, ["山脉", "Mountain"]) and contains_any(a, ["失去", "没有", "不能"])),
                ("引用新版 Saga/地类别规则", lambda a: contains_any(a, ["305.7", "714.4", "703.4f", "704.5s"])),
            ],
        ),
        (
            "那它还能找构组物吗？",
            [
                ("沿用克撒传上下文", lambda a: contains_any(a, ["克撒传", "Urza"])),
                ("结论为不能找构组物", lambda a: contains_any(a, ["不能", "不会", "无法"]) and contains_any(a, ["构组物", "Construct", "找"])),
            ],
        ),
        (
            "法禁里 2099 这个指挥官现在怎么样？",
            [
                ("使用法禁语境解析 2099", lambda a: "Spider-Man 2099" in a and "Miguel O'Hara" not in a),
                ("带赛制 meta 证据来源", lambda a: "meta evidence" in a and contains_any(a, ["MTGDecks", "MTGTop8"])),
                ("暴露资料/版本边界", lambda a: contains_any(a, ["资料不足", "as_of", "banlist", "版本", "来源"])),
            ],
        ),
        (
            "那 cEDH 里 blue farm 指什么？",
            [
                ("使用 cEDH 语境解析 blue farm", lambda a: contains_any(a, ["Tymna", "Kraum", "Blue Farm"])),
                ("没有沿用上一轮法禁 2099 为主体", lambda a: not contains_all(a, ["2099", "Spider-Man"])),
            ],
        ),
    ]

    ok = True
    for question, validators in cases:
        ok &= await ask(assistant, question, validators, group_id, user_id)

    session_key = _get_session_key(group_id, user_id)
    ok &= check("同一用户上下文已保存", len(_conversation_cache.get(session_key, [])) >= 8, str(_conversation_cache.keys()))
    return bool(ok)


async def main() -> int:
    ok = run_static_checks()
    ok &= await run_llm_checks()
    print()
    print("=" * 60)
    print("ALL PASSED" if ok else "FAILED")
    print("=" * 60)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
