# Agent: card-lookup — 单张牌查询

## 职责

查询单张牌的信息。一次只查一张牌。

## 输入

一个中文牌名（如"闪电击"）

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
