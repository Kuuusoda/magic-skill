# Hermes Agent 适配

本目录包含 [Hermes Agent](https://hermes-agent.nousresearch.com) 平台的 `mtg-wiki` skill 定义，复用本项目的 Wiki 知识库和 Python 工具链。

## 文件说明

```
contrib/hermes/
├── README.md          # 本文件
└── mtg-wiki.md        # Hermes skill 定义（可直接放入 ~/.hermes/skills/gaming/mtg-wiki/SKILL.md）
```

## 与上游 skill 的区别

| | 上游 `skill/mtg-wiki/` | 本适配 `contrib/hermes/` |
|---|---|---|
| 目标平台 | Claude Code / OpenClaw | Hermes Agent |
| 执行模式 | Agent pipeline（subagent） | LLM 顺序执行 pipeline |
| 校验方式 | validation.py | validation.py（相同，硬校验） |
| Fast Path | ✅ | ✅ |
| Pipeline 阶段 | Decompose → Parallel Lookup → Analyze → Verdict | 同（适配 Hermes 工具调用模式） |

## 安装

```bash
# 1. 克隆本项目
git clone https://github.com/<your-fork>/magic-skill.git ~/magic-skill

# 2. 安装 skill 到 Hermes
cp contrib/hermes/mtg-wiki.md ~/.hermes/skills/gaming/mtg-wiki/SKILL.md

# 3. 在 Hermes 中触发
#    自动触发：输入"万智牌"、"查牌"、"规则问题"等关键词
#    手动触发：/mtg-wiki
```

## 依赖

- Python 3（标准库即可，validation.py 无外部依赖）
- 本项目 `raw/tools/mtg_wiki/` 下的工具脚本
- 本项目 `wiki/` 和 `raw/cr/` 下的知识库数据
