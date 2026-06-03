---
created: 2026-05-03
updated: 2026-05-03
type: concept
tags: [万智牌, 策略, 套牌构组, 法术力基础, 摩登, 配地]
sources: []
---

# 法术力基础策略（Mana Base Strategy）

## 定义

法术力基础（Mana Base）指一套构筑套牌中所有产出法术力的牌——主要是地牌，也包括法术力神器、法术力生物等加速。**配地策略**是将地的总数、色源分布、特殊功能、生命减损做权衡的过程。

法术力曲线（mana curve）回答"我有多少咒语在哪些费用段"，法术力基础回答"我能不能按时把它们打出来"。两者必须配套设计，是 60 张构筑赛中最容易被低估、却最直接决定胜率的环节。

## 一、地的总数（Land Count）

### 1.1 经验数值

| 套牌速度 | 地数（含 MDFC 反面/Suspend 类有效地）| 备注 |
|----------|------|------|
| 极致快攻 | 18-20 | Burn、Hammer Time |
| 标准快攻 | 20-22 | Boros Energy、Domain Aggro |
| 中速 | 22-24 | Jeskai Blink、Esper Reanimator |
| 中速控制 | 24-26 | Azorius Control、UW Control |
| 重控 | 26-28 | Esper Control、Lantern |
| Tron / 大法术力 | 22-26（含 Tron 12 张特殊地）| Eldrazi Tron |
| Combo（依赖加速）| 18-22（含加速神器）| Amulet Titan、Ruby Storm |
| Combo（无地）| 0 真地 + 24-30 MDFC | Tameshi Belcher |
| Ramp/Loam | 24-28（含 Mishra's Foundry / 循环地）| Living End、Loam |

### 1.2 地数加减法则

**减地的合法理由**：
- 主牌含大量 cantrip（Preordain、Mishra's Bauble、Consider）每张视作 0.3-0.5 张地
- 主牌含 mana fixer 神器（Talisman、Mox Opal、Springleaf Drum）每张视作 0.5-0.8 张地
- MDFC 正反两面均有用（Sea Gate Restoration 是正面 8 费法术 + 反面海岛），按地的 0.6-0.8 张算
- 套牌曲线极低（平均 cmc < 2.0），3 地后多余的地变成卡牌劣势

**加地的合法理由**：
- 有大量"必须按时打出"的关键回合（如 T4 Cryptic Command）
- 需要双色或三色咒语在 T2-T3 落实（比如 {U}{U} on T2）
- 套牌内有终结地（Hall of Storm Giants / Mishra's Foundry / Faerie Conclave）
- 主牌依赖大量 X 法术（Walking Ballista、Hangarback Walker）

### 1.3 起手地数概率（参考表）

60 张套牌、不调度（mulligan）情况下，起手 7 张含特定地数的概率：

| 地数 | 起手 0 地概率 | 起手 1-2 地概率 | 起手 3+ 地概率 |
|------|------|------|------|
| 18 | 5.5% | 32.5% | 62% |
| 20 | 4.0% | 28% | 68% |
| 22 | 2.7% | 24% | 73% |
| 24 | 1.8% | 20% | 78% |
| 26 | 1.2% | 17% | 82% |

> **决策点**：3+ 起手地概率到 70% 一般是组牌底线，60-70% 必须配合大量 mana fixer 或 cantrip 才能跑得动。

## 二、颜色源（Color Sources）— Karsten 公式

### 2.1 Frank Karsten 90% 标准

Frank Karsten 通过模拟得出的"90% 概率按时打出特定颜色咒语"所需色源数（60 张套牌）：

#### 单色咒语

| 咒语费用 | 关键回合 | 90% 概率所需色源 |
|---------|---------|-----------------|
| {C} (1 费) | T1 | **14** 张色源 |
| {1}{C} (2 费) | T2 | **13** 张色源 |
| {2}{C} (3 费) | T3 | **12** 张色源 |
| {3}{C} (4 费) | T4 | **11** 张色源 |
| {4}{C} (5 费) | T5 | **10** 张色源 |

#### 双色咒语（同一颜色）

