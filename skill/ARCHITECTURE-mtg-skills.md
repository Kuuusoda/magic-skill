# MTG Skill 体系架构设计

- 文档地位:**全量万智牌 skill 体系的顶层架构设计**。所有 skill(含未来的 cedh)都是本架构的实例。
- 版本:v1.3(在 v1.2 基础上确认 5 个项目 skill 并补入 Limited 学习型 skill,2026-07-09)

## 地基实测结论(2026-07-09,以 `opencode debug skill` / `opencode debug config` 为权威)

第 1 轮校验曾担心"`./skill` 可能未被加载"。已用 opencode 1.15.6 实测确认:

- ✅ **`skills.paths: ["./skill"]` 生效**:`opencode debug skill` 列出 `duel-commander-breaker`、`limited-master`、`modern-breaker`、`mtg-judge-zh`、`mtg-wiki`,location 指向 `skill/<name>/SKILL.md`,确认本仓库 skill 被正常加载。`skills.paths` 是真实配置项,且**递归扫描 `**/SKILL.md`**。
- ✅ **`modern-breaker` 已复活**:已出现在 `debug skill` 输出中,不再是死 skill。
- ✅ **`skill/_shared/` 不会被误注册为 skill**:该目录无 `SKILL.md`,`debug skill` 不列出 `_shared`;公共文档通过 `opencode.json` 的 `instructions` 注入。
- ✅ **L2 shared 已注入主会话配置**:`opencode debug config` 可解析 `instructions: ["skill/_shared/mtg-common.md"]`。子 agent 是否继承仍需独立实测,但主会话级工具/实体解析契约已可作为共享层生效。
- **权威校验手段**:`opencode debug skill`(列已加载 skill)、`opencode debug config`(看解析后配置)、`opencode debug agent <name>`——本架构所有"是否生效"类断言以这些命令实测为准,不靠网页文档推断。

- 创建:2026-06-17
- 上位约束:`CONSTITUTION.md`(P5 分层、P6 单一事实源)。本架构是宪法在 skill 体系上的具体落地。
- 设计方法:自顶向下 —— 先定**整体分层与协作**,再由架构**倒逼**出每个 skill(含 cedh)的规格。

---

## 一、设计目标(针对盘点暴露的 5 大病灶)

| 病灶(现状) | 架构目标 |
|-----------|---------|
| mtg-wiki 全覆盖,与 judge/modern 重叠 | **description 路由引导 + 显式让渡**:mtg-wiki 保持全覆盖通才;专家 skill 靠 description 措辞引导模型在其领域被选中,mtg-wiki 内写明"复杂裁定/竞技 meta 让渡给专家"兜底。注:opencode 无系统级优先级,此为软引导非硬保证 |
| 规则裁判被实现 3 次 | **单一权威**:一种能力只有一个权威实现,其余引用 |
| 工具说明/层系统表/牌名规范多处重复 | **公共能力下沉**:共享层只定义一次,skill 引用 |
| 多个 skill 与分支/场景映射混乱 | **清晰映射**:skill ←→ 分支/赛制/学习场景 一一对应 |
| 索引未就绪却宣称已打包 | **显式依赖**:架构声明数据/索引为前置层 |

---

## 二、三层架构 + 路由约定

> 说明:opencode **无 skill 优先级/仲裁机制**(实测确认)。skill 的选择 = 模型读各 skill 的 `description` 自主调用 `skill()`。因此原 v0.2 的"L4 路由层"**不是一层**(无独立载体),降为贯穿 L3 的**路由约定**。另:`agent/` 下有真实的 agent 编排层(judge pipeline 调度 6 个 agent),按用户决策**不进主架构图**,在第四节单独说明。

