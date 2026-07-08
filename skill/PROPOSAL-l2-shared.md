# 提案：抽取 L2 公共能力层（`skill/_shared/mtg-common.md`）

- 文档地位：落地 `ARCHITECTURE-mtg-skills.md` 的 **L2 公共能力层**——把多个 L3 领域 skill（mtg-wiki / mtg-judge-zh / modern-breaker / 未来 cedh-breaker）重复声明的公共契约抽成**单一事实源**，各 skill 与 agent **显式引用**而非各自粘贴。
- 版本：**v0.4（实体解析补充）**——在 v0.3 已收敛基础上,补入全局牌名/简称实体解析契约。**待用户放行后实施。**
- 创建：2026-06-18　更新：2026-06-18
- 上位约束：`CONSTITUTION.md`（P6 单一事实源、P5 不破坏通用层、P11 破坏性变更可回退+记 log）、`ARCHITECTURE-mtg-skills.md`（L1/L2/L3 分层）、`.github/CONTRIBUTING.md`（社区内容块贡献规范）。

> 用户决策固化：L2 落地用**显式 Read 引用**（不依赖 `opencode.json` instructions 是否注入子 agent——该项本环境无法实测、docs 未载）。

---

## 一、为什么要抽 L2（问题陈述）

公共契约**散落且重复**，存在漂移风险（违反 P6）：工具脚本路径、牌名双语格式、引用格式在 `skill/*/SKILL.md`、`agent/*.md` 多处各写一遍；现状路径前缀已不一致（SKILL.md 用 `./raw/...`，agent 用 `raw/...`）。

---

## 二、L2 内容范围（`skill/_shared/mtg-common.md` 拟收录）

**原则：L2 只持"指针 + 操作契约"，事实本体留 L1（概念页）/ `schema/*.json`。** 这是满足 P6 的关键——把"详略差异"误当"分工"会制造二源。

1. **工具契约**：**7 个**脚本的路径、输入/输出约定、调用示例：
   `card_resolve.py` / `card_search.py` / `name_translator.py` / `rule_search.py` / `scryfall_rulings.py` / `mtgch_name_index.py` / `validation.py`（均在 `./raw/tools/mtg_wiki/`）。L2 是工具路径的**唯一事实源**。
2. **牌名双语规范 + 实体解析契约**：首次「中文（English）」、后续「中文」；必须经 `card_resolve.py` / `card_search.py` / `name_translator.py` 查证，禁凭记忆。短名、数字、绰号、半截牌名、多版本角色名必须先解析候选,不得直接采用单结果 fuzzy。
3. **层系统**：**只放"何时该查层系统"的操作指引 + `[[concepts/...]]` 指针**；CR 613 的 7 层顺序、613.6 跨层/613.8 从属等**事实本体不在 L2 复制**，唯一权威留概念页（L1）。
   > 注：此举同时收口 `ARCHITECTURE-mtg-skills.md` 把"层系统速查"列入 L2 的张力——以"L2 仅指针、L1 持事实"为准。
4. **引用格式**：`[[WikiLink]]`、`file:line`、规则号（CR/MTR/IPG）、数据时效 `as_of` 标注规范；明确**唯一相对路径前缀风格**（见第六节）。
5. **Schema 路径索引**：只列 `./schema/*.json` 的**文件名 + 一句用途**，**不复制任何字段级内容（含字段名清单）**；字段一律"以 json 为准，需要时 Read"。（避免字段名本身成为随 json 增删而漂移的二源）

> 排除项：各 skill 工作流（judge 4-step、wiki 五大能力、cedh 内容块）留各自 SKILL.md。**judge SKILL.md Step1-3 内联的完整 JSON 示例属"工作流产出契约"，保留不删**（它不是重复契约，是 agent 必须照此输出的可操作格式）。

### 全局实体解析契约(v0.4)

`card_search.py` 的职责是"给定确定牌名后查牌面详情";`card_resolve.py` 的职责是"从用户输入解析候选实体"。所有 skill 必须按以下顺序处理牌名:

1. 若用户输入是完整官方牌名或中文官方译名,可直接 `card_search.py` / `name_translator.py` 查证。
2. 若输入是短名、数字、绰号、半截名、套牌简称、组合技简称或多版本角色名,必须先调用 `card_resolve.py` 或等价候选流程。
3. `card_resolve.py` 输出候选列表、score、reasons、warnings、selected、needs_clarification。
4. L3 skill 只提供 `--format` 与 `--intent`:
   - `--format cedh --intent deck|commander|combo|card`
   - `--format duel-commander --intent commander|deck|meta|card`
   - `--format modern --intent deck|card|archetype`
   - `--format judge --intent card|rule|interaction`
5. 低置信或候选接近时先追问;自动选择时必须说明"我将 X 解析为 Y"。

候选重排的公共信号:
- alias 命中;
- 官方名/中文译名匹配;
- wiki 内容块命中(标题/frontmatter 高于正文);
- 格式合法性;
- 角色适配(intent=commander 时传奇且可作指挥官加权);
- banlist/禁用状态;
- 字符串相似度(只作最后一层,不得压过格式语境)。

赛制专属信号由 L3 提供,但算法留 L2:
- cEDH:pod/meta、组合技组件、常见 deck 名称、partner pair。
- Duel Commander:commander 使用率、banlist、局间换将、法禁别名。
- Modern:archetype/deck 名称优先于单卡 fuzzy。
- Judge:若实体不确定,不得给规则结论;必须先澄清牌名。

### L2 自身结构契约（升级为实施前置）
`mtg-common.md` 虽非 SKILL.md（不受 frontmatter/name 约束、不会被 `skills.paths` 当 skill 加载），但作为单一事实源须有最小规范：**固定 5 节锚点（对应上面 1-5）+ 领域红线（路径真实存在 / 牌名双语查证 / 规则号不编造）**，并配 lint 校验（见第五节），防 L2 自身漂移。

---

## 三、落地机制（主 agent 注入为主通路，修正自 v0.1）

**v0.1 的"让子 agent 自己 Read L2"不可靠**：子 agent 是通用体，只执行主 agent 注入到 prompt 的文本；"按 L2 契约执行"是软引用，不保证它真去 Read。修正为：

**主通路（确定性最高）——主 agent 编排时注入：**
- 各 `SKILL.md` 编排步骤中，凡需调用子 agent 处，先 `Read ./skill/_shared/mtg-common.md`，**连同 agent 定义一起拼进子 agent prompt**。子 agent 无需自读，契约必到。
- 主 agent 直接用 Bash 的路径（card-lookup/rule-lookup 多走主 agent），主 agent 自己 Read 一次 L2 即可，确定可控。

**子 agent 自读（仅作兜底，不作主依赖）：**
- 若个别 agent 仍需自读，其顶部写**强命令式第一步**："第一步（强制）：`Read ./skill/_shared/mtg-common.md`，未读取不得执行后续步骤"，并保留最小内联 fallback（读取失败时的关键路径），避免单点失败。

### 接入点（拟改动清单，已补齐遗漏）
1. `skill/mtg-wiki/SKILL.md`：加 L2 引用；删除已迁入 L2 的重复**工具路径/牌名格式**段（层系统速查按第六节 N 项处理）。
2. `skill/mtg-judge-zh/SKILL.md`："关键路径说明/工具脚本位置"改引用 L2；**Step 内联 JSON 示例保留**。
3. `skill/modern-breaker/SKILL.md`：加 L2 引用（牌名/引用格式）。
4. `agent/*.md` 全量复核（**补齐 v0.1 遗漏的两个**）：
   - card-lookup / rule-lookup / ruling-lookup / interaction-analyzer / checker / query-decomposer
   - **`agent/mtg-judge-zh.md`（~36KB，硬编码工具路径最密集）**、**`agent/mtg-wiki.md`**
   - 处理方式：硬编码工具路径/schema 路径改为由主 agent 注入的 L2 契约；本轮若某文件暂不收敛，须显式声明并说明为何不破坏 P6。
5. ~~`opencode.json` 加 instructions~~ **本轮删除此步**：主通路已是显式 Read/注入；instructions 对子 agent 收益不确定、对主会话确定膨胀且与 Read 重复加载。降为后续独立小变更，缩小爆炸半径。

---

## 四、迁移顺序与回退（固化 gate）

**硬规则：L2 未建成并通过机器校验前，不得删除任何 SKILL.md/agent 段落。**

