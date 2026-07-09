#!/usr/bin/env python3
"""万智牌竞技指挥官 QQ 机器人主入口"""

import sys
from pathlib import Path

# 添加 plugins 目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent / "plugins"))

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as OneBotV11Adapter

nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(OneBotV11Adapter)

# 加载插件
nonebot.load_plugin("mtg_bot")
nonebot.load_plugin("daily_news")

if __name__ == "__main__":
    nonebot.run()
