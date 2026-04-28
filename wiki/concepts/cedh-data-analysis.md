---
created: 2026-04-22
updated: 2026-04-22
type: concept
tags: [万智牌, 指挥官, cEDH, 数据分析, 方法论]
sources: []
---

# cEDH 数据分析方法

cEDH 数据分析是一套**数据驱动**的套牌评估框架，通过定量数据（胜率、Meta 占比、单卡表现）和定性分析（Primer 策略、环境趋势）相结合，生成标准化的套牌评估报告。

---

## 一、数据输入三层架构

cEDH 分析依赖三层数据来源，从宏观到微观：

### 第一层：赛事数据（Topdeck.gg）

**来源**：https://topdeck.gg（cEDH 赛事平台）

**提供的数据**：
- **Standings**：赛事排名、选手信息、牌表链接
- **Win Rate**：整体胜率、Swiss 阶段胜率、Bracket 阶段胜率
- **Opponent Win Rate**：对手平均胜率（用于评估赛程强度）
- **Round-by-round Results**：逐轮对局结果（用于 Matchup 分析）
- **Decklists**：套牌列表（用于 Staples 频率统计）

**关键指标**：

| 指标 | 含义 | 优秀标准 |
|------|------|---------|
| **Win Rate** | 总胜率 | > 50% |
| **Conversion Rate** | Top 4 转化率（进入淘汰赛的概率）| > 20% |
| **Opponent Win Rate** | 对手平均胜率 | 接近 50% 说明赛程均衡 |
| **Swiss Win Rate** | 瑞士轮胜率 | 反映稳定性 |
| **Bracket Win Rate** | 淘汰赛胜率 | 反映高压下的表现 |

**数据获取方式**：
```bash
# 通过 Topdeck API 自动获取
python utils/topdeck_client.py --commander "Kinnan, Bonder Prodigy"
```

### 第二层：统计聚合（edhtop16）

**来源**：https://edhtop16.com（cEDH 统计数据库）

**提供的数据**：
- **Entries**：使用该指挥官的参赛次数
- **Meta%**：该指挥官在环境中的占比
- **Conversion Rate**：Top 4 转化率
- **Win Rate**：整体胜率
- **Staples List**：按类型分类的高频单卡（Creature/Instant/Sorcery/Artifact/Enchantment）
- **Tournament History**：近期比赛记录（Top 16/Top 4/冠军）

**关键指标**：

| 指标 | 含义 | 优秀标准 |
|------|------|---------|
| **Meta%** | 环境占比 | 5–10% 为热门，>10% 为超热门 |
| **Conversion Rate** | Top 4 转化率 | > 20% 为强势 |
| **Win Rate** | 整体胜率 | > 45% 为竞技可用 |

**数据获取方式**：edhtop16 不提供 API，需要手动从网页提取或抓取。

### 第三层：策略文档（Moxfield Bracket 5 Primers）

**来源**：https://moxfield.com（牌表平台，Primer 为策略文档）

**提供的数据**：
- **策略概述**：套牌定位、核心思路、速度评级
- **起手保留（Mulligan）**：不同手牌的保留/重调度策略
- **Combo 执行**：具体步骤、替代方案、常见错误
- **对局指南**：vs 各主流套牌的策略
- **近期变动**：最新版本的单卡调整

**质量标准**：只使用 **Bracket 5** 级别的 Primer（社区公认的高质量策略文档）。

---

## 二、定量分析方法

### 1. 胜率分析

对比该套牌与环境中 S/A/B Tier 套牌的胜率差异，判断定位：

| 胜率区间 | 定位 | 说明 |
|---------|------|------|
| > 50% | 环境强势 | 超过半数对局获胜 |
| 45–50% | 均衡 | 竞技可用，但无绝对优势 |
| 40–45% | 边缘 | 特定环境下可用 |
| < 40% | 弱势 | 需要显著优化或环境变化 |

**单卡胜率分析**（基于 edhtop16 Staples 数据）：

| 单卡 | 携带胜率 | 未携带胜率 | 差值 | 影响评级 |
|------|---------|-----------|------|---------|
| Demonic Tutor | 62% | 42% | +20% | 极高 |
| Mana Crypt | 58% | 45% | +13% | 高 |
| Force of Will | 55% | 48% | +7% | 中 |

### 2. 效率分析

| 指标 | 含义 | cEDH 标准 |
|------|------|----------|
| **平均制胜回合** | 完成 Combo 的平均回合 | T3–T4 为标准，T1–T2 为极速 |
| **导师上手率** | 关键导师（Demonic Tutor 等）在前 X 回合上手的概率 | > 80% 为优秀 |
| **快速 Mana 上手率** | T1 可用的 Mana 加速数量 | 1.5–2.0 为优秀 |

### 3. 互动与重建分析

| 指标 | 含义 | 优秀标准 |
|------|------|---------|
| **互动密度** | 互动单卡数量 / 套牌总数 | 15–25% |
| **互动有效使用率** | 互动单卡实际成功干扰对手的比率 | > 70% |
| **重建成功率** | Combo 被干扰后，在 3 回合内重新建立制胜条件的能力 | > 70% |

### 4. 冗余分析

