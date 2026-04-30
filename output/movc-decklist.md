# MTGO Vintage Cube 限制策略分析报告

> 数据来源：`wiki/sources/MTGOVintageCube.txt`
> 分析范围：MTGO Vintage Cube 牌池（542 张单卡）
> 分析日期：2026-04-29

## 概述

Vintage Cube 是万智牌中历史最悠久、强度最高的轮抽赛制之一。其牌池基于特选（Vintage）可用的最大牌池——包括几乎所有万智牌历史上印刷的强力单卡。与普通限制赛不同，Vintage Cube 遵循 **Singleton 规则**：每张牌在牌池中只有 1 份，套牌构组时也最多放 1 张。

---

## 一、环境特征分析

### 1.1 牌池结构

从 542 张单卡分析，牌池可分为以下几类：

| 类别 | 代表单卡 | 张数估计 |
|------|----------|----------|
| **Power（Power Nine + 其他强力神器）** | Black Lotus、Mox、Time Walk、Ancestral Recall | ~15 |
| **顶级旅法** | Jace the Mind Sculptor、Liliana of the Veil、Chandra Torch of Defiance | ~20 |
| **组合技核心** | Doomsday、Tinker、Show and Tell、Survival of the Fittest | ~30 |
| **优质去除** | Swords to Plowshares、Lightning Bolt、Force of Will | ~50 |
| **加速资源** | Birds of Paradise、Bazaar of Baghdad、Mishra's Workshop | ~40 |
| **生物引擎** | Tarmogoyf、Griselbrand、Ledger Shredder | ~80 |
| **法术力地** | Dual Lands、Fetch Lands、Ancient Tomb、Gaea's Cradle | ~60 |
| **填充物** | 各类中等质量生物和咒语 | ~250 |

### 1.2 颜色强度分布

| 颜色 | 核心牌 | 强度评级 |
|------|--------|----------|
| **蓝** | Ancestral Recall、Brainstorm、Force of Will、Time Walk、Jace | ★★★★★ |
| **黑** | Demonic Tutor、Vampiric Tutor、Reanimate、Grief | ★★★★★ |
| **红** | Lightning Bolt、Wheel of Fortune、Chandra、ragavan | ★★★★☆ |
| **绿** | Survival of the Fittest、Birds of Paradise、Tarmogoyf | ★★★★☆ |
| **白** | Swords to Plowshares、Ephemerate、Solitude | ★★★☆☆ |
| **无色** | Mishra's Workshop、Urza's Saga、The One Ring | ★★★★☆ |

---

## 二、核心套牌原型

### 2.1 蓝黑控制/组合技

**核心组件**：
- 加速：Mox（任意色）、Lion's Eye Diamond、Chrome Mox
- 抓牌：Ancestral Recall、Brainstorm、Ponder、Preordain
- 干扰：Force of Will、Mana Drain、Spell Pierce
- 组合技：Doomsday + Thassa's Oracle、Tinker + Blightsteel Colossus
- 旅法：Jace the Mind Sculptor

**轮抽策略**：第一包优先抓 Ancestral Recall 或 Mana Drain。如果看到 Jace，毫不犹豫。第一包后半段如果看到 Doomsday 或 Tinker，开始构建组合技思路。

### 2.2 绿蓝加速组合技（Oath 路线）

**核心组件**：
- 加速：Birds of Paradise、Noble Hierarch、Delighted Halfling
- 组合技引擎：Oath of Druids、Survival of the Fittest
- 终结者：Griselbrand、Archon of Cruelty、Emrakul the Aeons Torn
- 旅法：Nissa Who Shakes the World

**轮抽策略**：抓 Oath of Druids 作为核心引擎，配合 Survival 和绿色加速。如果抓不到 Oath，可以走 Survival + Griselbrand 的 Reanimate 路线。

### 2.3 红色烧牌/攻击套牌

**核心组件**：
- 烧牌：Lightning Bolt、Chain Lightning、Lightning Greaves
- 加速：Goblin Bombardment、Orcish Lumberjack
- 威胁：Ragavan Nimble Pilferer、Glorybringer、Goldspan Dragon
- 旅法：Chandra Torch of Defiance

**轮抽策略**：红色是典型的"快攻+烧"思路。第一包抓 Lightning Bolt 或 Ragavan。中期用烧牌去除阻挡者，用 Chandra 终结对局。

### 2.4 MUD（神器高速）

**核心组件**：
- 加速：Mishra's Workshop、Mox、Lion's Eye Diamond、Lotus Petal
- 锁场：Trinket Mage、Mishra's Bauble、Phyrexian Metamorph
- 终结：Karn Scion of Urza、Urza Lord High Artificer、The One Ring

**轮抽策略**：第一包优先抓 Workshop 或 Mox。中期收集artifact加速组件，后期用 Karn 或 Urza 终结。

---

## 三、关键单卡分析（Top 20）

### 1. Black Lotus（黑莲花）
**费用**：{0} **类型**：神器
> 牺牲它，加三点任意颜色的法术力。

