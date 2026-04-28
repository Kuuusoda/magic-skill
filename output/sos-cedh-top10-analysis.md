# SOS（Secrets of Strixhaven）系列 cEDH 十大瞩目新牌分析

> 数据来源：`raw/data/oracle-cards-lite.json`  
> 分析范围：SOS 主系列（368 张）+ SOC 指挥官预组（426 张）  
> 分析日期：2026-04-15

## 分析框架

在 cEDH（竞技型指挥官）环境中，一张牌的价值主要取决于以下几个维度：

1. **费用效率**：低费咒语优先，高费咒语必须有终结游戏的能力
2. **资源循环**：能否赚卡、赚费、或提供稳定的法术力基础
3. **互动能力**：反击、去除、锁场（Stax）在多人竞技局中至关重要
4. **组合技潜力**：能否作为 combo piece 或 commander 直接支撑一套组合技体系
5. ** commander 独特性**：新的传奇生物/鹏洛客是否开辟了全新的套牌思路

基于以上标准，从 SOS + SOC 的 794 张牌中筛选出以下 10 张最值得关注的牌。

---

## Top 10 卡牌详解

### 1. Prismari, the Inspiration（SOS）

**费用**：{5}{U}{R}  
**类型**：传奇生物 ~ 长老龙  
**异能**：飞行；守护—支付 5 点生命；由你施放的瞬间和法术咒语具有**风暴（Storm）**。

**cEDH 评析**：
这是整个 SOS 系列中最具爆炸性的设计之一。风暴是万智牌中最强的机制之一，而 Prismari 将其赋予了**你施放的每一个瞬间和法术**。这意味着你不需要依赖传统的 Grapeshot / Tendrils of Agony 作为终结手段——任何便宜的烧牌、抽牌咒语，甚至是一张裸下的 Ritual，都可能在长串连锁后复制出十几份。

- **优势**：一旦启动，几乎所有 spellslinger 套牌都能变成风暴套牌；5 费身材带飞行+守护，存活率尚可。
- **劣势**：5 费指挥官偏慢，且对手会优先去除。
- **潜在套牌**：UR Storm、High Tide、Divergent Transformations 路线的指挥官版本。

---

### 2. Page, Loose Leaf（SOS）

**费用**：{2}  
**类型**：传奇神器生物 ~ 组构体  
**异能**：{T}：加 {C}；壮丽—弃置另一张名为 Page, Loose Leaf 的牌：磨库直到翻出一张瞬间或法术牌，将该牌置入你的手牌，其余置于牌库底。

**cEDH 评析**：
在万智牌历史上，**2 费且能产费的无色指挥官**屈指可数。Page 不仅是 mana dork，更是 colorless 套牌梦寐以求的低费曲线。虽然壮丽异能因需要第二张同名卡而难以触发，但在 EDH 中可以通过复制效应（如 Sculpting Steel）或克隆 token 来实现。

- **优势**：2 费无色，完全不绑定颜色，可以带领一套纯无色或 artifact combo 套牌。
- **劣势**：本身没有致胜异能，需要配合组合技（如 Basalt Monolith + Rings of Brighthearth）。
- **潜在套牌**：Colorless Artifact Combo、Karn 风格的 Stax/Combo 混合套牌。

---

### 3. Dina's Guidance（SOS）

**费用**：{1}{B}{G}  
**类型**：瞬间  
**效应**：从你的牌库中搜寻一张生物牌，展示之，将它置于你的手牌或坟墓场，然后洗牌。

**cEDH 评析**：
这是一张被严重低估的牌。它是**瞬间 speed 的 Worldly Tutor + Entomb 二合一**，而且不需要额外支付生命或让牌库顶牌暴露。2 费在 BG 色组中非常优质，可以：
- 在对手回合末找到关键 combo creature（如 Protean Hulk）直接丢进坟场
- 在手牌中作为常规的生物导师使用

- **优势**：瞬间 speed、选择灵活（手牌 or 坟场）、费用低廉。
- **劣势**：每局游戏只能带一张（非指挥官）。
- **适用套牌**：几乎所有 BG 或包含 BG 的 cEDH 套牌都会考虑它。

---

### 4. Quandrix, the Proof（SOS）

**费用**：{4}{G}{U}  
**类型**：传奇生物 ~ 长老龙  
**异能**：飞行、践踏、**倾曳（Cascade）**；由你从你手中施放的瞬间和法术咒语具有倾曳。

