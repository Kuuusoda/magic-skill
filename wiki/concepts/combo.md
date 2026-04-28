---
created: 2026-04-20
updated: 2026-04-21
type: concept
tags: [万智牌, 战略, 组合技, 无限, 制胜, EDH, 指挥官]
sources: [data/oracle-cards-lite.json, EDHREC_Combos/]
---

# 组合技（Combo）

## 定义

组合技（Combo）是万智牌中一种以特定牌张组合为核心的制胜策略。当两张或更多张牌按照特定顺序和方式互动时，可以产生远超单张牌价值的强大效果，甚至直接赢得游戏。组合技是许多竞技套牌的核心架构，也是万智牌深度和策略多样性的重要来源。

组合技的英文 "Combo" 源自 "Combination"，在万智牌社区中已成为一个专有术语，指任何利用牌张间协同效应产生决定性优势的策略。

## 核心类型

### 1. 无限组合技（Infinite Combo）

两张牌之间形成无限循环，产生无限的资源或直接杀死对手。这是万智牌中最具标志性的组合技类型。

#### 指挥官环境中最常见的无限效果

基于 EDHREC 49,646 个组合技的大数据分析：

| 效果类型 | 出现次数 | 说明 |
|---------|---------|------|
| 无限 ETB | 30,068 | 生物进场触发无限循环 |
| 无限 LTB | 25,956 | 生物离场触发无限循环 |
| 无限死亡触发 | 20,787 | 生物死去时触发无限循环 |
| 无限牺牲触发 | 19,542 | 生物被牺牲时触发无限循环 |
| 无限风暴计数 | 9,610 | 通过反复施放咒语累积风暴 |
| 无限有色法术力 | 6,870 | 产生无限有色法术力 |
| 无限生物衍生物 | 6,411 | 创造无限个生物衍生物 |
| 无限无色法术力 | 5,385 | 产生无限无色法术力 |
| 无限 +1/+1 指示物 | 4,140 | 在生物上放置无限 +1/+1 指示物 |
| 无限抓牌 | 3,646 | 抓无限张牌 |
| 无限伤害 | 3,477 | 对对手造成无限伤害 |
| 无限回合 | 2,658 | 获得无限额外回合 |

#### 经典无限组合技案例

| 组合 | 组件 | 效果 |
|------|------|------|
| Splinter Twin | Splinter Twin + Deceiver Exarch | 制造无限个具有敏捷的生物 |
| Dramatic Scepter | Dramatic Reversal + Isochron Scepter | 无限法术力、无限风暴 |
| Basalt Rings | Basalt Monolith + Rings of Brighthearth | 无限无色法术力 |
| KCI | Krark-Clan Ironworks + Scrap Trawler | 无限无色法术力 |

### 2. 直接获胜组合技（Win-the-Game Combo）

不依赖无限循环，而是通过特定条件直接满足游戏的获胜条件。

| 组合 | 组件 | 效果 |
|------|------|------|
| Consultation Oracle | Demonic Consultation + Thassa's Oracle | 清空牌库后 Oracle 触发获胜 |
| Tainted Pact Oracle | Tainted Pact + Thassa's Oracle | 同上，使用 Tainted Pact |
| Helm of Obedience | Helm of Obedience + Rest in Peace | 磨空对手牌库 |
| Laboratory Maniac | 配合大量抓牌 | 牌库抽空时获胜 |

### 3. 生命流失组合技（Lifeloss Combo）

通过生命获得和生命流失之间的互动形成无限循环。

| 组合 | 组件 | 效果 |
|------|------|------|
| Exquisite Bond | Exquisite Blood + Sanguine Bond | 一方获得生命时另一方失去等量生命，无限循环 |
| Exquisite Vito | Exquisite Blood + Vito, Thorn of the Dusk Rose | Vito 替代 Sanguine Bond 的作用 |
| Aetherflux Blood | Aetherflux Reservoir + Exquisite Blood | 无限生命后 Reservoir 一击必杀 |

### 4. 两卡组合技（Two-Card Combo）

仅需两张牌即可产生决定性优势，是最简洁高效的组合技形式。

| 组合 | 组件 | 效果 |
|------|------|------|
| Heliod Ballista | Heliod, Sun-Crowned + Walking Ballista | 无限 +1/+1 指示物 + 无限伤害 |
| Niv-Mizzet Curiosity | Niv-Mizzet, Parun + Curiosity | 抓牌时对目标造成 1 点伤害，无限循环 |
| Dualcaster Twinflame | Dualcaster Mage + Twinflame | 复制无限个具有敏捷的生物 |

