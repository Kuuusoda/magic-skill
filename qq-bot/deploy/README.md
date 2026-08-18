# 万智牌竞技指挥官 QQ 机器人部署指南

## 📋 目录

- [架构概览](#架构概览)
- [前置要求](#前置要求)
- [部署步骤](#部署步骤)
- [NapCat 配置](#napcat-配置)
- [启动机器人](#启动机器人)
- [常见问题](#常见问题)

---

## 架构概览

```
┌─────────────┐
│   QQ 客户端  │
└──────┬──────┘
       │ OneBot 协议
       ▼
┌─────────────┐
│   NapCat    │  ← QQ 协议层
└──────┬──────┘
       │ WebSocket
       ▼
┌─────────────┐
│  NoneBot2   │  ← 机器人框架
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  MTG Plugin │  ← 万智牌插件
└──────┬──────┘
       │
       ├──────────────┬──────────────┐
       ▼              ▼              ▼
┌────────────┐ ┌────────────┐ ┌────────────┐
│ DashScope  │ │ 知识库 RAG │ │  工具调用  │
│  (Qwen)    │ │  (wiki/)   │ │(card_search│
└────────────┘ └────────────┘ └────────────┘
```

**组件说明：**
- **NapCat**: QQ 协议实现，负责与 QQ 服务器通信
- **NoneBot2**: 机器人框架，处理消息路由和插件管理
- **MTG Plugin**: 万智牌插件，实现具体功能
- **DashScope**: 通义千问 API，提供 AI 能力
- **知识库**: 从 wiki/ 和 raw/ 加载的万智牌知识
- **工具**: card_search、rule_search 等查询工具

---

## 前置要求

### 服务器要求

- **操作系统**: Linux (推荐 Ubuntu 20.04+) / Windows / macOS
- **Python**: 3.10 或更高版本
- **内存**: 至少 2GB RAM
- **网络**: 可访问 QQ 服务器和 DashScope API

### 账号要求

1. **DashScope API Key**
   - 访问 https://dashscope.console.aliyun.com/
   - 注册阿里云账号
   - 开通 DashScope 服务
   - 创建 API Key（有免费额度）

2. **QQ 账号**
   - 用于机器人的 QQ 号
   - 建议使用小号，避免主号风险

---

## 部署步骤

### 步骤 1: 克隆项目

```bash
cd /path/to/magic
cd qq-bot
```

### 步骤 2: 运行部署脚本

```bash
chmod +x deploy/setup.sh
./deploy/setup.sh
```

脚本会自动：
- 创建 Python 虚拟环境
- 安装所有依赖
- 创建配置文件模板
- 生成启动脚本

### 步骤 3: 配置 DashScope API Key

编辑 `.env` 文件：

```bash
nano .env
```

填入你的 API Key：

```env
DASHSCOPE_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
DASHSCOPE_MODEL=qwen-max
```

**获取 API Key：**
1. 访问 https://dashscope.console.aliyun.com/apiKey
2. 点击"创建新的 API-KEY"
3. 复制生成的 Key

### 步骤 4: 安装 NapCat

NapCat 是 QQ 协议层，需要单独安装。

**Linux:**

```bash
cd napcat
# 下载最新版本（访问 https://github.com/NapNeko/NapCatQQ/releases 获取最新链接）
wget https://github.com/NapNeko/NapCatQQ/releases/download/v4.1.0/NapCat.Shell.zip
unzip NapCat.Shell.zip
mv NapCat.Shell NapCat
cd NapCat
chmod +x launcher.sh
```

**Windows:**
1. 访问 https://github.com/NapNeko/NapCatQQ/releases
2. 下载 `NapCat.Shell.zip`
3. 解压到 `napcat/NapCat` 目录

**macOS:**
```bash
cd napcat
brew install node  # NapCat 依赖 Node.js
# 然后下载 NapCat（同上）
```

### 步骤 5: 配置 NapCat

编辑 `napcat/config.json`（已预配置好，通常无需修改）：

```json
{
  "network": {
    "websocketClients": [
      {
        "name": "nonebot",
        "host": "127.0.0.1",
        "port": 8080,
        "enable": true
      }
    ]
  }
}
```

---

## NapCat 配置

### 首次启动 NapCat

```bash
cd napcat/NapCat
./launcher.sh
```

首次启动会显示二维码，使用机器人 QQ 号扫码登录。

**注意事项：**
- 扫码登录需要在有图形界面的环境（或使用 VNC/Terminal）
- 登录后 NapCat 会保持会话
- 如果掉线，需要重新扫码

### NapCat 常用命令

```bash
# 启动
./launcher.sh

# 后台运行
nohup ./launcher.sh > napcat.log 2>&1 &

# 查看日志
tail -f napcat.log

# 停止
pkill -f NapCat
```

---

## 启动机器人

### 方法 1: 使用启动脚本（推荐）

```bash
cd qq-bot
./start.sh
```

这会同时启动 NoneBot2 和提示你启动 NapCat。

### 方法 2: 手动启动

**终端 1 - 启动 NoneBot2:**

```bash
cd qq-bot
source venv/bin/activate
python bot.py
```

**终端 2 - 启动 NapCat:**

```bash
cd qq-bot/napcat/NapCat
./launcher.sh
```

### 方法 3: 使用 systemd（生产环境）

创建服务文件：

```bash
sudo nano /etc/systemd/system/mtg-bot.service
```

内容：

```ini
[Unit]
Description=MTG QQ Bot
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/magic/qq-bot
ExecStart=/path/to/magic/qq-bot/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

启用服务：

```bash
sudo systemctl daemon-reload
sudo systemctl enable mtg-bot
sudo systemctl start mtg-bot
sudo systemctl status mtg-bot
```

---

## 常见问题

### Q1: NapCat 扫码后无法登录

**原因：** QQ 安全检测或账号异常

**解决：**
1. 确保 QQ 号已实名认证
2. 在手机 QQ 上正常登录几天后再尝试
3. 检查服务器 IP 是否被风控

### Q2: NoneBot2 启动后收不到消息

**检查：**
1. NapCat 是否已启动并登录
2. 检查 WebSocket 连接：NoneBot2 日志应显示 "WebSocket connected"
3. 检查端口 8080 是否被占用：`lsof -i :8080`

### Q3: AI 回复很慢或超时

**原因：** DashScope API 响应慢或网络问题

**解决：**
1. 检查服务器网络：`ping api.dashscope.aliyuncs.com`
2. 查看 DashScope 控制台是否有错误
3. 尝试使用更快的模型：在 `.env` 中改 `DASHSCOPE_MODEL=qwen-plus`

### Q4: 工具调用失败（card_search 等）

**原因：** 工具路径配置错误或依赖缺失

**检查：**
1. 确认 `raw/tools/mtg_wiki/` 目录存在
2. 检查工具依赖：`cd raw/tools/mtg_wiki && python3 -c "import card_search"`
3. 查看 NoneBot2 日志中的错误信息

### Q5: 知识库加载失败

**原因：** wiki/ 或 raw/ 路径不正确

**解决：**
1. 检查 `.env` 中的 `WIKI_PATH` 和 `RAW_PATH`
2. 确保路径是相对于 `qq-bot` 目录的
3. 重启 NoneBot2 重新加载知识库

### Q6: 机器人在群里不响应

**检查：**
1. 机器人是否已加入群聊
2. 消息是否 @了机器人
3. 检查 NoneBot2 日志是否有错误
4. 确认群聊没有被设置为"仅管理员可发言"

---

## 监控和日志

### 查看 NoneBot2 日志

```bash
# 实时查看
tail -f logs/nonebot.log

# 查看最近 100 行
tail -n 100 logs/nonebot.log
```

### 查看 NapCat 日志

```bash
# 如果使用 nohup 启动
tail -f napcat/NapCat/napcat.log
```

### 监控资源使用

```bash
# 查看进程
ps aux | grep -E "(python|NapCat)"

# 查看内存和 CPU
top -p $(pgrep -f "python bot.py")
```

---

## 更新和维护

### 更新机器人代码

```bash
cd /path/to/magic
git pull
cd qq-bot
source venv/bin/activate
pip install -r requirements.txt  # 如果有新依赖
# 重启服务
sudo systemctl restart mtg-bot
```

### 更新知识库

知识库会在机器人启动时自动加载。如果 wiki/ 有更新：

```bash
sudo systemctl restart mtg-bot
```

### 备份

```bash
# 备份配置
cp .env .env.backup

# 备份日志
tar -czf logs-$(date +%Y%m%d).tar.gz logs/
```

---

## 安全建议

1. **不要将 `.env` 文件提交到 Git**
   ```bash
   echo ".env" >> .gitignore
   ```

2. **使用防火墙限制端口**
   ```bash
   sudo ufw allow 22/tcp  # SSH
   sudo ufw enable
   ```

3. **定期更新系统和依赖**
   ```bash
   sudo apt update && sudo apt upgrade
   pip install --upgrade -r requirements.txt
   ```

4. **监控日志异常**
   - 定期检查日志中的错误和警告
   - 关注异常的 API 调用量

---

## 联系支持

如果遇到问题无法解决：

- **NoneBot2 文档**: https://nonebot.dev/
- **NapCat 文档**: https://napneko.github.io/
- **DashScope 文档**: https://help.aliyun.com/zh/dashscope/
- **项目 Issue**: https://github.com/your-repo/issues

---

## 附录：完整文件结构

```
qq-bot/
├── bot.py                      # 主入口
├── pyproject.toml              # 依赖配置
├── .env                        # 环境变量（需创建）
├── .env.example                # 环境变量模板
├── start.sh                    # 启动脚本
├── plugins/
│   └── mtg_bot/
│       ├── __init__.py         # 插件初始化
│       ├── handler.py          # 消息处理
│       ├── llm.py              # DashScope 集成
│       ├── tools.py            # 工具封装
│       └── knowledge.py        # 知识库 RAG
├── napcat/
│   ├── config.json             # NapCat 配置
│   └── NapCat/                 # NapCat 程序（需下载）
└── deploy/
    ├── setup.sh                # 部署脚本
    └── README.md               # 本文档
```

---

**最后更新**: 2026-01-XX
**版本**: 1.0.0
