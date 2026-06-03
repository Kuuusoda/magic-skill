# 知识库日志

按时间顺序记录的 Ingest、Query 和 Lint 操作。

## [2026-06-03] ingest | 完整规则（CR）2026年4月17日中文版更新

将中文 CR 更新至 2026-04-17 生效版（Secrets of Strixhaven）：
- `magic-comp-rules-zh-cn/markdown/` → `raw/cr/`（9 个文件变更）
- 规则结构变化：新增 730 节「与永久物结聚」、732「进行简化」、733「处理非法动作」
- 类别更新：书籍、突变剂、德连、长颈鹿、乌创
- 异能提示新增：消失、输注、炫示、连辞
- 新建来源摘要：wiki/sources/2026-06-03-cr-2026-apr17-zh.md
- 更新概念页：wiki/concepts/comprehensive-rules.md
- 更新索引：wiki/index.md

## [2026-06-03] ingest | MTR 2026-02-27 英文版 + IPG 2024-09-23 英文版

将官方英文 PDF 转录为 Markdown：
- MTR PDF `MTG_MTR_2026_Feb27_EN-2.pdf` → `raw/mtr/mtr_2026_feb27_en.md`（56 页，10 章 + 6 附录）
- IPG PDF `mtg_ipg_2024sep23_en.pdf` → `raw/ipg/ipg_2024_sep23_en.md`（31 页，4 节 + 2 附录）
- 新建来源摘要：wiki/sources/2026-06-03-mtr-2026-feb27-en.md、wiki/sources/2026-06-03-ipg-2024-sep23-en.md
- 更新概念页：wiki/concepts/magic-tournament-rules.md（增加英文原文引用）、wiki/concepts/infraction-procedure-guide.md（英文原文引用）
- 更新索引：wiki/index.md

## [2026-05-20] ingest | WPN 零售商方针

来源 URL https://wpn.wizards.com/zh-Hans/wpn-retailer-policies#PromosProducts，因中文页面 JS 动态渲染限制，实际摄入英文版完整文本：
- 保存源文件：raw/wpn_retailer_policies.md
- 新建来源摘要：wiki/sources/2026-05-20-wpn-retailer-policies.md
- 新建概念页：wiki/concepts/wpn-retailer-policies.md（含产品发布规则、促销物品管理、店家义务、营销材料政策）
- 更新索引：wiki/index.md

## [2026-05-01] ingest | 摩登环境破解报告生成与策略分支 Wiki 构建

基于 output/modern_tournament_breaker.html 数据源，构建策略分支摩登专题：
- 新建决策树 3 篇：modern-meta-selection（Meta 套牌选择）、modern-sideboard（备牌决策）、modern-anti-energy（对抗 Boros Energy）
- 新建环境快照 1 篇：meta-snapshots/2026-05-01-modern（含 Meta 分布、食物链、备牌趋势）
- 新建套牌分析 3 篇：decks/boros-energy、decks/affinity、decks/jeskai-blink（含机制拆解、示例牌表、备牌局策略）
- 新建单卡评估 1 篇：card-evaluations/modern-2026-05（主牌威胁 + 备牌互动，含携带量建议）
- 更新索引：strategy/index.md、formats/modern.md

## [2026-04-27] ingest | MTR 2026-02-27 核对与补充

核对 raw/MTG_MTR_2026_Feb27_EN.pdf 与现有 raw/mtr/ 文件：
- 确认现有文件已基于 2026-02-27 版本（章节 1–10 及附录 A/B）
- 补充缺失的 4 个附录：附录 C（平分处理释疑）、附录 D（限制赛推荐补充包构成）、附录 E（瑞士式比赛建议轮数）、附录 F（各比赛的执法严格度）
- 更新 raw/mtr/README.md、wiki/sources/2026-04-14-mtr.md

## [2026-04-14] init | 创建 Wiki 结构

建立了 raw/、wiki/、output/ 三层目录，创建了 CLAUDE.md 规范、index.md 和页面模板。

## [2026-04-14] ingest | 万智牌官方文档资料集

用户将万智牌相关资料放入 raw/ 目录，包括：完整规则 Markdown 中文版（含 9 章及词汇表）、完整规则 PDF 英文版、违规处理方针（IPG）全套 Markdown、比赛规则（MTR）全套 Markdown、全牌张 JSON 数据库。完成以下操作：
- 整理 raw/ 目录：将 markdown/ 重命名为 cr/，PDF 移入 cr/，JSON 移入 data/
- 创建来源摘要页 5 篇（cr-markdown、cr-pdf、ipg、mtr、all-cards-json）
- 创建实体页 2 篇（威世智有限公司、DCI）
- 创建概念页 5 篇（完整规则、违规处理方针、比赛规则、执法严格度、万智牌赛制）
- 创建综合页 1 篇（万智牌官方文档体系概览）
- 更新 index.md 与 log.md

## [2026-04-14] ingest | 万智牌全牌张数据库深入学习

