---
created: 2026-04-27
updated: 2026-04-27
type: decision-tree
tags: [triggered_ability, 603.4, intervening_if, condition]
sources: []
---

# 介入性 If 子句裁判决策树

## 识别条件

以下任一情况触发此决策树：
- 触发式异能格式为 "When/Whenever/At [event], if [condition], [effect]"
- 题目涉及触发条件后的 "if" 子句
- 需要判断介入性 if 与 "If you do" / "When you do" 结构的区别
- 触发时条件为真，但结算时条件已改变

## 检索路径（按优先级排序）

1. **CR 603.4 介入性 If 定义** → 确认核心规则
   - **格式**: "When/Whenever/At [触发事件], if [条件], [效应]"
   - **触发时检查**: 触发事件发生时，检查条件是否为真。只有条件为真时才触发。
   - **结算时检查**: 异能结算时，再次检查条件。如果条件不再为真，异能被移出堆叠且没有任何效果。
   - **适用范围**: 只适用于**紧跟在触发条件之后**的 "if"。牌面其他位置的 "if" 只具有普通意义。

2. **CR 608.2a 结算时检查** → 确认结算阶段的行为
   - 结算时如果条件不符合，异能**被移出堆叠**
   - 这与检查合法目标的行为一致（mirrors the check for legal targets）

3. **区分 "介入性 if" 与 "条件效果"** → 避免混淆
   - **介入性 if**: 紧跟触发条件，控制触发和结算
   - **条件效果**: 出现在效应部分（如 "destroy target creature if it's tapped"），只在结算时判断，不影响触发

4. **区分 "介入性 if" 与 "When/If you do"** → 避免混淆
   - **介入性 if**: "When [event], if [condition], [effect]" — 条件在触发时和结算时各检查一次
   - **When you do**: "When [event], you may [do]. When you do, [effect]." — 见 [[Triggered Ability Structure]] 决策树（CR 603.12），创建延迟触发，不是介入性 if
   - **If you do**: 通常与 "you may" 搭配，创建延迟触发

## 常见陷阱

- **陷阱**: 介入性 if 只在触发时检查一次
  → **正确理解**: CR 603.4 明确说明触发时和结算时**各检查一次**。结算时条件不再满足则异能无效。

- **陷阱**: "When you do, if [condition]" 是介入性 if
  → **正确理解**: "When you do" 结构属于 CR 603.12（自身触发式异能），不是介入性 if。虽然语法上有 "if"，但它控制的是延迟触发的创建条件，不是 603.4 意义上的介入性 if。

- **陷阱**: 介入性 if 条件不满足时，异能仍然进入堆叠然后被反击
  → **正确理解**: 触发时条件不满足 → **根本不触发**，不会进入堆叠。结算时条件不满足 → 从堆叠移除，不是被"反击"。

- **陷阱**: 牌面中所有 "if" 都是介入性 if
  → **正确理解**: CR 603.4 明确说明只适用于**紧跟触发条件之后**的 "if"。效应部分的 "if"（如 "draw a card if you control a creature"）是普通条件，只在结算时判断。

- **陷阱**: 介入性 if 的触发事件发生后，即使条件变为假，异能仍会在堆叠上保留
  → **正确理解**: 如果条件在结算时变为假，异能**从堆叠移除**，不会继续结算。

## 测试验证

- **题目**: "At the beginning of your upkeep, if you control no creatures, draw a card." 牌手在维持开始时有生物，但响应中消灭了所有生物。异能触发了吗？结算时会抓牌吗？
  → 期望检索: CR 603.4
  → 期望结论: 不触发。触发时条件为假（有生物），异能根本不进入堆叠。

- **题目**: "Whenever a creature enters, if you control three or more creatures, draw a card." 第三个生物进场触发，但响应中一个生物被消灭。异能结算时会抓牌吗？
  → 期望检索: CR 603.4 + 608.2a
  → 期望结论: 不会。触发时条件为真（3个生物），但结算时只剩2个，条件为假，异能从堆叠移除。

## 关联概念
- [[Triggered Ability Structure]]
- [[Delayed Triggers]]
- [[Target Legality]]
