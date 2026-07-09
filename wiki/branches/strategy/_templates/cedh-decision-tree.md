---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: decision-tree
block: cedh-decision-tree
format: cedh
status: <seed|stub|draft|verified|deprecated>
tags: [cEDH, 决策树, <主题>]
commander: ""                               # 通用决策树留空；套牌专属则填
archetype: ""                               # 适用原型，可留空表示通用
sources: [<经验来源/讨论链接>]
as_of: YYYY-MM-DD
cards_cited: []                            # 决策树通常不点名具体牌；如点名则列出（双语）供 CI 查证
---

# <决策主题>（如：pod 位置评估 / 政治威胁排序 / 何时 combo off）

> 适用场景：<什么时候用这棵树>

## 决策树

```
<根节点：要判断的问题>
├── 条件 A 成立？
│   ├── 是 → <动作/下一节点>
│   └── 否 → <动作/下一节点>
└── 条件 B 成立？
    ├── 是 → <动作>
    └── 否 → <动作>
```

## 节点说明
- **<节点>**：<判断依据、阈值、为什么>
- **<节点>**：……

## 常见误区
- ……

---
*决策依据应可追溯到机制或实战经验，不臆断；涉及规则判定让渡 mtg-judge-zh。*
