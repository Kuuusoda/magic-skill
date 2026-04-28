---
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [万智牌, 组合技, 引擎牌, 指挥官, EDH, 无限]
sources: [EDHREC_Combos/]
---

# 组合技引擎牌（Combo Engine Cards）

## 定义

组合技引擎牌（Engine Card）是指在组合技体系中充当核心催化剂的牌。它们通常具有高效的资源转换能力——将一种资源（生物、法术力、牌库）转换为另一种更强大的资源。引擎牌的关键特征是**泛用性**：同一张引擎牌可以与多种不同的配合牌组合，形成多种不同的组合技。

在指挥官（EDH）环境中，引擎牌是组合技生态的基石。基于 EDHREC 49,646 个组合技的大数据分析，共识别出 6,258 张参与组合技的牌，其中约 32 张牌出现在 500 个以上的不同组合技中，构成真正的「引擎牌」阶层。

## 引擎牌分类

### 一、牺牲类引擎（Sacrifice Engines）

牺牲类引擎通过牺牲生物产生资源，是万智牌中最古老的组合技引擎类型之一。

#### 1. Ashnod's Altar（阿什诺德祭坛）

- **费用**：{3}
- **类型**：神器
- **异能**：牺牲一个生物：加 {2} 到你的法术力池。
- **EDHREC 组合数**：3,419（排名第一）
- **经典配合**：
  - + Reassembling Skeleton（重组骷髅）：支付 {2} 将骷髅从坟场移回战场，祭坛产 {2}，无限循环
  - + Gravecrawler（坟场匍尸）： gravecrawler 可从坟场施放，牺牲产 {2}，支付 {1}{B} 召回
  - + Pitiless Plunderer（无情掠夺者）：生物死去时产宝藏，每个宝藏可产任意颜色法术力
- **战略意义**：无色神器，任何颜色都可以使用，是组合技套牌最通用的引擎之一

#### 2. Phyrexian Altar（非瑞克西亚祭坛）

- **费用**：{3}
- **类型**：神器
- **异能**：牺牲一个生物：加一点任意颜色的法术力到你的法术力池。
- **EDHREC 组合数**：3,107（排名第二）
- **经典配合**：
  - + Gravecrawler + Diregraf Colossus（或任何 Zombie 类型来源）：无限有色法术力
  - + Reassembling Skeleton：无限有色法术力（骷髅需要 {2}{B} 召回，祭坛产 {1} 任意色，需要额外法术力支持）
- **与 Ashnod's Altar 对比**：产出有色法术力而非无色，在需要特定颜色法术力的组合技中更灵活

#### 3. Altar of Dementia（痴呆祭坛）

- **费用**：{2}
- **类型**：神器
- **异能**：牺牲一个生物：目标牌手磨等同于该生物力量的牌。
- **EDHREC 组合数**：1,190
- **经典配合**：
  - + Karmic Guide（卡米克向导）+ Saffi Eriksdotter：无限牺牲循环，磨空对手牌库
  - + 任何可以反复进场的生物：利用 ETB/LTB 循环直接获胜

#### 4. Viscera Seer（内脏占卜师）

- **费用**：{B}
- **类型**：生物 — 吸血鬼/巫师
- **异能**：{B}，牺牲一个生物：占卜 1。
- **EDHREC 组合数**：923
- **经典配合**：
  - + Melira, Sylvok Outcast：消除 -1/-1 指示物，配合 Persist 生物无限牺牲
  - + 任何「生物死去时」触发：低价启动费用使其成为最灵活的牺牲出口

#### 5. Goblin Bombardment（鬼怪炮轰）

- **费用**：{1}{R}
- **类型**：结界
- **异能**：牺牲一个生物：Goblin Bombardment 对目标生物或牌手造成 1 点伤害。
- **EDHREC 组合数**：916
- **经典配合**：
  - + Kiki-Jiki, Mirror Breaker + 任意生物：复制生物，牺牲原物造成伤害，无限伤害
  - + 任何无限生物来源：直接转化为无限伤害

#### 6. Carrion Feeder（食腐 feeders）

- **费用**：{B}
- **类型**：生物 — 僵尸
- **异能**：Carrion Feeder 进场时上面有一个 +1/+1 指示物。牺牲一个生物：在 Carrion Feeder 上放置一个 +1/+1 指示物。
- **EDHREC 组合数**：845
- **经典配合**：
  - + Gravecrawler：反复召唤和牺牲，无限 +1/+1 指示物
  - + Mikaeus, the Unhallowed：Persist 生物在 Carrion Feeder 上无限循环

### 二、法术力类引擎（Mana Engines）

#### 1. Krark-Clan Ironworks（克拉克族铁工所）

