---
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [万智牌, 关键字异能, 虚色, 奥札奇, 颜色]
sources: [cr/7.md, data/keywords-index.json, data/oracle-cards-lite.json]
---

# 虚色（Devoid）

## 定义

虚色（Devoid）是一个特征定义异能，使具有此异能的牌在规则上视为**无色**，即使它的法术力费用中包含 colored mana symbols。虚色不改变牌的实际颜色标识（color identity），只影响它在游戏中的「颜色」属性（CR 702.113）。

## 核心规则

### 颜色属性
- 具有虚色的牌在**所有区域**中都被视为无色
- 这意味着它不受「保护 from [颜色]」、不能被需要特定颜色的效应指定为目标
- 但虚色不改变牌的**颜色标识**（用于指挥官套牌构组）

### 法术力费用
- 虚色牌通常仍然需要 colored mana 来施放
- 例如：Spell Shrivel 费用为 {2}{U}，具有虚色，在规则上是无色牌，但施放时仍需支付蓝色法术力

### 与「无色」机制的关系
- 虚色与「Colorless matters」机制高度相关
- 某些效应奖励施放无色咒语或操控无色永久物
- 虚色牌可以满足这些要求

## 战略价值

### 1. 规避颜色保护
虚色牌可以绕过「保护 from [颜色]」和「辟邪」等异能，因为它们在规则上不属于任何颜色。

### 2. Colorless 套牌的融合
虚色牌可以在 Colorless matters 套牌中作为「有色费用的无色牌」使用，例如：
- 在 Eldrazi Tron 中，虚色牌同时满足「无色」要求和颜色法术力需求
- 某些套牌利用虚色牌来触发如 Matter Reshaper 等牌的异能

### 3. 指挥官中的色组扩展
虚色牌的颜色标识仍然包含其法术力费用中的颜色，因此：
- 一张 {1}{W}{B} 的虚色牌的颜色标识是 {W}{B}
- 它只能在颜色标识包含白黑的指挥官套牌中使用
- 但在游戏中，它视为无色，不受颜色相关异能影响

## 代表性牌张

| 牌名 | 费用 | 类型 | 效果 |
|------|------|------|------|
| Reality Smasher | {4}{C} | 生物 | 5/5 虚色，践踏，被咒语/异能瞄准时对手弃一张牌 |
| Thought-Knot Seer | {3}{C} | 生物 | 4/4 虚色，进战场时看对手手牌并放逐一张 |
| Eldrazi Displacer | {2}{W} | 生物 | 3/3 虚色，{2}{C}：流放并回场目标生物 |
| Spell Shrivel | {2}{U} | 瞬间 | 虚色，反击目标咒语，除非其操控者支付 {4} |
| Bearer of Silence | {1}{B} | 生物 | 2/1 虚色飞行，进战场时对手牺牲一个生物 |

## 历史

- 虚色首次出现于 **Battle for Zendikar（再战赞迪卡，2015）**
- 作为奥札奇（Eldrazi）主题的标志性机制
- 设计目的是让奥札奇牌在需要 colored mana 的同时保持「异域/外来」的无色风味
- 在 Modern Horizons 3 中，虚色机制以新的设计方向回归

## 相关页面

- [[keyword-abilities-overview|关键字异能总览]]
- [[color|颜色]]
- [[eldrazi|奥札奇]]
- [[commander|指挥官]]
- [[modern|摩登]]
- [[comprehensive-rules|完整规则]]
- [[mtg-formats|万智牌赛制]]