| 咒语费用 | 关键回合 | 90% 概率所需色源 |
|---------|---------|-----------------|
| {C}{C} (2 费) | T2 | **20** 张色源 |
| {1}{C}{C} (3 费) | T3 | **18** 张色源 |
| {2}{C}{C} (4 费) | T4 | **16** 张色源 |
| {3}{C}{C} (5 费) | T5 | **15** 张色源 |

#### 三色咒语（同一颜色）

| 咒语费用 | 关键回合 | 90% 概率所需色源 |
|---------|---------|-----------------|
| {C}{C}{C} (3 费) | T3 | **23** 张色源 |
| {1}{C}{C}{C} (4 费) | T4 | **20** 张色源 |
| {2}{C}{C}{C} (5 费) | T5 | **18** 张色源 |

#### 多色咒语（{U}{B}、{R}{W} 等）

T2 双色咒语（如 {U}{B} 的 Counterspell 加 Drown in the Loch）：
- 蓝色源 ≥ 13，黑色源 ≥ 13，**总地 ≥ 22**

T3 三色咒语（如 Bant Charm {G}{W}{U}）：
- 三色每色 ≥ 14，**总地 ≥ 24** + 至少 6 张取色地

### 2.2 色源计算细则

**全色源**（产任意当前需求颜色）：基本地、Shock lands、Surveil lands、对应 Triomes、对应取色地（搜出后才算）。

**取色地（Fetch lands）的色源贡献**：
- 1 张 Flooded Strand（搜 island/plains 类型地）= 同时是 1 蓝源 + 1 白源（**不是 2 张**）
- 计算时按它能搜的色合计 1 张
- 例：4 Flooded Strand 在套牌内含 Hallowed Fountain 时 = 4 蓝源 + 4 白源

**MDFC 正面是法术、反面是地**：
- Sea Gate Restoration 进战场必横置，反面是海岛
- 计入色源时按 0.5-0.7 张算（看是否需要 ETB 横置）
- 在牌库中按法术处理（CR 712.8a）

**Talisman / Signet 类双色神器**：
- 算 0.7-1 张色源（需要 T2 才能产，T1 不能用）
- 损失 1 回合速度

**Mox / Lotus Bloom**：
- 加速但不算稳定色源（Lotus Bloom 因 suspend 3 延迟）

### 2.3 颜色源最低门槛实操

> **铁则**：T1 关键牌色 14 源、T2 双色 20 源、T3 三色 23 源。任何低于此门槛的设计必须有补偿（cantrip / Talisman / mana fixer / 套牌可以"等"）。

## 三、地的种类与功能

### 3.1 取色地（Fetch Lands）

经典：Flooded Strand、Polluted Delta、Bloodstained Mire、Wooded Foothills、Windswept Heath（10 张），加 Misty Rainforest、Scalding Tarn、Verdant Catacombs、Marsh Flats、Arid Mesa（5 张）。

**作用**：
- 把"1 张地"变成"2 张地的颜色选择"（搜哪个 shock 决定颜色）
- 帮助 fetchable 双色地稳定上线
- 次级作用：洗牌（影响 Brainstorm 类）、削墓地配合 Snapcaster 类

**成本**：每张 1 生命（自行选择不为 0 生命的 fetch 极少见）

**摩登常见配置**：4-8 张取色，按 fetchable 双色地颜色对应分配

### 3.2 Shock lands（双色入场支付 2 生命）

经典 10 张：Hallowed Fountain (UW)、Watery Grave (UB) 等。

**作用**：被取色地搜出，提供两种基本地类型（"island plains"），可被 Path to Exile 等"找基本地"功能附带使用。

**成本**：进战场时支付 2 生命（或 2 生命换不横置）

### 3.3 Surveil lands（Murders at Karlov Manor）

经典 10 张：Meticulous Archive (UW)、Underground Mortuary (UB) 等。

**作用**：双色 + 进战场监视 1（看顶 1 张选放墓地或留库）。**进战场必横置**，T2 出会卡 1 回合。

**摩登优势**：被 fetch land 搜不到（只是基本类型），但适合 T1 调度局或墓地策略（Murktide、Esper Reanimator）

### 3.4 Triomes（Capenna 三色循环地）

10 张：Spara's Headquarters (GWU)、Raffine's Tower (UWB) 等。

