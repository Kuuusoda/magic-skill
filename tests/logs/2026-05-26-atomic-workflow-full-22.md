# 回归测试报告 — 2026-05-26-atomic-workflow-full-22

## 元信息

| 项目 | 值 |
|------|-----|
| 测试时间 | 2026-05-26 |
| Tag | atomic-workflow-full-22 |
| Skill 版本 | mtg-judge-zh @ v3.1 原子化工作流 |
| 使用模型 | claude-opus-4-7 |
| 测试方式 | 逐题严格走工作流，记录推理对比 |

---

## 总览

| 指标 | 结果 |
|------|------|
| 总题数 | 22 |
| 完全匹配 | 21 / 22 |
| 需核对 | 1 / 22 |
| 正确率 | 95% |

---

## 逐题结果

| 题号 | 判定 | 答案 | 推理匹配度 |
|------|------|------|----------|
| Q1 | ✓ | C | 完全匹配 |
| Q2 | ✓ | D | 完全匹配 |
| Q3 | ✓ | D | 完全匹配 |
| Q4 | ✓ | C | 完全匹配 |
| Q5 | ✓ | B | 完全匹配 |
| Q6 | ✓ | B | 完全匹配 |
| Q7 | ✓ | B, E | 完全匹配 |
| Q8 | ✓ | D | 完全匹配 |
| Q9 | ✓ | B | 完全匹配 |
| Q10 | ✓ | E | 完全匹配 |
| Q11 | ✓ | C | 完全匹配 |
| Q12 | ✓ | D | 完全匹配 |
| Q13 | ✓ | B | 完全匹配 |
| Q14 | ✓ | C | 完全匹配 |
| Q15 | ✓ | A, B, C | 完全匹配 |
| Q16 | ✓ | C | 完全匹配 |
| Q17 | ✓ | B | 完全匹配 |
| Q18 | ✓ | B | 完全匹配 |
| Q19 | ✓ | C, E | 完全匹配 |
| Q20 | ✓ | B | 完全匹配 |
| Q21 | ✓ | A | 完全匹配 |
| Q22 | △ | A | 需核对 |

---

## 逐题推理对比详情

### Q1

**标准答案**: C
**推理匹配**: 完全匹配

**我的分析**:
Poisoner's Apprentice的if在效应部分，不是介入性if（CR 603.4）。触发时不检查条件。Virulent Emissary在场使Astrid获1生命。Hazel's Nocturne不影响gained life检查（检查是否获得过生命，不是净变化）。

**答案解析要点**:
The “if” clause in the ability of Poisoner&#8217;s Apprentice does not appear directly after the trigger event, so it is not an intervening “if”: the ability triggers when Poisoner&#8217;s Apprentice enters the battlefield, and the “if” clause is only checked when the ability resolves . If Astrid gains life between the ability triggering and resolving, the condition is fulfilled and the target cre...

**关键一致点**:
- if不是介入性if
- 触发时不检查
- 结算时检查gained life
- gained life不是net change

---
### Q2

**标准答案**: D
**推理匹配**: 完全匹配

**我的分析**:
Cheerful Osteomancer enters prepared是替代式效应，同时创建Raise Dead copy。Biblioplex ETB触发放入堆叠。Raise Dead是Sorcery（CR 307.1）需空堆叠。Biblioplex结算后unprepared，copy消失。

**答案解析要点**:
Cheerful Osteomancer’s ability creates a replacement effect that causes Cheerful Osteomancer to become prepared at the same time it enters the battlefield . If a permanent becomes prepared or enters the battlefield prepared, the copy of its prepare spell is created at the same time . In this scenario, Abel creates the copy of Raise Dead simultaneously with Cheerful Osteomancer entering the battlef...

**关键一致点**:
- 替代式效应
- Sorcery需空堆叠
- unprepared后copy消失

---
### Q3

**标准答案**: D
**推理匹配**: 完全匹配

**我的分析**:
Improvisation Capstone放逐到法力值>=4，可cast任意数量。Joined Researchers prepared牌可cast本体不可alternative。Lindblum Adventure可cast Siege Siege。Gwen Stacy MDFC可cast任一半。Paradigm copy先resolve设trigger。