对 raw/data/all-cards-20260414092108.json（2.3GB，526,803 张卡片记录）进行了系统性的数据清洗、拆分和深度分析。具体工作：
- 运行 Python 脚本流式处理 2.3GB JSON，提取出 37,230 张唯一英文版 Oracle 牌
- 生成辅助索引文件：sets-index.json（1,028 个系列）、keywords-index.json（738 个关键字）、types-index.json（51 个类型标记）、colors-dist.json（32 种颜色组合）、formats-dist.json（21 种赛制）、cmc-dist.json、supertypes-dist.json、subtypes-dist.json
- 创建来源摘要更新（全牌张数据库页增加分析成果说明）
- 创建概念页 4 篇：牌张类型体系、关键字异能总览、五色轮、生物、神器、瞬间、法术、结界、地、鹏洛客
- 创建常青关键字概念页 16 篇：飞行、践踏、警戒、敏捷、闪现、系命、死触、先攻、连击、辟邪、守护、威慑、延势、守军、不灭、保护
- 创建机制/动作概念页 9 篇：磨牌、占卜、循环、多踢、闪回、刺探、转化、变身、侦查
- 创建综合页 1 篇：万智牌赛制可用性分析
- 更新 index.md 以完整收录所有新页面

## [2026-04-14] ingest | 深入拆解万智牌完整规则（CR）

系统阅读并拆解了 raw/cr/ 目录下的《万智牌完整规则》Markdown 中文版，重点拆分了第一章（游戏概念）、第五章（回合结构）、第六章（咒语/异能/效应）以及第四章（区域）的核心规则。具体创建页面如下：
- CR 核心概念页 22 篇：万智牌的最高原则、APNAP、永久物与物件、区域、堆叠、时机和优先权、回合结构、战斗阶段、施放咒语、费用、法术力、目标、异能、持续性效应、替代性效应与防止性效应、状态动作、衍生物、指示物、特殊动作、生命与伤害、抓牌、传奇规则
- 所有页面均包含精确的 CR 条文引用（如 CR 101.4、CR 601.2、CR 704.5 等），并建立了与现有牌张类型页、关键字异能页、数据库分析页之间的交叉引用
- 更新 index.md 新增 "CR 核心规则" 分类
- 当前 Wiki 总计：来源页 5 篇、实体页 2 篇、概念页 43 篇、综合页 2 篇

## [2026-04-14] lint | 万智牌 Wiki 健康检查

运行 `raw/data/lint_wiki_v2.py` 对全 Wiki 进行链接健康检查与孤立页面扫描：
- 总页面数：75 页
- 孤立页面：0 个（所有页面均有至少 1 条入链）
- 断链目标：0 个（所有内部 WikiLink 均解析成功）
- 修复过程：通过优化 `comprehensive-rules.md` 的「相关概念」交叉引用，将 14 个剩余孤儿页全部接入网络；修正 lint 脚本的中文标题匹配逻辑（引入「clean title」精确匹配优先），消除 `法术/法术力`、`异能/起动式异能` 等前缀歧义导致的假阳性
- 入链最多页面：`完整规则（Comprehensive Rules，CR）`（71 个入链）、`万智牌赛制`（33 个）、`万智牌关键字异能总览`（27 个）

## [2026-04-14] output | 原创万智牌卡牌生成器

在 `output/card-generator/` 下实现了一个基于 Wiki 知识库的智能卡牌生成工具：
- `generate_card.py`：主脚本，支持 Prompt 模式（默认）和 API 模式（需 `ANTHROPIC_API_KEY`）
- 核心能力：自动分析用户输入，从 `wiki/concepts/` 中提取相关规则概念（如飞行、敏捷、传奇规则等），将知识注入 LLM Prompt
- `templates/prompt_template.md`：可自定义的 Prompt 模板
- `generated/sample-dragon.md` / `.json`：示例输出「烬翼龙母卡拉达」
- 输出格式：Markdown 渲染 + 结构化 JSON，包含双语名称、规则叙述、风味叙述、设计笔记

## [2026-04-17] lint | 万智牌 Wiki 健康检查

运行 `raw/data/lint_wiki_v2.py` 对全 Wiki 进行定期健康检查：
- 总页面数：75 页
- 孤立页面：0 个（所有页面均有至少 1 条入链）
- 断链目标：0 个（所有内部 WikiLink 均解析成功）
- 状态：Wiki 结构保持健康，交叉引用网络完整

## [2026-04-19] ingest | 大规模补充缺失页面与补全原始文档链接

系统性地补充了 Wiki 中缺失的 MTR/IPG 细分规则页、具体赛制页、高频机制页和实体人物页，所有页面均链接回 `raw/` 目录下的原始规则文档。同时修复了所有新生成的孤儿页和断链。

