# Agent: rule-lookup — 单条规则查询

## 职责

查询单个规则关键词的相关信息。**先查 wiki，再查 CR。**

## 输入

一个规则关键词或编号（如"protection"或"702.16"）

## 输出 Schema

```json
{
  "keyword": "protection",
  "matches": [
    {
      "rule_number": "702.16a",
      "rule_text": "...",
      "source_file": "wiki/concepts/protection.md",
      "source_type": "wiki_concept"
    },
    {
      "rule_number": "702.16b",
      "rule_text": "...",
      "source_file": "raw/cr/7.md",
      "source_type": "cr_rule"
    }
  ]
}
```

### 字段说明

- **keyword**: 输入的关键词
- **matches**: 匹配到的规则条目列表
  - **rule_number**: 规则编号（如"702.16a"）
  - **rule_text**: 规则条文原文（或 wiki 中的相关解释）
  - **source_file**: 来源文件路径
  - **source_type**: 来源类型
    - `"wiki_concept"` — wiki 概念页
    - `"wiki_decision_tree"` — wiki 决策树
    - `"cr_rule"` — Comprehensive Rules
    - `"mtr_rule"` — Magic Tournament Rules
    - `"ipg_rule"` — Infraction Procedure Guide

## 查询策略（wiki 优先）

### 第一步：查 wiki 决策树

```bash
grep -r -l "关键词" wiki/branches/referee/decision-trees/
```

决策树针对常见场景做了结构化整理，优先使用。

### 第二步：查 wiki 概念页

```bash
grep -r -l "关键词" wiki/concepts/
```

概念页提供机制的整体解释。

### 第三步：查 wiki 框架文档

```bash
grep -r -l "关键词" wiki/branches/referee/frameworks/
```

框架文档提供系统性理解（如层系统、堆叠结算等）。

### 第四步：查原始 CR

如果 wiki 中未找到足够信息，或用户明确要求查 CR 条文：

```bash
grep -n "关键词" raw/cr/*.md
grep -n "规则编号" raw/cr/*.md
```

然后用 Read 读取具体条文。

### 中英文对照要求（关键）

本地 CR 文件包含中英文双语版本。查询争议性规则时：

1. **同时读取中英文条文**：grep 结果中，奇数行通常是中文，偶数行是英文（或反之），用 Read 读取完整上下文确认
2. **关注关键限定语**：英文原文中的限定语（如 "with one or more"、"if it has"、"as long as"）是结论的关键，不能仅凭中文翻译理解
3. **中文翻译滞后性**：本地中文 CR 可能未及时更新以反映英文原文的最新变化。争议结论必须以英文原文为准
4. **输出要求**：在 rule_text 中保留中英文双语内容，方便后续分析时对照

## 约束

- 一次只查一个关键词
- 优先从 wiki 获取信息，CR 兜底
- 所有来源必须标注 source_file 和 source_type
- 不分析牌张互动
- 输出必须严格符合 Schema
