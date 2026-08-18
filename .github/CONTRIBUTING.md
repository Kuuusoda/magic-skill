# 贡献策略内容块（GitHub 社区指南）

本指南面向**所有人**：通过 GitHub 提交 cEDH 或 Duel Commander（法禁）策略内容块，**无需在本地安装 opencode 或运行任何脚本**——格式校验与牌名查证都由 CI 自动完成。

> 这是"社区内容块"贡献流程。改 `skill/` 入口、`wiki/concepts/` 通用层、或刷新译名库属**维护者级**操作，不走本流程（见末尾）。

---

## 一、两条提交路径

### 路径 A（推荐 · 零 YAML）
1. cEDH：打开仓库 **Issues → New Issue → 「提交 cEDH 内容块」表单**。
2. 下拉选块类型/原型/配对，文本框填标题、牌名、正文。牌名写「中文（English）」。
3. 提交。机器人会把表单渲染成规范 `.md` 并**自动开 PR**。
4. 看 PR 上的 CI 结果：绿 → 等维护者评审；红 → 按 CI 报告改（机器人会逐张给出官方牌名）。

Duel Commander 的 Issue 表单与 `render_dc_issue.py` 仍未落地；法禁内容先走路径 B。

### 路径 B（进阶 · 直接改文件）
1. Fork 仓库或用 GitHub 网页编辑。
2. 复制对应模板：
   - cEDH：`wiki/branches/strategy/_templates/cedh-<类型>.md` → `wiki/branches/strategy/cedh/<子目录>/<slug>.md`
   - 法禁：`wiki/branches/strategy/_templates/dc-<类型>.md` → `wiki/branches/strategy/duel-commander/<子目录>/<slug>.md`
3. 填 frontmatter + 正文，发 PR。

两条路径都进入同一 CI 闸门 + 维护者评审。

---

## 二、内容块类型与落点

| 类型 | 目录 | `type` | cards_cited 要求 |
|------|------|--------|------------------|
| 套牌拆解 `cedh-deck` | `cedh/decks/<slug>.md` | synthesis | 核心+关键牌（允许代表性子集） |
| Meta 快照 `cedh-meta` | `cedh/meta-snapshots/YYYY-MM-DD-<slug>.md` | synthesis | 仅点名的代表牌（豁免穷举） |
| 决策树 `cedh-decision-tree` | `cedh/decision-trees/<slug>.md` | decision-tree | 通常空，点名则列 |
| 组合技/Stax锁 `cedh-combo` | `cedh/combos/<slug>.md` | concept | **穷举所有组件牌** |
| 单卡评估 `cedh-card-eval` | `cedh/card-evaluations/<slug>.md` | concept | **穷举（主卡+提及牌）** |
| 法禁套牌拆解 `dc-deck` | `duel-commander/decks/<slug>.md` | synthesis | 核心+关键牌（允许代表性子集） |
| 法禁 Meta 快照 `dc-meta` | `duel-commander/meta-snapshots/YYYY-MM-DD-<slug>.md` | synthesis | 仅点名的代表牌（豁免穷举） |
| 法禁决策树 `dc-decision-tree` | `duel-commander/decision-trees/<slug>.md` | decision-tree | 通常空，点名则列 |
| 法禁组合技/锁 `dc-combo` | `duel-commander/combos/<slug>.md` | concept | **穷举所有组件牌** |
| 法禁单卡评估 `dc-card-eval` | `duel-commander/card-evaluations/<slug>.md` | concept | **穷举（主卡+提及牌）** |
| 法禁禁牌快照 `dc-banlist` | `duel-commander/banlist/YYYY-MM-DD-<slug>.md` | synthesis | 不适用；维护者级来源快照 |

通用 frontmatter 契约字段：`created/updated/type/block/format/status/tags/commander/archetype/sources/as_of/cards_cited`（套牌块另含 `pair_type`）。`status` 取 `seed|stub|draft|verified|deprecated`：seed/stub 不能作为强度、meta 或合法性结论；verified 必须有来源。所有法禁内容块还应标注 `rules_as_of`；法禁 deck/meta 还需 `banlist_as_of` 与 `match_policy`，涉及赛事规则覆盖时补 `event_policy_source`。

---

## 三、CI 会强制校验什么（你不必本地跑）

- **格式**（`lint_strategy_block.py`）：frontmatter 齐全、`type↔block` 映射、`archetype` 按 `format` 取枚举、`as_of`=YYYY-MM-DD、文件落对目录、命名小写短横线、WikiLink 可解析、`cards_cited` 双语格式与穷举度。
- **牌名查证**（`verify_cards.py`，离线索引）：`commander` + `cards_cited` 逐张——英文名存在性、官方中文译名匹配。查不到 → error（新牌例外，走维护者放行）。
- **一致性**（warning）：正文出现的牌名应都在 `cards_cited`。
- **分层守卫**（P5）：社区内容块 PR 不得改 `wiki/concepts|entities|sources|synthesis`；维护者级 PR 改这些路径时由 CODEOWNERS 审批。

CI 红时报告会逐条指出问题（含官方正确牌名）；改完推送，CI 自动重跑。

---

## 四、内容红线（评审会查）

- **牌名双语**「中文（English）」，译名以官方为准（CI 校验）。
- **不编造**牌张/规则/数据/"必胜"策略（宪法 P2/P4）。
- **数据标时效**：meta/占比类必填 `as_of` + `sources`，标明定性 vs 定量，不外推"当前"（P3）。
- **法禁版本边界**：法禁 deck/meta 必须说明所依据的 `banlist_as_of`；问合法性或赛前审计时不得用“最新”倒推旧赛事。
- **法禁禁牌分类**：法禁禁牌快照至少区分 `banned`、`banned_as_commander`、`banned_as_companion`；行侣合法性不能只看 commander/99。
- **来源合规**：`sources` 可公开访问、禁整段复制他人正文（见 CODE_OF_CONDUCT）。

---

## 五、合并条件

**CI 全绿 + 维护者评审 approve**（required status checks + required reviews，由 branch protection 强制）。

---

## 六、修改/纠错与争议（治理）

- **改/纠错已有块**：同走 PR + CI；PR 标注"修订 <文件>"；改 meta/数据须刷新 `updated` 与 `as_of`/`sources`。纠错优先级：事实错 > 时效 > 风格。
- **争议内容**（Tier/评级）：标为定性判断；无共识时以"各方依据并列"呈现（各带 `as_of`+`sources`），不写死结论；必要时块 frontmatter 加 `disputed: true`，由维护者裁量与回退（记 log）。

---

## 七、维护者级操作（不走本流程）

改 `skill/` 入口、`wiki/concepts/` 通用层、`_templates/`、`raw/tools/`、`raw/data/cn_name_index.json`（译名库刷新）、法禁禁牌抓取脚本/官方快照等：由 CODEOWNERS 指定维护者审批，维护者本地验证（如 `opencode debug skill`），记 `wiki/log.md`。
