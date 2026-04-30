# Magic Skill — 万智牌通用知识基础设施

本项目是 **万智牌通用知识基础设施**（Magic: The Gathering General-Purpose Knowledge Infrastructure），由 LLM 构建和维护，服务于多个消费分支：裁判规则判定、策略研究、内容创作、DIY 卡牌设计等。基于 karpathy llm-wiki 启发，Wiki 作为核心知识库，在原始资料（规则文档、牌张数据、文章）和用户问题之间建立结构化的、可积累的知识层。

## 项目定位

| 层级 | 用途 | 内容 |
|------|------|------|
| **原始资料** (`raw/`) | 不可变数据源 | CR/MTR/IPG 规则文档、37,230 张牌数据、EDH 数据 |
| **通用知识库** (`wiki/`) | 面向所有受众 | 概念页、实体页、来源摘要、综合分析 |
| **分支专用层** (`wiki/branches/`) | 面向特定场景 | 裁判决策树、策略框架、创作模板 |
| **Agent/Skill** (`agent/`, `skill/`) | 可协作的配置 | 裁判 agent 定义、skill 工作流 |
| **生成产物** (`output/`) | 输出 artifacts | 周报、登记表、分析报告 |

## 快速概览

| 指标 | 数量 |
|------|------|
| Wiki 页面 | **254** |
| 概念页 | 190 |
| 裁判决策树 | 31 |
| 分析框架 | 4 |
| 常见陷阱 | 2 |
| 来源摘要 | 9 |
| 实体页 | 4 |
| 综合分析 | 4 |
| 原始资料文件 | 103 |

## 目录结构

```
├── agent/                          # Agent 定义（可协作、版本控制）
│   └── mtg-judge-zh.md             # 裁判 agent 的 persona、工作流、合规报告
├── skill/                          # Skill 定义（可协作、版本控制）
│   └── mtg-judge-zh/
│       └── SKILL.md                # 裁判 skill 的触发条件、回答流程
├── raw/                            # 原始资料（不可变）
│   ├── cr/                         # 完整规则（CR 1–9 章 + 词汇表）
│   ├── ipg/                        # 违规处理方针
│   ├── mtr/                        # 比赛规则
│   ├── data/                       # 牌张数据（37,230 Oracle 牌）
│   ├── references/                 # 专题参考文档（待重构为自动生成索引）
│   ├── tools/                      # Python 工具集（牌张查询、规则查询、牌名翻译）
│   └── assets/                     # 图片和附件
├── wiki/                           # LLM 生成和维护的知识库
│   ├── DESIGN.md                   # Wiki 架构设计文档
│   ├── index.md                    # 内容总索引
│   ├── log.md                      # 操作日志
│   ├── _templates/                 # 页面模板
│   ├── sources/                    # 来源摘要
│   ├── entities/                   # 实体页：人物、组织、产品
│   ├── concepts/                   # 概念页：规则、机制、策略术语
│   ├── synthesis/                 # 综合分析
│   └── branches/                   # 各分支专用层
│       ├── referee/                # 裁判分支（当前聚焦）
│       │   ├── decision-trees/     # 裁判决策树（按机制/关键词组织）
│       │   ├── frameworks/         # 分析框架（层系统、堆叠推演等）
│       │   ├── common-traps/       # 常见陷阱与误判
│       │   ├── mtr-ipg-guides/    # 比赛规则与违规处理指南
│       │   └── test-questions/     # 测试题库
│       ├── strategy/               # 策略分支（预留）
│       ├── creation/               # 创作分支（预留）
│       └── diy/                    # DIY 分支（预留）
└── output/                         # 生成的 artifacts
    ├── cedh小屋周报/               # cEDH 赛事周报
    ├── card-generator/             # AI 卡牌设计工具
    └── *.md                        # 其他报告和分析
```

## 覆盖内容

### 规则与机制
- **完整规则（CR）** — 全部 9 章拆解为概念页，精确引用规则条文（如 CR 101.4、CR 613、CR 704.5）
- **比赛文档** — MTR 和 IPG 分解为可搜索的概念页
- **关键词** — 16 个常青关键词 + 9 个机制关键词
- **核心系统** — 堆叠、层系统（613）、优先权、战斗阶段、状态动作、替代/预防效应

### 裁判决策支持（`wiki/branches/referee/`）
- **决策树路由** — 统一的决策入口页面，按问题类型快速导航到对应决策树
- **决策树** — 31 个机制/关键词的强制检索路径（Cascade、Flashback、替代效应、复制效应等）
- **分析框架** — 层系统判定、堆叠推演、异能类型识别、替代效应分析
- **合规报告** — Agent 每份回答附带执行合规报告，确保规则检索深度

