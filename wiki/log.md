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


## [2026-06-17] governance | MTG skill 提交规范 v1.0 定稿
- 新增 `skill/CONTRIBUTING-mtg-skill.md`(MTG skill 提交规范+模板)
- 权威参照:opencode 官方 Agent Skills 规范 + mtg-wiki 正样板
- 经 3 轮多视角校验(官方规范/样板一致性/可用性)收敛,三视角全部 approve

## [2026-06-18] governance | MTG skill 体系架构 v1.0 定稿
- 新增 `skill/ARCHITECTURE-mtg-skills.md`(全量 MTG skill 体系架构:三层+路由约定)
- 自顶向下:盘点现状→设计分层→用架构倒逼出 cedh-breaker 规格(边界由架构定、内容由领域素材填)
- 经 3 轮多视角校验(架构合理性/opencode机制/cedh倒逼)+ opencode debug 实测,收敛 approve
- 关键实测:skills.paths 生效;modern-breaker 因缺 frontmatter 未加载(死 skill);opencode 无系统级 skill 优先级

## [2026-06-18] lint | 修复 cEDH 概念页 4 处硬伤（凭官方 Oracle 文本核实）
- cedh-combo-patterns.md：Kinnan 异能（编造→官方翻倍效应）、Hullbreaker 异能（编造→弹回手牌）、Kinnan 无限法术力 combo（3牌→2牌重写）、Breach 逃脱费用（表格修正）、Oracle 胜利条件（少于5张→X≥牌库数×2处）
- cedh.md / cedh-pod-dynamics.md：座位胜率数学修正（45/43/38
## [2026-06-18] lint | 修复 cEDH 概念页 4 处硬伤(凭官方 Oracle 文本核实)
- cedh-combo-patterns.md: Kinnan 异能(编造→官方翻倍效应)、Hullbreaker 异能(编造→弹回手牌)、Kinnan 无限法术力 combo(3牌→2牌重写)、Breach 逃脱费用(表格修正)、Oracle 胜利条件(少于5张→X>=牌库数, 2处)
- cedh.md / cedh-pod-dynamics.md: 座位胜率数学修正(45/43/38%%→27/25/22%%, 4人pod期望=25%%)
- 官方文本来源: card_search.py 查证 Kinnan/Breach/Oracle/Hullbreaker
- 新发现待修: cedh-combo-patterns.md:117 Ad Nauseam 异能描述疑似有误(后续处理)

## [2026-06-18] lint | 修复 cEDH 组合技页剩余牌张硬伤（凭 card_search 官方 Oracle 核实）

排查 cedh-combo-patterns.md 与 blue-farm-analysis.md 中 Oracle/Ad Nauseam/Isochron 章节，修复 4 类编造或失准的牌张描述：
1. Ad Nauseam（cedh-combo-patterns.md:117）：编造的「支付生命将手牌放入战场」→ 官方「展示牌库顶牌置入手中，失去等同总MV的生命，可重复任意次」（实为抓牌引擎，非放入战场）
2. Tainted Pact（同页表格+脆弱点；blue-farm:65）：编造的「放逐两张不同名地、放逐整库失去1/2生命」→ 官方「逐张放逐顶牌可选择不留手，直到留一张或放逐两张同名牌；无生命损失」；脆弱点改为「同名牌中断」
3. Demonic Consultation（同页表格+步骤；blue-farm:64）：补官方「先放逐顶6张再展示放逐」机制
4. Thassa's Oracle（同页表格+步骤；blue-farm:63）：胜利条件「检视数>库数/小于5」→ 官方「X(对蓝献忠)≥牌库张数」
验证：card_search.py 查证 7 张卡（Ad Nauseam/Thassa's Oracle/Demonic Consultation/Tainted Pact/Isochron Scepter/Dramatic Reversal/Angel's Grace/Phyrexian Unlife）；Grep 确认旧表述无残留。Isochron Scepter、Dramatic Reversal 原描述准确，未改。

## [2026-06-18] 落地 | 复活 modern-breaker + 建 cEDH 内容块骨架与模板

第1步（复活 modern-breaker）：给 skill/modern-breaker/SKILL.md 补合法 frontmatter（name: modern-breaker + description 含触发场景与让渡边界）。`opencode debug skill` 验证：modern-breaker 已出现在已加载列表（之前因缺 frontmatter 被过滤）。

第2步（cEDH 内容块骨架，依 skill/ARCHITECTURE-cedh-skill.md 第二/七节）：
- 建目录：wiki/branches/strategy/cedh/{decks,meta-snapshots,decision-trees,combos,card-evaluations}/（各含 .gitkeep）
- 建 5 个模板：wiki/branches/strategy/_templates/cedh-{deck,meta,decision-tree,combo,card-eval}.md，含契约 frontmatter（block/archetype/commander/as_of）+ 按类型正文骨架 + 查证/双语/时效约束提示。
- 均为**新增**，未触碰 wiki/concepts/ 通用层与 modern 现有目录（遵 P5/C7）。

未执行（破坏性，待治理流程）：HANDOFF §4 决策中"把 modern 迁到 branches/strategy/modern/ 统一子目录"影响 ~19 文件 + modern-breaker 引用路径，且该决策尚未并入 ARCHITECTURE-cedh-skill.md，故暂缓，待提案/校验后再做。

