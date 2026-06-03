---
created: 2026-05-01
updated: 2026-05-01
type: decision-tree
tags: [modern, meta-selection, deck-choice, decision-tree]
sources: [output/modern_tournament_breaker.html]
---

# 摩登 Meta 套牌选择决策树

## 识别条件

以下任一情况触发此决策树：
- 你需要在摩登赛事前选择一套套牌
- 你不确定在当前 Meta 中该玩什么
- 你想根据对手的预期 Meta 选择反制套牌
- 你在多个套牌之间犹豫不决

## 决策路径（按优先级排序）

### 第一步：明确你的目标

1. **你的首要目标是？**
   - **"稳定拿分，不求冠军"** → 进入路径 A（稳健选择）
   - **"冲击冠军，接受风险"** → 进入路径 B（高上限选择）
   - **"偷环境，抓别人的备牌漏洞"** → 进入路径 C（反 Meta 选择）

### 路径 A：稳健选择（适合 Day 2 为目标）

2. **你对 Meta 的了解程度？**
   - **"熟悉当前环境"** → 选择 **Boros Energy（16.8%）**
     - 理由：整体胜率最高，对大多数对局有优势，操作门槛中等
     - 风险：镜像对局多，对组合技需精确备牌
     - 关键技能：掌握 Wrath of the Skies 的使用时机，备牌局识别组合技并换入 Consign to Memory + Orim's Chant
   - **"不太熟悉，想降低失误率"** → 选择 **Jeskai Blink（8.1%）**
     - 理由：对局稳定，失误率低，备牌空间充裕，每回合有明确的最优操作
     - 风险：对 Energy 胜率不足 40%，需大量备牌针对
     - 关键技能：掌握 Soulherder 的保护窗口，了解何时该激进闪烁 vs 保守站场

### 路径 B：高上限选择（适合冠军为目标）

3. **你愿意承担什么类型的风险？**
   - **"组合技速度碾压"** → 选择 **Neoform（2.4%）**
     - 理由：对 Energy 76% 胜率，对 Affinity 也优，上限极高
     - 风险：极度依赖备牌保护，被 Vexing Bauble 一卡锁死
     - 关键技能：熟练掌握 T2 组合技的每一条施放顺序，了解对手所有可能的干扰点
   - **"神器爆发铺场"** → 选择 **Affinity（10.2%）**
     - 理由：T1 铺满后 T2-T3 终结，速度极快，操作相对简单
     - 风险：极度依赖神器，被 Vexing Bauble / Wear//Tear 严重克制
     - 关键技能：掌握 0 费神器的最优铺场顺序，了解何时该激进展开 vs 保留资源防扫场
   - **"大法术力碾压"** → 选择 **Amulet Titan（4.4%）**
     - 理由：T2-T3 Primeval Titan 直接终结游戏，对控制套牌极优
     - 风险：怕组合技干扰和地破坏，操作复杂（地弹回顺序）
     - 关键技能：掌握 bounce 地的最优弹回顺序，计算每回合的法术力产出

### 路径 C：反 Meta 选择（适合预判对手备牌）

4. **你预判对手会大量携带什么备牌？**
   - **"Vexing Bauble 泛滥"** → 避开 Affinity / Neoform / Living End，选择 **Jeskai Blink** 或 **Esper Reanimator**
     - 理由：Blink 和 Reanimator 的游戏计划不依赖无费施放，Bauble 对它们影响有限
   - **"大量神器 hate"** → 避开 Affinity，选择 **Boros Energy** 或 **Domain Aggro**
     - 理由：Energy 和 Domain 不是纯神器套牌，神器 hate 的边际效用低
   - **"大量坟场 hate"** → 避开 Esper Reanimator / Living End，选择 **Boros Energy** 或 **Izzet Prowess**
     - 理由：Energy 和 Prowess 不依赖坟场，坟场 hate 对它们完全无效
   - **"缺乏针对"** → 选择 **Dimir Frog（2.1%）**
     - 理由：当前没有任何主流备牌能同时应对坟场+控制双维度，存在备牌真空
     - 数据支撑：Dimir Frog vs Energy 样本仅 12 场，但 Frog 对 Blink 胜率 62%

