# modern-breaker — 摩登环境分析 Skill

## 触发条件

当用户提出以下类型的问题时触发：
- 摩登 meta 环境查询（"摩登当前 T1 套牌有哪些？"）
- 套牌分析（"洁斯凯闪烁这套牌怎么运作？"）
- 对局优劣咨询（"红快攻打控制该怎么备牌？"）
- 环境突破口分析（"当前环境有什么弱点可以针对？"）
- 套牌选择建议（"我想入坑摩登，推荐什么套牌？"）

## 决策链

```
1. 识别查询意图
   → meta 查询 / 套牌分析 / 对局咨询 / 环境破解 / 套牌推荐

2. 收集信息
   → Read wiki/branches/strategy/ 相关文档
   → Read wiki/branches/strategy/meta-snapshots/ 最新 meta 快照
   → Read wiki/branches/strategy/decks/ 具体套牌分析
   → Read wiki/branches/strategy/decision-trees/ 决策树

3. 分析综合
   → 对比 meta 数据与套牌性能
   → 识别环境趋势和突破口
   → 给出可操作的建议

4. 输出
   → 结构化分析报告
   → 引用具体 wiki 文档来源
```

## 执行规范

### Meta 查询

查询最新 meta 快照：
```
Read ./wiki/branches/strategy/meta-snapshots/2026-05-01-modern.md
Read ./wiki/branches/strategy/formats/modern.md
```

### 套牌分析

查询具体套牌文档：
```
Read ./wiki/branches/strategy/decks/[deck-name].md
```

可用套牌文档：
- affinity.md, amulet-titan.md, azorius-control.md, boros-energy.md
- dimir-frog.md, domain-aggro.md, eldrazi-tron.md, esper-reanimator.md
- izzet-prowess.md, jeskai-blink.md, living-end.md, neoform.md
- ruby-storm.md, tameshi-belcher.md

### 对局咨询

查询决策树和备牌指南：
```
Read ./wiki/branches/strategy/decision-trees/modern-sideboard.md
Read ./wiki/branches/strategy/decision-trees/modern-anti-energy.md
Read ./wiki/branches/strategy/decision-trees/modern-meta-selection.md
```

### 环境破解

综合分析：
```
Read ./wiki/branches/strategy/meta-snapshots/*.md
Read ./wiki/branches/strategy/card-evaluations/*.md
Grep "弱点\|针对\|counter" ./wiki/branches/strategy/*.md
```

## 验收标准

### must_have
- [ ] 引用了具体的 wiki 策略文档作为来源
- [ ] 分析基于最新的 meta 快照数据
- [ ] 区分"数据驱动结论"和"主观推测"

### nice_to_have
- [ ] 引用了具体的对局数据（如 17lands 统计）
- [ ] 提供了多个备选方案
- [ ] 标注了信息的时间戳

### forbidden
- 不编造不存在的套牌或单卡
- 不声称知道未在 wiki 中记录的 meta 数据
- 不给出未经 wiki 支持的"必胜"策略

## 停止条件

- 查询的套牌在 wiki 中没有文档 → 说明缺乏该套牌的策略资料
- meta 快照过期 → 标注数据时间，建议查看最新来源
