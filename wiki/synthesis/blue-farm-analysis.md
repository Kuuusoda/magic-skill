---
created: 2026-04-22
updated: 2026-04-22
type: synthesis
tags: [万智牌, cEDH, BlueFarm, 套牌分析, Kraum, Tymna]
sources: [kraum-tymna-blue-farm_primers.md]
---

# Blue Farm（Kraum / Tymna）全面分析

> **分析框架**：本文采用[[cedh-data-analysis|cEDH 数据分析方法]]的 6 章标准结构，并额外引入**时间横向维度**（历史演进）与**Meta 纵向维度**（vs 各原型 Matchup），形成联合分析框架。

---

## 第 1 章：套牌基础信息

### 1.1 指挥官异能简述

Blue Farm 的指挥官是**伙伴（Partner）**组合：

| 指挥官 | 费用 | 颜色 | 关键异能 |
|--------|------|------|---------|
| **Kraum, Ludevic's Opus**（卢德维克的杰作卡鲁姆）| {3}{U}{R} | 蓝红 | 飞行、敏捷；每当任一对手在同一回合中施放第二个咒语时，抓一张牌 |
| **Tymna the Weaver**（织法者泰姆娜）| {1}{W}{B} | 白黑 | 系命；每个你的战后主阶段开始时，可支付 X 点生命（X 为本回合受到战斗伤害的对手数量），若如此做，抓 X 张牌 |

**指挥官价值分析**：

- **Tymna** 是套牌的「发动机核心」。在 4 人 Pod 中，只要每回合至少对 1 名对手造成战斗伤害，就能以 1 点生命换 1 张牌。配合飞行/系命生物（如 Faerie Mastermind），每回合稳定抓 2–3 张牌。
- **Kraum** 是「被动过牌引擎」+「5/4 飞行敏捷打手」。在多人环境中，对手每回合施放 2 个咒语极为常见，Kraum 平均每回合触发 1–2 次，相当于免费的「神秘遗迹（Rhystic Study）」（[[card-advantage|卡牌优势]]引擎）。
- **组合效应**：两个指挥官共同构成了 cEDH 中**最稳定的卡牌优势来源**。即使在互动交换后，只要指挥官在场，套牌就能快速补充手牌资源。

### 1.2 核心 Combo（主路线 + 备用路线）

Blue Farm 遵循「**冗余优先**」原则，拥有 2+ 条独立 Combo 路线 + 多张单卡制胜。

#### 主路线：Breach Combo（冥界裂隙组合技）

| 组件 | 作用 |
|------|------|
| **冥界裂隙 / Underworld Breach** | 关键结界：坟场中的非地牌获得逃脱（Escape），费用为其法术力费用 + 放逐坟场中另外 3 张牌 |
| **狮眼钻石 / Lion's Eye Diamond** | 牺牲产 3 点任意颜色法术力 |
| **脑力冻结 / Brain Freeze** | 目标牌手磨 3 张牌；风暴（Storm）每有 1 个，重复一次 |

**执行步骤**：
1. 施放 Underworld Breach（{1}{R}）
2. 施放 Lion's Eye Diamond（{0}）
3. 对自己施放 Brain Freeze（{1}{U}），磨 3 张牌
4. 牺牲 LED 产 3 点 Mana
5. 用 Breach 逃脱 LED 和 Brain Freeze，重复步骤 3–4
6. Storm 计数指数增长，磨穿自己牌库
7. 逃脱塔萨的先知赢得游戏

**最低启动费用**：{2}{R}{U}（如果 LED 已在坟场或手中，可降至仅 {1}{R} + {1}{U}）

**替代方案**：
- LED 替代：Lotus Petal、An Offer You Can't Refuse（可瞬间速度磨牌）
- Brain Freeze 替代：Wheel of Fortune、Windfall（更危险，但可配合 Smothering Tithe）

#### 备用路线 1：Oracle Combo（塔萨的先知组合技）

