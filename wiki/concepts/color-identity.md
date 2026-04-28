---
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [万智牌, 指挥官, EDH, 颜色认同, 构组规则, 核心规则]
sources: [cr/1.md, cr/9.md]
---

# 颜色认同（Color Identity）

## 定义

颜色认同（Color Identity）是指挥官赛制最核心的套牌构组限制。一张牌的颜色认同由该牌的**法术力费用中的颜色**和**规则叙述中的法术力符号**共同决定（CR 903.4）。套牌中的所有牌的颜色认同必须是指挥官颜色认同的子集。

颜色认同与「颜色」（Color）是两个不同的概念：
- **颜色**：由法术力费用决定，影响游戏内互动（如保护、目标选择）
- **颜色认同**：由费用 + 规则叙述中的法术力符号决定，仅影响套牌构组

## 规则详解

### 如何确定颜色认同

1. **法术力费用中的颜色符号**（牌张右上角）
2. **规则叙述中的法术力符号**（异能费用、起动式异能、替代性费用等）
3. **颜色标志（Color Indicator）**：部分牌无费用但有颜色标志（如 Pact of Negation）

**不决定颜色认同的因素**：
- 背景故事或插画中的颜色
- 牌张边框颜色
- 提示文字（Reminder Text）中的法术力符号

### 示例

| 牌名 | 法术力费用 | 叙述中的法术力符号 | 颜色 | 颜色认同 |
|------|-----------|-------------------|------|----------|
| Lightning Bolt | {R} | 无 | 红色 | 红色 |
| Cryptic Command | {1}{U}{U}{U} | 无 | 蓝色 | 蓝（无额外颜色符号） |
| Archangel Avacyn | {3}{W}{W} | 转化后异能含 {R} | 白色 | 白红 |
| Transguild Courier | 无 | 规则叙述"Transguild Courier 为所有颜色" | 无色 | 无色 |
| Pact of Negation | {0} | 维持费用含 {3}{U}{U}{U}{U} | 无色 | 蓝色 |
| Golgari Signet | {2} | 起动式异能含 {G/B} | 无色 | 黑绿 |
| Bosh, Iron Golem | {5} | 起动式异能含 {3}{R} | 无色 | 红色 |
| Garruk Relentless | {3}{G} | 背面起动式异能含 {B} | 绿色 | 绿黑 |

### 关键案例

**Pact of Negation（否定契约）**
- 费用 {0}，颜色为无色
- 但规则叙述中的维持费用包含 {3}{U}{U}{U}{U}
- 因此颜色认同为**蓝色**
- 只能在蓝色指挥官的套牌中使用

**Archangel Avacyn（天使艾维欣）**
- 正面费用 {3}{W}{W}，颜色为白色
- 但转化后的规则叙述中包含红色法术力符号 {R}
- 因此颜色认同为**白红**
- 只能在白红或更多色的指挥官套牌中使用

**Golgari Signet（葛加理 Signet）**
- 费用 {2}，颜色为无色
- 起动式异能费用包含 {G/B}
- 颜色认同为**黑绿**
- 只能在黑绿或更多色的指挥官套牌中使用

## 颜色认同与套牌构组

### 套牌合法性检查

一张牌可以放入某指挥官套牌的条件：
- 该牌的颜色认同 ⊆ 指挥官的颜色认同

**示例**：
- **Commander**: Thrasios, Triton Hero（颜色认同：{G}{U}）
- **合法牌**：Counterspell（{U} ✅）、Cultivate（{G} ✅）、Sol Ring（无色 ✅）
- **非法牌**：Swords to Plowshares（{W} ❌）、Demonic Tutor（{B} ❌）

### 混血法术力与颜色认同

混血法术力符号（如 {W/U}、{B/R}）同时属于两种颜色：
- **Azorius Guildgate**（含 {W/U}）的颜色认同为**白蓝**
- 因此不能在只有白色或只有蓝色的指挥官套牌中使用

