---
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [common_trap, mtr, rule_update, sideboard, outdated_knowledge]
sources: []
---

# 陷阱：引用过时规则记忆（MTR 备牌查看权）

## 现象

裁判在回答问题时，凭记忆引用旧版MTR条文，未检索本地最新版本，导致答案错误。

## 典型案例

**题目**：牌手在一盘对局中能否查看自己的备牌？

**错误答案**：D. "除非有异能要求允许查看备牌，牌手在对局中不可以查看自己的备牌"
- 依据（过时）：旧版 MTR "Players may look at their sideboards during a game only if a card allows them to do so."

**正确答案**：B. "牌手可以随时查看自己的备牌"
- 依据（当前 MTR 3.16, 2026-02-27）："During a game, players may look at their own sideboard, keeping it clearly distinguishable from other cards at all times."

## 为什么会产生这个错误

1. **训练数据包含多个版本**：LLM 的训练数据中同时包含新旧版本的 MTR 条文。
2. **旧条文逻辑上"更严格"**：旧规则（必须某张牌允许）更符合直觉（备牌是隐藏信息），因此更容易被记忆优先提取。
3. **没有执行强制文件检索**：如果查了本地 `raw/mtr/chapter_3.md`，就能发现当前版本已修改。

## 强制检索检查点

遇到以下情形时，**必须**从 `raw/mtr/` 或 `raw/cr/` 本地文件检索，禁止凭记忆作答：

- 涉及牌手权利/限制的问题（能否看备牌、能否看坟场、能否切牌等）
- 涉及处罚等级的问题（警告/一盘负/DQ 的适用条件）
- 涉及比赛流程的问题（洗牌、换备、登记牌表等）

## 规则更新追踪建议

- 每次 MTR/IPG 更新时，将**修改过的条文**单独整理到 `wiki/branches/referee/common-traps/rule-changes/` 中。
- 重点关注：被删除的条文、被放宽的限制、新增的权利。
