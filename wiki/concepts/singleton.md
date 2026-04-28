---
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [万智牌, 指挥官, EDH, 单例制, 构组规则, 赛制]
sources: [cr/9.md]
---

# 单例制（Singleton）

## 定义

单例制（Singleton）是万智牌的一种套牌构组规则，要求套牌中除基本地外，每种英文名称的牌只能包含**一张**。这一规则是指挥官（Commander/EDH）赛制的核心构组限制之一（CR 903.5），也用于其他休闲变体如 Canadian Highlander 和 Tiny Leaders。

单例制极大地增加了套牌的多样性和不可预测性，因为牌手无法依赖重复的牌张来稳定执行策略。

## 核心规则

### 指挥官赛制的单例制

- **套牌大小**：恰好 100 张牌（包括指挥官）
- **单例限制**：除基本地外，每种英文名称的牌只能放一张
- **基本地例外**：基本地（Basic Land）不受单例限制，可以放任意数量
- **指挥官**：位于统帅区，不计入 100 张套牌中

### 什么牌受单例限制

| 牌类型 | 是否受单例限制 | 说明 |
|--------|--------------|------|
| 基本地 | 否 | Plains、Island、Swamp、Mountain、Forest 及其雪境版本 |
| 非基本地 | 是 | 每种非基本地只能一张 |
| 法术 | 是 | 每种法术只能一张 |
| 瞬间 | 是 | 每种瞬间只能一张 |
| 生物 | 是 | 每种生物只能一张 |
| 神器 | 是 | 每种神器只能一张 |
| 结界 | 是 | 每种结界只能一张 |
| 鹏洛客 | 是 | 每种鹏洛客只能一张 |
| 战役 | 是 | 每种战役只能一张 |

### "可互换名称"规则

CR 201.3 规定：具有可互换名称的牌在套牌构组中视为具有相同的英文名称。

**示例**：
- **Spike, Tournament Grinder** 可以从套牌外使用任何被禁牌，但这些被禁牌仍然受单例限制
- **Silvercoat Lion** 和 **Graceful Cat** 不是可互换名称，可以各放一张

## 单例制对套牌设计的影响

### 1. 一致性降低

单例制意味着：
- 无法像构筑赛那样放 4 张关键牌来保证上手率
- 套牌的一致性主要依赖** tutors（检索）**和**滤牌**
- 运气因素比构筑赛更大

### 2. Tutors 的价值提升

在单例制中，能够搜索牌库的牌价值极高：

| 类型 | 示例 | 效果 |
|------|------|------|
| 地搜寻 | Cultivate、Farseek、Nature's Lore | 找地 + 法术力修正 |
| 生物搜寻 | Worldly Tutor、Eladamri's Call | 找特定生物 |
| 神器搜寻 | Enlightened Tutor、Fabricate | 找特定神器 |
| 瞬间/法术搜寻 | Mystical Tutor、Merchant Scroll | 找特定咒语 |
| 任意搜寻 | Demonic Tutor、Vampiric Tutor | 找任意牌 |
| 台面搜寻 | Birthing Pod、Prime Speaker Vannifar | 按曲线找生物 |

### 3. 多功能牌更受欢迎

单例制下，一张能处理多种情况的牌比多张专精牌更有价值：

| 牌名 | 类型 | 多功能性 |
|------|------|----------|
| Assassin's Trophy | 瞬间 | 去除任何永久物 |
| Anguished Unmaking | 瞬间 | 放逐任何非地永久物 |
| Chaos Warp | 瞬间 | 去除任何永久物（随机） |
| Beast Within | 瞬间 | 消灭任何永久物 |
| Generous Gift | 瞬间 | 消灭任何永久物 |
| Swords to Plowshares | 瞬间 | 消灭生物（最廉价） |
| Cyclonic Rift | 瞬间 | 弹回所有非己方永久物 |

### 4. 冗余策略（Redundancy）

由于不能放多张同名牌，套牌设计师会寻找**功能相似但名称不同**的牌来提供冗余：

**示例：加速法术力**
- Cultivate + Kodama's Reach + Skyshroud Claim + Migration Path
- 效果相似（找地并放入战场），但名称不同

**示例：去除**
- Swords to Plowshares + Path to Exile + Fateful Absence + Generous Gift
- 都是廉价白色生物去除，但名称不同

**示例：抽牌引擎**
- Phyrexian Arena + Dark Confidant + Necropotence + Underworld Connections
- 都是黑色持续抽牌来源

## 单例制与其他赛制的对比

| 特性 | 指挥官（Singleton） | 标准/摩登（Constructed） | 限制赛（Limited） |
|------|-------------------|------------------------|------------------|
| 套牌大小 | 100 | 60 | 40 |
| 同名牌限制 | 1 张（除基本地） | 4 张 | 无限制（依牌池） |
| 一致性 | 低 | 高 | 中 |
| Tutor 价值 | 极高 | 中 | 低 |
| 多功能牌价值 | 高 | 中 | 高 |
| 随机性 | 高 | 低 | 极高 |

## 单例制变体

### Canadian Highlander

- 100 张牌单例制
- **无指挥官**——纯构筑策略
- 有积分禁牌表（Points List），强力牌需要消耗积分
- 更偏向竞技

### Tiny Leaders

- 50 张牌单例制
- 指挥官 CMC ≤ 3
- 1v1 专用
- 已停止官方支持，但仍有社区维持

### Pauper Commander

- 100 张牌单例制
- 所有牌必须是**普通**（Common）稀有度
- 指挥官必须是**非传奇**的**不常见**（Uncommon）生物
- 成本极低的指挥官变体

### Oathbreaker

- 60 张牌单例制
- 使用**鹏洛客**作为"Oathbreaker"（类似指挥官）
- 有"Signature Spell"（专属法术），每次从统帅区施放
- 社群驱动的格式

## 单例制的设计哲学

单例制的设计目标：
1. **增加多样性**：每局游戏看到的牌不同
2. **降低门槛**：不需要购买多张昂贵的牌
3. **鼓励创意**：由于不能依赖重复牌，需要更灵活的策略
4. **平衡竞技与休闲**：高方差使新手也有机会击败老手

## 相关页面

- [[commander|指挥官]]
- [[cedh|cEDH]]
- [[color-identity|颜色认同]]
- [[tutor|检索]]
- [[ramp|跳费]]
- [[card-advantage|卡牌优势]]
- [[mtg-formats|万智牌赛制]]
