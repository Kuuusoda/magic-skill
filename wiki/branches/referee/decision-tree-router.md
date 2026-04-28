---
created: 2026-04-28
updated: 2026-04-28
type: concept
tags: [referee, router, retrieval, dispatch]
sources: []
---

# 决策树路由器

Agent 回答规则问题前，先通过此路由器确定需要查阅的决策树。

## 路由流程

```
问题输入
  │
  ├─ 1. 关键词匹配 → 查下表，确定候选决策树
  ├─ 2. 场景分类   → 确定问题类型
  ├─ 3. 交叉判定   → 多领域合并候选列表
  └─ 4. 加载树     → 按优先级读取决策树
```

## 一、关键词 → 决策树映射

| 关键词 | 主决策树 | 相关决策树 |
|--------|----------|------------|
| 目标、指定、fizzle、失效 | [[targeting]] | [[targeting-restrictions]], [[protection]] |
| 辟邪、帷幕、守护、不能被指定 | [[targeting-restrictions]] | [[targeting]], [[protection]] |
| 伤害、造成、系命、侵染、中毒 | [[damage]] | [[lifelink]], [[deathtouch]], [[trample]] |
| 战斗、攻击、阻挡、宣告 | [[combat-phase]] | [[first-strike-double-strike]], [[combat-keywords]], [[trample]] |
| 飞行、延势、敏捷、警戒 | [[combat-keywords]] | [[combat-phase]] |
| 先攻、连击、伤害步骤 | [[first-strike-double-strike]] | [[combat-phase]], [[deathtouch]] |
| 消灭、牺牲、死亡、不灭、重生 | [[removal-and-survival]] | [[state-based-actions]], [[damage]] |
| SBA、状态动作、防御力≤0、致命伤害 | [[state-based-actions]] | [[removal-and-survival]], [[damage]] |
| 指示物、+1/+1、-1/-1、增殖 | [[counters]] | [[state-based-actions]], [[tokens]] |
| 衍生物、token、populate | [[tokens]] | [[counters]], [[copy-effects]], [[zone-changes]] |
| 费用、施放、法术力、增幅、减费 | [[costs]] | [[mana-abilities]], [[x-spell-mana-value]] |
| 掘穴、delve | [[costs]] | [[flashback]] |
| 层、持续性效应、时间印记 | [[layer-system]] (fwk) | [[copy-effects]], [[protection]] |
| 堆叠、优先权、响应、结算 | [[stack-resolution]] (fwk) | [[targeting]], [[mana-abilities]] |
| 触发式异能、当...时 | [[triggered-ability-structure]] | [[intervening-if]], [[modal-abilities]] |
| 保护、反...保护、DEBT | [[protection]] | [[targeting]], [[combat-phase]], [[targeting-restrictions]] |
| 武具、佩带、灵气、结附 | [[equipment-auras]] | [[protection]], [[targeting-restrictions]] |
| 地、下地、法术力异能 | [[lands]] | [[mana-abilities]], [[costs]] |
| 鹏洛客、忠诚、旅法师 | [[planeswalkers]] | [[damage]], [[state-based-actions]], [[combat-phase]] |
| 传奇、同名 | [[state-based-actions]] | [[planeswalkers]], [[copy-effects]] |
| 延缓、suspend | [[suspend]] | [[costs]], [[x-spell-mana-value]] |
| X 咒语、CMC、MV | [[x-spell-mana-value]] | [[costs]], [[suspend]] |
| 复制、clone、copy | [[copy-effects]] | [[tokens]], [[state-based-actions]] |
| 模态、选择一项 | [[modal-abilities]] | — |
| 区域、离场、进坟场、放逐 | [[zone-changes]] | [[tokens]], [[removal-and-survival]] |

## 二、快速路由决策图

```
问题是关于...
├─ 能不能攻击/阻挡？
│   ├─ 先攻/连击？  → first-strike-double-strike + combat-phase
│   ├─ 飞行/延势？  → combat-keywords + combat-phase
│   ├─ 敏捷/警戒？  → combat-keywords + combat-phase
│   └─ 一般情况     → combat-phase
│
├─ 伤害怎么算？
│   ├─ 死触？       → deathtouch + damage
│   ├─ 践踏？       → trample + combat-phase + damage
│   ├─ 系命？       → lifelink + damage
│   ├─ 侵染？       → damage
│   ├─ 保护？       → protection + damage
│   └─ 一般         → damage
│
├─ 生物死不死？
│   ├─ 致命伤害？   → state-based-actions + removal-and-survival
│   ├─ 防御力≤0？  → state-based-actions
│   ├─ 被消灭？     → removal-and-survival
│   ├─ 被牺牲？     → removal-and-survival
│   ├─ 传奇规则？   → state-based-actions
│   └─ 重生？       → removal-and-survival
│
├─ 能不能指定为目标？
│   ├─ 辟邪/帷幕？  → targeting-restrictions + targeting
│   ├─ 守护？       → targeting-restrictions
│   └─ 目标非法？   → targeting
│
├─ 咒语怎么施放/支付？
│   ├─ 费用计算？   → costs
│   ├─ 掘穴？       → costs
│   ├─ 召集？       → convoke + costs
│   ├─ 返照？       → flashback + costs
│   └─ 延缓？       → suspend + costs
│
├─ 永久物特征？
│   ├─ 层系统？     → layer-system (fwk)
│   ├─ 复制品？     → copy-effects
│   ├─ 指示物？     → counters
│   └─ 区域变更？   → zone-changes
│
└─ 特殊机制？
    ├─ 倾曳/Cascade     → cascade
    ├─ 返照/Flashback   → flashback
    ├─ 延缓/Suspend     → suspend + costs
    ├─ 佩带/灵气        → equipment-auras
    └─ 鹏洛客           → planeswalkers
```

## 三、常见组合场景加载顺序

| 组合 | 顺序 |
|------|------|
| 死触 + 践踏 + 先攻 | `first-strike-double-strike` → `deathtouch` → `trample` → `combat-phase` |
| 保护 + 目标 | `protection` → `targeting` → `targeting-restrictions` |
| 侵染 + 系命 | `damage` → `lifelink` |
| 不灭 + 致命伤害 + 防御力≤0 | `state-based-actions` → `removal-and-survival` → `damage` |
| 复制 + 传奇 | `copy-effects` → `state-based-actions` |
| 灵气 + 辟邪 | `equipment-auras` → `targeting-restrictions` → `targeting` |
| 牺牲阻挡者 + 践踏 | `combat-phase` → `trample` → `damage` |
| 延缓 + X + 不支付 | `suspend` → `x-spell-mana-value` → `costs` |

## 四、使用说明

1. 扫描问题关键词，对照映射表确定候选决策树
2. 跨领域问题使用"常见组合场景"确定加载顺序
3. 无法确定时优先加载 `state-based-actions` 或 `targeting`
4. 加载决策树后按其"检索路径"顺序查阅规则
5. 框架（framework）用于深度推演，日常问题优先用决策树
