---
created: 2026-04-21
updated: 2026-04-21
type: source
tags: [万智牌, EDHREC, 组合技, 指挥官, 数据源]
sources: [EDHREC_Combos/]
---

# EDHREC 指挥官组合技数据库

## 来源说明

数据来源：[EDHREC](https://edhrec.com/combos) 指挥官组合技推荐系统。

EDHREC 是一个基于大数据分析的指挥官（Commander/EDH）套牌推荐网站，通过聚合全球玩家的套牌列表，统计牌张之间的协同效应和组合技出现频率。本次摄入的数据为 EDHREC 按指挥官**颜色认同**（Color Identity）分类的完整组合技数据集，涵盖从单色到五色的所有颜色组合。

## 数据规模

| 指标 | 数值 |
|------|------|
| 组合技总数 | **49,646** |
| 涉及不同牌张 | **6,258** |
| 颜色身份分类 | 33 个（含 5 单色 + 10 双色 + 10 三色 + 5 四色 + 无色 + 5 色） |
| 数据文件格式 | JSON（33 个文件，总计 ~500 MB） |
| 数据日期 | 2026-04-21 |

## 数据结构

每个组合技包含以下字段：

| 字段 | 说明 |
|------|------|
| `cardviews` | 组成组合技的牌（名称、Scryfall ID、EDHREC URL） |
| `header` | 组合标题（含使用套牌数） |
| `combo.comboId` | EDHREC 内部组合 ID |
| `combo.count` | 使用该组合的套牌数量 |
| `combo.percentage` | 在对应颜色身份中的使用率 |
| `combo.rank` | 在对应颜色身份中的排名 |
| `combo.results` | 组合产生的效果描述 |
| `combo.comboVote` | 社区评分（前置条件、结果评分、争议度） |

## 核心发现

### 最热门的组合技效果类型

1. **无限 ETB**（Infinite ETB）— 出现在 30,068 个组合中
2. **无限 LTB**（Infinite LTB）— 25,956 个组合
3. **无限死亡触发** — 20,787 个组合
4. **无限牺牲触发** — 19,542 个组合
5. **无限风暴计数** — 9,610 个组合

### 使用率最高的组合技

| 组合 | 使用套牌数 | 效果 |
|------|-----------|------|
| Hullbreaker Horror + Sol Ring | 300,846 | 无限无色法术力、无限风暴 |
| Demonic Consultation + Thassa's Oracle | 137,477 | 清空牌库后直接获胜 |
| Exquisite Blood + Sanguine Bond | 130,289 | 无限生命获得/生命流失 |
| Tainted Pact + Thassa's Oracle | 123,208 | 直接获胜 |
| Dramatic Reversal + Isochron Scepter | 96,706 | 无限法术力、无限风暴 |

### 最常见的引擎牌

引擎牌（Engine Card）是指在组合技中充当核心催化剂的牌，它们通常与多种其他牌配合形成组合技。

| 牌名 | 出现组合数 |
|------|-----------|
| Ashnod's Altar | 3,419 |
| Phyrexian Altar | 3,107 |
| Altar of Dementia | 1,190 |
| Pitiless Plunderer | 1,058 |
| Krark-Clan Ironworks | 1,012 |
| Viscera Seer | 923 |
| Goblin Bombardment | 916 |
| Carrion Feeder | 845 |

## 数据用途

- **套牌构筑参考**：了解某张牌的经典配合
- **禁限牌表分析**：高频组合技组件是禁牌候选
- **Meta 分析**：了解指挥官环境的组合技生态
- **教学素材**：经典组合技的教学案例

## 相关页面

- [[combo|组合技]]
- [[combo-engine-cards|组合技引擎牌]]
- [[commander|指挥官]]
- [[cedh|cEDH]]
