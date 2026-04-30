# Magic Skill — Magic: The Gathering General-Purpose Knowledge Infrastructure

This project is the **MTG General-Purpose Knowledge Infrastructure**, built and maintained by an LLM, serving multiple downstream consumers: judge rulings, strategy research, content creation, DIY card design, and more. Inspired by karpathy's llm-wiki, this Wiki acts as the core knowledge layer between raw sources (rule documents, card data, articles) and user questions.

## Project Structure

| Layer | Purpose | Content |
|-------|---------|---------|
| **Raw Data** (`raw/`) | Immutable source of truth | CR/MTR/IPG rule docs, 37,230 card records, EDH data |
| **General Knowledge Base** (`wiki/`) | Audience-agnostic | Concept pages, entity pages, source summaries, synthesis |
| **Branch-Specific Layer** (`wiki/branches/`) | Audience-specific | Judge decision trees, strategy frameworks, creation templates |
| **Agent/Skill** (`agent/`, `skill/`) | Collaborative configs | Judge agent definitions, skill workflows |
| **Generated Output** (`output/`) | Output artifacts | Weekly reports, registries, analysis reports |

## Quick Stats

| Metric | Count |
|--------|-------|
| Wiki Pages | **254** |
| Concept Pages | 190 |
| Judge Decision Trees | 31 |
| Analysis Frameworks | 4 |
| Common Traps | 2 |
| Source Summaries | 9 |
| Entity Pages | 4 |
| Synthesis Articles | 4 |
| Raw Data Files | 103 |

## Directory Structure

```
├── agent/                          # Agent definitions (collaborative, version-controlled)
│   └── mtg-judge-zh.md             # Judge agent: persona, workflow, compliance reports
├── skill/                          # Skill definitions (collaborative, version-controlled)
│   └── mtg-judge-zh/
│       └── SKILL.md                # Judge skill: trigger conditions, response flow
├── raw/                            # Raw data (immutable)
│   ├── cr/                         # Comprehensive Rules (CR chapters 1–9 + Glossary)
│   ├── ipg/                        # Infraction Procedure Guide
│   ├── mtr/                        # Magic Tournament Rules
│   ├── data/                       # Card data (37,230 Oracle cards)
│   ├── references/                 # Topic reference docs (索引 to be auto-generated)
│   ├── tools/                      # Python tools (card search, rule search, name translation)
│   └── assets/                     # Images and attachments
├── wiki/                           # LLM-generated and maintained knowledge base
│   ├── DESIGN.md                   # Wiki architecture design
│   ├── index.md                    # Master content index
│   ├── log.md                      # Operation log
│   ├── _templates/                 # Page templates
│   ├── sources/                    # Source summaries
│   ├── entities/                   # Entity pages: people, organizations, products
│   ├── concepts/                   # Concept pages: rules, mechanics, strategy terms
│   ├── synthesis/                  # Synthesis and analysis
│   └── branches/                   # Branch-specific layers
│       ├── referee/                # Referee branch (current focus)
│       │   ├── decision-trees/     # Judge decision trees (organized by mechanic/keyword)
│       │   ├── frameworks/         # Analysis frameworks (layer system, stack resolution, etc.)
│       │   ├── common-traps/       # Common pitfalls and misrulings
│       │   ├── mtr-ipg-guides/     # Tournament and infraction guides
│       │   └── test-questions/     # Practice question bank
│       ├── strategy/               # Strategy branch (reserved)
│       ├── creation/               # Creation branch (reserved)
│       └── diy/                    # DIY branch (reserved)
└── output/                         # Generated artifacts
    ├── cedh小屋周报/               # cEDH tournament weekly reports
    ├── card-generator/             # AI card design tool
    └── *.md                        # Other reports and analysis
```

## Coverage

### Rules and Mechanics
- **Comprehensive Rules (CR)** — All 9 chapters broken into concept pages with precise rule citations (e.g., CR 101.4, CR 613, CR 704.5)
- **Tournament Documents** — MTR and IPG broken into searchable concept pages
- **Keywords** — 16 evergreen keywords + 9 mechanics keywords
- **Core Systems** — The stack, layer system (613), priority, combat phase, state-based actions, replacement/prevention effects

### Judge Decision Support (`wiki/branches/referee/`)
- **Decision Tree Router** — Unified entry page with quick navigation by question type
- **Decision Trees** — 31 mandatory search paths by mechanic/keyword (Cascade, Flashback, replacement effects, copy effects, etc.)
- **Analysis Frameworks** — Layer system determination, stack resolution, ability type identification, replacement effect analysis
- **Compliance Reports** — Every agent response includes an execution compliance report, ensuring rule search depth

