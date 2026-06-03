---
created: 2026-05-02
updated: 2026-05-02
type: synthesis
tags: [modern, azorius-control, uw-control, deck-profile, scepter-chant]
sources: [data/decklists/azorius-control.json, data/analysis/azorius-control_analysis.json]
---

# Azorius Control（蓝白控）套牌分析

## 数据基础

- **样本量**：14 份真实牌表（mtgdecks.net 抓取，2026-04-16 至 2026-04-27）
- **变体分布**：主流 Scepter-Chant 控制 11 份；激进 Suppression Ray 变体 3 份
- **当前 Meta 占比**：未进入 2026-05-01 Top 12 快照（占比低于 2.1%）— 属于环境角落选择

本页主要分析主流变体（11 份）。

## 套牌定位

- **原型**：组合控制（Scepter-Chant 软锁 + 棋类控场）
- **关键回合**：T4-T6（Scepter+Chant 上线后开始锁牌）
- **操作难度**：高（需要精确判断每回合 1 张咒语的优先级、烙印时机、Day's Undoing 时点）
- **优势对局**：单威胁中速、纯组合技
- **劣势对局**：多威胁横铺（Boros Energy）、快速爆头（Izzet Prowess、Ruby Storm）

## 核心机制

操控者通过 **Isochron Scepter 烙印 Orim's Chant** 实现每回合软锁：

- 起动 Scepter → 复制 Orim's Chant（mv=1，符合烙印条件）
- 副本可选支付 {W} 加成 → 目标对手该回合不能施放咒语，且生物不能进攻
- 配合 Teferi, Time Raveler 阻止对手在己方回合做事
- 配合 Narset + Day's Undoing 完成"我抓 7 张、对手抓 1 张"的资源不平衡

**注意：Orim's Chant 不阻止以下动作**

- 起动式异能（含 Otawara 通灵、地的法术力异能、PW 忠诚异能）
- 触发式异能（Ragavan、Mox Opal、Urza's Saga 章节）
- 出地（特殊动作，非施放咒语）

