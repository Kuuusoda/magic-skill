---
created: 2026-04-22
updated: 2026-04-22
type: concept
tags: [万智牌, 指挥官, cEDH, 组合技]
sources: []
---

# cEDH 组合技模式

cEDH 的 Combo 设计遵循"**速度、冗余、隐蔽性**"三大原则。本文总结 cEDH 中最常见的制胜 Combo 模式，分析其组件、执行步骤、费用和脆弱点。

---

## 1. Breach Combo（冥界裂隙组合技）

### 核心组件

| 组件 | 作用 |
|------|------|
| **冥界裂隙 / Underworld Breach** | 关键咒语：你坟场中每张非地牌获得逃脱（Escape）。逃脱费用 = 该牌的法术力费用 + 额外放逐坟场中另外三张牌。结束步骤开始时牺牲此结界 |
| **狮眼钻石 / Lion's Eye Diamond** | 牺牲产 3 点任意颜色 Mana |
| **脑力冻结 / Brain Freeze** | 目标牌手磨 3 张牌；Storm（本回合中此前施放的咒语数量）每有 1 个，重复一次 |

### 执行步骤

1. 施放 **Underworld Breach**（费用 {1}{R}）
2. 施放 **Lion's Eye Diamond**（费用 {0}）
3. 对**自己**施放 **Brain Freeze**（费用 {1}{U}）— 磨自己 3 张牌
4. 牺牲 **LED**，产 3 点 Mana
5. 用 Breach 的异能，从坟场中**逃脱**（Escape）LED 和 Brain Freeze
   - 逃脱 LED：支付其法术力费用 {0} + 放逐坟场中另外 3 张牌
   - 逃脱 Brain Freeze：支付其法术力费用 {1}{U} + 放逐坟场中另外 3 张牌
6. 重复步骤 3–5，每次 Brain Freeze 的 Storm 计数增加，磨牌数量指数增长
7. 磨穿自己的整个牌库
8. 从坟场中**逃脱** **Thassa's Oracle**（或其他制胜组件）
9. Thassa's Oracle 的 ETB 触发：检视张数 X（X = 你对蓝的献忠）≥ 牌库剩余张数 → 你赢得游戏（牌库已磨空 = 0 张，X ≥ 0 恒成立）

### 费用

- 最低启动费用：**{2}{R}{U}**（Breach + Brain Freeze，LED 已在场上或费用已备）
- 实际费用通常：**{1}{R} + {1}{U} + 3 张手牌**（用于支付 LED 的牺牲）

### 优势
- **组件少**：仅需 3 张牌即可启动
- **费用低**：2 费 + 1 费即可启动
- **隐蔽性高**：Underworld Breach 本身不是威胁，直到 LED 进场
- **重建能力强**：Intuition 可以直接搜索 Breach + LED + Sevinne's Reclamation

### 脆弱点
- **需要 3 张手牌**：LED 牺牲需要弃掉手牌
- **坟场仇恨**：Rest in Peace、Leyline of the Void 直接封锁
- **Stack 互动**：对手可以在 Breach 结算后、Brain Freeze 施放前反击
- **检视条件**：Thassa's Oracle 制胜要求 X（对蓝献忠）≥ 牌库剩余张数，需先磨穿自身牌库（如配合 Demonic Consultation 放逐整个牌库），如果生命被压到 0 先死亡

### 代表套牌
- **Blue Farm**（主路线）
- **Rograkh/Silas**（主路线）
- **各种 Grixis/4 色 Combo**

---

## 2. Oracle Combo（塔萨的先知组合技）

### 核心组件

| 组件 | 作用 |
|------|------|
| **塔萨的先知 / Thassa's Oracle** | ETB：检视牌库顶 X 张牌（X 为你对蓝色的献忠），将其中至多一张置于牌库顶，其余以随机顺序置于牌库底。如果 X 大于或等于你牌库中的牌数，你赢得游戏 |
| **恶魔咨商 / Demonic Consultation** | 支付 {B}，说出一个牌名。放逐你牌库顶的六张牌，然后从牌库顶开始展示牌，直到展示出所说出名称的牌。将该牌置入手中，放逐以此法展示的所有其他牌。（若说出套牌中没有的牌名，则整个牌库被放逐） |
| **腐化协定 / Tainted Pact** | 支付 {1}{B}，放逐你牌库顶的牌。你可以将该牌置入手中，除非它与以此法放逐的另一张牌同名。重复此流程，直到你将一张牌置入手中，或放逐了两张同名的牌为止。（单卡构筑下可借此放逐整个牌库） |

### 执行步骤（Consultation 路线）

1. 施放 **Thassa's Oracle**（费用 {U}{U}）
2. Oracle 的 ETB 触发进入堆叠
3. 在 ETB 触发结算前，施放 **Demonic Consultation**（费用 {B}）
4. 说出一个**不在你套牌中**的牌名（如"Black Lotus"）
5. 先放逐牌库顶 6 张，再持续展示并放逐，因牌库中无该牌 → **整个牌库被放逐**
6. Consultation 结算后，ETB 触发结算：你牌库中的牌数为 0，X（献忠）≥ 0 → **赢得游戏**

