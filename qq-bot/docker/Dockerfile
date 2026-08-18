# 万智牌 QQ 机器人 Docker 镜像
# 多阶段构建: Python 依赖安装 + NapCat 运行时

# 阶段1: 安装 Python 依赖
FROM python:3.10-slim AS builder
WORKDIR /build
COPY qq-bot/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

# 阶段2: 最终镜像 (基于 NapCat)
FROM mlikiowa/napcat-docker:v4.18.8

# 安装 Python3 和 pip (NapCat 镜像可能没有)
USER root
RUN apt-get update && apt-get install -y --fix-broken && \
    apt-get install -y \
    python3-pip \
    python3-venv \
    python3-setuptools \
    python3-wheel \
    && rm -rf /var/lib/apt/lists/*

# 直接安装 Python 依赖（不依赖 builder 阶段的复制）
COPY qq-bot/requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com && \
    rm /tmp/requirements.txt

# 设置工作目录
WORKDIR /app/bot

# 复制机器人代码
COPY qq-bot/bot.py .
COPY qq-bot/plugins/ ./plugins/

# 复制知识库
COPY wiki/ /app/wiki/
COPY raw/ /app/raw/

# 复制 skill 定义
COPY skill/ /app/skill/

# 复制 agent 定义
COPY agent/ /app/agent/

# 暴露端口
EXPOSE 8080 6099

# 环境变量
ENV PYTHONUNBUFFERED=1
ENV WIKI_PATH=/app/wiki
ENV RAW_PATH=/app/raw
ENV SKILL_PATH=/app/skill
ENV AGENT_PATH=/app/agent
ENV DASHSCOPE_API_KEY=""
ENV DASHSCOPE_MODEL=glm-5.1
ENV LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
ENV PUSH_GROUP_ID=1054293271
ENV PUSH_HOUR=9
ENV PUSH_MINUTE=0
ENV TZ=Asia/Shanghai

# 启动脚本
COPY qq-bot/docker/start.sh /start.sh
RUN chmod +x /start.sh

# 覆盖 NapCat 的 ENTRYPOINT，使用我们自己的启动脚本
ENTRYPOINT []
CMD ["/start.sh"]