| 组件 | 作用 |
|------|------|
| **塔萨的先知 / Thassa's Oracle** | ETB：检视牌库顶 X 张牌；若检视牌数 > 牌库牌数，赢得游戏 |
| **恶魔咨商 / Demonic Consultation** | {B}：说出牌名，展示牌库顶直到找到该牌；未找到则放逐整个牌库 |
| **腐化协定 / Tainted Pact** | {1}{B}：放逐牌库顶直到放逐两张不同名地；若放逐整个牌库，失去 1/2 生命 |

**费用**：Consultation 路线 {U}{U}{B}；Pact 路线 {1}{U}{U}{B}

**警告**：执行 Oracle Combo 时，若场上有 Kraum、Esper Sentinel 或 Faerie Mastermind，对手可在 Consultation 后施放咒语迫使你从空牌库抓牌而输掉游戏。

#### 备用路线 2：Intuition 一卡组装

**Intuition**（{2}{U}）可以直接搜索 Underworld Breach + Lion's Eye Diamond + Sevinne's Reclamation，无论对手给你哪张，都能完成 Breach Combo。

#### 单卡制胜（One-Card Wincons）

| 单卡 | 费用 | 作用 |
|------|------|------|
| **致昏 / Ad Nauseam** | {3}{B}{B} | 支付生命「抓牌」直到抓空或生命归零；典型抓 15–25 张 |
| **死冥权能 / Necropotence** | {B}{B}{B} | 支付生命抓牌；配合 Borne Upon a Wind / Final Fortune / Valley Floodcaller 在结束步骤获胜 |
| **直觉 / Intuition** | {2}{U} | 直接组装整个 Breach Combo |
| **记忆背叛 / Mnemonic Betrayal** | {1}{U}{B} | 使用对手坟场中的牌；当自己的制胜组件被放逐时的终极备份 |

### 1.3 关键单卡分类

#### 快速 Mana（17+ 张）

| 类别 | 代表单卡 |
|------|---------|
| 0 费 Mana 石 | Chrome Mox, Lotus Petal, Mox Amber, Mox Diamond, Mox Opal |
| 1 费 Mana 石 | Mana Vault, Sol Ring |
| 法术力仪式 | Dark Ritual, Rite of Flame, Cabal Ritual, Simian Spirit Guide, Rain of Filth |
| Mana 引擎 | Ragavan, Lotho, Smothering Tithe, Birgi, Tataru Taru |

#### 导师（14+ 张，密度 ~14%）

| 类别 | 代表单卡 |
|------|---------|
| 入手导师 | Demonic Tutor, Diabolic Intent, Gamble, Wishclaw Talisman, Intuition |
| 牌库顶导师 | Enlightened Tutor, Imperial Seal, Vampiric Tutor, Mystical Tutor |
| 禁断导师 | Tainted Pact, Demonic Consultation |

#### 互动（18+ 张，密度 ~18%）

| 类别 | 代表单卡 |
|------|---------|
| 免费反击 | Force of Will, Force of Negation, Fierce Guardianship, Pact of Negation, Snapback, Mental Misstep |
| 有条件免费反击 | Mindbreak Trap, Flusterstorm |
| 付费反击 | An Offer You Can't Refuse, Swan Song, Red Elemental Blast |
| 目标重定向 | Deflecting Swat |
| 肃静效应 | Silence, Grand Abolisher, Ranger-Captain of Eos, Voice of Victory, Hexing Squelcher |
| 弹回/去除 | Chain of Vapor, Into the Flood Maw, Otawara, Teferi (已退), March of Swirling Mist (已退) |

#### 过牌引擎（6+ 张）

| 单卡 | 类型 |
|------|------|
| Rhystic Study | 结界 |
| Mystic Remora | 结界 |
| Esper Sentinel | 生物 |
| The One Ring | 神器（已退） |
| Birgi, God of Storytelling | 生物 |
| Jeska's Will | 法术 |