### 非瑞克西亚法术力（Phyrexian Mana）

非瑞克西亚法术力（如 {W/P}）同时属于白色和无色：
- **Gitaxian Probe**（含 {U/P}）的颜色认同为**蓝色**
- 即使在指挥官不含蓝色的套牌中，也不能使用生命支付来绕过颜色认同限制

## 颜色认同与指挥官选择

### 单色指挥官

| 颜色 | 代表指挥官 | 特点 |
|------|-----------|------|
| 白 | Heliod, Sun-Crowned | 生命获得、指示物 |
| 蓝 | Thassa, God of the Sea | 操控、占卜 |
| 黑 | K'rrik, Son of Yawgmoth | 生命支付、坟场 |
| 红 | Krenko, Mob Boss | 衍生物、敏捷 |
| 绿 | Yisan, the Wanderer Bard | 搜寻、生物 |

### 双色指挥官

| 色组 | 名称 | 代表指挥官 |
|------|------|-----------|
| {W}{U} | Azorius（俄佐立） | Brago, King Eternal |
| {U}{B} | Dimir（底密尔） | Yuriko, the Tiger's Shadow |
| {B}{R} | Rakdos（拉铎司） | Prosper, Tome-Bound |
| {R}{G} | Gruul（古鲁） | Kiki-Jiki, Mirror Breaker |
| {G}{W} | Selesnya（瑟雷尼亚） | Trostani, Selesnya's Voice |
| {W}{B} | Orzhov（欧佐夫） | Teysa Karlov |
| {U}{R} | Izzet（伊捷） | Niv-Mizzet, Parun |
| {B}{G} | Golgari（葛加理） | Meren of Clan Nel Toth |
| {R}{W} | Boros（波洛斯） | Feather, the Redeemed |
| {G}{U} | Simic（析米克） | Tatyova, Benthic Druid |

### 三色及以上指挥官

| 色组 | 名称 | 代表指挥官 |
|------|------|-----------|
| {W}{U}{B} | Esper（艾斯波） | Oloro, Ageless Ascetic |
| {U}{B}{R} | Grixis（格利极） | Kess, Dissident Mage |
| {B}{R}{G} | Jund（勇德） | Korvold, Fierceborn |
| {R}{G}{W} | Naya（纳亚） | Marisi, Breaker of the Coil |
| {G}{W}{U} | Bant（班特） | Chulane, Teller of Tales |
| {W}{B}{G} | Abzan（阿布赞） | Ghave, Guru of Spores |
| {U}{R}{W} | Jeskai（洁斯凯） | Elsha of the Infinite |
| {B}{G}{U} | Sultai（苏勒台） | Tasigur, the Golden Fang |
| {R}{W}{B} | Mardu（玛尔都） | Alesha, Who Smiles at Death |
| {G}{U}{R} | Temur（铁木尔） | Omnath, Locus of the Roil |
| 四色 | — | Thrasios + Tymna（伙伴）|
| 五色 | — | Golos, Tireless Pilgrim |

## 颜色认同的特殊情况

### 面牌（DFC / Modal DFC）

双面牌的颜色认同由**两面规则叙述中的所有法术力符号**共同决定。
- **Garruk Relentless**：正面 {3}{G}，背面起动式异能含 {B} → 颜色认同绿黑
- **Extus, Oriq Overlord**：正面 {W}{B}，背面咒术含 {B}{B}{R} → 颜色认同白黑红

### 指挥官的替代性费用

如果指挥官有异能允许以其他方式施放（如 Evoke、Overload），这些异能中的法术力符号**也计入**指挥官的颜色认同。

## 相关页面

- [[commander|指挥官]]
- [[cedh|cEDH]]
- [[color|颜色]]
- [[mana|法术力]]
- [[mtg-formats|万智牌赛制]]
- [[comprehensive-rules|完整规则]]