### 执行步骤（Pact 路线）

1. 施放 **Thassa's Oracle**（费用 {U}{U}）
2. Oracle 的 ETB 触发进入堆叠
3. 施放 **Tainted Pact**（费用 {1}{B}）
4. 逐张放逐牌库顶牌，每张都选择**不**置入手中（指挥官单卡构筑下无同名牌，流程不会被"两张同名"中断）
5. 一路放逐到牌库为空 → **整个牌库被放逐**
6. ETB 触发结算：牌库为 0，X（献忠）≥ 0 → **赢得游戏**

### 费用
- Consultation 路线：**{U}{U} + {B}** = {U}{U}{B}
- Pact 路线：**{U}{U} + {1}{B}** = {1}{U}{U}{B}

### 优势
- **费用极低**：2–3 费即可启动
- **难以互动**：ETB 触发在 Oracle 进场时已进入堆叠，去除 Oracle 不会取消触发
- **仅需 2 张牌**：Oracle + Consultation/Pact

### 脆弱点
- **需要空牌库**：如果对手在你 Consultation 前塞了一张牌到你的牌库（如 Field of Ruin 的替代性效应），Consultation 不会放逐整个牌库
- **针对性去除**：Drannith Magistrate 阻止你从牌库外施放（但 Consultation 是从牌库中放逐，不受 Magistrate 影响）
- **Pact 的同名牌风险**：Tainted Pact 本身**不造成生命损失**；但若套牌中存在两张同名牌（如非单卡的基础地），放逐到第二张同名牌时流程会被迫中断，无法清空牌库（标准 cEDH 单卡构筑中基础地极少，通常不受影响）

### 代表套牌
- **几乎所有蓝黑/4 色 cEDH 套牌**（备用路线）
- **Blue Farm**（备用路线）

---

## 3. Ad Nauseam（致昏组合技）

### 核心单卡

**致昏 / Ad Nauseam**（费用 {3}{B}{B}）

> 展示你牌库顶的牌并将其置入手中。你失去等同于其总法术力值的生命。你可以将此流程重复任意次数。

### 执行步骤

1. 控制场上的 Mana 源总量 ≥ 5（用于支付 Ad Nauseam 的费用）
2. 施放 **Ad Nauseam**
3. 反复"抓牌"，直到抓空或生命降至 0
4. 将所有抓到的牌的**法术力费用**作为生命损失累加
5. 理想情况下，抓 15–25 张牌，生命降至 1–5
6. 用抓到的牌中的 Combo 组件直接完成制胜

### 关键配合

Ad Nauseam 的强度取决于套牌的**平均法术力曲线**：

| 套牌类型 | 平均 CMC | Ad Nauseam 典型抓牌数 |
|---------|---------|---------------------|
| Turbo | 1.5–1.8 | 20–30 张 |
| Midrange | 1.8–2.2 | 15–25 张 |
| Stax | 2.2+ | 10–15 张 |

**Turbo 套牌**（如 Blue Farm）的 Ad Nauseam 可以抓 20+ 张牌，几乎保证能找到 Combo 组件。

### 优势
- **单卡建立压倒性优势**：一张牌改变整个对局
- **隐蔽性**：Ad Nauseam 看起来只是"抓几张牌"，直到你发现它抓了 20 张

### 脆弱点
- **需要 5 费**：T1–T2 难以施放
- **生命损失**：如果生命已被压低（如对手有 Sulfuric Vortex），可能无法安全施放
- **Angel's Grace 依赖**：某些版本需要 Angel's Grace 防止生命降至 0 时输掉

### 代表套牌
- **Blue Farm**（核心单卡制胜路线）
- **各种黑系 Turbo 套牌**

---

## 4. Isochron Scepter + Dramatic Reversal（等时权杖组合技）

### 核心组件

| 组件 | 作用 |
|------|------|
| **等时权杖 / Isochron Scepter** | {2} 进场时，你可以从手牌中将一张总法术力费用 ≤ 2 的瞬间牌放逐并放置于权杖下。{2}、{T}：复制该瞬间，你可以施放该复制品 |
| **戏剧性逆转 / Dramatic Reversal** | {1}{U} 瞬间：重置所有由你操控的非地永久物 |

### 执行步骤

1. 施放 **Isochron Scepter**（费用 {2}）
2. 将 **Dramatic Reversal** 放置于权杖下（Imprint）
3. 激活权杖（{2} + {T}）→ 施放 Dramatic Reversal 的复制品
4. Dramatic Reversal 重置所有非地永久物（包括权杖本身和 Mana 石）
5. 重复步骤 3–4，每次产生净 Mana 收益
6. 产无限 Mana，然后用 Mana 导师搜索 Thassa's Oracle + Consultation 或其他制胜方式