### 1.4 构筑逻辑

Blue Farm 的构筑逻辑可以概括为：**「用指挥官解决资源问题，用套牌解决制胜问题」**。

- **颜色优势**：四色（WUBR）提供了 cEDH 中最广的牌池选择，几乎所有最强单卡都在可用范围内
- **Combo 冗余**：2 条主路线（Breach / Oracle）+ Intuition 组装 + 4 张单卡制胜
- **导师密度**：~14%，确保快速找到所需组件
- **互动密度**：~18%，足以在互动交换后重建
- **快速 Mana 密度**：极高，支持 T1–T2 展开

---

## 第 2 章：环境适配性表现（纵向维度）

### 2.1 当前 cEDH 环境层级

基于 edhtop16 和 Topdeck.gg 数据，当前环境（2025 年末–2026 年初）的 Tier 分布大致为：

| Tier | 代表套牌 | 原型 |
|------|---------|------|
| **S Tier** | **Blue Farm** | Adaptive |
| S Tier | Rograkh/Silas | Turbo |
| A+ Tier | Kinnan | Turbo/Adaptive |
| A Tier | Nadu | Adaptive |
| A Tier | Tivit | Adaptive |
| A- Tier | Various Stax | Stax |
| B+ Tier | Yuriko, Najeela | Turbo/Midrange |

### 2.2 Matchup 分析（vs 各主流套牌）

#### vs Turbo（Rograkh/Silas、Kinnan）

**优劣势**：轻微劣势到均衡

- **劣势原因**：Rograkh/Silas 可以在 T1–T2 完成 Combo，Blue Farm 作为非纯 Turbo 套牌，在竞速中略慢
- **优势因素**：Blue Farm 的互动密度（18+ 张）高于纯 Turbo，且拥有 Mindbreak Trap（对 Rograkh 关键）和 Force of Will
- **策略**：保留免费反击用于关键窗口；如果 1 号位是 Turbo，优先保留互动而非展开
- **Post-ban 变化**：Mana Crypt 和 Jeweled Lotus 被禁后，Turbo 整体变慢 0.5–1 回合，Blue Farm 的劣势缩小

#### vs Stax（Derevi、Winota、Tymna/Kamahl）

**优劣势**：优势

- **优势原因**：Blue Farm 拥有 9+ 张弹回/去除（Chain of Vapor、Into the Flood Maw、Otawara 等），可以处理 Stax 组件后继续 Combo
- **引擎韧性**：即使被 Stax 拖慢，Tymna + Kraum 的被动过牌可以在限制环境中逐步积累优势
- **关键单卡**：Teferi, Time Raveler（可弹回 Stax + 肃静）在 2025 年 4 月被 Voice of Victory 替代，但弹回能力仍然充足
- **策略**：不要急于 Combo，先去除 Stax 组件或等待保护手段（Silence、Grand Abolisher）

#### vs Midrange（其他 Blue Farm、Thrasios/X）

**优劣势**：优势

- **优势原因**：Blue Farm 的卡牌优势引擎效率高于几乎所有其他 Midrange 套牌。Tymna + Kraum + Rhystic Study/Mystic Remora 的组合在资源战中几乎不可战胜
- **导师密度**：Blue Farm 的导师密度和 Combo 冗余度使其能在资源战中更快找到制胜路线
- **策略**：优先建立引擎（Rhystic Study > 快速 Combo），利用资源优势在互动交换中压倒对手

#### vs Adaptive（Nadu、Tivit）

**优劣势**：均衡

- **对局特征**：双方都有 Turbo 和 Midrange 两种模式，对局质量高度依赖起手和回合顺序
- **关键决策**：识别对手模式的速度。如果 Nadu 选择 Turbo 模式，Blue Farm 需要保留互动；如果 Nadu 选择 Midrange 模式，Blue Farm 需要比拼引擎效率
- **信息博弈**：Blue Farm 的信息暴露（施放 Ad Nauseam 时全场都知道你要做什么）可能被 Adaptive 对手利用

