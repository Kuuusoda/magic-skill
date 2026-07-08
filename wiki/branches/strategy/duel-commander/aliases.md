---
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [Duel Commander, 法禁, aliases, entity-resolution]
sources: []
---

# Duel Commander 别名与简称解析

本页记录法禁语境中的牌名、指挥官、套牌简称。它不是事实本体，只是 `card_resolve.py` 和 skill 消歧的提示层。

## 使用规则

- 短名、数字、绰号、半截英文名必须先解析候选。
- 别名命中不等于永久事实；必须结合 `as_of`、来源和当前内容块语境。
- 低置信或候选接近时，先追问用户。
- 不得把 `card_search.py` 的第一个 fuzzy 结果当作用户意图。

## 初始别名

| alias | preferred | entity | intent | as_of | reason |
|-------|-----------|--------|--------|-------|--------|
| `2099` | Spider-Man 2099, Miguel O'Hara | card | commander | 2026-07-08 | 法禁玩家可能用数字简称指该指挥官 |
| `spider99` | Spider-Man 2099, Miguel O'Hara | card | commander | 2026-07-08 | 避免落到 Spider token 或宽泛 Spider 搜索 |
| `phelia` | Phelia, Exuberant Shepherd | card | commander | 2026-07-08 | 避免被相近字符串误伤到 Aphelia |
| `kess` | Kess, Dissident Mage | card | commander | 2026-07-08 | 避免被 Kessig 前缀误伤 |
| `niv` | Niv-Mizzet, Parun | card | commander | 2026-07-08 | Niv-Mizzet 多版本，低置信时应列候选 |
| `squee/slimefoot` | Slimefoot and Squee | card | commander | 2026-07-08 | 单名与组合指挥官冲突 |

## 维护要求

新增别名时至少补：

- preferred 的英文官方牌名或套牌名；
- entity 类型：`card` / `deck` / `combo` / `archetype`；
- 适用 intent；
- `as_of`；
- 来源或添加理由。

