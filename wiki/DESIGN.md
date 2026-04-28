# Wiki 架构设计文档

本文档记录 `wiki/` 目录的架构设计决策、页面类型定义和协作规范。

## 架构哲学

Wiki 是**万智牌通用知识库**，采用"通用核心 + 分支专用层"的架构：

- **通用核心**（`concepts/`、`entities/`、`sources/`、`synthesis/`）面向所有受众，回答"这是什么"
- **分支专用层**（`branches/<branch>/`）面向特定消费场景，回答"怎么处理"

两层的页面通过 `[[WikiLink]]` 互相引用，通用页面不依赖分支页面，分支页面可以引用通用页面。

## 页面类型

| 类型 | 目录 | 用途 | 目标读者 |
|------|------|------|----------|
| `source` | `sources/` | 原始来源摘要 | 所有用户 |
| `entity` | `entities/` | 人物、组织、产品等实体 | 所有用户 |
| `concept` | `concepts/` | 规则概念、机制、术语 | 所有用户 |
| `synthesis` | `synthesis/` | 综合分析、比较、综述 | 所有用户 |
| `output` | `output/` | 生成的报告/表格/幻灯片 | 所有用户 |
| `decision-tree` | `branches/referee/decision-trees/` | 裁判决策路径 | 裁判、裁判 agent |

## 分支结构

### 裁判分支（`branches/referee/`）

```
branches/referee/
├── index.md                    # 裁判分支总索引 + 使用指南
├── decision-trees/             # 按机制/关键词组织的决策树（核心协作区）
│   └── *.md                    # type: decision-tree
├── frameworks/                 # 分析框架
│   └── *.md                    # 层系统、堆叠推演、异能类型、替代效应等
├── common-traps/               # 常见陷阱/误判（自然生长）
│   └── *.md
├── mtr-ipg-guides/             # 比赛规则与违规处理指南
│   └── *.md
└── test-questions/             # 测试题库（框架先行，题目逐步补充）
    └── *.md
```

#### 决策树页面规范（`type: decision-tree`）

每个决策树页面必须包含以下章节：

```markdown
---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: decision-tree
tags: [keyword_action, harmonize, graveyard]
sources: []
---

# [机制名称] 裁判决策树

## 识别条件
Agent 在什么情况下触发此决策树？

## 检索路径（按优先级排序）
1. [规则编号] [规则摘要] → 为什么先查这条
2. [规则编号] [规则摘要] → 为什么其次查这条
3. ...

## 常见陷阱
- **陷阱**: [描述] → **正确理解**: ...

## 测试验证
- [题目描述] → 期望检索的规则 → 期望结论

## 关联概念
- [[相关概念页]]
- [[其他决策树页]]
```

### 其他分支（预留）

- `branches/strategy/` — 策略分支
- `branches/creation/` — 创作分支
- `branches/diy/` — DIY 分支

各分支目录结构由对应负责人自行设计，但需遵循统一的 frontmatter 规范。

## 导航机制

### `wiki/index.md` 的分层索引

`wiki/index.md` 需要重构为三层索引：

1. **第一层**：通用概念索引（现有内容）
2. **第二层**：分支入口索引（裁判 / 策略 / 创作 / DIY）
3. **第三层**：分支内部索引（由各分支的 `index.md` 自行维护）

### Agent 检索路径

当裁判 agent 回答问题时：
1. 查询牌面信息 → 提取关键词
2. 检查 `wiki/branches/referee/decision-trees/` 是否有匹配的决策树页面
3. 如有 → 严格按照决策树的"检索路径"执行强制深度检索
4. 如无 → 回退到 `wiki/concepts/` 的通用概念页
5. 通用概念页作为辅助参考，不替代 CR 原文检索

## 协作规范

### 裁判社群贡献流程

1. 发现 agent 回答错误 → 在 `test-questions/` 记录错题
2. 分析错误根因 → 判断是否需要新建/更新决策树
3. 在 `decision-trees/` 新建或更新决策树页面
4. 更新 `branches/referee/index.md` 索引
5. 提交变更（通过 git PR 或直接提交）

### 变更审查要点

- 决策树的"检索路径"是否按正确优先级排序？
- 规则编号是否准确？
- "常见陷阱"是否基于实际判例？
- 是否通过 `[[WikiLink]]` 链接到相关通用概念页？

## 演进计划

| 阶段 | 内容 | 负责人 |
|------|------|--------|
| 1 | 建立 `branches/referee/` 目录结构 + 第一批决策树 | 架构负责人 |
| 2 | 裁判社群补充决策树和测试题 | 裁判社群 |
| 3 | 根据测试反馈迭代决策树 | 协同 |
| 4 | 规划其他分支目录结构 | 各分支负责人 |