**cEDH 评析**：
自己带倾曳已经够强了，更可怕的是它把倾曳赋予了**所有从手中施放的瞬间和法术**。这意味着：
- 你施放 0 费咒语（如 Mox）时，倾曳会翻出你牌库里下一张免费的牌
- 你施放任何 cantrip（如 Brainstorm）时，都会额外附赠一个免费咒语
- 配合 "0 费神器大军" 可以打出极其夸张的连锁

- **优势**：GU 色组有优质的 ramp 和 protection，4 费指挥官配合加速可以在 T2-T3 登场。
- **劣势**：4 费在 cEDH 中仍不算最快，且倾曳结果是随机的。
- **潜在套牌**：GU Cascade Value、Food Chain（倾曳可能直接翻出 Food Chain 本身）等。

---

### 5. Mana Sculpt（SOS）

**费用**：{1}{U}{U}  
**类型**：瞬间  
**效应**：反击目标咒语。若你操控一个法师，则在你的下一个行动阶段开始时，加数量等同于施放该咒语所花费之法术力的 {C}。

**cEDH 评析**：
对于**操控法师**的套牌来说，这几乎是一张**免费的反击咒语**。在 cEDH 中，你通常会用 {1}{U}{U} 或更少的费用反击对手的 key spell，然后在下回合的行动阶段把全部费用赚回来。

- **优势**：对于法师 tribal（如 Inalla、Adeliz 或某些 Storm 套牌）而言，这是 Mental Misstep 级别的资源效率。
- **劣势**：非法师套牌只能当普通的 2 费反击使用，竞争力一般。
- **适用套牌**：任何以法师为核心或含有大量法师生物的 spellslinger 套牌。

---

### 6. Silverquill, the Disputant（SOS）

**费用**：{2}{W}{B}  
**类型**：传奇生物 ~ 长老龙  
**异能**：飞行、警戒；由你施放的每个瞬间和法术咒语具有**伤亡 1（Casualty 1）**。

**cEDH 评析**：
伤亡 1 意味着你可以牺牲一个力量 ≥1 的生物来**复制**该瞬间/法术咒语。在 cEDH 的 aristocrats 或 token 套牌中，廉价生物遍地都是（Deranged Hermit、Dockside Extortionist 产出的宝藏衍生物也可以被牺牲）。这让 Silverquill 成为一张**低费却高上限**的 copy engine。

- **优势**：2WB 费用极低；飞行+警戒提供稳定的进攻/防守；复制 Demonic Tutor、Ad Nauseam 等牌的价值不可估量。
- **劣势**：需要生物作为燃料，纯控制套牌较难发挥。
- **潜在套牌**：WB Aristocrats、Tymna + Silverquill 搭档组合。

---

### 7. Nita, Forum Conciliator（SOS）

**费用**：{1}{W}{B}  
**类型**：传奇生物 ~ 人类/顾问  
**异能**：每当你施放一个你不拥有的咒语时，在由你操控的每个生物上各放置一个 +1/+1 指示物；{2}，牺牲另一个生物：放逐目标对手坟墓场中的一张瞬间或法术牌。你可以在本回合施放它，且你可以使用任意类别的法术力来施放该咒语。若该咒语将被置入坟墓场，则改为放逐之。

**cEDH 评析**：
Nita 是一个**兼具 graveyard hate、资源窃取和增幅**的 2 费指挥官。在 cEDH 中，对手坟场里几乎总有可用的咒语（Counterspell、Tutor、Draw spell）。你可以主动牺牲廉价衍生物来「借」用对手的资源，同时给自己的生物团队 buff。

- **优势**：费用极低（1WB）； graveyard hate 在 meta 中价值极高；异能不限制目标数量，只要不断牺牲就能不断使用。
- **劣势**：需要对手坟场有货，且是法术力时机。
- **潜在套牌**：Tymna 搭档、WB Hatebears 或 Theft 主题。

---

### 8. Mica, Reader of Ruins（SOS）

**费用**：{3}{R}  
**类型**：传奇生物 ~ 人类/神器师  
**异能**：守护—支付 3 点生命；每当你施放一个瞬间或法术咒语时，你可以牺牲一个神器。若你如此做，则复制该咒语，且你可以为其选择新的目标。