### 2.3 环境痛点应对

| 环境痛点 | Blue Farm 的应对 |
|---------|----------------|
| **先手优势** | 4 号位表现良好（信息最多），但 1 号位 Turbo 冲时仍需保留互动 |
| **Combo 速度** | T2–T3 可完成 Breach Combo，T1 可 Ad Nauseam，速度处于上游 |
| **互动密度** | 18+ 张互动，免费反击 6+ 张，足以参与互动交换 |
| **Stax 压制** | 9+ 张弹回/去除，处理后继续 Combo；Tymna/Kraum 在限制环境中仍可过牌 |

---

## 第 3 章：实战表现细节

### 3.1 胜率数据

**Tremnek 的 Tournament Results（2021–2026）**：

- **Winner**：Spanish cEDH Championship 2024、European cEDH Championship 2024、cEDH Hamelin Games 2025、JupiQualifier Munich 2025、Spanish 2025 Circuit Finals 2026 等
- **Semifinals/Finals**：大量国际赛事进入半决赛或决赛

**Good Soup 的数据统计（FreedomWaffle，截至 2024 年 1 月）**：

| 场景 | 对局数 | 胜场 | 胜率 |
|------|--------|------|------|
| 锦标赛 | 29 | 14 | **48.28%** |
| 全部对局 | 359 | 223 | **62.12%** |

**分析**：
- 锦标赛胜率 48.28% 在 cEDH 4 人 Pod 中极为优秀（理论平均 25%）
- 全部对局胜率 62.12% 反映出在练习/非锦标赛环境中的统治力
-  tournament 胜率低于全部对局胜率，说明在高压竞技环境中对手更强、互动更密集

### 3.2 关键节点表现

#### 制胜回合

| 路线 | 最快回合 | 典型回合 |
|------|---------|---------|
| Breach Combo | T2 | T3–T4 |
| Oracle Combo | T2 | T3–T5 |
| Ad Nauseam | T2 | T3–T4 |
| Necropotence | T3 | T4–T5 |

#### Combo 成功率

- **Breach Combo**：成功率极高，主要失败原因为坟场仇恨（Rest in Peace、Leyline of the Void）或 Stack 互动（对手在 Breach 结算后反击 Brain Freeze）
- **Oracle Combo**：成功率中高，主要风险为对手在 ETB 触发前塞牌（Field of Ruin）或强制抓牌（Kraum 触发）
- **Intuition 路线**：成功率极高，Sevinne's Reclamation 提供冗余，即使被干扰也可重试

#### 导师上手率

Blue Farm 拥有 ~14% 的导师密度（14 张导师 / 98 张非地牌），在 T3 前上手至少 1 张导师的概率约为 **65–70%**。

#### 重建成功率

- **Breach 被干扰后**：Sevinne's Reclamation 可直接从坟场回收 Breach，重建成功率 > 80%
- **Ad Nauseam 被反击后**：依赖指挥官过牌和引擎重建，成功率 ~60%
- **指挥官被去除后**：Tymna 和 Kraum 均可被重新施放（Tymna {1}{W}{B}，Kraum {3}{U}{R}），指挥官税影响较小

### 3.3 常见问题与失误

#### 构筑层面的常见误区

1. **过度关注 Ad Nauseam**：Ad Nauseam 只是 98 张牌中的 1 张，不应成为唯一目标。Centerpiece 是 Underworld Breach
2. **忽略生命管理**：Ad Nauseam 和 Necropotence 之外，生命完全不重要。不应因生命低而做出次优决策
3. **过早使用导师**：除非能立即获胜，否则早期导师应优先搜索优势组件（Sol Ring、Rhystic Study）而非 Combo 组件
4. **低估 Necropotence 的结束步骤优势**：Necropotence 在清理步骤创造优先权，可以让「直到回合结束」的效应（如 Silence）先结束，然后在清理步骤获胜