### 优势
- **仅需 2 张牌**
- **费用低**：权杖 {2} + 激活 {2} = 初始 4 费

### 脆弱点
- **需要 Mana 石**：如果没有 2+ 个 Mana 产费永久物，净 Mana 收益为 0
- **Artifact 去除**：权杖被去除后整个 Combo 崩溃
- **Silence 效应**：如果无法施放复制的瞬间，Combo 停止

### 代表套牌
- **Kinnan**（备用路线）
- **各种蓝系 Combo 套牌**

---

## 5. Kinnan 专属：Basalt Monolith 无限法术力

### 核心组件

| 组件 | 作用 |
|------|------|
| **持券俊杰季宁 / Kinnan, Bonder Prodigy** | 每当你横置一个非地永久物产生法术力时，额外产生一点该永久物所产类型的法术力（翻倍效应）。{5}{G}{U}：检视牌库顶五张，可将一张非人类生物放进战场 |
| **玄武巨石 / Basalt Monolith** | {3} 进场未横置。{T}：加 {C}{C}{C}。{3}：重置玄武巨石 |

> 注：Kinnan + Basalt Monolith **两牌即可**产生无限法术力，不需要第三张牌。逸脱实界（Hullbreaker Horror）在 Kinnan 套牌中是**保护与互动组件**（每当你施放咒语，可将目标咒语或非地永久物移回拥有者手上），用于弹回威胁、保护自己的引擎，并非无限法术力 loop 的必需环节。

### 执行步骤

1. Kinnan 已在战场
2. 施放 **Basalt Monolith**（费用 {3}），进场未横置
3. 横置 Monolith 产 {C}{C}{C}（3 点无色）→ **Kinnan 触发，额外产生 1 点无色 → 共 {C}{C}{C}{C}（4 点）**
4. 花 {3} 重置 Monolith → 净赚 {1}
5. 重复步骤 3–4 → **无限无色法术力**

### 优势
- **两牌 combo**：Kinnan + Monolith 即可启动，组件极少
- **Kinnan 本身即为引擎**：不需要额外的 tutor 搜索 Kinnan
- **多条路线**：Monolith + Kinnan 只是其中一条，还有等时权杖路线

### 脆弱点
- **依赖 Kinnan**：如果 Kinnan 被去除，整个策略崩溃
- **Drannith Magistrate**：直接锁死指挥官施放

---

## Combo 对比总结

| Combo | 组件数 | 最低费用 | 隐蔽性 | 重建能力 | 代表套牌 |
|-------|--------|---------|--------|---------|---------|
| **Breach** | 3 | {2}{R}{U} | 高 | 极强（Intuition 直接组装） | Blue Farm, Rograkh/Silas |
| **Oracle** | 2 | {U}{U}{B} | 极高 | 中（需重新搜索 Oracle） | 几乎所有蓝黑套牌 |
| **Ad Nauseam** | 1 | {3}{B}{B} | 中 | 低（被反击后难以重建） | Blue Farm, Turbo |
| **Scepter/Reversal** | 2+ | {4}+ | 中 | 低（权杖被去除后崩溃） | Kinnan, 蓝系 Combo |
| **Kinnan/Monolith** | 3 | {3}{U}{G} | 高 | 中（依赖 Kinnan 存活） | Kinnan |

## Combo 选择的原则

### 1. 冗余优先
优秀的 cEDH 套牌至少有 **2 条独立 Combo 路线** + **1 张单卡制胜**。

Blue Farm 的冗余设计：
- 主路线：Breach Combo
- 备用路线：Oracle Combo
- 单卡制胜：Ad Nauseam、Necropotence
- Intuition 可以直接组装整个 Breach Combo

### 2. 费用梯度
Combo 的费用应该形成梯度，以便在不同 Mana 条件下都能尝试制胜：

| 费用 | Combo | 适用场景 |
|------|-------|---------|
| 1–2 费 | Oracle Combo | 低费窗口 |
| 2–3 费 | Breach Combo | 标准窗口 |
| 3–5 费 | Ad Nauseam | 中速窗口 |
| 5+ 费 | Scepter/Reversal | 慢速窗口 |

### 3. 隐蔽性
越隐蔽的 Combo 越难被对手预判和干扰：
- **高隐蔽**：Oracle Combo（看起来只是施放一个 2 费生物）
- **中隐蔽**：Breach Combo（Breach 本身不是威胁）
- **低隐蔽**：Ad Nauseam（施放时全场都知道你要做什么）

## 相关页面

- [[cedh|cEDH 概述]] — cEDH 核心竞技维度
- [[cedh-deck-archetypes|cEDH 套牌原型]] — Turbo / Stax / Midrange / Adaptive
- [[combo|组合技]] — 组合技通用理论
- [[combo-engine-cards|组合技引擎牌]] — cEDH 高频引擎牌详解
- [[stack|堆叠]] — 堆叠互动与时机
- [[infinite-mana-combos|无限法术力组合技]] — 无限 Mana 的经典案例
