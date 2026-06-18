# 提案：GitHub 社区贡献体系（Fork + PR + CI 强制查证）

- 文档地位:**回滚后重做**的 cEDH 社区协作架构 + 贡献规范 + CI 校验设计三合一提案。取代已回滚的 `ARCHITECTURE-cedh-skill.md`(v0.4) 与 `CONTRIBUTING-mtg-skill.md`(v1.0)。
- 版本:**v0.5(已收敛)**——v0.3 经 2 轮校验全 approve;v0.4 并入用户 4 项裁决(Q1 译名库固定/Q2 采用现成 Action/Q3 补治理第九节/Q4 接受 all-cards);v0.5 并入对新材料的确认评审 blocking:Q2 工具链**安全硬化**(label 门控 + shell/YAML/路径三类注入防护 + App token 降权 + 确定性分支),Q3 治理**去悬空**(9.2 版权自包含不依赖未定稿 P13、9.3 disputed 为 frontmatter 标记不碰 SKILL.md 逻辑、log 归维护者级、Q1 刷新逾期兜底)。**待用户放行后实施。**
- 创建:2026-06-18　更新:2026-06-18
- 上位约束:`CONSTITUTION.md`(P1–P12)、`ARCHITECTURE-mtg-skills.md`(cedh 在 L3、消费 L1、不改通用层 P5)。

> **用户决策固化**:① 所有人 GitHub Fork + PR 提交,贡献者**无需本地装 opencode/跑脚本**;② CI 自动校验且**强制牌名/Oracle 查证**;③ 合并 = CI 全绿 + 维护者 approve;④ 提交单元 = 内容块(不动 SKILL.md)。

> **v0.1→v0.2 关键修正**(评审收敛):强制查证降为"**硬前置依赖:离线索引就绪后**才具备"(不预先宣称);译名库改用 **Scryfall `all-cards` 过滤 `lang=zhs` 离线抽取**(单一源可复现,弃 mtgch+人工单点);补齐 **fork PR 权限模型**、**always-run gate 避免 required-check 死锁**、**bulk 按 updated_at 缓存**;`cards_cited` 定位为**派生索引**;新增 **Issue 表单转 PR** 降门槛;PR 模板去重(只留人工信息);查证分 **error/warning 两级**。

---

## 一、模型总览

```
贡献者(零本地环境)
  │ 1. 走 Issue 表单(结构化填写,推荐) → bot 渲染成合规 .md 开 PR
  │    或 Fork/网页编辑 → 按模板新增/改一个「内容块」.md
  ▼
GitHub Actions CI(自动,base 分支定义,贡献者改不动 → 这是"强制"的前提)
  │ A. 格式校验  frontmatter / 路径 / WikiLink / 目录命名(新写 lint 脚本)
  │ B. 强制查证  commander + cards_cited 逐张:存在性 + 双语 + 官方译名(离线索引)
  │ C. 一致性    正文牌名 ⊆ cards_cited(warning)
  │ D. 分层守卫  PR 只允许改 cedh/** 与 _templates/cedh-*.md(allowlist,P5)
  ▼
维护者评审(领域正确性) + CI required checks 全绿 ──► 合并 ──► 合并后由 default 分支 workflow 记 log
```

核心理念延续:**SKILL.md 是稳定编排器,内容块是数据**。社区加一套套牌 = 加一个文件 + 一个 PR,**不碰 SKILL.md**。

**强制力来自机制(reviewer 指出的正面属性)**:`pull_request` 事件运行的是 **base 分支的 workflow 定义**(非 fork 改过的),贡献者无法改 CI 绕过查证——这是"CI 强制"成立的根本前提。

---

## 二、cEDH 协作架构(GitHub 版)

### 2.1 内容块类型(沿用回滚保留的 5 类模板)

落 `wiki/branches/strategy/cedh/`,模板 `wiki/branches/strategy/_templates/cedh-*.md`:套牌拆解(decks,synthesis)/Meta 快照(meta-snapshots,synthesis)/决策树(decision-trees,decision-tree)/combo-lock(combos,concept)/单卡评估(card-evaluations,concept)。

### 2.2 frontmatter 契约 + `cards_cited`(**派生索引,非第二事实源**)

