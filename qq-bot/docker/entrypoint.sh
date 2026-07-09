#!/bin/bash
# 容器启动脚本

set -e

echo "=========================================="
echo "万智牌 QQ 机器人启动中..."
echo "=========================================="

# 检查必要的环境变量
if [ -z "$DASHSCOPE_API_KEY" ]; then
    echo "错误: 未设置 DASHSCOPE_API_KEY 环境变量"
    echo "请使用 -e DASHSCOPE_API_KEY=your_key 传入"
    exit 1
fi

echo "✓ DashScope API Key 已配置"
echo "✓ 模型: ${DASHSCOPE_MODEL:-qwen-max}"

# 启动 supervisor (管理 NapCat 和 NoneBot2)
echo ""
echo "启动服务..."
echo "- NapCat (QQ 协议层)"
echo "- NoneBot2 (机器人框架)"
echo ""
echo "=========================================="
echo "NapCat WebUI 地址: http://localhost:6099"
echo "请使用浏览器访问上述地址扫码登录 QQ"
echo "=========================================="
echo ""

exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