### 新增页面
- **MTR/IPG 规则页 7 篇**：牌手权利与义务、主牌与备牌、洗牌要求、牌张代言、游戏行动失误、比赛失误、举止违背运动道德
- **具体赛制页 6 篇**：标准赛、先驱、摩登、薪传、限制赛、指挥官（更新）
- **高频机制页 3 篇**：倾曳（Cascade）、风暴（Storm）、召集（Convoke）
- **实体人物页 2 篇**：理查德·加菲尔德（Richard Garfield）、马克·罗斯沃特（Mark Rosewater）

### 健康检查
- 运行 `lint_wiki_v2.py`：总页面数从 75 增至 92，孤立页面 0，断链目标 0
- 修复过程：在 `comprehensive-rules.md` 中添加全面交叉引用；修正 cascade/storm/legacy/proxy-cards/game-play-errors 中的断链
- 更新 `index.md` 完整收录所有新增页面
- 当前 Wiki 总计：来源页 5 篇、实体页 4 篇、概念页 66 篇、综合页 2 篇

## [2026-04-20] lint | 全面补充缺失的高频概念页面

运行 `raw/data/lint_wiki_v2.py` 进行健康检查，重点扫描新增页面和断链目标，随后系统性地补充了所有缺失的高频概念页和规则概念页。

### 修复的断链
- `proliferate.md`：修复 `感染` → `[[infect|感染（Infect）]]`
- `threshold.md`：修复 `诈术（Delve）` → `[[delve|掘穴（Delve）]]`

### 新增规则概念页（5 篇）
- [[graveyard|坟场]] — 核心区域，被 5 个页面引用
- [[exile|放逐]] — 放逐区规则
- [[discard|弃牌]] — 手牌破坏与坟场填充
- [[color|颜色]] — 五色轮与颜色认同
- [[extra-turn|额外回合]] — 额外回合的触发与顺序

### 新增牌张类型/类别页（3 篇）
- [[equipment|武具]] — 神器副类别与佩带机制
- [[eldrazi|奥札奇]] — 无色异界泰坦生物类别
- [[cedh|cEDH]] — 竞技指挥官赛制

### 新增高频关键字/机制页（15 篇）
- [[delve|掘穴（Delve）]] — 放逐坟场牌替代费用
- [[seek|寻觅（Seek）]] — 数字平台专属随机寻牌
- [[goad|唆使（Goad）]] — 多人游戏中的战斗引导
- [[changeling|变境（Changeling）]] — 具有所有生物类别
- [[manifest|显化（Manifest）]] — 面朝下 2/2 进场
- [[domain|领地（Domain）]] — 基本地类别计数机制
- [[amass|集军（Amass）]] — 创造/增强 Zombie Army
- [[echo|回响（Echo）]] — 延迟支付费用或牺牲
- [[landfall|领地落（Landfall）]] — 地进场触发
- [[ninjutsu|忍术（Ninjutsu）]] — 战斗中换忍者进场
- [[buyback|购回（Buyback）]] — 额外费用使咒语回手
- [[shroud|帷幕（Shroud）]] — 不能被咒语或异能指定为目标

### 补充新增页（第二轮）
- [[sacrifice|牺牲]] — 核心游戏动作
- [[dredge|发掘（Dredge）]] — 坟场填充机制
- [[aura|灵气（Aura）]] — 结界副类别
- [[evoke|唤起（Evoke）]] — 替代性费用进场后牺牲
- [[hand|手牌]] — 核心区域与资源
- [[tribal|部族（Tribal）]] — 牌张类型与生物类别
- [[annihilator|歼灭（Annihilator）]] — 奥札奇攻击触发
- [[combo|组合技]] — 制胜策略体系
- [[mtg-arena|万智牌竞技场]] — 官方数字平台

### 交叉引用修复
- 修复 `creature.md`、`land.md`、`tokens.md`、`morph.md`、`artifact.md`、`kicker.md`、`surveil.md`、`flashback.md`、`turn-structure.md`、`combat-phase.md` 等页面的相关页面链接
- 消除全部剩余孤立页面和断链

### 最终健康检查
- 运行 `lint_wiki_v2.py`：总页面数 141，孤立页面 0，断链目标 0
- 更新 `index.md` 完整收录所有新增页面
- 当前 Wiki 总计：来源页 5 篇、实体页 4 篇、概念页 98 篇、综合页 2 篇

## [2026-04-21] lint | 批量修复链接格式并补充核心节点

### 修复链接格式
- 批量将所有 `[[sources/2026-04-14-cr-markdown|中文]]` 格式链接改为 `[[slug|中文]]` 格式（166 个文件）
- 修复 `lint_wiki_v2.py`：移除对 `index.md`/`log.md` 的排除，使其正确计入入链统计；增加反引号跳过逻辑，避免误判代码块中的 `[[...]]`