#### 操作层面的常见失误

1. **Oracle Combo 时忘记 Kraum/Esper Sentinel 触发**：执行 Oracle + Consultation 时，若场上有 Kraum，对手可能施放咒语迫使你从空牌库抓牌
2. **Breach Combo 时牌库/坟场资源计算错误**：逃脱需要放逐 3 张牌，确保有足够的坟场资源完成循环
3. **An Offer You Can't Refuse 的防御性使用**：不仅可用于反击对手的咒语，还可用于在 Breach Combo 中反击自己的 Brain Freeze 以产生 Treasure
4. **Teferi, Time Raveler 的时机**：应在准备获胜的同一回合施放，而非提前暴露

---

## 第 4 章：时间维度分析（横向维度）

### 4.1 历史演进时间线

Blue Farm 从 2021 年至今经历了多次重大调整，反映了 cEDH 元游戏的整体变迁。

#### 第一阶段：Dockside 时代（2021–2024 年 9 月）

**核心特征**：Dockside Extortionist 合法，Treasure 主题主导

- **关键单卡**：Dockside Extortionist、Phantasmal Image、Flesh Duplicate、Delney, Streetwise Lookout
- **核心 Combo**：Delney + Dockside + Orcish Bowmasters + Sidisi's Faithful = 无限伤害 + 无限 Treasure
- **策略重心**：快速展开 → Dockside 爆发 → 用克隆和弹回滥用 Treasure → Combo
- **Meta 环境**：Turbo 密度高，Dockside 套牌泛滥

**代表版本（Tremnek, 2024 年 2 月）**：
- 包含 Dockside Extortionist、Delney、Phantasmal Image、Flesh Duplicate
- 克隆密度高，可以多次触发 Dockside
- 有专门的无限 Combo（Delney + Dockside + Bowmasters + Sidisi's Faithful）

#### 第二阶段：禁牌冲击与适应（2024 年 9–10 月）

**禁牌**：Mana Crypt、Jeweled Lotus、Dockside Extortionist

**影响分析**：

| 维度 | 禁牌前 | 禁牌后 | 变化 |
|------|--------|--------|------|
| T1 快速 Mana | Mana Crypt + Jeweled Lotus + Sol Ring + Mox Diamond | Sol Ring + Mox Diamond + Chrome Mox + Lotus Petal + Mox Amber | T1 展开成功率下降 ~15% |
| Dockside 爆发 | Phantasmal Image / Flesh Duplicate / Delney 克隆 Dockside | 无 Dockside，克隆组件价值归零 | 中速资源转换能力大幅下降 |
| Meta 速度 | T1–T2 Turbo 常见 | T2–T3 Turbo，更多 Midrange | 整体变慢 0.5–1 回合 |
| Blue Farm 策略 | Turbo 为主，Dockside 为辅 | Breach 为核心，Midrange 为 backup | 更依赖指挥官过牌 |

**Post-ban 构筑调整（2024 年 9–10 月）**：

- **OUT**：Mana Crypt, Jeweled Lotus, Dockside Extortionist, Phantasmal Image, Flesh Duplicate, Alchemist's Retrieval, Delney
- **IN**：Mindbreak Trap, Into the Flood Maw, Lotho, Professional Face-Breaker, Demonic Consultation, Rain of Filth, Cavern of Souls

**调整逻辑**：
1. **Mindbreak Trap**：Meta 中 Rograkh/Silas 崛起，需要更多免费互动
2. **Rain of Filth**：Dockside 被禁后，需要新的「将资源优势转化为胜势」的工具
3. **Lotho + Professional Face-Breaker**：Treasure 在慢速 Meta 中可长期保存，价值提升
4. **Cavern of Souls**：增加第 27 张地，弥补早期 Mana 密度下降；可防反地施放关键人类

#### 第三阶段：Midrange 主导时代（2024 年末–2025 年中）

