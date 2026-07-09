"""每日早报推送插件"""

import os
import json
import urllib.request
from datetime import datetime, timedelta

from nonebot import get_bot, require
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import MessageSegment

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

# 配置
PUSH_GROUP_ID = int(os.getenv("PUSH_GROUP_ID", "0"))
PUSH_HOUR = int(os.getenv("PUSH_HOUR", "9"))
PUSH_MINUTE = int(os.getenv("PUSH_MINUTE", "0"))
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")
DASHSCOPE_MODEL = os.getenv("DASHSCOPE_MODEL", "glm-5.1")


def _http_get_json(url, timeout=15):
    """简单的 HTTP GET"""
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "mtg-bot/1.0",
            "Accept": "application/json"
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        logger.warning(f"HTTP 请求失败 {url}: {e}")
        return None


def fetch_scryfall_sets():
    """获取最近发售和即将发售的系列"""
    data = _http_get_json("https://api.scryfall.com/sets")
    if not data or "data" not in data:
        return []

    today = datetime.now().strftime("%Y-%m-%d")
    week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    week_later = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

    recent = []
    upcoming = []

    for s in data["data"]:
        released = s.get("released_at", "")
        name = s.get("name", "")
        code = s.get("code", "")
        set_type = s.get("set_type", "")
        card_count = s.get("card_count", 0)

        # 过滤掉不重要的类型
        if set_type in ("token", "memorabilia", "ministry", "alchemy",
                        "masterpiece", "plane", "scheme", "vanguard",
                        "arsenal", "spellbook"):
            continue
        if card_count < 20:
            continue

        if week_ago <= released <= today:
            recent.append({"name": name, "code": code, "date": released, "type": set_type})
        elif today < released <= week_later:
            upcoming.append({"name": name, "code": code, "date": released, "type": set_type})

    # 按日期排序
    recent.sort(key=lambda x: x["date"], reverse=True)
    upcoming.sort(key=lambda x: x["date"])

    return recent[:3], upcoming[:3]


def fetch_scryfall_new_cards():
    """获取最近发布的新卡（按发布日期）"""
    today = datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    url = f"https://api.scryfall.com/cards/search?q=is:new+date>{yesterday}&order=released&dir=desc&unique=art"
    data = _http_get_json(url)
    if not data or "data" not in data:
        return []
    cards = []
    for c in data["data"][:5]:
        cards.append({
            "name": c.get("name", ""),
            "set": c.get("set_name", ""),
            "type": c.get("type_line", ""),
            "rarity": c.get("rarity", "")
        })
    return cards


def generate_llm_tip():
    """使用 LLM 生成每日万智牌小贴士"""
    if not DASHSCOPE_API_KEY:
        return "（AI 服务未配置）"

    try:
        from openai import OpenAI
        import time

        client = OpenAI(api_key=DASHSCOPE_API_KEY, base_url=LLM_BASE_URL)

        today_str = datetime.now().strftime("%Y年%m月%d日")
        weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        weekday = weekdays[datetime.now().weekday()]

        messages = [
            {
                "role": "system",
                "content": "你是重庆市竞技指挥官社群的万智牌智能助手。请生成一段简短的每日万智牌小贴士（100-150字），内容可以是：规则技巧、套牌构建建议、combo 解析、赛场经验等。要求内容有趣、实用、准确。"
            },
            {
                "role": "user",
                "content": f"今天是{today_str} {weekday}，请生成今天的每日万智牌小贴士。"
            }
        ]

        completion = client.chat.completions.create(
            model=DASHSCOPE_MODEL,
            messages=messages,
            stream=False
        )

        return completion.choices[0].message.content or "今天的小贴士生成失败啦~"

    except Exception as e:
        logger.warning(f"LLM 小贴士生成失败: {e}")
        return f"今天的小贴士生成出错：{e}"


def build_news():
    """构建每日早报"""
    now = datetime.now()
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    today_str = now.strftime("%Y年%m月%d日")
    weekday = weekdays[now.weekday()]

    lines = []
    lines.append(f"重庆市竞技指挥官社群 - 每日早报")
    lines.append(f"{today_str} {weekday}")
    lines.append("=" * 30)

    # 1. Scryfall 系列动态
    lines.append("")
    lines.append("系列动态")
    lines.append("-" * 16)
    try:
        recent, upcoming = fetch_scryfall_sets()
        if recent:
            lines.append("最近发售：")
            for s in recent:
                lines.append(f"  - {s['name']} ({s['code'].upper()}) - {s['date']}")
        else:
            lines.append("  近期无新系列发售")

        if upcoming:
            lines.append("即将发售：")
            for s in upcoming:
                lines.append(f"  - {s['name']} ({s['code'].upper()}) - {s['date']}")
        else:
            lines.append("  近期无即将发售的系列")
    except Exception as e:
        lines.append(f"  数据获取失败: {e}")

    # 2. 每日小贴士
    lines.append("")
    lines.append("每日小贴士")
    lines.append("-" * 16)
    try:
        tip = generate_llm_tip()
        lines.append(tip)
    except Exception as e:
        lines.append(f"小贴士生成失败: {e}")

    # 3. 社群信息
    lines.append("")
    lines.append("社群信息")
    lines.append("-" * 16)
    lines.append("  赛制：cEDH (4人pod) + 法禁 (1v1)")
    lines.append("  赛事：T1休闲 / T2锦标赛 / T3全国赛")
    lines.append("  场地：星懿卡牌")
    lines.append("  问题咨询：@机器人 + 问题")

    lines.append("")
    lines.append("祝大家新的一天打牌愉快！")

    return "\n".join(lines)


@scheduler.scheduled_job(
    "cron",
    hour=PUSH_HOUR,
    minute=PUSH_MINUTE,
    id="daily_news",
    timezone="Asia/Shanghai"
)
async def daily_news_push():
    """每天定时推送早报到群"""
    if not PUSH_GROUP_ID:
        logger.warning("[每日早报] 未配置 PUSH_GROUP_ID，跳过推送")
        return

    logger.info("[每日早报] 开始生成并推送...")

    try:
        news = build_news()
        bot = get_bot()

        # 分段发送（QQ 消息长度限制）
        max_len = 2000
        if len(news) <= max_len:
            await bot.send_group_msg(group_id=PUSH_GROUP_ID, message=MessageSegment.text(news))
        else:
            chunks = [news[i:i+max_len] for i in range(0, len(news), max_len)]
            for i, chunk in enumerate(chunks):
                await bot.send_group_msg(group_id=PUSH_GROUP_ID, message=MessageSegment.text(chunk))

        logger.info("[每日早报] 推送完成")
    except Exception as e:
        logger.error(f"[每日早报] 推送失败: {e}")
