---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept
block: cedh-combo
format: cedh
lock_type: ""                              # 留空=制胜 combo；soft-lock/hard-lock=stax 锁
tags: [cEDH, 组合技, <combo名>]
commander: ""                               # 通用 combo 留空；主将专属则填
archetype: ""                               # 常见承载原型，可留空
sources: [<规则/裁定/primer 链接>]
as_of: YYYY-MM-DD
cards_cited:                               # 穷举：本块涉及的所有组件牌（双语）；CI 逐张离线查证
  - "<牌名中文（English）>"
---

# <combo / lock 中文名>（<English>）

> 一句话：<这条线产出什么 / 如何制胜，或这把锁锁住什么>

## 核心组件
| 组件 | 官方异能（card_search 查证） | 作用 |
|------|------------------------------|------|
| <中文（English）> | <Oracle 文本，逐字核实> | … |
| … | … | … |

## 执行步骤
1. ……
2. ……
3. ……

## 费用与前置
- 启动费用：……
- 前置条件：<场上需要什么 / 牌库状态>

## 锁信息（仅 lock 类填，制胜 combo 留空本节）
- 锁类型：<soft-lock 软锁 / hard-lock 硬锁>
- 锁住什么：<对手被禁止的动作>
- 解锁条件：<对手如何挣脱>
- 我方豁免：<如何不被自己的锁锁住>

## 脆弱点
- ……（如：可被某类去除/反制打断）

## 与套牌的关系
- 承载套牌：`[[branches/strategy/cedh/decks/<deck>]]`

---
*每张牌异能必须以 `card_search.py` 官方 Oracle 文本为证，严禁凭记忆编造。*
