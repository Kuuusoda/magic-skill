---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: synthesis
block: dc-deck
format: duel-commander
status: <seed|stub|draft|verified|deprecated>
tags: [Duel Commander, 法禁, 套牌, <原型>]
commander: "<主将中文（English）>"
pair_type: <single|partner|partner-with|friends-forever|background>
archetype: <Aggro|Control|Midrange|Combo|Stax|Voltron|Tempo>
sources: [<赛事报告/牌表/primer 链接或本地文件>]
as_of: YYYY-MM-DD
banlist_as_of: YYYY-MM-DD
rules_as_of: YYYY-MM-DD
match_policy: default
event_policy_source: ""
cards_cited:
  - "<中文（English）>"
---

# <套牌中文名>（<English>）

> 一句话定位：<这套牌的主要计划、速度档位、最怕的对局>。

## 信息边界

- 数据时效：`<as_of>`
- 禁牌表版本：`<banlist_as_of>`
- 规则快照：`<rules_as_of>`
- 赛事政策：`<default / event-specific>`，来源：`<event_policy_source>`
- 可信度：<公开牌表充足 / 少量样本 / 观察假设>

## 牌表审计

- 牌表完整度：<100 张完整 / 核心牌包 / stub>
- 单例制风险：<无 / 待查 / 说明>
- 禁牌风险：<无 / 待查 / 说明>
- 仅禁指挥官风险：<无 / 待查 / 说明>
- 结构风险：<companion / outside-the-game / stickers / attractions / acorn / digital-only / ante / dexterity>

## 指挥官与颜色身份

- 指挥官：<中文（English）>
- 颜色身份：<WUBRG 子集>
- 指挥官依赖度：<commander-centric | commander-enabled | commander-optional>
- 指挥官被处理后的备用计划：<说明>

## 原型定位

- 原型：<Aggro / Control / Midrange / Combo / Stax / Voltron / Tempo>
- 判定理由：<为什么不是相邻原型>
- 典型速度：<T1/T2/T3 目标动作>
- 先手 plan：<T1/T2/T3>
- 后手 plan：<T1/T2/T3>

## 核心计划

- 主计划：<说明>
- 备用计划：<说明>
- 关键资源：<手牌 / 坟场 / 战场 / 法术力 / 生命>

## 起手与 London Mulligan

| 场景 | Keep 标准 | Mulligan 标准 |
|------|-----------|----------------|
| 先手 | <两地一动/一费互动/曲线> | <缺地/过慢/互动不足> |
| 后手 | <补互动/防快攻/防组合技> | <无法影响前两回合> |
| vs Aggro | <说明> | <说明> |
| vs Control | <说明> | <说明> |
| vs Combo | <说明> | <说明> |

## 20 血资源账本

- 付血资源：<痛地/抓牌/古墓类效应>
- Race 阈值：<何时不能继续付血>
- 对快攻的生命线：<说明>

## 地基与曲线审计

- 地数量：<n>
- 彩色源：<W/U/B/R/G 各自数量或待补>
- 横置地密度：<说明>
- 一费动作：<数量/类型>
- 二费动作：<数量/类型>
- 三费动作：<数量/类型>
- 不能接受的起手模式：<说明>

## 互动配置

| 类型 | 代表牌 | 角色 |
|------|--------|------|
| 去除 | <中文（English）> | <说明> |
| 反击 | <中文（English）> | <说明> |
| 弃牌 | <中文（English）> | <说明> |
| 扫场 | <中文（English）> | <说明> |
| 坟场针对 | <中文（English）> | <说明> |
| 地针对 | <中文（English）> | <说明> |

## Flex Slots

| 卡位 | 默认选择 | 替换方向 | 适用 meta |
|------|----------|----------|-----------|
| <slot> | <中文（English）> | <说明> | <偏快/偏控/偏 combo/未知> |

## 对局矩阵

| 对手原型 | 先手 | 后手 | 关键分岔 |
|----------|------|------|----------|
| Aggro | <优/平/劣> | <优/平/劣> | <说明> |
| Control | <优/平/劣> | <优/平/劣> | <说明> |
| Midrange | <优/平/劣> | <优/平/劣> | <说明> |
| Combo | <优/平/劣> | <优/平/劣> | <说明> |
| Stax | <优/平/劣> | <优/平/劣> | <说明> |
| Tempo | <优/平/劣> | <优/平/劣> | <说明> |

## 局间换将

- 是否适用：<不适用 / partner / partner-with / friends forever / background>
- 默认组合：<说明>
- 换将条件：<说明>
- 注意：颜色身份不能改变，只能使用牌表登记的合法指挥官组合。

## 时钟计划

- BO3/50 默认下的慢速风险：<低/中/高>
- 领先时：<如何收束>
- 落后时：<何时转为高风险进攻线>
- 平局风险：<说明>

---
*规则裁定让渡给 `mtg-judge-zh`；套牌强度判断必须绑定 `as_of`、`banlist_as_of` 与来源。*
