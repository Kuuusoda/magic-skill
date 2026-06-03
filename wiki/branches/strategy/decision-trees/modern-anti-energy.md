---
created: 2026-05-01
updated: 2026-05-01
type: decision-tree
tags: [modern, anti-energy, boros-energy, decision-tree, matchup-guide]
sources: [output/modern_tournament_breaker.html]
---

# 对抗 Boros Energy 决策树

## 识别条件

以下任一情况触发此决策树：
- 你预计赛事中 Boros Energy 占比超过 15%
- 你的套牌对 Energy 胜率低于 45%
- 你想专门针对 Energy 调整主牌或备牌
- 你是 Energy 玩家，想了解对手可能如何针对你

## 关键数据

- Energy Meta 占比：16.8%（当前最高）
- Energy 整体胜率：53.2%
- Energy 弱点：对组合技（Neoform 24% 胜率）、怕坟场 hate（对 Living End 42%）、怕地干扰（对 Amulet 胜率低）

## 决策路径

### 路径一：选择反制套牌

1. **你想用什么维度击败 Energy？**
   - **"比它更快"** → 选择 **Neoform（对 Energy 76% 胜率）**
     - 原理：Energy 的交互集中在 T2-T3，T2 组合技在其反应窗口之前完成
     - 风险：极度依赖组合技保护，需熟练掌握 T2 回合的施放顺序
     - 备牌关键：Orim's Chant、Pact of Negation 防对手互动
   - **"破坏其地基础"** → 选择 **Amulet Titan（对 Energy 58% 胜率）**
     - 原理：Blood Moon 锁死 Energy 的双色地体系，Primeval Titan 的站场压力 Energy 难以处理
     - 风险：操作复杂，Titan 被去除后翻盘困难
     - 备牌关键：Blood Moon 3 张、Damping Sphere 2 张
   - **"坟场维度绕开其去除"** → 选择 **Living End（对 Energy 45% 胜率）**
     - 原理：Energy 缺少坟场 hate 主牌，Living End 的循环体系不受 Energy 的去除影响
     - 风险：Energy 备牌可换入 Grafdigger's Cage / Surgical Extraction
     - 备牌关键：Force of Vigor（去除 Cage）、Subtlety（干扰对手节奏）
   - **"比它更有价值"** → 选择 **Jeskai Blink（对 Energy 38% 胜率，不推荐）**
     - 原理：Blink 的价值引擎理论上能超越 Energy，但数据不支持
     - 现实：Energy 的 Guide of Souls + Ocelot Pride 展开速度超过 Blink 的价值积累速度

### 路径二：在同一维度击败 Energy（如果你已选择非反制套牌）

2. **你是什么套牌原型？**
   - **快攻/铺场（Affinity / Domain Aggro）** → 比拼展开速度
     - Energy 的 Wrath of the Skies 是你的最大威胁
     - 策略：铺得更宽（避免被 1 张扫场清完），保留资源防扫场
     - 备牌：换入 Haywire Mite（去除 Guide of Souls）、Wear//Tear（去除能量指示物来源）
   - **中速/控制（Esper Reanimator / Jeskai Blink）** → 争夺场面 + 干扰地基础
     - Energy 怕 Blood Moon，如果你有白/红，换入 2-3 张
     - 优先去除 Ocelot Pride（ Energy 的资源引擎）
     - 备牌：Surgical Extraction（拔除 Guide of Souls）、Wrath of the Skies（如果你有能量体系）
   - **组合技（Storm / Belcher）** → 速度竞赛
     - Energy 的 T2-T3 互动有限，争取在其建立场面之前完成组合技
     - 备牌：Veil of Summer（防白色去除）、Orim's Chant（锁 Energy 的干扰回合）
   - **大法术力（Eldrazi Tron）** → 大生物碾压
     - Energy 缺少处理 T3 Thought-Knot Seer 或 Reality Smasher 的高效手段
     - 风险：Energy 的速攻可能在 Tron 完成前结束游戏
     - 备牌：Chalice of the Void（锁 1 费咒语，打击 Energy 的 1 费生物曲线）

### 路径三：备牌局具体换牌方案