```
┌─────────────────────────────────────────────────────────────┐
│ L3  领域 Skill 层  Domain Skills                             │
│     通才全覆盖 + 专家专精,并存:                              │
│   ┌──────────────────────────────────────────────────────┐  │
│   │ 通才基线:mtg-wiki(全覆盖规则/牌张/赛制/策略/背景)     │  │
│   │   ——任何问题都能答,在专家领域让位给专家             │  │
│   ├──────────────┬──────────────┬──────────────────────────┤ │
│   │ 规则裁判类    │ 赛制策略类    │ (预留) 创作/DIY 类        │ │
│   │ mtg-judge-zh │ <赛制>-breaker│ creation-* / diy-*        │ │
│   │ (referee)    │ limited-master│                          │ │
│   └──────────────┴──────────────┴──────────────────────────┘ │
│   〔路由约定〕模型读 description 自主选 skill;无系统优先级。 │
│   靠 description 措辞引导"专家领域选专家、其余回落 wiki",    │
│   并用各 skill 内显式"让渡边界"兜底误选(非系统保证)。       │
├─────────────────────────────────────────────────────────────┤
│ L2  公共能力层  Shared Capabilities (单一事实源)             │
│     落地形式:`skill/_shared/mtg-common.md`,经 opencode.json │
│     的 "instructions" 字段注入主会话规则上下文。            │
│     已实测主会话配置解析通过;子 agent 继承性仍需单独实测。 │
│     内容:                                                    │
│     · 工具契约:card_search / rule_search / name_translator   │
│       / card_resolve / format_meta_evidence / scryfall_rulings│
│       (调用方式只定义一次)                                    │
│     · 公共规范:牌名双语格式、查证优先、层系统速查、引用格式  │
│     · 实体解析:简称/绰号/半截名 → 候选列表 + 语境重排        │
│     · Schema 契约:query-plan/card-info/rule-info/analysis... │
│     L3 skill 不再重复粘贴,改一处全局生效                     │
├─────────────────────────────────────────────────────────────┤
│ L1  知识与数据层  Knowledge & Data (只读底座)                │
│     · 通用知识库 wiki/concepts|entities|sources|synthesis    │
│     · 分支层 wiki/branches/{referee,strategy,creation,diy}   │
│     · 原始资料 raw/{cr,mtr,ipg,references}                   │
│     · 牌张数据来源 + 可选本地索引(build_indices.py 生成);    │
│       索引缺失时由 mtgch/Scryfall API 回退                  │
└─────────────────────────────────────────────────────────────┘
```

### 层间规则
- 上层只能消费下层,不能跨层重定义下层已有的东西。
- L3 **路由约定(无系统优先级,实测确认)**:mtg-wiki 全覆盖作通才基线;专家 skill(judge/各 breaker)靠 description 措辞引导模型在其领域被选中。重叠问题靠 description 的"专属定位 + 让渡边界"软引导(非系统仲裁),误选时由各 skill 内显式让渡兜底。
- L2 是**唯一**定义工具/规范/Schema 的地方,落地为 `skill/_shared/mtg-common.md` + `opencode.json` 的 `instructions` 注入;L3 skill 引用而非复制(直接消灭"重复粘贴"病灶)。

### 全局牌名实体解析层(v1.2)

`card_search.py` 是单卡详情查询器,不是实体解析器。所有 skill 在遇到短名、数字、绰号、半截英文名、角色名、多版本同名角色时,必须先走 L2 的实体解析契约,再查单卡详情。

典型失败并非某个赛制独有:
- 法禁:`2099`、`spider99`、`phelia`、`tivit`、`kess`、`niv` 等会被普通 fuzzy 搜索误指。
- cEDH:`blue farm`、`tymna/kraum`、`rogsi`、`tnt`、`sisay`、`najeela`、`thoracle`、`breach` 等既可能指套牌/组合技/单卡,也可能指不同版本或不同组件。
- 摩登:`frog`、`energy`、`belcher`、`amulet`、`scam` 等常指套牌或 archetype,不是单张牌。
- 裁判问答:用户说"oracle combo"可能是牌名、组合技路径或胜利条件缩写,不能直接查第一张牌。