### 补充核心节点（20 篇）
- **根节点**：[[magic-the-gathering|万智牌]] — 整个知识树的总览入口
- **赛制 4 篇**：[[draft|轮抽]]、[[sealed|现开]]、[[vintage|特选]]、[[prerelease|售前赛]]
- **规则 1 篇**：[[banned-and-restricted|禁限牌表]]
- **产品 4 篇**：[[set|系列]]、[[block|环境]]、[[booster-pack|补充包]]、[[rarity|稀有度]]、[[sideboard|备牌]]
- **策略 7 篇**：[[deck-archetypes|套牌原型]]、[[card-advantage|卡牌优势]]、[[mana-curve|法术力曲线]]、[[removal|去除]]、[[counterspell|反击咒语]]、[[tutor|检索]]、[[ramp|跳费]]
- **背景 2 篇**：[[multiverse|多重宇宙]]、[[planeswalker-spark|鹏洛客火花]]

### 最终健康检查
- 总页面数 187，断链目标 0，孤立页面 2（index/log 为预期根页面）
- 更新 `index.md` 完整收录所有新增页面与分类
- 当前 Wiki 总计：来源页 5 篇、实体页 4 篇、概念页 118 篇、综合页 2 篇

## [2026-04-21] lint | 全面健康检查与最终修复

### 修复链接格式
- 批量修复所有页面中的 `[[concepts/slug|display]]` 和 `[[sources/slug|display]]` 格式为 `[[slug|display]]`
- 修复所有剩余的纯中文 `[[中文]]` 格式链接为 `[[slug|中文]]` 格式
- 修复 `counterspell.md`、`card-advantage.md`、`removal.md` 中的断链 `[[blue-magic]]` 和 `[[control]]`

### 充实薄页面（17 篇）
- 核心节点：`万智牌`、`套牌原型`、`补充包`、`多重宇宙`、`鹏洛客火花`
- 赛制：`轮抽`、`现开`、`特选`、`禁限牌表`、`售前赛`
- 产品：`系列`、`环境`、`稀有度`、`备牌`
- 策略：`卡牌优势`、`法术力曲线`、`去除`、`反击咒语`、`检索`、`跳费`

### 索引完整性
- 补充 11 个此前遗漏的页面到 `index.md`：灵气、牺牲、组合技、万智牌竞技场、唤起、手牌、部族、歼灭、法术力异能、起动式异能、忠诚异能

### 最终状态
- 总页面数：187
- 断链目标：0
- 孤立页面：2（index/log 为预期根页面）
- 入链最多：`完整规则`（149）、`万智牌赛制`（124）、`关键字异能总览`（85）

## [2026-04-21] lint | 补充高频缺失概念页并修复 lint 脚本

运行数据分析脚本系统扫描缺失的高频关键字与牌张类型页面，发现此前 lint 脚本因排除 `index.md` 导致大量「隐形缺失」未被识别。本次进行了以下工作：

### 修复 lint 脚本
- `lint_wiki_v2.py`：移除对 `index.md` 和 `log.md` 的排除，使索引引用被正确计入入链统计
- 修复 `log.md` 中历史记录残留的旧断链语法（`[[感染]]`、`[[诈术（Delve）]]`）

### 新增概念页（24 篇）
- **超级类型/牌张类型 5 篇**：传奇（Legendary）、基本地（Basic）、雪境（Snow）、亲缘（Kindred）、战役（Battle）
- **高频关键字/机制 19 篇**：结附（Enchant）、伪装（Disguise）、劫掠（Raid）、深入地下城（Venture into the Dungeon）、授形（Bestow）、通渠（Channel）、巨物化（Monstrosity）、幽影（Shadow）、星座（Constellation）、密谋（Connive）、崇高（Exalted）、金属工艺（Metalcraft）、突变（Mutate）、脱逃（Escape）、超载（Overload）、即兴（Improvise）、求学（Learn）、日限（Daybound）、夜限（Nightbound）

### 最终健康检查
- 运行修复后的 `lint_wiki_v2.py`：总页面数 167，孤立页面 2（index/log 为预期根页面），断链目标 0
- 更新 `index.md` 完整收录所有新增页面

## [2026-04-21] ingest | EDHREC 指挥官组合技数据库

将 `raw/EDHREC_Combos/` 目录下的 33 个 JSON 文件（~500 MB，49,646 个组合技）系统性地分析并整理进 Wiki：

### 数据分析成果
- 总组合技数：49,646（覆盖 33 个颜色身份分类）
- 涉及不同牌张：6,258 张
- 高频引擎牌（500+ 组合）：32 张
- 最热组合：Hullbreaker Horror + Sol Ring（300,846 套牌）
- 最热门效果类型：无限 ETB（30,068 次）、无限 LTB（25,956 次）

### 新增与更新页面
- **来源摘要页 1 篇**：[[sources/2026-04-21-edhrec-combos|EDHREC 指挥官组合技数据库]]
- **概念页更新 1 篇**：[[combo|组合技]] — 大幅扩充，加入 EDHREC 大数据洞察、引擎牌排名、经典组合案例
- **新增概念页 2 篇**：
  - [[combo-engine-cards|组合技引擎牌]] — 四大类引擎牌（牺牲/法术力/触发/生物）详解，含 Ashnod's Altar、Phyrexian Altar、Hullbreaker Horror、Basalt Monolith 等核心牌
  - [[infinite-mana-combos|无限法术力组合技]] — 五大类型（产费重置/牺牲召回/地落循环/风暴连锁/闪烁循环）及经典案例
