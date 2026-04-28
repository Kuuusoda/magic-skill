# 强制深度检索机制测试报告

**测试日期**: 2026-04-27
**测试方法**: 模拟 agent 按新工作流（问题拆解 → 决策树检索 → 强制深度检索 → 验证清单 → 合规报告）回答三道历史错题

---

## 测试概览

| 题号 | 机制 | 测试文件答案 | 强制检索后正确答案 | 差异 |
|------|------|-------------|-------------------|------|
| 第9题 | Harmonize | 1、2、3 | **1、3** | 选项2错误 |
| 第11题 | 触发结构 603.12 | 1 | **1、2** | 遗漏选项2 |
| 第12题 | Modal 700.2 | 1 | **1、4** | 遗漏选项4 |

**结论**: 三道题的错误根源完全相同——**未执行强制深度检索，基于牌面文字快速推理**。

---

## 逐题详细分析

### 第9题 — Harmonize（Nature's Rhythm）

#### 测试文件的分析路径
- 基于牌面文字 "Then exile this spell" 推断
- 认为 Harmonize **没有** Flashback 式的替代性放逐规则
- 结论：被反击后进入坟墓场，选项2正确

#### 强制深度检索结果
**CR 702.180a** 正式定义：
> "Harmonize [cost]" means ... "If the harmonize cost was paid, **exile this card instead of putting it anywhere else any time it would leave the stack**."

#### 关键发现
- Harmonize 的 CR 定义明确包含 **替代性放逐规则**（"instead of putting it anywhere else any time it would leave the stack"）
- 这与 Flashback（702.34a）的行为**完全一致**
- **被反击的 Harmonize 咒语也会被放逐**
- 选项2（"被反击后不会被放逐"）→ **错误**

#### 正确答案
**1、3**

---

### 第11题 — 触发结构（Leatherhead）

#### 测试文件的分析路径
- 基于牌面文字结构推断
- 认为 "Whenever... you may... When you do..." 是**单一触发式异能**
- 结论：不存在独立的 "消灭" 触发，选项2错误

#### 强制深度检索结果
**CR 603.12** 正式定义：
> "A resolving spell or ability may allow or instruct a player to take an action and create a triggered ability that triggers 'when [a player] [does or doesn't] take that action' ... These **reflexive triggered abilities** follow the rules for delayed triggered abilities."

#### 关键发现
- "When you do" 结构创建的是**自身触发式异能**（reflexive triggered ability）
- 自身触发遵循延迟触发规则，是**独立的触发事件**
- 主触发结算后，自身触发进入堆叠，**可以被单独反击**
- 时序上：
  1. NAP 可以在主触发进入堆叠后立即施放 Tishana's Tidebinder → 反击主触发（选项1）
  2. NAP 也可以等主触发结算（创建自身触发）后再施放 → 反击自身触发（选项2）

#### 正确答案
**1、2**

---

### 第12题 — Modal（Monument to Endurance）

#### 测试文件的分析路径
- 基于牌面文字（非 Oracle）推断
- 认为 Monument to Endurance "没有使用 Choose one — 的标准分栏格式"
- 结论：不是 modal triggered ability，模式选择在结算时做出，选项4错误

#### 强制深度检索结果
**CR 700.2** 正式定义：
> "A spell or ability is modal if it has two or more options in a **bulleted list** preceded by instructions for a player to choose a number of those options, such as 'Choose one —.'"

**Monument to Endurance Oracle 文字**（经 Scryfall 确认）：
> "Whenever you discard a card, choose one that hasn't been chosen this turn —\n• Draw a card.\n• Create a Treasure token.\n• Each opponent loses 3 life."

#### 关键发现
- Oracle 文字明确使用 "choose one ... —" + 分栏列表（•）格式
- **符合 CR 700.2 的 modal 定义**
- 根据 **CR 700.2b**：modal triggered ability 的模式选择是"作为该异能进入堆叠的一部分"（as part of putting that ability on the stack）
- 选项4（"进入堆叠时就需要选择模式"）→ **正确**

#### 正确答案
**1、4**

---

## 错误模式总结

| 错误类型 | 出现次数 | 描述 |
|---------|---------|------|
| 未查关键字 CR 定义 | 3/3 | Harmonize 未查 702.180a，"When you do" 未查 603.12，Modal 未查 700.2 |
| 基于牌面文字推理 | 3/3 | 三道题均基于牌面（非 Oracle）文字做推断 |
| 遗漏正确选项 | 2/3 | 第11题遗漏选项2，第12题遗漏选项4 |
| 接受错误结论 | 1/3 | 第9题将错误选项2判定为正确 |

---

## 新工作流有效性验证

### 强制问题拆解 ✅
- 三题均可按机制维度拆出需要查的规则点
- Harmonize → 702.x；触发结构 → 603.12；Modal → 700.2

### 决策树检索 ✅
- 三个机制均有对应的决策树页面
- 决策树明确指向需要查的 CR 条文

### 强制深度检索 ✅
- 按决策树指引查 CR 后，发现测试文件答案错误
- 证明"未检索不得引用"约束的必要性

### 验证检查清单 ✅
- "所有涉及的关键字动作是否已查 CR 正式定义？" → 测试文件未通过
- "如果涉及触发式异能，是否已确认结构？" → 测试文件未通过
- "如果涉及模式选择，是否已确认 modal 选择时机？" → 测试文件未通过

---

## 结论与建议

1. **强制深度检索机制被验证为必要**：三道历史错题的共同根因都是未查 CR 正式定义，新工作流的"未检索不得引用"约束可以有效阻止此类错误。

2. **测试文件答案需要修正**：`raw/mtg_referee_test_202604.md` 中第9、11、12题答案有误，应更新为正确答案并在 `wiki/branches/referee/test-questions/` 中归档。

3. **决策树需补充关键规则引用**：当前决策树已指明检索方向，但 Harmonize 决策树中的"关键确认点"（是否包含替代性放逐）应直接引用 702.180a 原文，避免 agent 再次推断。

4. **建议将本次测试作为 regression test**：这三道题加正确答案应放入 `test-questions/` 作为强制深度检索的回归测试用例。

---

*报告生成时间: 2026-04-27*