- **费用**：{4}
- **类型**：神器
- **异能**：牺牲一个神器：加 {2} 到你的法术力池。
- **EDHREC 组合数**：1,012
- **经典配合**：
  - + Scrap Trawler（废铁拖网船）+ 0 费神器（Mox Opal、Mana Crypt 等）：反复牺牲和回收，无限法术力
  - + Myr Retriever（秘耳回收员）：类似 Scrap Trawler 的回收循环
- **历史意义**：在摩登赛中一度被禁（2019 年），其在组合技中的效率极高

#### 2. Basalt Monolith（玄武岩巨石）

- **费用**：{3}
- **类型**：神器
- **异能**：{T}：加 {3} 到你的法术力池。Basalt Monolith 的起动式异能费用增加 {3}。
- **EDHREC 组合数**：极高
- **经典配合**：
  - + Rings of Brighthearth（亮火指环）：复制重置异能，反复产费
  - + Forsaken Monument（被遗忘的纪念碑）：巨石额外产 {2}，净赚法术力
  - + Kinnan, Bonder Prodigy：翻倍激活式法术力异能产出
- **特点**：本身不赚费，需要配合才能形成无限

#### 3. Hullbreaker Horror（破船恶兽）

- **费用**：{5}{U}{U}
- **类型**：生物 — 海怪/ horror
- **异能**：每当你施放一个瞬间或法术咒语时，选择一项——反击目标咒语；或将至多一个目标非地永久物移回其拥有者手上。
- **EDHREC 组合数**：极高（与 Sol Ring 的组合使用于 300,846 个套牌）
- **经典配合**：
  - + Sol Ring：施放 0 费或 1 费咒语，Horror 回手 Sol Ring，再次施放 Sol Ring，无限法术力
  - + Mana Vault：类似 Sol Ring 的配合
  - + 任何 0 费神器或低费瞬间
- **特点**：需要大量廉价咒语支持，在 EDH 中极为高效

#### 4. Sensei's Divining Top（尊师占卜陀螺）

- **费用**：{1}
- **类型**：神器
- **异能**：{1}：查看你牌库顶的三张牌，然后以任意顺序放回。{T}：抓一张牌，然后将 Sensei's Divining Top 置于你的牌库顶。
- **EDHREC 组合数**：794
- **经典配合**：
  - + Mystic Forge（神秘熔炉）+ Foundry Inspector（铸造厂监察员）：Forge 允许从牌库顶施放神器，Top 可以抓顶牌，配合 Inspector 减费无限施放
  - + Bolas's Citadel（波拉斯的巨座）：支付生命施放牌库顶牌，Top 可以控制牌库顶
- **特点**：不仅是组合技组件，也是优质的滤牌工具

### 三、触发类引擎（Trigger Engines）

#### 1. Pitiless Plunderer（无情掠夺者）

- **费用**：{3}{B}
- **类型**：生物 — 人类/海盗
- **异能**：每当另一个由你操控的非衍生物生物死去时，创建一个珍宝衍生物。
- **EDHREC 组合数**：1,058
- **经典配合**：
  - + Ashnod's Altar + Reassembling Skeleton：骷髅死去产珍宝，珍宝换 {2}，召回骷髅
  - + Gravecrawler + Carrion Feeder：坟场匍尸死去产珍宝，从坟场召回
- **特点**：将生物牺牲转化为法术力，是多色组合技套牌的关键引擎

#### 2. Animation Module（活化模块）

- **费用**：{1}
- **类型**：神器
- **异能**：每当你在一个由你操控的生物上放置一个或数个 +1/+1 指示物时，你可以支付 {1}。若你如此作，则创建一个 1/1 无色 伺服 衍生神器生物。
- **EDHREC 组合数**：1,004
- **经典配合**：
  - + Ashnod's Altar：牺牲 1/1 产 {2}，配合任何 +1/+1 来源无限循环
  - + 任何 +1/+1 指示物来源（如 Hardened Scales、Corpsejack Menace）

#### 3. Ghostly Flicker（鬼影闪烁）

- **费用**：{2}{U}
- **类型**：瞬间
- **异能**：闪现两个由你操控的非地永久物。然后将它们移回战场。
- **EDHREC 组合数**：770
- **经典配合**：
  - + Peregrine Drake（游隼龙）+ Archaeomancer（考古学家）：闪烁 Drake 产 {5}，闪烁 Archaeomancer 回手 Flicker，无限法术力
  - + 任何 ETB 产费的生物：反复触发进场异能

#### 4. Kodama of the East Tree（东树 Kodama）

- **费用**：{4}{G}{G}
- **类型**：传奇生物 — 精怪
- **异能**：每当你的一个永久物从你的手牌进入战场时，你可以将一张永久物牌从你的手上放进战场。
- **EDHREC 组合数**：760
- **经典配合**：
  - + Sakura-Tribe Scout（樱花部落斥候）或 Skyshroud Ranger：将地放进战场触发 Kodama，从手中放另一个地，反复循环
  - + 任何可以从坟场或手牌反复进场的永久物
