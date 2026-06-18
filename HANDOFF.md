# 会话交接文档（HANDOFF）

> 本文件用于跨对话窗口交接。下一个窗口**先读本文件**即可接续工作。
> 最后更新：2026-06-18

---

## 0. 一句话现状

正在为 opencode 构建一套**万智牌（MTG）skill 知识基础设施**。已建立治理三件套（宪法/体系架构/提交规范），正在执行落地路径。**当前进行中的任务：排查并修复 cEDH 概念页剩余的牌张描述硬伤，之后做 1/2/3 步落地。**

---

## 1. 用户的真实意图（多次澄清后的最终理解）

用户要的**不是**直接造一个 cedh skill，而是要**自顶向下的体系**：
1. 先有**宪法**（不可违背的原则）
2. 再有**整体 skill 体系架构**
3. 再有**单 skill 提交规范**（让社区能按格式提交）
4. 用上述架构**倒逼出 cEDH skill 的协作架构**——核心目标是**让社区能参与提交**（提交"知识内容块"，不动 SKILL.md 入口）
5. 贡献者定位：**技术型**（能接受目录约定/模板/git/校验脚本）

工作方式要求：**提案先行 → 多轮校验（用 reviewer subagent 并行评审）→ 改到全部 approve 才收敛**。不要直接动手做，先出文档请审。破坏性变更要走治理流程、可回退、记 log。

---

## 2. 已产出的文档及状态

| 文件 | 版本/状态 | 说明 |
|------|----------|------|
| `CONSTITUTION.md` | v0.1 草案（**未走多轮校验**） | 12 条 P1-P12，分四编。曾跑过 1 轮校验得 approve-with-changes，建议项（补 P13 IP/版权、判据分机器/人工两栏、P3 数学不变量、P10 批准人、log 格式等）**尚未并入** |
| `skill/ARCHITECTURE-mtg-skills.md` | **v1.0 定稿** ✓ | 整体体系架构。三层（L3 领域skill/L2 公共能力/L1 知识数据）+ 路由约定。经 3 轮校验 + opencode 实测收敛 |
| `skill/CONTRIBUTING-mtg-skill.md` | **v1.0 定稿** ✓ | 单 skill 提交规范+模板。经 3 轮校验收敛 |
| `skill/ARCHITECTURE-cedh-skill.md` | v0.1 草案（**未走多轮校验**） | cEDH skill 协作架构（社区按"内容块"提交）。**用户两个决策尚未并入**（见第 4 节） |
| `wiki/branches/strategy/PROPOSAL-cedh-breaker.md` | 提案+评审记录 | cedh-breaker 早期提案，含 4 位 reviewer 意见。无 frontmatter（规范 reviewer 已指出违规） |

**所有文档均未提交 git。**

---

## 3. 关键事实（已用实测/工具查证，不要再凭记忆推翻）

- **opencode 1.15.6**。`skills.paths: ["./skill"]` **生效且递归扫描 `**/SKILL.md`**（实测 `opencode debug skill` 确认）。验证命令：`opencode debug skill`（列已加载）、`opencode debug config`（看解析配置）。
- **实际加载的 skill**：`customize-opencode`(built-in)、`mtg-wiki`、`mtg-judge-zh`。
- **`modern-breaker` 是死 skill**：缺 YAML frontmatter，被过滤，未加载。
- **opencode 无 skill 优先级/仲裁机制**：skill 选择 = 模型读 description 自主调用。不要写"系统级优先级路由"。
- **L2 公共层落地机制**：`opencode.json` 的 `instructions` 字段（注入主会话规则上下文，官方支持）；是否传递到子 agent **文档未载，需实测**。`opencode.json` 目前**无** `instructions` 字段。
- **frontmatter 官方只认 5 字段**：name/description（必填）、license/compatibility/metadata（可选）。name 正则 `^[a-z0-9]+(-[a-z0-9]+)*$`，=目录名。description 1-1024 字符。
- **MTG 工具**（`raw/tools/mtg_wiki/`）：`card_search.py`、`name_translator.py`、`rule_search.py`、`scryfall_rulings.py`、`validation.py` 等，可正常运行（python3）。查牌：`python3 ./raw/tools/mtg_wiki/card_search.py "卡名"`。
- **`rg` 未安装**，用 Grep 工具或 grep 命令。
- **bash printf 对中文有编码问题**，写中文用 python3 写文件或 Write/Edit 工具。

---

## 4. 用户已做的决策（必须遵守，不要再问）

- mtg-wiki **保持全覆盖**通才（不收缩为兜底）；专家 skill 靠 description 软引导 + 让渡兜底。
- L2 用 `skill/_shared/mtg-common.md` + `opencode.json` 的 `instructions` 落地。
- 不喜欢 modern-breaker → 但最终决定：**保留并复活它**（补 frontmatter），cedh 与之并存。
- cEDH 内容**不迁移**：概念页留 `wiki/concepts/cedh-*`，竞技产物放 `wiki/branches/strategy/` 下 cEDH 子结构。
- **cEDH skill 协作架构 v0.2 的两个待并入决策**：
  1. **统一加赛制子目录**：cedh 放 `branches/strategy/cedh/`，**modern 也迁到 `branches/strategy/modern/`**（破坏性变更，影响 modern 现有 ~19 文件 + modern-breaker 引用路径，需走治理流程）。
  2. **5 类内容块定稿**：套牌拆解/Meta快照/决策树/组合技/单卡评估。
  （这两个决策**尚未写入** `ARCHITECTURE-cedh-skill.md`，下个窗口需并入并重新校验）

