---
created: 2026-04-27
updated: 2026-04-27
type: decision-tree
tags: [triggered_ability, delayed_trigger, when_you_do, 603]
sources: []
---

# Triggered Ability Structure 裁判决策树

## 识别条件

以下任一情况触发此决策树：
- 牌面包含 "Whenever... you may [do]. When you do, [effect]." 结构
- 牌面包含 "When/Whenever [event], you may [action]. If you do, [effect]."
- 题目涉及判断一个异能是"单一触发"还是"触发+延迟触发"
- 题目涉及 "When you do" / "If you do" 结构的反击/互动

## 检索路径（按优先级排序）

1. **CR 603.2 Triggered Abilities** → 确认触发式异能的基本定义
   - 触发事件发生时，异能进入堆叠

2. **CR 603.12 Delayed Triggered Abilities** → 确认延迟触发的定义
   - **关键确认点**: "When you do" / "If you do" 结构是否创建了**延迟触发**？
   - 标准结构: "Whenever [event], you may [do A]. When you do, [effect B]."
     - 第一部分 "Whenever [event]..." 是**触发式异能**（进入堆叠）
     - 当玩家选择 "do A" 时，创建了一个**延迟触发**: "When you do, [effect B]"（进入堆叠）
   - 这意味着存在**两个独立的触发事件**，可以分别被反击

3. **CR 603.4 Intervening If Clauses** → 区分 "When you do" 和介入性 if
   - 介入性 if: "When [event], if [condition], [effect]" — 条件在触发时检查
   - "When you do": 不是介入性 if，而是创建延迟触发的信号

4. **CR 603.10a Last Known Information** → 涉及离场触发时的对象追踪
   - 如果延迟触发的源永久物已离场，使用最后已知信息

## 常见陷阱

- **陷阱**: "Whenever... you may... When you do..." 是单一触发式异能
  → **正确理解**: 这是**一个触发式异能 + 一个延迟触发**。"When you do" 是独立的事件，会创建进入堆叠的延迟触发。可以分别被 Tishana's Tidebinder 等效应反击。

- **陷阱**: 反击了主触发，延迟触发仍然会发生
  → **正确理解**: 如果主触发（"Whenever..."）被反击，玩家没有机会 "do"，因此不会创建延迟触发。但如果主触发结算了（玩家选择 "do"），延迟触发已经创建，可以单独被反击。

- **陷阱**: "When you do" 和 "If you do" 效果相同
  → **正确理解**: 两者在规则上通常等效，都创建延迟触发。但 "may" 表示选择是可选的，不选择就不会创建延迟触发。

## 测试验证

- **题目**: Leatherhead "Whenever deals combat damage... you may remove a counter. When you do, destroy..." 是几个触发？
  → 期望检索: CR 603.12
  → 期望结论: 两个触发 — (1) 伤害触发 (2) "When you do" 延迟触发。可以分别被反击。

- **题目**: 如果 Tishana's Tidebinder 反击 Leatherhead 的伤害触发，延迟触发还会创建吗？
  → 期望检索: CR 603.12 + 113.7a
  → 期望结论: 不会。主触发被反击 → 不结算 → 玩家没有机会 remove counter → 不创建延迟触发。

## 关联概念
- [[Triggered Abilities]]
- [[Delayed Triggers]]
- [[Intervening If]]
- [[Countering Abilities]]