- **更新 `index.md`** 收录新增页面
- **当前 Wiki 总计**：来源页 6 篇、实体页 4 篇、概念页 120 篇、综合页 2 篇

## [2026-04-21] ingest | 补充 EDH 指挥官赛制核心页面

系统性地补充了指挥官（EDH）赛制缺失的核心概念页面，使 Wiki 对指挥官赛制的覆盖更加完整。

### 新增概念页（10 篇）
- [[color-identity|颜色认同]] — 指挥官套牌构组最核心的颜色限制规则
- [[command-zone|统帅区]] — 指挥官的起始区域与替代性移动规则
- [[commander-damage|指挥官伤害]] — 21 点战斗伤害致胜规则及 Voltron 策略
- [[commander-tax|指挥官税]] — 反复施放指挥官的额外费用机制
- [[singleton|单例制]] — 100 张 singleton 规则详解
- [[legendary-creature|传奇生物]] — 可作为指挥官的牌张类型
- [[background|背景]] — Baldur's Gate 的背景机制
- [[edh-banned-list|EDH 禁牌表]] — 指挥官规则委员会的禁牌列表
- [[edh-social-contract|EDH 社交契约]] — 指挥官赛制的非正式玩家共识
- [[duel-commander|Duel Commander]] — 1v1 竞技指挥官变体

### 更新页面
- [[commander|指挥官]] — 添加与新页面的交叉引用

### 更新 `index.md`
- 当前 Wiki 总计：来源页 6 篇、实体页 4 篇、概念页 130 篇、综合页 2 篇

## [2026-04-21] update | 创建 Obsidian 导航页并修复 SKILL.md 路径

创建 `wiki/obsidian-nav.md` 作为 Obsidian 内的快速导航中心，汇总所有关键概念页、赛制页、规则页的 `[[wikilink]]` 链接。同时修复 `.claude/skills/mtg-wiki/SKILL.md` 中的路径错误，并在 SKILL.md 末尾添加 Obsidian URI 导航附录，支持从外部点击直接跳转到 Obsidian。

### 新增页面
- [[wiki/obsidian-nav|Obsidian 导航中心]] — output 类型，汇总 40+ 关键页面的可点击链接

### 更新页面
- `wiki/index.md` — 在「输出」分类下注册 Obsidian 导航中心
- `.claude/skills/mtg-wiki/SKILL.md` — 修复所有相对路径为绝对路径，添加 Obsidian URI 导航附录

## [2026-04-21] update | 修复 mtg-judge-zh skill 路径并迁移 references

将 mtg-judge-zh 的知识库根目录指向当前项目目录。复制 `~/.agents/skills/mtg-judge-zh/references/`（6 篇专题参考文档）到 `raw/references/`。修改 `.claude/skills/mtg-judge-zh/SKILL.md` 中的所有路径为项目内相对路径：
- `references/` → `raw/references/`
- `markdown/` → `raw/cr/`
- `mtr/` → `raw/mtr/`
- `ipg/` → `raw/ipg/`
- `wiki/concepts/` → `wiki/concepts/`
- 工具路径全部改为项目内相对路径

同时更新查证流程，优先推荐使用本地 `card_search.py` / `name_translator.py` 而非仅依赖 API，并添加中文牌名查证教训（"变境"= Scapeshift 案例）。

## [2026-04-22] ingest | 17lands 限制赛数据分析（TMT 系列）

通过 17lands API 获取 TMT 系列 Premier Draft 数据（210 张牌、数十万对局），系统分析限制赛中各稀有度的实际表现：

### 数据来源
- 原始数据：`raw/data/17lands_tmt_premier.json`（160KB，210 张卡牌记录）
- 分析脚本：`raw/data/analyze_17lands.py`

### 核心发现
- **各稀有度平均胜率**：Mythic (56.07%) > Uncommon (55.78%) > Rare (54.98%) ≈ Common (54.90%)
- **Rare 波动最大**（标准差 3.54%）：既有 61.4% 的顶级牌，也有 38.8% 的极低胜率牌
- **抽到改进率随稀有度递增**：Common +0.71pp → Mythic +6.16pp
- **陷阱牌识别**：高使用率但低胜率的 Rare/Mythic（如 Conqueror's Flail、Michelangelo, Improviser）

### 新增与更新页面
- **来源摘要页 1 篇**：[[2026-04-22-17lands-tmt|17lands TMT Premier Draft 数据]]
- **概念页更新 3 篇**：
  - [[limited|限制赛]] — 大幅扩充，加入稀有度胜率分布、陷阱牌分析、抽到改进率
  - [[rarity|稀有度]] — 加入限制赛实际表现数据，解释 Rare 平均胜率低于 Uncommon 的原因
  - [[draft|轮抽]] — 加入数据驱动的 5 大选牌教训（不要迷信稀有度、Uncommon 是甜蜜点、识别陷阱牌等）
