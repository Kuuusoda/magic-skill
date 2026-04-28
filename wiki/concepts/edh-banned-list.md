---
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [万智牌, 指挥官, EDH, 禁牌表, 赛制规则]
sources: [data/oracle-cards-lite.json]
---

# EDH 禁牌表（Commander Banned List）

## 定义

EDH 禁牌表（Commander Banned List）是由指挥官规则委员会（Commander Rules Committee，简称 RC）制定和维护的禁限牌表。它规定了在官方指挥官赛制中不能使用的牌张。与标准、摩登等赛制的禁牌表不同，EDH 禁牌表的制定不仅考虑平衡性，还考虑「游戏体验」——即使一张牌在强度上并非过强，如果它会破坏多人游戏的乐趣，也可能被禁。

## 禁牌表哲学

指挥官规则委员会的禁牌哲学核心原则：

1. **创造多样性**：鼓励不同策略和套牌类型的存在
2. **促进社交体验**：避免让游戏变得单调或不愉快
3. **限制过于一致的获胜手段**：防止套牌过于依赖单张牌
4. **防止资源失衡**：限制过于高效的法术力加速

## 当前禁牌表（截至 2026 年）

### 法术力加速（Mana Acceleration）

以下牌因提供过于高效且难以互动的法术力优势而被禁：

| 牌名 | 类型 | 费用 | 被禁原因 |
|------|------|------|---------|
| **Black Lotus** | 神器 | {0} | 0 费产三点任意色法术力，远超合理强度 |
| **Mox Emerald** | 神器 | {0} | 0 费产绿法术力 |
| **Mox Jet** | 神器 | {0} | 0 费产黑法术力 |
| **Mox Pearl** | 神器 | {0} | 0 费产白法术力 |
| **Mox Ruby** | 神器 | {0} | 0 费产红法术力 |
| **Mox Sapphire** | 神器 | {0} | 0 费产蓝法术力 |
| **Mox Diamond** | 神器 | {0} | 0 费产双色法术力（需弃一张地） |
| **Chrome Mox** | 神器 | {0} | 0 费产单色法术力（需放逐手牌） |
| **Mana Crypt** | 神器 | {0} | 0 费产 {2}，仅每回合 3% 概率掉 1 血 |
| **Sol Ring** | 神器 | {1} | 1 费产 {2}，在多人游戏中优势累积过快 |

### 组合技组件（Combo Pieces）

以下牌因在特定组合技中过于高效或难以互动而被禁：

| 牌名 | 类型 | 被禁原因 |
|------|------|---------|
| **Protean Hulk** | 生物 | Flash Hulk 组合技的核心，一卡拉出整套获胜组合 |
| **Leovold, Emissary of Trest** | 生物（指挥官）| 作为指挥官时，封锁对手抓牌能力过于压制 |
| **Golos, Tireless Pilgrim** | 生物（指挥官）| 提供过于一致的五色法术力基础和牌库顶施放 |

### 大规模破坏（Mass Destruction）

以下牌因破坏游戏体验而被禁：

| 牌名 | 类型 | 被禁原因 |
|------|------|---------|
| **Sway of the Stars** | 法术 | 重置整个游戏，过于拖延 |
| **Worldfire** | 法术 | 清空所有资源后让游戏变成「谁先抓到地谁赢」 |
| **Sundering Titan** | 神器生物 | 反复进出战场破坏地，过于压制 |
| **Tinker** | 法术 | 2 费搜索任意神器放入战场，包括 Sundering Titan |

### 资源锁定（Resource Lock）

| 牌名 | 类型 | 被禁原因 |
|------|------|---------|
| **Braids, Cabal Minion** | 生物（指挥官）| 每回合强制牺牲，作为指挥官过于压制 |
| **Rofellos, Llanowar Emissary** | 生物（指挥官）| 作为指挥官时提供过于高效的法术力 |
| **Erayo, Soratami Ascendant** | 生物（指挥官）| 翻面后封锁对手施放非生物咒语 |

### 其他禁牌

