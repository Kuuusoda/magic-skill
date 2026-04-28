---
created: 2026-04-20
updated: 2026-04-22
type: concept
tags: [万智牌, 赛制, 指挥官, 竞技, 多人, cEDH]
sources: [data/oracle-cards-lite.json]
---

# cEDH（Competitive EDH）

cEDH（Competitive Elder Dragon Highlander，竞技指挥官）是万智牌[[commander|指挥官]]赛制中以**竞技胜利为唯一目标**的分支。它在 4 人 Pod 中进行，遵循与休闲 EDH 相同的构组规则（100 张 singleton、颜色认同、统帅区），但套牌设计、对局决策和元游戏理解均围绕最大化获胜概率展开。

---

## 与 Casual EDH 的核心区别

| 维度 | cEDH | Casual EDH |
|------|------|-----------|
| **对局目标** | 最大化获胜概率 | 社交娱乐、主题体验、避免「太早结束游戏」|
| **平均制胜回合** | T2–T6 | T10+ |
| **地牌数量** | 28–32 张（低曲线、快速法术力） | 35–40 张 |
| **互动密度** | 15–25%（大量免费反击和去除） | <10% |
| **组合技密度** | 2+ 条独立制胜路线 + 单卡制胜 | 低或中等 |
| **平均预算** | $5,000–$20,000（老圈地、P9、FOW 等） | 灵活 |
| **社交契约** | 弱或无 | 强（限制强度、避免早期 Combo）|

---

## cEDH 核心竞技维度

cEDH 的竞技深度体现在五个相互关联的维度上，每个维度都有独立的策略体系和决策框架：

### 1. 套牌原型（Deck Archetypes）

cEDH 套牌按核心战术分为四大原型：[[cedh-deck-archetypes|Turbo、Stax、Midrange、Adaptive]]。理解各原型的特征是分析 Matchup 优劣势和环境适配性的基础。

- **Turbo**：T1–T3 极速 Combo，组件少、费用低、怕互动
- **Stax**：通过 Tax / Lock / Denial 拖慢对手，T5–T8 逐步获胜
- **Midrange**：T4–T6 通过卡牌优势引擎建立资源领先，然后 Combo
- **Adaptive**：根据起手和对局灵活切换 Turbo / Midrange 模式，最难针对

### 2. 组合技模式（Combo Patterns）

cEDH 的 Combo 设计遵循「速度、冗余、隐蔽性」三大原则。常见制胜路线包括：[[cedh-combo-patterns|Breach Combo、Oracle Combo、Ad Nauseam、等时权杖组合技]]等。

- 优秀套牌至少有 **2 条独立 Combo 路线** + **1 张单卡制胜**
- Combo 费用应形成梯度（1–2 费 → 2–3 费 → 3–5 费 → 5+ 费），覆盖不同 Mana 条件

### 3. Pod 动态与位置策略（Pod Dynamics）

cEDH 在 4 人 Pod 中进行，回合顺序带来独特的博弈空间：[[cedh-pod-dynamics|位置效应、政治博弈、原型在不同位置的表现]]。

- **1 号位**（先手）：最快展开，但需防守 3 个方向，典型胜率 ~45%
- **2–3 号位**（中位）：观察后决策，典型胜率 ~40–43%
- **4 号位**（后手）：信息最多但展开最慢，典型胜率 ~38%

政治博弈的核心原则：**「我不干扰你，因为有人更值得干扰」**。

### 4. 数据分析方法（Data Analysis）

cEDH 分析依赖三层数据来源：[[cedh-data-analysis|赛事数据（Topdeck.gg）、统计聚合（edhtop16）、策略文档（Moxfield Bracket 5 Primers）]]。

- **定量**：胜率、Conversion Rate、平均制胜回合、互动密度、冗余度
- **定性**：环境适配性、操作难度、成本适配性
- **报告结构**：6 章标准框架（基础信息 → 环境适配 → 实战表现 → 未来预判 → 结论优化 → 附录）

### 5. 互动与资源管理

互动是 cEDH 中最稀缺的资源之一。关键原则：

- **必须互动**：对手将在当前回合完成 Combo；对手施放了「游戏结束」级威胁（如 Ad Nauseam）
- **不应该互动**：对手只是「展开」尚未进入 Combo 窗口；干扰后让第三方获益；你有更好的机会下回合完成自己的 Combo
- **多层互动**：1 号位用免费反击，2 号位保留去除（防止保护手段）

---

## 环境元游戏（Metagame）

### 2024 年 9 月禁牌调整的影响

禁牌：Mana Crypt、Jeweled Lotus、Dockside Extortionist

- **Turbo 变慢**：少了 3 张 T1 快速 Mana，平均制胜回合延后 0.5–1 回合
- **Midrange 受益**：环境整体变慢，卡牌优势引擎价值提升
- **Stax 微调**：Dockside 被禁减少了一个 Stax 目标

### 环境特征与原型选择

| 环境特征 | 推荐原型 | 理由 |
|---------|---------|------|
| 互动密度低 | Turbo | 对手难以干扰你的 Combo |
| Stax 密度高 | Midrange / Adaptive | 需要去除和韧性 |
| Turbo 密度高 | Stax / Adaptive | 需要限制效应或互动 |
| 环境未知 | Adaptive | 最稳健的默认选择 |

---

## 常见误区

1. **「我是 4 号位，所以我最弱」** → 4 号位信息最强，精准互动可逆转局势
2. **「我应该在每回合都互动」** → 互动是有限资源，过早消耗等于给对手开绿灯
3. **「Stax 套牌不需要互动」** → Stax 也需要互动保护自己的 Stax 组件
4. **「我应该针对上一把赢我的人」** → 每局独立，基于当前 Pod 组成和位置做决策

---

## 相关页面

- [[cedh-deck-archetypes|cEDH 套牌原型]] — Turbo / Stax / Midrange / Adaptive 详解
- [[cedh-combo-patterns|cEDH 组合技模式]] — Breach / Oracle / Ad Nauseam 等制胜路线
- [[cedh-pod-dynamics|cEDH Pod 动态]] — 4 人位置策略与政治博弈
- [[cedh-data-analysis|cEDH 数据分析方法]] — 数据驱动的套牌评估框架
- [[commander|指挥官]] — 指挥官赛制通用规则
- [[color-identity|颜色认同]] — 套牌构组的颜色限制
- [[command-zone|统帅区]] — 指挥官的起始区域
- [[combo|组合技]] — 组合技通用理论
- [[combo-engine-cards|组合技引擎牌]] — EDH 高频引擎牌
- [[counterspell|反击咒语]] — 堆叠互动体系
- [[edh-banned-list|EDH 禁牌表]] — 指挥官规则委员会禁牌列表
