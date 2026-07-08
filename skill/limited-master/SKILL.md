---
name: limited-master
description: 万智牌限制赛（Limited）学习、单卡评分、系列评测与实战教练。用于解释限制赛、现开、轮抽规则，指导40张限制赛套牌构组，分析轮抽抓位、信号、调度、17Lands数据、现开牌池、对局计划、换备，撰写LSV/ChannelFireball风格的限制赛单卡点评，以及“谁是进攻者/防守方”的攻守角色判断。触发词包括限制赛、现开、轮抽、Draft、Sealed、单卡评分、set review、LSV评分、CFB评分、调度、看信号、组牌、曲线、去除、生物数量、17Lands、P1P1、攻守角色。具体牌张文本、官方译名和规则判定应结合 mtg-wiki 或 mtg-judge-zh，不凭记忆编造单卡信息。
---

# 限制赛大师

用这个 skill 把限制赛问题转成可执行的判断：这是什么赛制、这套牌怎么组、这一抓怎么选、这手牌该不该留、这一局谁该进攻、如何查 17Lands 数据、赛后如何复盘。

## 先读资料

处理限制赛学习、组牌或复盘任务时，优先读取这些 wiki 页面：

- `wiki/synthesis/limited-learning-path.md`：总学习路径与核心框架。
- `wiki/sources/2026-06-22-topdeck-limited-reading-list.md`：本 skill 的来源索引和抓取状态。
- `wiki/concepts/limited.md`、`wiki/concepts/sealed.md`、`wiki/concepts/draft.md`：赛制基础。
- `wiki/concepts/mana-curve.md`、`wiki/concepts/removal.md`、`wiki/concepts/mulligan.md`、`wiki/concepts/mana-base-strategy.md`：组牌与对局基础。

需要完整操作框架、启发式清单、17Lands 查询方式、单卡评分写法或教学回答时，再读取 `references/limited-playbook.md`。需要直接获取 17Lands 单卡数据时，运行 `scripts/fetch_17lands_card_ratings.py`。需要把自己的评分和 LSV/CFB/17Lands 等外部参照对比时，运行 `scripts/calibrate_limited_ratings.py`。

## 回答原则

- 先判断任务类型：解释概念、现开组牌、轮抽选牌、对局计划、调度、17Lands 数据、赛后复盘。
- 输出可操作结论，不只给原则。用户给牌池或抓位时，给候选方案、取舍理由、风险和下一步。
- 默认限制赛套牌为 40 张，常见基线是 17 地 + 23 非地；生物数量、去除数量和曲线根据套牌角色调整。
- 把“强牌”放回套牌计划里判断：同一张牌在快攻、中速、控制、协同套牌中的价值可能不同。
- 写限制赛单卡评分时，先给 0-5 分数，再写 baseline、ceiling、deck condition 和 pick/build implication；遇到强烈依赖环境或构筑条件的牌，用范围分或分裂评分。
- 评分后必须校准：按高估/低估模式复盘，而不是只看平均误差。优先修正 P1P1、4.0+ 强牌、0-1.5 陷阱牌和 2.5-3.0 中间桶。
- 处理具体牌名、官方中文译名、Oracle 文本、规则互动或比赛规则判定时，调用/结合 `mtg-wiki` 或 `mtg-judge-zh` 的资料；不要凭记忆断言单卡细节。
- 明确资料边界：本 skill 基于已摄入的 TopDeck 限制赛学习资料；`04 TDM 现开指南`和`08 团队现开示例`当前不作为核心来源。

## 常用工作流

### 解释限制赛

说明限制赛是“用现场获得的随机牌池构筑套牌”的赛制，核心形式是现开和轮抽。强调限制赛同时考察单卡评价、曲线、法术力基础、对局计划、调度、战斗和动态角色判断。

### 构筑现开/轮抽套牌

1. 先找牌池的 superpower：炸弹、去除、修色、协同、颜色深度或曲线。
2. 选主色骨架：优先能稳定施放、曲线完整、能支撑套牌计划的颜色，而不是单纯稀有最多的颜色。
3. 决定角色：快攻、地面防守天上进攻、中速、控制、协同组合。
4. 填 23 张非地：检查生物密度、去除数量、曲线、抓牌/法术力水槽、战斗 tricks 和非生物比例。
5. 配地：主色通常需要 8-9 个来源；溅色依据费用、强度、出牌回合和修色数量决定。
6. 做 sanity check：起手能否执行前三回合计划，是否有过多高费/双费/条件牌，去除是否能处理真正会输的威胁。
7. 记录换备：对快攻补低费阻挡/便宜互动；对慢牌提高威胁质量、抓牌和不可被单去除解决的计划。

