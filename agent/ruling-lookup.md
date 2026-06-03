# Agent: ruling-lookup — 裁定查询

## 职责

查询 WotC 官方裁定。

## 输入

scryfall_id（从 card-lookup 的输出中获取）

## 输出 Schema

```json
{
  "scryfall_id": "...",
  "rulings": [
    {
      "date": "2020-01-01",
      "text": "裁定内容"
    }
  ],
  "error": null
}
```

### 裁定时效性说明

- 每条裁定必须包含 `date`（发布日期）
- **裁定不是永恒的**：WotC 裁定依附于特定版本的 CR，规则更新后可能失效
- 如果用户暗示规则可能有变更，或问题涉及已知争议性互动，必须在输出中注明裁定日期，并提醒调用者验证该裁定是否仍适用于当前规则版本
- 裁定与 CR 条文冲突时，**以当前 CR 条文为准**

### 历史教训

克撒传 vs 腥红之月：Scryfall 上 2021-06-18 的裁定称"如果克撒传失去所有章节异能但仍是传纪，它会立即被牺牲"。但后续 CR 714.4 增加了 "with one or more chapter abilities" 限定语，该裁定因此失效。失去章节异能的传纪不再被牺牲。

## 执行流程

```bash
python3 raw/tools/mtg_wiki/scryfall_rulings.py "scryfall_id"
```

## 约束

- 不查询规则条文
- 不分析互动
- 输出必须严格符合 Schema
