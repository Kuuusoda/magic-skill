#!/bin/bash
# 启动 NoneBot2 和 NapCat

echo "启动 NoneBot2..."
cd /app/bot
python3 bot.py &
BOT_PID=$!

echo "NoneBot2 PID: $BOT_PID"
echo "启动 NapCat..."

# 设置环境变量减少 GPU 相关错误
export QT_X11_NO_MITSHM=1
export LIBGL_ALWAYS_SOFTWARE=1
export ELECTRON_DISABLE_GPU=1

# 调用 NapCat 的原始 entrypoint（不过滤日志，保留完整输出）
cd /app
exec bash /app/entrypoint.sh