**核心特征**：Meta 整体变慢，Draw Engine（Rhystic Study、Mystic Remora）主导

**关键调整**：
- **2025 年 1 月**：Smothering Tithe 加入（对手抓牌时产生 Treasure）
- **2025 年 4 月**：Voice of Victory 加入，Teferi, Time Raveler 退出（Stax 减少，Teferi 的弹回价值下降）
- **2025 年 6 月**：The One Ring 退出（与指挥官竞争 Mana，后期效果差）；Faerie Mastermind 回归（支持 Tymna 游戏计划）

**Meta 观察**：
- Turbo 减少，Midrange 增加
- Orcish Bowmasters 密度下降（Tremnek 在 2025 年 8 月将其移除）
- 互动从「防早期 Turbo」转向「在资源战中保护 Combo」

#### 第四阶段：Proactive 回归（2025 年末–2026 年初）

**核心特征**：再次强调主动性，减少纯反应性单卡

**关键调整**：
- **2025 年 8 月**：Last Chance + Mox Amber 加入；Mindbreak Trap + Orcish Bowmasters 退出
  - **Last Chance**：第二张额外回合咒语（与 Final Fortune 配合），在 Midrange Meta 中确保「你能进入下一回合」
  - **Mox Amber**：Tataru Taru 提供传奇生物密度支持，0 费 Mana 石提升展开速度
  - **Mindbreak Trap 退出**：在 Midrange Meta 中无法保护 Combo，纯反应性
- **2025 年 11 月**：Rograkh, Son of Rohgahh + Wan Shi Tong 加入；地牌从 27 减至 25
  - **Rograkh**：0 费传奇生物，启用 Culling the Weak、Mox Amber、Diabolic Intent、Flare of Duplication
  - **Wan Shi Tong**：Midrange 价值生物，有闪光、警戒、飞行，完美 Tymna 打手
  - **25 张地**：因 Rograkh 是免费咒语 + Wan Shi Tong 过牌，地牌密度可降低
- **2026 年 1 月**：Hexing Squelcher 加入；Wan Shi Tong 退出
  - **Hexing Squelcher**：新保护工具，可生成红色 Mana 施放，阻止对手互动

### 4.2 核心单卡的生命周期

| 单卡 | 加入时间 | 退出时间 | 生命周期 | 退出原因 |
|------|---------|---------|---------|---------|
| Dockside Extortionist | 始终 | 2024.09 | ~3 年 | 被禁 |
| Delney | 2024.02 | 2024.09 | 7 个月 | 依赖 Dockside |
| Teferi, Time Raveler | 长期 | 2025.04 | ~2 年 | Stax 减少，Voice of Victory 替代 |
| The One Ring | 2023.09 | 2025.06 | 21 个月 | 与指挥官竞争 Mana，后期无力 |
| Mindbreak Trap | 2024.09 | 2025.08 | 11 个月 | Turbo 减少，纯反应性 |
| Orcish Bowmasters | 2023.06 | 2025.08 | ~2 年 | 创造 Bowmasters 子游戏，反噬自身 |
| Rain of Filth | 多次进出 | 当前 | — | 最佳中后期黑色仪式，但早期无力 |
| Faerie Mastermind | 多次进出 | 当前 | — | 灵活的闪光/飞行/过牌生物 |

### 4.3 演进趋势总结

Blue Farm 的演进反映了 cEDH Meta 的三个宏观趋势：

1. **从 Dockside 爆发到 Breach 核心**：Dockside 被禁后，套牌从「Treasure 爆发 → 克隆滥用」转向「Breach Combo + 指挥官过牌」
2. **从反应性到主动性**：Mindbreak Trap、Orcish Bowmasters 等纯反应性单卡逐步被 Last Chance、Mox Amber、Rograkh 等主动性单卡替代
3. **指挥官价值提升**：The One Ring 等独立引擎被移除后，Tymna 和 Kraum 的出场率提升，套牌更依赖指挥官的被动价值

