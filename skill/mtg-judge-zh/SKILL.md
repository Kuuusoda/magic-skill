---
name: mtg-judge-zh
description: 万智牌中文规则裁判。用于回答规则解释、牌张互动、赛制合法性、比赛政策(MTR/IPG)等问题。当用户询问任何涉及万智牌完整规则(CR)、比赛规则(MTR)、违规处理方针(IPG)的问题时触发。
---

# mtg-judge-zh — 万智牌中文规则裁判 Skill

## 触发条件

当用户提出以下类型的问题时触发：
- 规则解释（"践踏是怎么运作的？"）
- 牌张互动（"闪电击能指定有保护的生物吗？"）
- 赛制合法性（"这张牌在摩登赛制合法吗？"）
- 比赛政策（"慢打怎么判罚？"）
- 任何涉及万智牌 Comprehensive Rules (CR)、Magic Tournament Rules (MTR)、Infraction Procedure Guide (IPG) 的问题

## 工作流概览

```
┌─────────────────────────────────────────────────────────────────────┐
│                         快速路径判断                                   │
│  简单规则解释 → 跳过 ruling-lookup，query-decomposer 可简化           │
│  单张牌查询   → card-lookup 用 Bash 直接调用，不走 Agent               │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
Step 1: query-decomposer → 输出 QueryPlan
  ↓ 硬编码 Schema 校验 (validation.py)
Step 2: [并行] card-lookup × N (Bash) + rule-lookup × N (Bash) + ruling-lookup(可选, Bash)
  ↓ 硬编码内容审查 (validation.py)
  ↓ [如有 error 的 card] → 提前终止并报告
Step 3: interaction-analyzer + checker (合并为 1 个 Agent)
  ↓ 硬编码引用审查 + 迭代检查 (validation.py)
  ↓ [如需补充] → 回到 Step 2（最多 2 轮）
Step 4: 输出最终答案
```

**优化后 Agent 调用次数**：
- 标准问题（规则解释）：**1 次**（analyzer+checker 合并）
- 复杂互动（2 张牌 × 2 规则）：**1 次**（analyzer+checker 合并）
- 最坏情况（需要补充查询）：**3 次**（analyzer → 补充查询 → analyzer）

**对比旧流程**：旧流程最坏情况下需要 N+M+3 次 Agent 调用（N=牌数, M=规则关键词数）。优化后最坏情况只需 3 次。

**硬编码验证脚本位置**：`./raw/tools/mtg_wiki/validation.py`

验证脚本使用 Python 标准库实现，**不依赖外部包**。在每个步骤后，将 agent 的 JSON 输出通过脚本验证，确保格式正确性和内容完整性。

项目根目录：`./`

**L2 公共契约注入（必须执行）**：
- 在任何 `Agent(...)` 调用前，先读取 `./skill/_shared/mtg-common.md`。
- 构造子 agent prompt 时，把该公共契约与对应 `agent/*.md` 定义一起拼入 prompt。
- 不依赖子 agent 自行读取 L2，也不假设 `opencode.json` 的 `instructions` 一定会传递到子 agent。

---

## 执行步骤

### Step 1: query-decomposer

**操作：**
1. 读取公共契约：`Read ./skill/_shared/mtg-common.md`
2. 读取 agent 定义：`Read ./agent/query-decomposer.md`
3. 构造 prompt：将公共契约 + agent 定义作为系统指令，加上用户原始问题
4. 调用 `Agent(subagent_type="general-purpose", prompt="...")`
5. 从输出中提取 JSON 格式的 QueryPlan

**硬编码 Schema 校验（必须执行）：**
```bash
echo '{agent输出的JSON}' | python3 ./raw/tools/mtg_wiki/validation.py --schema query-plan
```
校验内容：
- 必须包含字段：cards, rule_keywords, question_type, needs_rulings, needs_strategy
- cards 和 rule_keywords 必须是字符串数组
- question_type 必须是 interaction / rule / policy / format 之一
- **校验失败（exit code ≠ 0）→ 要求 agent 修正输出，不得进入下一步**

---

### Step 2: 并行查询

根据 QueryPlan 并行调用多个 Agent。

#### card-lookup（每张牌一个 Bash 调用，全部并行）

**操作（对 QueryPlan.cards 中的每张牌）：**

**方法 A（推荐）：直接用 Bash 调用工具脚本**
```bash
# Step 0: 解析牌名/简称/多组件互动
python3 ./raw/tools/mtg_wiki/card_resolve.py "用户输入" --format judge --intent card

# 若用户输入是组合技或多牌互动，使用 interaction intent
python3 ./raw/tools/mtg_wiki/card_resolve.py "用户输入" --format judge --intent interaction

# Step 1: 对 resolver 选中的 card 或 components 翻译牌名
python3 ./raw/tools/mtg_wiki/name_translator.py "中文牌名"

# Step 2: 查询 Oracle（使用英文牌名）
python3 ./raw/tools/mtg_wiki/card_search.py "English Name"
```

