# QQ 机器人快速启动指南

## 🚀 5 分钟快速开始

### 1. 获取 DashScope API Key

访问 https://dashscope.console.aliyun.com/apiKey 创建 API Key（有免费额度）

### 2. 配置环境变量

```bash
cd qq-bot
cp .env.example .env
nano .env
```

填入你的 API Key：
```env
DASHSCOPE_API_KEY=sk-你的密钥
```

### 3. 安装依赖

```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install nonebot2 nonebot-adapter-onebot dashscope python-dotenv pydantic
```

### 4. 下载 NapCat

访问 https://github.com/NapNeko/NapCatQQ/releases 下载最新版本，解压到 `napcat/NapCat` 目录

### 5. 启动机器人

**终端 1 - 启动 NoneBot2:**
```bash
python bot.py
```

**终端 2 - 启动 NapCat:**
```bash
cd napcat/NapCat
./launcher.sh
```

首次启动 NapCat 会显示二维码，用机器人 QQ 号扫码登录。

### 6. 测试

在 QQ 群里 @机器人 并提问：
```
@专属机器人 泰莎的 Oracle 怎么结算？
```

---

## 📁 项目结构

```
qq-bot/
├── bot.py                 # 主入口
├── .env                   # 配置文件（需创建）
├── plugins/mtg_bot/       # 万智牌插件
│   ├── handler.py         # 消息处理
│   ├── llm.py            # AI 集成
│   ├── tools.py          # 工具调用
│   └── knowledge.py      # 知识库
├── napcat/
│   ├── config.json       # NapCat 配置
│   └── NapCat/           # NapCat 程序（需下载）
└── deploy/
    └── README.md         # 详细文档
```

---

## 🔧 常用命令

```bash
# 启动机器人
python bot.py

# 后台运行
nohup python bot.py > bot.log 2>&1 &

# 查看日志
tail -f bot.log

# 停止机器人
pkill -f "python bot.py"
```

---

## ❓ 常见问题

**Q: 机器人不响应？**
- 检查 NapCat 是否已登录
- 检查消息是否 @了机器人
- 查看日志：`tail -f bot.log`

**Q: AI 回复很慢？**
- 检查网络连接
- 尝试更快的模型：改 `.env` 中 `DASHSCOPE_MODEL=qwen-plus`

**Q: 工具调用失败？**
- 确认 `raw/tools/mtg_wiki/` 目录存在
- 检查工具依赖是否安装

---

## 📚 详细文档

完整部署指南请查看：[deploy/README.md](deploy/README.md)

---

## 🎯 功能列表

- ✅ 规则查询（引用具体规则编号）
- ✅ 卡牌查询（中英文名称）
- ✅ 套牌建议（基于竞技 meta）
- ✅ 牌张互动解释
- ✅ 法禁/cEDH 策略建议
- ✅ 知识库 RAG（自动检索 wiki/）
- ✅ 工具调用（card_search, rule_search 等）

---

**祝使用愉快！** 🎮
