---
created: 2026-05-01
updated: 2026-05-01
type: decision-tree
tags: [modern, sideboard, decision-tree, boarding-guide]
sources: [output/modern_tournament_breaker.html]
---

# 摩登备牌决策树

## 识别条件

以下任一情况触发此决策树：
- 你需要为摩登套牌配置备牌
- 你不确定在特定对局中该换入/换出什么
- 你想理解备牌单卡在当前环境中的定位和取舍
- 对手换牌后，你不确定自己的游戏计划是否需要调整

## 决策路径

### 第一层：识别对手套牌原型

1. **对手是哪一类套牌？**

   | 套牌类型 | 典型代表 | 核心特征 |
   |----------|---------|---------|
   | **快攻/铺场** | Boros Energy, Affinity, Domain Aggro, Izzet Prowess | T1-T2 铺场，T3-T4 终结 |
   | **组合技** | Neoform, Amulet Titan, Ruby Storm, Belcher | T2-T3 组合技启动，一回合致胜 |
   | **中速/价值** | Jeskai Blink, Esper Reanimator | 价值交换，资源优势 |
   | **大法术力** | Eldrazi Tron, Eldrazi Ramp | 大生物碾压，Chalice 锁费 |
   | **坟场主题** | Living End, Dimir Frog, Grixis Reanimator | 坟场互动，循环/重返 |

### 第二层：根据对手类型选择备牌方向

#### 对快攻/铺场

2. **你是什么套牌？**
   - **你也是快攻** → 换入扫场 + 镜子去除
     - Boros Energy: 换入 3 Wrath of the Skies + 2 Celestial Purge（去除对方 Guide of Souls / Ocelot Pride）
     - Affinity: 换入 2 Dispatch + 2 Haywire Mite（处理对方大生物）
   - **你是中速/控制** → 换入扫场 + 生命增益 + 早期阻挡
     - Jeskai Blink: 换入 3 Wrath of the Skies + 2 Wear//Tear + 2 Blood Moon
     - Esper Reanimator: 换入 3 Wrath of the Skies + 2 Collective Brutality
   - **你是组合技** → 换入早期互动 + 拖延手段
     - Amulet Titan: 换入 2 Force of Vigor + 2 Endurance
     - Ruby Storm: 换入 2 Aether Gust + 2 Fury

#### 对组合技

3. **组合技的速度层级？**
   - **T2 组合技（Neoform / Belcher）** → 换入回合锁定 + 坟场去除 + 0 费互动
     - 有白: Orim's Chant, Hallowed Moonlight
     - 有蓝: Consign to Memory, Flusterstorm, Spell Pierce
     - 有黑: Surgical Extraction, Thoughtseize
     - 无色: Vexing Bauble, Damping Sphere, Grafdigger's Cage
   - **T3 组合技（Amulet Titan / Storm）** → 换入干扰 + 减费破坏
     - Amulet: Consign to Memory（反击 Titan 进场触发）, Damping Sphere（锁法术力翻倍）, Blood Moon（锁地）
     - Storm: Damping Sphere（每咒语多 1 费）, Vexing Bauble（锁无费施放）, Orim's Chant（锁回合）

#### 对中速/价值

4. **对手的价值来源？**
   - **闪烁价值（Jeskai Blink）** → 换入去除 + 地干扰 + 牌面封锁
     - Blood Moon（锁 Jeskai 三色地）, Vexing Bauble（锁闪烁的免费部分）, Wear//Tear（去除 Soulherder）
   - **坟场价值（Esper Reanimator）** → 换入坟场 hate + 手牌干扰
     - Surgical Extraction（拔除 Atraxa / Unburial Rites）, Grafdigger's Cage（封锁坟场重返）, Leyline of the Void
   - **奥札奇价值（Eldrazi Tron）** → 换入地干扰 + 神器去除 + 快速威胁
     - Blood Moon（锁 Tron 地）, Wear//Tear（去除 Chalice）, Damping Sphere（锁法术力翻倍）

#### 对大法术力

5. **对手的大法术力来源？**
   - **Tron 地（Eldrazi Tron）** → 地干扰是最高优先级
     - Blood Moon（第一优先级）, Damping Sphere（第二优先级）, Field of Ruin
   - **Amulet 加速（Amulet Titan）** → 干扰加速 + 反击 Titan
     - Consign to Memory（反击 Titan 触发）, Vexing Bauble（锁 Summoner's Pact）, Blood Moon