### 5. 风暴组合技（Storm Combo）

在一回合内施放大量咒语，利用 Storm 机制或类似效应终结游戏。

- **Grapeshot**：本回合施放的每个咒语都复制一次，对任意目标造成 1 点伤害
- **Tendrils of Agony**：每个复制对对手造成 2 点伤害并为你恢复 2 点生命
- **Brain Freeze**：磨对手牌库，配合 Underworld Breach 和 Lion's Eye Diamond 形成循环

### 6. 锁定组合技（Lock Combo）

使对手完全丧失行动能力，而非直接获胜。

- **Stasis + Forsaken City**：冻结所有永久物，同时维持 Stasis 的费用
- **Knowledge Pool + Teferi, Time Raveler**：对手无法施放任何咒语
- **Drannith Magistrate + Uba Mask**：对手无法从牌库外使用牌

## 组合技引擎牌

引擎牌（Engine Card）是组合技体系中的核心催化剂，它们通常具有高效的资源转换能力，可以与多种其他牌配合形成组合技。

基于 EDHREC 数据分析，出现频率最高的引擎牌：

### 牺牲类引擎

| 牌名 | 出现组合数 | 核心机制 |
|------|-----------|---------|
| Ashnod's Altar | 3,419 | 牺牲生物获得 {2} |
| Phyrexian Altar | 3,107 | 牺牲生物获得任意颜色法术力 |
| Altar of Dementia | 1,190 | 牺牲生物磨牌 |
| Viscera Seer | 923 | {B} 牺牲生物占卜 1 |
| Goblin Bombardment | 916 | 牺牲生物对目标造成 1 点伤害 |
| Carrion Feeder | 845 | +1/+1 计数器，牺牲生物 |

### 法术力类引擎

| 牌名 | 出现组合数 | 核心机制 |
|------|-----------|---------|
| Krark-Clan Ironworks | 1,012 | 牺牲神器获得 {2} |
| Basalt Monolith | 大量 | {3} 产 {3}，可反复重置 |
| Hullbreaker Horror | 极高 | 法术/瞬间反弹产费 |
| Sensei's Divining Top | 794 | {1} 抓顶牌 |

### 触发类引擎

| 牌名 | 出现组合数 | 核心机制 |
|------|-----------|---------|
| Pitiless Plunderer | 1,058 | 生物死去时产宝藏 |
| Animation Module | 1,004 | +1/+1 指示物时产 1/1 伺服 |
| Ghostly Flicker | 770 | 闪现两个非地永久物 |
| Kodama of the East Tree | 760 | 永久物进场时放第二个 |
| Intruder Alarm | 729 | 生物进场时重置所有生物 |

更多引擎牌详见 [[combo-engine-cards|组合技引擎牌]] 页面。

## 战略考量

### 何时追求组合技

- 套牌中有大量 tutors（搜寻牌库的牌）可以快速凑齐组件
- 环境互动较少，组合技容易安全结算
- 组合技的「致死回合」快于对手的中速/控制套牌
- 指挥官环境中，组合技是许多 cEDH 套牌的主要获胜手段

### 如何应对组合技

- **去除关键组件**：Counterspell、弃牌、去除永久物
- **破坏资源**：Strip Mine、Wasteland 破坏法术力基础
- **备牌针对**：Grafdigger's Cage、Pithing Needle、Torpor Orb 等
- **施加压力**：Aggro 套牌在组合技凑齐前压死对手
- **规则相关**：CR 104.3 定义了游戏的结束条件，了解替代获胜条件（如 Thassa's Oracle）的规则基础有助于正确应对

## 组合技的赛制差异

### 构筑赛（Constructed）
- 组件固定，通过 tutors 快速凑齐
- 互动牌密度高，组合技需要保护手段
- Splinter Twin 等组合技已被禁

### 限制赛（Limited）
- 组合技极为罕见，依赖补充包中恰好开出组件
- 通常只有非常简单的两卡配合

### 指挥官（Commander/EDH）
- 100 张牌单例制，组合技组件分散
- 社交契约影响组合技的接受度（休闲桌通常不喜无限组合技）
- cEDH 中组合技是主流获胜手段
- 统帅区（Command Zone）提供稳定的指挥官资源

## 相关页面

- [[combo-engine-cards|组合技引擎牌]]
- [[storm|风暴]]
- [[cedh|cEDH]]
- [[casting-spells|施放咒语]]
- [[stack|堆叠]]
- [[mtg-formats|万智牌赛制]]
- [[sources/2026-04-21-edhrec-combos|EDHREC 组合技数据库]]