史上最强单卡，没有之一。任何轮抽到它的思路都应该围绕最大化其价值构建——无论是加速出旅法还是配合 Mox 打出一回合统治。

### 2. Ancestral Recall（先人的召还）
**费用**：{U} **类型**：瞬间
> 抓三张牌。

限制牌表成员。蓝黑控制或组合技思路的第一抓。1 费抓三张在任何思路中都是绝对核心。

### 3. Time Walk（时间行走）
**费用**：{1}{U}{U} **类型**：法术
> 额外回合。

限制牌表成员。在 Cube 中能与 Mox 配合打出"一回合 T4 出旅法 T5 再动"的统治力。

### 4. Jace, the Mind Sculptor
**费用**：{2}{U}{U} **类型**：鹏洛客 - Jace
> +2 控心 / -1 洗牌 / -9 获胜

特选最强旅法之一。在 Cube 中几乎无解——+2 持续抓牌，-1 可以控顶或去除旅法，-9 几乎直接获胜。

### 5. Liliana of the Veil
**费用**：{1}{B}{B} **类型**：鹏洛客 - Liliana
> +1 弃牌 / -2 牺牲 / -6 产生 2/2 僵尸

控制黑色套牌的核心旅法。-2 的牺牲异能在组合技和配合套牌中极强。

### 6. Demonic Tutor（恶魔导随）
**费用**：{1}{B} **类型**：法术
> 抓一张牌。

限制牌表成员。任意黑色思路的第一抓。配合 Doomsday 或其他组合技组件效率极高。

### 7. Force of Will（强行借力）
**费用**：{3}{U}{U} **类型**：瞬间
> 反击一个咒语。你弃一张非地牌。

蓝色的标志性反击咒语。在 Cube 高强度环境中几乎必带——可以反击组合技、Tinker、Show and Tell 等关键咒语。

### 8. Mishra's Workshop（米斯拉工作室）
**费用**：— **类型**：地（神器）
> 横置产任意量 {C}。

MUD 套牌的核心。如果轮抽到 Workshop，围绕它构建神器加速思路是最高效的策略。

### 9. Survival of the Fittest（残物存活）
**费用**：{1}{B}{G} **类型**：法术
> 弃一张牌，抓一张生物牌。

绿色最强检索咒语。可以将无用手牌转换为生物牌，或将特定生物送入坟场配合 Reanimate。

### 10. Doomsday（末日）
**费用**：{B}{B}{B} **类型**：法术
> 堆叠牌库顶五张牌。以此法堆叠的牌描述一个组合技。

蓝色组合技的核心终结手段。配合 Thassa's Oracle 或 Laboratory Maniac 可以直接获胜。

### 11. Tinker（发明）
**费用**：{1}{U} **类型**：法术
> 牺牲一个神器，抓一张牌，然后展示你手牌中一张 artifact 或一张生物牌，将一张 5/5 artifact 生物或一张artifact creature 倒模进战场。

配合 Blightsteel Colossus 或 Phyrexian Metamorph 直接获胜。

### 12. Birds of Paradise（天堂鸟）
**费用**：{G} **类型**：生物～鸟
> 飞行；横置产任意量 {G}。

绿色加速的标准。1 费加速让绿色思路能在 T2-T3 做出关键动作。

### 13. Swords to Plowshares（剑到梨）
**费用**：{W} **类型**：瞬间
> 消灭一个目标生物。目标牌手获得等量生命。

白色最强去除。几乎任何白色思路的第一抓。

### 14. Lightning Bolt（闪电击）
**费用**：{R} **类型**：瞬间
> Lightning Bolt 对任意目标造成 3 点伤害。

红色去除的标准。3 点伤害能去除 Cube 中大部分生物，且费用极低。

### 15. Wheel of Fortune（命运之轮）
**费用**：{2}{R} **类型**：法术
> 每位牌手弃掉其手牌，然后抓七张牌。

红色标志性过牌咒语。配合 Wasteboard 或 Demonic Tutor 可以造成对手资源枯竭。

### 16. Show and Tell（展示与述说）
**费用**：{2}{U} **类型**：法术
> 每位牌手展示其手牌中一张永久物牌，然后将等量永久物各倒模进战场。

配合 Emrakul the Aeons Torn 可以一回合结束游戏。

### 17. Vampiric Tutor（吸血鬼导随）
**费用**：{B} **类型**：法术
> 抓一张牌。支付 2 点生命，否则将其放置到牌库顶。

限制牌表成员。灵活性极高的检索咒语。

### 18. Ledger Shredder
**费用**：{1}{U} **类型**：生物～海妖
> 飞行；每当一个对手抽第二张牌时，抓一张牌。

蓝色优质海妖。在 Cube 环境中能持续抓牌，配合蓝色抓牌咒语形成引擎。

### 19. Ragavan, Nimble Pilferer
**费用**：{R} **类型**：生物～猩红海盗
> 敏捷；每当 Ragavan 向一个牌手造成战斗伤害时，弃一张牌，抓一张牌，然后获得一张宝藏。