沿用模板字段,新增机器可查证的牌名清单:
```yaml
cards_cited:                 # 派生索引(非权威):仅供 CI 确定性查证,牌张权威仍是工具查证
  - "塔萨的先知（Thassa's Oracle）"
```
- **定位(消解 P6)**:`cards_cited` 是**非权威派生索引**,不构成第二事实源;牌张权威文本以离线 Oracle 索引/工具查证为准。
- **一致性守卫**:CI 校验"正文出现的牌名 ⊆ cards_cited"(warning 级,防漂移)。
- **强制度按块差异化(定 Q1)**:
  - **穷举必填**:单卡评估、combo-lock(牌少、查证价值高);
  - **核心+关键牌(允许代表性子集)**:套牌拆解(不强求列满 100 张);
  - **豁免穷举**:Meta 快照(只列被定性断言点名的代表牌,CI 对该块降 warning)。
- **可半填**:贡献者可留空/半填,CI 在报告里**回填候选官方名**(见四.3),把查证职责真正归 CI。
- `as_of`/`sources` 按块差异化:Meta 快照强制;combo/单卡的物理事实可不强制 `as_of`(减负)。

### 2.3 同步改动
新增 `cards_cited` 需同步进 5 个模板;并清理模板里指向已回滚 `ARCHITECTURE-cedh-skill` 的注释(如 `cedh-deck.md:4`)。

---

## 三、贡献流程与规范(CONTRIBUTING GitHub 版)

### 3.1 两条提交路径(降门槛)

- **路径 A(推荐·零 YAML)**:GitHub **Issue 表单**(`.github/ISSUE_TEMPLATE/cedh-block.yml`)——下拉选 block/archetype/pair_type、文本框填牌名与正文;提交后 Action 渲染成合规 `.md` 自动开 PR。**避免手写 YAML 易错**,真正兑现"会 GitHub 即可"。
  **工具链(已调研现成方案,Q2):**
  - `stefanbuck/github-issue-parser`(v3,MIT):把 Issue 表单解析成 JSON(`issueparser_<field>`)——成熟的 codeless-contribution 标准件。
  - 小胶水脚本:把 JSON 字段映射成 frontmatter + 正文,写入 `cedh/<type>/<name>.md`。
  - `peter-evans/create-pull-request`(v8,MIT):把渲染文件开成 PR。
  - **关键集成约束**:用默认 `GITHUB_TOKEN` 创建的 PR **不会触发** `on: pull_request` 的校验 CI → 必须用 token。该 Issue→PR workflow 跑在 **`issues` 事件、base 仓库内**,secrets 可用。**首选 fine-grained GitHub App token**(仅 `contents:write`+`pull-requests:write`、短时、可审计),**不用宽权限 classic PAT**;workflow `permissions:` 最小化。
  - 二者均 MIT,与本仓库许可兼容、活跃维护、采用广泛,**采用现成而非自研**。
  - **安全硬化(公开仓库:任何人可开 Issue 触发此高权限 workflow,必须防注入)**:
    - **门控**:`on: issues: types:[opened,edited]` + `if: contains(github.event.issue.labels.*.name,'cedh-block')`;靠 ISSUE_TEMPLATE 自动打 label + workflow `if` 双重门控,避免任意 issue 触发建 PR。
    - **命令注入**:胶水脚本**禁止**在 `run:` 内联 `${{ github.event.issue.* }}`,一律经 `env:` 或中间文件传入由脚本读取。
    - **frontmatter 注入**:JSON→YAML 必须**安全序列化**(强制 quote/escape,禁裸字符串拼接),防用户值含 `:`/`"`/换行/`---` 破坏或新增 frontmatter 键。
    - **路径穿越**:由牌名/name 推导文件名时白名单化(仅小写短横线),拒 `../`、`/`、空字符;渲染期先净化,分层守卫(4.3 step8)只作事后兜底。
    - **create-pull-request 前置**:确定性分支名(如 `issue-<number>`,支持同 Issue 编辑后更新 PR 而非反复新建);若走 GITHUB_TOKEN 路径需开仓库设置"Allow Actions to create PRs"(本方案用 App token,以该身份创建,交付物说明清楚)。
