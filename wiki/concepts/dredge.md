---
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [万智牌, 关键字异能, 发掘, 坟场, 抓牌]
sources: [cr/7.md, data/keywords-index.json, data/oracle-cards-lite.json]
---

# 发掘（Dredge）

## 定义

发掘（Dredge）是一个替代式异能，当牌手将要抓一张牌时，可以选择改为从牌库顶将指定数量的牌置入坟墓场，然后将具有发掘异能的牌从其坟墓场移回手牌（CR 702.52）。发掘是万智牌中最强大的坟场填充机制之一，也是 Dredge 套牌的核心引擎。

## 核心规则

### 标准叙述
```
发掘 N（若你将要抓一张牌，你可以改为从牌库顶将 N 张牌置入你的坟墓场。若你如此作，将此牌从你的坟墓场移回你手牌。）
```

### 关键限制
- **替代抓牌**：发掘只能在「将要抓一张牌」时触发，包括正常的抓牌步骤、咒语/异能导致的抓牌等
- **坟场必须有该牌**：若具有发掘的牌不在坟场中，则无法使用发掘异能
- **数量固定**：必须精确从牌库顶置入指定数量的牌（如 Dredge 6 就必须置入 6 张）
- **可选使用**：每次抓牌时都可以选择是否使用发掘，而非强制
- **多张发掘牌**：若坟场中有多个具有发掘的牌，每次只能使用其中一个的发掘异能

### 与「不能抓牌」的交互
若某效应阻止你抓牌（如 Narset, Parter of Veils、Spirit of the Labyrinth），你不能使用发掘，因为发掘的前提是「将要抓一张牌」。

## 战略价值

### 1. 坟场填充引擎
发掘的核心价值不在于「将牌回手」，而在于「将大量牌从牌库置入坟场」。在 Dredge 套牌中，牌库顶的牌被快速填入坟场，然后通过 Flashback、Unearth、Ichorid 等机制从坟场直接使用。

### 2. 规避手牌限制
发掘牌从坟场回手，因此可以规避手牌上限限制。更常见的策略是根本不关心它们是否回手——只要坟场被填满即可。

### 3. 自磨制胜
某些 Dredge 变体通过大量自磨后直接利用坟场资源获胜：
- **Ichorid**：在你的维持开始时，若它在坟场中，可以将其移回战场
- **Narcomoeba**：从牌库置入坟场时进场
- **Cabal Therapy**：从坟场施放（Flashback）来破坏对手手牌
- **Dread Return**：从坟场施放，拉回大型生物（如 Flame-Kin Zealot 或 Elesh Norn）

## 代表性牌张

| 牌名 | 费用 | 发掘 | 效果 |
|------|------|------|------|
| Golgari Grave-Troll | {4}{G} | 6 | 0/0；进战场时得 +1/+1（X 为你坟场中的生物牌数量）；{1}：再生 |
| Stinkweed Imp | {2}{B} | 5 | 1/2 飞行、延势；当它造成战斗伤害时，消灭该生物 |
| Life from the Loam | {1}{G} | 3 | 法术；将最多三张目标地牌从你的坟场移回手牌 |
| Darkblast | {B} | 3 | 瞬间；目标生物得 -1/-1 直到回合结束； dredge 3 |
| Shambling Shell | {1}{B}{G} | 3 | 3/1；牺牲 Shambling Shell：目标生物得 +1/+1 和 trample |

## 历史

- 发掘首次出现于 **Ravnica: City of Guilds（拉尼卡：公会城，2005）**
- 作为葛加理（Golgari）公会「循环利用」主题的机制
- 在 **Modern** 中，Dredge 套牌曾多次成为顶级套牌，迫使 Wizards 对关键牌进行限制或禁掉
- **Golgari Grave-Troll** 曾因 Dredge 套牌过于强势而在 Modern 中被禁
- **Life from the Loam** 在 Legacy 和 Commander 中长期作为 staple

## 与「门槛」和「掘穴」的关系

发掘会快速填满坟场，因此与 Threshold（门槛）和 Delve（掘穴）有天然协同。但需要注意：发掘本身消耗抓牌机会，因此在使用 Dredge 套牌时，通常不需要传统的「抓牌」手段，而是直接利用坟场资源。

## 相关页面

- [[graveyard|坟场]]
- [[threshold|门槛]]
- [[delve|掘穴]]
- [[flashback|闪回]]
- [[discard|弃牌]]
- [[comprehensive-rules|完整规则]]
- [[mtg-formats|万智牌赛制]]