```
① 建 ./skill/_shared/mtg-common.md → 过机器校验（路径真实 / schema 文件存在 / 无字段级复制）
② 逐文件改引用+删重复段，每改一个立即 `opencode debug skill` 验证三 skill 仍加载
③ 跑端到端冒烟测试（见第五节）
④（本轮不做 opencode.json 变更）
```
每步可独立 git 回退；全程逐 diff、记 `wiki/log.md`（P11）。

**实施前必须产出"逐行删除清单"**：列明"哪个文件第几行删 → 对应 L2 哪节覆盖"，作为第五节人工校验的输入；无逐行对照，"迁移无信息丢失"不可核验。已知需逐行界定的高密度区（mtg-wiki SKILL.md）：关键规则速查、跨层/从属、回合结构+APNAP、完整规则文件表、层系统速查表——逐条判定"迁/留/删"。

---

## 五、校验计划（分机器/人工）

**【机器】**
- `mtg-common.md` 存在；其引用的每条路径逐条 `test -f` 解析通过（含 7 个工具、`./schema/*.json`；若 `card_resolve.py` 尚未落地,实施 PR 必须同步新增或将其标为待建且不得删除旧牌名流程）。
- 断言 L2 **不含** schema 字段级内容（含字段名清单）、不含 CR 613 层序事实本体（防二源）。
- 改动后 `opencode debug skill`（三 skill 加载）+ `opencode debug config`（配置解析）通过。
- （前置）lint 脚本：校验 L2 路径真实 + schema 文件存在，从开放问题升级为实施前置。

**【人工】**
- 逐行删除清单对照：被删段在 L2 有等价覆盖，无信息丢失（重点核对 `mtgch_name_index.py`、judge 内联 schema 示例是否误删）。
- 牌名/层系统/引用口径与概念页不矛盾（P6）。
- **端到端冒烟测试**（验证主通路真生效的唯一手段）：跑 1 个标准 judge 查询（如"践踏怎么运作"）+ 1 个牌名互动查询，确认工具路径解析成功、agent 输出过 Schema 校验、结论未丢信息。

---

## 六、相对路径口径（统一，作为引用格式事实源的一部分）

- **唯一前缀风格：`./` 开头，基准为项目根 / cwd**（与现有 `./raw`、`./agent`、`./schema` 一致），不是"相对引用文件自身目录"。L2 文档显式写明这一句。
- 全提案与后续实施统一用 `./skill/_shared/mtg-common.md`；现状 agent 里的 `raw/...`（无 `./`）在迁移触及时一并规整。

---

## 七、剩余开放问题（v0.2 收敛后仅存非阻塞项）

1. 惰性 Read：是否在接入措辞里写"仅在该次任务需要工具/Schema 时才 Read L2"以控 token？（建议采纳，写入 SKILL.md 编排）
2. `agent/mtg-judge-zh.md` 36KB 的硬编码工具路径，本轮全收敛还是分期？（影响改动面，需用户定节奏）
3. lint 脚本范围：仅校 L2，还是顺带校 cedh 内容块 frontmatter（与 ARCHITECTURE-cedh-skill.md 第五节合并）？

---

## 附：v0.1 → v0.2 变更摘要（评审收敛）

| 来源 | blocking 项 | v0.2 处置 |
|------|-----------|-----------|
| 机制/架构 | 子 agent 不会自读 L2 | 改"主 agent 注入"为主通路（第三节） |
| 架构 P6 | 层系统速查在 L2 复制事实 | L2 只留指针，事实留概念页（二.3） |
| 架构 P6 / 规范 | Schema 字段摘要=二源；judge 内联示例误删 | L2 只索引、不复制字段；judge 内联示例保留（二.5/排除项） |
| 规范 | 漏 agent/mtg-judge-zh.md、mtg-wiki.md | 补入接入清单（三.4） |
| 规范 | 工具清单漏 mtgch_name_index.py | 补为 6 个工具（二.1） |
| 规范 | 无逐行删除清单 | 列为实施前必产物（第四节） |
| 规范/机制 | 迁移顺序/回退未固化；校验不足 | 固化"先建后删"gate + 端到端冒烟测试（四/五） |
| 机制/架构/规范 | opencode.json instructions 副作用 | 本轮删除步骤5（三.4-5） |
| 机制/规范 | 相对路径前缀不一致 | 统一 `./` 基准项目根（第六节） |
| 规范 | L2 自身无结构契约/lint | 5 节锚点+红线+lint 前置（二末） |
