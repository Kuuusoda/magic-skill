# MO Vintage Cube 深度分析报告

## 数据来源

- **平台**：Magic Online (MTGO)
- **牌池大小**：540 张
- **分析时间**：2026-04-29
- **数据文件**：`raw/tools/mtg_wiki/data/movc_cards.json`

---

## 一、牌池概览

### 颜色分布
| 颜色 | 数量 | 占比 | 定位 |
|------|------|------|------|
| 蓝 (U) | 74 | 16.0% | 🥇 最强，控制/Combo 核心 |
| 黑 (B) | 65 | 14.1% | 🥈 Tutors + Rituals |
| 无色 (C) | 64 | 13.9% | 🥉 0费神器密度极高 |
| 红 (R) | 64 | 13.9% | 快攻/Storm |
| 绿 (G) | 61 | 13.2% | Channel/Fastbond |
| 白 (W) | 56 | 12.1% | 去除/Stoneforge |
| 多色 | 56 | 12.1% | 双金为主 |
| 地 | ~100 | - | Fetchlands + Duals + 功能地 |

### 费用曲线
| CMC | 数量 | 关键牌 |
|------|------|--------|
| 0 | 117 | Lotus、Moxen、Sol Ring、Ballista |
| 1 | 96 | Brainstorm、Bolt、Path、Birds |
| 2 | 128 | Counterspell、Stoneforge、Snapcaster |
| 3 | 92 | Tarmogoyf、Liliana、Jace VP |
| 4+ | 50 | Griselbrand、Tinker 目标 |

### 稀有度
| 稀有度 | 数量 |
|--------|------|
| Rare | 297 |
| Mythic | 123 |
| Uncommon | 68 |
| Common | 40 |
| Special | 12 |

---

## 二、多色分布

| 组合 | 数量 | 典型原型 |
|------|------|---------|
| UW | 7 | Azorius Control |
| RU | 7 | Izzet Tempo |
| BU | 6 | Dimir Midrange |
| BG | 5 | Golgari Graveyard |
| BR | 5 | Rakdos Aggro |
| GR | 5 | Gruul Stompy |
| RW | 5 | Boros Aggro |
| GW | 4 | Selesnya Ramp |
| GU | 4 | Simic Value |
| BW | 3 | Orzhov Reanimator |
| BUW | 1 | Esper Control |
| GRU | 1 | Temur Midrange |
| BGU | 1 | Sultai Control |
| GRUW | 1 | 4C Omnath |
| BGUW | 1 | 5C Good Stuff |

---

## 三、五大套牌原型

### 🏆 1. Blue-X Control（最强）
**牌池支撑度：★★★★★**

**核心 1 费：**
- Brainstorm、Ponder、Preordain、Ancestral Recall
- Spell Pierce、Stern Scolding

**核心 2 费：**
- Counterspell、Daze、Mana Drain、Lose Focus
- Memory Lapse、Miscalculation、Remand
- Snapcaster Mage、Jace, Vryn's Prodigy

**核心 3 费+：**
- Force of Will、Force of Negation
- Jace, the Mind Sculptor
- Mystic Confluence

**终结手段：**
- Thassa's Oracle（自体磨牌胜利）
- Tinker → Blightsteel Colossus
- Jace TMS 磨牌

**最佳配合色：** 白（去除）> 黑（Tutors）> 红（Tempo）

---

### 🌩️ 2. Storm Combo
**牌池支撑度：★★★★☆**

**Rituals（法术力爆发）：**
- Dark Ritual、Cabal Ritual
- Manamorphose

**Storm Payoff（胜利条件）：**
- Tendrils of Agony
- Brain Freeze

**Tutors（组合技一致性）：**
- Demonic Tutor、Vampiric Tutor、Mystical Tutor
- Imperial Seal、Wishclaw Talisman

**加速：**
- Black Lotus、5x Mox、Lotus Petal
- Lion's Eye Diamond（配合 Breach）
- Mana Crypt

**Breach 变体：**
- Underworld Breach + Brain Freeze（自体磨牌库再回收）
- LED 弃手 → Breach 回收 → 循环

---

### ⚰️ 3. Reanimator
**牌池支撑度：★★★★☆**

**核心组件：**
- Entomb（精确送坟）
- Reanimate / Exhume / Animate Dead / Shallow Grave

**目标生物：**
- Griselbrand（抓7+生命交换）
- Archon of Cruelty（进场触发）
- Inkwell Leviathan（Shroud）

**自磨引擎：**
- Bazaar of Baghdad（一回合磨5张）
- Thassa's Oracle（备 victory 条件）

**加速配合：**
- Dark Ritual → 2费 Reanimate
- Lotus Petal → 绕过费用限制

---

### 🏗️ 4. Tinker / Big Mana
**牌池支撑度：★★★★☆**

**Tinker 组件：**
- Tinker（牺牲神器→找神器放入场）
- 目标：Blightsteel Colossus、Inkwell Leviathan