- **更新 `index.md`** 收录新增来源页

### 当前 Wiki 总计
- 来源页 7 篇、实体页 4 篇、概念页 130 篇、综合页 2 篇

## [2026-04-22] ingest | 17lands TDM 系列数据（跨系列对比与数据质量分析）

尝试通过 17lands API 获取 TDM（Tarkir: Dragonstorm）系列 TradDraft 数据，发现 TradDraft 无有效数据。改用 PremierDraft 获取到部分数据，但覆盖率显著低于 TMT 系列：

### 数据覆盖情况
- **PremierDraft 数据**：`raw/data/17lands_tdm_premier.json`（170KB，281 张卡牌）
- **数据覆盖率**：Common 76%、Uncommon 69%、Rare 36%、Mythic 0%
- **TradDraft 数据**：完全无有效数据

### 核心发现
- **TDM 平均胜率整体偏高**（Common 56.67%、Uncommon 57.42%、Rare 58.24%），但 Rare 数据存在严重的幸存者偏差（仅 25/70 有数据）
- **跨系列共同模式验证**：Uncommon 是甜蜜点、Common 最稳定、抽到改进率随稀有度递增——在两个系列中均成立
- **「风味陷阱」识别**：TDM 中多张 Stormbrood（龙族主题）Uncommon 使用率极高但胜率低于平均线
- **数据质量教训**：低覆盖率的数据集会扭曲平均胜率，分析前必须检查样本量和覆盖率

### 新增与更新页面
- **来源摘要页 1 篇**：[[sources/2026-04-22-17lands-tdm|17lands TDM Premier Draft 数据]]
- **概念页更新 3 篇**：
  - [[limited|限制赛]] — 加入跨系列对比（TMT vs TDM）、数据覆盖率的重要性
  - [[draft|轮抽]] — 加入「风味陷阱」识别、数据质量检查方法
  - [[rarity|稀有度]] — 加入跨系列验证和幸存者偏差警告
- **更新 `index.md`** 收录新增来源页

### 当前 Wiki 总计
- 来源页 8 篇、实体页 4 篇、概念页 130 篇、综合页 2 篇

## [2026-04-22] lint | 全面健康检查与断链修复

运行 `lint_wiki_v2.py` 进行全面健康检查，发现并修复了多个结构性问题：

