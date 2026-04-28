# TODO List — 裁判 Agent 优化项目

## 高优先级（已完成）

- [x] **测试强制深度检索机制**
  - 15 道测试题全部重做，3 道错题修正（Q9 Harmonize、Q11 触发结构、Q12 Modal）
  - 强制深度检索流程验证通过

- [x] **补充决策树（decision-trees/）**
  - [x] Flashback（对比 Harmonize）
  - [x] Cascade / 倾曳
  - [x] Convoke / 召集
  - [x] X 咒语费用计算（CR 202.3e）
  - [x] 替代性效应（CR 614）
  - [x] 复制效应（CR 707）
  - [x] 介入性 If 子句（CR 603.4）
  - [x] Harmonize / 谐颂
  - [x] Modal 异能（CR 700.2）
  - [x] 触发式异能结构（CR 603.12）

- [x] **补充分析框架（frameworks/）**
  - [x] 堆叠推演框架（stack-resolution.md）
  - [x] 异能类型识别框架（ability-types.md）
  - [x] 替代/预防效应框架（replacement-effects.md）
  - [x] 层系统框架（layer-system.md）

## 中优先级（逐步推进）

- [x] **诊断并修复牌名检索问题**
  - `normalize_name()` 已修复，保留 CJK 字符
  - `local_exact()` 已添加空字符串保护
  - 中文查询跳过本地索引直接走 API

- [ ] **填充 MTR/IPG 指南（mtr-ipg-guides/）**
  - [ ] 沟通交流信息类别指南（MTR 4.1）
  - [ ] 处罚等级与升级指南（IPG 第1章）
  - [ ] 游戏行动失误（GPE）处理指南（IPG 第2章）
  - [ ] 比赛失误（TE）处理指南（IPG 第3章）
  - [ ] 举止违规处理指南（IPG 第4章）

- [ ] **填充测试题库（test-questions/）**
  - [ ] 整理已有的 15 道测试题（`raw/mtg_referee_test_202604.md`）
  - [ ] 按机制分类归档到 `test-questions/` 子目录
  - [ ] 标注每道题涉及的决策树，用于回归测试

- [ ] **填充常见陷阱（common-traps/）**
  - [ ] 关键字动作误解合集
  - [ ] 触发时机陷阱
  - [ ] Modal 选择时机陷阱
  - [ ] 层系统常见误判

## 低优先级（未来拓展）

- [ ] **自动生成规则索引（raw/references/ 重构方案 B）**
  - 用脚本解析 `raw/cr/` 生成按主题/关键字/规则编号组织的索引
  - 替代现有人工整理的 6 篇专题文档

- [ ] **规划其他分支目录**
  - [ ] `branches/strategy/` — 赛制元游戏、套牌分析框架
  - [ ] `branches/creation/` — 公众号创作辅助模板
  - [ ] `branches/diy/` — DIY 卡牌设计规范

- [ ] **裁判实战能力边界探索**
  - 询问技巧模板
  - 沟通话术模板
  - 升级决策树（什么情况下叫主裁）

## 协作入口

- **裁判社群** → 主要负责 `decision-trees/`、`common-traps/`、`test-questions/`
- **架构负责人** → 主要负责 agent/skill 定义、`frameworks/`、整体架构演进
- **工具开发者** → 主要负责 `raw/tools/` 优化、自动生成索引脚本