由 mtg-judge-zh agent 核对，详见 [核心规则交互](#核心规则交互)。

## 主牌（60 张，主流变体均值）

### 地（24 张）

**取色地（8 张）**
- 4 Flooded Strand
- 2 Scalding Tarn
- 2 Arid Mesa

**双色 / 索价地（4 张）**
- 2 Hallowed Fountain
- 2 Meticulous Archive

**单色基础地（4 张）**
- 2 Island
- 2 Plains

**功能地（5 张，均为 1 张 1 张配置）**
- 1 Hall of Storm Giants（终结手段，{5}{U} 起动 7/7 守护 3）
- 1 Monumental Henge（搜历史咒物）
- 1 Geier Reach Sanitarium
- 1 Otawara, Soaring City（通灵：{3}{U}+弃，回手任一非地永久物）
- 1 Mystic Gate（Lorwyn 滤色地）

**多色拓展槽（3 张，因 Cosmic Rebirth / 多色 X 法术等需要）**
- 1 Steam Vents
- 1 Sacred Foundry
- 1 Watery Grave 或 1 Breeding Pool

> **数据观察**：8/11 份主流变体含 Steam Vents，主要用于通过取色地搜出双色源；少数列表运行 Cosmic Rebirth 或 Wrath of the Skies 大 X 时需要更多颜色源。

### 法术（36 张）

**1 法术力（5 张）**
- 4 Orim's Chant — 核心组合件，13/14 牌表 4 张
- 1 Spell Snare — 反 mv=2 的低费威胁（Ragavan、Goblin Bombardment、Counterspell 镜像）

**2 法术力（13 张）**
- 4 Prismatic Ending — 万能 X 费除惧
- 4 Consult the Star Charts — {1}{U} 主调度，加成 {1}{U} 抓 2 张
- 3 Counterspell — {U}{U}，硬反
- 2 Isochron Scepter — 烙印对象 Orim's Chant

**3 法术力（5 张）**
- 3 Teferi, Time Raveler — 闪现进场，对手无法瞬间施放，PW 抓 1 弃 1 / 弹回非地永久物
- 2 Day's Undoing — 必须在己方回合施放（结算 end the turn 放逐堆叠物）

**4 法术力（6 张）**
- 4 Solitude — 寄宿白色单卡免费施放，放逐 1 个目标生物
- 2 Wrath of the Skies — {X}{W}{W} 累积能量，用任意能量销毁神器/生物/结界（不打地、不打 PW、可打代币）

**5 法术力（1 张）**
- 1 Lórien Revealed — 海岛循环 {1}（实际即第 25 张地，硬施放 5 费抓 3）

**忠诚 3-4-5 棋（3 张）**
- 3 Narset, Parter of Veils — 静止式：每位对手每回合至多抓 1 张；-2 看顶 4 选非生物非地

> **额外槽位** ：1/11 份主流变体含 Force of Negation（备牌中 7/11，主要进入备牌），1/11 份含 Cosmic Rebirth、Logic Knot、Kasmina 等单张科技。

### 法术力曲线

| 总费用 | 张数 | 占非地比例 |
|--------|------|------------|
| 1 | 5 | 14% |
| 2 | 13 | 36% |
| 3 | 5（含 Narset 算 3）| 14% |
| 4 | 6 | 17% |
| 5 | 1（实际 1 费循环）| 3% |
| PW 3 | 3 | 8% |

> **关键观察**：2 费段密集（13 张），3 费段轻、4 费段重。这是因为 Solitude 通常以寄宿（pitch）方式施放，**实际操控者很少在 4 费段额外投放法术力**——曲线"看起来到 4"，实操体感"卡在 2-3"。Wrath of the Skies 在 X=2 即 {2}{W}{W} 时才会硬释，否则当 sweeper 留到 X=3+ 销毁更多。

### 生物结构

**主牌仅 1 类生物：Solitude（精灵 Elemental，4 张）**

这一构成意义重大：

1. 满足 **Kaheera, the Orphanguard 同伴条件**（猫/精灵/夜魇/恐龙/野兽），可用作第 16 张备牌
2. 主牌生物极少 → 对手的生物移除（Wear Down、Galvanic Discharge、Phlage 燃烧）失去目标
3. 仅依赖 Hall of Storm Giants 作为创造生物的备用胜利手段

> **数据观察**：6/11 份主流变体在备牌中带 Kaheera 作同伴；1 份变体（25-Apr-2026）额外运行 3 张 Quantum Riddler，破坏同伴资格但增加进攻速度。

## 备牌（15 张，主流变体均值）

| 张数 | 单卡 | 出现率 | 主要去向 |
|------|------|--------|----------|
| 4 | Consign to Memory | 11/11（100%）| Eldrazi Tron、Ruby Storm、Living End、Affinity 触发链 |
| 3 | Mystical Dispute | 7/11（64%）| 镜像、Jeskai Blink、Dimir Frog |
| 2 | High Noon | 6/11（55%）| Ruby Storm、Neoform、Living End |
| 1-2 | Surgical Extraction | 7/11（64%）| Esper Reanimator、Living End、风暴 |
| 1-2 | Celestial Purge | 7/11（64%）| Boros Energy、Izzet Prowess（红黑威胁） |
| 0-1 | Rest in Peace | 5/11（45%）| 全坟场套牌 |
| 1 | Kaheera, the Orphanguard | 6/11（55%）| 同伴位（不进牌库，不占 15 槽） |

### Consign to Memory 的限制（关键！）

由 mtg-judge-zh 验证：Consign to Memory 仅能反击：
- 触发式异能
- **无色咒语**

**不能反击有色咒语**——即使是非生物的有色法术、瞬间也不行。  
所以这张牌不是万能反击，主要去向是：
- Ragavan ETB 触发（偷 Treasure）
- Urza's Saga 章节触发
- Eldrazi 无色咒语（Karn, the Great Creator 例外，因 Karn 是有色）
- Ruby Storm 的 Birgi、Galvanic 触发链
- Phlage 的进战返手触发

## 主流套牌 Matchup 与游戏路径

> 数据来源：当前 meta 由 [[2026-05-01-modern]] 快照提供。下文 Matchup 评估依据：单卡角色契合度 + 操控者视角的牌差计算，**未基于实战胜率统计**（数据样本不足）。所有"优劣势"判断均为推论，需以实战验证。

### vs Boros Energy（T1 16.8%）— 劣势

**对手威胁路径**：T1 Guide of Souls 或 Ocelot Pride → T2 Phlage / Ajani / Galvanic Discharge → T3 Goblin Bombardment + Phlage 循环。

**操控者计划**：
- T1：留 Spell Snare 反 Ragavan / Galvanic Discharge / Bombardment
- T2：Prismatic Ending 点除关键威胁（Ocelot Pride、Phlage）
- T3-4：Wrath of the Skies (X=2-3) 横扫
- 关键：**必须 T4 之前部署 Scepter+Chant**，否则 Phlage 燃烧会绕过软锁压死你

**换牌（操控者视角）**：
- 拿出：3 Counterspell（对手 1-2 费威胁多，硬反低效）、1 Day's Undoing（对手手少，反而帮对手）
- 加入：2 Celestial Purge（杀 Phlage、Bombardment、红色 PW）、2 Wrath of the Skies #3（如有）

### vs Affinity（T1 10.2%）— 中等偏劣

**对手威胁路径**：T2 横铺神器生物 → T3 Cranial Plating / Nettlecyst → T4 杀人。

**操控者计划**：
- Wrath of the Skies 是核心牌（X=1-2 即销毁全部低费神器和生物）
- Prismatic Ending 点除 Cranial Plating
- 注意：**Affinity 自带 Welding Jar / Springleaf Drum 反应，且 Saga 章节触发不被 Counterspell 反**

**换牌**：
- 拿出：3 Counterspell（很多关键牌走神器触发非咒语线）、1 Orim's Chant（Bombardment 类无法封）
- 加入：2 Celestial Purge（红色威胁 + Goblin Bombardment）、Consign to Memory 留 4 张（专门反 Saga 触发和 Plating ETB）

### vs Jeskai Blink（T1 8.1%）— 微优

**对手威胁路径**：T1-2 Ragavan / Phelia / Quantum Riddler → T3-4 Ephemerate 闪烁循环 → T5+ 资源碾压。

**操控者计划**：
- 镜像式资源对拼，操控者优势在 Day's Undoing + Narset 不平衡抓牌
- T3 Teferi, Time Raveler 是关键：阻止对手 Ephemerate 在你的回合内闪烁
- T4 Scepter+Chant 后，对手无法部署关键 ETB 触发

**换牌**：
- 拿出：2 Wrath of the Skies（对手生物少，Solitude 即可点除）、1-2 Supreme Verdict
- 加入：3 Mystical Dispute（对手蓝色咒语多）、1 Surgical Extraction（拔 Phlage 或 Ephemerate）

### vs Eldrazi Tron（T2 5.0%）— 优势

**对手威胁路径**：T3 Tron 上线 → T4-5 Karn / Ulamog / Ugin / All Is Dust。

**操控者计划**：
- Spell Snare 反 Talisman / Mind Stone（攒 mv=2 加速）
- Counterspell 留 Karn 和 Ugin
- Consign to Memory 反 Karn 起动后获得的有色咒语？**注意：Consign 不能反 Karn 直接起动，但可反 All Is Dust（无色咒语）**

**换牌**：
- 拿出：2 Solitude（对手生物极少）、1 Orim's Chant（无大量生物攻击）
- 加入：2 Surgical Extraction（拔 Tron 地）、Consign to Memory 全留、Mystical Dispute（Karn 有色但不蓝……取消，留 Mystical 用于其他对局）

### vs Izzet Prowess（T2 4.5%）— 中等偏劣

**对手威胁路径**：T1 Ragavan / Slickshot Show-Off → T2-3 Prowess 触发 + 燃烧 → T4 杀人。

**操控者计划**：
- Wrath of the Skies (X=2) 是关键牌
- Prismatic Ending 点除 Slickshot
- 难点：**对手 1 费咒语极多，操控者每回合只能 1 张反击**

**换牌**：
- 拿出：1 Day's Undoing（手少时对手反获利）、1 Lórien Revealed（速度对局抓 3 太慢）
- 加入：2 Celestial Purge（点除 Phlage、Slickshot、Ral）、Consign to Memory（反 Manaless 触发）

### vs Amulet Titan（T2 4.4%）— 中等

**对手威胁路径**：T2-3 Amulet of Vigor + Bouncelands → T3-4 Primeval Titan 搜地终结。

**操控者计划**：
- Counterspell + Force of Negation 反 Titan
- Surgical Extraction 拔 Primeval Titan 是核心备牌
- T3 Teferi 闪现进场弹 Amulet（Otawara 通灵也可弹）

**换牌**：
- 拿出：2 Solitude（对手早期生物少）、2 Wrath of the Skies（生物点不到 Bouncelands）
- 加入：2 Surgical Extraction（拔 Titan）、3 Mystical Dispute（Sword of Forge 类不蓝？保留 1 张）

### vs Ruby Storm（T2 4.0%）— 优势

**对手威胁路径**：T2-3 Ruby Medallion + Galvanic Discharge → T3-4 Storm count → 杀人。

**操控者计划**：
- High Noon 是核心备牌（每回合限 1 咒语 = 风暴熄火）
- Consign to Memory 反 Birgi、Galvanic Iteration 触发
- T3 Scepter+Chant 上线后，对手无法在己方回合 storm 链

**换牌**：
- 拿出：4 Solitude（对手无生物）、2 Wrath of the Skies、3 Prismatic Ending（点不到非永久物）
- 加入：4 Consign to Memory、3 Mystical Dispute、2 High Noon、2 Surgical Extraction（拔 Ruby Medallion 或 Galvanic）

### vs Esper Reanimator（T2 3.8%）— 优势

**对手威胁路径**：T2 Faithful Mending / Persist 弃牌 → T3-4 召集 Atraxa / Griselbrand。

**操控者计划**：
- Surgical Extraction 拔 Atraxa
- Rest in Peace 关闭整个引擎
- Counterspell 反 Persist

**换牌**：
- 拿出：4 Solitude（对手无小生物）、2 Wrath of the Skies、1 Orim's Chant
- 加入：1-2 Rest in Peace、2 Surgical Extraction、4 Consign to Memory（反 Atraxa ETB）、3 Mystical Dispute

### vs Living End（T2 3.2%）— 优势

**对手威胁路径**：T3 Cascade 串 Living End → 反咒带回所有循环生物。

**操控者计划**：
- Counterspell 反 Living End
- Consign to Memory 反 Cascade 触发（Living End 是无色法术？**否，是黑色——所以 Consign 不打它本身**，但能反 Force of Negation 等触发）
- 实际反 Living End 的最佳方式：硬反、Mystical Dispute 蓝色（Living End 不是蓝色）……需要 Counterspell + Force of Negation 起手

**换牌**：
- 拿出：4 Solitude、2 Wrath of the Skies、3 Prismatic Ending
- 加入：1-2 Rest in Peace、2 Surgical Extraction（拔 Living End）、High Noon（限制 Cascade 回合多动作）

### vs Domain Aggro（T3 3.6%）— 中等

**对手威胁路径**：T1-2 1/2 Domain creatures → T3-4 Atraxa / Leyline Binding。

**操控者计划**：
- Wrath of the Skies (X=2-3) 横扫
- Prismatic Ending 点除大单卡
- 注意：Leyline Binding 走 Domain mv 减费，**Counterspell 反不到的话需要 Force of Negation**

**换牌**：参考 vs Boros Energy。

### vs Neoform（T3 2.4%）— 优势

**对手威胁路径**：T2 Neoform 把小生物换成 Atraxa。

**操控者计划**：
- 反 Neoform 本牌
- Surgical Extraction 拔 Atraxa
- Solitude 点除小生物 → 对手无 Neoform 燃料

**换牌**：参考 vs Esper Reanimator。

### vs Dimir Frog（T2 2.1%）— 中等偏劣

**对手威胁路径**：T1-2 弃牌（Thoughtseize、Inquisition）+ Murktide 准备 → T3-4 Murktide / Tasigur。

**操控者计划**：
- 操控者难点：**手牌被弃牌掏空**，反击保护不足
- T3 Teferi, Time Raveler 是关键：Teferi 作为 PW 可被攻击但不能被反对手手牌干扰
- Force of Negation 反 Murktide

**换牌**：
- 拿出：4 Solitude（对手无小生物）、2 Wrath of the Skies（对手生物少）
- 加入：3 Mystical Dispute、1-2 Surgical Extraction（拔 Murktide）、Force of Negation 全留

## 核心规则交互

由 mtg-judge-zh agent 核对：

### Orim's Chant + Isochron Scepter

- 烙印 Orim's Chant（mv=1，符合 ≤ 2）
- 起动 {2}{T} 复制并施放副本，复制时**可选择支付 {W} 加成**
- 加成版本同时阻止施放咒语和宣告攻击
- **不影响**：起动式异能、触发式异能、出地、已经在堆叠/已结算的咒语

### Day's Undoing + Narset, Parter of Veils

- Day's Undoing：**必须在己方回合施放**，否则 end the turn 跳到对手回合结束，对手获得 7 张
- Narset 在场时：双方各洗手→各抓 7→Narset 静止式将对手抓 7 替换为只抓 1
- 操控者在己方回合：抓 7 张，对手抓 1 张（资源不平衡 6 牌差）

### Wrath of the Skies 的能量机制

- {X}{W}{W} 法术：你获得 X 个能量指示物（{E}）
- 然后**支付任意数量 {E}**（可使用先前累积的能量）
- 销毁所有 mv ≤ 已支付能量的神器、生物、结界
- **不打地、不打 PW、不打战斗**
- 包括代币（mv=0），所以即使 X=0 仍可清场

### Consign to Memory 的反击范围

- **能反**：触发式异能、无色咒语
- **不能反**：起动式异能、有色咒语（即使是非生物的）、静止式异能
- 主要去向：Ragavan ETB、Urza's Saga 章节触发、Phlage 进战返手触发、Eldrazi 无色咒语

## 操作要点（操控者视角）

### 烙印时机

不要 T2 直接烙印 Scepter——等到 T3-4 与 Teferi 配套。原因：

- T2 烙印 = 弃牌权重过高，对手 T3 可消耗你的 Scepter（Wear Down、Crashing Footfalls 类破坏）
- T3+ 烙印时通常已有 Teferi 或 Counterspell backup

### Day's Undoing 时机

- 手中 ≤ 3 张时考虑施放
- **必须在己方回合**：否则跳到对手回合结束（你的 end the turn 没把对手回合掐掉）
- 配合 Narset：先解决 Narset 再 Day's Undoing
- 不要在对手攻击步时施放（end the turn 不取消已宣告战斗）

### Solitude 寄宿决策

- 默认寄宿（pitch a white card from hand）实现 0 费瞬间除惧
- 如手白牌 ≤ 1，考虑硬释放（{3}{W}{W}）
- 寄宿首选弃 Wrath of the Skies、Lórien Revealed、Plains（保留 Orim's Chant、Solitude、Teferi）

### Otawara 通灵

- 是起动式异能，**不被 Orim's Chant 阻止**
- 用于解决 Counterspell 反不掉的永久物威胁（如对手已经下场的 Karn、Phlage、Atraxa）
- 注意 {3}{U} + 弃这张地是高成本，T6+ 才容易凑出

### Hall of Storm Giants 终结时机

- {5}{U} 起动，本回合变成 7/7 守护 3 蓝色巨人
- 通常 T8-10 才能稳定起动
- 由于守护 3，对手 Galvanic Discharge / Lightning Bolt / Solitude 难以一回合解决
- 备用胜利手段，因主牌仅 4 Solitude 一类生物

## 数据局限与不确定性

1. **样本量小**（14 份），方差较大；3 份激进变体可能反映不同流派
2. **未捕获禁牌后的反应**：本数据仅 4 月 16-27 日，禁牌动态未计入
3. **Matchup 评估为推论**：基于单卡契合度，无实战胜率统计
4. **中文译名未完全确认**：以下牌张本地词库未命中，需以官方页面核实
   - Wrath of the Skies、Consult the Star Charts、Day's Undoing、Lórien Revealed、Orim's Chant、Isochron Scepter、Consign to Memory、High Noon、Meticulous Archive、Monumental Henge、Otawara、Suppression Ray、Thundertrap Trainer
5. **Cosmic Rebirth、Lush Portico、Logic Knot、Kasmina** 等单张科技未深入分析

## 关联页面

- [[2026-05-01-modern|2026-05 摩登环境快照]]
- [[boros-energy|Boros Energy 套牌分析]]
- [[jeskai-blink|Jeskai Blink 套牌分析]]
- [[ruby-storm|Ruby Storm 套牌分析]]
- [[esper-reanimator|Esper Reanimator 套牌分析]]
