"""万智牌竞技指挥官 QQ 机器人插件"""

from nonebot import get_driver
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="万智牌助手",
    description="万智牌竞技指挥官智能助手，提供规则查询、牌张查询、套牌建议等功能",
    usage="@机器人 + 问题，例如：@专属机器人 泰莎的 Oracle 怎么结算？",
)

try:
    get_driver()
except ValueError:
    # 允许本地测试直接导入 mtg_bot.tools / mtg_bot.llm。
    # 正式运行时 bot.py 会先 nonebot.init()，再通过 load_plugin 触发 handler 注册。
    pass
else:
    from . import handler
