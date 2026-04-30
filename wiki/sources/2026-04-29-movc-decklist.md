---
created: 2026-04-29
updated: 2026-04-29
type: source
tags: [数据来源, MO, MTGO, Vintage Cube, 牌池分析]
sources: [MTGOVintageCube.txt, raw/tools/mtg_wiki/data/movc_cards.json]
---

# MO Vintage Cube 牌池分析

## 来源信息

- **平台**：Magic Online (MTGO)
- **系列**：Vintage Cube（MO 版本）
- **牌池大小**：540 张
- **数据获取**：Raymond 提供原始牌表，`card_search.py` 批量查询 Oracle 数据

## 颜色分布

| 颜色 | 数量 | 占比 |
|------|------|------|
| 蓝 (U) | 74 | 16.0% |
| 黑 (B) | 65 | 14.1% |
| 无色 (C) | 64 | 13.9% |
| 红 (R) | 64 | 13.9% |
| 绿 (G) | 61 | 13.2% |
| 白 (W) | 56 | 12.1% |
| 多色 | 56 | 12.1% |
| **非地总计** | 440 | 100% |

## 费用分布

| CMC | 数量 | 典型牌 |
|------|------|--------|
| 0 | 117 | Black Lotus、Moxen、Sol Ring、Ballista |
| 1 | 96 | Brainstorm、Lightning Bolt、Path to Exile |
| 2 | 128 | Swords to Plowshares、Force of Will、Jace |
| 3 | 92 | Dig Through Time、Tarmogoyf、Liliana |
| 4 | 47 | Griselbrand、Dack Fayden |
| 5+ | 50 | 大量高费威胁和组合技组件 |

## 稀有度分布

| 稀有度 | 数量 |
|--------|------|
| Rare | 297 |
| Mythic | 123 |
| Uncommon | 68 |
| Common | 40 |
| Special | 12 |

## 单卡类型

| 类型 | 数量 |
|------|------|
| 生物 | 205 |
| 地 | 99 |
| 瞬间 | 68 |
| 神器 | 67 |
| 法术 | 60 |
| 鹏洛客 | 21 |
| 结界 | 20 |

## Power 9 确认

- [ ] Black Lotus
- [ ] Mox Pearl / Mox Sapphire / Mox Jet / Mox Ruby / Mox Emerald
- [ ] Ancestral Recall
- [ ] Time Walk
- [ ] Time Twister

## 套牌原型适配性

### Blue-X Control（最强路线）
- 蓝：74 张，包含 Brainstorm、Force of Will、Jace the Mind Sculptor
- 关键配合：Brainstorm + fetchland 滤牌、FoW 主牌、Counterspell 互动

### Storm Combo
- Demonic Tutor、Ad Nauseam、Tendrils of Agony、Brain Freeze
- 需要 Rituals：Dark Ritual、C肢 Flame of the Night

### 白/红 Aggro
- 56 白牌 + 64 红牌，支持节奏快攻路线
- Swords to Plowshares、Path to Exile 去除

### Tinker / Big Mana
- 大量 0 费神器（Moxen、Lotus Petal、Mana Crypt）
- Tinker + Blightsteel Colossus

## 相关链接

- [[vintage-cube-draft-strategy|Vintage Cube 选卡策略]]
- [[draft|轮抽]]
- [[combo|组合技]]