### Strategy and Formats
- Format pages: Standard, Pioneer, Modern, Legacy, Limited, Commander
- Strategy concepts: card advantage, mana curve, removal, counterspells, tutors, acceleration, combo
- Deck archetype overview

### Data and Analysis
- 37,230 unique Oracle cards extracted from 526,803 records
- Distribution index: color, mana cost, format, supertype, subtype, keyword, set (1,028 sets)

## Core Operations

This project is maintained by Claude Code together with the `mtg-judge-zh` agent. Three core operations drive knowledge base growth:

### 1. Ingest (Source Intake)
Place a source into `raw/` and tell the agent to process it. The agent reads the source, discusses key points, writes a summary in `wiki/sources/`, updates related concept/entity pages, and appends a log entry. A single source typically touches 10–15 wiki pages.

### 2. Query (Answer Questions)
Ask the Wiki a question. The agent reads `index.md` to locate relevant pages, synthesizes an answer with `[[citations]]`, and archives valuable responses to `wiki/synthesis/` or `output/`.

### 3. Lint (Health Check)
Periodically scan for contradictions, outdated claims, orphaned pages, broken links, and missing cross-references. A Python script (`raw/data/lint_wiki_v2.py`) validates that all internal WikiLinks resolve correctly.

## Page Standards

- All pages are Markdown with YAML frontmatter (`created`, `updated`, `type`, `tags`, `sources`)
- Internal links use `[[WikiLink]]` syntax (Obsidian-compatible)
- Filenames: lowercase, hyphenated (e.g., `comprehensive-rules.md`)
- Chinese filenames are allowed but must end in `.md`
- `type: decision-tree` is used for judge decision tree pages

## Tools and Scripts

| Script | Purpose |
|--------|---------|
| `raw/tools/mtg_wiki/card_search.py` | Card search (local 37K + mtgch API + Scryfall API) |
| `raw/tools/mtg_wiki/rule_search.py` | Rule search (by rule number or keyword) |
| `raw/tools/mtg_wiki/name_translator.py` | Card name translation (EN↔CN) |
| `raw/data/lint_wiki_v2.py` | Link health check, orphaned page scan, broken link detection |
| `raw/data/process_cards.py` | Streaming process 2.3 GB all-cards JSON |
| `raw/data/generate_keyword_pages.py` | Auto-generate concept pages from keyword corpus |
| `raw/data/generate_missing_pages.py` | Identify and scaffold missing wiki pages |

## Browsing the Wiki

Open the `wiki/` folder in [Obsidian](https://obsidian.md/) for the best experience:
- **Graph View** shows connections between concepts
- **WikiLinks** (`[[ ]]`) enable seamless navigation
- **Dataview** plugin queries YAML frontmatter to generate dynamic tables

## Agent Integration

The `mtg-judge-zh` agent (MTG Chinese Judge Assistant) uses this Wiki as one of its knowledge bases. When answering rules questions, it synthesizes queries from:
- Raw CR rule documents (`raw/cr/`)
- Compiled Wiki (`wiki/concepts/`, `wiki/synthesis/`)
- Judge decision trees (`wiki/branches/referee/decision-trees/`)

The agent's response flow includes **mandatory deep search** and **execution compliance reports**, ensuring rule citations are accurate and not based on memory.

## Why This Approach

Traditional RAG retrieves raw document fragments on every query. This Wiki **compiles knowledge once and keeps it updated**. Cross-references are already established, contradictions are flagged, and synthesis reflects everything read. The knowledge base grows richer with every source and every question — never lost to chat history.

## How to Collaborate

- **Architecture Lead** — agent/skill definitions, frameworks/, overall architectural evolution
- **Judge Community** — content contributions to decision-trees/, common-traps/, test-questions/
- **Tool Developers** — raw/tools/ optimization, auto-generated index scripts

See `TODO.md` for current backlog and priorities.

## LLM Wiki Pattern

This project follows the LLM Wiki pattern: a general-purpose approach for building persistent, compound-growth knowledge bases with LLM agents. The same structure applies to research, competitive analysis, reading notes, or any domain where knowledge accumulates over time.

---

## License

MIT License — see [LICENSE](LICENSE)

---

*Built with Claude Code + Obsidian. Wiki pages generated by LLM; raw data curated by humans.*
