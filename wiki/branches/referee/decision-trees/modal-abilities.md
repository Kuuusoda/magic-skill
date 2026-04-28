---
created: 2026-04-27
updated: 2026-04-27
type: decision-tree
tags: [mechanic, modal, triggered_ability, choose]
sources: []
---

# Modal Abilities 裁判决策树

## 识别条件

以下任一情况触发此决策树：
- 牌面包含 "Choose one —" 或类似格式
- 牌面包含 "choose one that hasn't been chosen this turn" 或类似限制
- 题目涉及"模式选择"、"选项"、"不能重复选择"
- 异能效果包含多个互斥选项

## 检索路径（按优先级排序）

1. **CR 700.2 Modal Spells and Abilities** → 确认 modal 的定义
   - **关键确认点**：什么格式算 modal？（标准格式为 "Choose one —" 前缀）
   - 如果异能**没有** "Choose one —" 前缀 → **不是** modal triggered ability
   - 模式选择限制（如 "that hasn't been chosen this turn"）属于效果内限制，不是 modal 本身的规则

2. **CR 601.2b（咒语）/ 603.3c（触发式异能）** → 确认模式选择时机
   - **Modal 咒语**: 模式选择是施放过程的一部分（601.2b），在选择目标**之前**做出
   - **Modal 触发式异能**: 模式选择是触发进入堆叠的一部分（603.3c），在进入堆叠时做出
   - **非 modal 触发**: 模式选择（如果存在）在异能**结算时**做出

3. **CR 700.2b** → 确认模式重复选择限制
   - "A player can't choose the same mode more than once for a modal spell or ability"
   - 牌面文字 "that hasn't been chosen this turn" 是**额外限制**，叠加在 700.2b 之上

## 常见陷阱

- **陷阱**: 看到 "choose one" 就认为是 modal ability
  → **正确理解**: 必须有 "Choose one —" 标准前缀格式才算 modal。如果只是效果中包含 "choose one" 而没有标准前缀，则不是 modal，选择时机在结算时。

- **陷阱**: Modal 触发式异能的选择时机在结算时
  → **正确理解**: Modal 触发式异能的选择时机在进入堆叠时（603.3c），不是结算时。这与非 modal 触发不同。

- **陷阱**: "that hasn't been chosen this turn" 是 modal 的规则
  → **正确理解**: 这是牌面文字添加的额外限制，不是 modal 机制本身的规则。Modal 本身的规则是 700.2b（不能重复选择同一模式一次以上）。

## 测试验证

- **题目**: Monument to Endurance 的触发是 modal 吗？选择时机是？
  → 期望检索: CR 700.2（modal 定义）+ 牌面 Oracle 确认是否有 "Choose one —" 前缀
  → 期望结论: 如果有 "Choose one —" 前缀 → 是 modal triggered ability → 选择时机在进入堆叠时

- **题目**: 非 modal 触发的 "choose one" 选择时机是？
  → 期望检索: CR 601.2c（非 modal 选择）
  → 期望结论: 在异能结算时做出选择

## 关联概念
- [[Triggered Abilities]]
- [[Mode Selection]]
- [[Stack Resolution]]
