---
created: 2026-04-27
updated: 2026-04-27
type: decision-tree
tags: [mana_value, x_spell, cost, 202.3e]
sources: []
---

# X 咒语法力值与费用计算裁判决策树

## 识别条件

以下任一情况触发此决策树：
- 牌面 mana cost 包含 {X}
- 题目涉及 "X 等于 0 时 mana value 是多少"
- 题目涉及 X 咒语在战场/坟墓场/手牌中的 mana value
- 题目涉及 X 咒语的 counter/interaction（如 Spell Snare 反击 mana value = 2 的咒语）

## 检索路径（按优先级排序）

1. **CR 202.3e X 咒语法力值** → 核心规则
   - **不在堆叠上**（战场、坟墓场、手牌、牌库、放逐区）：**X = 0**
   - **在堆叠上**：**X = 施放时选择的数字**
   - mana value = X 值 + 其他有色/无色费用部分

2. **CR 601.2b 选择 X 值** → 确认 X 的选择时机
   - 在施放过程中，于宣告咒语和选择模式（如适用）之后选择 X 值
   - X 值的选择在确定总费用之前

3. **CR 107.3a X 的合法值**
   - X 可以是任何非负整数（0, 1, 2, ...）
   - 牌手宣告 X 值时即被锁定，后续不能更改

4. **CR 601.2f 总费用计算** → X 与费用增减的互动
   - 总费用 = mana cost（含 X） + 额外费用 + 费用增加 - 费用减少
   - X 值在费用计算前已确定，因此费用增减不影响 X 值本身，只影响总费用

## 常见陷阱

- **陷阱**: X=0 时 mana value 为 0
  → **正确理解**: mana value = X + 其他费用部分。X=0 时 mana value = 其他费用部分。例如 {X}{G}{G} 的牌，X=0 时 mana value = 2。

- **陷阱**: X 咒语在战场上的 mana value 等于最后施放时的 X 值
  → **正确理解**: 在战场上时 X = 0（CR 202.3e）。与最后施放时选择的 X 值无关。

- **陷阱**: 费用减少效应（如 Goblin Electromancer）会使 X 值减小
  → **正确理解**: X 值在费用计算前已确定，不受费用减少影响。费用减少只减少总费用中的非法术力部分（即 generic mana 部分）。

- **陷阱**: X 咒语被复制后，复制品的 X 值与原咒语不同
  → **正确理解**: 复制咒语时，复制品继承原咒语的所有选择，包括 X 值（CR 707.10）。

- **陷阱**: 选择 X=0 的 X 咒语可以被 Spell Snare（反击 mana value=2）反击
  → **正确理解**: 取决于 mana cost。{X}{G}{G} 且 X=0 时 mana value=2，可以被 Spell Snare 反击。{X}{U} 且 X=0 时 mana value=1，不能被 Spell Snare 反击。

## 测试验证

- **题目**: Nature's Rhythm 费用 {X}{G}{G}，X=0 时 mana value 是多少？
  → 期望检索: CR 202.3e
  → 期望结论: mana value = 0 + 2 = 2

- **题目**: Walking Ballista（费用 {X}{X}）在战场上的 mana value 是多少？
  → 期望检索: CR 202.3e
  → 期望结论: X=0，mana value = 0

## 关联概念
- [[Harmonize]]
- [[Flashback]]
- [[Mana Value]]
- [[Copy Effects]]
