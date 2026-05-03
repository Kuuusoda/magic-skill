## OpenClaw 技能规范

### 技能目录结构

每个技能是一个文件夹，包含 **SKILL.md**（必需）和可选的打包资源：

```
skill-name/
├── SKILL.md (必需)
│   ├── YAML frontmatter：name + description（触发机制）
│   └── Markdown 正文：指令和指导
├── scripts/      - 可执行脚本（Python/Bash等）
├── references/   - 参考文档（按需加载）
└── assets/       - 静态资源（模板、图片等）
```

**SKILL.md 格式：**
```markdown
---
name: skill_name
description: 技能描述（这是主要的触发机制）
metadata:
  openclaw:
    requires:
      bins: ["uv"]           # 必需的二进制的PATH
      env: ["API_KEY"]       # 必需的环境变量
      config: ["browser.enabled"]  # 必需的配置文件路径
    os: ["darwin"]           # 仅在特定平台生效
---
# 技能说明（仅在触发后加载）
```

### 技能加载与优先级

OpenClaw 从多个来源加载技能，优先级从高到低：

```
<workspace>/skills/           最高（workspace专属）
~/.agents/skills/             其次（个人级）
~/.openclaw/skills/           再次（机器共享）
<捆绑的skills>               更低
skills.load.extraDirs/        最低（额外目录）
```

**调用层处理逻辑：**
1. Session 启动时扫描所有技能目录，建立技能列表快照
2. 根据 `metadata.openclaw` 进行**加载时过滤**（OS、bins、env、config）
3. 构建系统提示词时，将技能元数据注入 prompt（`<name>` + `<description>` + `<location>`）
4. 模型根据 `description` 自主判断触发哪个技能（description 就是触发器）
5. 技能命中后，SKILL.md 正文才被加载进上下文

### Token 消耗公式

```
总开销 = 195 + Σ(97 + len(name) + len(description) + len(location))
```
约 **97 chars ≈ 24 tokens** 每技能（不含实际字段长度）。

### 分层加载（Progressive Disclosure）

- **元数据层**：始终在 context（~100 words）
- **SKILL.md 正文**：技能触发后加载（<5k words）
- **references/ 文件**：按需显式读取，不进 context

### 技能分发

- `.skill` 文件 = zip 压缩包，可通过 ClawHub 分发
- `openclaw skills install <slug>` 安装到 workspace
- 技能也可内置在插件中（`openclaw.plugin.json` 声明 `skills` 目录）

---

总结：**description 就是触发器**，模型根据描述自主判断何时使用；过滤在加载时完成；正文只在技能命中后才加载，避免污染 context。