- **路径 B(进阶)**:Fork/网页直接新建 `cedh/<type>/<name>.md`(粘贴模板内容),填 frontmatter + 正文,发 PR。

两条都进入同一 CI + 评审闸门。

### 3.2 PR 模板(只保留**机器无法判断**的人工信息,不与 CI 重复)

`.github/PULL_REQUEST_TEMPLATE.md`:
```markdown
## 内容块类型
- [ ] 套牌拆解 / Meta 快照 / 决策树 / combo-lock / 单卡评估
## 一句话摘要
## 数据来源与信心(meta/占比类必填:来源链接 + 是否定性推测)
## 是否含新牌(bulk 可能未收录,触发维护者放行)  [ ] 是
```
> 字段齐全/双语/分层/一PR一块 等**全部交给 CI**,模板不再让贡献者勾选机器会复核的项(去仪式负担)。

### 3.3 边界:社区 PR vs 维护者级
- **社区内容块 PR**:走本规范 + CI 强制。
- **改 SKILL.md 入口 / 改 wiki/concepts 通用层 / 刷新译名库**:**维护者级**,不走社区 CI 强制,由维护者本地验证(`opencode debug skill`)+ `CODEOWNERS` 限定 + branch protection,呼应宪法 P8/P10。

---

## 四、CI 校验设计(GitHub Actions)

### 4.1 触发与"防死锁"(reviewer B3 致命坑)
**不能**直接用 `on: pull_request: paths:` 再设为 required check——不碰 cedh 路径的 PR 会永远卡 "waiting for status"。改为:
- workflow **始终触发**(`on: pull_request`,不加 paths);
- job 内用 `dorny/paths-filter` 判断是否动了 cedh 内容块;**未命中则主动上报成功**(或拆一个 always-run 的 gate job 汇总),保证 required check 永远会上报。

### 4.2 fork PR 权限模型(reviewer B2,最大风险,固化)
- 用 `pull_request` 事件:对 fork,`GITHUB_TOKEN` **只读**、**secrets 不可用**。本方案查证**不需要任何 secret**(Scryfall 无鉴权、不回写仓库)→ 只读 token 足够,**明确声明 CI 不依赖 secret**。
- **缓存隔离**:`actions/cache` 对 fork 写入隔离。故由 **default 分支的 schedule/push workflow 预热 bulk 缓存**;fork PR 只**只读 restore**,**miss 时回退现网下载**(无 secret 可行)。
- **绝不在 fork PR 的 workflow 写 `wiki/log.md`**(只读 token 写不了;`pull_request_target` 写会引入注入漏洞)。log 由**合并后 default 分支 push workflow** 或维护者补,与查证 workflow 物理隔离。

### 4.3 Job 步骤
```
1. checkout(fetch-depth: 0,以便 diff origin/<base>...HEAD 取改动文件)
2. setup-python
3. 准备离线索引(见五):restore cache → 命中即用;miss 则下载 bulk 生成
4. 格式校验(★ 新写 lint 脚本,非"扩展 validation.py"——后者只做判定流水线 JSON schema):
   frontmatter 必填齐全;type↔block 映射;archetype 按 format 取枚举;as_of=YYYY-MM-DD;
   文件落对目录、命名小写短横线;[[WikiLink]]/路径 test -e
5. 强制牌名查证(error 级,挡合并):
   commander + cards_cited 逐张 → 英文名在离线 Oracle 索引存在 + Oracle 文本非空;
   中文译名 ∈ 离线 CN↔EN 索引;「中文（English）」格式正确(双面/拆分牌 // 特判)
   · 查不到/译名不符 → fail,报告逐张回填官方名 + 可推 suggested change
6. 查证分级:bulk 未收录的新牌 → warning + 需"新牌放行"label(**维护者动作**:fork 贡献者无 base 仓库 write 权限、加不了 label;PR 模板的"含新牌"勾选仅作信号,放行由维护者打 label)
   · 区分"**无索引**"(前置数据全缺)= 查证 job 跳过/标 neutral,与"新牌 warning"不同场景
7. 一致性(warning):正文牌名 ⊆ cards_cited
8. 分层守卫(allowlist,P5):git diff 仅允许 cedh/** 与 _templates/cedh-*.md;
   命中 wiki/concepts|entities|sources|synthesis 等通用层 → fail
9. gate job 汇总 → required check 上报
```

