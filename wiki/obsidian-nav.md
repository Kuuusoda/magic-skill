---
created: 2026-04-21
updated: 2026-04-22
type: output
tags: [导航, Obsidian, 万智牌]
sources: []
---

# MTG Wiki 导航中心

本页是 Obsidian 内的快速导航入口。点击任意链接即可在 Obsidian 中跳转。

---

## 核心概念

| 页面 | 链接 |
|------|------|
| 组合技 | [[wiki/concepts/combo\|组合技]] |
| 组合技引擎牌 | [[wiki/concepts/combo-engine-cards\|组合技引擎牌]] |
| 无限法术力组合技 | [[wiki/concepts/infinite-mana-combos\|无限法术力组合技]] |
| 风暴 | [[wiki/concepts/storm\|风暴]] |
| 万智牌 | [[wiki/concepts/magic-the-gathering\|万智牌]] |
| 完整规则（CR） | [[wiki/concepts/comprehensive-rules\|完整规则（CR）]] |

## 策略与构筑

| 页面 | 链接 |
|------|------|
| 套牌原型 | [[wiki/concepts/deck-archetypes\|套牌原型]] |
| 卡牌优势 | [[wiki/concepts/card-advantage\|卡牌优势]] |
| 法术力曲线 | [[wiki/concepts/mana-curve\|法术力曲线]] |
| 去除 | [[wiki/concepts/removal\|去除]] |
| 反击咒语 | [[wiki/concepts/counterspell\|反击咒语]] |
| 检索 | [[wiki/concepts/tutor\|检索]] |
| 跳费 | [[wiki/concepts/ramp\|跳费]] |

## 赛制

| 页面 | 链接 |
|------|------|
| 万智牌赛制 | [[wiki/concepts/mtg-formats\|万智牌赛制]] |
| 标准赛 | [[wiki/concepts/standard\|标准赛]] |
| 先驱 | [[wiki/concepts/pioneer\|先驱]] |
| 摩登 | [[wiki/concepts/modern\|摩登]] |
| 薪传 | [[wiki/concepts/legacy\|薪传]] |
| 特选 | [[wiki/concepts/vintage\|特选]] |
| 指挥官 | [[wiki/concepts/commander\|指挥官]] |
| cEDH | [[wiki/concepts/cedh\|cEDH]] |
| 颜色认同 | [[wiki/concepts/color-identity\|颜色认同]] |
| 指挥官税 | [[wiki/concepts/commander-tax\|指挥官税]] |
| EDH 禁牌表 | [[wiki/concepts/edh-banned-list\|EDH 禁牌表]] |

## 规则核心

| 页面 | 链接 |
|------|------|
| 堆叠 | [[wiki/concepts/stack\|堆叠]] |
| 时机和优先权 | [[wiki/concepts/timing-and-priority\|时机和优先权]] |
| 回合结构 | [[wiki/concepts/turn-structure\|回合结构]] |
| 战斗阶段 | [[wiki/concepts/combat-phase\|战斗阶段]] |
| 施放咒语 | [[wiki/concepts/casting-spells\|施放咒语]] |
| 法术力 | [[wiki/concepts/mana\|法术力]] |
| 异能 | [[wiki/concepts/abilities\|异能]] |
| 持续性效应 | [[wiki/concepts/continuous-effects\|持续性效应]] |
| 状态动作 | [[wiki/concepts/state-based-actions\|状态动作]] |
| 替代性效应与防止性效应 | [[wiki/concepts/replacement-and-prevention-effects\|替代性效应与防止性效应]] |

## 牌张类型

| 页面 | 链接 |
|------|------|
| 生物 | [[wiki/concepts/creature\|生物]] |
| 神器 | [[wiki/concepts/artifact\|神器]] |
| 瞬间 | [[wiki/concepts/instant\|瞬间]] |
| 法术 | [[wiki/concepts/sorcery\|法术]] |
| 结界 | [[wiki/concepts/enchantment\|结界]] |
| 地 | [[wiki/concepts/land\|地]] |
| 鹏洛客 | [[wiki/concepts/planeswalker\|鹏洛客]] |

## 来源摘要

| 页面 | 链接 |
|------|------|
| EDHREC 组合技数据库 | [[wiki/sources/2026-04-21-edhrec-combos\|EDHREC 组合技数据库]] |
| 万智牌完整规则（Markdown） | [[wiki/sources/2026-04-14-cr-markdown\|万智牌完整规则（Markdown 中文版）]] |
| 万智牌比赛规则 | [[wiki/sources/2026-04-14-mtr\|万智牌比赛规则（MTR）]] |
| 违规处理方针 | [[wiki/sources/2026-04-14-ipg\|万智牌违规处理方针（IPG）]] |

## 综合

| 页面 | 链接 |
|------|------|
| 万智牌官方文档体系概览 | [[wiki/synthesis/mtg-official-documents\|万智牌官方文档体系概览]] |
| 万智牌赛制可用性分析 | [[wiki/synthesis/format-legality-analysis\|万智牌赛制可用性分析]] |

## 工具脚本

以下脚本可在项目根目录下直接执行（假设你已将此仓库克隆到本地）：

```bash
# 牌张查询
python3 raw/tools/mtg_wiki/card_search.py "闪电击"

# 规则查询
python3 raw/tools/mtg_wiki/rule_search.py "堆叠"

# 牌名翻译
python3 raw/tools/mtg_wiki/name_translator.py "Lightning Bolt"
```

---

*最后更新：2026-04-21*