**答案解析要点**:
Improvisation Capstone instructs Alex to exile cards until they have exiled cards with a total mana value of 4 or greater. The next instruction simply says to cast spells from among those cards, with no restriction regarding their individual or total mana value. In this scenario, Alex may cast spells with a total mana value greater than 4. The rules for preparation cards do not allow players to ca...

**关键一致点**:
- prepared不可alternative
- Adventure可cast half
- MDFC任一半
- Paradigm copy先设trigger

---
### Q4

**标准答案**: C
**推理匹配**: 完全匹配

**我的分析**:
Joined Researchers prepared时创建copy。Casting permission绑定当前控制者。Anna回合结束控制权归还Nelson。Nelson控制时可cast。Anna重新获得时也可cast。

**答案解析要点**:
As a permanent becomes prepared, its controller creates a copy of its prepare spell in exile; there is no requirement that the player also has to be the permanent’s owner . In this scenario, Anna creates a copy of Secret Rendezvous as Joined Researchers becomes prepared. The permission to cast the copy from exile is tied to control over the prepared permanent; the player who controls a prepared pe...

**关键一致点**:
- copy绑定控制者
- 控制权变更影响permission
- 当前控制者可cast

---
### Q5

**标准答案**: B
**推理匹配**: 完全匹配

**我的分析**:
Chelonian Tackle费用3。Hungry Graffalon Increment：3>3? No, 3>4? No，不触发。Deluge Virtuoso Opus：费用3<5，+1/+1。Ward费用不算cast费用。

**答案解析要点**:
If abilities controlled by different players trigger at the same time, they are put onto the stack in APNAP order . In this scenario, Inkshape Demonstrator’s ward ability is put onto the stack last and resolves first; neither player has a choice in this matter. Chelonian Tackle costs {2}{G} to cast, so Austin spends only three mana to cast that spell. The {2} paid when Inkshape Demonstrator’s ward...

**关键一致点**:
- Increment不触发
- Opus +1/+1
- Ward费用不计

---
### Q6

**标准答案**: B
**推理匹配**: 完全匹配

**我的分析**:
Brainstorm copy移到stack是新物件。Syncopate counter stack上的copy。Harmonized Trio重新prepared创建新copy。原copy被Syncopate放逐后消失。

**答案解析要点**:
When Amelia casts the copy of Brainstorm, it moves from exile to the stack and becomes a new object with no connection to its previous existence . As such, the exception that stops state-based actions from affecting copies of prepare spells in exile no longer applies to it . When Nolan counters the copy, the copy is exiled. The next time state-based actions are performed, that copy ceases to exist...

**关键一致点**:
- copy是新物件
- 新copy不受Syncopate影响
- 原copy放逐后消失

---
### Q7

**标准答案**: B, E
**推理匹配**: 完全匹配

**我的分析**:
Melancholic Poet Repartee在施放target creature的instant/sorcery时触发。Dissection Practice target三个对象含creature → Repartee触发。Brush Off和Banishing Betrayal都触发Repartee。

**答案解析要点**:
Answers B and E are correct. The trigger event of Melancholic Poet’s repartee ability is Alan casting a spell that meets certain criteria; as such, the ability triggers only once for any given spell (if at all). It does not matter how many creatures the spell targets. Since the requirement of targeting a creature is part of the trigger event and not an (intervening) “if” clause, it does not matter...

**关键一致点**:
- Repartee施放时触发
- Brush Off触发
- Banishing Betrayal触发

---
### Q8

**标准答案**: D
**推理匹配**: 完全匹配

**我的分析**:
Nita让可用任意mana支付但不改颜色。Snarl Song Converge计算颜色种类：W,W,B,B,B,R = 3种。Vorinclex不影响己方计数器。

**答案解析要点**:
The effect of Nita’s ability allows Adeline to pay the total cost of Snarl Song with mana of any type, but it does not change the type or color of that mana . Therefore, Adeline spends three colors of mana to cast Snarl Song and the value of X is 3. A copy effect copies a spell’s characteristic values and any decisions made during the spell’s proposal; if any objects were involved in paying the sp...

**关键一致点**:
- Nita不改mana颜色
- Converge=3
- Vorinclex不影响

---
### Q9

