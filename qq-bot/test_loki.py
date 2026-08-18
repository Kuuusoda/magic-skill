#!/usr/bin/env python3
"""测试洛基的权杖问题"""
import time, asyncio

from test_bootstrap import setup_test_env

setup_test_env()

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as OneBotV11Adapter
nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(OneBotV11Adapter)
nonebot.load_plugin("mtg_bot")

from mtg_bot.llm import MTGAssistant

async def test():
    assistant = MTGAssistant()
    question = "洛基的权杖在Sisay套牌会有好表现吗"
    print("问题:", question)
    t = time.strftime("%H:%M:%S")
    print("开始:", t)

    start = time.time()
    result = await assistant.chat(question)
    elapsed = time.time() - start

    print("耗时: %.1fs" % elapsed)
    print("长度: %d 字符" % len(result))
    print()
    print(result)

asyncio.run(test())
