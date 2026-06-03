# 回归测试报告 — 2026-05-26-atomic-workflow-v1

## 元信息

| 项目 | 值 |
|------|-----|
| 测试时间 | 2026-05-26 00:04 UTC+8 |
| Tag | atomic-workflow-v1 |
| Skill 版本 | mtg-judge-zh @ architecture-v3.1 原子化工作流 |
| 使用模型 | claude-opus-4-7 |
| 测试耗时 | ~15 分钟 |
| 备注 | 原子化工作流首次端到端测试。验证 query-decomposer → card-lookup/rule-lookup → interaction-analyzer → checker 的完整流程，含假设审查机制。 |

---

## 总览

| 指标 | 结果 |
|------|------|
| 总题数 | 1（Q18 作为工作流验证） |
| 正确 | 1 / 1 |
| 错误 | 0 / 1 |
| 总正确率 | 100% |

---

## 逐题结果

| 题号 | 你的回答 | 标准答案 | 判定 | 用时 |
|------|---------|---------|------|------|
| Q18 | B | B | ✓ | ~15min |

---

## 工作流执行记录（Q18）

### 题目摘要

Alex casts Applied Geometry and targets Adrix and Nev, Twincasters. What happens?

### Step 1: query-decomposer

**输入**: "Alex casts Applied Geometry and targets Adrix and Nev, Twincasters. What happens when Applied Geometry resolves?"

**输出**:
```json
{
  "cards": ["Applied Geometry", "Adrix and Nev, Twincasters"],
  "rule_keywords": ["copy effects", "tokens", "replacement effects"],
  "question_type": "interaction",
  "needs_rulings": false,
  "needs_strategy": false
}
```

**Schema 校验**: PASS

### Step 2: 并行查询

#### card-lookup("Applied Geometry")

**输出**:
```json
{
  "input_name": "Applied Geometry",
  "english_name": "Applied Geometry",
  "scryfall_id": "f109f2eb-895b-44a6-b6b5-81bf3831ccd5",
  "oracle_text": "Create a token that's a copy of target non-Aura permanent you control, except it's a 0/0 Fractal creature in addition to its other types. Put six +1/+1 counters on it.",
  "mana_cost": "{2}{G}{U}",
  "type_line": "Sorcery"
}
```

**内容审查**: PASS（oracle_text 非空，scryfall_id 存在）

#### card-lookup("Adrix and Nev, Twincasters")

**输出**:
```json
{
  "input_name": "Adrix and Nev, Twincasters",
  "english_name": "Adrix and Nev, Twincasters",
  "scryfall_id": "6adadbc9-4a08-4c1d-adf7-edee73799d9e",
  "oracle_text": "Ward {2}\nIf one or more tokens would be created under your control, twice that many of those tokens are created instead.",
  "mana_cost": "{2}{G}{U}",
  "type_line": "Legendary Creature — Merfolk Wizard",
  "power": "2",
  "toughness": "2"
}
```

**内容审查**: PASS

#### rule-lookup("copy effects")

**查询路径**: wiki 优先 → `wiki/branches/referee/decision-trees/copy-effects.md`

**关键获取**:
- CR 707.2: 可复制特征值（名称、法术力费用、颜色、类别、规则叙述、力量/防御力）
- CR 707.2b: 一旦复制完成，改变原物件不影响复制品
- CR 707.4: 战场上再复制不触发 ETB/LTB

**来源**: wiki_decision_tree
**内容审查**: PASS

#### rule-lookup("tokens")

**查询路径**: wiki 优先 → `wiki/branches/referee/decision-trees/tokens.md`

**关键获取**:
- CR 111.5: 衍生物复制获得原始特征
- CR 111.7: 战场外区域的衍生物消失（SBA 704.5d）

**来源**: wiki_decision_tree
**内容审查**: PASS

#### rule-lookup("replacement effects")

**查询路径**: wiki → raw/cr/6.md

**关键获取**:
- CR 614.1: 替代性效应于事件发生过程中生效
- CR 614.5: 替代性效应不会反复引发本身
- CR 614.6: 如果被替代，事件从未发生；改为发生被更改过的事件

**来源**: cr_rule (`raw/cr/6.md`)
**内容审查**: PASS（source_file 以 raw/ 开头）

