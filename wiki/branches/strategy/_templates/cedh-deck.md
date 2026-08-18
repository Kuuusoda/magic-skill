---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: synthesis                             # 块类型映射：deck→synthesis（见贡献规范）
block: cedh-deck
format: cedh                               # 校验键，决定 archetype 取值域
status: <seed|stub|draft|verified|deprecated>
tags: [cEDH, 套牌, <原型>]
commander: "<主将中文（English）> // <副将/背景中文（English）>"  # 单将则右侧留空
pair_type: <single|partner|partner-with|friends-forever|background>
archetype: <Turbo|Stax|Midrange|Adaptive>  # cedh 域枚举
sources: [<赛事报告或 primer 链接/文件>]
as_of: YYYY-MM-DD                          # 数据时效（P3），粒度到日
cards_cited:                               # 核心 combo 件 + 关键牌（允许代表性子集，非全 100 张）；CI 逐张离线查证
  - "<牌名中文（English）>"
---

# <套牌中文名>（<English>）

> 一句话定位：<这套牌靠什么赢、在什么环境位>

## 原型定位
- 原型：<Turbo / Stax / Midrange / Adaptive>，理由：……
- 速度档位：<典型制胜回合 T?>
- 颜色认同：<WUBRG 子集>

## 核心 combo 线
| 制胜路线 | 组件 | 启动费用 | 备注 |
|---------|------|---------|------|
| 主线 | <[[combos/<combo>]]> | … | … |
| 备线 | … | … | … |

（combo 细节引用 `[[branches/strategy/cedh/combos/<combo>]]`，不在此重复编造牌张异能）

## 关键对局
- vs <对手原型>：<优劣 + 关键交互点>
- vs <对手原型>：……

## 起手保留（Mulligan）
- 必留：……
- 可留：……
- 弃掉：……

## 弱点与针对
- <已知弱点>：<对手如何针对 / 本套牌如何应对>

---
*牌名首次出现用「中文（English）」，经 `card_search.py` 查证；规则裁定让渡 mtg-judge-zh。*
