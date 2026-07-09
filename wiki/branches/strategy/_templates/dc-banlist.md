---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: synthesis
block: dc-banlist
format: duel-commander
status: <seed|stub|draft|verified|deprecated>
tags: [Duel Commander, 法禁, banlist]
banlist_as_of: YYYY-MM-DD
rules_as_of: YYYY-MM-DD
sources: ["<official banlist URL from source-registry>"]
banned: []
banned_as_commander: []
banned_as_companion: []
generated_by: manual
source_hash: ""
---

# Duel Commander 禁牌表（<banlist_as_of>）

本页是法禁模块的禁牌表快照。机器校验读取 frontmatter 中的 `banned` 与 `banned_as_commander`，正文只做人类说明。

## 来源

- 官方来源：<URL>
- 抓取/维护方式：<manual / fetch_dc_banlist.py>

## 说明

- `banned`：全面禁用，不能作为指挥官，也不能进入 99。
- `banned_as_commander`：仅禁作指挥官，仍可能作为 99 使用。
- `banned_as_companion`：仅禁作行侣，仍需按官方列表判断是否可进主牌或指挥官位。