新增 L2 工具契约:
- `card_resolve.py`(或 `card_search.py --candidates`)输出候选列表、置信度、重排理由和是否需要追问。
- `format_meta_evidence.py` 查询赛制 meta 证据,把简称/套牌名/指挥官名与 Duel Commander、cEDH、Modern 等赛制的当前聚合实体对齐。

L3 skill 只提供赛制语境权重(例如 cEDH pod/meta、法禁 commander/meta、Modern deck archetype),不得各自重写实体解析算法。

硬规则:
- 低置信或多候选接近时先追问。
- 如果根据格式语境自动选择,答案必须写明"我将 X 解析为 Y"。
- 不得把数据库/API 第一结果当作用户意图。
- 当用户询问“现在/当前/meta/占比/强度/Tier/环境/热门/怎么样”等赛制问题时,必须要求 meta evidence gate;无 meta evidence 时不得声称当前 meta 结论。

---

## 三、L3 skill 分类法(skill 如何切分)

切分维度 = **(知识分支 × 赛制/场景)**。mtg-wiki 是横跨所有格子的**通才基线**,专家 skill 各占一个**专属格子,靠 description 在该格被引导选中**:

| 类别 | skill 命名 | 专属领域(description 引导被选中) | 消费的 L1 分支 | 与其它 skill 的关系 |
|------|-----------|---------------|---------------|---------|
| 通才基线 | `mtg-wiki` | **全覆盖**:规则+牌张+赛制+策略+背景+翻译 | concepts 通用层 + 各分支 | 任何问题都能答;在专家领域让位给专家 |
| 规则裁判 | `mtg-judge-zh` | 规则/互动/合法性/政策裁定 | branches/referee | 策略让给 breaker;非裁定回落 wiki |
| 赛制策略 | `modern-breaker` | 摩登 meta/套牌/对局 | branches/strategy(摩登) | 规则让给 judge;其它赛制让给对应 breaker |
| 赛制策略 | `duel-commander-breaker` | Duel Commander/法禁 1v1 竞技策略、禁牌表/规则版本边界、20 血资源判断 | `branches/strategy/duel-commander/` + `concepts/duel-commander.md` | 规则让给 judge;多人 cEDH 让给 cEDH;通用牌张回落 wiki |
| 限制赛学习/策略 | `limited-master` | 限制赛学习、轮抽/现开组牌、P1P1、单卡评分、17Lands 数据阅读、对局复盘 | `concepts/limited|draft|sealed` + `synthesis/limited-learning-path.md` + `sources/2026-06-22-topdeck-limited-reading-list.md` | 具体牌面/译名回落 wiki;规则判定让给 judge |
| 赛制策略 | **`cedh-breaker`(待建)** | 竞技指挥官 meta/原型/组合技/pod 博弈 | `concepts/cedh-*` + `branches/strategy/` cEDH 薄层(待建) + `output/周报` | 规则让给 judge;休闲 EDH/非专精回落 wiki |
| 创作(预留) | `creation-*` | 文章/背景故事 | branches/creation | — |
| DIY(预留) | `diy-*` | 卡牌设计 | branches/diy | — |

> 切分维度说明(据校验修正):真正的一级维度是**知识分支**(referee/strategy/creation/diy);**赛制**只是 strategy 分支内部的二级切分(modern/duel-commander/cedh)。但并非所有 strategy skill 都叫 `<赛制>-breaker`:限制赛是学习/评分/实战教练场景,落为 `limited-master`。referee 一个 judge 吃全赛制;creation/diy 无赛制维度。新赛制 = strategy 下加 breaker 或场景型 skill;新分支 = 一级新增。

**关键决策(据用户)**:mtg-wiki **保持全覆盖**作通才基线,**不收缩为兜底**。专家 skill 通过 description 措辞引导,在其领域被模型引导选中;专家领域之外由 mtg-wiki 接管。注意:opencode **无系统级优先级仲裁**,这是 description 软引导 + 让渡兜底,非系统硬保证(实测确认)。病灶 1 因此**部分缓解而非结构性消除**——彻底消除需用 agent 调用做硬转交(见第四节)。