**加速密度（极高）：**
- 0费：Black Lotus、5x Mox、Chrome Mox、Mox Diamond、Mox Opal
- 1费：Sol Ring、Mana Crypt、Lotus Petal、LED
- 2费：Everflowing Chalice、Grim Monolith

**配合：**
- Urza's Saga → 找 Sol Ring / Shadowspear
- Mishra's Workshop → 放神器减费
- Tolarian Academy → 每神器产U

---

### ⚔️ 5. Aggro（白/红/ Gruul）
**牌池支撑度：★★★☆☆**

**白快攻：**
- Mother of Runes、Thraben Inspector
- Stoneforge Mystic（找 Batterskull）
- Adeline、Luminarch Aspirant
- 去除：Swords to Plowshares、Path to Exile

**红快攻：**
- Ragavan、Dragon's Rage Channeler
- Lightning Bolt、Chain Lightning
- Goblin Guide（如存在）

**Gruul 中速：**
- Tarmogoyf
- Wrenn and Six
- Bloodtithe Harvester

---

## 四、关键单卡分类

### Power 9 ✅
- Black Lotus
- Mox Pearl / Sapphire / Jet / Ruby / Emerald
- Ancestral Recall
- Time Walk
- Timetwister

### 0费神器（17张）
| 牌名 | 作用 |
|------|------|
| Black Lotus | 3费任意，最强加速 |
| Chrome Mox | 弃牌印卡，0费产1 |
| Everflowing Chalice | 多踢，储能 |
| Lion's Eye Diamond | 弃手产3，Storm/Breach 用 |
| Lotus Petal | 牺牲产1任意 |
| Mana Crypt | 0费产2，每回合赌硬币 |
| Mishra's Bauble | 0费看牌库顶 |
| Mox Diamond | 弃地印卡，0费产1 |
| 5x 基础 Mox | 各产对应色 |
| Urza's Bauble | 看任意牌库顶 |
| Zuran Orb | 牺牲地回2血 |
| Walking Ballista | 0费进但有X指示物 |

### Tutors（6张）
- Demonic Tutor（B，任意牌库顶）
- Vampiric Tutor（B，任意牌库顶，-2血）
- Mystical Tutor（U，瞬间/法术牌库顶）
- Imperial Seal（B，任意牌库顶，-2血）
- Worldly Tutor（G，生物牌库顶）
- Enlightened Tutor（W，神器/结界牌库顶）

### 反击咒语（14张）
| 费用 | 牌名 |
|------|------|
| 1 | Mana Tithe(W)、Spell Pierce(U)、Stern Scolding(U) |
| 2 | Counterspell、Daze、Lose Focus、Mana Drain、Mana Leak、Memory Lapse、Miscalculation、Remand |
| 3+ | Force of Negation、Force of Will、Mystic Confluence |

---

## 五、实战选牌优先级（修正版）

### 一抓（Pack 1, Pick 1）
| 优先级 | 类型 | 例子 |
|--------|------|------|
| S | Power 9 / 0费加速 | Black Lotus、Moxen |
| A | 最强蓝牌 | Brainstorm、FoW、Jace TMS |
| A | Tutors | Demonic Tutor |
| B | 顶级去除 | Swords to Plowshares |
| B | 强 2费生物 | Stoneforge、Snapcaster |

### 中期信号
- **蓝开放**：连续收到 2费反击 / 1费滤牌 → 入蓝
- **黑开放**：Entomb + Reanimate 同时出现 → Reanimator 可行
- **0费神器多**：Tinker / Big Mana 路线
- **无蓝牌**：转白/红 Aggro

### 构组要点
1. **17-18 地**（低曲线可 16 地）
2. **保证 8+ 张 1-2 费咒语**（Cube 节奏极快）
3. **至少 2 张 Tutors**（提升 singleton 一致性）
4. **备牌准备**：
   - 对 Combo：更多反击
   - 对 Aggro：Wrath / 生命增益
   - 对 Control：额外威胁

---

## 六、隐藏强路线

### Underworld Breach Combo
```
Underworld Breach（2费结界）
+ LED（弃手产3）
+ Brain Freeze（磨3张，Storm 后磨更多）
= 自体磨空牌库 → Thassa's Oracle 胜利
```

### Channel + 大生物
```
Channel（1费产任意法术力）
→ Emrakul / Kozilek（15费生物）
→ 或配合 Fastbond 一回合多次下地
```

### Oath of Druids
```
Oath of Druids（2费结界）
→ 对手生物更多时，自己免费翻生物
→ 目标：Griselbrand、Archon
```

---

## 七、与通用 Vintage Cube 的差异

| 维度 | 通用 VC | MO VC |
|------|---------|-------|
| 总牌数 | ~540 | 540 |
| 0费神器 | ~15 | 17 |
| Reanimator | 不完整 | **完整**（Entomb+Reanimate+目标） |
| Breach | 少见 | **存在**（Underworld Breach） |
| Channel | 常见 | **存在**（+ Fastbond） |
| 新牌 | 无 | **有**（MO 会更新） |

---

*报告生成时间：2026-04-29*
*数据来源：MTGO Vintage Cube 牌表 + Scryfall API Oracle 数据*