### 策略与赛制
- 赛制页：标准、先驱、摩登、薪传、限制、指挥官
- 策略概念：卡牌优势、法术力曲线、去除、反击、导师、加速、组合技
- 套牌原型概览

### 数据与分析
- 37,230 张唯一 Oracle 牌，从 526,803 条记录中提取
- 分布索引：颜色、法术力费用、赛制、超类型、副类型、关键词、系列（1,028 个）

## 核心操作

本项目由 Claude Code 配合 `mtg-judge-zh` agent 维护。三个核心操作驱动知识库增长：

### 1. Ingest（摄入来源）
将来源放入 `raw/` 并告知 agent 处理。agent 读取来源、讨论核心要点、在 `wiki/sources/` 写摘要、更新相关概念/实体页、追加日志记录。单一来源通常涉及 10–15 个 wiki 页面。

### 2. Query（回答问题）
向 Wiki 提问。agent 读取 `index.md` 定位相关页面，综合出带 `[[引用]]` 的答案，并将有价值的回答归档到 `wiki/synthesis/` 或 `output/`。

### 3. Lint（健康检查）
定期扫描矛盾、过时主张、孤立页面、断链和缺失交叉引用。Python 脚本（`raw/data/lint_wiki_v2.py`）验证所有内部 WikiLink 是否正确解析。

## 页面规范

- 所有页面为带 YAML frontmatter 的 Markdown（`created`、`updated`、`type`、`tags`、`sources`）
- 内部链接使用 `[[WikiLink]]` 语法（兼容 Obsidian）
- 文件名：小写，短横线连接（如 `comprehensive-rules.md`）
- 中文文件名允许，需以 `.md` 结尾
- 新增 `type: decision-tree` 用于裁判决策树页面

## 工具与脚本

| 脚本 | 用途 |
|------|------|
| `raw/tools/mtg_wiki/card_search.py` | 牌张查询（本地 37K + mtgch API + Scryfall API） |
| `raw/tools/mtg_wiki/rule_search.py` | 规则查询（支持规则号或关键词） |
| `raw/tools/mtg_wiki/name_translator.py` | 牌名翻译（EN↔CN） |
| `raw/data/lint_wiki_v2.py` | 链接健康检查、孤立页面扫描、断链检测 |
| `raw/data/process_cards.py` | 流式处理 2.3 GB all-cards JSON |
| `raw/data/generate_keyword_pages.py` | 从关键词语料自动生成概念页 |
| `raw/data/generate_missing_pages.py` | 识别并脚手架缺失的 wiki 页面 |

## 浏览 Wiki

在 [Obsidian](https://obsidian.md/) 中打开 `wiki/` 文件夹获得最佳体验：
- **图谱视图** 展示概念之间的连接
- **WikiLinks** (`[[ ]]`) 无缝导航
- **Dataview** 插件可查询 YAML frontmatter 生成动态表格

## Agent 集成

`mtg-judge-zh` agent（万智牌中文裁判助手）以本 Wiki 为知识库之一。回答规则问题时，它综合查询：
- 原始 CR 规则文档（`raw/cr/`）
- 编译后的 Wiki（`wiki/concepts/`、`wiki/synthesis/`）
- 裁判决策树（`wiki/branches/referee/decision-trees/`）

Agent 的回答流程包含**强制深度检索**和**执行合规报告**，确保规则引用准确、不凭记忆回答。

## 为什么选择这种方式

传统 RAG 每次查询都检索原始文档片段。本 Wiki **一次性编译知识并保持更新**。交叉引用已经建立，矛盾已经标记，综合已经反映所有已读内容。知识库随每个来源和每个问题而丰富——不会因为聊天历史而丢失。

## 协作方式

- **架构负责人** — agent/skill 定义、frameworks/、整体架构演进
- **裁判社群** — decision-trees/、common-traps/、test-questions/ 的内容补充
- **工具开发者** — raw/tools/ 优化、自动生成索引脚本

详见 `TODO.md` 了解当前待办事项和优先级。

## LLM Wiki 模式

本项目遵循 LLM Wiki 模式：一种使用 LLM agent 构建持久化、复利式增长知识库的通用方法。相同结构适用于研究、竞争分析、读书笔记或任何知识随时间积累的领域。

---

## License

MIT License — 详见 [LICENSE](LICENSE)

---

*Built with Claude Code + Obsidian. Wiki 页面由 LLM 生成；原始资料由人工策划。*
