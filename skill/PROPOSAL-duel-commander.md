# 提案：法禁 EDH（Duel Commander）模块架构

- 文档地位:在 strategy 分支下新增 **Duel Commander（法式指挥官，"法禁"）** 赛制模块,与 cedh 对称并列。复用既有 GitHub Fork+PR+CI 贡献基础设施。
- 版本:**v1.0(CI 泛化与共享契约落地)**——v0.2 并入第1轮 9 项 blocking;v0.3 banlist 改自动抓取;v0.4 并入**确认轮**(3 reviewer:v0.2 闭环 approve + 自动抓取 7 项 + 泛化集成 3 项)全部 blocking;v0.5 修正 banlist 决策遗留冲突,补齐内容生产/导航/验收设计;v0.6 修正 Bo1/55 误口径,补规则版本/合法性/实战路线图;v0.7 补实体消歧;v0.8 落地目录、模板、种子内容与 skill;v0.9 补大型赛事备战/牌表审计/时钟计划;v1.0 落地 `lint_strategy_block.py`、`verify_cards.py` 覆盖 Duel Commander、workflow runtime/strategy gate 与 L2 shared。**后续待实施 banlist 自动抓取、dc issue 表单与 render_dc_issue.py。**
- 创建:2026-06-18　更新:2026-07-09
- **v0.7→v0.8 种子落地补充**:新增 `wiki/branches/strategy/duel-commander/` 目录骨架、`index.md`、`aliases.md`、`rules/source-registry.md`、最小 meta seed、Kess/Niv 两个 deck stub、6 个 dc 模板与 `skill/duel-commander-breaker/SKILL.md`;同步 strategy/wiki 索引入口。此轮只落知识层与 skill 层,暂不触碰 CI/banlist 抓取脚本。
- **v0.8→v0.9 大型赛事备战补充**:以长期参加大型法禁赛事的牌手视角补缺口:skill 增加冠军赛压力测试、牌表审计、flex slots、已知对手准备、时钟计划、地基/曲线审计与“缺少快照不得确认合法性”红线;`dc-deck` 模板增加牌表审计、地基与曲线、flex slots、时钟计划;新增 `decision-trees/tournament-prep-checklist.md`。
- **v0.9→v1.0 CI 泛化落地**:`lint_cedh_block.py` 改为 `lint_strategy_block.py` shim 化;`verify_cards.py` 覆盖 `wiki/branches/strategy/duel-commander/**`;GitHub workflow 在保留 required check 名称的前提下加入 dc paths/runtime paths、skill frontmatter 检查和 `card_resolve.py` 回归测试;L2 shared 通过 `opencode.json` 注入主会话。
- **v0.5→v0.6 规则版本补充**:① 撤回"Bo1/55 分钟"固化口径,改为官方默认 BO3/50 分钟,主办方可在赛前覆盖;② 增加官方来源注册表与新旧规则选择算法;③ 增加法禁合法性校验矩阵;④ 增加高手向实战内容路线图(调度、先后手、换将、指挥官依赖度、威胁/解牌基准)。
- **v0.6→v0.7 牌名消歧补充**:针对"2099"这类简称/别名/部分牌名,新增实体解析与赛制语境重排规则:不得直接采用数据库第一个命中;必须列候选、按法禁合法性与 meta/内容块出现率重排,低置信时追问用户。
- **v0.4→v0.5 设计补充**:① 修正"用户决策固化"中 banlist 仍写手动维护的遗留冲突,统一为自动抓取+自动开 PR+人工 review/merge;② 补 `index.md` 导航与 strategy/wiki 总索引回链;③ 补内容来源分层、模板必备章节、首批种子内容、skill 输出契约、验收矩阵,避免只落 CI/banlist 而缺少可消费知识层。
- **v0.3→v0.4 确认轮修正**:① as_of 与 banlist_as_of **正交双字段**(dc deck/meta 都要,不可顶替);② lint 日期校验循环(:147)是漏网硬编码,须加 banlist_as_of;③ **workflow 不可裸改名**(会击穿 branch protection required check→PR 永久 hang),仅在 paths-filter 加 dc 目录;④ 抓取脚本 YAML 安全转义(json.dumps,牌名含 '/,//)、断言 HTTP200+Content-Type、canary 稳定牌、两列表分别突变检测+归零即失败;⑤ source_hash=解析结果哈希(非整页);⑥ App token + 固定分支 auto/dc-banlist(幂等)+ 失败通知 + manual 兜底;⑦ banlist_as_of 优先取官网生效日;⑧ dc 开独立 render_dc_issue.py + dc-block 表单。
- **v0.2→v0.3 修正**:禁牌表来源从"维护者手动"改为 **`fetch_dc_banlist.py` 自动抓取 + 定时自动开 PR + 维护者 review/merge**(用户决策)。实测官网纯静态、class 语义稳定(`ban-item banned` 88 张 / `commander-restricted` 24 张),标准库可解析;加**卫生检查(数量突变/类名消失则失败不覆盖)**。
- **v0.1→v0.2 关键修正**(评审收敛):① banlist 拆 `banned` / `banned_as_commander` 两类(法禁核心特征);② 撤回"verify_cards 不用改"——其 CEDH_DIR 硬编码需泛化;③ banned 列表放 **frontmatter**(非正文)以确定性解析;④ 比对归一化 EN 面、抽 `split_bilingual`/`normalize_name` 到 `utils.py` 共用;⑤ 禁牌校验基准 = "块 `banlist_as_of` ≤ 之的最新快照"(非全局最新);⑥ 泛化连带改动(render/issue-to-pr/CONTRIBUTING/workflow/REQUIRED_FIELDS 按 format 分表)列为同 PR 原子项;⑦ 概念页既存禁牌表标"非权威";⑧ 首份 banlist 设为 deck/meta 前置闸门;⑨ Voltron 标注边缘原型、补 Tempo 判定准则、补先后手/mulligan 维度
- 上位约束:`CONSTITUTION.md`(P1–P12)、`ARCHITECTURE-mtg-skills.md`(L1/L2/L3 分层、cedh 仅命名对称不照搬)、`.github/CONTRIBUTING.md`(社区内容块贡献规范)。

> **用户决策固化**:
> ① 法禁 = **Duel Commander**（1v1、起始 20 血、无 21 点指挥官伤害、独立法国禁牌表;官方默认 BO3/50 分钟,主办方可在赛前公告改成其他赛制/时长）。
> ② archetype 枚举(**7 类**):Aggro / Control / Midrange / Combo / Stax / Voltron / Tempo。
> ③ 禁牌表 = **单一事实源快照**,由 `fetch_dc_banlist.py` 从 source-registry 记录的官方 B&R 端点自动抓取,定时自动开 PR,维护者 review/merge 后生效;快照带 `banlist_as_of`。
> ④ 禁牌**硬校验**:套牌块 cards_cited/commander 命中禁牌 → CI **ERROR 挡合并**。
> ⑤ skill 命名 **`duel-commander-breaker`**。
> ⑥ lint **泛化**为 `lint_strategy_block.py`(一份管 cedh + duel-commander + 未来赛制)。

---

## 一、定位与分层（遵现有架构）

- **L1 知识层**:概念页 `wiki/concepts/duel-commander.md`(**已存在**)回答"是什么";竞技产物放新建 `wiki/branches/strategy/duel-commander/`。
- 与 cedh **对称并列、非子集**——两者赛制规则不同(人数/血量/指挥官伤害/禁牌表),各自独立目录。遵 ARCHITECTURE §5.1"仅命名借鉴,不照搬"。
- **L3 skill**:`duel-commander-breaker`,description 软引导边界:法禁 1v1 策略→它;规则裁定→mtg-judge-zh;多人 cEDH→cedh-breaker;通用/休闲→mtg-wiki。
- **复用 L2 + CI**:工具/牌名/查证契约共用;CI 流水线复用,lint 泛化(见五)。

---

## 二、目录骨架（对称 cedh）

```
wiki/branches/strategy/duel-commander/
├── index.md            # 法禁分支入口:范围、导航、最新快照、贡献方式
├── decks/              # 套牌拆解
├── meta-snapshots/     # 环境快照（带 as_of+sources）
├── decision-trees/     # 1v1 对局/mulligan 决策（无多人政治）
├── combos/             # combo/lock 线
├── card-evaluations/   # 单卡评估（法禁语境）
└── banlist/            # ★法禁专属：禁牌表快照（单一事实源）
```
> `banlist/` 是法禁相对 cedh 的**专属新增**(cedh 无此需求,因其用官方 EDH 禁牌表)。

### 导航与索引补充

- `wiki/branches/strategy/duel-commander/index.md` 是法禁模块的分支入口,必须包含:赛制边界、目录导航、最新 banlist 快照链接、已归档 meta 快照、贡献入口、与 [[duel-commander]] 概念页的分工说明。
- `wiki/branches/strategy/index.md` 增加 Duel Commander 入口;`wiki/index.md` 保留通用概念页 `[[duel-commander]]`,并可在 strategy 分支入口处指向法禁策略层。
- 通用概念页只回答"法禁是什么";策略层 index 回答"本模块如何使用和贡献"。两者不得互相复制禁牌表或 meta 结论(P5/P6)。

---

## 三、内容块类型（5 类 + 1 个赛制专属 banlist）

5 类内容块与 cedh 对称,但 frontmatter 赛制专属字段不同:

| 块 | 目录 | type | archetype 枚举 | cards_cited |
|----|------|------|---------------|-------------|
| 套牌拆解 | `decks/` | synthesis | 7 类(见下) | 核心+关键牌 |
| Meta 快照 | `meta-snapshots/` | synthesis | 空 | 代表牌(豁免穷举) |
| 决策树 | `decision-trees/` | decision-tree | 可空 | 通常空 |
| combo/lock | `combos/` | concept | 可空 | 穷举 |
| 单卡评估 | `card-evaluations/` | concept | 可空 | 穷举 |
| **禁牌表快照** | `banlist/` | synthesis | — | — |

**archetype 7 类**:Aggro / Control / Midrange / Combo / Stax / **Voltron** / **Tempo**。模板/枚举注释须写明(reviewer 领域 N2):
- **Voltron**:法禁取消 21 点指挥官伤害后已近绝迹,**标注为边缘原型**,防被滥用为标签(用户要求保留,但需提示其弱势)。
- **Tempo**:1v1+20 血+廉价干涉使其成立(如 Yuriko 系),与 Aggro/Midrange 边界模糊,模板给一句**判定准则**。

**法禁专属维度(模板章节,reviewer 领域 N5)**:决策树/套牌块应覆盖 ① **先后手(play/draw)**——20 血 1v1 先手优势显著;② **London mulligan 起手判断**——20 血对颜色/曲线容错低。与 cedh 的"pod 政治"明确区分(1v1 无政治)。

### frontmatter 契约（与 cedh 的差异点）
```yaml
format: duel-commander          # 校验键（新枚举）
archetype: <Aggro|Control|Midrange|Combo|Stax|Voltron|Tempo>   # 法禁 7 类
commander: "<中文（English）>"   # 法禁多为单将；partner 少但存在
pair_type: <single|partner|partner-with|friends-forever|background>
as_of: YYYY-MM-DD               # 本块分析/观测时效（P3，与 cedh 一致，所有 deck/meta 块都要）
banlist_as_of: YYYY-MM-DD       # ★法禁专属：所依据的禁牌表版本日期（仅 deck/meta 需要）
cards_cited: [...]              # CI 强制查证（复用）
```
> **`as_of` 与 `banlist_as_of` 正交、不可互相顶替(reviewer3 B1)**:`as_of`=观测/分析时效;`banlist_as_of`=依据哪版禁牌表(合法性)。dc 的 **deck/meta 块两者都要**;decision-tree/combo/card-eval 不需要 `banlist_as_of`。
> 这意味着 lint 的 `REQUIRED_FIELDS` **和日期校验都要按 format+block 分表**(见 §5):cedh 校 `as_of`;dc 的 deck/meta 校 `as_of` + `banlist_as_of`。

### 规则版本与来源优先级（v0.6）

法禁模块必须能回答"按哪一天的规则/禁牌表判断?"。新增 `rules/` 快照层与来源注册表,避免用最新规则回溯误判旧比赛。

```
wiki/branches/strategy/duel-commander/
├── rules/              # 官方 DC 规则快照与来源注册表
└── banlist/            # 官方 B&R 快照
```

- **官方来源注册表**:`rules/source-registry.md` 记录 canonical URL、备用 URL、最后抓取时间、内容 hash、parser 版本。规则文本优先抓 Duel Commander 官方综合规则;B&R 抓官方规则文档声明的 banlist 端点。不得把 `.com` 或 `.org` 单点硬编码进业务逻辑,脚本读取注册表。
- **来源优先级**:
  1. Wizards of the Coast 的法律/官方 MTG 文档;
  2. Duel Commander 官方综合规则快照;
  3. Duel Commander 官方 B&R 快照;
  4. 对应日期的 CR/MTR/IPG 本地快照;
  5. Duel Commander FAQ/官方公告;
  6. 第三方 meta 文章、社群战报、玩家经验。
- **新旧规则选择算法**:
  - 用户给定赛事日期或 `as_of` 时,选择 `effective_date <= as_of` 的最新 `rules/` 与 `banlist/` 快照。
  - 用户问"现在"时,使用本地最新快照;若本地 `fetched_at` 早于官方最新 hash 或超过维护阈值,回答必须标注"本地快照可能过期"。
  - 比赛已开始后,使用比赛开始时生效的规则与禁牌表;赛中不因官网更新而改变。
  - 无法确定 `effective_date` 时,使用抓取日作为下限并输出 WARN,不得把该快照声称为官方生效日。
- **规则差异必须显式建模**:例如 BO3/50 默认、主办方赛前覆盖、20 血、无指挥官伤害、双指挥官每局仅能从指挥官区施放一个、局间 commander swapping、无 sideboard/outside-the-game 效应等,均写入 `rules/` 快照摘要,不散落在 deck/meta 块中。

### 内容生产补充（v0.5）

当前 v0.4 偏重 banlist 与 CI,但法禁模块还需要可消费的知识层。实施时新增以下内容契约:

- **来源分层**:
  - 规则/合法性来源:只认 `banlist/` 快照 + `wiki/concepts/duel-commander.md` 的赛制定义;不得在 deck/meta/card-eval 中重复定义禁牌表。
  - Meta/套牌来源:每个 `dc-meta` 和 `dc-deck` 必须写 `sources` 与 `as_of`;没有足够公开来源时只能写定性观察,不得写"当前 T1"或胜率。
  - 单卡/组合技来源:牌面与译名必须经 `verify_cards.py`/离线索引校验;涉及规则互动时只描述策略用途,规则裁定让渡给 `mtg-judge-zh`。
- **模板必备章节**:
  - `dc-deck`: 指挥官与身份、核心计划、关键牌、先后手差异、London mulligan、常见对局、禁牌表版本、信息边界。
  - `dc-meta`: 数据来源、样本边界、原型分布(可为空)、趋势判断、争议/不确定项、适用 banlist。
  - `dc-decision-tree`: 触发条件、起手/先后手分支、对局中关键分岔、不可替代的查证点。
  - `dc-combo`: 组件穷举、启动条件、易受干涉点、与 banlist 的关系。
  - `dc-card-eval`: 角色定位、适用原型、替代选项、禁牌/仅禁指挥官状态。
- **首批种子内容闸门**:只建空目录还不算模块可用。首轮实施至少应包含 `index.md`、首份 banlist 快照、5 个模板、1 个最小 meta 快照占位(明确样本不足)、2 个代表 deck stub 或"待补"清单。若缺少 banlist 快照,deck/meta 不得合入。
- **skill 输出契约**:`duel-commander-breaker` 回答必须标注 `as_of`、`banlist_as_of`、引用的具体内容块;若只读到概念页而无策略块,必须明确"本库尚无足够法禁策略资料",不能补脑生成 meta。
- **验收矩阵**:
  - 格式:dc 5 类块 + dc-banlist 均可被 `lint_strategy_block.py` 识别。
  - 查证:`verify_cards.py --changed` 能覆盖 `duel-commander/**`,不会静默跳过。
  - 禁牌:全面禁牌在 commander/cards_cited 均 ERROR;仅禁指挥官牌只在 commander ERROR,在 99 的 cards_cited 不报错。
  - 导航:index 与总索引无断链;`[[duel-commander]]` 指向通用概念页,策略内容从 strategy index 进入。
  - 回归:cedh 现有模板与 CI 行为不漂移(除脚本名 shim 外)。

### 法禁合法性校验矩阵（v0.6）

CI 不应只查牌名与 banlist,还要覆盖法禁玩家最常踩的合法性边界:

| 检查项 | deck | meta | combo/card-eval | banlist | 失败等级 |
|--------|------|------|-----------------|---------|----------|
| commander 双语名存在 | 必须 | 可选 | 可选 | 不适用 | ERROR |
| commander 颜色认同覆盖 cards_cited | 建议先 WARN,后续可升 ERROR | 不适用 | 不适用 | 不适用 | WARN |
| singleton 重名 | decklist 完整时 ERROR;stub 阶段跳过 | 不适用 | 不适用 | 不适用 | ERROR/WARN |
| `banned` 命中 commander 或 99 | 必须 | 可选 | 必须标注 | 不适用 | ERROR |
| `banned_as_commander` 命中 commander | 必须 | 可选 | 必须标注 | 不适用 | ERROR |
| `banned_as_commander` 仅出现在 99 | 允许,但建议标注 | 不适用 | 允许 | 不适用 | INFO |
| companion 合法性 | decklist 完整时校验 | 不适用 | 不适用 | 不适用 | WARN/ERROR |
| sideboard / outside-the-game | decklist 完整时不得出现 | 不适用 | 涉及时标注不生效 | 不适用 | ERROR |
| stickers/attractions/acorn/digital-only/ante/dexterity 等结构禁用 | 必须 | 不适用 | 必须 | 不适用 | ERROR |
| 规则快照版本 | deck/meta 必须有 `rules_as_of` 或可由 `banlist_as_of` 同步推得 | 必须 | 可选 | 必须 | ERROR/WARN |

新增 frontmatter 字段建议:

```yaml
rules_as_of: YYYY-MM-DD      # 所依据的 DC 官方规则快照日期;deck/meta 必填
match_policy: default        # default | event-specific
event_policy_source: ""      # 若赛事公告覆盖 BO3/50、计时、淘汰赛结构,填来源
```

`rules_as_of` 与 `banlist_as_of` 独立:规则变更和禁牌更新可能不同步。

### 高手向实战内容路线图（v0.6）

法禁模块要像长期参赛玩家会用的工具,首批内容不应只罗列牌表。每个代表 deck/meta/decision-tree 逐步补这些维度:

- **起手与调度**:按先手/后手、对快攻/控制/组合技分别写 keep/mulligan 标准;记录"两地一动"、"一地 cantrip"、"无一费互动"等可操作判断。
- **指挥官依赖度**:标注套牌是 commander-centric、commander-enabled 还是 commander-optional;写清指挥官被反复处理后的备用计划。
- **局间换将**:针对 partner/background/friends forever 写"默认将"与"局间换将条件";模板必须提醒颜色认同不能改变、只能用 decklist 中登记的指挥官组合。
- **20 血资源账本**:记录痛地/抓牌付血/震地/古墓类效应对 race 的影响;20 血环境中"多抓一张 vs 少两点血"要作为实战判断维度。
- **节奏基准**:每个 deck 写 T1/T2/T3 目标动作、关键交互窗口、先手抢节奏与后手补互动的差异。
- **互动配置**:按 removal/counter/discard/sweeper/graveyard hate/land hate 分类统计,避免只写"互动很多"。
- **对局矩阵**:至少覆盖 Aggro、Control、Midrange、Combo、Stax、Tempo 六个维度;Voltron 标为边缘原型,只在有实际样本时展开。
- **meta 可信度**:所有"强势/弱势/Tier"必须绑定样本来源、地区、时间、banlist 版本;无样本时写"观察假设",不写结论。

### 大型赛事备战补充（v0.9）

从常年打大型法禁赛事的玩家视角,skill 还必须能处理“赛前最后一周”的问题,而不仅是解释套牌:

- **牌表审计**:完整 100 张、singleton、commander 合法性、`banned`/`banned_as_commander`、companion/outside-the-game/结构禁用风险。缺少完整牌表和快照时不得确认“可参赛”。
- **赛事政策确认**:赛事日期、banlist/rules 快照、主办方是否覆盖 BO3/50、淘汰赛时长/平局处理。没有 event policy 时使用 default 但标注风险。
- **三回合计划**:每套 deck 必须能回答先手/后手 T1/T2/T3 想做什么,否则无法给出实战强度判断。
- **地基/曲线审计**:颜色源、横置地密度、一费/二费动作、付血地对 20 血 race 的影响。
- **Flex slots**:最后 3-8 个可替换卡位按 meta 偏快/偏控/偏 combo/未知拆解。
- **已知对手准备**:针对热门指挥官和本地常见对手写关键回合、必须保留的互动、不能掉进的心理陷阱。
- **时钟计划**:BO3/50 下慢速套牌必须有领先/落后时的速度策略,避免“理论优势但现场平局”。
- **测试题输出**:当资料不足时,skill 应给下一轮测试的具体问题,而不是用空泛建议填补。

### 牌名简称与实体消歧（v0.7）

问题示例:`2099` 在牌库中可能匹配多张牌。若 skill 只把用户输入丢给 `card_search.py` 并拿第一个结果,就会把"数据库排序"误当成"用户意图"。法禁 skill 必须把这类输入当作**实体解析问题**,而不是普通语义理解问题。

#### 触发条件

出现以下任一情况时进入消歧流程:
- 输入是数字/短词/绰号/半截英文名,如 `2099`、`spider99`、`yoshi`、`squee`、`thrasios combo`。
- `name_translator.py` 失败,但 `card_search.py` 或 Scryfall fuzzy/search 能返回结果。
- 候选牌超过 1 张,或候选中既有常见 commander 又有边缘/无用牌。
- 用户问题包含赛制语境,如"法禁里 2099 怎么样"、"DC 2099 占比"。

#### 候选发现

新增 `card_resolve.py` 或扩展 `card_search.py --candidates`:

```bash
python3 raw/tools/mtg_wiki/card_resolve.py "2099" --format duel-commander --intent commander
```

输出不应只有一张牌,而应是候选列表:

```json
{
  "query": "2099",
  "format": "duel-commander",
  "candidates": [
    {
      "name": "Spider-Man 2099, Miguel O'Hara",
      "match_reason": ["name_contains", "legendary_creature", "duel_legal"],
      "format_signals": ["seen_in_dc_meta_or_content"],
      "confidence": 0.91
    }
  ],
  "needs_clarification": false
}
```

候选发现来源:
- 官方牌名/别名/中文译名索引;
- substring/fuzzy 搜索;
- `wiki/branches/strategy/duel-commander/**` 中的 commander、cards_cited、正文提及;
- meta snapshot 的出现率或样本提及;
- banlist 合法性。

#### 压力测试样例（本地工具暴露的问题）

用现有 `card_search.py` / `name_translator.py` 模拟法禁玩家常用简称,可见它们会把歧义压扁成单一结果:

| 输入 | 现有工具可能输出 | 失败类型 | 法禁解析应做什么 |
|------|------------------|----------|------------------|
| `spider99` | `Spider` token | 缩写未命中,退化到宽泛 fuzzy/substring | 查 alias/meta,解析到实际法禁简称候选,否则追问 |
| `phelia` | `Aphelia, Viper Whisperer` | 字符串相近但语境错误 | 优先法禁内容块中的 Phelia 候选 |
| `tivit` | `End the Festivities` / 译名"喜庆终结" | fuzzy 误伤普通牌 | 若问题是法禁 commander/meta,优先传奇 commander 候选 |
| `kess` | `Kessig Wolf Run` | 前缀/相似度误伤非 commander | commander 语境下优先 `Kess, Dissident Mage` 等候选 |
| `niv` | `University Campus` / 译名"洁尸客" | 短词过短,搜索噪声极大 | 必须列 `Niv-Mizzet` 系候选并追问或按 meta 重排 |
| `squee` | `Squee, Goblin Nabob` 或译名指向 `Slimefoot and Squee` | 单名与组合名冲突 | 结合当前 DC meta/内容块判断用户是否指组合 commander |
| `slimefoot` | `Slimefoot, the Stowaway` 或译名指向 `Slimefoot and Squee` | 单名与组合名冲突 | 若法禁 meta 语境高频为组合 commander,优先组合名并标注 |
| `aragorn` | 某一个 Aragorn 版本 | 多版本同名角色 | 按法禁内容块/颜色/commander 使用率重排,否则列版本 |
| `atraxa` | `Atraxa, Grand Unifier` | 多版本同名角色 | 若 deck/meta 指向另一 Atraxa,不得靠数据库默认版本 |

结论:现有 `card_search.py` 是**查单卡详情工具**,不是**实体解析器**。法禁 skill 应把它放在 resolver 的候选详情阶段,不能把它作为最终 disambiguation。

#### resolver 工具设计

新增 `raw/tools/mtg_wiki/card_resolve.py`,输出候选而非单结果:

```bash
python3 raw/tools/mtg_wiki/card_resolve.py "kess" --format duel-commander --intent commander
```

建议输出字段:

```json
{
  "query": "kess",
  "format": "duel-commander",
  "intent": "commander",
  "candidates": [
    {
      "name": "Kess, Dissident Mage",
      "score": 0.86,
      "reasons": ["legendary", "name_prefix", "dc_alias_or_content_hit"],
      "warnings": []
    },
    {
      "name": "Kessig Wolf Run",
      "score": 0.22,
      "reasons": ["name_prefix"],
      "warnings": ["not_legendary", "unlikely_commander_intent"]
    }
  ],
  "selected": "Kess, Dissident Mage",
  "needs_clarification": false
}
```

评分信号:
- `exact_alias`: +100;
- `dc_content_hit`: +40,按 `commander` frontmatter > `cards_cited` > 正文提及排序;
- `legendary_commander_candidate` 且 intent=commander: +30;
- `duel_legal`: +20;
- `banned_as_commander` 且 intent=commander: -80;
- `not_legendary` 且 intent=commander: -40;
- `short_query_noise`(长度<=4 且无 alias):触发候选展示/追问;
- `string_similarity`: 只作为最后一层,不得压过 format/context 信号。

resolver 的实现可以先不复杂:读取 alias 表 + 遍历本地 oracle name index + 搜索 `duel-commander/**` 的 frontmatter/正文,再用 `card_search.py` 给候选补全详情。

#### 法禁语境重排

候选排序不按数据库默认顺序,而按以下权重:

1. **明确上下文匹配**:用户说"法禁/duel commander/DC/指挥官/套牌/meta"时,优先 commander 候选与法禁内容块中出现过的候选。
2. **合法性**:不合法、全面禁用、仅禁作指挥官的候选降权或标注;如果用户问 deck commander,`banned_as_commander` 候选不能默认选中。
3. **格式使用信号**:在 `dc-meta`、`dc-deck`、`dc-card-eval` 中出现越多,置信度越高;没有来源只能作为低置信候选。
4. **牌张角色**:传奇生物/鹏洛客且可作 commander 的候选,在"法禁 2099"语境下优先于普通 99 单卡。
5. **名字匹配质量**:全名包含、别名表命中、中文译名命中优先于宽泛 fuzzy。

#### 低置信处理

如果最高候选置信度低于阈值(建议 0.75),或前两名差距小于 0.15,skill 必须追问:

> 你说的 `2099` 可能是 A 或 B。你是在问法禁中作为指挥官的 A,还是另一张牌?

不得在低置信时直接生成策略建议。若用户问题中已有"法禁 meta/占比/指挥官"上下文,可以先给出最可能候选,但必须标注:

> 我按法禁语境将 `2099` 解析为 `Spider-Man 2099, Miguel O'Hara`;若你指另一张牌请纠正。

#### 别名表

新增 `wiki/branches/strategy/duel-commander/aliases.md` 或 `raw/data/format_aliases/duel-commander.json`,由维护者/社区 PR 更新:

```yaml
aliases:
  "2099":
    preferred: "Spider-Man 2099, Miguel O'Hara"
    format: duel-commander
    reason: "DC meta shorthand; commander usage signal"
    as_of: YYYY-MM-DD
    sources: [...]
```

别名不是事实本体,只是解析提示。别名必须带 `as_of` 与来源;过期或争议别名可标 `disputed: true`。

#### skill 写法要求

`duel-commander-breaker/SKILL.md` 中必须加入:

```markdown
## 牌名/简称消歧

当用户输入短名、数字、绰号或部分牌名时,不得直接采用 `card_search.py` 的第一个结果。
必须:
1. 调用候选解析工具或同时检索 aliases、dc 内容块和牌名索引;
2. 按 duel-commander 语境重排候选;
3. 若低置信或多候选接近,先追问;
4. 输出中说明"我将 X 解析为 Y"并给出可纠正空间。
```

这样解决的是**实体解析/检索重排**问题,不是单纯 prompt 语义问题。

---

## 四、禁牌表快照（单一事实源 + 硬校验）

### 4.1 快照文件
`wiki/branches/strategy/duel-commander/banlist/<YYYY-MM-DD>-banlist.md`：
```yaml
---
created/updated: ...
type: synthesis
block: dc-banlist
format: duel-commander
banlist_as_of: 2026-06-18
sources: ["<source-registry.banlist_canonical_url>"]  # 官方 B&R 来源（P1/P3）
banned:                          # ★放 frontmatter（非正文）→ 现有 parse_frontmatter 零成本解析
  - "Sol Ring"                   # 全面禁用：比对 commander + cards_cited（按归一化 EN 面）
  - ...
banned_as_commander:             # ★仅禁作指挥官：只比对 commander 字段
  - "..."
generated_by: fetch_dc_banlist.py # ★自动生成标记（区别于人工编辑）
source_hash: <抓取页面校验和>     # ★卫生检查用：结构突变检测
---
# Duel Commander 禁牌表（2026-06-18）
（正文为人类可读说明 + 官方更新周期；牌名以 EN 为准，可选双语展示）
```
- **拆两类(法禁核心特征,reviewer B3/领域 B1)**:`banned`=整副禁(指挥官区+99);`banned_as_commander`=仅禁放指挥官区、仍可作 99 普通牌。扁平单表会双向误判。
  - 实测 duelcommander.com 的 class 正好对应:`ban-item banned`(88 张)→ `banned`;`ban-item banned commander-restricted`(24 张)→ `banned_as_commander`;`unbanned` 忽略。
- **banned 列表放 frontmatter**(非正文):复用 `lint` 现有 `parse_frontmatter` 的 block-list 分支,确定性解析(reviewer CI B2)。**牌名存 EN**(抓取输出 EN,比对按归一化 EN 面;CN 可选)。
- **单一事实源**:全模块禁牌判断只认 `banlist/` 快照;套牌/单卡块**不各自重复禁牌清单**(P6)。
- **数据来源 = 自动抓取(改自 v0.2,见 §4.3)**:由 `fetch_dc_banlist.py` 从 source-registry 记录的官方 B&R 端点生成,**定时自动开 PR**,维护者 review+merge(不直接推 main,保留人工把关)。
- **概念页既存表去二源(reviewer B5)**:`wiki/concepts/duel-commander.md:51-66` 已有"特有禁牌示例"表,须标注"**非权威示例,以 banlist/ 最新快照为准**"并指向之(避免 P6 二源;改通用层一行声明走维护者级)。

### 4.2 硬校验（CI）
- 校验基准(**定 Q2,reviewer B2 + CI Q2**):按套牌块的 `banlist_as_of`,取 **`banlist_as_of ≤ 块日期的最新快照**(非全局最新——否则新禁牌误杀旧块);无符合快照则回落最新 + WARN。
- 比对(**reviewer B6**):`commander` 命中 `banned ∪ banned_as_commander` → ERROR;`cards_cited` 仅命中 `banned` → ERROR。比对前 `split_bilingual` + `normalize_name` 归一化 **EN 面**为键(CN 译名变体不影响)。
- 报告指出:哪张牌在 `<banlist_as_of>` 版被禁、属哪类禁。
- **边界**:只对 `format: duel-commander` 块生效(cedh 不受影响)。
- **前置闸门(reviewer N3)**:首份 banlist 快照存在前,deck/meta 块不得合入(仿 ARCHITECTURE §5.4),避免无快照期裸跑跳过。
- `lint` 须校验 `banlist_as_of` 指向**真实存在**的快照文件(P1,reviewer N2)。

### 4.3 banlist 自动化抓取（fetch_dc_banlist.py，定时自动开 PR）

**已实测可行**(2026-06-18 探测 duelcommander.com/banlist/):纯静态 HTML、class 名语义稳定,标准库可解析。实测抓到 88 张 `banned` + 24 张 `banned_as_commander`,牌名清晰、分类准确。

- **脚本 `fetch_dc_banlist.py`**(stdlib-only):
  - 读取 `rules/source-registry.md` 中的 banlist canonical URL(带 UA + timeout + 重试,复用 `fetch_bulk.py` 风格);**先断言 HTTP 200 + Content-Type: text/html**(防 Cloudflare/软 404 返回 200 错误页)。
  - 解析 `class="ban-item banned"`(全面禁)与 `ban-item banned commander-restricted`(仅禁指挥官),`unbanned` 忽略。
  - 输出 §4.1 格式快照。**牌名写入 frontmatter 必须正确 YAML 转义**(reviewer B6:牌名含 `'`/`,`/`//`/`:`/`"`,如 Urza's Saga、Gaea's Cradle、split 牌)——stdlib 无 PyYAML,**用 `json.dumps(name)` 做安全双引号序列化**(合法 YAML、防注入),不裸拼字符串。删除"无注入面"措辞,明确"官网内容=不可信输入"。
- **卫生检查(定:加检查 + 失败不覆盖;确认轮 reviewer2 B4 加固)**:
  - ① 两个列表**分别**做数量断言(`banned`≥50、`banned_as_commander`≥1)与**分别**突变检测(任一列表较上一快照变动 >±50% 或**归零**→失败)——防"class 改动致 24 张全落入 banned"这类分类错位漏判。
  - ② 两个 class 都命中(类名消失=改版→失败)。
  - ③ **canary 断言**:若干长期稳定禁牌(如 Sol Ring、Black Lotus)必须在结果中,否则判为错误页/解析失效。
  - 任一失败 → **报错退出、不生成/不覆盖旧快照**。
- **`source_hash` 语义明确(reviewer B5)**:不是整页哈希(会因广告/日期每次变),而是**对归一化解析结果(两个排序后牌名列表)的哈希**;用途 = "结果无语义变化则不开 PR"(幂等)+ provenance。
- **`banlist_as_of` 锚点(reviewer N1/确认轮 N1)**:优先解析**官网页面声明的禁牌表生效日**;解析不到才回落抓取日(另存 `fetched_at`)。
- **自动化级别(定:定时自动开 PR)**:GitHub Actions `schedule`(如每周)+ `workflow_dispatch` 跑脚本;有 `source_hash` 变化才用 `peter-evans/create-pull-request` 开 PR。
  - **token(reviewer B1)**:**必须用 App token `CEDH_BOT_TOKEN`**(非默认 `GITHUB_TOKEN`)——否则自动 PR 不触发 `cedh-block-validate`,会绕过快照格式校验。permissions: `contents:write`+`pull-requests:write`。
  - **固定分支名(reviewer B2)**:用 `auto/dc-banlist`(非带时间戳),让 create-pull-request **幂等更新同一 PR**,避免周期任务堆积重复 PR。
  - **无递归(reviewer B3)**:fetch workflow 只挂 `schedule`+`workflow_dispatch`(不挂 push/pull_request);开出的 PR 只触发 validate、不再触发 fetch。
  - **add-paths** 限 `duel-commander/banlist/**`。
- **失败通知 + 人工兜底(reviewer B7)**:GitHub 默认**不通知**定时 workflow 失败 → 须显式配置(失败时自动开 issue 或通知步骤)。人工兜底:维护者可手改快照并把 `generated_by` 标记改为 `manual`,**lint 接受 `manual` 快照**(不强制 generated_by=脚本)。
- **维护者 review 要求(reviewer B4)**:banlist PR 不能"格式过就 merge"——须**人工 diff 牌名清单**(防官网被改/删单张牌漏放),这是"不直推 main"的核心兜底。
- **安全**:固定官方 HTTPS URL(无 SSRF),但解析内容视为不可信(见上 YAML 转义)。
- **同日二次抓取(reviewer N2)**:`<YYYY-MM-DD>-banlist.md` 同日重跑,若 `source_hash` 无变化则不开 PR;有变化则覆盖当日文件(同日以最新为准)。
- **与硬校验的关系**:自动 PR 合并后成为新快照;套牌块按各自 `banlist_as_of ≤ 之` 取对应快照(§4.2),互不耦合。
  - **取舍声明(reviewer N3)**:旧 deck 块**永按其 banlist_as_of 对应快照判合法**,后续新禁牌不回溯重检——这是有意取舍(块声明依据哪版就按哪版),非 bug。

---

## 五、CI/校验泛化（lint_strategy_block.py）

把现有 `lint_cedh_block.py` **泛化**为 `lint_strategy_block.py`,一份管所有赛制。**按 format 查表**改造的硬编码(reviewer B3/B4 + 确认轮补全清单):
- `BLOCKS`、`ARCHETYPE_ENUM`(已是 format-keyed)、`EXHAUSTIVE/SUBSET/EXEMPT`、`CEDH_DIR`、`changed_files` 路径过滤、`if fmt != "cedh"`、cedh-meta 的 sources 校验、cedh-deck 的 pair_type。
- **`REQUIRED_FIELDS`(:42)按 format+block 分表**:cedh→`as_of`;dc 的 deck/meta→`as_of`+`banlist_as_of`;dc 其它块→`as_of`。
- **★日期校验循环(`lint_cedh_block.py:147` 的 `for df in ("created","updated","as_of")`)也是漏网硬编码(确认轮 reviewer3 B2)**:须按 format 加入 `banlist_as_of` 的 YYYY-MM-DD 断言,否则 dc 的 banlist_as_of 永不被格式校验。
- **块名枚举显式补全**:dc 的 5 块 = `dc-deck`/`dc-meta`/`dc-decision-tree`/`dc-combo`/`dc-card-eval` + `dc-banlist`(确认轮 N-d)。
- format 表:`cedh`→{Turbo,Stax,Midrange,Adaptive}/目录 `cedh/`;`duel-commander`→{Aggro,Control,Midrange,Combo,Stax,Voltron,Tempo}/目录 `duel-commander/`。
- **新增**:`format: duel-commander` 套牌块跑禁牌硬校验(读 §4.2 对应 banlist 快照)。
- 正文一致性检查的归一化(`:190`)若改用抽取后的 `normalize_name`,cedh 块 WARN 集合会轻微漂移(仅 warning 不挡合并);**决定:保留 lint 原 `\s` 归一化语义,避免漂移**(确认轮 N-c)。

**`verify_cards.py` 也必须改(撤回 v0.1 的"不用改",reviewer B1)**:其 `CEDH_DIR` 与 `changed_files` 路径过滤(`verify_cards.py:37/148`)只认 cedh 目录,dc 块的 cards_cited 会被静默跳过(破 P2/P4)。改:把目录集合提为 `STRATEGY_DIRS`(cedh + duel-commander + 未来),lint 与 verify 共用。oracle 查证逻辑本身赛制无关,确实不改。

**抽公共函数到 utils.py(reviewer B6)**:`split_bilingual` / `normalize_name`(及目录集合)抽到 `utils.py`,`lint_strategy_block.py` 与 `verify_cards.py` 共用,禁牌比对与牌名查证用同一份归一化,避免两份漂移。

**改名连带改动(同 PR 原子完成,reviewer B4/B5)**:`lint_cedh_block.py → lint_strategy_block.py` 会断引用,须同步:
- `.github/workflows/cedh-block-validate.yml`(引用旧名 + paths 增 `duel-commander/**`、`_templates/dc-*.md`)
- `.github/CONTRIBUTING.md`(引用旧名)
- 脚本自身 docstring
- 可留一行 `lint_cedh_block.py` shim 转发新模块(防外部/缓存调用断裂)
- `wiki/log.md` 历史日志**不改**(append-only)

**render/issue 表单泛化(reviewer B4,严重低估项)**:`render_cedh_issue.py` 与 `cedh-issue-to-pr.yml` 是 cedh 全硬编码(路径/BLOCK_MAP/ARCH_OK 4类/写死 format:cedh/add-paths 限 cedh/**)。须参数化或各开 dc 版。**GitHub Issue Form dropdown 是静态的**(cedh 4 类 vs dc 7 类 archetype 无法按 format 条件切换)→ **定:开独立 dc 版**(`render_dc_issue.py` 复制脚本 + 独立 `dc-block.yml` 表单)。dc 版 issue-to-pr 的具体改点(确认轮 N-b):新 label `dc-block`(对应 `if:` 门控 + ISSUE_TEMPLATE)、`template-path: dc-block.yml`、branch/commit/title 前缀 `dc-`、**`add-paths: duel-commander/**`**、复用 `CEDH_BOT_TOKEN`。dc render 脚本含 `as_of`+`banlist_as_of`(非 cedh 单 as_of)。

**workflow 命名(reviewer N4 + 确认轮 reviewer3 B3 严重警示)**:**不可裸改名** `cedh-block-validate.yml`——它的 job 名是维护者手动配的 branch protection required check,改名 → 旧 check 名消失 → **所有 PR 永久 hang**(正是原设计极力规避的死锁)。**定:保留 `cedh-block-validate.yml` 文件名/job 名,仅在内部 paths-filter 增 `duel-commander/**` + `_templates/dc-*.md`**(零运维风险)。banlist 自动 PR 也由它校验。

**向后兼容**:cedh 现有块校验行为不变(泛化只按 format 分流)。

---

## 六、skill：duel-commander-breaker（v0.8 已建种子版）

- L3 实例,占"赛制策略 × Duel Commander"格。
- description:专属定位(法禁 1v1/20 血/法国禁牌表/无指挥官伤害)+ 让渡边界(规则→judge;多人 cEDH→cedh;通用→wiki)。
- 消费 `wiki/concepts/duel-commander.md` + `branches/strategy/duel-commander/`。
- 遵 `.github/CONTRIBUTING.md` 社区贡献流程。
- 须合法 frontmatter(P8);当前已新增 `skill/duel-commander-breaker/SKILL.md`,后续仍需在目标运行环境执行 skill 加载验证。
- **领域内容由素材填充**(架构只倒逼边界/接口,不产出 meta 数据,守 P3)。

---

## 七、实施顺序（待提案定稿后）

```
① 建 duel-commander/ 目录骨架 + banlist/ 子目录
② 写 `duel-commander/index.md` + 5 个 duel-commander 模板 + 1 个 banlist 快照模板（_templates/dc-*.md 或泛化模板）
③ 泛化 lint_cedh_block.py → lint_strategy_block.py（按 format 分流 + 禁牌硬校验）；抽 split_bilingual/normalize_name 到 utils.py；泛化 verify_cards.py 的 STRATEGY_DIRS
④ 写 fetch_dc_banlist.py（抓取 + 卫生检查）+ 定时 workflow（有 diff 自动开 PR）；跑出首份 banlist 快照
⑤ 泛化/新增 CI workflow paths（duel-commander/**）+ 独立 dc Issue 表单（7 类 archetype）+ render 参数化；改名连带（CONTRIBUTING/docstring/shim）
⑥ 建首批种子内容（最小 meta 快照占位 + 代表 deck stub/待补清单），确保模块不是空壳
⑦ 建 duel-commander-breaker/SKILL.md，opencode debug skill 验证加载
⑧ 概念页既存禁牌表标"非权威"、修引用、更新 strategy/wiki 索引、按验收矩阵跑检查、记 log
```
每步可独立 gate、可回退、记 log（P11）。

### 当前落地状态（v0.8）

- 已完成:① 目录骨架;② `duel-commander/index.md`、6 个模板、`rules/source-registry.md`;⑥ 最小 meta seed + 2 个代表 deck stub;⑦ `duel-commander-breaker/SKILL.md`;⑧ strategy/wiki 索引入口。
- 待完成:③ `lint_strategy_block.py` 与 `verify_cards.py` 泛化;④ `fetch_dc_banlist.py` 与自动 PR;⑤ workflow paths、dc issue 表单与 render 脚本;首份真实 banlist 快照。

---

## 八、开放问题（v0.2 多数已收敛）

1. ✅ **banlist 布局**:按日期多快照(`<YYYY-MM-DD>-banlist.md`),文件名日期天然排序,**无需 current 标记**(reviewer N1)。
2. ✅ **校验基准**:按块 `banlist_as_of`,取 **`banlist_as_of ≤ 块日期的最新快照**(无符合则最新+WARN)。已写入 §4.2。
3. ✅ **改名连带**:已列同 PR 原子项(workflow/CONTRIBUTING/docstring/shim),见 §5。
4. ✅ **partner/双将**:与 cedh `commander`/`pair_type` 语法一致复用,确认。
5. ✅ **专属正文章节**:已定 → 先后手(play/draw)+ London mulligan,区别于 cedh pod 政治(§3)。

**仍开放(非阻塞)**:
- Leviathan / EU DC 变体(概念页提及)未来是否复用本模块 banlist 机制?(预留,本轮不做,reviewer N6)
- 概念页 frontmatter `sources` 与禁牌主张来源不符,迁移期顺手修(reviewer N5)。