将 Bash 输出解析为 card-info JSON 格式：
```json
{
  "input_name": "中文牌名",
  "english_name": "English Name",
  "scryfall_id": "...",
  "oracle_text": "...",
  "mana_cost": "{R}",
  "type_line": "Instant",
  "power_toughness": null,
  "error": null
}
```

**方法 B（fallback）**：如果 Bash 调用返回错误或多义结果，才启动 Agent

**方法 A 与方法 B 的选择标准**：
- 方法 A 适用于：`card_resolve.py` 已选中唯一实体，且 name_translator.py / card_search.py 成功的情况
- 方法 B 适用于：resolver 输出 `needs_clarification=true`、翻译失败、返回多张候选牌、或需要额外判断时
- 若 resolver 输出 `components`，必须分别查询每个组件；若任一组件不确定，先追问，不得给规则结论

**并行化**：所有牌的查询是独立的，可以**全部并行**用 Bash 调用。"general-purpose", prompt="[agent定义] 查询牌名: {card_name}")`

Agent 内部会执行：
```bash
python3 ./raw/tools/mtg_wiki/card_resolve.py "牌名或互动输入" --format judge --intent card
python3 ./raw/tools/mtg_wiki/name_translator.py "牌名"
python3 ./raw/tools/mtg_wiki/card_search.py "英文牌名"
```

**硬编码内容审查（必须执行）：**
```bash
echo '{agent输出的JSON}' | python3 ./raw/tools/mtg_wiki/validation.py --schema card-info
```
校验内容：
- oracle_text 非空？
- scryfall_id 存在？
- english_name 存在？
- type_line 存在？
- **校验失败（exit code ≠ 0）→ 标记 WARN，继续但记录问题**

**输出 Schema（card-info.json）：**
```json
{
  "input_name": "中文牌名",
  "english_name": "English Name",
  "scryfall_id": "...",
  "oracle_text": "...",
  "mana_cost": "{R}",
  "type_line": "Instant",
  "power_toughness": null,
  "error": null
}
```

#### rule-lookup（每个关键词 Bash 并行查询）

**操作（对 QueryPlan.rule_keywords 中的每个关键词）：**

**方法 A（推荐）：直接用 Bash 调用 grep + Read**
```bash
# Step 1: 查 wiki 决策树
grep -r -l "关键词" ./wiki/branches/referee/decision-trees/

# Step 2: 查 wiki 概念页
grep -r -l "关键词" ./wiki/concepts/

# Step 3: 查 wiki 框架
grep -r -l "关键词" ./wiki/branches/referee/frameworks/

