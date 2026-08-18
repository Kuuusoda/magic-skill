---
created: 2026-07-08
updated: 2026-07-09
type: source
tags: [Duel Commander, 法禁, rules, source-registry]
sources: ["https://www.duelcommander.org/rules/duelcommander_comprehensiverules/"]
---

# Duel Commander 来源注册表

本页记录法禁规则与禁牌表抓取入口。脚本应读取本页或由本页生成的结构化注册表，避免把域名和路径散落到业务逻辑中。

## Canonical Sources

| 用途 | URL | 备注 |
|------|-----|------|
| 官方综合规则 | https://www.duelcommander.org/rules/duelcommander_comprehensiverules/ | 规则快照来源 |
| 官方禁牌表 | https://www.duelcommander.com/banned-restricted/ | 官方 Banned / Restricted 页面；首份本地快照见 [[duel-commander/banlist/2026-01-26-official]] |

## 来源优先级

1. Wizards of the Coast 官方 MTG 文档。
2. Duel Commander 官方综合规则快照。
3. Duel Commander 官方禁牌表快照。
4. 对应日期的 CR/MTR/IPG 本地快照。
5. Duel Commander FAQ/官方公告。
6. 第三方 meta 文章、社群战报、玩家经验。

## 快照选择

- 用户给出日期或内容块有 `as_of` 时，选择 `effective_date <= as_of` 的最新规则与禁牌表快照。
- 用户问“现在”时，使用本地最新快照；若快照过期，回答必须标注可能过期。
- 比赛开始后，按比赛开始时生效的规则与禁牌表判断。
