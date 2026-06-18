# 提案：6 项基础设施修复（R1–R6）

- 文档地位:对 2026-06-18 全景盘点暴露的 6 个隐患的**修复提案**。逐项含 问题/证据、方案、推荐、影响、治理类别、gate。
- 版本:v0.2(已并入 3 位 reviewer 全部 blocking;**待用户放行后逐项实施**)
- 创建:2026-06-18　更新:2026-06-18
- 上位约束:`CONSTITUTION.md`(P1–P12)、`ARCHITECTURE-mtg-skills.md`、`.github/CONTRIBUTING.md`(社区内容块贡献规范)。
- 原则:每项独立可实施、可回退;破坏性项走 P11 gate + 记 log;涉及内容真实性的以工具/文件查证为证(P1/P2)。

> 投放顺序:R5 → R1 → R6 → R2 → R4 → R3。存在**弱依赖**(R2 范围视 R1 是否已删根 SKILL.md;R4 的 P13 动机由 R2 暴露的数据来源问题倒逼),**已由该排序消解**,故可顺序实施而非真正"互不阻塞"。

> 评审收敛(第 1 轮 3 reviewer:架构/宪法、集成实测、领域数据)→ 全 approve-with-changes。v0.2 已并入:R2 修正文件清单(补最强夸大源 + 区分"运行时夸大"vs"构建溯源")、R4 覆盖宪法全部 5 个 OQ、R5 改 P7 + 正本清源前置、R6 改"删/转定性为主非盲迁 + 锁单一权威 + 扩普查范围"。

---

## R1 — 删除根级僵尸 `SKILL.md`

**问题/证据**:项目根 `./SKILL.md`(`name: mtg-wiki`)是旧版重复体——含**非法 frontmatter 字段** `triggers:`(官方只认 5 字段,被忽略)、正文与 `skill/mtg-wiki/SKILL.md` 不同步。`opencode debug skill` 实测**只加载 `skill/mtg-wiki/SKILL.md`**,根级这份**从未被注册**(`skills.paths=["./skill"]` 不含项目根)。

**违反**:P6(同一 skill 两处定义=二源)、混淆维护者。

**方案**:
- **A(推荐)**:`git rm ./SKILL.md`。git 历史保留可追溯,无需另存。
- B:移到 `raw/archive/SKILL.legacy.md` 并加注释"已废弃,正本在 skill/mtg-wiki/"。

**影响**:仅删 1 文件;实测无任何文件 `Read`/引用根级 SKILL.md(待 gate 内再次 grep 确认)。

**治理/gate**(P11 破坏性):
```
① grep 全仓确认无对 ./SKILL.md 的引用(WikiLink/Read 路径)
② git rm(或 git mv 到 archive)
③ opencode debug skill 确认仍是 4 个 skill、mtg-wiki 仍指向 skill/mtg-wiki/
④ 记 log;失败 git checkout 回退
```

---

## R2 — L1 数据层"名实不符"(37k 本地库实为 API-only)

**问题/证据**(已查证):
- `utils.py:24` `ORACLE_CARDS_PATH = raw/data/oracle-cards-lite.json` → **文件不存在**。
- `utils.py:16` `DATA_DIR = raw/tools/mtg_wiki/data` 下 `card_name_index.json` 等 → **不存在**。
- `card_search.py:27-41` 本地索引缺失时回退空 dict → **本地精确/前缀匹配恒空,实际全靠 mtgch/Scryfall API**。
- 但 `SKILL.md`/`mtg-wiki` description 反复宣称"37,230 张牌**本地**数据库""已打包在 skill 目录内"。

**违反**:P3(可信度边界/不外推)、P4(禁编造能力)、架构自列病灶 #5("索引未就绪却宣称已打包")。

**方案**:
- **A(推荐,诚实声明)**:修正"运行时能力"措辞为"**在线 API(mtgch→Scryfall)为主**;本地索引为**可选加速**,需先放置源数据 `raw/data/oracle-cards-lite.json` 并跑 `build_indices.py` 生成,**当前未内置**"。
- B(补数据,**另案**):获取 `oracle-cards-lite.json`(Scryfall bulk 裁剪)入库 + 跑 `build_indices.py`。**但**:体积大、需定期更新、来源/版权与入库策略需单独决策(与 R4 的 P13 联动)——不在本提案承诺,仅记可选增强。

**需改文件清单(实测核定,区分"改"与"留")**:

【必改·运行时能力夸大】
- `skill/mtg-wiki/SKILL.md` 及其 `description`、`skill/mtg-wiki/SKILL_EN.md`
- 根 `SKILL.md`(若 R1 未删则一并改)、`README*`
- `ARCHITECTURE-mtg-skills.md` 病灶 #5 状态
- **`agent/mtg-judge-zh.md:293/312/350`**(最强夸大:"本地 37k 牌库""**O(1) 精确匹配**"——原 v0.1 误写成 agent/mtg-wiki.md,实测在此)
- **`agent/mtg-wiki.md:7`**("**不查网络**…优先本地工具",与 API-only 直接矛盾,须整句改)
- **`wiki/branches/strategy/decks/tameshi-belcher.md:916`**(点名不存在的 `oracle-cards-lite.json` 作"离线查询备用",须删/改)

【勿误伤·构建期溯源统计(保留)】
- `wiki/concepts/*.md` 的"基于 37,230 张…数据概览"、`wiki/synthesis/format-legality-analysis.md`、`wiki/sources/2026-04-14-all-cards-json.md`、`wiki/log.md`——这些描述 Wiki **构建时所用 bulk 数据的历史统计**,非运行时本地库,改之反失真。

**影响**:多处文案修正(非功能改动);不动工具代码。
**治理/gate**:P9 内容修正 + 逐文件 diff + 记 log。**人工核**:改后描述与 `card_search.py` 实际行为一致;严守"运行时夸大改 / 构建溯源留"的边界。

---

## R3 — 落地 L2 公共能力层

**问题**:三个 skill 的工具路径/牌名规范/层系统表/Schema 仍各自重复(P6 漂移)。

**现状**:**已有 `PROPOSAL-l2-shared.md` v0.3(2 轮校验收敛)**。本项**不另起提案**,即"放行实施已收敛的 L2 提案"(主 agent 注入 `skill/_shared/mtg-common.md`、先建后删 gate、端到端冒烟测试)。

**治理**:按 L2 提案第四节 gate 执行;**以 L2 v0.3 评审结论为准,不在本提案重开评审**;破坏性(删 SKILL.md 重复段)需用户放行。

---

## R4 — 宪法 v0.1 草案 → 校验定稿

**问题/证据**:`CONSTITUTION.md` 自称"项目级最高治理规范",却**未走它自己要求的 P9–P12 多轮校验**(头部标 v0.1 草案)。其 5 个 open questions 未决:① 分编完备性;② 每条校验判据可脚本化;③ **P10 批准人/法定人数/平票处理未定义**;④ `wiki/log.md` skill/governance 操作类型格式未定义;⑤ 放置位置与中英文命名。

**违反**:P12(宪法自修订须走 P9–P11)。

**方案**:对宪法跑一轮多视角校验,**逐条收口它自己的 5 个 open questions**(不得默认略过,否则"定稿而未定"违反 P12):
- **OQ1 分编完备性**:复核四编是否覆盖全部已知失败模式;盘点新暴露的需补条款(见 P13)。
- **OQ2 判据可脚本化**:不止"分机器/人工两栏",须**承诺落地** lint 脚本(扩展 `lint_wiki_v2.py`,覆盖 P1 路径真实/P7 frontmatter+断链/P8 skill frontmatter 等机器可校验项);无法脚本化的明确标"人工"。
- **OQ3 P10 批准人**:补批准人(≥1 名人类终批)、法定评审视角数、平票/未决默认不合入(复用 CONTRIBUTING §六口径)。
- **OQ4 log 格式**:操作类型枚举定稿 `ingest|lint|提案|决策|落地|skill-add|governance`。
- **OQ5 放置/命名**:对根级 `CONSTITUTION.md` 与中英文命名给出"维持/调整 + 理由"的明确结论。
- **新增 P13(由 R2 倒逼)**:IP/版权与数据来源合规(Scryfall/WotC/mtgch 数据使用边界)。

递增 **v1.0**,记变更理由。

**治理/gate**:P12→P9–P11。多视角评审 + 记 log + 版本递增。**P13 连锁**:新增 P13 后,**全仓所有"P1–P12"引用须同步更新**(本提案头部、`ARCHITECTURE-*`、`CONTRIBUTING`、自检/评审清单),此项纳入 gate,避免断引用(P1)。

---

## R5 — modern 孤儿页 + affinity 链接消歧(轻量)

**问题/证据**:
- `branches/strategy/index.md` 只链 **12/14** 个 deck:缺 `azorius-control`、`tameshi-belcher`(孤立页,P7 无入链)。
- 裸 `[[affinity|…]]` 在 `decks/boros-energy.md:705`、`decks/tameshi-belcher.md:903` **意指套牌**,但与 `concepts/affinity.md`(关键词"连结")**basename 撞名**,Obsidian 会误解析到概念页。

**违反**:P7(孤立页/链接可解析性与歧义解析)。(原 v0.1 误标 P6——撞名是"不同事实同名致误解析",属 P7 范畴。)