3. **对手是 Boros Energy，备牌局你该如何换牌？**
   - **有白/红色源** → 换入 Celestial Purge（去除 Guide of Souls / Ocelot Pride）+ Wear//Tear（去除能量指示物永久物）
   - **有蓝色源** → 换入 Consign to Memory（反击 Energy 的关键咒语）+ Spell Pierce（T2 干扰）
   - **有黑色源** → 换入 Thoughtseize（T1 去除 Energy 的最优曲线）+ Collective Brutality（多维度干扰）
   - **无色套牌** → 换入 Damping Sphere（降低 Energy 的爆发法术力）+ Grafdigger's Cage（如果 Energy 有 Graveyard 维度）

### 路径四：作为 Energy 玩家的自我保护

4. **你是 Energy 玩家，对手可能在针对你，你该如何应对？**
   - **预期对手有大量扫场** → 备牌局保留部分 threats 在手上，不要一次出完；换入更多 threats（如 Scurry Oak）减少依赖单一大生物
   - **预期对手有 Blood Moon** → 调整地基础：增加基本地数量，减少非基本地依赖；备牌局优先出基本地
   - **预期对手有组合技** → 主牌保持 2-3 张互动（如 Wear//Tear 或 Celestial Purge），备牌换入 Consign to Memory 或 Orim's Chant
   - **预期对手有坟场策略** → 备牌携带 2 Grafdigger's Cage 或 2 Surgical Extraction

## Energy 核心机制拆解

### Energy 的资源引擎

| 组件 | 功能 | 优先级 |
|------|------|--------|
| Guide of Souls | T2 产能量 + 抽牌 | **最高** — 去除第一目标 |
| Ocelot Pride | T1 铺场 + 持续威胁 | **高** — 防其 T2 展开 |
| Wrath of the Skies | 扫场 + 终结 | **高** — 如果你是铺场套牌需防 |
| Scurry Oak | 无限 combo 终结 | **中** — 仅在对手有能量储备时危险 |

### Energy 的典型展开时间线

- T1: 基本地 → Ocelot Pride（如有）
- T2: 第二块地 → Guide of Souls（产能量，抽牌）
- T3: 能量爆发 → Scurry Oak 或 多个 threats
- T4: Wrath of the Skies 清场或直接终结

**关键窗口**：T2 的 Guide of Souls 是 Energy 的转折点。如果 T2 能去除 Guide of Souls，Energy 的节奏会被严重拖延。

## 常见陷阱

- **陷阱**："带满 4 张 Blood Moon 就能赢 Energy"
  → **正确理解**：Blood Moon 确实对 Energy 有效，但它也会锁你自己的 fetch 地。而且 Energy 可以调整地基础增加基本地。Blood Moon 是"拖延"而非"终结"，你需要在 Blood Moon 生效的窗口内完成自己的游戏计划。

- **陷阱**："Neoform 对 Energy 76% 胜率，所以我选 Neoform"
  → **正确理解**：76% 胜率的数据基于特定样本。Neoform 的胜率方差极大——T2 成功=赢，被干扰=输。如果你不熟悉 Neoform 的所有分支对局和施放顺序，实际胜率会远低于 76%。

- **陷阱**："Energy 是快攻，所以我用控制套牌克制它"
  → **正确理解**：Energy 不是纯快攻，它是"中速+资源引擎"。纯控制套牌（如传统 UW Control）反而会被 Energy 的资源积累拖垮。对 Energy 最有效的不是"控制"而是"速度碾压"或"维度绕开"。

- **陷阱**："G1 输给 Energy，G2 我把所有针对牌都换入"
  → **正确理解**：过度换牌会破坏你自己的游戏计划。对 Energy 的备牌应聚焦在 3-5 张最高效的单卡上，而不是试图用备牌"完全重写"对局策略。

## 关联页面

- [[modern-meta-selection|摩登 Meta 套牌选择决策树]]
- [[modern-sideboard|摩登备牌决策树]]
- [[../decks/boros-energy|Boros Energy 套牌分析]]
- [[../meta-snapshots/2026-05-01-modern|2026-05 摩登环境快照]]
