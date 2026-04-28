---
created: 2026-04-27
updated: 2026-04-27
type: decision-tree
tags: [keyword_action, harmonize, graveyard, cast]
sources: []
---

# Harmonize 裁判决策树

## 识别条件

以下任一情况触发此决策树：
- 牌面包含 "Harmonize" 关键字动作
- 题目涉及从坟墓场支付替代费用施放咒语
- 题目涉及 "Then exile this spell" 且与坟墓场施放相关

## 检索路径（按优先级排序）

1. **CR 702.XXX Harmonize** → 确认 Harmonize 的正式规则定义
   - **关键确认点**：Harmonize 是否包含替代性放逐（"instead of putting it anywhere else any time it would leave the stack"）？
   - 如果包含 → 被反击的 Harmonize 咒语**也会被放逐**（与 Flashback 行为一致）
   - 如果不包含 → 被反击后进入坟墓场，正常结算后才放逐

2. **CR 118.8 替代性费用** → 确认替代性费用与额外费用的区别
   - Harmonize 是**替代性费用**（alternative cost），不是额外费用
   - 替代性费用可以被费用增加效应（如 Thalia）影响

3. **CR 601.2f 费用计算** → 确认费用增减顺序
   - 顺序：替代性费用 → 费用增加（Thalia 等）→ 费用减少（横置生物等）

4. **CR 202.3d X咒语法力值** → 确认 X 值与 mana value 的关系
   - X 咒语在堆叠上的 mana value = X 选择值 + 有色费用部分
   - X 咒语在战场上的 mana value = 0 + 有色费用部分

## 常见陷阱

- **陷阱**: "Then exile this spell" 看起来只在结算后放逐
  → **正确理解**: 必须查 CR 702.XXX 中 Harmonize 的正式规则定义。如果规则包含替代性放逐（类似 Flashback 的 702.34a），则被反击后也会被放逐。

- **陷阱**: "without paying its mana cost" 免除了所有费用
  → **正确理解**: 只免除 mana cost，不免除额外费用（如 Blight）或强制性额外费用

- **陷阱**: X=0 时 mana value 为 0
  → **正确理解**: X 咒语的 mana value = X + 有色费用部分。X=0 时 mana value = 有色费用部分的数量

## 测试验证

- **题目**: Nature's Rhythm (X)(G)(G)，Harmonize (X)(G)(G)(G)(G)。X=0 时 mana value 是多少？
  → 期望检索: CR 202.3d
  → 期望结论: mana value = 0 + 2 = 2

- **题目**: Harmonize 的牌被反击后会放逐吗？
  → 期望检索: CR 702.XXX Harmonize 规则定义
  → 期望结论: 取决于 Harmonize 是否包含替代性放逐规则

## 关联概念
- [[Flashback]]
- [[Escape]]
- [[Jump-Start]]
- [[Alternative Costs]]