---

## 5. 当前正在做的任务（被打断处）

**任务：解决剩余硬伤，然后做 1/2/3 步。**

### 5a. 剩余硬伤排查（进行中，未完成）
已修复的 4 处硬伤（见第 6 节）。**新发现待修**：`wiki/concepts/cedh-combo-patterns.md:117` 的 **Ad Nauseam 异能描述疑似有误**。

下一步动作（被打断时正要做）：**读取 cedh-combo-patterns.md 第 2/3/4 节全文（约 :63-187），提取所有提到的卡牌，用 `card_search.py` 批量查证官方文本，全面排查 Oracle Combo / Ad Nauseam / Isochron Scepter 章节是否还有编造的牌张描述**。涉及卡牌至少：Demonic Consultation、Tainted Pact、Ad Nauseam、Angel's Grace、Phyrexian Unlife、Isochron Scepter、Dramatic Reversal。

修复原则：每处改动必须有 `card_search.py` 官方 Oracle 文本为证，不凭记忆。修完用 Grep 确认无残留旧表述，记 `wiki/log.md`（用 python3 写，避免 printf 中文编码问题）。

### 5b. 然后依次做（用户明确要求"做 1 2 3 步"）
- **第 1 步：复活 modern-breaker** —— 给 `skill/modern-breaker/SKILL.md` 补合法 frontmatter（name: modern-breaker + description 含触发+让渡边界），使其能被 opencode 加载。改完用 `opencode debug skill` 验证它出现在列表里。
- **第 2 步：建 cedh 目录骨架 + 5 个模板** —— 建 `wiki/branches/strategy/cedh/{decks,meta-snapshots,decision-trees,combos,card-evaluations}/`；写 5 个模板 `wiki/branches/strategy/_templates/cedh-*.md`（或按 ARCHITECTURE-cedh-skill.md 第二节定义的路径）。模板含 frontmatter 契约字段（block/archetype/commander/as_of）。
- **第 3 步：抽 L2 公共能力层** —— 建 `skill/_shared/mtg-common.md`（工具契约 + 牌名双语规范 + 层系统速查 + 引用格式 + Schema 契约），在 `opencode.json` 加 `instructions` 引用它。**注意先实测 instructions 是否注入子 agent**（reviewer 标的待验证项）。

---

## 6. 已完成的硬伤修复（本会话，已记 log）

`wiki/concepts/` 下 4 处已修（凭官方 Oracle 文本核实）：
1. `cedh-combo-patterns.md` Kinnan 异能：编造的"{T}:加X=永久物总MV" → 官方"横置非地永久物产法术力时额外产1点该类型"（翻倍效应）
2. 同上 Hullbreaker Horror 异能：编造的"横置/重置" → 官方"弹回咒语/非地永久物到手"；Kinnan combo 从"3牌(含Hullbreaker)"改为正确的"Kinnan+Basalt Monolith 2牌无限法术力"
3. 同上 Underworld Breach 逃脱费用：表格"放逐等同于法术力费用" → 官方"法术力费用+放逐另外3张"
4. 同上 Thassa's Oracle 胜利条件 ×2处："牌库少于5张就赢" → 官方"X(对蓝献忠)≥牌库剩余张数"
5. `cedh.md` + `cedh-pod-dynamics.md` 座位胜率：45/43/38%（合计166%，数学不可能）→ 27/25/22%（4人pod单胜者期望=25%、合计≈100%）

---

## 7. 文档体系全景（产物间关系）

- `CONSTITUTION.md` = 原则（为什么）
- `skill/ARCHITECTURE-mtg-skills.md` = 整体体系架构（怎么分层协作）
- `skill/ARCHITECTURE-cedh-skill.md` = cedh skill 的社区协作架构（怎么按块提交）
- `skill/CONTRIBUTING-mtg-skill.md` = 单 skill 提交规范+模板（怎么写一个）

整体架构倒逼出的 cedh 落地关键路径：
`instructions注入实测 → 抽L2 → 修硬伤+复活modern-breaker → 建薄分支层 → 造cedh-breaker`

---

## 8. 行为提醒（用户在本会话中反复纠正过的点）

- **不要擅自扩大范围或先斩后奏**（违反过 C7，曾未提案直接删 modern-breaker，靠 git checkout 恢复）。
- **不要凭记忆写牌张/规则**，必须 `card_search.py`/`rule_search.py` 查证（曾因此写错 Kinnan，连 reviewer 也记错过）。
- **实测 > 文档推断**（曾因网页文档误判 skills.paths）。
- 用户偏好：先出文档/diff 请审，多轮校验到收敛；用**中文**回答。
- `mcp__question` 工具调用时每个 question 对象必须含 `question` 字段（本会话多次因漏字段报错）。