| 牌名 | 类型 | 被禁原因 |
|------|------|---------|
| **Ancestral Recall** | 法术 | 1 费抓三张牌，效率过高 |
| **Time Walk** | 法术 | 2 费额外回合 |
| **Timetwister** | 法术 | 重置所有资源（与 Power Nine 一同被禁） |
| **Tolarian Academy** | 地 | 每操控一个神器产 {U}，法术力爆发过于极端 |
| **Gaea's Cradle** | 地 | 每操控一个生物产 {G}，类似 Tolarian Academy |
| **Library of Alexandria** | 地 | 免费抓牌引擎 |
| **Karakas** | 地 | 反复弹回传奇生物，破坏指挥官机制 |
| **Recurring Nightmare** | 结界 | 每回合反复从坟场拉回生物，过于高效 |
| **Panoptic Mirror** | 神器 | 每回合免费复制结附的法术 |
| **Coalition Victory** | 法术 | 10 费直接获胜条件过于简单 |
| **Biorhythm** | 法术 | 直接根据生物数量决定胜负 |
| **Sylvan Primordial** | 生物 | ETB 破坏非基本地并搜索地，过于全面 |
| **Primeval Titan** | 生物 | ETB 搜索任意两张地放入战场，提供过大法术力优势 |
| **Prophet of Kruphix** | 生物 | 让所有永久物具有闪现，每回合重置，给予额外产费 |
| **Paradox Engine** | 神器 | 施放咒语时重置所有非地永久物，组合技引擎 |
| **Iona, Shield of Emeria** | 生物 | 封锁单色套牌的所有咒语 |
| **Emrakul, the Aeons Torn** | 生物 | 15/15 飞行保护，额外回合，过于全面 |
| **Griselbrand** | 生物 | 支付 7 血抓七张牌，过于高效的抽牌引擎 |
| **Leonin Relic-Warder** | 生物 | 与 Animate Dead 等形成无限循环 |

## 禁牌表的变化趋势

### 近年解禁的牌

| 牌名 | 解禁时间 | 说明 |
|------|---------|------|
| **Golos, Tireless Pilgrim** | 2024 年被禁 | 此前长期作为最受欢迎的五色指挥官之一 |
| **Hullbreacher** | 2021 年被禁 | 封锁对手抓牌并为自己产宝藏 |
| **Opposition Agent** | 2021 年被禁 | 控制对手搜索并揭示其手牌 |

### 禁牌表争议

以下牌长期存在是否应该被禁的争论：

| 牌名 | 争议点 |
|------|--------|
| **Rhystic Study** | 几乎每副蓝色套牌都放，过于「必放」|
| **Smothering Tithe** | 类似 Rhystic Study，白色最强加速 |
| **Dockside Extortionist** | ETB 产大量宝藏，组合技效率极高 |
| **Thassa's Oracle** | 一卡获胜条件，但认为互动牌可以应对 |
| **Demonic Tutor** | 2 费搜索任意牌，但认为 single 例制下可接受 |

## 与 Duel Commander 禁牌表的区别

Duel Commander（1v1 指挥官）拥有独立的禁牌表，通常比官方 EDH 禁牌表更严格：

| 牌名 | EDH | Duel Commander |
|------|-----|---------------|
| **Sol Ring** | 合法 | 被禁 |
| **Mana Crypt** | 合法 | 被禁 |
| **Ancient Tomb** | 合法 | 被禁 |
| **Demonic Tutor** | 合法 | 被禁 |
| **Vampiric Tutor** | 合法 | 被禁 |

## 禁牌表的查询方式

- **官方来源**：[Commander Rules Committee](https://mtgcommander.net/)
- **EDHREC 禁牌表**：[EDHREC Banned Cards](https://edhrec.com/banned-list)
- **Scryfall 查询**：`is:banned f:edh`

## 相关页面

- [[commander|指挥官]]
- [[cedh|cEDH]]
- [[duel-commander|Duel Commander]]
- [[banned-and-restricted|禁限牌表]]
- [[mtg-formats|万智牌赛制]]
