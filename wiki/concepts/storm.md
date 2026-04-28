---
created: 2026-04-19
updated: 2026-04-19
type: concept
tags: [万智牌, 机制, 风暴, Storm, 组合技, 关键字异能]
sources: [cr/7.md, data/keywords-index.json, data/oracle-cards-lite.json]
---

# 风暴（Storm）

## 定义

风暴（Storm）是一个触发式异能，当具有风暴的咒语被施放时，会额外复制该咒语若干次，复制的次数等于本回合中在该咒语之前已被施放的咒语数量（CR 702.40）。

## 核心规则

### 触发条件
- 风暴在具有风暴的咒语**被施放时**触发
- 计算本回合中**此前已被施放的咒语数量**（包括对手施放的咒语，也包括该风暴咒语本身之前的所有咒语）
- 风暴触发后，会复制该咒语那么多次

### 复制规则
- 每次复制都可以选择新的目标（如果原咒语需要目标）
- 复制产生的咒语直接进入堆叠，不经过施放过程
- 复制的咒语结算后若将进入坟墓场，则改为被放逐
- 原版咒语的结算不受复制影响

### 关键细节
- **「施放」的定义**：只有从手中或其他区域被施放的咒语才算数。被复制、被倾曳、从坟墓场闪回的咒语是否算「施放」取决于具体机制
- **本回合计数重置**：每个新回合开始时，风暴计数清零
- **多人游戏中的风暴**：在多人游戏中，风暴计算的是**整个回合中所有牌手施放的咒语总数**，不仅仅是施放风暴咒语的牌手

## 风暴与组合技

风暴是万智牌中最著名的**终结型组合技机制**之一。典型的风暴套牌思路是：

1. **快速产生法术力**：通过 Dark Ritual、Rite of Flame、Lion's Eye Diamond 等牌产生大量法术力
2. **连续施放廉价咒语**：施放大量零费或低费咒语（如 Gitaxian Probe、Manamorphose、Chrome Mox）
3. **施放风暴终结技**：当本回合已施放足够多咒语后，施放 Tendrils of Agony 或 Grapeshot 等风暴咒语
4. **复制终结对手**：风暴咒语被复制数十次，直接击杀对手

### 经典风暴套牌

| 套牌 | 赛制 | 核心思路 |
|------|------|---------|
| ANT（Ad Nauseam Tendrils）| Legacy | Ad Nauseam 抽光牌库后用 Tendrils 终结 |
| TES（The Epic Storm）| Legacy | Burning Wish 找终结技 + 快速 mana |
| Gifts Storm | Modern | Gifts Ungiven 堆坟 + Past in Flames |
| High Tide | Legacy | 利用 High Tide 翻倍海岛产费 |

## 代表牌张

| 牌名 | 费用 | 效果 | 说明 |
|------|------|------|------|
| Tendrils of Agony | {2}{B}{B} | 目标牌手失去 2 点生命，你获得 2 点生命 | Legacy 风暴的经典终结技 |
| Grapeshot | {1}{R} | 对任意目标造成 1 点伤害 | Modern 风暴的终结技 |
| Brain Freeze | {1}{U}{U} | 目标牌手磨三张牌 | 可用于 mill 对手 |
| Empty the Warrens | {3}{R} | 创建 2/2 鬼怪衍生物 | 风暴计数低时的备选终结 |
| Flusterstorm | {U} | 反击目标非生物咒语 | 反风暴的风暴咒语 |

## 风暴的 counterplay

由于风暴套牌依赖连续施放多个咒语，以下手段可以有效对抗：
- **单一强力反击**：如 Force of Will、Flusterstorm（本身也是风暴，可以在对手的风暴咒语上产生更多复制）
- **锁场效应**：如 Rule of Law、Ethersworn Canonist（限制每回合只能施放一个咒语）
- ** graveyard hate**：针对依赖坟场的风暴套牌（如 Past in Flames）

## 历史

- 风暴首次出现于 **灾祸（Scourge，2003）**
- 最初被认为是一个有趣但难以控制的机制
- 随着 Lion's Eye Diamond、Dark Ritual 等快速 mana 牌的存在，风暴迅速成为 Legacy 和 Vintage 中最强的组合技之一
- 万智牌设计团队后来表示风暴是一个「设计失误」——因为它太难平衡，且对游戏体验的影响过于极端

## 相关页面

- [[keyword-abilities-overview|关键字异能总览]]
- [[comprehensive-rules|完整规则]]
- [[stack|堆叠]]
- [[异能|触发式异能]]
- [[cascade|倾曳（Cascade）]]
- 诈术（Delve）
- 组合技思路
- [[mtg-formats|万智牌赛制]]
- [[legacy|薪传]]
- [[modern|摩登]]