**方案**(实施前须**先正本清源**,reviewer 实测两页数据不可直接填表):
- **链接消歧**:把 `boros-energy.md:705`、`tameshi-belcher.md:903` 的裸 `[[affinity|…]]` 改为 `[[decks/affinity|…]]`(其余 affinity 链接已正确,勿动 `index.md:236`、`artifact.md:49` 指概念页者)。
- **补孤儿页入 index**,但数据须如实:
  - `azorius-control`:页内**无 Tier、无精确占比**(仅"<2.1%、未进 Top12")→ index 填"未进榜 / <2.1% / 样本 14",**不得编造 Tier**。
  - `tameshi-belcher`:页内占比**自相矛盾**(元数据 2.27% vs §6.12 的 2.1%)**且与 `2026-05-01-modern` 快照 Top12 不符**(快照不含此牌)→ **先修页内矛盾、坐实来源**,再填;暂填"Tier 3 / 占比待核 / 样本 15"并标注。

**影响**:链接消歧 2 文件(非破坏、可立即做);补 index 须先解决两页数据问题(查证 P2/P3)。**治理**:P11 记 log;index 数字须与 deck 页一致且不编造。

---

## R6 — 概念页越界(cEDH 时效数据混入通用层)

**问题/证据**(实测核定):`concepts/cedh-deck-archetypes.md`(`sources: []`)混入**无源时效数据**:L160 当前环境占比 ~40/20/30/10%、L136 "Blue Farm 为何是 S Tier"、L169-171 禁牌量化影响("0.5–1 回合")。把时点环境判断混进"可长期复用概念层"。

**违反**:P5(分支时效内容不进通用层)、P3(数据无来源/时效)。

**核心修正(reviewer 指出"盲迁不成立")**:这批数字**多数无源**,迁到 snapshot 仍是无源 meta。正确做法是**以"删/转定性"为主,而非整体迁移**:

| 数据 | 处置 |
|------|------|
| L160 占比 ~40/20/30/10%(无源) | **删或转定性**("Turbo/Midrange 为主流,Stax 次之,Adaptive 最少") |
| L136 Blue Farm S Tier(时效判断) | 概念页不断言 Tier,改 `[[引用]]` meta 快照 |
| L169-171 禁牌影响量化(无源推测) | 删数字或标"定性推测" |
| L166 2024-09 禁牌名单(真实历史) | **保留**,补 `sources` + 日期(核对是否漏列 Nadu) |
| 各原型制胜回合/互动密度(定义性特征) | **保留概念页**(是原型定义,非时点 meta) |
| L25 "Kinnan(T3 无限 Mana)" | **需复核**(疑似套牌速度标签,非确证异能硬伤);若确为速度描述则保留,异能细节让渡 combo 页 |

**单一权威方向(锁定,防 P6 二源)**:**原型定义权威留 `concepts/`;时效占比/Tier 权威在 `meta-snapshots/` 块**,两者**只互相 `[[引用]]`、互不重定义**。(与 `ARCHITECTURE-mtg-skills.md` §5.3"不迁概念页、建薄分支层"对齐——R6 迁的是**数据**不是概念页。)

**范围扩展(同类普查)**:reviewer 实测同目录另两页有同类无源数字,一并纳入:
- `cedh-pod-dynamics.md`(`sources: []`):按位胜率 ~27/25/22%(L31/49/68)——补源或标定性。
- `cedh-data-analysis.md`(`sources: []`):单卡胜率表(Demonic Tutor 62% 等 L100-102)——标"示例/示意"或补来源。

**前置闸门(ARCHITECTURE §5.4)**:编辑这些页时若发现未修硬伤(如 Kinnan 异能),同次顺手修或显式记为闸门,避免改一半留病灶。

**影响**:改 3 概念页(+ 视情新建 meta 快照块);触及通用层(走 P5 更严格评审 + 领域数据评审)。**治理**:P9 提案 + 领域评审 + 记 log。

---

## 附:6 项治理类别与风险一览

| 项 | 类别 | 破坏性 | 触及通用层 | 依赖 |
|----|------|--------|-----------|------|
| R1 删僵尸 SKILL.md | P11 | 是(删文件) | 否 | — |
| R2 数据名实修正 | P9 文案 | 否 | 否 | — |
| R3 落地 L2 | P9/P11 | 是(删重复段) | 否 | L2 提案 v0.3 |
| R4 宪法校验定稿 | P12 | 否 | 否(治理文档) | — |
| R5 孤儿页/链接 | P7/P11 | 否 | 否 | 先正本清源两页数据 |
| R6 概念页越界 | P5/P9 | 否 | **是** | cedh meta 模板(已建) |
