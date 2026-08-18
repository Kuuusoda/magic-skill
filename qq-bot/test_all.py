#!/usr/bin/env python3
"""全工具测试"""
import time, asyncio

from test_bootstrap import setup_test_env

setup_test_env()

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as OneBotV11Adapter
nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(OneBotV11Adapter)
nonebot.load_plugin("mtg_bot")

from mtg_bot.tools import resolve_card, search_card, search_rule, translate_card_name
from mtg_bot.knowledge import get_knowledge_base
from pathlib import Path

passed = 0
failed = 0

def check(name, condition, detail=""):
    global passed, failed
    if condition:
        passed += 1
        print(f"  PASS  {name}")
    else:
        failed += 1
        print(f"  FAIL  {name}  {detail}")

print("=" * 60)
print("全工具测试（本地/容器通用）")
print("=" * 60)

# 1. resolve_card
print()
print("--- 1. resolve_card ---")
r = resolve_card("2099", format="duel-commander", intent="commander")
check("法禁 2099 消歧", r is not None and r.get("selected") == "Spider-Man 2099", str(r))

r = resolve_card("blue farm", format="cedh", intent="deck")
check("cEDH blue farm 消歧", r is not None and "Tymna" in (r.get("selected") or ""), str(r))

r = resolve_card("breach LED", format="judge", intent="interaction")
check("多组件互动消歧", r is not None and len(r.get("components", [])) >= 2, str(r))

# 2. search_card
print()
print("--- 2. search_card ---")
r = search_card("Sol Ring")
check("Sol Ring", r is not None and r.get("name") == "Sol Ring", str(r))

r = search_card("Lightning Bolt")
check("Lightning Bolt", r is not None, str(r))

r = search_card("Loki Scepter")
check("Loki Scepter", r is not None and "Loki" in r.get("name", ""), str(r))

r = search_card("Thassa Oracle")
check("Thassa Oracle", r is not None, str(r))

r = search_card("Sisay")
check("Sisay", r is not None, str(r))

r = search_card("不存在xyz123")
check("不存在返回None", r is None)

# 3. search_rule
print()
print("--- 3. search_rule ---")
r = search_rule("commander")
check("commander", r is not None and len(r) > 10, str(r)[:80])

r = search_rule("702.16")
check("702.16", r is not None and len(r) > 10, str(r)[:80])

r = search_rule("堆叠")
check("堆叠", r is not None and len(r) > 10, str(r)[:80])

r = search_rule("zzz不存在zzz")
check("不存在返回None", r is None)

# 4. translate_card_name
print()
print("--- 4. translate_card_name ---")
r = translate_card_name("Sol Ring")
check("Sol Ring", r is not None, str(r))

# 5. 知识库
print()
print("--- 5. 知识库 ---")
kb = get_knowledge_base()
r = kb.search("法禁", top_k=3)
check("搜索法禁", len(r) > 0, str(len(r)))

r = kb.search("cedh", top_k=3)
check("搜索cedh", len(r) > 0, str(len(r)))

r = kb.search("Duel Commander", top_k=3)
check("搜索Duel Commander", len(r) > 0, str(len(r)))

ctx = kb.get_context("法禁赛制")
check("上下文含20", "20" in ctx or "Duel" in ctx, ctx[:80])

skill_ctx = kb.get_skill_context()
check("加载skills", "duel-commander-breaker" in skill_ctx and "card_resolve.py" in skill_ctx, skill_ctx[:120])

# 6. LLM
print()
print("--- 6. LLM (限时60s) ---")

async def test_llm():
    from mtg_bot.llm import MTGAssistant
    assistant = MTGAssistant()
    start = time.time()
    result = await assistant.chat("闪电击的规则是什么")
    elapsed = time.time() - start
    check(f"LLM回复({elapsed:.0f}s)", len(result) > 20, result[:80])
    return result

try:
    result = asyncio.run(asyncio.wait_for(test_llm(), timeout=60))
    print(f"  回复前100字: {result[:100]}")
except asyncio.TimeoutError:
    failed += 1
    print("  FAIL  LLM超时(>60s)")
except Exception as e:
    failed += 1
    print(f"  FAIL  LLM错误: {e}")

# 汇总
print()
print("=" * 60)
total = passed + failed
print(f"总计: {total} | 通过: {passed} | 失败: {failed}")
print("ALL PASSED" if failed == 0 else f"FAILED: {failed}")
print("=" * 60)
