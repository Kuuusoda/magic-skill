#!/bin/bash
# 万智牌 QQ 机器人部署脚本

set -e

echo "=========================================="
echo "万智牌竞技指挥官 QQ 机器人部署脚本"
echo "=========================================="

# 检查 Python 版本
echo "[1/6] 检查 Python 版本..."
python3 --version || { echo "错误: 未找到 Python 3"; exit 1; }

# 创建虚拟环境
echo "[2/6] 创建 Python 虚拟环境..."
python3 -m venv venv
source venv/bin/activate

# 安装依赖
echo "[3/6] 安装 Python 依赖..."
pip install --upgrade pip
pip install nonebot2 nonebot-adapter-onebot dashscope python-dotenv pydantic

# 创建 .env 文件
echo "[4/6] 创建配置文件..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "已创建 .env 文件，请编辑并填入你的 DashScope API Key"
    echo "文件位置: $(pwd)/.env"
fi

# 检查 NapCat
echo "[5/6] 检查 NapCat..."
if [ ! -d "napcat/NapCat" ]; then
    echo "警告: NapCat 未安装"
    echo "请手动下载 NapCat: https://github.com/NapNeko/NapCatQQ/releases"
    echo "下载后解压到 napcat/NapCat 目录"
else
    echo "NapCat 已安装"
fi

# 创建启动脚本
echo "[6/6] 创建启动脚本..."
cat > start.sh << 'EOF'
#!/bin/bash
# 启动 QQ 机器人

echo "启动 NoneBot2..."
source venv/bin/activate
python bot.py &
BOT_PID=$!

echo "NoneBot2 已启动 (PID: $BOT_PID)"
echo "现在请启动 NapCat..."
echo "按 Ctrl+C 停止机器人"

wait $BOT_PID
EOF

chmod +x start.sh

echo ""
echo "=========================================="
echo "部署完成！"
echo "=========================================="
echo ""
echo "下一步操作："
echo "1. 编辑 .env 文件，填入你的 DashScope API Key"
echo "   nano .env"
echo ""
echo "2. 下载并安装 NapCat"
echo "   访问: https://github.com/NapNeko/NapCatQQ/releases"
echo "   下载对应系统的版本，解压到 napcat/NapCat 目录"
echo ""
echo "3. 启动机器人"
echo "   ./start.sh"
echo ""
echo "4. 启动 NapCat 并登录 QQ"
echo "   cd napcat/NapCat"
echo "   ./launcher.sh"
echo ""
echo "详细说明请查看 deploy/README.md"
echo ""