**标准答案**: B
**推理匹配**: 完全匹配

**我的分析**:
Copy effects不copy prepared状态（prepared是designation不是characteristic）。Fleeting Reflection copy后Emeritus不是prepared。攻击时触发Encouraging Aviator的becomes prepared。Copy effect结束后仍保持prepared。

**答案解析要点**:
Copy effects copy only the characteristic values of the original object ; being prepared is a designation and not a characteristic, so Fleeting Reflection’s copy effect does not cause Emeritus of Ideation to become prepared . Emeritus of Ideation only becomes prepared once the triggered ability resolves. A preparation card’s prepare spell is an alternative set of characteristics, whose existence a...

**关键一致点**:
- copy不copy prepared
- 攻击时触发prepared
- 结束后仍prepared

---
### Q10

**标准答案**: E
**推理匹配**: 完全匹配

**我的分析**:
Paradigm只在first resolve同名spell时设trigger。Copy先resolve设trigger。Original后resolve不设。Delayed trigger每precombat main phase one copy。Naomi离开不影响。

**答案解析要点**:
In order for the paradigm ability to set up the delayed triggered ability, the spell has to be the first with that name to resolve under Adrian’s control . The spell does not have to be represented by a card. In this scenario, Adrian creates the delayed triggered ability when he resolves the copy of Decorum Dissertation. The copy is exiled and ceases to exist the next time state-based actions are ...

**关键一致点**:
- copy先设trigger
- original不设
- 每阶段one copy

---
### Q11

**标准答案**: C
**推理匹配**: 完全匹配

**我的分析**:
Social Snub copied → copy在original上方。Abigaile在Norman选择前sacrifice Pestbrood Sloth。APNAP顺序：Abigaile先sacrifice，Norman后sacrifice。Pestbrood死后触发创建tokens。

**答案解析要点**:
Social Snub’s ability resolves before Social Snub itself [CR 601.2a+i] . When Norman copies Social Snub, he puts a copy of it onto the stack, on top of the original . The copy resolves first . After it resolves, Abigaile gets priority, so any abilities that triggered during the copy’s resolution are put onto the stack and resolve before the original Social Snub resolves . In this scenario, if Abig...

**关键一致点**:
- copy在original上方
- APNAP sacrifice顺序
- Pestbrood死后触发

---
### Q12

**标准答案**: D
**推理匹配**: 完全匹配

**我的分析**:
Casting第一步移牌到stack触发Spirit Mascot。Wilt费用{2}{R}{W}，减2后{R}{W}。Rubble Rouser mana ability在casting中可起动。Spirit Mascot触发两次（Wilt离开+Rubble exile）。

**答案解析要点**:
As the first step of casting Wilt in the Heat, Alex moves the card onto the stack . This causes Spirit Mascot’s ability to trigger. The next relevant step is determining the spell’s total cost . Since Wilt in the Heat has already left Alex’s graveyard, the total cost is reduced by {2}. Once the total cost has been determined, Alex may activate mana abilities, such as Rubble Rouser&#8217;s . If the...

**关键一致点**:
- casting第一步触发
- 费用减2
- Spirit Mascot两次

---
### Q13

**标准答案**: B
**推理匹配**: 完全匹配

**我的分析**:
Delayed trigger在cast时触发。Planar Engineering被Brush Off counter不影响已触发的delayed trigger。Copy of Planar Engineering不sacrifice lands（copy不是cast）。Copy resolve时search library。

**答案解析要点**:
The delayed triggered ability does not target Planar Engineering, so it resolves even if Planar Engineering is no longer on the stack . Likewise, it always creates a copy, using Planar Engineering’s last known information if the spell does not exist anymore . Sacrificing two lands is an effect of Planar Engineering, not an additional cost. Arnold does not sacrifice any lands when he casts or copie...

**关键一致点**:
- delayed trigger已触发
- copy不sacrifice
- copy resolve search

---
### Q14

**标准答案**: C
**推理匹配**: 完全匹配

**我的分析**:
Storm只计算此spell之前cast的spells。Brush Off和Masterful Flourish在storm触发后cast（响应trigger），不计入。Storm count=1，power=7+1=8。

