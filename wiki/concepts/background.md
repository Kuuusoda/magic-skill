---
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [万智牌, 指挥官, EDH, 背景, 博德之门, 套牌构组]
sources: [cr/9.md]
---

# 背景（Background）

## 定义

背景（Background）是万智牌指挥官赛制中的一种特殊机制，首次出现于 **Commander Legends: Battle for Baldur's Gate（CLB）**。它允许某些传奇生物与一张「背景牌」共同作为套牌的指挥官，从而扩展色组和策略选择。

背景机制的设计灵感来自《龙与地下城》（Dungeons & Dragons）中的角色背景设定。

## 核心规则

### 标准背景机制

某些传奇生物具有规则叙述：
> 「选择一张背景牌（Choose a Background）」

这意味着：
1. 该传奇生物可以作为你的主指挥官
2. 你必须从合法牌池中选择一张**背景牌**（Enchantment — Background）作为第二指挥官
3. 两张牌共同位于统帅区，各自独立计算指挥官税

### 背景牌的特征

- **牌张类型**：结界 — 背景（Enchantment — Background）
- **颜色**：各有不同，提供额外色组
- **异能**：通常提供持续性的全局加成或触发式效应
- **只能在统帅区中作为背景使用**，不能在套牌中作为普通结界使用

### 色组合并

- 传奇生物的颜色认同 + 背景牌的颜色认同 = 套牌的可用色组
- 例如：
  - **Abdel Adrian, Gorion's Ward**（{W}）+ **Street Urchin**（{R}）= 白红套牌
  - **Galea, Kindler of Hope**（{G}{W}{U}）+ **Master Chef**（{G}）= 绿白蓝套牌（无变化）

## 代表性指挥官与背景组合

| 传奇生物 | 颜色 | 核心异能 | 常见背景 | 组合色组 |
|---------|------|---------|---------|---------|
| **Abdel Adrian, Gorion's Ward** | {W} | 闪现，ETB 放逐永久物并创建士兵 | Street Urchin（{R}）| 白红 |
| **Galea, Kindler of Hope** | {G}{W}{U} | 装备和灵气具有闪现，翻看牌库顶 | Master Chef（{G}）| 绿白蓝 |
| **Karlach, Fury of Avernus** | {R}{W} | 额外战斗阶段 | Tavern Brawler（{R}）| 白红 |
| **Lozhan, Dragon's Legacy** | {U}{R}{W} | 瞬间/法术造成伤害 | Cultist of the Absolute（{B}）| 白蓝黑红 |
| **Viconia, Drow Apostate** | {B} | 从坟场放逐生物抓牌 | Criminal Past（{U}）| 蓝黑 |

## 背景与伙伴的区别

| 特性 | 背景（Background） | 伙伴（Partner） |
|------|-------------------|----------------|
| 主指挥官类型 | 特定传奇生物（印有"Choose a Background"） | 任何具有「伙伴」异能的传奇生物 |
| 第二指挥官类型 | 背景结界牌 | 另一张具有「伙伴」异能的传奇生物 |
| 自由选择 | 必须从所有背景牌中选择 | 可以从所有伙伴牌中自由配对 |
| 色组扩展 | 通常扩展 1-2 色 | 可扩展 1-3 色 |
| 异能类型 | 背景提供全局/持续性效应 | 伙伴通常是生物异能 |

## 战略价值

### 1. 色组灵活性

背景机制允许单色或双色传奇生物进入更多色组：
- 原本只能玩单色的牌手现在可以尝试双色
- 获得更多法术力基础和牌池选择

### 2. 双核策略

传奇生物提供主动异能，背景提供被动加成：
- **Abdel Adrian**（主动去除/创造生物）+ **Street Urchin**（被动伤害）
- **Galea**（主动装备/灵气）+ **Master Chef**（被动 +1/+1 指示物）

### 3. 与伙伴的对比

背景相比伙伴：
- **更受限**：只能与特定传奇生物配对
- **更稳定**：背景牌通常是全局效应，不需要进入战场
- **费用更低**：背景牌通常 CMC 较低（2-4 费）

## 常见背景牌

| 背景牌 | 颜色 | 费用 | 核心效应 |
|--------|------|------|----------|
| **Criminal Past** | {U}{B} | {1}{U}{B} | 坟场中的生物获得+1/+1 |
| **Cultist of the Absolute** | {B} | {B} | 你的生物具有死触，但需每回合牺牲一个生物 |
| **Master Chef** | {G} | {1}{G} | 你的生物 ETB 时获得一个 +1/+1 指示物 |
| **Street Urchin** | {R} | {1}{R} | 每当你的生物对牌手造成伤害，你可以支付 {1} 对该牌手造成 1 点伤害 |
| **Tavern Brawler** | {R} | {1}{R} | 你的生物攻击时抓一张牌 |
| **Agent of the Iron Throne** | {B} | {2}{B} | 每当你的一个非衍生物永久物进入坟墓场，每位对手失去 1 点生命 |

## 相关页面

- [[commander|指挥官]]
- [[partner|伙伴]]
- [[color-identity|颜色认同]]
- [[command-zone|统帅区]]
- [[legendary-creature|传奇生物]]
- [[mtg-formats|万智牌赛制]]