**cEDH 评析**：
3 费红色指挥官，自带 Fork 效果，且触发条件只需要「施放瞬间/法术 + 牺牲神器」。在 artifact-heavy 的 storm 套牌中，这相当于你的每一个关键咒语都可以被复制。尤其值得注意的是，这个复制不需要支付额外费用，只需要一个廉价的神器（如 Mox、Treasure token、Mana Crypt 的复制 token）。

- **优势**：红色少有的稳定复制引擎；守护异能使其难以被廉价去除指向。
- **劣势**：3 费纯红，色组限制较大，需要 artifact ramp 支撑。
- **潜在套牌**：Mono-R Artifact Storm、Prosper 风格或 Daretti 风格的 combo 套牌。

---

### 9. Study Hall（SOC）

**费用**：无（地牌）  
**类型**：地  
**异能**：{T}：加 {C}；{1}，{T}：加一点任意颜色的法术力。当你使用此法术力来施放你的指挥官时，占卜 X，X 为本局游戏中它从统帅区被施放的次数。

**cEDH 评析**：
Study Hall 是一张为 Commander 赛制量身定做的地牌。它的定位和 Command Tower 类似，但额外附赠了**指挥官加速/修正 + 反复施放指挥官时的占卜深度**。对于需要多次从统帅区施放指挥官的套牌（如 Tymna、Thrasios 等 value commanders），占卜 3-5 次可以显著提升牌库质量。

- **优势**：无色地牌，几乎可以进所有套牌；提供 commander mana fixing；后期占卜价值高。
- **劣势**：进场可能是 tapped（不在文本中明确说明，但作为标准设计通常是的，不过此牌文本未写 enters tapped，所以可能是**未横置地进场**！）—— 若为未横置进场，则强度更高。
- **适用套牌**：几乎所有 cEDH 套牌都会考虑携带。

---

### 10. Rootha, Mercurial Artist（SOC）

**费用**：{1}{U}{R}  
**类型**：传奇生物 ~ 兽人/祭师  
**异能**：{2}，将 Rootha 移回其拥有者手上：复制目标由你操控的瞬间或法术咒语。你可以为该复制品选择新的目标。

**cEDH 评析**：
Rootha 是一个**极其灵活的复制工具**。她可以：
- 复制你的高价值 tutor（如 Mystical Tutor）
- 复制终结技（如 Brain Freeze、Grapeshot）
- 复制互动咒语（如 Counterspell 反击两个不同的咒语）
- 每次使用后只需 2 费即可「重置」并再次使用

- **优势**：费用极低（1UR），复制能力无限次循环使用；可以躲避 board wipe  by 回手。
- **劣势**：需要 2 费「充电」回合，且本身是生物，容易被去除。
- **潜在套牌**：UR Storm、Jeskai/Izzet Spellslinger、任何需要额外 spell copy 的 combo 套牌。

---

## 归纳总结

### 系列整体特征

SOS（Secrets of Strixhaven）+ SOC 的 cEDH 可用牌呈现出非常鲜明的主题倾向：

| 主题 | 代表牌 | 评价 |
|------|--------|------|
| **Spellslinger / Storm** | Prismari, Quandrix, Silverquill, Rootha, Mica | 这是 SOS 最强势的 design space，大量新牌直接赋能瞬间和法术 |
| **Tutor / 资源循环** | Dina's Guidance, Mana Sculpt | 2 费瞬间 speed 的 tutor 和资源咒语，竞技价值极高 |
| **Commander 多样性** | Page, Nita, Prismari, Silverquill | 出现了 2 费无色、2 费 WB、2 费 UR 等低费 commander |
| **地牌支持** | Study Hall, Petrified Hamlet, Great Hall of the Biblioplex | 地牌设计贴合 commander 赛制， Study Hall 有望成为泛用 staple |

### cEDH 展望

- **最可能改变 meta 的牌**：**Prismari, the Inspiration**。在正确的构筑下，它可能是第一个真正让 "Storm Commander" 成为 T1 竞争力的牌。
- **最泛用的 staple**：**Study Hall** 和 **Dina's Guidance**。前者是地牌，后者是 tutor，两者都会进入大量套牌的主牌。
- **最具潜力的冷门 commander**：**Page, Loose Leaf**。2 费无色 commander 的历史地位不容小觑，artifact combo 玩家一定会深入研究。

---

*分析基于 SOS/SOC 的英文 Oracle 数据。部分牌的具体裁定（如 Prismari 的风暴与 commander tax 的互动）需等待正式发售后以 CR 为准。*
