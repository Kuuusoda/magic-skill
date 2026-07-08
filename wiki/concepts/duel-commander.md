---
created: 2026-04-21
updated: 2026-07-08
type: concept
tags: [万智牌, 指挥官, EDH, Duel Commander, 1v1, 竞技]
sources: [data/oracle-cards-lite.json, "https://www.duelcommander.org/rules/duelcommander_comprehensiverules/"]
---

# Duel Commander（指挥官对决 / 法禁）

## 定义

Duel Commander（指挥官对决，简称 DC，中文社区俗称**法禁**），是指挥官赛制的一种**1v1 竞技变体**。与标准的多人指挥官不同，Duel Commander（法禁）专为两位牌手之间的竞技对局设计，具有独立的禁限牌表、特殊的生命规则和对局结构。

Duel Commander（法禁）由社区维护，而非威世智官方管理。法禁因其独立于官方 EDH 的法国禁牌表而得名。

## 核心规则差异

### 与标准指挥官（Multiplayer EDH）的对比

| 特性 | Duel Commander | 标准指挥官（Multiplayer） |
|------|---------------|--------------------------|
| 玩家人数 | 2 人 | 3-4 人（通常 4 人） |
| 起始生命 | 20 | 40 |
| 套牌大小 | 100 张（单例制） | 100 张（单例制） |
| 指挥官伤害 | **不存在** | 21 点战斗伤害致胜 |
| 禁牌表 | Duel Commander 独立禁牌表 | 官方 EDH 禁牌表 |
| 对局时长 | 通常 20-40 分钟 | 通常 60-120 分钟 |
| 社会契约 | 无（纯竞技） | 强（休闲为主） |
| 套牌强度 | 极高 | 从休闲到 cEDH 不等 |

### 起始生命 20

Duel Commander 的起始生命为 **20 点**（而非 40 点），这使得：
- 快攻策略更加可行
- 组合技的「致死回合」更快
- 每一点生命更加珍贵
- 类似传统构筑赛的生命压力

### 无指挥官伤害规则

Duel Commander **取消了 21 点指挥官伤害规则**：
- 只能通过生命归零或替代获胜条件获胜
- Voltron 策略大幅削弱
- 控制和中速策略更强

### 禁牌表

Duel Commander 拥有独立的禁牌表，与官方 EDH 禁牌表不同：

**Duel Commander 特有禁牌（部分示例）**：

| 牌名 | 类型 | 被禁原因 |
|------|------|---------|
| **Sol Ring** | 神器 | 0 费产 {2}，法术力优势过大 |
| **Mana Crypt** | 神器 | 0 费产 {2}，过强 |
| **Strip Mine** | 地 | 免费破坏关键地，过于压制 |
| **Wasteland** | 地 | 同上 |
| **Ancient Tomb** | 地 | 免费产 {2}，生命代价在 20 点生命中可接受 |
| **Demonic Tutor** | 法术 | 1 费搜索任意牌，一致性过高 |
| **Vampiric Tutor** | 瞬间 | 1 费搜索任意牌到牌库顶 |
| **Natural Order** | 法术 | 以生物为代价搜索任意绿色生物 |
| **Oko, Thief of Crowns** | 鹏洛客 | 过于全面 |
| **Teferi, Time Raveler** | 鹏洛客 | 封锁对手响应时机 |

**注意**：下表只是历史/示例性说明，不是权威禁牌表。Duel Commander 禁牌表会定期更新，实际合法性应以官方 B&R 与本 Wiki 后续 `wiki/branches/strategy/duel-commander/banlist/` 快照为准。

## 赛制结构

### 对局规则

- 对局进行直到一方牌手生命归零或满足替代获胜条件
- 官方规则默认比赛为三局两胜（Best of 3），主办方可在比赛开始前公告改用其他赛制结构
- 比赛通常为瑞士轮 + 八强/四强淘汰赛，具体轮数与淘汰赛结构以赛事公告为准

### 计时

- 官方规则默认每轮 50 分钟；主办方可在比赛开始前公告延长为 55 或 60 分钟，淘汰赛/决赛也可能使用更长或不限时
- 时间到后进入额外回合（通常为当前回合起额外 5 个回合）；具体平局/胜负处理以赛事规则与裁判公告为准

## 套牌策略

### Duel Commander 的 Meta

由于 1v1 和 20 点生命的特点，Duel Commander 的 Meta 与传统 EDH 截然不同：

| 策略类型 | 可行性 | 说明 |
|---------|--------|------|
| **快攻（Aggro）** | 高 | 20 点生命使快攻成为可能 |
| **控制（Control）** | 高 | 1v1 使控制策略更易执行 |
| **组合技（Combo）** | 中 | 需要更快、更隐蔽的组合技 |
| **中速（Midrange）** | 高 | 传统强策略 |
| **Stax** | 中 | 无多人政治的 Stax 更直接 |
| **Voltron** | 低 | 无指挥官伤害规则 |

### 代表性套牌

| 指挥官 | 颜色 | 策略类型 |
|--------|------|---------|
| **Kess, Dissident Mage** | {U}{B}{R} | 控制/组合技 |
| **Niv-Mizzet, Parun** | {U}{R} | 控制/组合技 |
| **Tatyova, Benthic Druid** | {G}{U} | 中速/法术力 |
| **Yuriko, the Tiger's Shadow** | {U}{B} | 快攻/节奏 |
| **Najeela, the Blade-Blossom** | {W}{U}{B}{R}{G} | 快攻/组合技 |
| **Dargo, the Shipwrecker + Thrasios** | {U}{R}{G} | 组合技 |

## Duel Commander 与 cEDH 的区别

| 特性 | Duel Commander | cEDH |
|------|---------------|------|
| 人数 | 1v1 | 多人（通常 4 人） |
| 生命 | 20 | 40 |
| 指挥官伤害 | 无 | 有 |
| 禁牌表 | 独立（更严格） | 官方 EDH 禁牌表 |
| 快攻可行性 | 高 | 低（40 点生命） |
| 互动密度 | 极高（1v1） | 高（多人互动更复杂） |
| 资源争夺 | 直接对抗 | 多人政治博弈 |

## 相关变体

### Leviathan

- 与 Duel Commander 类似
- 起始生命 **30** 点（介于 DC 的 20 和标准 EDH 的 40 之间）
- 使用官方 EDH 禁牌表

### European Duel Commander (EU DC)

- Duel Commander 的欧洲版本
- 规则基本相同，但禁牌表可能略有差异

## 相关页面

- [[commander|指挥官]]
- [[cedh|cEDH]]
- [[singleton|单例制]]
- [[color-identity|颜色认同]]
- [[mtg-formats|万智牌赛制]]
- [[banned-and-restricted|禁限牌表]]