### 第二步：验证你的选择

5. **检查以下三个问题是否都为"是"**
   - 你对该套牌的换牌策略有清晰认识（至少知道对前 5 名套牌的主备牌换牌方案）
   - 你有至少 20 局该套牌的实战经验（或至少在模拟器上练过 50+ 局）
   - 你能熟练操作该套牌的"关键回合"（如 Neoform 的 T2 组合技、Titan 的地弹回顺序）
   - **任一答案为"否"** → 回到第一步，选择一个更熟悉或更简单的套牌
   - **全部为"是"** → 进入备牌决策树验证备牌配置

## 常见陷阱

- **陷阱**："Energy 占比最高，所以我必须玩 Energy"
  → **正确理解**：Energy 的高占比 = 高人气 ≠ 最高胜率。熟练玩家手中 Affinity（54.7%）和 Blink（55.1%）的胜率更高。选择套牌时应考虑你的操作水平，而非单纯看占比。

- **陷阱**："带满针对 Energy 的备牌就能赢 Energy"
  → **正确理解**：Energy 的备牌空间同样充裕，且它知道你是来针对它的。备牌博弈是对称的。真正有效的反制是选一套 Energy 不擅长应对的套牌（如 Neoform），而不是在同一维度上硬拼。

- **陷阱**："组合技上限高，所以比赛就该玩组合技"
  → **正确理解**：组合技（Neoform / Storm / Belcher）的胜率方差极大——T2 成功 = 赢，被干扰 = 直接输。在长时间赛事（Day 1 + Day 2）中，方差累积会导致"神一把鬼一把"。稳健套牌在长赛事中的期望值更高。

- **陷阱**："对手不知道我玩什么，所以我有信息优势"
  → **正确理解**：在大型赛事中，主流套牌的牌表是公开信息。你玩冷门套牌（如 Dimir Frog）确实有信息优势，但如果你自己也不熟悉该套牌的所有分支对局，信息优势会被操作失误抵消。

## 典型案例

- **案例 1**：你是一个时间有限的上班族，每周只能练 5 局。选择什么？
  → 路径 A → "不太熟悉" → Jeskai Blink。理由：操作线性，每回合有明确最优解，失误率低。

- **案例 2**：你预判本地赛事会有大量 Affinity（因为上周冠军是 Affinity）。选择什么？
  → 路径 C → "大量神器 hate" → Boros Energy。理由：Energy 的扫场（Wrath of the Skies）和能量机制对 Affinity 的 0 费铺场天然克制。

- **案例 3**：你是一个经验丰富的组合技玩家，目标是冲击 Pro Tour 资格。选择什么？
  → 路径 B → "组合技速度碾压" → Neoform。理由：对 Energy 76% 胜率是环境内最高上限，熟练后 Day 1 出轮概率极高。

- **案例 4**：你发现最近 Vexing Bauble 在环境中泛滥（超过 35% 携带率）。选择什么？
  → 路径 C → "Vexing Bauble 泛滥" → Esper Reanimator。理由：Reanimator 的坟场策略不触发 Bauble，且 Bauble 的泛滥会导致其他套牌减少神器 hate，反而让 Reanimator 的坟场维度更安全。

## 关联页面

- [[modern-sideboard|摩登备牌决策树]]
- [[modern-anti-energy|对抗 Boros Energy 决策树]]
- [[../decks/boros-energy|Boros Energy 套牌分析]]
- [[../decks/affinity|Affinity 套牌分析]]
- [[../decks/jeskai-blink|Jeskai Blink 套牌分析]]
- [[../meta-snapshots/2026-05-01-modern|2026-05 摩登环境快照]]
