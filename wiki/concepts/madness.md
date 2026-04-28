---
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [万智牌, 关键字异能, 疯魔, 坟场, 弃牌, 机制]
sources: [cr/7.md, data/keywords-index.json, data/oracle-cards-lite.json]
---

# 疯魔（Madness）

## 定义

疯魔（Madness）是一个关键字异能，当具有疯魔的牌被弃置时，牌手可以选择将其放逐（而非置入坟墓场），然后选择是否支付其疯魔费用来施放该牌（CR 702.34）。疯魔是万智牌中最著名的坟场互动机制之一，与黑色和红色的弃牌主题高度相关。

## 核心规则

### 触发流程
1. 具有疯魔的牌被**弃置**（discard）
2. 触发疯魔异能，牌被**放逐**（而非进入坟墓场）
3. 牌手选择是否支付**疯魔费用**来施放该牌
4. 若选择不施放，该牌从放逐区进入坟墓场

### 关键限制
- 疯魔只在牌**被弃置时**触发，从其他区域（如牌库顶磨入坟场）不会触发
- 疯魔施放遵循正常的咒语施放规则（需要合法时机、目标等）
- 疯魔费用通常低于正常费用，但也可能相同或更高
- 疯魔是**触发式异能**的替代性效应，使用堆叠

### 与「弃牌」的区别
- **正常弃牌**：牌进入坟墓场
- **疯魔弃牌**：牌被放逐，有机会以更低费用施放
- 这让弃牌从「负面效果」变成了「资源转换」

## 战略价值

### 1. 资源转换
疯魔让弃牌从「失去资源」变成「获得资源」。在大量弃牌效应（如 Burning Inquiry、Careful Study）的套牌中，疯魔牌被弃置时可以以更低费用施放，实现「免费」价值。

### 2. 规避坟场 hate
由于疯魔牌先被放逐，因此不受坟墓场针对性去除（如 Rest in Peace、Leyline of the Void）影响，只要疯魔结算，牌就能被施放。

### 3. 组合技引擎
某些疯魔牌本身就是强力组合技部件：
- **Living End**：疯魔 {0}，消灭所有生物，将坟场生物回场
- **Glimpse of Tomorrow**：疯魔 {0}，将所有永久物洗回牌库，翻出等量的新永久物
- **Avalanche Riders**：疯魔，炸对手地

## 代表性牌张

| 牌名 | 正常费用 | 疯魔费用 | 效果 |
|------|---------|---------|------|
| Living End | {3}{B}{B}{R} | {0} | 消灭所有生物，将坟场生物回场 |
| Glimpse of Tomorrow | {2}{R}{R} | {0} | 将所有永久物洗回牌库，翻出等量新永久物 |
| Basking Rootwalla | {G} | {0} | 1/1 生物；可以支付 {0} 得 +2/+2 |
| Arrogant Wurm | {3}{G}{G} | {2}{G} | 4/4 践踏 |
| Big Game Hunter | {1}{B}{B} | {B} | 1/1；进场时消灭目标力量 4 以上的生物 |

## 经典套牌

### Living End（Modern）
- 核心：Violent Outburst / Demonic Dread（倾曳）→ 翻出 Living End（唯一 0 费牌）
- 配合：Street Wraith、Fulminator Mage 等具有循环或自磨效应的牌
- 思路：将生物送入坟场，然后用 Living End 集体复活

### Hollow One / Vengevine
- 利用 Burning Inquiry、Goblin Lore 等随机弃牌
- 弃掉 Hollow One（通常可以免费施放）或 Vengevine（从坟场直接回场）

## 历史

- 疯魔首次出现于 **Torment（折磨，2002）**
- 最初作为黑色主题的弃牌互动机制
- 后来在 **Time Spiral（2006）** 和 **Shadows over Innistrad（2016）** 中回归
- **Modern Horizons 2（2021）** 引入了 Glimpse of Tomorrow 等新的疯魔组合技

## 相关页面

- [[keyword-abilities-overview|关键字异能总览]]
- [[graveyard|坟场]]
- [[discard|弃牌]]
- [[cascade|倾曳（Cascade）]]
- [[comprehensive-rules|完整规则]]
- [[mtg-formats|万智牌赛制]]
- [[modern|摩登]]
