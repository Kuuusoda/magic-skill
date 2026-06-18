# 提案:cedh-breaker Skill(竞技指挥官环境分析)

- 状态:**Proposal / 待评审**
- 提出日期:2026-06-17
- 替代关系:拟替代或与 `modern-breaker` 并存(待 review 决定)
- 评审对象:本提案的「计划 / 架构 / 宪法」三部分

---

## 一、背景与动机

用户希望拥有一个像 `modern-breaker` 一样、但面向 **EDH/cEDH 赛制**的专属 strategy skill。
初次实现时未走治理流程(直接创建并删除既有 skill),现回退并改为提案先行。

关键事实(已核实):
- cEDH 真实素材集中在 `wiki/concepts/cedh-*.md`(5 页)+ `output/cedh小屋周报/`(1 份赛事周报)。
- 摩登策略素材在 `wiki/branches/strategy/`(decks/、meta-snapshots/、decision-trees/)。
- 两个赛制的**数据归属结构不对称**(见架构待决项 D1)。
- cEDH 是 4 人 pod、多为 BO1,**无传统 sideboard 概念**,核心是政治博弈与位置效应。

---

## 二、计划(Plan)

| 阶段 | 产出 | 关口(Gate) |
|------|------|-----------|
| P0 提案与治理 | 本文档(计划+架构+宪法) | 用户批准方向 |
| P1 架构评审 | 定位、数据归属、触发边界结论 | 架构 reviewer 通过 |
| P2 内容/数据评审 | 引用真实性、cEDH 内容正确性 | 领域 + 正确性 reviewer 通过 |
| P3 实现 | SKILL.md(依评审修订) | 通过宪法检查清单 |
| P4 验证与合入 | 路径校验、触发测试、更新 index.md/log.md | 集成 reviewer 通过 |

---

## 三、架构(Architecture)

定位:`cedh-breaker` 属于 **strategy 分支的 skill 层**,消费通用知识库,不修改它。

```
通用层  wiki/concepts/cedh-*.md       ← "cEDH 是什么"(原型/组合技/pod/数据)
        wiki/concepts/commander*.md    ← 指挥官通用规则
赛事数据 output/cedh小屋周报/*.md       ← meta 快照
────────────────────────────────────
skill 层 skill/cedh-breaker/SKILL.md    ← "本分支怎么用这些知识做竞技分析"
边界     mtg-wiki(休闲/百科) · mtg-judge-zh(规则裁定)
```

可引用的真实素材(已校验存在):
- `wiki/concepts/cedh.md` — 赛制总览、竞技维度、环境元游戏
- `wiki/concepts/cedh-deck-archetypes.md` — Turbo/Stax/Midrange/Adaptive 四原型
- `wiki/concepts/cedh-combo-patterns.md` — 5 大组合技路线
- `wiki/concepts/cedh-pod-dynamics.md` — 位置、政治、互动决策
- `wiki/concepts/cedh-data-analysis.md` — 数据驱动评估方法
- `output/cedh小屋周报/cedh-tournament-report-2026-04-07-to-2026-04-21.md` — 赛事 meta 数据

### 架构待决项(需 review 拍板)
- **D1 数据归属不对称**:cEDH 策略内容散在 `concepts/`,摩登在 `branches/strategy/`。是否迁移/聚合 cEDH 到 strategy 分支以保持对称?(影响 skill 引用路径与未来可维护性)
- **D2 单一过期快照**:仅 1 份 2026-04 周报。meta 查询可信度边界如何约束?
- **D3 触发重叠**:cEDH 规则问题归 cedh-breaker 还是 mtg-judge-zh?休闲 EDH 归 cedh-breaker 还是 mtg-wiki?
- **D4 modern-breaker 去留**:替代 / 并存 / 停用。

---

## 四、宪法(Constitution,草案)

所有分支 skill 须遵守的不可违背原则:

- **C1 分层不破坏** — 分支层只消费、不修改通用知识库;通用库答"是什么",分支层答"本分支怎么处理"。
- **C2 来源真实性** — 所有引用指向真实存在的本地文件;禁止编造路径、牌名、规则号、数据。
- **C3 可溯源** — 数据须标注来源与时间戳;区分"数据驱动结论"与"主观推测"。
- **C4 牌名核实** — 牌名经 name_translator/card_search 取官方译名,「中文(English)」双语格式。
- **C5 触发边界** — description 同时声明"触发"与"不触发",避免与同库其他 skill 抢占。
- **C6 规范遵从** — frontmatter / WikiLink / 命名规范一致。
- **C7 变更需评审** — 删除或改动既有 skill 须经评审 + 回退预案。

