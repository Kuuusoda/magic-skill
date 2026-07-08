---
created: 2026-07-08
updated: 2026-07-08
type: decision-tree
block: dc-decision-tree
format: duel-commander
tags: [Duel Commander, 法禁, tournament-prep, decision-tree]
commander: ""
archetype: ""
sources: []
as_of: 2026-07-08
rules_as_of: 2026-07-08
cards_cited: []
---

# Duel Commander 大型赛事备战检查

本页是法禁大型赛事备战的通用决策树。它不替代具体牌表测试，也不在缺少 banlist 快照时确认合法性。

## 触发条件

- 用户问“这套能不能打比赛”“国家赛/大型赛怎么备战”“最后几张怎么改”“我该选哪套”。
- 用户给出完整或部分牌表，希望得到赛前建议。
- 用户询问已知对手、热门 meta 或某个对局计划。

## Step 1：确定版本边界

1. 如果用户给出赛事日期，记录为 `event_date`。
2. 如果用户给出赛事公告，记录 `event_policy_source`。
3. 查找 `rules_as_of <= event_date` 与 `banlist_as_of <= event_date` 的最新快照。
4. 如果没有快照，不确认合法性，只输出“需要补官方 rules/banlist 快照”。

## Step 2：牌表审计

1. 是否完整 100 张。
2. commander 是否可作为指挥官。
3. 是否存在 `banned` 或 `banned_as_commander` 风险。
4. 是否有 companion、outside-the-game、stickers、attractions、acorn、digital-only、ante、dexterity 等结构风险。
5. 是否存在明显 singleton 重名风险。

## Step 3：三回合计划

| 位置 | 必须回答的问题 |
|------|----------------|
| 先手 | T1/T2/T3 如何建立节奏或保护计划？ |
| 后手 | T1/T2/T3 如何不被对手滚雪球？ |
| 对快攻 | 哪些起手没有资格 keep？ |
| 对控制 | 哪些威胁必须保留到对手 tapped out 或互动耗尽？ |
| 对组合技 | 哪个回合必须有 interaction？ |

## Step 4：London Mulligan

- 7 张：写清“可接受但不理想”的 hand。
- 6 张：写清必须保留的功能轴。
- 5 张：只保留能执行一条明确计划的 hand。
- 任何没有前两回合动作的 hand 都需要解释为什么能 keep。

## Step 5：互动配置

| 类别 | 审计问题 |
|------|----------|
| 去除 | 能否处理主流低费指挥官与 snowball 生物？ |
| 反击 | 能否覆盖关键非生物咒语和保护窗口？ |
| 弃牌 | 是否只在先手强，后手过慢？ |
| 扫场 | 是否会拖慢自己的 clock？ |
| 坟场针对 | 是否影响自己的坟场计划？ |
| 地针对 | 是否值得在 20 血 race 中投入低 tempo 卡位？ |

## Step 6：Flex Slots

1. 列出最后 3-8 个可替换卡位。
2. 对每个卡位写“偏快 meta / 偏控 meta / 偏 combo meta / 未知 meta”的选择。
3. 没有样本时，不把 flex 结论写成最佳构筑。

## Step 7：时钟与比赛计划

- BO3/50 默认下，慢速 deck 要写何时转进攻。
- 领先时避免无意义延长对局。
- 落后时识别必须冒险的回合。
- 容易平局的对局要在赛前练习操作速度。

## 输出格式

回答大型赛事备战问题时，优先输出：

1. 缺失信息。
2. 不能确认的合法性点。
3. 最高风险的 3 个对局/构筑问题。
4. 下一轮测试的 5 个具体问题。