### 分析轮抽

- P1P1 先看炸弹、无条件去除和高质量单卡，再看颜色分布和协同上限。
- 前几抓保持开放，强通用牌和单色牌优先于窄协同；可以放弃第一抓炸弹。
- 2-4 抓信号弱，5 抓以后还看见 premium 牌才是强信号；连续缺席比单包缺席更重要。
- 注意自己传出的信号：如果连续放过一个颜色的强牌，避免后面又切进同色。
- 第二包开始拼套牌结构，不只是拿最高分牌；第三包补洞、修曲线、拿修色和备牌。
- Hate draft 优先级很低，只有没有可用牌、修色或备牌时才考虑。

### 撰写单卡评分

先确认牌面文本、费用、颜色、稀有度和系列机制，再按 0-5 限制赛评分输出。点评要短但有判断：这张牌的普通表现是什么、在哪类套牌或局面会变强、失败情形是什么、抓牌/组牌时应该怎么处理。具体评分口径、范围分和点评模板见 `references/limited-playbook.md` 的“单卡评分与点评写法”。

### 校准评分表

将自己的评分 JSON/CSV 与外部评分表对齐时，运行：

```bash
python3 skill/limited-master/scripts/calibrate_limited_ratings.py \
  --ours output/my_ratings.json \
  --reference output/reference_ratings.json \
  --output output/rating_calibration.md
```

看 `delta >= 1.0` 和 `delta <= -1.0` 的牌，按牌型、稀有度、颜色和角色总结误评原因，再更新评分规则或重评中间桶。

### 判断调度

- 在限制赛里找“留下的理由”：功能手牌优先于完美手牌。
- 看前 3 回合计划、颜色来源、关键费用、生物/互动比例，以及未来 1-2 抽能否自然修正问题。
- 先手更重视保留资源，后手可接受部分颜色风险但更怕太慢。
- 快攻没有早期威胁要更严格；强套牌可以更愿意调掉边缘手。
- 调到 6 后不要机械放回最高费牌；保留能执行计划和改变局面的牌，放回冗余或低影响牌。

### 制定对局计划

- 每局都问：谁有长局优势？谁的 clock 更快？谁从交换中获益？谁需要打破僵局？
- 进攻方通常要珍惜伤害、逼迫阻挡、用去除清路；防守方要保护血量、交换资源、把游戏拖到炸弹或牌差阶段。
- 不要为了“曲线顺”乱交去除。优先处理穿透威胁、难交换的大生物、能滚雪球的引擎、或能被你一换二惩罚的光环/trick。
- 炸弹不一定按费拍下；若对手有开放费用或关键互动，考虑先用次级威胁诱出解牌。

### 使用 17Lands

- 网页查询入口：`https://www.17lands.com/card_data` 查单卡数据，`https://www.17lands.com/deck_color_data` 查色组数据，`https://www.17lands.com/trophy_decks` 查奖杯套牌，`https://www.17lands.com/public_datasets` 查公开数据集。
- 脚本查询入口：运行 `python3 skill/limited-master/scripts/fetch_17lands_card_ratings.py --expansion TDM --format PremierDraft --sort gih --top 20`。常用参数有 `--rarity common uncommon`、`--color W`、`--name "card name"`、`--min-games 200`、`--output output.md`。
- 数据端点：脚本使用 `https://www.17lands.com/card_ratings/data?expansion=<SET>&format=<FORMAT>`。如果端点变动，先让用户用网页入口确认系列和赛制。
- 用数据校准直觉，不把数据当自动 pick order。
- GIH WR 是最常用的强度指标；OH WR 更适合评估早期牌/快攻牌；ALSA 帮助判断牌被拿走的平均时机；IWD 偏差大，不要替代 GIH WR。
- 结合色组、样本量、用户水平、牌的角色和套牌结构阅读数据。
- 优先使用 draft/game replay 做复盘：找出自己和高水平牌手在抓位、攻击、阻挡、去除时机上的分歧。
