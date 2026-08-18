"""消息处理模块 - 处理 QQ 群消息"""

from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from nonebot.rule import to_me
from nonebot.params import EventPlainText

from .llm import get_assistant

# 监听 @机器人 的消息
mtg_handler = on_message(rule=to_me(), priority=10, block=True)


def safe_text(text: str) -> str:
    """确保文本是 UTF-8 安全的纯文本"""
    if not text:
        return ""
    # 移除可能导致编码问题的字符
    import re
    # 只保留常见的 UTF-8 字符
    text = re.sub(r'[^\u0000-\uFFFF]', '', text)
    # 确保可以编码为 UTF-8
    try:
        text.encode('utf-8')
    except:
        # 如果编码失败，使用 ASCII 安全字符
        text = text.encode('ascii', 'ignore').decode('ascii')
    return text

@mtg_handler.handle()
async def handle_mtg_question(
    bot: Bot,
    event: GroupMessageEvent,
    plain_text: str = EventPlainText()
):
    """处理万智牌问题"""

    # 获取用户问题（去除 @提及部分）
    question = plain_text.strip()

    if not question:
        await mtg_handler.finish(safe_text("请 @我 并提问，例如：@专属机器人 泰莎的 Oracle 怎么结算？"))
        return

    # 获取助手实例
    assistant = get_assistant()

    # 发送"正在思考"提示
    await mtg_handler.send(safe_text("正在查询，请稍候..."))

    try:
        # 调用 LLM 助手（传入群ID和用户ID用于上下文管理）
        response = await assistant.chat(question, group_id=event.group_id, user_id=event.user_id)

        # 确保回复是 UTF-8 安全的
        safe_response = safe_text(response)

        if len(safe_response) > 500:
            # 长消息：按段落分割，用合并转发发送
            paragraphs = []
            current = ""
            for line in safe_response.split("\n"):
                if len(current) + len(line) > 800:
                    if current:
                        paragraphs.append(current)
                    current = line + "\n"
                else:
                    current += line + "\n"
            if current:
                paragraphs.append(current)

            # 构建合并转发消息节点
            from nonebot.adapters.onebot.v11 import Message
            nodes = []
            for i, para in enumerate(paragraphs):
                para = para.strip()
                if para:
                    nodes.append(MessageSegment.node_custom(
                        user_id=event.self_id,
                        nickname="万智牌助手",
                        content=para
                    ))

            if nodes:
                await bot.call_api(
                    "send_group_forward_msg",
                    group_id=event.group_id,
                    messages=nodes
                )
            else:
                await mtg_handler.send(MessageSegment.text(safe_response))
        else:
            # 短消息：直接发送
            await mtg_handler.send(MessageSegment.text(safe_response))

    except Exception as e:
        # 错误处理 - 确保错误消息也是安全的
        import traceback
        error_detail = str(e)
        error_msg = safe_text(f"抱歉，处理您的问题时出错了：{error_detail}\n请稍后重试或联系管理员。")
        await mtg_handler.send(MessageSegment.text(error_msg))


# 监听特定命令（可选）
from nonebot import on_command

help_cmd = on_command("help", aliases={"帮助"}, priority=5, block=True)


@help_cmd.handle()
async def handle_help():
    """显示帮助信息"""
    help_text = """🎮 万智牌竞技指挥官助手

使用方法：
@我 + 问题

示例：
• @专属机器人 泰莎的 Oracle 怎么结算？
• @专属机器人 搜索卡牌「闪电击」
• @专属机器人 法禁赛制有什么特殊规则？
• @专属机器人 推荐一套白黑指挥官套牌

功能：
✅ 规则查询（引用具体规则编号）
✅ 卡牌查询（中英文名称）
✅ 套牌建议（基于竞技 meta）
✅ 牌张互动解释
✅ 法禁/cEDH 策略建议

如有问题请联系管理员：球哥
"""
    await help_cmd.finish(help_text)


# 欢迎新成员（可选）
from nonebot import on_notice
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent

welcome = on_notice(priority=50, block=False)


@welcome.handle()
async def handle_welcome(bot: Bot, event: GroupIncreaseNoticeEvent):
    """欢迎新成员"""
    if isinstance(event, GroupIncreaseNoticeEvent):
        # 确保正确获取 user_id 和 group_id
        user_id = int(event.user_id) if hasattr(event, 'user_id') else None
        group_id = int(event.group_id) if hasattr(event, 'group_id') else None

        if user_id and group_id:
            # 使用 Message 对象构建消息
            from nonebot.adapters.onebot.v11 import Message
            welcome_msg = Message()
            welcome_msg.append(MessageSegment.text("欢迎新成员 "))
            welcome_msg.append(MessageSegment.at(user_id))
            welcome_msg.append(MessageSegment.text(" 加入重庆市竞技指挥官社群！\n\n"))
            welcome_msg.append(MessageSegment.text("📋 请阅读群公告了解社群规则\n"))
            welcome_msg.append(MessageSegment.text("🤖 可以 @我 提问万智牌相关问题\n"))
            welcome_msg.append(MessageSegment.text("🎮 输入 /帮助 查看使用指南\n\n"))
            welcome_msg.append(MessageSegment.text("祝您在这里玩得开心！"))

            await bot.send_group_msg(group_id=group_id, message=welcome_msg)
