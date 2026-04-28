---
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [万智牌, 核心规则, 额外回合, 回合结构]
sources: [cr/5.md]
---

# 额外回合（Extra Turn）

## 定义

额外回合（Extra Turn）是指某牌手在当前回合结束后，立即获得一个新的完整回合（CR 500.7）。额外回合会插入正常的回合顺序中，在该牌手本应进行的回合之前进行。额外回合是万智牌中最强大的效应之一，因为它直接给予牌手更多的资源、行动机会和胜利时间。

## 核心规则

### 额外回合的触发
额外回合通常由以下方式获得：
- **咒语/异能效应**：如 Time Warp、Temporal Manipulation、Nexus of Fate
- **连锁额外回合**：某些牌在特定条件下自动获得额外回合（如 Emrakul, the Aeons Torn 被施放时）
- **Suspend（延缓）**：某些延缓牌在最后一个时间指示物被移除时获得额外回合

### 额外回合的顺序
- 若多个牌手在同一回合中获得额外回合，**最后创造的额外回合最先进行**（LIFO，Last In First Out）
- 额外回合结束后，回到正常的回合顺序
- 若某效应让牌手「跳过一个回合」，该回合被完全跳过；若该回合中有额外回合，额外回合仍然发生

### 额外回合中的限制
- **正常规则仍然适用**：额外回合是一个完全正常的回合，包括正常的阶段和步骤
- **地牌上限**：额外回合中仍然只能放一张地（除非有特定效应允许额外下地）
- **维持、抓牌等**：额外回合中的所有正常触发都会发生

### 连锁额外回合
某些套牌专门围绕连锁额外回合构建，连续获得多个回合直至对手无法应对：
- **Time Walk 链**：通过回收 Time Walk 效应连续获得额外回合
- **Nexus of Fate**：将自身洗回牌库，反复获得额外回合
- **Wilderness Reclamation + Nexus of Fate**：利用 Wilderness Reclamation 的法术力在对手回合末施放 Nexus

## 战略价值

### 1. 时间优势
额外回合直接给予牌手「多行动一次」的机会。在控制套牌中，一个额外回合意味着多抓一张牌、多恢复一次生命、多留一次开放法术力。

### 2. Combo 套牌的终结手段
许多 combo 套牌利用额外回合来「凑齐组件」或「执行 combo」：
- **Taking Turns（Modern）**：通过 Gigadrowse、Part the Waterveil 等牌连续获得额外回合，最终用 Molten Psyche 或 Madcap Experiment 终结
- **Nexus of Fate（Standard 历史）**：利用 Azcanta 和 Wilderness Reclamation 反复施放 Nexus，直到用大量生物压死对手

### 3. 资源翻倍
在额外回合中，所有「每回合一次」的资源都会重置：
- 生物可以再次攻击
- 鹏洛客的忠诚异能可以再次起动
- 地牌可以再次横置产费
- 手牌上限检查再次进行

## 代表性牌张

| 牌名 | 费用 | 效果 |
|------|------|------|
| Time Walk | {1}{U} | 法术；本回合后进行额外回合（Power Nine 之一） |
| Time Warp | {3}{U}{U} |  Sorcery；目标牌手本回合后进行额外回合 |
| Temporal Manipulation | {3}{U}{U} |  Sorcery；本回合后进行额外回合 |
| Nexus of Fate | {5}{U}{U} | 瞬间；本回合后进行额外回合；将此牌洗回牌库而非置入坟场 |
| Emrakul, the Aeons Torn | {15} | 15/15；被施放时获得额外回合 |
| Part the Waterveil | {4}{U}{U} |  Sorcery；本回合后进行额外回合；觉醒 6（若支付觉醒费用，造一个 6/6 并得地） |

## 历史

- **Time Walk** 是万智牌最早的额外回合牌之一，也是著名的 **Power Nine** 成员
- 额外回合牌在 Vintage 和 Legacy 中被严格限制（Time Walk 限制，Time Warp 等可用）
- **Nexus of Fate** 因在 Standard 中配合 Wilderness Reclamation 形成「不可互动的无限回合锁」而被禁
- 额外回合效应通常成本较高（5+ 法术力），以防止早期滥用
- 设计团队对额外回合牌非常谨慎，因为「跳过对手回合」的体验往往对互动性有害

## 相关页面

- [[turn-structure|回合结构]]
- [[timing-and-priority|时机和优先权]]
- [[stack|堆叠]]
- 时间行走（Time Walk）
- [[comprehensive-rules|完整规则]]
- [[mtg-formats|万智牌赛制]]
