#!/usr/bin/env python3
"""测试每日早报生成（不推送）"""
import os
import sys

from test_bootstrap import BOT_ROOT, setup_test_env

setup_test_env()

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as OneBotV11Adapter
nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(OneBotV11Adapter)

# 测试 build_news（不加载定时任务，只测生成）
from pathlib import Path as _P

# 直接导入 daily_news 的函数
import importlib.util
spec = importlib.util.spec_from_file_location("daily_news_test", str(BOT_ROOT / "plugins/daily_news/__init__.py"))
# 先手动 import 依赖
import sys
sys.path.insert(0, str(_P(".")))

print("=== 测试每日早报生成 ===")
print()

from datetime import datetime

# 测试 Scryfall 数据
print("--- 1. Scryfall 系列数据 ---")
try:
    # 手动执行函数
    import json, urllib.request
    url = "https://api.scryfall.com/sets"
    req = urllib.request.Request(url, headers={"User-Agent": "mtg-bot/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    today = datetime.now().strftime("%Y-%m-%d")
    week_ago = (datetime.now() - __import__("datetime").timedelta(days=7)).strftime("%Y-%m-%d") if hasattr(__import__("datetime"), "timedelta") else today

    from datetime import timedelta
    week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    week_later = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

    recent = []
    upcoming = []
    for s in data.get("data", []):
        released = s.get("released_at", "")
        name = s.get("name", "")
        set_type = s.get("set_type", "")
        card_count = s.get("card_count", 0)
        if set_type in ("token", "memorabilia", "ministry", "alchemy", "masterpiece", "plane", "scheme", "vanguard", "arsenal", "spellbook"):
            continue
        if card_count < 20:
            continue
        if week_ago <= released <= today:
            recent.append(f"  {name} ({s.get('code','').upper()}) - {released}")
        elif today < released <= week_later:
            upcoming.append(f"  {name} ({s.get('code','').upper()}) - {released}")

    if recent:
        print("最近发售:")
        for r in sorted(recent, reverse=True)[:3]:
            print(r)
    else:
        print("  无近期发售")

    if upcoming:
        print("即将发售:")
        for u in sorted(upcoming)[:3]:
            print(u)
    else:
        print("  无即将发售")

    print("  PASS")
except Exception as e:
    print(f"  FAIL: {e}")

# 测试 LLM 小贴士
print()
print("--- 2. LLM 每日小贴士 ---")
try:
    from openai import OpenAI
    client = OpenAI(
        api_key=os.environ["DASHSCOPE_API_KEY"],
        base_url=os.environ["LLM_BASE_URL"]
    )
    completion = client.chat.completions.create(
        model=os.environ["DASHSCOPE_MODEL"],
        messages=[
            {"role": "system", "content": "你是万智牌智能助手。请生成一段简短的每日万智牌小贴士（100-150字），内容可以是规则技巧、套牌构建建议等。"},
            {"role": "user", "content": "请生成今天的每日万智牌小贴士。"}
        ],
        stream=False
    )
    tip = completion.choices[0].message.content
    print(f"  小贴士: {tip[:150]}")
    print("  PASS")
except Exception as e:
    print(f"  FAIL: {e}")

# 测试完整早报
print()
print("--- 3. 完整早报预览 ---")

# 直接导入 daily_news 模块的 build_news
import types
sys.path.insert(0, "plugins")

# 手动加载
exec(open(BOT_ROOT / "plugins/daily_news/__init__.py").read().split("@scheduler")[0])  # 只执行函数定义部分
try:
    news = build_news()
    print(news)
    print()
    print(f"长度: {len(news)} 字符")
    print("  PASS")
except Exception as e:
    print(f"  FAIL: {e}")
    import traceback
    traceback.print_exc()
