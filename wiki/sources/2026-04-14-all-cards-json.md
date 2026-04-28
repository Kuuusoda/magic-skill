---
created: 2026-04-14
updated: 2026-04-14
type: source
tags: [万智牌, 牌张数据, JSON, 数据库, 数据分析]
sources: [data/all-cards-20260414092108.json, data/oracle-cards-lite.json, data/sets-index.json, data/keywords-index.json, data/types-index.json, data/colors-dist.json, data/formats-dist.json]
---

# 万智牌全牌张数据库（JSON）

**原始文件**：`data/all-cards-20260414092108.json`
**导出日期**：2026年4月14日
**格式**：JSON（Scryfall all-cards bulk data）

## 摘要

这是截至 2026年4月14日 的万智牌全牌张数据导出文件，以 JSON 格式存储。原始文件大小 **2.3GB**，包含 **526,803 张卡片记录**（涵盖所有语言版本和重印版本）。经过流式数据清洗后，提取出 **37,230 张唯一英文版 Oracle 牌**，作为 Wiki 知识库的核心数据资产。

## 核心数据成果

### 数据库规模
- **原始记录**：526,803 张
- **英文版记录**：111,094 张
- **唯一 Oracle 牌（去重后英文版）**：37,230 张
- **涵盖系列**：1,028 个（从 1993 年 Alpha 到 2026 年 Marvel Super Heroes）
- **关键字/机制**：738 个不同标记
- **主类型标记**：51 种

### 生成的分析索引文件

为便于后续查询和分段学习，原始数据库已被拆分为以下精简索引：

- `data/oracle-cards-lite.json` — 37,230 张去重精简牌库（48MB）
- `data/sets-index.json` — 1,028 个系列的元数据与牌张统计
- `data/keywords-index.json` — 738 个关键字的出现频率
- `data/types-index.json` — 51 个主类型的分布统计
- `data/colors-dist.json` — 32 种颜色组合的分布
- `data/formats-dist.json` — 21 种赛制的可用性统计
- `data/cmc-dist.json` — 法术力费用分布
- `data/supertypes-dist.json` — 超级类型分布
- `data/subtypes-dist.json` — 热门副类别 TOP200

### 数据洞察摘要

- **生物 dominance**：19,289 张生物牌，占总牌的 51.8%
- **最热门关键字**：飞行（Flying）出现在 3,356 张牌中
- **五色平衡**：单色牌数量非常接近（约 4,850~5,050 张/色）
- **Eternal 赛制牌池**：Vintage、Legacy、Commander 可用牌均超过 30,000 张
- **标准牌池**：约 4,168 张可用牌

## 使用场景

- 牌名核对与规则叙述查询
- 套牌构建辅助与赛制合法性检查
- 关键字/机制/颜色/类型的统计分析
- 作为 LLM 生成知识库页面的底层数据源

## 相关页面

- [[wizards-of-the-coast|威世智有限公司]]
- [[comprehensive-rules|完整规则]]
- [[card-types-overview|牌张类型体系]]
- [[keyword-abilities-overview|关键字异能总览]]
- [[color-pie|五色轮]]
- [[synthesis/format-legality-analysis|万智牌赛制可用性分析]]