### 第三层：验证换牌后的游戏计划

6. **换牌后检查清单**
   - [ ] 你的换牌是否让某个对局从"劣势"变成"均势"或"优势"？
   - [ ] 换牌后你的地基础是否仍然稳定？（尤其是换入 Blood Moon 后）
   - [ ] 换牌后你是否仍然有明确的获胜路径？（不要换入太多互动而失去终结能力）
   - [ ] 对手可能换入什么针对你？（换牌是对称博弈）

### 第四层：备牌局策略调整

7. **游戏计划是否需要转变？**
   - **从"展开者"转为"锁死者"**：Boros Energy 对阵 Neoform 时，换入 Consign to Memory + Orim's Chant，不再追求场面优势，而是锁死对手组合技回合
   - **从"价值交换"转为"快速终结"**：Jeskai Blink 对阵控制套牌时，换出部分去除，换入更多威胁，争取在对手备牌生效前结束游戏
   - **从"组合技"转为"中速"**：Amulet Titan 对阵控制套牌时，换出部分组合技组件，换入更多互动和威胁，利用 Primeval Titan 的站场压力获胜

## 常见陷阱

- **陷阱**："把备牌所有针对牌都换入"
  → **正确理解**：过度换牌会导致主牌计划瓦解。一般换入 4-6 张为宜，最多不超过 8 张。保留核心引擎，只换入边际收益最高的牌。

- **陷阱**："Blood Moon 对任何人都好"
  → **正确理解**：Blood Moon 也会锁你自己的 fetch 地/双色地。如果你的套牌依赖 fetch + shock 地基础（如 Jeskai Blink），换入 Blood Moon 可能导致自己卡色。只有在自己地基础以基本地为主时才应换入。

- **陷阱**："Vexing Bauble 对所有组合技都好"
  → **正确理解**：Bauble 只针对"无费施放"和"神器减费"。对手如果是正规施放的组合技（如 Amulet Titan 的 Summoner's Pact 是 1 费绿色法术），Bauble 完全无效。对 Titan 应换入 Consign to Memory 和 Damping Sphere。

- **陷阱**："对手的备牌和我无关"
  → **正确理解**：备牌博弈是对称的。对手知道你带什么，你也知道对手带什么。例如：对手是 Affinity，你换入 Wear//Tear，对手也会换入更多 threats（减少 0 费神器，增加 Kappa Cannoneer）。你的策略应随之调整。

- **陷阱**："G1 赢了，G2 不换牌"
  → **正确理解**：即使 G1 赢了，对手 G2 几乎肯定会换入针对你的备牌。如果你不换牌，可能面临对手的针对性策略（如 Energy G2 遇到对手的 Blood Moon）。至少换入 2-4 张应对对手备牌的牌。

## 备牌携带量决策

| 备牌单卡 | 携带量 | 理由 |
|----------|--------|------|
| Vexing Bauble | 2-3 | 针对多个原型，但超过 3 张边际效用递减 |
| Consign to Memory | 2-3 | 蓝牌专属，覆盖面广 |
| Wrath of the Skies | 2-3 | 仅限有能量的套牌，但对铺场套牌致命 |
| Surgical Extraction | 2 | 坟场套牌必带，但对非坟场套牌完全死卡 |
| Wear//Tear | 2 | 神器+结界双杀，但只能处理已结算的永久物 |
| Blood Moon | 2-3 | 惩罚多色基础，但也会伤自己 |
| Damping Sphere | 2-3 | 同时针对 Tron + 风暴，但对纯快攻无效 |
| Orim's Chant | 1-3 | 组合技克星，但对非组合技完全死卡 |
| Celestial Purge | 1-2 | 针对黑红永久物，覆盖面窄 |
| High Noon | 2 | 针对风暴和每回合多咒语套牌 |

## 关联页面

- [[modern-meta-selection|摩登 Meta 套牌选择决策树]]
- [[modern-anti-energy|对抗 Boros Energy 决策树]]
- [[../decks/boros-energy|Boros Energy 套牌分析]]
- [[../decks/affinity|Affinity 套牌分析]]
- [[../decks/jeskai-blink|Jeskai Blink 套牌分析]]
- [[../card-evaluations/modern-2026-05|2026-05 摩登单卡评估]]