**作用**：3 个基本地类型 → 同时被 island/plains/swamp 三类 fetch 搜到；提供循环 {3} 弃地抓 1。

**摩登优势**：3 色或 5 色套牌（Domain Aggro、Bant 类）核心

**成本**：进战场必横置

### 3.5 Pain lands（Sulfurous Springs 等）

老牌 10 张：Adarkar Wastes、Underground River 等。

**作用**：T1-T2 出双色不损节奏（无入场横置），但起动产色 mana 时支付 1 生命

**适合**：低曲线的快攻或中速，不在乎少量生命减损

### 3.6 Fast lands（Scars of Mirrodin / Kaladesh）

经典 10 张：Seachrome Coast (UW)、Botanical Sanctum (GU) 等。

**作用**：前 3 回合不横置（"只要你战场上 ≤ 2 张地"），T4 之后需横置入场。

**适合**：T1-T3 想稳定双色的快攻、Tempo 套牌

### 3.7 Check lands（Innistrad 原版）

10 张：Sunpetal Grove (GW)、Dragonskull Summit (BR) 等。

**作用**：如果你战场上有任意基本地类型对应的地，则不横置入场。

**摩登劣势**：T1 必横置入场，节奏差；少用

### 3.8 Filter lands（Lorwyn / Shadowmoor）

10 张：Mystic Gate (UW)、Rugged Prairie (RW) 等。

**作用**：横置 + 牺牲 {1} 转换两个特定颜色（{U/W} → {U}{U} 或 {W}{W} 或 {U}{W}）

**适合**：需要双色压缩的高密度套牌（Ad Nauseam、Scapeshift）

### 3.9 特殊功能地（Utility Lands）

不可缺少的"非传统功能"地：

| 类型 | 代表 | 功能 |
|------|------|------|
| 终结地 | Hall of Storm Giants ({5}{U} 7/7) / Castle Ardenvale (制造 1/1) | 后期不卡地的胜利手段 |
| 通灵地 | Otawara, Soaring City ({3}{U} + 弃) / Boseiju, Who Endures | 起动式异能反咒/破除 |
| 抓牌地 | Geier Reach Sanitarium / Mikokoro, Center of the Sea | 后期 mana sink |
| Tron 地 | Urza's Mine + Tower + Power Plant | 集齐 7 mana |
| 加速地 | Zhalfirin Void / Field of Ruin | 加速 / 反非基本地 |
| 横置地 | Mishra's Foundry / Mutavault / Faerie Conclave | 后期横置变生物 |
| Saga 地 | Urza's Saga | T1 出 / 章节触发 / 终结 |

### 3.10 MDFC（Modal Double-Faced Cards）

Zendikar Rising 推出的模式式双面牌。**两面合一张牌**，进战场可选哪面（部分是法术正面 / 地反面）。

**关键 CR 规则**（CR 712）：
- 在牌库 / 坟墓场 / 放逐区只显示**正面**特征
- 因此对 Belcher、Cascade、Living End 等"非地"判定有特殊意义
- 反面是地必横置入场

**摩登常见 MDFC**：Sea Gate Restoration / Hagra Mauling / Shatterskull Smashing / Glasspool Mimic 等

## 四、地的不同套牌策略画像

### 4.1 快攻类（Aggro）

**目标**：18-21 张地，快速上 3 地后压力释放。

**配置原则**：
- 大量基本地（抗 Blood Moon、抗 Field of Ruin）
- 取色地 4-8 张（避免过多生命减损）
- 0-2 张特殊功能地
- 几乎不放 ETB 横置类地（fastland / surveil land 例外）

**示例（Boros Energy 风格）**：
- 2 山 + 2 平原（基本）
- 4 Inspiring Vantage（fastland）
- 4 Sacred Foundry（shock）
- 4 Arid Mesa / Bloodstained Mire（fetch）
- 1 Bonders' Enclave（特殊抓牌）
- 1 Den of the Bugbear（终结）

**关键考量**：每减 1 张地 ≈ 多 1 张快攻牌，但要保证 90% 概率 T2 双色（≥ 13 双色源）。

### 4.2 中速类（Midrange）

**目标**：22-24 张地，T3-T5 持续打出 2-4 费威胁。