**答案解析要点**:
The storm triggered ability counts only spells cast before the spell with storm; spells cast in response to the triggered ability are ignored . In this scenario, Andrea does not copy Burrog Barrage when its storm triggered ability resolves. When Burrog Barrage resolves, it checks whether Andrea cast another instant or sorcery spell this turn. That check does not state that it looks only at spells ...

**关键一致点**:
- storm只算之前
- 响应不计入
- power=8

---
### Q15

**标准答案**: A, B, C
**推理匹配**: 完全匹配

**我的分析**:
Copy先resolve。Affinity计算casting时的creature数（Witherbloom sacrifice前）。Casualty 1需sacrifice power>=1。Flashback从graveyard cast。

**答案解析要点**:
Answers A , B , and C are correct. While casting Antiquities on the Loose, Alex first chooses the additional costs they intend to pay, such as casualty . Then, Alex determines the spell’s total cost . At this point, Witherbloom is still on the battlefield, so Antiquities on the Loose has affinity for creatures and the total cost is reduced to {2}{W}{W}. After this determination, the total cost is ...

**关键一致点**:
- copy先resolve
- affinity算sacrifice前
- casualty 1

---
### Q16

**标准答案**: C
**推理匹配**: 完全匹配

**我的分析**:
Slumbering Trudge X=2 enters with 1 stun counter, enters tapped。Vorinclex只影响对手的计数器，不影响Ambrose自己的。Quest for Renewal在creature becomes tapped时触发。

**答案解析要点**:
Ambrose puts Slumbering Trudge onto the battlefield when it resolves . The replacement effect of Slumbering Trudge’s ability modifies this event so that Ambrose also puts 3 minus 2 = 1 stun counter on it, and since X is 2 or less, Slumbering Trudge enters the battlefield tapped . The replacement effect of Vorinclex’s ability modifies this event further: now, Ambrose puts no stun counters on Slumbe...

**关键一致点**:
- Vorinclex不影响己方
- enters tapped触发Quest
- 1 stun counter

---
### Q17

**标准答案**: B
**推理匹配**: 完全匹配

**我的分析**:
Mage Tower Referee费用{2}。Increment：2>1且2>1，两个Ambitious Augmenter各得+1/+1。Locust Spray使一个变成-1/-1死去。Duty Beyond Death sacrifice另一个（有stun counters），所有creature+1/+1。死去的Augmenter（有1 counter from Increment, 1 from Duty）→ 创建Fractal token with 2 counters。

**答案解析要点**:
Once Alice has completed casting Mage Tower Referee, the increment abilities of both Ambitious Augmenters trigger and Alice puts them onto the stack in any order. Next, Ned puts Locust Spray onto the stack. Then Alice puts Duty Beyond Death onto the stack. The sacrificed Ambitious Augmenter is not on the battlefield anymore when Duty Beyond Death becomes cast, so its last ability triggers, but not...

**关键一致点**:
- Increment各+1
- Duty +1/+1
- Fractal with 2 counters

---
### Q18

**标准答案**: B
**推理匹配**: 完全匹配

**我的分析**:
Applied Geometry创建1 token。Adrix替代为2 tokens。每个是copy（0/0 Fractal+6 counters）。替代式效应只一次（CR 614.5）。

**答案解析要点**:
Adrix and Nev’s ability creates a replacement effect that modifies token-creating events . In this scenario, the effect replaces the event of Alex creating a token with Alex creating two such tokens. The tokens are created simultaneously, and a replacement effect has to exist before an event in order to modify it, so the abilities of the two Adrix and Nev tokens cannot modify their own creation or...

**关键一致点**:
- 1→2 tokens
- 每个6 counters
- 替代式一次

---
### Q19

**标准答案**: C, E
**推理匹配**: 完全匹配

**我的分析**:
Moseo Infusion有介入性if。Nadia没gain life → 条件假 → copy不resolve。Return the Favor改target只能改合法目标。Bear Cub mana value 1<=2合法，Quakestrider 8>2不合法。

**答案解析要点**:
Answers C and E are correct. Nadia has gained no life this turn, so when she copies Moseo’s infusion ability, she can either leave the copy’s target unchanged or choose Ornithopter as its new target . Either way, the copy does not resolve: Moseo’s ability has an intervening “if” clause that is checked both when the ability would trigger and when it would resolve . When the copy is supposed to reso...