红色攻击套牌的核心。1 费敏捷生物能持续造成压力并过牌。

### 20. Urza's Saga
**费用**：**类型**：传奇超剑地
> 抓一张地；每回合产任意量 {C}。

无色套牌的核心。抓牌异能配合 artifact 可以制造强大的持续优势。

---

## 四、轮抽策略框架

### 4.1 第一包策略

```
优先级排序：

1. 【必抓】Power Nine（Black Lotus > Mox > Time Walk > Ancestral > Timetwister）
   ↓
2. 【极高优先级】顶级旅法
   - 蓝：Jace, the Mind Sculptor
   - 黑：Liliana of the Veil
   - 红：Chandra, Torch of Defiance
   - 绿：Nissa, Who Shakes the World
   ↓
3. 【高优先级】限制牌表成员
   - Demonic Tutor、Vampiric Tutor、Imperial Seal
   - Tinker、Show and Tell、Survival of the Fittest
   ↓
4. 【优先】优质加速（Mox、Birds of Paradise、Chrome Mox）
   ↓
5. 【参考】如果无明显强牌，选该颜色最强单卡
```

### 4.2 颜色选择决策树

```
第一包第一张抓到什么？
│
├─ Power Nine → 确定走对应颜色思路
│
├─ 顶级旅法 → 走对应颜色路线
│
├─ Tinker/Show and Tell → 蓝
│
├─ Survival of the Fittest → 绿
│
├─ Lightning Bolt → 红
│
├─ Swords to Plowshares → 白
│
└─ 无明显炸弹 → 抓双面地或中性强牌（Fetch Land、Baleful Strix）
```

### 4.3 信号判断

Cube 轮抽中，"信号"是指传递给邻居的牌透露的颜色信息：

| 信号类型 | 含义 | 应对策略 |
|----------|------|----------|
| 某颜色强牌被传下来 | 该颜色在传递方向上"开放" | 考虑进入该颜色 |
| 某颜色关键牌被传走 | 该颜色竞争激烈 | 避免进入该颜色 |
| 同色稀有地传下来 | 邻居可能在玩该颜色 | 谨慎进入该颜色 |

---

## 五、典型曲线与法术力

### 5.1 建议法术力曲线

| 费用 | 张数 | 示例单卡 |
|------|------|----------|
| 0 | 2-3 | Mox、Black Lotus、Lotus Petal |
| 1 | 4-5 | Birds of Paradise、Chrome Mox、Brainstorm |
| 2 | 6-8 | Ledger Shredder、Lightning Bolt、Force of Will |
| 3 | 5-7 | Jace the Mind Sculptor、Survival of the Fittest |
| 4 | 4-5 | Liliana of the Veil、Chandra Torch of Defiance |
| 5+ | 3-4 | Griselbrand、Emrakul、Archon of Cruelty |
| 地 | 17 | Dual Land、Fetch Land、Basic Land |

### 5.2 地类别分布（建议）

| 地类型 | 张数 | 作用 |
|--------|------|------|
| Fetch Land | 5-7 | 调整法术力、触发异能 |
| Dual Land | 4-6 | 稳定多色法术力 |
| Utility Land | 2-3 | Mishra's Workshop、Bazaar、Gaea's Cradle |
| Basic Land | 3-5 | 填充、防止卡地 |

---

## 六、常见陷阱

| 陷阱 | 描述 | 正确策略 |
|------|------|----------|
| **抓 Power 不建思路** | 抓了 Mox 但套牌缺少高费咒语 | Mox 必须配合 4-5 费咒语才有意义 |
| **过度追求组合技** | Doomsday + Oracle 需要 3 张牌配合 | 确保套牌有足够备份 plan |
| **忽视法术力曲线** | 太多高费咒语导致前期卡地 | 遵循 0-2 费 6-8 张的曲线原则 |
| **邻居颜色竞争** | 所有人都抓蓝黑核心 | 观察信号，必要时转向红绿加速 |
| **Singleton 误解** | 以为可以用 4 张同名牌 | 每张牌最多 1 张，这是 Cube 不是构筑 |

---

## 七、结论

Vintage Cube 是高强度的限制赛环境，需要玩家对万智牌历史有深刻理解。以下是关键要点：

1. **Power 优先**：Black Lotus 和 Mox 是任何思路的核心
2. **旅法为王**：Jace、Liliana、Chandra 是获胜的主要手段
3. **组合技要备份**：Doomsday、Tinker 等组合技需要备用方案
4. **法术力管理**：Cube 中"卡地"是致命的，确保曲线合理
5. **观察信号**：Cube 是 8 人轮抽，与邻居的颜色博弈至关重要

---

## 相关页面

- [[vintage|特选（Vintage）]] — 限牌列表与 Power Nine 介绍
- [[draft|轮抽（Draft）]] — 轮抽技巧与信号判断
- [[combo|组合技]] — 组合技原理与常见类型
- [[mana-curve|法术力曲线]] — 限制赛曲线管理