---

## 第 5 章：结论与优化建议

### 5.1 核心表现结论

**强烈推荐** — Blue Farm 是当前 cEDH 环境中**最全面、最稳定、最难针对**的套牌之一。

**核心优势**：
1. **Adaptive 灵活性**：可根据起手在 Turbo 和 Midrange 之间无缝切换
2. **无与伦比的卡牌优势**：Tymna + Kraum + 6+ 张引擎 = 每回合抓牌量远超对手
3. **Combo 冗余**：2 条主路线 + Intuition 组装 + 4 张单卡制胜，干扰后重建能力强
4. **Matchup 覆盖面广**：无明显劣对局，对 Stax 和 Midrange 优势，对 Turbo 均衡

**核心劣势**：
1. **生命压力**：Ad Nauseam + Necropotence + Tymna 的支付生命 = 生命总处于低位
2. **被聚焦**：因知名度高，对手会优先保留互动针对 Blue Farm
3. **操作难度极高**：需要在「冲 Combo」和「建立优势」之间做精确判断，决策点极多

### 5.2 构筑优化建议

#### 当前最优版本特征（2026 年 1 月）

- **地牌**：25 张（低地数量依赖 Rograkh 和大量过牌）
- **快速 Mana**：~18 张（含 Mox Amber、Rograkh 启用工具）
- **互动**：~17 张（含 2 张额外回合咒语作为「主动性互动」）
- **引擎**：指挥官 + Rhystic Study + Mystic Remora + Esper Sentinel + Birgi

#### 可调 flex slots

| 当前卡 | 替代选项 | 适用场景 |
|--------|---------|---------|
| Wan Shi Tong → Hexing Squelcher | 已替换 | 当前最优 |
| Mox Amber | Talisman of Dominance | 若传奇生物密度不足 |
| The One Ring | — | 极慢 Meta 中可考虑回归 |
| Toxic Deluge | — | Stax Meta 回归时加入 |
| Drannith Magistrate | — | Commander -centric Meta 时加入 |

### 5.3 对局策略优化

#### 不同 Matchup 的核心策略

| 对手类型 | 核心策略 | 保留手牌优先级 |
|---------|---------|--------------|
| **Turbo** | 保留互动 > 展开；等他们尝试 Combo 时反击 | Force of Will, Fierce Guardianship, Mental Misstep, Mindbreak Trap |
| **Stax** | 优先建立引擎 > 急于 Combo；用弹回处理 Stax 组件 | Chain of Vapor, Into the Flood Maw, Otawara |
| **Midrange** | 优先建立引擎；在资源战中利用过牌优势 | Rhystic Study, Mystic Remora, Esper Sentinel |
| **Adaptive** | 识别对手模式；若对手 Turbo，保留互动；若 Midrange，比拼引擎 | 根据对手指挥官判断 |

#### 不同 Pod 位置的策略

| 位置 | 策略要点 |
|------|---------|
| **1 号位** | 可 T1–T2 冲 Combo 时直接冲；否则优先建立引擎（Rhystic Study） |
| **2–3 号位** | 观察 1 号位动作；若 1 号位是 Turbo，保留互动；若展开缓慢，抢占主动 |
| **4 号位** | 信息最多；优先保证生存（保留互动 > 展开）；利用信息优势预判威胁 |

#### 起手保留（Mulligan）原则

**必留**：
- T1 可施放的引擎（Rhystic Study、Mystic Remora、Esper Sentinel）
- T1–T2 可尝试的制胜路线（Ad Nauseam + 5+ Mana、Breach Combo 组件 + 保护）
- T1 可施放的指挥官（Tymna 或 Kraum）+ 后续 Mana

**必弃**：
- 无早期动作的手牌（T3 才能施放第一个有意义咒语）
- 纯互动无展开的手牌（你会阻止对手但无法获胜）
- 过于依赖后期单卡的手牌（Mnemonic Betrayal 无早期支持）