---

## 五、评审记录(2026-06-17,4 位 reviewer 并行)

**总判:四票 approve-with-changes。** 方向、提案先行、宪法 C1/C2/C7 均获认可;实现前须解决以下硬约束。

### A. 架构 reviewer
- D1 → **不整体迁移**;cedh.md/pod-dynamics/commander* 是百科应留 concepts,只在 branches/strategy/ 补建薄分支层承载竞技产物。须先定 "What vs How" 判定标准。
- D2 → 非阻塞;照搬 modern-breaker 时效约束即可。
- D3 → 提案**漏了最大重叠方 mtg-wiki**(其 description 自述覆盖"赛制、策略")。须在 description 写明对 mtg-wiki 的优先级。
- D4 → **并存**;但发现 modern-breaker 无 frontmatter,须补回(C5 才可执行)。
- 风险:照抄 modern-breaker 决策链会指向**不存在的 cEDH 路径**(decks/、decision-trees/),触 C2。SKILL.md 须只引用已存在文件。

### B. cEDH 领域 reviewer(查出底层素材硬伤)
- **季宁(Kinnan)异能描述错误**(cedh-combo-patterns.md:194),整条 Kinnan 组合技机制叙述错。
- **冥界裂隙逃脱费用**表格(:21)与步骤(:32)自相矛盾。
- **Pod 座位胜率数学不自洽**:45%+43%+38%≈166%,四座位期望应=25%、合计≈100%。
- **塔萨的神谕胜利条件**"牌库<5 就赢"是错误表述,应为"检视张数≥牌库剩余"。
- 原型环境占比(~40/20/30/10%)**无来源**,且周报是按指挥官统计、无原型维度 → 违反 C3。
- 数据工具链(topdeck_client.py 等 4 个)**全部不存在**;唯一周报维度过浅(无胜率/conversion)。skill 不能承诺"数据驱动定量评估",只能做定性分析。
- 素材清单漏列:output 里的"小屋严选"primer、sos-cedh-top10、GENERATION_GUIDE;真实 meta 头部"罗噶克系"缺专门拆解。

### C. 集成 reviewer
- 配置无需改;新 skill 会被自动发现,**前提是带合法 frontmatter**。
- **modern-breaker 当前无 frontmatter → 实际未注册、是死 skill**;"并存"前必须先修。
- description 须显式反向排除:摩登→modern-breaker、裁定→mtg-judge-zh、休闲/百科→mtg-wiki。
- 提案 6 条引用路径**逐个 test -e 全部存在**,无悬空。
- D4 若选替代,README.md/README_EN.md 两处引用须同步改(否则悬空)。

### D. 规范 reviewer
- **本提案文件自身违规**:无 frontmatter(违反 C6)、文件名含大写 PROPOSAL、type 无归属、未进 index.md(孤立页)。
- 宪法补充:**C8 时效性**、**C9 禁编造能力**、**C10 治理与记录**;并厘清 C6 只约束 wiki 页面、C1-C5/C7 约束 skill 行为。
- 计划:D1-D4(含 D4)须全部绑定到 P1 关口;C1-C7 须转成可勾选 checklist;C4 工具可用性须在 P2 前置校验;P4 补 rollback 步骤。
- 治理缺失:批准人未定义、log.md 无 skill op 类型、无 git/PR 工作流、skill 无注册表、提案生命周期未定义。

### 合入前强制修订清单(P3 gate)
- [ ] 本提案文件补 frontmatter + 改小写文件名 + 进 index(自我合规)
- [ ] 宪法补 C8/C9/C10,厘清 C6 作用域
- [ ] D1-D4 在 P1 拍板;采用"保留概念页+薄分支层";D4 定并存
- [ ] **先修底层素材 4 处硬伤(Kinnan/Breach/座位胜率/Oracle)** —— 优先级最高,独立于 skill
- [ ] SKILL.md 仅引用真实存在文件;补合法 frontmatter + 反向排除 description
- [ ] 修复 modern-breaker 缺失 frontmatter
- [ ] 收窄能力声明为"定性分析"(不存在的数据工具链降级为方法论参考)
- [ ] 定义批准人、log.md 的 skill op 格式、git/PR 工作流