**配置原则**：
- 平衡 fetch + shock + surveil
- 含 1-3 张特殊功能地（终结地 / 通灵地）
- 主色 + 1 splash（如 Jund 三色）

### 4.3 控制类（Control）

**目标**：24-27 张地，T4-T6 不能卡地（要持续反击 / 抓 / 清场）。

**配置原则**：
- 大量取色地（双色压缩）+ 多色源
- 4-6 张特殊功能地（终结、通灵、抓牌）
- 至少 4 张基本地抗 Blood Moon

### 4.4 组合技类（Combo）

#### Type A：依赖加速（Amulet Titan / Storm）

**目标**：18-22 张地 + 加速神器（Amulet of Vigor、Ruby Medallion）

**配置原则**：
- 加速神器代替部分地（每张算 0.5-0.7 张）
- 弹回地（Bouncelands）配合 Amulet of Vigor 双倍加速
- 真地数 18-22 + 加速神器 8-12 = 实际 mana 来源 24+

#### Type B：神器加速（Ad Nauseam / Belcher）

**目标**：减少真地数到极端（10-12 真地或 0 真地），用 Lotus Bloom / Pyromancer's Goggles / Mox 类加速。

**配置原则**：
- 真地极少 → 必须有 cantrip 或 mana fixer 支援
- 神器加速含 cmc=0 类（Lotus Bloom、Mishra's Bauble）
- 关键回合（T2-T3 起动加速 → T3-T4 出胜利件）

#### Type C：MDFC 无地（Tameshi Belcher）

**目标**：0 真地，所有"地槽"由 MDFC 提供。

**配置原则**：
- MDFC 正面是法术/反面是地，进战场可选哪面
- 在牌库内全部按法术正面计算（CR 712.8a）
- Belcher 起动翻牌时全部按"非地"处理 → 一次翻光全部牌库
- 配合 Lotus Bloom / Whir of Invention 加速

### 4.5 Tron / 大法术力

**目标**：22-26 张地（含 4-4-4 Tron 地），T3 集齐 7 mana。

**配置原则**：
- 4 Urza's Mine + 4 Urza's Tower + 4 Urza's Power Plant
- 0-3 张基本地（被 Field of Ruin 锁地后不至于卡死）
- Sylvan Scrying / Expedition Map 找 Tron 地
- 警惕：Magus of the Moon / Blood Moon → Tron 地变山

## 五、关键回合分析（What Can I Do on Turn N）

每套牌都必须答出"我 T1-T6 各回合在做什么"。下面用一套套牌示例：

### 示例：Boros Energy（22 地）

| 回合 | 法术力 | 操作 |
|------|------|------|
| T1 | 1 | 出 Guide of Souls / Ocelot Pride / Nurturing Pixie |
| T2 | 2 | Phlage（寄宿）/ Galvanic Discharge / Goblin Bombardment |
| T3 | 3 | Ajani, Nacatl Pariah → 翻面 6/4 |
| T4 | 4 | Ajani 翻面 + Goblin Bombardment 燃烧 |
| T5 | 5 | 持续燃烧或 Hall of Storm Giants 终结（如有） |
| T6+ | 6 | 通常已结束游戏 |

**关键决策**：
- T2 卡 2 颜色（{R}{W}）必须 13-14 双色源 → 满足 Karsten 公式
- T3 三色（如 Galvanic Discharge / Phlage / Ajani）必须 11-12 红源 + 11-12 白源

## 六、地的破坏与防御

### 6.1 主流地破坏威胁

| 威胁 | 影响 | 防御 |
|------|------|------|
| Blood Moon | 所有非基本地变山 | 多放基本地 / 主牌 Boseiju / 备牌 Force of Negation |
| Magus of the Moon | 同上（生物形式）| 杀生物 |
| Field of Ruin | 锁定非基本地（每个对手各搜一基本）| 多放基本地 |
| Wasteland-类 | 单点摧毁非基本地 | 多放基本地 |
| Damping Sphere | 同名地横置至多产 1 mana → 锁 Tron | 备牌反神器（Hurkyl's Recall）|
| Alpine Moon | 命名某非基本地，那种地变 Plains 类型 | 备牌反结界 |

### 6.2 地破坏抗性的设计

