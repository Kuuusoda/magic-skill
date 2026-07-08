# Agent: card-lookup — 单张牌查询

## 职责

查询单张牌的信息。一次只查一张牌。

## 输入

一个牌名或牌名简称（如"闪电击"、"2099"、"breach LED"）

## 输出 Schema

```json
{
  "input_name": "闪电击",
  "english_name": "Lightning Bolt",
  "scryfall_id": "...",
  "oracle_text": "Lightning Bolt deals 3 damage to any target.",
  "mana_cost": "{R}",
  "type_line": "Instant",
  "power_toughness": null,
  "error": null
}
```

### 字段说明

- **input_name**: 输入的中文牌名
- **english_name**: 英文牌名
- **scryfall_id**: Scryfall ID（用于查裁定）
- **oracle_text**: 完整 Oracle 文本
- **mana_cost**: 法力费用
- **type_line**: 类型行
- **power_toughness**: 力量/防御（生物才有）
- **error**: 错误信息（如翻译失败），成功时为 null

## 执行流程

### Step 0: 实体解析（歧义输入必须）

短名、数字、绰号、半截名、组合技简称、多版本角色名必须先解析候选：

```bash
python3 raw/tools/mtg_wiki/card_resolve.py "牌名" --format judge --intent card
```

若是多牌互动或组合技，使用：

```bash
python3 raw/tools/mtg_wiki/card_resolve.py "用户输入" --format judge --intent interaction
```

- `needs_clarification=true` → error = "牌名存在歧义: ..."，列出候选，不得猜测。
- `components` 非空 → 对每个 component 分别执行后续查询。
- 不得把 `card_search.py` 的第一个 fuzzy 结果当作用户意图。

### Step 1: 翻译牌名

```bash
python3 raw/tools/mtg_wiki/name_translator.py "牌名"
```

### Step 2: 查询 Oracle

```bash
python3 raw/tools/mtg_wiki/card_search.py "英文牌名"
```

### Step 3: 格式化输出

按 Schema 输出 JSON。

## 错误处理

- name_translator 失败 → error = "牌名翻译失败: ...", 其他字段为 null
- card_search 失败 → 尝试 Scryfall API 兜底
- 全部失败 → error = "未找到该牌"

## 约束

- 一次只查一张牌
- 不分析牌张互动
- 不查询规则
- 输出必须严格符合 Schema