### Step 3: interaction-analyzer

**Evidence 包**:
- cards: Applied Geometry（创建 token 复制 + 6 个指示物）, Adrix and Nev（token 翻倍替代式效应）
- rules: copy effects（707.2, 707.4）, tokens（111.5）, replacement effects（614.1, 614.5, 614.6）

**分析推理**:
1. Applied Geometry 的效应包含两部分：(a) 创建 1 个 token（复制目标永久物）；(b) 放置 6 个 +1/+1 指示物
2. Adrix and Nev 的替代式效应监控"token would be created"事件
3. 根据 CR 614.1/614.5，替代式效应将"创建 1 个 token"替换为"创建 2 个 token"
4. 替代式效应只作用一次（CR 614.5），不会反复引发
5. 新创建的 2 个 token 同时进入战场，每个都是 Adrix and Nev 的复制品（额外是 0/0 Fractal 生物）
6. "Put six +1/+1 counters on it" — 由于替代后创建了 2 个 token，指示物放置对 each 生效
7. 新创建的 token 的异能（包括替代式效应本身）不会影响自己的创建事件，因为替代式效应必须在事件前已存在（CR 614.1）

**输出**:
```json
{
  "conclusion": "Alex creates two tokens and puts six +1/+1 counters on each of them.",
  "reasoning": "Applied Geometry creates a token copy of Adrix and Nev. Adrix and Nev's replacement effect (CR 614.1) modifies this to create two tokens instead of one. The replacement effect only applies once (CR 614.5). The instruction to put six +1/+1 counters applies to each created token. The newly created tokens' abilities do not affect their own creation.",
  "confidence": "certain",
  "cited_rules": ["614.1", "614.5", "614.6", "707.2"],
  "cited_cards": ["Applied Geometry", "Adrix and Nev, Twincasters"],
  "assumptions": [
    {"assumption": "Applied Geometry initially creates 1 token", "evidence_based": true},
    {"assumption": "Adrix replacement effect doubles to 2 tokens", "evidence_based": true},
    {"assumption": "Counter placement applies to each created token", "evidence_based": true},
    {"assumption": "New tokens' replacement effects don't modify their own creation", "evidence_based": true}
  ],
  "needs_more_evidence": null
}
```

**引用审查**: PASS（所有 cited_rules 在 Evidence 中，所有 cited_cards 在 Evidence 中）
**迭代检查**: PASS（needs_more_evidence 为 null，无需补充）

### Step 4: checker

**输入**: Evidence + Analysis

| 检查项 | 结果 | 说明 |
|--------|------|------|
| card_check | PASS | 两张牌 Oracle 文本完整 |
| rule_check | PASS | 来源为 wiki_decision_tree 和 cr_rule |
| evidence_check | PASS | 证据充分支撑结论 |
| citation_check | PASS | 所有引用在 Evidence 中存在 |
| assumption_check | PASS | 4 个假设全部 evidence_based = true |

**输出**:
```json
{
  "status": "PASS",
  "card_check": "PASS",
  "rule_check": "PASS",
  "evidence_check": "PASS",
  "citation_check": "PASS",
  "assumption_check": "PASS",
  "notes": "所有检查通过。假设审查无未验证假设。"
}
```

---

## 原始回答记录

### Q18

> Agent 原始回答: Alex creates two tokens and puts six +1/+1 counters on each of them. (Answer B)
>
> 推理: Applied Geometry creates a token copy of Adrix and Nev. Adrix and Nev's replacement effect modifies this to create two tokens instead of one (CR 614.1, 614.5). The instruction to put six +1/+1 counters applies to each created token. The newly created tokens' abilities do not affect their own creation because the replacement effect must exist before the event.

---

## 工作流验证结论

| 验证项 | 结果 |
|--------|------|
| query-decomposer Schema 输出 | ✓ |
| card-lookup 牌面查询 | ✓ |
| rule-lookup wiki 优先策略 | ✓ |
| 并行查询执行 | ✓ |
| 内容审查（每步） | ✓ |
| interaction-analyzer 假设审查 | ✓ |
| 引用审查 | ✓ |
| 迭代检查（无需迭代） | ✓ |
| checker 独立验证 | ✓ |
| 最终答案正确 | ✓ |

**原子化工作流首次端到端测试通过。**
