---
name: duel-commander-breaker
description: 万智牌 Duel Commander（法禁/法式指挥官）1v1 竞技策略分析。用于法禁 meta、套牌拆解、对局优劣、起手调度、禁牌表版本与规则版本边界、20 血资源判断。当用户明确询问法禁、DC、Duel Commander 或法式指挥官竞技策略时触发。边界：精确规则裁定让渡给 mtg-judge-zh；多人 cEDH 让渡给 cedh 相关 skill；通用牌张查询让渡给 mtg-wiki。
---

# duel-commander-breaker — Duel Commander 法禁策略 Skill

## 触发条件

当用户提出以下类型的问题时触发：
- 法禁 meta 或套牌选择。
- 法禁某个指挥官/套牌的强度、对局、起手、调度。
- 1v1/20 血语境下的资源交换和互动配置。
- 大型赛事备战：牌表审计、对局计划、时间管理、已知对手准备、最后 flex slot 取舍。
- 法禁禁牌表、`banlist_as_of`、`rules_as_of` 相关策略边界。
- “DC”“Duel Commander”“法式指挥官”“法禁”等明确语境。

## 边界

- 精确规则互动、CR/MTR/IPG 判定：交给 `mtg-judge-zh`。
- 多人 cEDH pod、政治、40 血、官方 EDH 禁牌表：交给 cEDH 相关 skill。
- 通用单卡 Oracle 查询：交给 `mtg-wiki`，但本 skill 可先解析法禁语境下的实体。
- 若本库没有策略资料，必须说明资料不足，不得编造 meta。
- 不替用户声称牌表合法；没有 banlist/rules 快照时只能给审计清单和风险点。

## 执行流程

### Step 0: 牌名/简称消歧

短名、数字、绰号、半截名、套牌简称、组合技简称必须先解析实体：

```bash
python3 ./raw/tools/mtg_wiki/card_resolve.py "2099" --format duel-commander --intent commander
python3 ./raw/tools/mtg_wiki/card_resolve.py "kess" --format duel-commander --intent commander
python3 ./raw/tools/mtg_wiki/card_resolve.py "squee/slimefoot" --format duel-commander --intent commander
```

- `needs_clarification=true`：列候选并追问。
- 自动选择时说明“我按法禁语境将 X 解析为 Y”。
- 不得把 `card_search.py` 的第一个 fuzzy 结果当作用户意图。
- 当用户问当前 meta、占比、强度、Tier、热门度或“现在怎么样”时，必须使用 meta evidence gate：

```bash
python3 ./raw/tools/mtg_wiki/card_resolve.py "2099" --format duel-commander --intent commander --require-meta-evidence
python3 ./raw/tools/mtg_wiki/format_meta_evidence.py "2099" --format duel-commander --intent commander
```

- 有 meta evidence 时，回答中标注来源与 `as_of`；无 meta evidence 时，不得把 alias 或 fuzzy 结果当成当前法禁 meta 结论。

### Step 1: 读取法禁入口

优先读取：

```text
wiki/branches/strategy/duel-commander/index.md
wiki/concepts/duel-commander.md
```

### Step 2: 按问题类型读取内容块

Meta 查询：

```text
wiki/branches/strategy/duel-commander/meta-snapshots/*.md
```

套牌分析：

```text
wiki/branches/strategy/duel-commander/decks/[deck-name].md
```

起手/先后手/对局决策：

```text
wiki/branches/strategy/duel-commander/decision-trees/*.md
```

组合技/单卡评估：

```text
wiki/branches/strategy/duel-commander/combos/*.md
wiki/branches/strategy/duel-commander/card-evaluations/*.md
```

禁牌表与规则版本：

```text
wiki/branches/strategy/duel-commander/banlist/*.md
wiki/branches/strategy/duel-commander/rules/*.md
```

### Step 3: 版本边界

回答必须标注：

- `as_of`：策略/样本时效。
- `status`：内容成熟度（`seed/stub/draft/verified/deprecated`）。
- `banlist_as_of`：合法性依据的禁牌表版本。
- `rules_as_of`：规则快照版本。

如果只读到 `seed` / `stub` 或占位快照，必须明确说明“本库尚无足够法禁策略资料”，不得输出强度、Tier、占比、胜率或可参赛合法性结论。

### Step 4: 分析维度

法禁策略回答优先覆盖：

- 用户目标：练习、选套牌、改牌表、赛前审计、现场对局复盘。
- 先手/后手差异。
- London mulligan 起手标准。
- 指挥官依赖度。
- 20 血资源账本。
- T1/T2/T3 节奏基准。
- removal/counter/discard/sweeper/graveyard hate/land hate 的互动配置。
- 地基稳定性：颜色源、横置地密度、1/2/3 回合可行动率、付血地对 race 的影响。
- flex slots：最后 3-8 个可替换卡位按 meta 预期解释，不把 100 张牌表当成固定圣经。
- threat/answer alignment：威胁是否能穿过主流互动，解牌是否能处理主流威胁。
- clock management：BO3/50 默认下的慢速套牌时间计划、何时转进攻、何时保平/争胜。
- known-opponent prep：已知对手指挥官、惯用线、局间调整与心理陷阱。
- Aggro、Control、Midrange、Combo、Stax、Tempo 对局矩阵；Voltron 仅在有实际样本时展开。

### Step 5: 冠军赛压力测试

当用户问“这套能不能打比赛 / 怎么备战 / 怎么调牌 / 法禁环境怎么选套牌”时，必须像赛前测试伙伴一样先检查这些问题：

1. 你按哪个赛事日期、banlist、rules 和 event policy 准备？
2. 你的牌表是否完整到 100 张，是否含 companion、outside-the-game、贴纸/景点/acorn/digital-only 等结构风险？
3. 你的 commander、99 或 companion 是否触及 `banned` / `banned_as_commander` / `banned_as_companion`？
4. 前三回合计划是什么：先手、后手分别要做什么？
5. 7 张、6 张、5 张起手的最低 keep 标准是什么？
6. 对 Aggro、Control、Midrange、Combo、Stax、Tempo 分别有哪些不可输的关键回合？
7. 你的去除、反击、弃牌、扫场、坟场针对、地针对数量是否和预期 meta 对齐？
8. 哪些牌是 flex slots，遇到 meta 偏快/偏控/偏 combo 时怎么换？
9. 指挥官被连续处理两次后，套牌是否还有可执行计划？
10. 50 分钟 BO3 下，你的慢速对局是否容易超时？领先/落后时如何调整速度？
11. 已知热门指挥官或本地常见对手有哪些专门计划？
12. 哪些结论来自数据，哪些只是观察假设？

如果用户没有给牌表或赛事信息，先说明缺失项，再给“可继续分析但置信度较低”的版本。

## 输出要求

- 引用具体 wiki 内容块。
- 区分资料事实、样本结论、个人推断。
- 不写无来源的 Tier、占比、胜率。
- 大型赛事备战问题必须输出缺失信息清单、主要风险、下一步测试题。
- 不把 cEDH 或多人 EDH 结论迁移到法禁。
- 若赛事规则覆盖 BO3/50 默认结构，必须标注 `event_policy_source`。

## 停止条件

- 没有对应 deck/meta 内容块：说明缺资料，并给出需要摄入的来源类型。
- 没有可用 banlist 快照：不得给最终合法性结论。
- 用户要求“确认这份牌表可参赛”但未提供完整牌表、赛事日期或 banlist/rules 版本：不得确认，只能列审计步骤。
- 规则互动不确定：转交 `mtg-judge-zh`。
