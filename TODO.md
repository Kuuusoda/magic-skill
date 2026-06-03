# mtg-judge-zh Skill 待办事项

## 背景

2026-05-26 session：克撒传 vs 腥红之月规则分析出错，原因是 CR 714.4 规则更新后增加了 "with one or more chapter abilities" 限定语，旧裁定失效。已从错误中吸取教训并更新了 skill 文件和硬编码校验脚本。

---

## TODO 1：生成边缘测试套件（鲁棒性测试）

**目标**：验证 `validation.py` 在各种异常输入下的行为，确保系统不会因格式问题崩溃或产生误导性输出。

### 测试类别

- [x] **Schema 字段缺失测试**
  - query-plan 缺少 cards / rule_keywords / question_type 等必需字段
  - card-info 缺少 oracle_text / scryfall_id
  - analysis 缺少 conclusion / reasoning / confidence
  - verdict 缺少 status / card_check 等

- [x] **类型错误测试**
  - cards 字段传入字符串而非数组
  - confidence 传入整数而非字符串
  - needs_rulings 传入字符串而非布尔值
  - cited_rules 传入包含非字符串元素的数组

- [x] **枚举值越界测试**
  - question_type = "invalid_type"
  - confidence = "maybe"
  - source_type = "unknown_source"
  - status = "OK"

- [x] **空值/空数组边界测试**
  - cards = [] 但 question_type = "interaction"
  - rule_keywords = []
  - matches = []
  - cited_rules = [] 但 reasoning 中引用了规则

- [x] **跨引用不一致测试**
  - analysis.cited_rules 包含 evidence.rules 中不存在的编号
  - analysis.cited_cards 包含 evidence.cards 中不存在的牌名
  - ruling.scryfall_id 与 evidence.cards 中的任何牌都不匹配

- [x] **内容完整性测试**
  - card-info error=null 但 oracle_text 为空
  - cr_rule 的 source_file 不以 "raw/" 开头
  - card-info scryfall_id 为空但 error 也为空

- [x] **Verdict 状态不一致测试**
  - card_check=FAIL 但 status=PASS
  - evidence_check=FAIL 但 status=PASS
  - 所有检查都是 PASS 但 status=BLOCK

- [x] **JSON 格式错误测试**
  - 非 JSON 输入
  - 缺少闭合括号
  - 非法字符
  - 顶层不是对象

**实现文件**：`tests/validation/test_edge_cases.py`（55 个测试用例，全部通过）

---

## TODO 2：正确性回归测试（避免过拟合）

**目标**：确保新增的规则变更检查和硬编码校验不会导致正常情况下的误判。验证系统对合法、标准的问题仍能正确回答。

### 测试类别

- [x] **标准互动问题（不应触发规则变更警觉）**
  - 闪电击 vs 幽灵选手（保护）
  - 践踏机制解释
  - 传奇规则（同名传奇）
  - 这些问题的分析应该 confidence=certain，不触发任何警告

- [x] **验证器不应过度敏感**
  - 标准 analysis 输出（cited_rules 全部在 evidence 中）→ 必须 PASS
  - 标准 verdict（所有检查 PASS，status=PASS）→ 必须 PASS
  - 没有 assumptions 的 analysis 且 confidence=certain → 不应产生警告

- [x] **引用完整性检查不应误报**
  - 使用 wiki 来源的规则编号（如 "N/A"）→ 验证器不应报错
  - 使用 wiki_decision_tree 类型的 source_type → 验证器应接受

- [x] **裁定新鲜度检查不应过度反应**
  - 普通问题（非争议性互动）使用旧裁定 → 不应强制要求验证时效性
  - 只有用户明确暗示规则变更时才触发额外审查

### 回归测试用例（真实数据）

- [x] 用历史成功的闪电击 vs 保护分析数据跑完整 pipeline → 应全部 PASS
- [x] 用标准践踏机制解释的数据跑完整 pipeline → 应全部 PASS
- [x] 用传奇规则分析数据跑完整 pipeline → 应全部 PASS

**实现文件**：`tests/validation/test_correctness.py`（21 个测试用例，全部通过）

---

## TODO 3：提升规则判定效率

**目标**：减少 LLM Agent 调用次数，缩短端到端响应时间，同时保持输出质量。

### 诊断（当前瓶颈）

当前流程：
```
Step 1: query-decomposer (1 Agent)
Step 2: card-lookup × N (N Agents) + rule-lookup × M (M Agents) + ruling-lookup (可选, Agents)
Step 3: interaction-analyzer (1 Agent)
Step 4: checker (1 Agent)
```

最坏情况下：1 + N + M + 1 + 1 = N+M+3 次 LLM 调用，每次数秒到十几秒。

### 优化方向

- [x] **简化 query-decomposer**
  - 简单问题（单张牌规则解释）可简化步骤
  - 只有复杂互动问题才需要完整流程

- [x] **card-lookup 去 Agent 化**
  - 方法 A：直接 Bash 调用 `name_translator.py` + `card_search.py`
  - 方法 B（fallback）：翻译失败时启动 Agent
  - 减少 N 次 Agent 调用

- [x] **rule-lookup 去 Agent 化**
  - 方法 A：直接 Bash 调用 `grep` + `Read`
  - 方法 B（fallback）：多文件结果需综合时启动 Agent
  - 减少 M 次 Agent 调用

- [x] **ruling-lookup 去 Agent 化**
  - 直接 Bash 调用 `scryfall_rulings.py`
  - 简单规则解释跳过 ruling-lookup

- [x] **合并 analyzer + checker**
  - 在一个 Agent prompt 中同时要求分析和 verdict
  - 减少 1 次 Agent 调用

- [x] **提前终止**
  - 简单规则解释跳过 ruling-lookup
  - card-lookup 返回 error 时提前终止

- [x] **减少迭代轮次**
  - 从最多 3 轮减少到最多 2 轮

### 目标指标

- [x] 标准问题（如"践踏是怎么运作的"）端到端 < 30 秒，Agent 调用 ≤ 1 次
- [x] 复杂互动问题（如"克撒传和红月互动"）端到端 < 90 秒，Agent 调用 ≤ 3 次

**实现位置**：`SKILL.md` 工作流概览及执行步骤已更新

---

## 优先级建议

| 优先级 | 事项 | 原因 |
|--------|------|------|
| P0 | 边缘测试套件 | 确保今天新增的 validation.py 可靠 |
| P0 | 正确性回归测试 | 避免今天的改动破坏正常功能 |
| P1 | 效率优化 | 提升用户体验，减少等待时间 |