- **基本地数量**：抗 Blood Moon 的最简单方案。8+ 张基本地通常足够保留 1-2 个色源
- **Boseiju, Who Endures**：反结界类破坏 / 反神器
- **Cavern of Souls**：选定生物类型免疫反击（部落套牌核心）

## 七、配地的常见反模式

| 反模式 | 后果 | 修复 |
|--------|------|------|
| 取色 + Shock 比例过高（10+ 张）| 30-40% 起手生命 -2-4 | 加 1-2 张基本地 |
| 全部 ETB 横置地 | T1 卡 mana | 必须 4 张以上 ETB 直立地（基本 / Shock / Filter） |
| 双色无 fetch | 卡颜色概率高 | 加 4-8 张 fetch |
| 三色但仅 1 类 fetch | 第三色源不稳 | 加 Triome 或 splash 色 fetch |
| 特殊地 > 6 张 | 抗 Blood Moon 弱 | 减少 1-2 张特殊地 / 加基本地 |
| 0 真地但无加速 | T1-T2 完全瘫痪 | 加 Lotus Bloom / Mox / cantrip 引导 |

## 八、配地决策树

```
1. 套牌速度？
   ├─ 快攻 → 18-21 地，4-8 fetch，2-4 特殊
   ├─ 中速 → 22-24 地，6-8 fetch，3-5 特殊
   ├─ 控制 → 24-27 地，6-8 fetch，4-6 特殊
   ├─ Combo（加速）→ 18-22 地 + 加速神器
   └─ Tron / 特殊 → 22-26 地（含 12 张 Tron）

2. 颜色数？
   ├─ 单色 → 18-22 张，0-2 fetch（不必要）
   ├─ 双色 → 22-24 张，4-8 fetch + 4 shock
   ├─ 三色 → 22-26 张，8 fetch + 4 shock + 4 Triome
   └─ 4-5 色 → 24-26 张，10-12 fetch + 多种 Triome

3. 关键回合？
   ├─ T1 关键 1 费（{C}）→ 14 张该色源（≥ 14/22 = 64%）
   ├─ T2 关键双色（{C}{C}）→ 20 张该色源
   ├─ T3 关键三色（{C}{C}{C}）→ 23 张该色源
   └─ 多色 T3 → 三色每色 ≥ 14 张

4. 反 Moon 需求？
   ├─ 高（环境多 Blood Moon）→ 6-8 张基本地
   ├─ 中 → 4-6 张基本地
   └─ 低 → 2-4 张基本地

5. 终结地需求？
   ├─ 控制 → 1-2 张终结地（Hall of Storm Giants 类）
   ├─ 中速 → 1 张终结地
   └─ 快攻 / 组合 → 0 张
```

## 九、检查清单（套牌完成前）

完成主牌设计后，按以下清单核对：

- [ ] 总地数符合速度档位（aggro 18-22 / midrange 22-24 / control 24-27）
- [ ] 每个关键回合的色源 ≥ Karsten 公式门槛
- [ ] 取色地数与 fetchable 双色地（shock / triome）数量相匹配
- [ ] 至少 4 张基本地（抗 Blood Moon）
- [ ] ETB 直立地比例 ≥ 50%（避免 T1 必横置卡 mana）
- [ ] 1-3 张特殊功能地（终结 / 通灵 / 抓牌，视套牌定位）
- [ ] 无 splash 色仅靠 1-2 张色源（要么 4-8 张要么剪掉那一色）
- [ ] 加速神器与真地总和满足曲线需求（每张加速算 0.5-0.7 张地）

任何一条不达标必须返工。

## 相关概念

- [[mana-curve|法术力曲线]]
- [[land|地]]
- [[mana-abilities|法术力异能]]

## 相关页面（策略分支）

- [[constructed-deck-construction|构筑套牌组牌总论]]（待创建）
- [[modern-format|摩登赛制总览]]
- [[deck-analysis-template|套牌分析模板]]

## 来源

- Frank Karsten, "How Many Sources Do You Need to Consistently Cast Your Spells?" — TCGplayer (2018)
- Frank Karsten, "How Many Lands Do You Need in Your Deck?" — TCGplayer (2017)
- 实战观察：MTGTop8 / MTGGoldfish 摩登套牌牌表（2026-04）
