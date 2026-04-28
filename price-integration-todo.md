# 卡牌价格数据接入 TODO

## 背景

当前 Wiki 已覆盖规则、机制、策略、限制赛数据（17lands），但缺少**卡牌价格**维度。接入价格数据后，可以实现：
- 查询单卡的实时/历史价格
- 套牌造价估算
- 价格趋势分析（哪些牌在涨/跌）
- 性价比筛选（限制赛中低价高效的牌）

---

## Phase 1：数据源调研与选择

### 1.1 国际数据源评估

| 平台 | 优势 | 劣势 | API 可用性 |
|------|------|------|-----------|
| **Scryfall** | 已有接入，含 USD/EUR 价格 | 价格更新有延迟（非实时）| 已有 API，免费 |
| **TCGPlayer** | 美国最大平台，价格最准 | 需要 API Key，国内访问慢 | 需申请 |
| **Card Kingdom** | 价格稳定，质量分级 | 无公开 API | 需爬虫 |
| **MTGGoldfish** | 历史价格、套牌造价 | 无公开 API | 需爬虫 |

### 1.2 国内数据源评估

| 平台 | 优势 | 劣势 | 接入方式 |
|------|------|------|---------|
| **MTGSO** | 国内主流，中文 | 价格可能偏区域化 | 未知 API，需调研 |
| **旅法师营地** | 中文社区，有价格板块 | 数据不一定结构化 | 需调研 |
| **淘宝/闲鱼** | 真实成交价 | 反爬虫严格 | 极难接入 |

### 1.3 建议优先级

1. **Scryfall（已有）** — 零成本扩展，先接入 USD 价格
2. **TCGPlayer** — 如果需要更准的美国市场价格
3. **国内数据源** — 如果需要人民币价格（后续可选）

---

## Phase 2：数据模型设计

### 2.1 需要存储的价格字段

```json
{
  "oracle_id": "uuid",
  "card_name": "Lightning Bolt",
  "set_code": "2X2",
  "set_name": "Double Masters 2022",
  "rarity": "common",
  "prices": {
    "usd": 2.50,
    "usd_foil": 5.00,
    "eur": 2.30,
    "tix": 0.05
  },
  "price_history": [
    {"date": "2026-04-01", "usd": 2.30},
    {"date": "2026-04-15", "usd": 2.50}
  ],
  "last_updated": "2026-04-22T10:00:00Z",
  "source": "scryfall"
}
```

### 2.2 文件存储方案

- `raw/data/prices/` — 按系列分目录存储 JSON
- `raw/data/prices/card-price-index.json` — 按 oracle_id 索引的最新价格
- `raw/data/prices/price-history/` — 历史价格时间序列

---

## Phase 3：工具脚本开发

### 3.1 Scryfall 价格抓取脚本

`raw/tools/mtg_wiki/fetch_prices.py`

功能：
- 从 Scryfall API 批量获取价格（`/cards/search?q=e:SET`）
- 增量更新（只抓自上次更新后有变化的牌）
- 保存到 `raw/data/prices/`

输入：`--set DSK`（系列代码）
输出：`raw/data/prices/dsk-prices.json`

### 3.2 价格查询脚本

`raw/tools/mtg_wiki/price_search.py`

功能：
- 按牌名查询当前价格
- 支持中英文模糊搜索
- 显示价格趋势（涨/跌箭头）

```bash
python3 raw/tools/mtg_wiki/price_search.py "Lightning Bolt"
python3 raw/tools/mtg_wiki/price_search.py "闪电击"
```

### 3.3 套牌造价估算

`raw/tools/mtg_wiki/deck_price.py`

功能：
- 读取牌表（MTGO/MTGA 格式）
- 估算总价和按稀有度分解
- 标记最贵的几张牌

```bash
python3 raw/tools/mtg_wiki/deck_price.py decklist.txt
```

---

## Phase 4：Wiki 页面整合

### 4.1 新增概念页

- **[[card-prices|卡牌价格体系]]** — 介绍各大交易平台、价格影响因素（稀有度、赛制需求、重印等）
- **[[mtg-finance|万智牌金融]]** — 价格波动的原因、投资/投机 vs 收藏
- **[[budget-decks|预算套牌]]** — 如何用低价牌组出竞技套牌

### 4.2 更新现有页面

- **[[rarity|稀有度]]** — 加入「稀有度与价格的关系」
- **[[limited|限制赛]]** — 加入「限制赛 vs 构筑赛的价格差异」
- **[[booster-pack|补充包]]** — 加入「期望价值（EV）计算」
- **[[set|系列]]** — 加入「系列价格概况」

### 4.3 卡牌查询增强

在 `card_search.py` 的输出中加入价格字段：
```
价格: USD $2.50 | EUR €2.30
```

---

## Phase 5：自动化与维护

### 5.1 定时更新

- 每周运行一次 `fetch_prices.py` 更新全系列价格
- 保存历史数据用于趋势分析

### 5.2 价格预警（可选）

- 标记价格异常波动（7 天内涨跌 >30%）
- 可能原因：禁牌表公布、新系列发售、重印消息

---

## 待决策问题

1. **是否接入人民币价格？** — 需要调研国内平台 API
2. **历史价格存储多久？** — 建议保留最近 2 年
3. **是否接入 TCGPlayer？** — 需要 API Key，国内访问有网络问题
4. **价格数据是否进 git？** — 建议只保留索引，原始价格数据用 `.gitignore` 排除（类似 oracle-cards-lite.json）

---

*创建日期：2026-04-22*