## [2026-06-18] 提案 | L2 公共能力层抽取（skill/_shared/mtg-common.md）提案收敛至 v0.3

按用户"提案先行→多轮校验→全 approve 收敛"工作方式，产出 skill/PROPOSAL-l2-shared.md（未实施，纯文档）：
- v0.1：显式 Read 引用方案（用户选定，不依赖 instructions 注入子 agent）。
- 第 1 轮校验（3 reviewer 并行：架构/P6、opencode 机制、规范/迁移）：全 approve-with-changes。并入 v0.2 的关键修正：① 主通路改为"主 agent 编排时 Read L2 并注入子 agent prompt"（子 agent 不会自读）；② 层系统/Schema 在 L2 只持指针、事实留 L1 概念页/schema json（P6）；③ judge SKILL.md Step 内联 JSON 示例属工作流产出契约，保留不删；④ 接入清单补 agent/mtg-judge-zh.md、agent/mtg-wiki.md；⑤ 工具清单补 mtgch_name_index.py（6 个）；⑥ 固化"先建 L2 后删段"迁移 gate + 逐行删除清单 + 端到端冒烟测试；⑦ 本轮删除 opencode.json instructions 步骤；⑧ 统一相对路径 ./ 基准项目根。
- 第 2 轮确认校验：机制 approve、规范/迁移 approve、架构 approve-with-changes（唯一项"schema 字段名清单仍是二源"）。v0.3 删除字段名清单 → 全部收敛。

前置实测受阻记录：opencode.json instructions 是否注入子 agent，在本会话内 `opencode run` 报 Session not found（嵌套调用不可行），docs 未载，无法实测；故方案选定不依赖该机制（显式 Read + 主 agent 注入）。

待用户放行后进入实施（建 mtg-common.md + 逐行删除清单 + 逐文件接入，属破坏性迁移，走 gate）。

## [2026-06-18] 提案 | cEDH 协作架构并入两决策 + 多轮校验至 v0.3（遗留 1 项待用户裁决）

按用户选项(b)：把 HANDOFF §4 的两个待定决策并入 skill/ARCHITECTURE-cedh-skill.md 并重新校验（未实施迁移，纯文档）。
- v0.2 并入：决策③赛制子目录统一（cedh 已建 cedh/ 子目录；modern 同步迁 modern/ 子目录，破坏性）+ 决策④ 5 类内容块定稿；新增第九节 modern 迁移治理（实测影响清单 + gate + 回退）。
- 第 1 轮校验（3 reviewer 并行：架构/宪法、迁移影响实测、cEDH 领域）→ 全 approve-with-changes。并入 v0.3 修正：
  ① type 字段不再一律 decision-tree，按块映射（deck/meta→synthesis、combo/card-eval→concept、决策树→decision-tree）；
  ② archetype 按 format 取枚举（cedh 域 Turbo/Stax/Midrange/Adaptive；modern 域 Aggro/Control/Combo/Midrange），新增 format 校验键；
  ③ combo 块外延放宽含 stax lock；commander 加 pair_type 消 // 歧义；as_of 粒度到日；
  ④ log.md 断链 lint 豁免固化（P7）；迁移影响订正 log.md 为 2 处（L40+L499）、补 decks 间裸 slug 互链说明、补孤儿 deck/撞名消歧；
  ⑤ gate 增 ②.5 补 frontmatter 步骤（archetype 属领域判断非机械）+ ⑦ P10 多视角评审记录；
  ⑥ 补"概念层 vs 块层"判据（概念=可复用模式无 as_of；块=具体实例带 as_of+sources），标注 concepts/cedh-deck-archetypes.md 时效数据越界为后续整改项。
- 同步对齐 step2 已建的 5 个模板 frontmatter（cedh-deck type 改 synthesis、全加 format、deck 加 pair_type、combo 加 lock_type+锁信息段、as_of 改到日）。

遗留唯一阻塞（8.1，需用户裁决，未擅改）：决策③ 与父文档 ARCHITECTURE-mtg-skills.md（v1.0 定稿）§5.1 第124行"cedh 与 modern 仅命名对称、不照搬结构/路径"直接冲突。选项 A=同步修订父文档（推荐）；选项 B=cedh 不迁 modern、放弃对称统一。用户拍板前第九节迁移不执行。

## [2026-06-18] 决策 | cEDH 架构 8.1 父文档冲突裁决：选 B（不迁 modern）→ 文档 v0.4

用户裁决 8.1：选 **B**——父文档 ARCHITECTURE-mtg-skills.md（v1.0 定稿）不动，cEDH 不迁移 modern。
- decision③ 的"对称迁移"部分撤回；仅保留"cEDH 用自己的 branches/strategy/cedh/ 子目录 + 5 类内容块约定"。
- modern 维持现状顶层目录，其引用路径/index.md/modern-breaker SKILL.md/agent/mtg-wiki.md 均不改。
- 结果：本文档与父文档 §5.1"cedh 与 modern 仅命名对称、不照搬结构/路径"重新自洽，无需改 v1.0 定稿。
- ARCHITECTURE-cedh-skill.md 更新至 v0.4：第九节 modern 迁移治理整体作废（保留实测数据备查）；§7 前置依赖删除"modern 迁子目录"条；§8 Q2 解为接受不对称、Q3 不适用；§5 archetype 校验简化为 format=cedh 单赛制（为未来 EDH 赛制预留 format 键）。
- 5 个 cedh 模板 frontmatter 维持 v0.3 对齐（type 映射/format/pair_type/lock_type/as_of 到日），与 v0.4 一致。

