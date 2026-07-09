#!/usr/bin/env python3
"""测试对话上下文 + glm-5.1"""
import time, asyncio

from test_bootstrap import setup_test_env

setup_test_env()

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as OneBotV11Adapter
nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(OneBotV11Adapter)
nonebot.load_plugin("mtg_bot")

from mtg_bot.llm import MTGAssistant, _conversation_cache, _get_session_key

async def test():
    assistant = MTGAssistant()
    print("模型:", assistant.model)
    print()

    # 模拟同一用户的连续对话
    group_id = 1054293271
    user_id = 398103524

    # 第1轮
    print("=" * 50)
    print("第1轮")
    print("用户: 法禁赛制起始生命值是多少？")
    start = time.time()
    r1 = await assistant.chat("法禁赛制起始生命值是多少？", group_id, user_id)
    print("机器人:", r1[:200])
    print("耗时: %.1fs" % (time.time() - start))
    print()

    # 第2轮（带上下文，应该知道"它"指的是什么）
    print("=" * 50)
    print("第2轮（测试上下文）")
    print("用户: 那cEDH呢？")
    start = time.time()
    r2 = await assistant.chat("那cEDH呢？", group_id, user_id)
    print("机器人:", r2[:200])
    print("耗时: %.1fs" % (time.time() - start))
    print()

    # 第3轮（继续上下文）
    print("=" * 50)
    print("第3轮（继续上下文）")
    print("用户: 这两个赛制有什么主要区别？")
    start = time.time()
    r3 = await assistant.chat("这两个赛制有什么主要区别？", group_id, user_id)
    print("机器人:", r3[:300])
    print("耗时: %.1fs" % (time.time() - start))
    print()

    # 验证上下文是否被保存
    print("=" * 50)
    print("缓存状态:")
    key = _get_session_key(group_id, user_id)
    print("缓存条数:", len(_conversation_cache.get(key, [])))
    print()

    # 检查第2轮是否正确理解了上下文
    has_40 = "40" in r2
    has_context = "cEDH" in r2 or "竞技" in r2
    print("上下文测试:")
    if has_40 and has_context:
        print("  PASS  第2轮正确理解了上下文（cEDH=40血）")
    else:
        print("  FAIL  第2轮可能没有理解上下文")
    print()
    print("ALL DONE")

asyncio.run(test())