- **特点**：绿色组合技的核心引擎，在 commander 中极受欢迎

#### 5. Intruder Alarm（入侵者警报）

- **费用**：{2}{U}
- **类型**：结界
- **异能**：每当一个生物进场时，重置所有生物。
- **EDHREC 组合数**：729
- **经典配合**：
  - + 任何可以横置产生法术力的生物（如 Heritage Druid、Bloom Tender）：生物进场重置所有生物，再次横置产费
  - + 任何可以反复召唤的生物来源
- **特点**：重置所有生物的能力在组合技中极其强大

### 四、生物类引擎（Creature Engines）

#### 1. Mikaeus, the Unhallowed（不洁者米凯厄斯）

- **费用**：{3}{B}{B}{B}
- **类型**：传奇生物 — 灵/牧师
- **异能**：由你操控的非人类生物获得+1/+1和不灭。每当一个由你操控的非人类生物死去时，将它在其拥有者的操控下横置移回战场。其上有一个-1/-1指示物。
- **EDHREC 组合数**：531
- **经典配合**：
  - + Triskelion（三臂机）：Triskelion 移去指示物对自己造成 3 点伤害，死去后 Mikaeus 将其带回，移去 -1/-1 指示物，无限伤害
  - + Ashnod's Altar / Phyrexian Altar + 任何非人类生物：无限牺牲循环
- **特点**：提供不灭和 Persist 效果，是黑绿组合技套牌的核心

#### 2. Dualcaster Mage（双身法师）

- **费用**：{1}{R}{R}
- **类型**：生物 — 人类/巫师
- **异能**：闪现。当 Dualcaster Mage 进场时，复制目标瞬间或法术咒语。你可以为复制品选择新的目标。
- **EDHREC 组合数**：极高
- **经典配合**：
  - + Twinflame（双生火焰）：复制 Twinflame，目标指向自己，制造无限个具有敏捷的 Dualcaster Mage
  - + Molten Duplication（熔融复制）：类似 Twinflame 的配合
- **特点**：经典的「复制自己」组合技，红蓝套牌的最爱

#### 3. Springheart Nantuko（春心楠图库）

- **费用**：{1}{G}
- **类型**：生物 — 昆虫/德鲁伊
- **异能**：地落——每当你将一个地放进战场时，你可以从手上放置一个地。如果你如此做，则创建两个 1/1 昆虫 衍生生物。
- **EDHREC 组合数**：658
- **经典配合**：
  - + Tireless Provisioner（不知疲倦的供给者）：地落产宝藏，放置额外地产更多宝藏
  - + Lotus Cobra（莲花眼镜蛇）：地落产任意颜色法术力
- **特点**：在摩登新禁牌环境中崛起的组合技引擎

#### 4. Gravecrawler（坟场匍尸）

- **费用**：{B}
- **类型**：生物 — 僵尸
- **异能**：Gravecrawler 不能阻挡。你可以从你的坟墓场施放 Gravecrawler。
- **EDHREC 组合数**：极高
- **经典配合**：
  - + Phyrexian Altar / Ashnod's Altar：牺牲产费，从坟场召回
  - + Carrion Feeder：反复牺牲和召回，无限 +1/+1 指示物
  - + Rooftop Storm（屋顶风暴）：{0} 施放 Gravecrawler
- **特点**：只要坟场中有僵尸就可以无限召回，是黑色组合技的标志性组件

## 引擎牌的战略意义

### 为什么引擎牌如此重要

1. **模块化设计**：同一张引擎牌可以与多种不同的配合牌组合，提高套牌的一致性
2. **冗余性**：多个引擎牌提供相似的功能，降低被对手针对后无法获胜的风险
3. **资源效率**：引擎牌通常能将廉价的资源（如 1/1 衍生物）转化为无限的强大资源

### 引擎牌的限制与反制

| 反制手段 | 针对引擎 | 示例牌 |
|---------|---------|--------|
| 神器去除 | Ashnod's Altar, Basalt Monolith | Nature's Claim, Vandalblast |
| 坟场针对 | Gravecrawler, Reassembling Skeleton | Rest in Peace, Leyline of the Void |
| 生物去除 | Viscera Seer, Carrion Feeder | Swords to Plowshares |
| 堆叠干扰 | Dualcaster Mage, Hullbreaker Horror | Counterspell, Stifle |
| 异能关闭 | Mikaeus, Kodama | Pithing Needle, Phyrexian Revoker |

## 相关页面

- [[combo|组合技]]
- [[cedh|cEDH]]
- [[commander|指挥官]]
- [[sacrifice|牺牲]]
- [[infinite-mana-combos|无限法术力组合技]]
- [[sources/2026-04-21-edhrec-combos|EDHREC 组合技数据库]]