### 4.4 失败友好性(reviewer 贡献者体验 B1)
CI 报告**逐张**列错名 + 官方正确名(不只举一例),并支持 GitHub **suggested change** 一键应用;贡献者改/接受建议后推送,CI 自动重跑,全程零本地环境。

---

## 五、强制查证的可靠性与数据依赖(核心)

**硬前置依赖(reviewer 架构 B1,不预先宣称已具备)**:CI 强制查证依赖两份离线索引,**二者就绪前不得宣称"已具备强制查证"**:
1. **英文 Oracle 索引**:Scryfall bulk `oracle-cards`(经 `/bulk-data` 拿 `download_uri`,**会变,cache key 用其 `updated_at`**;约 30–40MB);经 `build_indices.py` 生成 `card_name_index.json`。
2. **CN↔EN 官方译名索引**:**首选** Scryfall bulk **`all-cards`**(注:`default-cards` 每 oracle 只留一个英文优先印刷,过滤 `lang=zhs` 会几乎为空,**必须用 `all-cards`**)过滤 `lang=="zhs"` 抽 `printed_name`+`oracle_id` 离线生成(**单一源、可在 CI 完全复现、无需 mtgch、无需人工**);mtgch 批量生成降为备选。代价是 all-cards 体积大(数百 MB),同样 cache、仅 default 分支预热跑一次,预热**刷新周期宜短**以收窄 miss 窗口。
   **索引归属与刷新(定 Q1)**:单一事实源固定为 **`raw/data/cn_name_index.json`**(英文 Oracle 索引同理落 `raw/data/`);抽取脚本本提案交付物 6 自建。**刷新责任 = 维护者**,周期 = **每次 Scryfall 新系列发布后 / 至少每月一次**,刷新**走 PR + 评审**(可追溯、防"谁都不刷")。**逾期兜底**:若维护者漏刷致译名库滞后,查不到的牌按 4.3 step6 降为 **warning + 维护者放行**,**不阻塞存量 PR**(刷新逾期≠合并停摆)。数据入库策略与版权仍归 R2(单向)。

**build_indices 对接(reviewer CI B1)**:`oracle-cards` 是 lite 的超集,解析逻辑(全 `card.get`)**无需改**;但 `ORACLE_CARDS_PATH` 是硬编码常量 → 需**加环境变量覆盖**,让 CI 把下载文件指过去,而非伪造 lite 文件名;需确认全量 prefix_index 体积。`name_translator.py` 是逐张 Scryfall API,**不能复用做离线库**,需**新写 bulk 抽取脚本**。

**与 R2 的关系(reviewer 架构 B2,单向不耦合)**:本提案**消费** R2/方案 B 产出的离线索引;**数据入库策略与 IP/版权(R4 待定的 P13)由 R2+P13 决定,本提案不承接**。CI 与本地"共用 `build_indices.py`"仅是实现复用,不改变 R2 的另案边界。**硬依赖顺序**:R2 离线索引未落地前,本提案 CI 查证无数据源、按 4.3 step6 降级。

**残余风险**:bulk 有发布延迟(新牌数日后才进)→ 对 cEDH(老牌为主)影响极小,由新牌 warning + 维护者放行兜底。

---

## 六、与上位文档 / 遗留断引用(走 P9 同步)

- `ARCHITECTURE-mtg-skills.md` 引用已回滚 `CONTRIBUTING-mtg-skill.md` **三处**(§四 L101、§五表 L123、§六 L149)——定稿后一并改为指向本提案产出的新规范。
- `PROPOSAL-repairs.md` R4、`PROPOSAL-cedh-breaker.md` 同样断引用,一并修。
- 模板里指向已回滚 `ARCHITECTURE-cedh-skill` 的注释(`cedh-deck.md:4` 等)清理。
- 备份:被回滚两文件在 `…/claudecode/rollback-2026-06-18/`,可挑拣其"领域红线/正文结构"等仍有效片段并入新规范(非整体恢复)。

