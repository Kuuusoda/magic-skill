---
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [万智牌, 关键字异能, 领地, 多色, 地]
sources: [cr/7.md, data/keywords-index.json, data/oracle-cards-lite.json]
---

# 领地（Domain）

## 定义

领地（Domain）是一个静止式异能，其效果取决于某牌手操控的**基本地类别**（basic land type）的数量（CR 702.44）。基本地类别包括平原（Plains）、海岛（Island）、沼泽（Swamp）、山脉（Mountain）和树林（Forest）。领地鼓励玩家使用多色/多地套牌，以获得更强力的效果。

## 核心规则

### 触发条件
- 领地计算的是牌手操控的**基本地类别**数量，而不是地牌的总数
- 一张地牌可以具有多个基本地类别（如 shock lands、fetchable dual lands），因此可以贡献多个领地计数
- 基本地（Basic Land）各具有一个基本地类别
- 非基本地如果具有基本地类别（如 Hallowed Fountain 具有 Plains 和 Island），也计入领地

### 常见效果形式
- **法术力产出**：横置地牌产生等同于领地数量的法术力
- **+N/+N 加成**：生物获得 +X/+X，X 为领地数量
- **伤害**：对目标造成等同于领地数量的伤害
- **抓牌/生命**：获得等同于领地数量的生命或抓牌

## 战略价值

### 1. 五色/Domain 套牌
领地机制天然鼓励使用多种颜色的地牌，因此 Domain 套牌通常是三色、四色甚至五色：
- 使用 fetch lands（如 Windswept Heath）寻找不同类别的 shock lands
- 使用 Triome 地牌（具有三个基本地类别）快速堆叠领地计数
- 使用 basic lands 保证稳定的法术力基础

### 2. 效率曲线
领地牌在游戏早期较弱（领地计数低），但随游戏进行逐渐增强。这种设计让领地牌在中后期成为优质资源。

### 3. 与「多地类别」地的配合
某些非基本地具有多个基本地类别，是领地套牌的核心：
- **Shock lands**：如 Steam Vents（Island Mountain）
- **Triomes**：如 Ketria Triome（Forest Island Mountain）
- **Pain lands**、**Check lands** 等不具有基本地类别，不计入领地

## 代表性牌张

| 牌名 | 费用 | 效果 |
|------|------|------|
| Territorial Kavu | {R}{G} | 2/2；每当它攻击时，抓一张牌然后弃一张牌；得 +1/+1（X 为你操控的基本地类别数） |
| Tribal Flames | {1}{R} | 瞬间；对任意目标造成 X 点伤害，X 为你操控的基本地类别数 |
| Sunburst/Domain 地 | — | 各种产生多色法术力的地牌 |
| Leyline of the Guildpact | {2}{G}{W} | 结界；你操控的基本地类别数 +1；你每操控一种基本地类别，从你的牌库中搜寻一张基本地牌放进战场 |
| Nishoba Brawler | {1}{G} | 0/0 践踏；进战场时得 +X/+X，X 为你操控的基本地类别数 |

## 历史

- 领地首次出现于 **Invasion（入侵，2000）**
- 作为多色环境的标志性机制，鼓励玩家使用所有五种颜色的地
- 在 **Planar Chaos（2007）** 和 **Dominaria（2018）** 中少量回归
- 在 **Dominaria United（2022）** 中作为该系列核心机制大规模回归
- 在 **Modern Horizons 2** 和 **March of the Lachine** 等后续系列中也有出现

## 相关页面

- [[keyword-abilities-overview|关键字异能总览]]
- [[land|地]]
- [[mana|法术力]]
- [[comprehensive-rules|完整规则]]
- [[mtg-formats|万智牌赛制]]
