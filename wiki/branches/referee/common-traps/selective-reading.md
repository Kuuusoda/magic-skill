---
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [common_trap, mtr, reading_comprehension, selective_blindness]
sources: []
---

# 陷阱：条文阅读不完整（选择性忽略关键词）

## 现象

虽然从本地文件检索了原文，但只关注了自己预期会看到的内容，忽略了条文中的**限定词、例外条款或修饰语**。

## 典型案例

**题目**：竞争级别轮抽中，将已抽取的牌分成两堆放在面前是否被允许？

**错误答案**：被允许。MTR 7.7 只禁止"查看"选中的牌，没有禁止分堆。

**正确答案**：不被允许。

**检索到的原文**（MTR 7.7）:
> "Once a player has removed a card from the pack and put it on top of their **single**, front face-down drafted pile, it is considered selected and may not be returned to the pack."

**被忽略的限定词**：**single**

- "single" 明确限定已选牌堆只能是**一堆**。
- 分成两堆直接违反此限定，即使牌面朝下、不看内容。

## 为什么会发生

1. **先入为主**：心里预设"这道题考的是看牌规则"，于是只读了"may not look at their drafted cards"部分。
2. **跳读**：看到熟悉的关键词后就停止继续分析，漏掉了紧邻的限定词。
3. **过度泛化**：将"没有明确禁止"等同于"允许"，忽略了条文通过正面限定（"single pile"）已经隐含了禁止。

## 强制检索检查点

阅读规则条文时，必须逐词确认以下要素：

| 要素 | 检查方法 | 示例 |
|------|---------|------|
| 数量限定 | 注意 "single/a/an/one/all/any number" 等 | single pile = 只能一堆 |
| 时机限定 | 注意 "during/between/before/after/at" 等 | between or during picks |
| 范围限定 | 注意 "you control/they control/opponent's" 等 | your own sideboard |
| 例外条款 | 注意 "except/if/unless" 引导的从句 | except double-faced cards |
| 否定/禁止 | 注意 "may not/cannot/must not" 等 | may not be returned |

## 修正方法

每次读取规则条文后，强制执行以下步骤：

1. **抄写关键句**：将决定答案的那一句完整抄写出来（不要只抄片段）。
2. **圈限定词**：在抄写的句子中，把所有数量词、时机词、例外词标记出来。
3. **反向验证**：如果答案选X，检查条文中是否有任何词与X矛盾。

## 与其他陷阱的区别

| 陷阱类型 | 表现 | 解决方法 |
|---------|------|---------|
| **过时规则记忆** | 凭记忆引用，未查本地文件 | 强制从 `raw/` 检索 |
| **选择性忽略** | 查了文件，但漏看关键词 | 强制逐词分析，抄写完整句子 |