## 七、交付物清单(实施期产出)
1. `.github/workflows/cedh-validate.yml`(查证 workflow,含 always-run gate)
2. `.github/workflows/cache-warm.yml`(default 分支预热 bulk 缓存)
3. `.github/ISSUE_TEMPLATE/cedh-block.yml`(Issue 表单)+ 渲染成 PR 的 Action
4. `.github/PULL_REQUEST_TEMPLATE.md`、`.github/CODEOWNERS`
5. 新 lint 脚本(frontmatter/路径/命名/WikiLink/cards_cited 校验)
6. bulk → CN↔EN 离线索引抽取脚本 + `ORACLE_CARDS_PATH` env 覆盖补丁
7. 新贡献规范文档(取代回滚的 CONTRIBUTING,只覆盖内容块 PR)
8. branch protection 配置(required checks + required reviews)
9. `.github/CODE_OF_CONDUCT.md`(行为准则,见 9.2)

## 八、开放问题(用户已裁决,v0.4 收口)
1. ✅ **Q1 译名库**:固定 `raw/data/cn_name_index.json`,维护者刷新、走 PR+评审(见五)。
2. ✅ **Q2 Issue→PR**:**采用现成**(github-issue-parser + create-pull-request + 胶水脚本,均 MIT,见三.1)。
3. ✅ **Q3 治理空白**:**本提案补**——见第九节。
4. ✅ **Q4 all-cards 体积**:**接受**(数百 MB 走 actions/cache,仅 default 分支预热跑一次;预热刷新周期宜短以收窄 miss 窗口)。

---

## 九、社区治理补全(Q3:本提案补)

### 9.1 修改 / 纠错已有内容块
- 改已有块与新增同走 **Fork+PR+CI**;PR 标题/标签标注"修订 <文件>"。
- **纠错优先**:对已合入块的事实错误(牌张/数据),任何人可发"纠错 PR";CI 同样强制查证;维护者优先合并纠错(**优先级判据:事实错 > 数据时效 > 风格**,避免主观)。
- `updated` 字段必须刷新;若改动 meta/数据,`as_of`+`sources` 同步更新(P3)。

### 9.2 行为准则 + 来源版权合法性
- **行为准则**:沿用社区通行 Code of Conduct(交付 `.github/CODE_OF_CONDUCT.md`);PR 讨论保持技术、对事不对人。
- **来源版权(自包含,不依赖未定稿条款)**:`sources` 必须是**可公开访问**的链接;**禁止整段复制**他人 primer/文章正文(只可引用要点 + 注明出处);卡图/牌张文本来自 Scryfall/WotC,遵其使用条款。CI 无法判版权 → 列入**维护者人工评审项**;争议来源不合入。
  > 注:以上规则**本节自包含、立即生效**,不依赖尚未存在的条款。R4 若将 P13(IP/版权)写入宪法,本节再**对齐引用**(非阻塞;在 P13 定稿前不引用它,避免引用空条款违反 P1)。

### 9.3 争议内容(评级/Tier/胜率判断)的处置与回退
- **定性优先**:Tier/评级一律标为**定性判断 + `as_of`**,不冒充定量(P3);有定量来源才可给数字并附 `sources`。
- **争议处置**:对评级类争议,维护者可要求 PR 补来源或降级为"定性"表述;无法达成共识的主观评级**不写死结论**,以"社区存在分歧 + 各方依据"并列呈现(**并列各条目同样各自带 `as_of`+`sources`**,P3)。
- **`disputed` 标记(定义清楚,不碰 SKILL.md 逻辑)**:争议块在**自身 frontmatter** 加 `disputed: true`(+ 一行 `disputed_note`);"降权"= SKILL.md 编排时**读该 frontmatter 标记**对其结论降级处理(与"不碰 SKILL.md"理念一致——改的是数据的标记,非编排逻辑)。**谁打**:维护者;**解除**:争议消解后由维护者去标,走 PR。
- **回退**:已合入块若证伪/来源失效,走纠错 PR(9.1)或 `git revert`。**记 log 归维护者级**(default 分支 workflow 或维护者手动,与 4.2"不在 fork PR 写 log"一致;区别于 9.1 社区纠错 PR),P11。
