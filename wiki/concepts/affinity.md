---
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [万智牌, 关键字异能, 连结, 神器, 费用减免]
sources: [cr/7.md, data/keywords-index.json, data/oracle-cards-lite.json]
---

# 连结（Affinity）

## 定义

连结（Affinity）是一个静态异能，在计算具有此异能的咒语的法术力费用时，减少等同于牌手操控的某种特定类型永久物数量的费用。最常见的形式是「连结神器」（Affinity for artifacts），即每操控一个神器，该咒语的费用减少 {1}（CR 702.41）。

## 核心规则

### 费用减免
- 连结是**费用减免**机制，不是替代性费用
- 例如：一张费用为 {3}{U}、具有「连结神器」的牌，若你操控 3 个神器，则实际只需支付 {U}
- 费用不能减至低于 0（即不能变成「负费用」）

### 连结对象
最常见的连结对象是**神器**，但理论上可以连结任何永久物类型：
- 连结神器（Affinity for artifacts）
- 连结地（Affinity for lands）
- 连结生物（Affinity for creatures）
- 连结平原（Affinity for Plains）等

### 与有色费用
- 连结只减免**无色部分**的费用（即 {1}、{2} 等）
- **不能**减免有色法术力费用（如 {U}、{R}{W} 等）
- 因此即使操控大量神器，有连结的牌通常仍需要支付其 colored mana

## 战略价值

### 1. 快速铺场
连结套牌的核心策略是快速在场上积累大量廉价神器，然后以极低费用甚至零费用施放强力威胁。

### 2. 零费威胁
在神器密集套牌中，连结牌可以成为「免费」的咒语。这在回合早期施放大威胁时极其强势。

### 3. 与神器主题的协同
- **珍宝**（Treasure）：作为廉价可消耗的神器来源
- **Memnite**、**Ornithopter**：零费神器，免费增加连结计数
- **Springleaf Drum**：生物变神器产费
- **Mox Opal**：传奇零费神器（满足条件时）

## 代表性牌张

| 牌名 | 费用 | 类型 | 说明 |
|------|------|------|------|
| Frogmite | {4} | 生物 | 连结神器；4/2 |
| Myr Enforcer | {7} | 生物 | 连结神器；4/4 |
| Thought Monitor | {6}{U} | 生物 | 连结神器；飞行；进场时抓两张牌 |
| Sojourner's Companion | {6} | 生物 | 连结神器；可以当地牌使用 |
| Tezzeret, Agent of Bolas | {2}{U}{B} | 鹏洛客 | +1：看牌库顶五张，将其中神器置入战场 |

## 历史

- 连结首次出现于 **Mirrodin（秘罗地，2003）**
- 当时「 affinity 套牌」是标准赛史上最强势的套牌之一，导致 Skullclamp、Arcbound Ravager、Disciple of the Vault 等牌被禁
- 后续在 **Modern Horizons 2（2021）** 中以 Thought Monitor 等牌回归摩登
- SOS 系列中的 **Witherbloom, the Balancer** 引入了「咒语具有连结生物」的新方向

## 相关页面

- [[keyword-abilities-overview|关键字异能总览]]
- [[artifact|神器]]
- [[treasure|珍宝]]
- [[costs|费用]]
- [[comprehensive-rules|完整规则]]
- [[mtg-formats|万智牌赛制]]
- [[modern|摩登]]
