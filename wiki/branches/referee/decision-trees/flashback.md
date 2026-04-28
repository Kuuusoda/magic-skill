---
created: 2026-04-27
updated: 2026-04-27
type: decision-tree
tags: [keyword_action, flashback, graveyard, cast]
sources: []
---

# Flashback 裁判决策树

## 识别条件

以下任一情况触发此决策树：
- 牌面包含 "Flashback" 关键字动作
- 题目涉及从坟墓场支付替代费用施放咒语（瞬间/法术）
- 题目涉及 "exile this card instead of putting it anywhere else any time it would leave the stack"
- 需要对比 Flashback 与 Harmonize / Escape / Jump-Start 的差异

## 检索路径（按优先级排序）

1. **CR 702.34 Flashback** → 确认 Flashback 的正式规则定义
   - **关键确认点**：Flashback 仅出现在**瞬间或法术**上
   - 如果牌是**非瞬间/法术**（如地牌、神器、生物）→ 不能从坟墓场用 Flashback 施放
   - Flashback 的替代性放逐规则："exile this card instead of putting it anywhere else any time it would leave the stack"
   - 被反击、被清场、被移回手牌——任何离开堆叠的情况都会被放逐

2. **CR 702.34a 费用支付** → 确认替代性费用的计算
   - Flashback 费用是**替代性费用**（alternative cost），不是额外费用
   - 遵循 CR 601.2b 和 601.2f-h 的替代性费用规则
   - 费用增加效应（如 Thalia）会影响 Flashback 费用
   - 费用减少效应（如 Goblin Electromancer）会影响 Flashback 费用

3. **对比检索（如题目涉及多种坟场施放机制）**
   - Flashback vs Harmonize：Harmonize 可以横置生物减费，Flashback 不行
   - Flashback vs Escape：Escape 有额外放逐成本，Flashback 没有
   - Flashback vs Jump-Start：Jump-Start 需要弃牌，Flashback 不需要

## 常见陷阱

- **陷阱**: Flashback 的牌被反击后进入坟墓场
  → **正确理解**: CR 702.34a 明确包含替代性放逐。被反击后**放逐**，不进坟墓场。

- **陷阱**: 具有 Flashback 的牌可以从任何地方施放
  → **正确理解**: 只能从**坟墓场**施放。如果牌被移出坟墓场（如被放逐、被移回手牌），Flashback 异能不可用。

- **陷阱**: Flashback 费用可以部分支付
  → **正确理解**: Flashback 是替代性费用，必须完整支付（或受费用增减效应影响后的总额）。不能"支付一部分 mana cost + Flashback 费用"。

- **陷阱**: 复制 Flashback 咒语时，复制品也会被放逐
  → **正确理解**: 复制品不是"牌"（card），是堆叠上的咒语。复制品离开堆叠时消失，不适用 Flashback 的放逐规则。但原牌（如果有）仍遵循正常规则。

## 测试验证

- **题目**: Flashback 的咒语被反击后会放逐吗？
  → 期望检索: CR 702.34a
  → 期望结论: 会放逐。"instead of putting it anywhere else any time it would leave the stack"

- **题目**: 具有 Flashback 的生物牌能从坟墓场施放吗？
  → 期望检索: CR 702.34a 第一句
  → 期望结论: 不能。Flashback 仅出现在瞬间和法术上。

## 关联概念
- [[Harmonize]]
- [[Escape]]
- [[Jump-Start]]
- [[Alternative Costs]]