## [2026-06-18] 提案 | 6 项基础设施修复提案（R1-R6）收敛至 v0.2

按用户"全部提出修复提案"，针对全景盘点暴露的 6 隐患产出 skill/PROPOSAL-repairs.md（纯文档，未实施）：
- R1 删根级僵尸 SKILL.md（重复 mtg-wiki、含非法 triggers、实测未加载）
- R2 修正"37k 本地数据库"夸大（实测：源数据 raw/data/oracle-cards-lite.json 与索引均不存在，card_search 实为 API-only）
- R3 落地已收敛的 L2 提案（引用 v0.3，不另起）
- R4 宪法 v0.1→校验定稿（走 P12，逐条收口 5 个 OQ + 新增 P13 IP/版权）
- R5 modern 孤儿页(azorius-control/tameshi-belcher)入 index + affinity 裸链消歧
- R6 概念页越界（cedh-deck-archetypes 等无源时效数据）

第 1 轮校验（3 reviewer：架构/宪法、集成实测、领域数据）→ 全 approve-with-changes。并入 v0.2：
- R2 修正需改文件清单：补最强夸大源 agent/mtg-judge-zh.md:293/312/350（O(1)本地库）、tameshi-belcher.md:916（点名不存在的离线卡库）、agent/mtg-wiki.md:7（"不查网络"）；并区分"运行时能力夸大(改)"vs"构建期溯源统计(留：concepts数据概览/synthesis/sources/log)"。
- R4 覆盖宪法全部 5 个 OQ（含 OQ2 承诺扩展 lint_wiki_v2.py、OQ5 放置/命名结论）；P13 连锁要求全仓 P1-P12 引用同步更新纳入 gate。
- R5 类别改 P7（撞名属链接解析非二源）；实测两页数据不可直接填表（azorius 无 Tier/占比、tameshi 占比 2.27% vs 2.1% 自相矛盾且不在快照），须先正本清源。
- R6 核心改为"删/转定性为主，非盲迁"（无源数字迁 snapshot 仍无源）；锁单一权威方向（定义留 concepts、时效数据留 snapshot、互不重定义）；范围扩展普查 cedh-pod-dynamics/cedh-data-analysis 同类无源数字；与 §5.4 硬伤闸门协同；L25 Kinnan 标"需复核非确证"。

待用户放行后按 R5→R1→R6→R2→R4→R3 顺序逐项实施（各项独立 gate、可回退、记 log）。

## [2026-06-18] 回滚 | 撤回 cEDH 架构 + CONTRIBUTING 提交规范（改用 GitHub Fork+PR+CI 模型重做）

用户澄清社区提交模型为「所有人通过 GitHub Fork + PR 提交，CI 自动校验」（贡献者无需本地装 opencode 或跑脚本）。原 cEDH 协作架构与 CONTRIBUTING 假设「技术型贡献者本地跑 card_search.py / opencode debug / 校验脚本」，与之冲突，故回滚。
- 移除（均为未提交 untracked，已备份到 /var/folders/.../claudecode/rollback-2026-06-18/ 作回退预案，P11）：
  - skill/ARCHITECTURE-cedh-skill.md（v0.4）
  - skill/CONTRIBUTING-mtg-skill.md（v1.0）
- 保留：wiki/branches/strategy/cedh/ 目录骨架 + _templates/cedh-*.md 5 个模板（内容块 frontmatter 契约，与提交方式无关，正是未来 CI 校验对象，新设计复用）；硬伤修复、modern-breaker frontmatter、PROPOSAL-l2-shared.md、PROPOSAL-repairs.md 均保留。
- 遗留断引用待新设计处理：ARCHITECTURE-mtg-skills.md §六、PROPOSAL-repairs.md R4、PROPOSAL-cedh-breaker.md 中对 CONTRIBUTING 的引用。
- 待办：按 GitHub Fork+PR+CI 重做 cEDH 协作架构 + 贡献规范（CI Actions 跑 frontmatter/路径/Schema 校验，PR 模板，维护者评审合并）。

## [2026-06-18] 提案 | GitHub 社区贡献体系（Fork+PR+CI 强制查证）起草并并入第1轮评审 → v0.2

回滚后按用户「Fork+PR+CI 强制查证」重做，产出 skill/PROPOSAL-github-contribution.md（取代回滚的 ARCHITECTURE-cedh-skill + CONTRIBUTING）。
第1轮校验（3 reviewer：架构/宪法、CI/GitHub 机制、贡献者体验）→ 全 approve-with-changes。并入 v0.2 关键修正：
- 强制查证降为「硬前置依赖：离线索引就绪后才具备」，不预先宣称（避免重蹈病灶5/R2 名实不符）；与 R2 改为单向消费（数据入库+P13版权由 R2 决定，本提案不承接）。
- CI 机制补齐（reviewer 实测 GitHub Actions 坑）：① always-run gate 避免 paths+required check 死锁；② fork PR 权限模型（只读token/secrets不可用/cache隔离→default分支预热+miss回退/log隔离到合并后）；③ bulk 经 /bulk-data 拿 download_uri、cache key 用 updated_at；④ build_indices 加 ORACLE_CARDS_PATH env 覆盖；⑤ 格式校验是新写 lint 脚本非扩展 validation.py；⑥ 双面/拆分牌 // 特判。
- 译名库改用 Scryfall all-cards 过滤 lang=zhs 离线抽取（单一源可复现，弃 mtgch+人工单点）。
- 降门槛：Issue 表单转 PR（避免手写 YAML）；CI 逐张回填官方名+suggested change；cards_cited 可半填。
- cards_cited 定位为「派生索引非第二事实源」+ 正文⊆cards_cited 一致性 warning + 按块强制度（穷举/子集/豁免）。
- 查证分 error/warning（新牌 bulk 未收录走 warning+维护者放行 label）；PR 模板去重（只留人工信息）；P5 守卫改 allowlist；branch protection/CODEOWNERS；断引用三处+模板注释清理；交付物清单 8 项。
待确认轮校验。