# Step 4: 查 CR
grep -n "关键词" ./raw/cr/*.md
```

然后用 **Read** 读取 grep 结果中的具体文件内容。

将查询结果组装为 rule-info JSON 格式：
```json
{
  "keyword": "protection",
  "matches": [
    {
      "rule_number": "702.16a",
      "rule_text": "...",
      "source_file": "raw/cr/7.md",
      "source_type": "cr_rule"
    }
  ]
}
```

**方法 B（fallback）**：如果 grep 返回过多结果或需要跨文件综合判断，才启动 Agent

**并行化**：所有规则关键词的查询是独立的，可以**全部并行**用 Bash 调用。"general-purpose", prompt="[agent定义] 查询规则关键词: {keyword}")`

Agent 内部查询策略（wiki 优先）：
```bash
grep -r -l "关键词" ./wiki/branches/referee/decision-trees/
grep -r -l "关键词" ./wiki/concepts/
grep -r -l "关键词" ./wiki/branches/referee/frameworks/
grep -n "关键词" ./raw/cr/*.md
```

**硬编码内容审查（必须执行）：**
```bash
echo '{agent输出的JSON}' | python3 ./raw/tools/mtg_wiki/validation.py --schema rule-info
```
校验内容：
- source_type 是否合法？（wiki_concept / wiki_decision_tree / wiki_framework / cr_rule / mtr_rule / ipg_rule）
- cr_rule 类型的 source_file 是否以 raw/ 开头？
- **校验失败（exit code ≠ 0）→ 标记 WARN，继续但记录问题**

**输出 Schema（rule-info.json）：**
```json
{
  "keyword": "protection",
  "matches": [
    {
      "rule_number": "702.16a",
      "rule_text": "...",
      "source_file": "wiki/concepts/protection.md",
      "source_type": "wiki_concept"
    }
  ]
}
```

#### ruling-lookup（可选，仅当 needs_rulings = true）

**操作：**

**方法 A（推荐）：直接用 Bash 调用**
```bash
python3 ./raw/tools/mtg_wiki/scryfall_rulings.py "scryfall_id"
```

**快速路径**：简单规则解释（如"践踏是怎么运作的"）不涉及具体牌张互动，**跳过 ruling-lookup**。

---

### Step 3: interaction-analyzer + checker（合并为一个 Agent 调用）

**优化说明**：analyzer 和 checker 原本是两个独立的 Agent 调用，但它们处理的是同一组 Evidence，且 checker 的工作本质上是对 analyzer 输出的审查。合并后可以减少 1 次 LLM 调用。

**操作：**
1. 合并 Step 2 的所有查询结果为 Evidence 包
2. 读取公共契约：`Read ./skill/_shared/mtg-common.md`
3. 读取 agent 定义：
   - `Read ./agent/interaction-analyzer.md`
   - `Read ./agent/checker.md`
4. 构造 Evidence 包 + 公共契约 + 两个 agent 定义合并作为 prompt，要求同时输出 analysis 和 verdict
5. 调用 `Agent(subagent_type="general-purpose", prompt="...")`

**Agent 输出格式要求**（合并为一个 JSON）：
```json
{
  "analysis": {
    "conclusion": "结论陈述",
    "reasoning": "推理过程",
    "confidence": "certain | likely | uncertain",
    "cited_rules": ["702.16a"],
    "cited_cards": ["Lightning Bolt"],
    "assumptions": [{"assumption": "...", "evidence_based": true, "note": "..."}],
    "needs_more_evidence": null
  },
  "verdict": {
    "status": "PASS | WARN | BLOCK",
    "card_check": "PASS | FAIL",
    "rule_check": "PASS | FAIL",
    "evidence_check": "PASS | WARN | FAIL",
    "citation_check": "PASS | FAIL",
    "notes": "说明"
  }
}
```

**硬编码校验（必须执行）：**
```bash
# 将 Evidence 包保存到 evidence.json
# 提取 analysis 和 verdict 分别校验
python3 ./raw/tools/mtg_wiki/validation.py --schema analysis --evidence evidence.json analysis.json
python3 ./raw/tools/mtg_wiki/validation.py --schema verdict verdict.json
```
校验内容：
- analysis: cited_rules / cited_cards 存在性、confidence/assumptions 一致性
- verdict: 状态一致性、字段类型和枚举值
- **校验失败（exit code ≠ 0）→ 要求 agent 修正输出**

**迭代检查：**
- analysis.needs_more_evidence 非空？
  - 是 → 回到 Step 2，并行补充查询缺失的规则关键词
  - 最多 **2 轮**迭代（旧流程为 3 轮，减少以提升效率），超过则 WARN 并继续
- 为空 → 进入 Step 4

**verdict 处理：**
- PASS → 输出最终答案
- WARN → 输出最终答案，标注不确定点
- BLOCK → 不输出结论，向用户说明缺少什么证据

---

### Step 4: 输出最终答案

基于通过审查的证据输出答案：
- 引用具体规则条文（标注来源：wiki 或 CR）
- 标注置信度（certain / likely / uncertain）
- verdict = WARN 时标注不确定点
- 使用准确的中文牌名

---

## 效率优化策略总结

### 核心原则

**Bash 优先，Agent fallback**。绝大多数数据查询工作可以用 Bash 工具直接完成，不需要启动 LLM Agent。Agent 只用于需要推理、综合、判断的环节。

### 优化措施

| 优化项 | 旧方式 | 新方式 | 节省 |
|--------|--------|--------|------|
| card-lookup | N 个 Agent | N 个 Bash 调用 | N-0 次 Agent |
| rule-lookup | M 个 Agent | M 个 Bash 调用 | M-0 次 Agent |
| ruling-lookup | 1 个 Agent | 1 个 Bash 调用 | 1-0 次 Agent |
| analyzer + checker | 2 个 Agent | 1 个 Agent | 1 次 Agent |
| 迭代轮次 | 最多 3 轮 | 最多 2 轮 | 减少 1 轮 |
| 简单规则解释 | 全部步骤 | 跳过 ruling-lookup | 节省 ruling 查询时间 |
| 错误 card | 继续全部步骤 | 提前终止 | 节省后续步骤时间 |

### 目标指标

- **标准规则解释问题**（如"践踏是怎么运作的"）：端到端 < 30 秒，Agent 调用 ≤ 1 次
- **标准互动问题**（如"闪电击 vs 保护"）：端到端 < 60 秒，Agent 调用 ≤ 1 次
- **复杂争议问题**（如"克撒传 vs 腥红之月"）：端到端 < 90 秒，Agent 调用 ≤ 3 次

### 何时必须用 Agent

以下情况**不能**用 Bash 替代，必须使用 Agent：
1. query-decomposer：需要自然语言理解来拆分问题
2. interaction-analyzer：需要推理牌张互动
3. checker：需要独立验证分析的正确性
4. 规则变更警觉处理：需要判断用户意图和重新评估

---

## 规则变更警觉处理

当用户暗示规则可能有变更（如"这个问题很 tricky"、"裁定已经变了"、"规则更新过"等），**必须**执行以下额外步骤：

1. **暂停当前分析流程**，不要继续基于已有证据推理
2. **重新读取关键规则条文的最新英文原文**：用 Read 直接读取 `./raw/cr/` 中相关条文的精确措辞
3. **中英文对照**：对比中英文版本，确认关键限定语（如 "with one or more"、"if it has" 等）是否一致
4. **重新评估裁定时效性**：Scryfall 返回的 ruling 包含 `published_at` 日期，确认该裁定是否仍适用于当前规则版本
5. **确认无误后再继续分析**

**历史教训**：克撒传 vs 腥红之月的互动中，CR 714.4 在规则更新后增加了 "with one or more chapter abilities" 限定语，彻底改变了互动结果。旧裁定（2021-06-18）因此失效。

---

## 常见陷阱与校验清单

### 陷阱 1：裁定依赖
- **问题**：WotC 裁定依附于特定 CR 版本，规则更新后可能失效
- **校验**：引用裁定时，必须注明发布日期；若规则条文已有更新，以当前 CR 为准

### 陷阱 2：规则条文措辞微变
- **问题**：一个新增/删除的限定语（如 "with one or more"）可能完全改变结论
- **校验**：争议性互动必须逐字核对英文原文，不依赖记忆或旧翻译

### 陷阱 3：层系统时序误解
- **问题**：连续效应在物件进战场时已生效，不能假设"先进场→后受效应"
- **校验**：分析进场时效应时，直接应用层系统，不假设"裸状态"进场

### 陷阱 4：中英文 CR 不同步
- **问题**：本地中文 CR 翻译可能滞后于英文原文
- **校验**：争议结论必须以英文 CR 为准，中文翻译仅作参考

---

## 验收标准

### must_have
- [ ] 所有提及的牌已查 Oracle 文本
- [ ] 所有引用的规则来自本地文件（wiki 或 raw/cr/）
- [ ] 答案只引用已收集的证据
- [ ] checker verdict ≠ BLOCK

### nice_to_have
- [ ] 有 WotC 官方裁定支持，且已验证该裁定仍适用于当前规则版本
- [ ] 引用了 wiki 概念页或决策树
- [ ] 区分了"确定"和"推测"
- [ ] 争议性互动已核对英文 CR 原文的关键限定语

### forbidden
- 不引用训练数据中的规则记忆
- 不跳过关键词的 CR 702 定义
- 不编造规则编号
- 不编造牌名翻译
- 不依赖未经验证时效性的旧裁定（尤其是用户暗示规则有变更时）
- 不忽略英文 CR 原文的关键限定语（如 "with one or more"、"if it has" 等）

---

## 关键路径说明

### 工具脚本位置
- `name_translator.py`: `./raw/tools/mtg_wiki/name_translator.py`
- `card_resolve.py`: `./raw/tools/mtg_wiki/card_resolve.py`
- `card_search.py`: `./raw/tools/mtg_wiki/card_search.py`
- `rule_search.py`: `./raw/tools/mtg_wiki/rule_search.py`
- `scryfall_rulings.py`: `./raw/tools/mtg_wiki/scryfall_rulings.py`
- `mtgch_name_index.py`: `./raw/tools/mtg_wiki/mtgch_name_index.py`
- **`validation.py`** (硬编码校验): `./raw/tools/mtg_wiki/validation.py`

### 数据位置
- CR 规则: `./raw/cr/`
- MTR: `./raw/mtr/`
- IPG: `./raw/ipg/`
- Wiki 概念: `./wiki/concepts/`
- Wiki 决策树: `./wiki/branches/referee/decision-trees/`
- Wiki 框架: `./wiki/branches/referee/frameworks/`

### Agent 定义文件位置
- `query-decomposer`: `./agent/query-decomposer.md`
- `card-lookup`: `./agent/card-lookup.md`
- `rule-lookup`: `./agent/rule-lookup.md`
- `ruling-lookup`: `./agent/ruling-lookup.md`
- `interaction-analyzer`: `./agent/interaction-analyzer.md`
- `checker`: `./agent/checker.md`

### Schema 文件位置
- `query-plan.json`: `./schema/query-plan.json`
- `card-info.json`: `./schema/card-info.json`
- `rule-info.json`: `./schema/rule-info.json`
- `analysis.json`: `./schema/analysis.json`
- `verdict.json`: `./schema/verdict.json`
