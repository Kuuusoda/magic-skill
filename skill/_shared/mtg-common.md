# MTG Common Skill Contract

本文件是 MTG skills 的 L2 公共能力层。它通过 `opencode.json` 的 `instructions` 注入运行时上下文，定义所有 MTG skill 必须共享的工具与查证契约。

## 工具路径

所有路径以项目根目录为基准：

- `./raw/tools/mtg_wiki/card_resolve.py`：实体解析；处理短名、数字、俗称、半截名、套牌简称、组合技简称、多版本角色名。
- `./raw/tools/mtg_wiki/card_search.py`：确定牌名后的单卡详情查询；不是实体解析器。
- `./raw/tools/mtg_wiki/name_translator.py`：中英文牌名翻译。
- `./raw/tools/mtg_wiki/rule_search.py`：CR/MTR/IPG 规则检索。
- `./raw/tools/mtg_wiki/scryfall_rulings.py`：Scryfall/WotC 裁定查询。
- `./raw/tools/mtg_wiki/validation.py`：judge pipeline JSON 校验。

## 实体解析

遇到以下输入时，必须先调用 `card_resolve.py`：

- 短名、数字、绰号、半截英文名。
- 套牌简称、组合技简称、archetype 俗称。
- 多版本角色名或可能同时指牌、套牌、组合技的词。

示例：

```bash
python3 ./raw/tools/mtg_wiki/card_resolve.py "2099" --format duel-commander --intent commander
python3 ./raw/tools/mtg_wiki/card_resolve.py "blue farm" --format cedh --intent deck
python3 ./raw/tools/mtg_wiki/card_resolve.py "breach LED" --format judge --intent interaction
python3 ./raw/tools/mtg_wiki/card_resolve.py "frog" --format modern --intent deck
```

规则：

- `needs_clarification=true` 时先追问，不得继续生成规则或策略结论。
- 自动选择候选时，回答必须说明“我将 X 解析为 Y”。
- 不得把 `card_search.py` 或 API fuzzy 的第一结果当作用户意图。
- 解析出 card 后，再用 `card_search.py` 查 Oracle 详情。
- 解析出 deck / archetype / combo 后，优先读取对应 wiki 内容块。

## 数据能力边界

本仓库的 Wiki 中有历史构建时的 37k Oracle 数据统计；运行时本地索引是可选加速，不应默认声称已内置。

- 若 `raw/tools/mtg_wiki/data/card_name_index.json` 存在，可使用本地精确/前缀/模糊查询。
- 若本地索引缺失，`card_search.py` 会退化为 mtgch/Scryfall API 查询。
- 回答时不得把“构建期数据来源”说成“当前运行时离线数据库已可用”。

## 规则与策略让渡

- 精确规则裁定、CR/MTR/IPG 适用：优先 `mtg-judge-zh`。
- 赛制竞技策略：优先对应 `<format>-breaker`。
- 通用百科、背景、翻译、轻量查询：`mtg-wiki` 可回答。
- 策略 skill 遇到复杂规则互动，不自行裁定；转交或建议使用 `mtg-judge-zh`。

## 输出规范

- 牌名首次出现使用 `中文（English）`；后续可用中文简称。
- 规则回答引用具体规则号或原文文件。
- 策略/meta/Tier/占比必须带 `as_of` 与来源；无来源时标为观察假设。
- 法禁内容必须标注 `as_of`、`banlist_as_of`、`rules_as_of`；没有快照时不得确认合法性。