## [2026-06-18] 提案 | GitHub 社区贡献体系 确认轮全 approve → 收敛 v0.3

确认轮 3 reviewer（架构/宪法、CI 机制、贡献者体验）对 v0.2 全部 **approve**，blocking 全闭合。v0.3 顺手收口 4 个非阻塞精度项：① 译名源只用 Scryfall all-cards（default-cards 过滤 zhs 几乎为空）；② 新牌放行 label 属维护者动作（fork 贡献者无 write 权限加不了）；③ 区分"无索引=查证 job 跳过/neutral"与"新牌=warning"；④ CN↔EN 抽取脚本本提案自建，数据入库/版权归 R2+P13 单向。
skill/PROPOSAL-github-contribution.md 已收敛 v0.3，待用户放行后按交付物清单（8 项：workflows/Issue表单/PR模板/CODEOWNERS/lint脚本/bulk抽取脚本+env补丁/新贡献规范/branch protection）实施。

## [2026-06-18] 提案 | GitHub 贡献体系 并入用户 4 项裁决 → v0.4

用户裁决 4 个开放问题，并入 skill/PROPOSAL-github-contribution.md v0.4：
- Q1 译名库：固定 raw/data/cn_name_index.json，维护者刷新（每新系列/至少每月），走 PR+评审。
- Q2 Issue→PR：采用现成 Action（已 webfetch 调研）——stefanbuck/github-issue-parser(v3,MIT 解析 Issue 表单成 JSON) + 胶水脚本渲染 frontmatter + peter-evans/create-pull-request(v8,MIT 开 PR)；关键集成约束：默认 GITHUB_TOKEN 建的 PR 不触发 on:pull_request 校验 CI，须用 PAT/App token（Issue 事件在 base 仓库、secrets 可用，可行）。
- Q3 治理空白：本提案补第九节——9.1 改/纠错已有块（纠错优先、刷新 updated/as_of）；9.2 行为准则 + 来源版权（sources 须公开可访问、禁整段复制、维护者人工审、联动 P13）；9.3 争议内容（Tier 定性优先、分歧并列呈现、git revert/disputed 降权回退）。
- Q4 all-cards bulk 体积：接受（actions/cache，default 分支预热，刷新周期宜短）。
交付物增至 9 项（+CODE_OF_CONDUCT.md）。待对新增材料做确认评审。

## [2026-06-18] 提案 | GitHub 贡献体系 确认评审(新材料）→ 收敛 v0.5

对 v0.4 新增材料（Q2 工具链 / Q3 治理）做确认评审（CI 集成 + 治理/宪法 2 reviewer）→ approve-with-changes，并入 v0.5：
- Q2 工具链安全硬化（CI reviewer）：① Issue 事件 + label 双重门控（on:issues + if contains label）；② 禁 run: 内联 ${{ issue.* }}（命令注入）经 env/文件传入；③ JSON→YAML 安全序列化（frontmatter 注入）；④ 文件名白名单防路径穿越；⑤ token 改 fine-grained GitHub App（弃宽权限 PAT）+ permissions 最小化；⑥ 确定性分支 issue-<number> 支持更新而非反复建 PR。"默认 GITHUB_TOKEN 建 PR 不触发校验 CI→须 App token"判断经核实正确。
- Q3 治理去悬空（治理 reviewer）：① 9.2 版权规则自包含、立即生效，P13 仅未来对齐（不引用尚不存在的条款，守 P1）；② 9.3 disputed 改为"块自身 frontmatter 标记 + SKILL.md 读标记降权"（不碰编排逻辑），定义谁打/解除；③ revert/disputed 记 log 归维护者级（与 4.2 fork PR 不写 log 对齐）；④ Q1 刷新逾期兜底引用 step6 warning、不阻塞存量 PR；⑤ 并列分歧条目各带 as_of+sources、纠错优先级判据（事实错>时效>风格）。
skill/PROPOSAL-github-contribution.md 收敛 v0.5，交付物 9 项，待用户放行实施。

## [2026-06-18] 落地 | 实施 CI 强制查证的依赖项（离线索引脚本 + env 覆盖）

