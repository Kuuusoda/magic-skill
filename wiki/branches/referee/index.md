---
created: 2026-04-27
updated: 2026-04-28
type: concept
tags: [referee, index, navigation]
sources: []
---

# 裁判分支索引

本目录包含裁判 agent (`mtg-judge-zh`) 专用的决策知识。

## 快速导航

| 目录 | 内容 | 状态 |
|------|------|------|
| [decision-tree-router](./decision-tree-router.md) | **决策树路由器**（关键词→决策树映射） | ✅ |
| [decision-trees](./decision-trees/) | 决策树（31 个） | ✅ |
| [frameworks](./frameworks/) | 分析框架（4 个） | 🚧 |
| [common-traps](./common-traps/) | 常见陷阱与误判 | 📋 |
| [mtr-ipg-guides](./mtr-ipg-guides/) | 比赛规则与违规处理 | 📋 |
| [test-questions](./test-questions/) | 测试题库 | 📋 |

---

## 决策树

### 核心规则

| 决策树 | CR | 核心内容 |
|--------|-----|----------|
| [[state-based-actions]] | 704 | SBA 检查时机、致命伤害、防御力≤0、传奇规则、指示物抵消 |
| [[targeting]] | 115 | 目标定义、合法目标、fizzle vs 反击、"any target"限制 |
| [[damage]] | 120 | 伤害处理四步骤、侵染、系命、干枯 |
| [[costs]] | 118, 702.66 | 总费用计算顺序、替代/额外费用、三定法球、掘穴 |
| [[counters]] | 122 | +1/+1 与 -1/-1 抵消、增殖、加倍 |
| [[tokens]] | 111 | 衍生物创建、区域变更、复制、消失 |
| [[zone-changes]] | 400 | 区域变更 = 新对象、云移、离开战场触发 |
| [[mana-abilities]] | 605 | 法术力异能三条件、不使用堆叠 |

### 战斗

| 决策树 | CR | 核心内容 |
|--------|-----|----------|
| [[combat-phase]] | 506-511 | 五步骤、宣告攻击/阻挡合法性、被阻挡后牺牲阻挡者 |
| [[combat-keywords]] | 702.9/10/17/20 | 飞行、延势、敏捷、警戒 |
| [[first-strike-double-strike]] | 702.4/7 | 两个伤害步骤、连击两次伤害 |
| [[trample]] | 702.19 | 践踏伤害分配、死触 1 点致命 |
| [[deathtouch]] | 702.2 | 死触 SBA、与先攻/不灭/践踏互动 |

### 永久物存活

| 决策树 | CR | 核心内容 |
|--------|-----|----------|
| [[removal-and-survival]] | 700.4, 701.7/15/17, 702.12 | 死亡/消灭/牺牲区别、不灭、重生 |
| [[protection]] | 702.16 | DEBT 四要素、反一切保护 |
| [[targeting-restrictions]] | 702.11/18/21 | 辟邪、帷幕、守护（对比表） |

### 牌张类别

| 决策树 | CR | 核心内容 |
|--------|-----|----------|
| [[equipment-auras]] | 301, 303 | 佩带时机、灵气贴附、非施放进场 |
| [[lands]] | 305 | 使用地牌、类别改变、地生物 |
| [[planeswalkers]] | 306 | 忠诚异能、伤害转移、鹏洛客类别传奇规则 |

### 常用机制

| 决策树 | CR | 核心内容 |
|--------|-----|----------|
| [[cascade]] | 702.85 | 倾曳放逐与施放 |
| [[convoke]] | 702.51 | 召集横置支付、召唤失调不影响 |
| [[flashback]] | 702.34 | 返照替代费用、放逐替代进坟 |
| [[suspend]] | 702.62 | 延缓只能从手牌、X=0 |
| [[harmonize]] | — | Harmonize 关键字动作 |

### 异能机制

| 决策树 | CR | 核心内容 |
|--------|-----|----------|
| [[copy-effects]] | 707 | 复制品可复制值、进战场作为复制品 |
| [[intervening-if]] | 603.4 | 干涉条件、触发 vs 结算 |
| [[modal-abilities]] | 700.2 | Modal 模式选择时机 |
| [[replacement-effects]] | 614 | 替代效应判断、多重顺序 |
| [[triggered-ability-structure]] | 603 | "When you do" 结构 |
| [[x-spell-mana-value]] | 202.3 | 堆叠上/非堆叠上 X 咒语的 MV |
| [[lifelink]] | 702.15 | 系命静止式异能、与侵染同时 |

## 分析框架

- [[layer-system|层系统判定框架]] — CR 613 跨层效应与从属关系
- [[stack-resolution|堆叠推演框架]] — 堆叠结算与优先级传递
- [[ability-types|异能类型识别框架]] — 启动式/触发式/静止式
- [[replacement-effects|替代/预防效应框架]] — CR 614/615

## 关联通用知识

- [[../../concepts/layer-system|层系统（通用概念）]]
- [[../../concepts/stack|堆叠（通用概念）]]
- [[../../concepts/triggered-abilities|触发式异能（通用概念）]]
