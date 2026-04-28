# 万智牌原创卡牌生成器

基于项目的万智牌 Wiki 知识库，根据用户输入的设计需求生成一张完全原创的万智牌卡牌。

## 功能特点

- **知识注入**：自动扫描 `wiki/concepts/` 中的规则概念，将用户提及的关键字、机制、牌张类型等相关知识注入 Prompt
- **规则合规**：生成的卡牌严格遵守万智牌完整规则（CR）术语规范
- **双语输出**：同时输出中文和英文的卡牌名称、规则叙述、风味叙述
- **两种模式**：
  1. **Prompt 模式**（默认）：构建优化后的 Prompt，用户可复制到 Claude/ChatGPT 等 LLM 中使用
  2. **API 模式**（可选）：若设置了 `ANTHROPIC_API_KEY`，可直接调用 Claude API 生成卡牌并保存

## 目录结构

```
output/card-generator/
├── generate_card.py          # 主脚本
├── templates/
│   └── prompt_template.md    # Prompt 模板
├── generated/                # 生成的卡牌存放处
└── README.md                 # 本文件
```

## 使用方法

### 1. Prompt 模式（推荐）

```bash
python3 output/card-generator/generate_card.py \
  -p "我想设计一张红色的3费传奇龙，具有飞行和敏捷，进场时可以对任意目标造成2点伤害"
```

脚本会输出一个经过知识增强的 Prompt。你可以直接复制这个 Prompt，粘贴到 Claude 或 ChatGPT 中，由 LLM 生成卡牌。

### 2. API 模式（直接生成）

需要安装 `anthropic` SDK：

```bash
pip install anthropic
export ANTHROPIC_API_KEY="sk-ant-..."
```

然后运行：

```bash
python3 output/card-generator/generate_card.py \
  -p "我想设计一张红色的3费传奇龙，具有飞行和敏捷，进场时可以对任意目标造成2点伤害" \
  --generate \
  -o output/card-generator/generated/dragon-001.md
```

这会在 `generated/` 下同时输出：
- `dragon-001.md` — 美观的 Markdown 格式卡牌
- `dragon-001.json` — 结构化的 JSON 数据

## 设计需求写作建议

为了让生成的卡牌更符合预期，建议在 Prompt 中包含以下信息：

| 要素 | 示例 |
|------|------|
| **颜色** | 红色、蓝白双色、无色 |
| **法术力费用** | 3费、{1}{R}{R}、6费以上 |
| **牌张类型** | 生物、瞬间、神器、鹏洛客、结界 |
| **异能/机制** | 具有循环、闪现、践踏、系命等 |
| **主题/风味** | 巨龙、海盗、时空旅行、机械造物 |
| **强度预期** | 限制赛炸弹、标准赛可用、EDH 娱乐 |

## 示例输出

见 `generated/` 目录下的示例文件：

- [`generated/sample-dragon.md`](generated/sample-dragon.md) — Markdown 格式卡牌「烬翼龙母卡拉达」
- [`generated/sample-dragon.json`](generated/sample-dragon.json) — 对应的结构化 JSON 数据