---

## 四、协作与路由机制

- **路由 = 模型自主选择(无系统优先级)**:opencode 把各 skill 的 description 列给模型,由模型读 description 自主 `skill()`。架构要求每个 L3 专家 skill 的 description 含"专属定位 + 让渡边界",mtg-wiki 保持全覆盖并写明"复杂裁定/竞技 meta 让渡专家"。这是**软引导**,非系统保证(SKILL.md 入口规范由维护者把关,见 P8;社区内容块贡献规范见 `.github/CONTRIBUTING.md`)。
- **裁判单一权威(结构手段)**:规则裁判统一走 `mtg-judge-zh`。mtg-wiki 的"裁判专用"段改为"复杂裁定交 mtg-judge-zh"。更强的做法是 **mtg-wiki 遇规则裁定调用 judge agent** 而非自答——这是结构性单一权威,比纯 description 引导可靠。消灭"裁判实现 3 次"。
- **跨 skill 让渡**:策略 skill 遇规则裁定不自行裁定,显式指向 judge;非本赛制策略指向对应 breaker 或 wiki。
- **L2 共享生效**:工具契约/牌名规范/Schema 由 `skill/_shared/mtg-common.md` 经 `instructions` 注入主会话;judge/wiki/各 breaker 共用同一份,改一处全局可见。子 agent 是否继承仍列为待实测项(见第七节 Q3)。
- **L2 版本治理**:`mtg-common.md` 是全局单点,任何改动影响所有 skill。工具契约/Schema 一旦发布即视为稳定契约,变更须走 P9 提案(限制爆炸半径)。
- **agent 编排层(存在但不入主图,据用户决策)**:`agent/` 下有 8 个 agent;`mtg-judge-zh` skill 的 pipeline 真实调度其中 6 个(query-decomposer/card-lookup/rule-lookup/ruling-lookup/interaction-analyzer/checker),经 `Agent(subagent_type=...)` 串联。它位于 skill 与工具之间,是 judge 的内部实现,不在 L1–L3 主图中体现;skill↔agent↔tool 的依赖细节由各 skill 自身文档描述。

---

## 五、用架构倒逼出 cedh-breaker 规格(边界由架构倒逼,内容由领域素材填充)

cedh-breaker **不是独立设计的**,而是从架构推导出来的。但须诚实区分:架构能倒逼出它的**边界/接口/依赖**,推导不出它的**领域内容**(四原型、组合技路线等是 cEDH 固有知识,非架构产物)。

### 5.1 架构倒逼的(边界 / 接口 / 依赖)

| 架构约束 | 推导出的 cedh-breaker 规格 |
|---------|--------------------------|
| L3 职责 | 占"赛制策略 × 竞技指挥官"格,只做竞技 cEDH 策略;**不做**规则裁定、不做休闲 EDH |
| 路由约定 / 让渡 | description 写明让渡:规则裁定→mtg-judge-zh;休闲 EDH/非专精→回落 mtg-wiki。与 modern-breaker **以赛制(摩登 vs cEDH)区分**(同属 description 软引导路由,无系统优先级) |
| 消费 L1 | `wiki/concepts/cedh-*`(知识)+ `wiki/branches/strategy/` 下 cEDH **薄分支层(待建,不迁移概念页)** + `output/cedh小屋周报/`;**不修改**通用层(P5) |
| 引用 L2 | 工具/牌名规范/Schema 引用公共层,不重复粘贴 |
| 依赖 L1 数据 | 牌名查证依赖 card_search + 索引(前置 build_indices.py) |
| 遵守 CONTRIBUTING | frontmatter 合法、引用路径真实、牌名双语、卡牌查证、走提案+评审+log 流程 |
| 与 modern-breaker 关系 | **仅命名对称** `<赛制>-breaker`;**不照搬其正文结构/路径**(modern 的 decks/decision-trees 对 cEDH 不存在);cedh 决策链只引用真实存在的 cEDH 路径 |