| 指标 | 含义 | 优秀标准 |
|------|------|---------|
| **Combo 路线数** | 独立的制胜路线数量 | ≥ 2 |
| **导师密度** | 导师数量 / 套牌总数 | 10–15% |
| **关键单卡冗余** | 核心组件是否有替代方案 | 每个组件有 ≥ 1 个替代 |

---

## 三、定性分析方法

### 1. 环境适配性分析

结合当前环境主流战术，判断套牌的战术契合度：

| 环境特征 | 适配套牌类型 | 不适配套牌类型 |
|---------|------------|--------------|
| 快攻 Combo 为主 | 高互动 Midrange / Adaptive | 慢速 Stax |
| 互动密度高 | 韧性强的 Adaptive | 单一路线的 Turbo |
| Stax 密度高 | 高去除 Midrange | 依赖特定引擎的 Turbo |

### 2. 操作难度分析

| 难度等级 | 特征 | 代表套牌 |
|---------|------|---------|
| **低** | 单一路线，决策点少 | 某些 Turbo |
| **中** | 多条路线，需要 Mana 计算 | Blue Farm |
| **高** | 多层 Combo，Stack 互动复杂 | Kinnan（等时权杖 + Mana 流量计算）|
| **极高** | 需要实时评估对手手牌和 Mana | 复杂 Adaptive |

### 3. 成本适配性分析

cEDH 套牌的构筑成本通常在 **$5,000–$20,000 USD** 之间，主要成本来源：

| 类别 | 典型单卡 | 成本占比 |
|------|---------|---------|
| ** Reserved List 地牌** | Underground Sea、Volcanic Island | 30–50% |
| **快速 Mana** | Mana Crypt、Mox Diamond | 15–25% |
| **导师** | Imperial Seal、Vampiric Tutor | 10–15% |
| **互动** | Force of Will、Force of Negation | 5–10% |

---

## 四、报告标准结构（6 章）

cEDH 分析报告的标准结构，确保覆盖所有关键维度：

### 第 1 章：套牌基础信息
- 指挥官异能简述
- 核心 Combo（主路线 + 备用路线）
- 关键单卡分类（快速 Mana / 导师 / 互动 / 过牌）
- 构筑逻辑（颜色优势、Combo 冗余、Tutors 密度、互动密度）

### 第 2 章：环境适配性表现
- 当前 cEDH 环境层级（S/A/B Tier 分布）
- Matchup 分析（vs 各主流套牌的优劣势）
- 环境痛点应对（先手优势 / Combo 速度 / 互动密度 / Stax 压制）

### 第 3 章：实战表现细节（核心）
- 胜率数据（整体 / Swiss / Bracket / vs 各类型 / Pod 位置）
- 关键节点表现（制胜回合 / Combo 成功率 / 重建成功率 / 导师上手率）
- 常见问题（失误类 / 构筑漏洞 / 对局策略误区）

### 第 4 章：套牌未来表现预判
- 环境趋势预判
- 禁限牌调整影响
- 新卡发布的强化/削弱
- 玩家习惯变化的影响

### 第 5 章：结论与优化建议
- 核心表现结论（强烈推荐 / 推荐 / 需优化 / 不推荐）
- 构筑优化（具体单卡调整建议）
- 对局策略优化（不同 Matchup / 先手后手 / Pod 位置）

### 第 6 章：附录
- 数据表格
- 参考资料（数据来源、Primer 链接）
- 术语注释

---

## 五、质量检查清单

生成报告前必须完成以下检查：

- [ ] 赛事数据已获取（Topdeck.gg 或手动补充）
- [ ] 所有牌名已通过官方中文翻译验证（双语格式）
- [ ] 生成分类翻译对照表（主将 / Mana / 导师 / 互动 / 过牌 / 地牌）
- [ ] 第 3 章"实战表现细节"完整详实
- [ ] 胜率数据有来源标注
- [ ] Matchup 分析覆盖主流套牌
- [ ] 未来预判有逻辑依据
- [ ] 优化建议可落地执行

---

## 六、数据获取工具链

| 工具 | 功能 | 路径 |
|------|------|------|
| **topdeck_client.py** | Topdeck.gg API 赛事数据获取 | `utils/topdeck_client.py` |
| **topdeck_processor.py** | 赛事数据标准化处理 | `utils/topdeck_processor.py` |
| **mtgch_card_translator.py** | 牌名中英翻译 | `utils/mtgch_card_translator.py` |
| **cedh_excel_generator.py** | 单卡胜率 Excel 表格生成 | `utils/cedh_excel_generator.py` |

---

## 相关页面

- [[cedh|cEDH 概述]] — cEDH 核心竞技维度
- [[cedh-deck-archetypes|cEDH 套牌原型]] — Turbo / Stax / Midrange / Adaptive
- [[cedh-combo-patterns|cEDH 组合技模式]] — 常见制胜路线
- [[combo|组合技]] — 组合技通用理论
- [[combo-engine-cards|组合技引擎牌]] — cEDH 高频引擎牌
- [[tutor|检索]] — 导师体系详解
- [[card-advantage|卡牌优势]] — 资源获取理论
- [[commander|指挥官]] — 指挥官赛制通用规则