### 修复 lint 脚本
- **修复 `\|` 转义处理**：Obsidian 表格中的 `[[wiki/concepts/slug\|display]]` 格式被错误解析为 `slug\`（含反斜杠），修复后正确提取为 `slug`
- **修复 `wiki/` 前缀处理**：Obsidian 中以 vault 根路径链接（如 `wiki/concepts/xxx`）的格式，lint 脚本现在会去掉 `wiki/` 前缀再匹配 slug

### 修复断链
- **obsidian-nav.md**：修复 2 个错误路径，`wiki/concepts/mtg-official-documents` → `wiki/synthesis/mtg-official-documents`，`wiki/concepts/format-legality-analysis` → `wiki/synthesis/format-legality-analysis`

### 补充交叉引用（消除 1 入链孤立页）
在以下页面添加相关机制链接，将 15+ 个仅有 1 个入链的概念页提升至 2+ 个入链：
- [[creature|生物]] — 新增 legendary、monstrosity、disguise、channel
- [[enchantment|结界]] — 新增 constellation
- [[graveyard|坟场]] — 新增 escape
- [[land|地]] — 新增 snow
- [[transform|转化]] — 新增 daybound、nightbound
- [[keyword-abilities-overview|关键字异能总览]] — 新增 constellation、monstrosity、escape、snow、disguise、legendary、channel、daybound、connive、improvise、metalcraft、overload、shadow、kindred、battle、venture-into-the-dungeon、raid、exalted、mutate、bestow、enchant、learn、basic

### 最终状态
- 总页面数：203
- 断链目标：**0**
- 孤立页面：**2**（index、log 为预期根页面）
- 最低入链：**2**（无 1 入链页面）
- 入链最多：完整规则（154）、万智牌赛制（132）、关键字异能总览（85）

## [2026-04-22] ingest | 17lands ECL 系列数据（数据质量最高的限制赛分析）

通过 17lands API 获取 ECL 系列 TradDraft 数据（288 张牌），数据覆盖率为本 Wiki 分析的 17lands 数据集中最高：

### 数据覆盖情况
- **TradDraft 数据**：`raw/data/17lands_ecl_trad.json`（170KB，288 张卡牌）
- **数据覆盖率**：Common 98.8%、Uncommon 96.2%、Rare 76.9%、Mythic 87.5%
- **对比**：显著优于 TDM（Rare 36%、Mythic 0%）和 TMT（PremierDraft）

### 核心发现
- **正常稀有度梯度恢复**：Rare (59.81%) > Uncommon (58.86%) > Common (58.42%)，与 TMT 的「Uncommon > Rare」异常模式形成对比
- **整体胜率偏高**：所有稀有度平均胜率均高于 58%，显著高于 TMT 的 ~55%
- **Rare 标准差仅 2.01%**：远低于 TMT 的 3.54%，说明 ECL 的 Rare 牌强度更均匀
- **「构筑强牌 ≠ 限制赛强牌」**：Oko, Lorwyn Liege 在构筑赛中被禁，但在 ECL 限制赛中是秘稀陷阱（胜率 57.2%，低于平均线 59.8%）
- **三系列共同模式确认**：抽到改进率随稀有度严格递增、Common 最稳定、陷阱牌普遍存在

### 新增与更新页面
- **来源摘要页 1 篇**：[[sources/2026-04-22-17lands-ecl|17lands ECL TradDraft 数据]]
- **概念页更新 3 篇**：
  - [[limited|限制赛]] — 三系列综合对比（TMT vs TDM vs ECL），解释 Rare 胜率系列依赖性的原因
  - [[draft|轮抽]] — 加入「构筑强牌 ≠ 限制赛强牌」教训（Oko 案例）、TradDraft 数据质量优势
  - [[rarity|稀有度]] — 更新跨系列验证，ECL 证明 Rare 可以正常高于 Uncommon
- **更新 `index.md`** 收录新增来源页

### 当前 Wiki 总计
- 来源页 9 篇、实体页 4 篇、概念页 130 篇、综合页 2 篇

## [2026-04-22] synthesis | SOS（School of Spells）限制赛全面分析

基于 17lands API 获取的 SOS 完整卡牌列表（341 张）和三个已分析系列（TMT/TDM/ECL）的 17lands 数据模式，撰写 SOS 限制赛环境预测分析：

### SOS 系列特征
- **主题**：史崔海文（Strixhaven）魔法学校回归，五大 Mage College（Witherbloom BG、Quandrix UG、Prismari UR、Silverquill WB、Lorehold WR）
- **多色牌占比 24.3%**（83 张），Common 多色牌 15 张（每 College 3 张）——双色套牌是主流
- **生物仅占 42.8%**，非生物咒语占 48.4%——咒语密集环境
- **Wizard 子类型占生物 19.9%**——隐性的 tribal 配合维度

### 核心预测
1. **Prismari (UR) 和 Quandrix (UG) 预计最强 College**：蓝系 College 在限制赛中历史表现优异
2. **控制/节奏套牌可能比快攻更强**：咒语密集 + 低生物比例 = 慢节奏环境
3. **Rare 平均胜率预计 ~59%**：多色牌设计得当，构筑专用陷阱比例低于 TMT
4. **Mascot 系列和 Legendary 角色可能是陷阱牌**：风味驱动的过高估值

### 新增页面
- **综合页 1 篇**：[[sos-limited-analysis|SOS 限制赛全面分析]] — 包含系列组成分析、五大 College 强度排名、选牌策略建议、与 TMT/TDM/ECL 的跨系列对比
- **原始数据**：`raw/data/17lands_sos_premier.json`（341 张卡牌列表，尚无 draft 数据）
- **更新 `index.md`** 收录新增综合页

## [2026-04-22] ingest | cEDH 竞技指挥官知识体系构建

基于本地 mtg-edh-tutor 项目的 cEDH 知识，系统性地构建了竞技指挥官的完整知识框架：

### 新增概念页（4 篇）
- [[cedh-deck-archetypes|cEDH 套牌原型]] — 四大原型（Turbo / Stax / Midrange / Adaptive）的特征、优劣势对局、环境适配性
- [[cedh-combo-patterns|cEDH 组合技模式]] — Breach Combo、Oracle Combo、Ad Nauseam、等时权杖组合技、Kinnan 专属组合技，含组件、费用、优劣对比
- [[cedh-pod-dynamics|cEDH Pod 动态]] — 4 人 Pod 位置效应（1–4 号位）、政治博弈、原型在不同位置的表现、关键决策框架
- [[cedh-data-analysis|cEDH 数据分析方法]] — 三层数据架构（Topdeck.gg / edhtop16 / Moxfield Primers）、定量/定性分析方法、6 章标准报告结构

### 更新页面
- [[cedh|cEDH]] — 从基础概述扩展为完整的知识枢纽页，新增核心竞技维度、环境元游戏、常见误区，并建立与 4 个子专题的交叉引用

### 当前 Wiki 总计
- 来源页 9 篇、实体页 4 篇、概念页 134 篇、综合页 3 篇

## [2026-04-22] synthesis | Blue Farm（Kraum/Tymna）cEDH 套牌全面分析

基于 Tremnek、FreedomWaffle、Kazu 三篇 Moxfield Bracket 5 Primer 的原始数据，结合 cEDH 竞技指挥官知识框架，撰写了 Blue Farm 套牌的时间横向（2021–2026 历史演进）与 Meta 纵向（vs Turbo/Stax/Midrange/Adaptive Matchup）联合分析报告。

### 报告结构
- **第 1 章**：套牌基础信息（指挥官价值、4 条 Combo 路线、单卡分类、构筑逻辑）
- **第 2 章**：环境适配性（当前 Tier 分布、4 类 Matchup 分析、环境痛点应对）
- **第 3 章**：实战表现（锦标赛胜率 48.28%、全部对局 62.12%、制胜回合、重建成功率、常见失误）
- **第 4 章**：时间维度（Dockside 时代 → 禁牌冲击 → Midrange 主导 → Proactive 回归，含核心单卡生命周期表）
- **第 5 章**：结论与优化（强烈推荐评级、构筑建议、对局策略、位置策略、Mulligan 原则）
- **第 6 章**：附录（中英对照表、数据来源、术语注释）

### 核心发现
- Blue Farm 是当前 cEDH 环境中最全面的 Adaptive 套牌，无明显劣对局
- 2024 年 9 月禁牌后从 Dockside 爆发转向 Breach 核心 + 指挥官过牌
- 2025 年下半年至 2026 年初趋势：从反应性（Mindbreak Trap）转向主动性（Last Chance + Rograkh）
- 地牌数量从 27 张降至 25 张（Rograkh 免费 + Wan Shi Tong 过牌支持）

### 新增页面
- **综合页 1 篇**：[[blue-farm-analysis|Blue Farm 全面分析]]
- **更新 `index.md`** 收录新增综合页

### 当前 Wiki 总计
- 来源页 9 篇、实体页 4 篇、概念页 134 篇、综合页 4 篇

## [2026-04-23] synthesis | SOS 轮抽抉择分析

基于 Bilibili 万智牌官方账号发布的「抉择时刻」轮抽场景（第一抓振奋塑望师，分析传递来的13张牌中第二抓最优选择），撰写选牌策略分析。

### 核心结论
第二抓选择 **Snooping Page**，走银毫学院白黑连辞路线。理由：与第一抓异能配合、连辞密度需求、非普通生物价值高于普通去除、方向一致性优于 Bring to Light 的多色偏离。

### 新增页面
- **综合页 1 篇**：[[2026-04-23-sos-draft-p2p-choice|SOS 轮抽抉择分析]]
- **更新 `index.md`** 收录新增综合页

### 当前 Wiki 总计
- 来源页 9 篇、实体页 4 篇、概念页 134 篇、综合页 5 篇

## [2026-05-03] synthesis | Tameshi Belcher（无地蓝炮）完整重写

按 `wiki/_templates/deck-analysis.md` 模板（10 节 + 关联 + 检查清单）重写 Tameshi Belcher 分析。原版本仅 187 行、含多项卡文错误（Tameshi 费用、Hydroelectric Specimen 类型 / 文本、Sea Gate cmc）+ 漏写 Suppression Ray + matchup 胜率与实测数据矛盾，本次彻底返工。

### 重构原因（前置任务问题清单）
1. **结构不全**：缺 4 / 5 / 8 / 9 / 10 节；与同期合规版本 azorius-control（392 行）相距过远
2. **卡牌文本错误**：5 张关键牌（Tameshi、Hydroelectric Specimen、Sea Gate Restoration、Sink into Stupor、Suppression Ray）正反面文本与 Scryfall 不一致
3. **核心牌缺漏**：100% 出现 4x 的 Suppression Ray // Orderly Plaza（唯一稳定白源）完全未提
4. **Matchup 数据捏造**：旧报告 vs Boros "稍劣"、vs Affinity "均势"、vs Amulet "微优"——matchup_data_v2.json 实测分别为 67% / 10% / 17%，方向全反

### 修正后核心数据
- Meta 占比：**2.27%** Tier 3（来源 modern_meta_report 2026-05-01）
- 颜色身份：**蓝白（Azorius）**（旧版本误标"单蓝"）
- 实测胜率：Boros 67%（12 局）/ Affinity 10%（10 局）/ Jeskai Blink 67%（15 局）/ Amulet Titan 17%（6 局）/ Domain Aggro 50%（6 局）/ Ruby Storm 60%（5 局）等共 12 个对局
- 关键回合修正：旧"无干扰下 T3 lethal"改为"T3 仅 nut hand 成立，典型 kill T4-T5"

### 新增页面
- **综合页 1 篇**：[[branches/strategy/decks/tameshi-belcher|Tameshi Belcher（无地蓝炮）套牌分析]]（954 行）
- **更新 `index.md`** 收录至综合页栏

### 校对工具链
- Scryfall API（curl）核对 17 张核心牌 + 33 张关联牌正反面文本
- mtg-judge-zh agent 路径校对 7 条 CR 互动（CR 712.8a / 117.6 / 603.1 / 603.7 / 702.62a / 702.127a / 115.7）
- mtgch API 关联牌名待二次校对（第 10.4 节列出 33 张）

### 当前 Wiki 总计
- 来源页 9 篇、实体页 4 篇、概念页 134 篇、综合页 6 篇