### 5.2 领域自带的(内容,非架构产物)

四原型(Turbo/Stax/Midrange/Adaptive)、五大组合技路线、pod 位置与政治、无 sideboard 等 —— 这些是 cEDH 领域知识,来自现有 concepts/cedh-* 素材,**不是架构推导出来的**,实现时据素材填充。

### 5.3 倒逼出的前置依赖(cedh skill 成立前必须满足)

1. **建薄分支层**:在 `wiki/branches/strategy/` 下建 cEDH 竞技产物层(**定性原型/meta 分级、决策树**,非数据驱动 tier——与下方第 5 条口径一致),概念页**留在 concepts**(不迁移,符合 P5 与此前评审结论)。
2. **L2 抽取**:先抽出公共能力层,否则 cedh 又重复粘贴工具说明。
3. **底层硬伤修复**:Kinnan/Breach/Oracle/座位胜率 4 处错误先修(P2/P4)。
4. **赛事数据时效与深度**:周报仅 1 份 2026-04、按指挥官统计、无胜率/原型维度 → cedh 必须标注数据时效、不得外推"当前 meta"。
5. **能力声明收窄为定性**:数据工具链(topdeck_client.py 等)在仓库不存在 → cedh 只承诺**定性分析**(原型/组合技/pod),**不承诺数据驱动定量**(tier/胜率/conversion)。
6. **对称样板已复活**:`modern-breaker` 已有合法 frontmatter 并被 `opencode debug skill` 加载;后续新建 `<赛制>-breaker` 仍须通过同一 frontmatter gate。

### 5.4 拦截闸门(避免带病上线)

**下层素材存在已知硬伤(Kinnan/Breach/Oracle/座位胜率)未修复前,cedh-breaker 不得引用对应页面**;数据/工具不存在的能力不得写入 description。把前置 3/5 从口头承诺变成实现期的硬闸门。

---

## 六、与现有产物的关系

- `CONSTITUTION.md` = 不可违背的原则(为什么)
- 本文档 = 体系架构(整体长什么样、怎么分层协作)
- `.github/CONTRIBUTING.md` = 社区内容块 PR 贡献规范(怎么提交一个内容块,GitHub Fork+PR+CI);SKILL.md 入口为维护者级,守 P8
- `skill/PROPOSAL-github-contribution.md` = 上述社区贡献体系(Fork+PR+CI 强制查证)的设计提案(v0.5)
- cedh-breaker = 架构推导出边界/接口、领域素材填内容的一个 L3 实例(产物)

---

## 七、待校验事项(本架构 v0.3 的 open questions)

1. ~~L4 是否独立一层~~ → **已定:降为路由约定**(opencode 无优先级机制,实测确认)。
2. **全覆盖 + description 软引导**能否让模型可靠选对 skill?会不会专家被通才抢答?(opencode 不做仲裁,只能靠 description 措辞 + 让渡兜底)——需实跑会话观察。
3. **L2 的 `instructions` 注入是否传递到被调度的子 agent**?主会话注入已实测;子 agent 继承性文档未载,需 `opencode debug agent` 或端到端任务实测。若不传递,judge pipeline 的子 agent 需自行引用 `_shared`。
4. "裁判单一权威":mtg-wiki 裁判段改让渡 + 协调 judge 的 skill/agent 双实现——改动范围与回退?
5. ~~cEDH 内容是否迁移~~ → **已定:不迁移,概念留 concepts + 建薄分支层**(与 P5 自洽)。
6. 6 个前置依赖的执行关键路径建议更新:`子 agent 继承实测 → cEDH 硬伤修复 → cEDH 薄分支层 → cedh-breaker`。`instructions` 主会话注入、L2 抽取、modern-breaker frontmatter 已完成。
