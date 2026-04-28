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
| **冥界裂隙 / Underworld Breach** | 关键咒语：本回合内，你可以从坟场中施放牌，并支付「放逐等同于该牌法术力费用的牌」作为额外费用 |
| **狮眼钻石 / Lion's Eye Diamond** | 牺牲产 3 点任意颜色 Mana |
| **脑力冻结 / Brain Freeze** | 目标牌手磨 3 张牌；Storm（本回合中此前施放的咒语数量）每有 1 个，重复一次 |

### 执行步骤

1. 施放 **Underworld Breach**（费用 {1}{R}）
2. 施放 **Lion's Eye Diamond**（费用 {0}）
3. 对**自己**施放 **Brain Freeze**（费用 {1}{U}）— 磨自己 3 张牌
4. 牺牲 **LED**，产 3 点 Mana
5. 用 Breach 的异能，从坟场中**逃脱**（Escape）LED 和 Brain Freeze
   - 放逐 3 张牌（LED 的费用 {0}）
   - 放逐 3 张牌（Brain Freeze 的费用 {1}{U}）
6. 重复步骤 3–5，每次 Brain Freeze 的 Storm 计数增加，磨牌数量指数增长
7. 磨穿自己的整个牌库
8. 从坟场中**逃脱** **Thassa's Oracle**（或其他制胜组件）
9. Thassa's Oracle 的 ETB 触发：你牌库中的牌少于 5 张 → 你赢得游戏

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
- **生命限制**：Thassa's Oracle 需要牌库中少于 5 张牌，如果生命被压到 0 先死亡

### 代表套牌
- **Blue Farm**（主路线）
- **Rograkh/Silas**（主路线）
- **各种 Grixis/4 色 Combo**

---

## 2. Oracle Combo（塔萨的先知组合技）

### 核心组件

| 组件 | 作用 |
|------|------|
| **塔萨的先知 / Thassa's Oracle** | ETB：检视牌库顶 X 张牌（X 为你献忠的 Devotion），将其中任意数量放到底部，其余放顶部。如果以此法检视的牌数大于牌库中的牌数，你赢得游戏 |
| **恶魔咨商 / Demonic Consultation** | 支付 {B}，说出一个牌名。展示牌库顶牌，直到展示出该牌名的牌。放逐展示的所有牌。如果未展示出该牌名的牌，放逐整个牌库 |
| **腐化协定 / Tainted Pact** | 支付 {1}{B}，放逐牌库顶牌，直到放逐两张不同名的地。将所有以此法放逐的非地牌放入手中。如果以此法放逐了整个牌库，输掉 1/2 生命 |

### 执行步骤（Consultation 路线）

1. 施放 **Thassa's Oracle**（费用 {U}{U}）
2. Oracle 的 ETB 触发进入堆叠
3. 在 ETB 触发结算前，施放 **Demonic Consultation**（费用 {B}）
4. 说出一个**不在你套牌中**的牌名（如"Black Lotus"）
5. 展示整个牌库，未找到该牌 → **放逐整个牌库**
6. Consultation 结算后，ETB 触发结算：你牌库中的牌数为 0，小于 5 → **赢得游戏**

### 执行步骤（Pact 路线）

1. 施放 **Thassa's Oracle**（费用 {U}{U}）
2. Oracle 的 ETB 触发进入堆叠
3. 施放 **Tainted Pact**（费用 {1}{B}）
4. 持续放逐牌库顶牌，直到放逐两张不同名的地
5. 如果牌库中无地或地牌同名 → **放逐整个牌库**
6. ETB 触发结算：牌库为 0 → **赢得游戏**

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
- **Pact 的生命损失**：如果 Pact 放逐了整个牌库，失去 1/2 生命（通常为 20 → 10），在生命已被压低时可能致命

### 代表套牌
- **几乎所有蓝黑/4 色 cEDH 套牌**（备用路线）
- **Blue Farm**（备用路线）

---

## 3. Ad Nauseam（致昏组合技）

### 核心单卡

**致昏 / Ad Nauseam**（费用 {3}{B}{B}）

> 支付生命而不是支付你手牌中的牌之法术力费用来将它们放入战场。你失去等同于其总法术力值的生命。

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

## 5. Kinnan 专属：Basalt Monolith + 逸脱实界

### 核心组件

| 组件 | 作用 |
|------|------|
| **持券俊杰季宁 / Kinnan, Bonder Prodigy** | {T}：加 {U} 或 {G}，数量等同于本回合中由你操控的永久物的总法术力值 |
| **玄武巨石 / Basalt Monolith** | {3} 进场未横置。{T}：加 {3}。{3}：重置玄武巨石 |
| **逸脱实界 / Hullbreaker Horror** | 每当你施放瞬间或法术时，选择一项：横置目标永久物；或重置目标永久物 |

### 执行步骤

1. Kinnan 已在战场
2. 施放 **Basalt Monolith**（费用 {3}）
3. Monolith 产 {3}
4. Kinnan 的异能：加 {U} 或 {G}，数量 = 永久物总法术力值（至少 6：Kinnan {2} + Monolith {3} + 其他）
5. 用 {3} 重置 Monolith
6. 用 Kinnan 的 Mana 施放一个瞬间（如 Brainstorm）
7. **Hullbreaker Horror** 触发：重置 Monolith
8. 重复步骤 3–7，产生无限 Mana

### 优势
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
