# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

# 万智牌通用知识基础设施 (MTG Wiki)

本项目是**万智牌通用知识基础设施**（Magic: The Gathering General-Purpose Knowledge Infrastructure），由 LLM 构建和维护，服务于裁判规则判定、策略研究、内容创作、DIY 卡牌设计等多个消费分支。

## 项目架构

```
┌─────────────────────────────────────────────────────────────┐
│                      OpenClaw Skill                          │
│              skill/mtg-wiki/SKILL.md                        │
│   (description = 触发器，正文仅在命中后加载)                  │
└────────────────────────────┬────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  raw/         │   │  wiki/        │   │  output/      │
│  (不可变数据)  │   │  (LLM知识库)   │   │  (生成产物)    │
│  CR/MTR/IPG   │   │  concepts/    │   │  分析报告     │
│  牌张数据库    │   │  entities/    │   │  周报         │
│  Python工具   │   │  synthesis/   │   │  表格         │
└───────────────┘   │  branches/    │   └───────────────┘
                    │  decision-trees│
                    └───────────────┘
```

**数据流**：`raw/` → Ingest → `wiki/` → Query → 用户答案 + `output/`

## 目录结构

```
<project-root>/
├── skill/                      # OpenClaw Skill（触发器）
│   └── mtg-wiki/
│       └── SKILL.md           # YAML frontmatter + 使用说明
├── raw/                        # 原始资料（不可变）
│   ├── cr/                    # 完整规则文档（CR 1–9 + 词汇表）
│   ├── mtr/                   # 比赛规则（MTR）
│   ├── ipg/                   # 违规处理方针（IPG）
│   ├── references/            # 专题参考文档
│   └── tools/mtg_wiki/        # Python 工具集
├── wiki/                       # LLM 生成和维护的知识库
│   ├── index.md              # 内容总索引
│   ├── log.md                # 操作日志
│   ├── concepts/             # 概念页：规则、机制、策略（~174页）
│   ├── entities/             # 实体页：人物、组织、产品
│   ├── sources/              # 来源摘要页
│   ├── synthesis/            # 综合分析
│   └── branches/referee/     # 裁判分支专用层
│       ├── decision-trees/   # 裁判决策树（31个）
│       ├── frameworks/       # 分析框架（层系统、堆叠等）
│       ├── common-traps/     # 常见陷阱
│       ├── mtr-ipg-guides/   # 比赛规则指南
│       └── test-questions/   # 测试题库
└── output/                    # 生成的 artifacts
```

## OpenClaw Skill 格式

SKILL.md 必须包含 YAML frontmatter：

```markdown
---
name: mtg-wiki
description: 万智牌全知识库助手。当用户询问万智牌相关内容时触发。
metadata:
  openclaw:
    requires:
      bins: ["python3"]
      env: []
    os: ["darwin", "linux"]
---

# 技能说明（仅在触发后加载）
```

- **`description` 就是触发器** — 模型根据描述自主判断何时触发
- **分层加载** — frontmatter 元数据始终在 context，正文只在技能命中后才加载

## 常用命令

```bash
# 牌张查询（支持中英文模糊检索）
python3 raw/tools/mtg_wiki/card_search.py "Lightning Bolt"
python3 raw/tools/mtg_wiki/card_search.py "闪电击"

# 规则查询（支持规则号或关键词）
python3 raw/tools/mtg_wiki/rule_search.py "613.6"
python3 raw/tools/mtg_wiki/rule_search.py "堆叠"

# 牌名翻译（EN↔CN）
python3 raw/tools/mtg_wiki/name_translator.py "Lightning Bolt"
```

## Wiki 页面规范

- 所有页面为带 YAML frontmatter 的 Markdown
- 必需字段：`created`、`updated`、`type`、`tags`、`sources`
- 内部链接使用 `[[WikiLink]]` 语法（兼容 Obsidian）
- `type` 可选值：`source`、`entity`、`concept`、`synthesis`、`output`、`decision-tree`

## 核心操作

### 1. Ingest（摄入来源）
将文件放入 `raw/` 并说"摄入这个"：
1. 读取原始文件，与用户讨论核心要点
2. 在 `wiki/sources/YYYY-MM-DD-<slug>.md` 创建来源摘要页
3. 更新或创建相关的 `wiki/entities/` 和 `wiki/concepts/` 页面
4. 更新 `wiki/index.md`
5. 在 `wiki/log.md` 追加记录：`## [YYYY-MM-DD] ingest | <来源标题>`

### 2. Query（回答问题）
1. 先读取 `wiki/index.md` 定位相关页面
2. 读取这些页面并综合出带 `[[引用]]` 的答案
3. 如果答案内容充实且可复用，询问用户是否归档到 `wiki/synthesis/` 或 `output/`

### 3. Lint（健康检查）
说"检查 Wiki"时：
1. 扫描矛盾、过时主张、缺失的交叉引用
2. 识别孤立页面（无入链）以及缺少独立页面但重要的术语
3. 提出具体的修复建议
4. 在 `wiki/log.md` 追加记录：`## [YYYY-MM-DD] lint | <检查结果>`

## 层系统速查 (CR 613)

| 层 | 内容 | 经典案例 |
|----|------|----------|
| 1 | 复制效应 | 克隆 |
| 2 | 改变操控权 | 背叛 |
| 3 | 改变文字栏 | 基因改造 |
| 4 | 改变类别 | 腥红之月 vs 乌尔博格 |
| 5 | 改变颜色 | 染蓝 |
| 6 | 添加/移除异能 | 潮缚师、史芬斯的训谕 |
| 7 | 改变力量/防御力 | 各种加/减P/T |

**关键区分**：
- **跨层效应 (613.6)**：同一异能的不同部分在各层独立生效，即使源异能消失
- **从属关系 (613.8)**：仅当效应在**同一层**时才存在从属