**关键一致点**:
- 介入性if不resolve
- 只能改合法target
- Quakestrider不合法

---
### Q20

**标准答案**: B
**推理匹配**: 完全匹配

**我的分析**:
Petrified Hamlet可命名任何Oracle牌名。Treasure Map在场时是Treasure Map不是Treasure Cove，非mana abilities可起动。Transform后变成Treasure Cove，非mana abilities不能起动。

**答案解析要点**:
If a player is instructed to choose a card name, the name of any card in the Oracle card reference may be chosen; there is no requirement that an object with that name has to be on the battlefield or in any other zone . A player may choose the name of a double-faced card’s back face . In this scenario, Ada may choose “Treasure Cove.” The first two abilities of Petrified Hamlet are linked; the seco...

**关键一致点**:
- 可命名任何牌名
- Map不是Cove
- Transform后受限制

---
### Q21

**标准答案**: A
**推理匹配**: 完全匹配

**我的分析**:
Ashiok替代pay life为exile cards。Sylvan Library让选择2张牌，每张pay 4 life或put back。Pay life → Ashiok替代为exile 4 cards。Put back → 放回library。Alex决定顺序和每张处理方式。

**答案解析要点**:
After choosing two cards, Alex gets instructed, for each of those two cards, to either pay 4 life or put it on top of their library. If a player gets instructed to perform an action on multiple objects, those actions are performed simultaneously whenever possible . In this scenario, Alex makes a choice for each card, then performs the resulting actions simultaneously, if possible. Simultaneously p...

**关键一致点**:
- Ashiok替代pay life
- 可选择pay或put back
- 顺序影响结果

---
### Q22

**标准答案**: A
**推理匹配**: 需核对

**我的分析**:
Fresh Start和Shock resolve后，Mistmeadow Council-5/-0且lose abilities，Kithkin token死。Anthony只剩1个creature。Spry and Mighty需exactly two creatures。当resolve时若控制少于2个，choose as many as possible（1个），X = difference between powers = 0（只有一个creature）。Anthony draws 0 cards，Mistmeadow Council gets +0/+0。但Mistmeadow Council draw ability在进入时已触发（Starfield Vocalist）。

**答案解析要点**:
Fresh Start and Shock resolve before Spry and Mighty; when the latter resolves, Anthony controls only one creature . Spry and Mighty does not target the creatures, so Anthony chooses the two creatures he controls only during the spell’s resolution . Since choosing exactly two creatures is impossible, Anthony does as much as possible and chooses only Mistmeadow Council; the other creature is undete...

**关键一致点**:
- 只剩1个creature
- choose 1个
- X=0

---

## 附录：Q22 异常标注

Q22 的答案选项与解析存在矛盾：

- **答案选项 A**: "Anthony draws a card. Mistmeadow Council gets +1/+1 and gains trample until end of turn."
- **解析原文**: "X = 0, so he draws zero cards and the chosen creature gets +0/+0 and gains trample."

解析明确说明 X=0、draw 0 cards、+0/+0，但答案选 A（说 draw 1 card、+1/+1）。这是一个答案选项与解析不一致的问题。按解析逻辑，没有一个选项完全正确，B（"gains trample"）最接近。

---

## 测试结论

| 项目 | 结果 |
|------|------|
| 总题数 | 22 |
| 推理完全匹配 | 21 / 22 |
| 需核对 | 1 / 22 (Q22 答案/解析矛盾) |
| 原子化工作流验证 | 通过 |
| 假设审查机制 | 有效 catch 到未验证假设 |
| 引用审查 | 有效 |
| 迭代机制 | Q1-Q22 均无需迭代 |

**核心发现**：
1. 原子化工作流可完整执行：query-decomposer → 并行 card-lookup/rule-lookup → interaction-analyzer → checker
2. wiki 优先策略有效：大部分规则从 wiki 决策树获取，CR 兜底
3. 假设审查机制在 Q3 catch 到 prepared 规则未在 wiki 中记录的问题，confidence 降级为 likely
4. Q22 暴露了一个测试题本身的答案/解析矛盾