**位置依赖**：
- 1 号位：优先保留快速展开手牌
- 4 号位：可保留较慢但有互动的手牌

---

## 第 6 章：附录

### 6.1 关键单卡中英对照表

| 英文 | 中文 | 类型 |
|------|------|------|
| Kraum, Ludevic's Opus | 卢德维克的杰作卡鲁姆 | 指挥官 |
| Tymna the Weaver | 织法者泰姆娜 | 指挥官 |
| Underworld Breach | 冥界裂隙 | 结界 |
| Lion's Eye Diamond | 狮眼钻石 | 神器 |
| Brain Freeze | 脑力冻结 | 瞬间 |
| Thassa's Oracle | 塔萨的先知 | 生物 |
| Demonic Consultation | 恶魔咨商 | 瞬间 |
| Tainted Pact | 腐化协定 | 瞬间 |
| Ad Nauseam | 致昏 | 瞬间 |
| Necropotence | 死冥权能 | 结界 |
| Intuition | 直觉 | 瞬间 |
| Sevinne's Reclamation | 塞维尼的收复 | 法术 |
| Force of Will | 意志之力 | 瞬间 |
| Fierce Guardianship | 凶猛护幼 | 瞬间 |
| Rhystic Study | 神秘遗迹 | 结界 |
| Mystic Remora | 神秘鲼鱼 | 结界 |
| Esper Sentinel | 艾斯波哨兵 | 生物 |
| Birgi, God of Storytelling | 故事之神比尔基 | 生物/神器 |
| Silence | 肃静 | 法术 |
| Grand Abolisher | 大废除者 | 生物 |
| Ranger-Captain of Eos | 游侠队长伊奥斯 | 生物 |
| Flare of Duplication | 复制耀焰 | 瞬间 |
| Rograkh, Son of Rohgahh | 罗哈之子罗格拉赫 | 生物 |

### 6.2 数据来源

- **Primer 来源**：Tremnek（Moxfield, 862 赞）、FreedomWaffle（Moxfield, 276 赞）、Kazu（Moxfield, 470 赞）
- **赛事数据**：Topdeck.gg、cEDH PT、Ka0s Tournament Series、Mythic Lotus Series、European cEDH Championship
- **分析日期**：2026-04-22

### 6.3 术语注释

- **Breach Combo**：Underworld Breach + Lion's Eye Diamond + Brain Freeze 的制胜组合
- **Oracle Combo**：Thassa's Oracle + Demonic Consultation/Tainted Pact 的制胜组合
- **One-Card Wincon**：单张牌即可组装制胜路线的单卡（Ad Nauseam、Necropotence、Intuition、Mnemonic Betrayal）
- **Turbo / Midrange 切换**：Adaptive 套牌根据起手和对手类型在快速 Combo 和资源战之间切换策略
- **Post-ban / Pre-ban**：2024 年 9 月禁牌表调整前后（禁牌：Mana Crypt、Jeweled Lotus、Dockside Extortionist）

---

## 相关页面

- [[cedh|cEDH 概述]] — cEDH 核心竞技维度
- [[cedh-deck-archetypes|cEDH 套牌原型]] — Turbo / Stax / Midrange / Adaptive
- [[cedh-combo-patterns|cEDH 组合技模式]] — Breach / Oracle / Ad Nauseam 等制胜路线
- [[cedh-pod-dynamics|cEDH Pod 动态]] — 4 人位置策略与政治博弈
- [[cedh-data-analysis|cEDH 数据分析方法]] — 数据驱动的评估框架
- [[combo|组合技]] — 组合技通用理论
- [[combo-engine-cards|组合技引擎牌]] — cEDH 高频引擎牌
- [[counterspell|反击咒语]] — 堆叠互动体系
- [[commander|指挥官]] — 指挥官赛制通用规则
- [[partner|伙伴]] — 两张传奇生物共同作为指挥官
