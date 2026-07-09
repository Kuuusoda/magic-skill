---
created: 2026-07-08
updated: 2026-07-09
type: concept
tags: [Duel Commander, 法禁, strategy, index]
sources: []
---

# Duel Commander（法禁）策略分支

本分支记录 Duel Commander（法禁）的竞技策略资料。通用赛制定义见 [[duel-commander]]；本分支只回答“如何准备、分析和使用法禁策略资料”。

## 范围

- 1v1、20 起始生命、无指挥官伤害。
- 官方默认 BO3/50 分钟；赛事可在赛前公告覆盖。
- 使用 Duel Commander 独立禁牌表。
- 与多人 cEDH 并列，不能套用多人政治、40 血或官方 EDH 禁牌表结论。

## 导航

- [[duel-commander/meta-snapshots/2026-07-08-dc-seed|最小环境快照占位]]
- [[duel-commander/banlist/2026-01-26-official|官方禁牌表快照（2026-01-26）]]
- [[duel-commander/decks/kess-dissident-mage|Kess, Dissident Mage 待补套牌块]]
- [[duel-commander/decks/niv-mizzet-parun|Niv-Mizzet, Parun 待补套牌块]]
- [[duel-commander/decision-trees/tournament-prep-checklist|大型赛事备战检查]]
- [[duel-commander/aliases|法禁别名与简称解析]]
- [[duel-commander/rules/source-registry|规则与禁牌表来源注册表]]

## 目录

| 目录 | 内容 |
|------|------|
| `decks/` | 指挥官套牌拆解 |
| `meta-snapshots/` | 环境快照 |
| `decision-trees/` | 起手、先后手、对局决策 |
| `combos/` | 组合技与 lock 线 |
| `card-evaluations/` | 法禁语境下的单卡评估 |
| `banlist/` | 禁牌表快照，合法性判断的单一事实源 |
| `rules/` | 官方规则快照与来源注册表 |

## 内容要求

- deck/meta 块必须同时标注 `status`、`as_of`、`banlist_as_of`、`rules_as_of`。
- 强弱、Tier、占比必须绑定来源；没有样本只能写观察假设。
- 禁牌表不得散落在套牌或单卡页中重复维护。
- `seed` / `stub` 只可作为导航或待补结构，不得作为强度、meta 或合法性结论。
- 短名、数字、俗称、半截名先用 `card_resolve.py --format duel-commander` 解析。
- 大型赛事备战必须先确认赛事日期、规则版本、禁牌表版本和 event policy；缺少这些信息时不得确认牌表合法。

## 当前状态

本分支处于种子阶段：已有目录、模板、别名解析约定和最小占位内容；正式 meta 结论需要后续导入公开赛事样本与首份 banlist 快照后再写入。