按用户「先实施依赖项」，落地 GitHub 贡献体系 CI 强制查证所硬依赖的离线索引基础设施（不下载/提交多 GB bulk，只交付脚本 + 路径契约）：
- raw/tools/mtg_wiki/utils.py：ORACLE_CARDS_PATH/CN_NAME_INDEX_PATH/RAW_DATA_DIR 改为 env 可覆盖（MTG_ORACLE_CARDS_PATH / MTG_CN_NAME_INDEX_PATH / MTG_RAW_DATA_DIR），默认路径不变 → CI 可指向下载的 bulk 而不必伪造 lite 文件名。实测向后兼容：无 env 时 card_search.py 仍正常（走 API）。
- raw/tools/mtg_wiki/fetch_bulk.py（新）：经 /bulk-data 拿 type 对应 download_uri（非固定 URL）流式下载；--print-meta 输出 updated_at（供 actions/cache key）。实测 --print-meta 对 oracle_cards/all_cards 返回真实 uri+updated_at。
- raw/tools/mtg_wiki/build_cn_index.py（新）：从 Scryfall all_cards 过滤 lang==zhs 抽 name/printed_name/oracle_id 生成 cn_name_index.json（en_to_cn/cn_to_en/by_oracle_id），处理 card_faces（DFC/split 逐面 + "A // B" 合并），可选 ijson 流式应对 2.5GB。实测单面(Sol Ring 阳光戒)+DFC(Fire//Ice 火//冰)+跳过 en 全部正确。字段形状经 live Scryfall 核实。
- raw/data/.gitignore（新）：忽略 oracle-cards*/all-cards*/default-cards*/*-bulk-* 大文件，保留 cn_name_index.json（小、单一事实源、维护者刷新）。实测 gitignore 规则正确。
- build_indices.py 无需改解析逻辑（oracle_cards 是 lite 超集，全 card.get），仅靠 utils env 覆盖即可对接 CI bulk。实测 env 覆盖跑通生成 card_name_index。

实测约束：rulings(25MB) 真实下载因超 120s 工具超时未跑完（吞吐问题非脚本 bug，--print-meta 已证 download_uri 正确）；all_cards 2.5GB 仅 CI 缓存场景下载，本地不试。

待决（浮出，归 R2/P13，本次不决）：oracle-cards-lite.json 是否要生成并提交一份精简本地库（R2 方案 B）、Scryfall 数据入库与版权策略（宪法 P13 待 R4 定稿）。本次只交付生成工具，不做数据入库决策。

## [2026-06-18] 落地 | 实施 GitHub 社区贡献体系 CI 主体（v0.5 提案剩余交付物）

按用户「实施」，落地除 branch protection（仓库设置，非文件）外的全部交付物，并端到端实测：

模板（5 个）：补 cards_cited 字段（combo/card-eval 穷举、deck 子集、meta/decision-tree 豁免[]）；清理 cedh-deck.md 指向已回滚 ARCHITECTURE-cedh-skill 的注释。

工具脚本（raw/tools/mtg_wiki/，stdlib-only，CI 可直接跑）：
- lint_cedh_block.py：格式 gate——frontmatter 齐全/type↔block 映射/archetype 按 format 枚举/as_of 日期/目录命名/WikiLink 可解析/cards_cited 双语+穷举度/正文⊆cards_cited 一致性 warning。--changed BASE 取 PR 改动文件。实测：合法块 0 错；非法块（错 type/错 archetype/错日期/空 cards_cited）逐条 ERROR。
- verify_cards.py：强制查证 gate（离线）——commander+cards_cited 逐张查英文存在性 + 官方中文译名匹配；无索引=neutral skip exit0；新牌=warning。实测：正确块 exit0；错译名「塔萨的神谕≠官方塔萨的先知」→ ERROR exit1。
- render_cedh_issue.py：Issue 表单 JSON→规范 .md；安全硬化——值经 JSON 文件传入（非 shell 内联）、YAML 安全序列化（json.dumps）、slug 白名单防路径穿越。实测：slug 含 ../../ 被净化为 etcevil-oracle，产物过 lint 0 错。

.github/（8 文件）：
- workflows/cedh-block-validate.yml：on:pull_request 不加 paths（避免 required check 死锁）+ dorny/paths-filter 内部判断 + always-run gate；permissions: contents:read（fork 只读 token 足够，无 secret 依赖）；cache restore（key 用 bulk updated_at 日期）+ miss 时 fetch_bulk+build_indices 重建；lint+verify+P5 分层守卫（git diff 命中 concepts/entities/sources/synthesis 即 fail）。
- workflows/cache-warm-indices.yml：main 分支 schedule(每日)+manual 预热 oracle(176MB)与 CN(all_cards 2.5GB,ijson 流式)索引，供 fork PR 只读命中；用完删 bulk 不留存。
- workflows/cedh-issue-to-pr.yml：on:issues + label 双重门控；github-issue-parser→JSON 写文件→render→peter-evans/create-pull-request；用 secrets.CEDH_BOT_TOKEN（App token，非默认 GITHUB_TOKEN，否则 PR 不触发校验 CI）。
- ISSUE_TEMPLATE/cedh-block.yml（零 YAML 填表）、PULL_REQUEST_TEMPLATE.md（只留人工信息）、CODEOWNERS（维护者级路径占位 @MAINTAINER）、CODE_OF_CONDUCT.md、CONTRIBUTING.md（社区内容块贡献指南）。

YAML 全部 yaml.safe_load 通过。修断引用：ARCHITECTURE-mtg-skills.md §四/§六、PROPOSAL-repairs.md/PROPOSAL-l2-shared.md 的 CONTRIBUTING-mtg-skill 引用改为 .github/CONTRIBUTING.md（HANDOFF/log 历史记录不改，append-only）。

待维护者手动配置（无法用文件落地）：① branch protection（required checks=cedh-block-validate + required reviews）；② secrets.CEDH_BOT_TOKEN（fine-grained GitHub App token: contents:write+pull-requests:write）；③ CODEOWNERS 的 @MAINTAINER 换真实账号；④ 仓库设置允许 Actions 创建 PR（若改用 GITHUB_TOKEN 路径）。
git 干净无测试残留。

## [2026-06-18] 提案 | 法禁 EDH（Duel Commander）模块架构 起草 + 第1轮校验 → v0.2

确认"法禁 EDH"=Duel Commander 法式指挥官（1v1/20血/无指挥官伤害/独立法国禁牌表）。产出 skill/PROPOSAL-duel-commander.md，与 cedh 对称并列（非子集）。
用户决策：archetype 7 类(Aggro/Control/Midrange/Combo/Stax/Voltron/Tempo)；禁牌表单一事实源快照+维护者手动维护(duelcommander.com)+硬校验(用禁牌 ERROR)；skill=duel-commander-breaker；lint 泛化为 lint_strategy_block.py。

第1轮校验（架构/法禁领域/CI 集成 3 reviewer）→ 全 approve-with-changes。并入 v0.2：
- banlist 拆 banned（全面禁，比对 commander+cards_cited）+ banned_as_commander（仅禁作指挥官，只比对 commander）——法禁核心特征，原扁平单表会双向误判（领域+架构 reviewer 独立指出）。
- banned 列表放 frontmatter（非正文）→ 复用现有 parse_frontmatter 确定性解析。
- 撤回"verify_cards.py 不用改"：其 CEDH_DIR/changed_files 硬编码会让 dc 块 cards_cited 静默跳过（破 P2）；需把目录集合提为 STRATEGY_DIRS 共用。
- split_bilingual/normalize_name 抽到 utils.py，lint 与 verify 共用，禁牌比对按归一化 EN 面。
- 校验基准定为"块 banlist_as_of ≤ 之的最新快照"（非全局最新，避免新禁牌误杀旧块）。
- 泛化连带改动列为同 PR 原子项：cedh-block-validate.yml/CONTRIBUTING.md/docstring 引用改名 + shim；render_cedh_issue.py + cedh-issue-to-pr.yml 全 cedh 硬编码需参数化或开 dc 版；GitHub Issue Form dropdown 静态→cedh 4类 vs dc 7类 archetype 用两套表单。
- 概念页 duel-commander.md:51-66 既存禁牌表标"非权威，以快照为准"去 P6 二源；首份 banlist 设为 deck/meta 前置闸门；Voltron 标边缘原型；补 Tempo 判定准则 + 先后手/London mulligan 维度。
待确认轮校验后实施。

## [2026-06-18] 提案 | 法禁 banlist 改为自动抓取 → PROPOSAL-duel-commander v0.3

用户要求"验证禁牌表作为自动化脚本"。实测 duelcommander.com/banlist/：纯静态 HTML（115KB，非 JS 渲染），class 语义稳定——成功提取 88 张 class="ban-item banned"（全面禁→banned）+ 24 张 "ban-item banned commander-restricted"（仅禁指挥官→banned_as_commander），牌名清晰、分类准确，标准库可解析。可行性坐实（后续一次抓取因环境 SSL 抖动失败，非逻辑问题）。
用户决策：① 自动化级别=定时自动开 PR（GitHub Actions 周期跑 fetch_dc_banlist.py，有 diff 用 create-pull-request 自动开 PR，维护者 review+merge，不直推 main）；② 卫生检查+失败不覆盖（banned 数量<阈值/类名消失/数量突变>±50% → 报错退出不生成快照，不静默覆盖旧快照）。
并入 v0.3：§4.1 banlist 快照 banned 存 EN 名 + generated_by/source_hash 标记；新增 §4.3 自动化抓取小节（脚本+卫生检查+定时PR+安全）；§7 实施顺序加 fetch_dc_banlist.py + 定时 workflow。banlist 数据来源从 v0.2 的"维护者手动"改为"自动抓取+人工 merge 把关"。
待确认轮校验后实施。

## [2026-06-18] 提案 | 法禁 Duel Commander 确认轮 → 收敛 v0.4

确认轮 3 reviewer：① v0.2 的 9 项 blocking 逐条核验全闭环（approve）；② 自动抓取机制 approve-with-changes（7 项）；③ 泛化集成 approve-with-changes（3 项）。并入 v0.4：
泛化集成（reviewer3）：
- as_of 与 banlist_as_of 正交双字段——dc 的 deck/meta 两者都要（as_of=观测时效，banlist_as_of=禁牌表版本），不可顶替；之前 v0.3 误删了 dc 的 as_of。
- lint 日期校验循环 lint_cedh_block.py:147 (created/updated/as_of) 是漏网硬编码，须按 format 加 banlist_as_of 断言。
- ★workflow 不可裸改名：cedh-block-validate 是维护者手配的 branch protection required check，改名→旧 check 消失→所有 PR 永久 hang。定：保留文件名/job 名，仅 paths-filter 加 duel-commander/**。dc 开独立 render_dc_issue.py + dc-block 表单（add-paths: duel-commander/**, label dc-block）。
自动抓取（reviewer2）：
- YAML 注入：牌名含 '/,/// (Urza's Saga 等)，stdlib 无 PyYAML，用 json.dumps 安全序列化；删"无注入面"措辞。
- 卫生检查加固：两列表分别突变检测+归零即失败（防分类错位）；断言 HTTP200+Content-Type；canary 稳定禁牌断言（防200错误页）；删单张牌靠维护者 diff 兜底。
- source_hash=解析结果（排序牌名列表）哈希，非整页哈希；用于幂等不开重复 PR。
- App token CEDH_BOT_TOKEN（非 GITHUB_TOKEN，否则自动 PR 不触发校验）；固定分支 auto/dc-banlist 幂等更新；无递归（仅 schedule 触发）；失败通知（默认不通知定时任务）+ manual 手改快照兜底（lint 接受 generated_by=manual）。
- banlist_as_of 优先取官网生效日，回落抓取日。
v0.4 收敛，待用户放行实施（§7 七步）。

## [2026-07-08] 提案 | 法禁 Duel Commander v0.5 设计补充

修正 skill/PROPOSAL-duel-commander.md 内部遗留冲突：用户决策固化处的 banlist 来源从"维护者手动维护/不写抓取脚本"改为与 v0.3/v0.4 一致的"fetch_dc_banlist.py 自动抓取 + 定时自动开 PR + 维护者 review/merge"。

补齐此前偏薄的内容层设计：新增 duel-commander/index.md 导航与 strategy/wiki 索引回链要求；补来源分层、各 dc 内容块模板必备章节、首批种子内容闸门、duel-commander-breaker 输出契约、lint/verify/禁牌/导航/cedh 回归验收矩阵。实施顺序从 7 步扩展为 8 步，加入 index、种子内容和验收检查，避免模块只落 CI/banlist 而缺少可消费知识层。

## [2026-07-08] 提案 | 法禁 Duel Commander v0.6 规则版本与实战补充

追查 Bo1/55 分钟来源：来自既有 `wiki/concepts/duel-commander.md` 的赛制结构段落,后被 `skill/PROPOSAL-duel-commander.md` 固化到用户决策中。根据 Duel Commander 官方综合规则,修正为"默认 BO3/50 分钟,主办方可在赛前公告覆盖"；同时更新概念页,将禁牌表示例标注为非权威,以官方 B&R 与后续 banlist 快照为准。

提案推进到 v0.6：新增规则版本与来源优先级、`rules/` 快照层、source-registry、按 `effective_date <= as_of` 选择新旧规则的算法；补法禁合法性校验矩阵（commander、banned、banned_as_commander、companion、sideboard/outside-the-game、结构性禁用等）；补高手向实战内容路线图（起手调度、指挥官依赖度、局间换将、20 血资源账本、节奏基准、互动配置、对局矩阵、meta 可信度）。

## [2026-07-08] 提案 | 法禁 Duel Commander v0.7 牌名简称消歧

新增失败模式：用户问"2099"时,牌库/搜索可能返回多张候选牌；AI 若直接采用数据库第一个命中,会选到法禁语境下完全不使用的牌,而不是法禁 meta 中高占比的候选。实测本地 `name_translator.py "2099"` 失败,`card_search.py "2099"` 可返回 `Spider-Man 2099, Miguel O'Hara`,但这只是当前工具排序结果,不能作为稳定策略。

提案补 v0.7：将短名/数字/绰号/部分牌名定义为实体解析问题,不是普通语义理解问题。新增候选发现、法禁语境重排、低置信追问、别名表、以及 `duel-commander-breaker/SKILL.md` 必须写入的牌名消歧规则。核心要求：不得直接采用 `card_search.py` 第一结果；必须按法禁合法性、commander 可能性、dc 内容块/meta 出现率、别名来源与置信度重排,低置信时先追问。

补充压力测试：`spider99` → Spider token、`phelia` → Aphelia、`tivit` → End the Festivities/喜庆终结、`kess` → Kessig Wolf Run、`niv` → University Campus/洁尸客、`squee/slimefoot` 在单名与组合 commander 间摇摆。结论：现有 `card_search.py` 是查单卡详情工具,不是实体解析器；提案新增 `card_resolve.py` 设计,用 alias、法禁内容块/meta 命中、commander 可能性、合法性、banlist、字符串相似度分层评分,再调用 `card_search.py` 补全候选详情。

## [2026-07-08] 架构 | 全局 MTG 牌名实体解析层上提到 L2

确认简称/绰号/半截牌名误解析不是法禁独有,而是全 MTG skill 体系共性问题：cEDH 有 `blue farm` / `rogsi` / `tnt` / `thoracle` / `breach` 等套牌、组合技、单卡混合简称；摩登有 `frog` / `energy` / `belcher` / `amulet` 等 archetype 与单卡冲突；裁判问答中歧义牌名会导致错误规则结论。

更新 `skill/ARCHITECTURE-mtg-skills.md` 到 v1.1：在 L2 公共能力层新增全局牌名实体解析层,明确 `card_search.py` 是单卡详情查询器,不是实体解析器；新增 `card_resolve.py`/`card_search.py --candidates` 契约,所有 L3 skill 共享候选列表、置信度、语境重排、低置信追问机制。

更新 `skill/PROPOSAL-l2-shared.md` 到 v0.4：工具契约从 6 个扩展为 7 个,加入 `card_resolve.py`;新增全局实体解析契约,由 L2 定算法,由 L3 仅提供 `--format` 与 `--intent` 权重(cEDH/法禁/摩登/裁判各自语境)。硬规则：不得把数据库/API 第一结果当作用户意图；自动解析必须说明"我将 X 解析为 Y"；低置信必须追问。

## [2026-07-08] 落地 | 实现 card_resolve.py 牌名实体解析器

新增 `raw/tools/mtg_wiki/card_resolve.py`：区别于 `card_search.py` 的单卡详情查询,该脚本返回候选列表、score、reasons、warnings、components、selected、needs_clarification。支持 `--format judge|cedh|duel-commander|modern` 与 `--intent`；内置首批 alias（2099/spider99/phelia/kess/niv、blue farm/rogsi/tnt/thoracle/breach/LED、frog/energy/belcher/amulet 等）；读取 wiki 语境命中；必要时可调用 mtgch/Scryfall 扩展候选；支持 `--no-api` 供 CI/回归测试离线跑。

新增 `tests/validation/test_card_resolve.py`：覆盖法禁简称避免 bad fuzzy、cEDH deck/combo 简称、Modern archetype 简称、裁判多组件互动（oracle consultation、breach LED）。验证通过：`python3 tests/validation/test_card_resolve.py`（4 tests OK）与 `python3 -m py_compile raw/tools/mtg_wiki/card_resolve.py tests/validation/test_card_resolve.py`。

## [2026-07-08] 落地 | active skills/agents 接入 card_resolve.py

将实体解析契约从提案层落到会被实际加载的 skill/agent 文档：更新 `skill/mtg-wiki/SKILL.md`、`skill/mtg-wiki/SKILL_EN.md`、`skill/mtg-judge-zh/SKILL.md`、`skill/modern-breaker/SKILL.md`、`agent/card-lookup.md`、`agent/mtg-wiki.md`、`agent/mtg-judge-zh.md`。短名、数字、俗称、半截名、套牌简称、组合技简称、多版本角色名必须先调用 `card_resolve.py`;若 `needs_clarification=true` 先追问;解析到 card 后再用 `card_search.py` 查 Oracle;解析到 deck/archetype/combo 后先读对应 wiki 内容。

验证：`rg` 确认 active 文档均出现 `card_resolve.py`/`needs_clarification` 约束；`python3 tests/validation/test_card_resolve.py` 通过；`python3 -m py_compile raw/tools/mtg_wiki/card_resolve.py tests/validation/test_card_resolve.py` 通过；手动冒烟 `2099`/`blue farm`/`breach LED`/`frog` 均解析到预期实体或组件。

## [2026-07-08] 落地 | 法禁 Duel Commander 知识层与 skill 种子

继续补充法禁模块,将 `skill/PROPOSAL-duel-commander.md` 推进到 v0.8:新增 `wiki/branches/strategy/duel-commander/` 目录骨架、分支入口 `index.md`、`aliases.md`、`rules/source-registry.md`、最小 meta seed、Kess/Niv 两个 deck stub、6 个 dc 模板(`dc-deck`/`dc-meta`/`dc-decision-tree`/`dc-combo`/`dc-card-eval`/`dc-banlist`)与 `skill/duel-commander-breaker/SKILL.md`。

同步 `wiki/branches/strategy/index.md` 与 `wiki/index.md` 入口,让法禁策略层可被发现。种子内容明确标注资料不足,不得生成 Tier/占比/胜率;专用 skill 要求回答带 `as_of`、`banlist_as_of`、`rules_as_of`,并优先用 `card_resolve.py --format duel-commander` 处理简称/歧义。

本轮只落知识层与 skill 层;`lint_strategy_block.py`/`verify_cards.py` 泛化、`fetch_dc_banlist.py`、自动 PR workflow、dc issue 表单与首份真实 banlist 快照仍为后续实施项。验证通过:`python3 tests/validation/test_card_resolve.py` 与 `python3 -m py_compile raw/tools/mtg_wiki/card_resolve.py tests/validation/test_card_resolve.py`。

## [2026-07-08] 落地 | 法禁 skill 大型赛事备战能力补充

按“长期参加大型法禁赛事的牌手”视角审查 `duel-commander-breaker`:原 skill 能读法禁资料与处理简称,但缺少真实备赛会反复追问的关键项——牌表审计、赛事日期/banlist/rules/event policy 确认、前三回合计划、地基与曲线审计、flex slots、已知对手准备、时钟/平局风险、缺少快照时不得确认合法性的红线。

更新 `skill/duel-commander-breaker/SKILL.md`:新增大型赛事备战触发、冠军赛压力测试 12 问、缺失信息/风险/下一轮测试题输出要求,并要求 flex slots、known-opponent prep、clock management、threat/answer alignment 等维度。更新 `wiki/branches/strategy/_templates/dc-deck.md`:新增牌表审计、赛事政策、先后手 T1/T2/T3、地基与曲线、Flex Slots、时钟计划。新增 `wiki/branches/strategy/duel-commander/decision-trees/tournament-prep-checklist.md`,并接入法禁 index 与 strategy index。提案推进到 v0.9。

验证通过:`rg` 确认大型赛事/牌表审计/flex/时钟等关键约束落入 skill、模板、决策树与提案;`python3 tests/validation/test_card_resolve.py`;`python3 -m py_compile raw/tools/mtg_wiki/card_resolve.py tests/validation/test_card_resolve.py`。
