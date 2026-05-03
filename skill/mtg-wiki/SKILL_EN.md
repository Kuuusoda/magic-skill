---
name: mtg-wiki
description: MTG general-purpose knowledge assistant. Handles MTG rules questions, card lookups (EN/CN), card interaction analysis, format/strategy explanation, and lore. Triggered when users ask about MTG (card names, rule concepts, formats, strategies, lore) or invoke /mtg-wiki.
metadata:
  openclaw:
    requires:
      bins: ["python3"]
      env: []
    os: ["darwin", "linux"]
---

# MTG General-Purpose Knowledge Assistant (MTG Wiki)

[**English**](https://raw.githubusercontent.com/RaymondYHH/mtg-skill/main/skill/mtg-wiki/SKILL_EN.md) | [**中文**](https://raw.githubusercontent.com/RaymondYHH/mtg-skill/main/skill/mtg-wiki/SKILL.md)

## Purpose

Encyclopedic MTG assistant covering **rules, cards, formats, strategy, and lore** in five dimensions. Core advantage is the local knowledge base — 187 wiki pages, 37,230-card Oracle database, and complete bilingual CR/MTR/IPG rule documents.

## Knowledge Base Structure

| Directory | Content |
|-----------|---------|
| `wiki/concepts/` | Concept pages: rules, mechanics, strategy (~174 pages) |
| `wiki/entities/` | Entity pages: people, organizations, products |
| `wiki/sources/` | Source summary pages |
| `wiki/synthesis/` | Synthesis and analysis |
| `raw/cr/` | Complete Comprehensive Rules (bilingual) |
| `raw/mtr/` | Magic Tournament Rules |
| `raw/ipg/` | Infraction Procedure Guide |

## Core Capabilities

### 1. Rule Lookup (CR/MTR/IPG)

Trigger: User asks about "first strike + deathtouch interaction", "stack resolution order", "layer system"

Flow:
1. Read relevant concept pages in `wiki/concepts/`
2. If precise rule text is needed, use `rule_search.py` to search local rule index, then read original `raw/cr/` text
3. Cite precise rule numbers (e.g., CR 510.4, CR 613.6)

Key Rule Reference:
- Layer system: CR 613 (copy → control → text → type → color → abilities → P/T)
- APNAP: CR 101.4 (active player decides first)
- Stack: CR 405 (LIFO)
- State-based actions: CR 704 (execute automatically, do not use stack)

### 2. Card Lookup (EN/CN fuzzy search)

Trigger: User mentions a specific card name (EN, CN, fuzzy input, or nickname)

Flow:
1. Call `card_search.py` for unified search
2. Return bilingual card info (name, cost, type, rules text, format legality)

Card name format standard:
- First occurrence: `Chinese Name (English Name)`
- Subsequent references: `Chinese Name`

### 3. Card Interaction Analysis

Trigger: User describes multi-card scenarios ("what happens if...?")

Typical analysis framework:
- Layer system determination: first determine which layer each effect belongs to → check for cross-layer (613.6) or dependency (613.8)
- Stack resolution: APNAP order onto stack → LIFO resolution
- Zone determination: distinguish "permanents" (battlefield only) vs "spells" (stack only)

### 4. Strategy and Format Analysis

Trigger: User discusses deck archetypes, format selection, banned/restricted lists

Format pages: `standard.md` / `pioneer.md` / `modern.md` / `legacy.md` / `vintage.md`
Commander: `commander.md` / `cedh.md`

### 5. Article Translation

When user translates MTG deck guides or strategy articles:
1. Extract card names and look up official Chinese translations with `name_translator.py`
2. Standardize terminology
3. Generate Markdown document with card name对照表 and terminology对照表

## Tool Usage

```bash
# Card search (EN/CN fuzzy search supported)
python3 ./raw/tools/mtg_wiki/card_search.py "Lightning Bolt"
python3 ./raw/tools/mtg_wiki/card_search.py "闪电击"

# Rule search (by rule number or keyword)
python3 ./raw/tools/mtg_wiki/rule_search.py "101.4"
python3 ./raw/tools/mtg_wiki/rule_search.py "stack"

# Card name translation (EN↔CN)
python3 ./raw/tools/mtg_wiki/name_translator.py "Lightning Bolt"
```

API priority:
1. mtgch API (`https://mtgch.com/api/v1/`) — Chinese preferred
2. Scryfall API (`https://api.scryfall.com/`) — English primary
3. Local 37k Oracle database — offline exact match

## Layer System Reference (CR 613)

| Layer | Content | Classic Example |
|-------|---------|-----------------|
| 1 | Copy effects | Clone |
| 2 | Control-changing effects | Treachery |
| 3 | Text-changing effects | Alter Reality |
| 4 | Type-changing effects | Blood Moon vs. Urborg |
| 5 | Color-changing effects | Blue dye |
| 6 | Add/remove abilities | Tidebinder, Sphinx's Revelation |
| 7 | Power/toughness-changing effects | Various +/– P/T |

Key distinctions:
- **Cross-layer effects (613.6)**: Different parts of the same ability resolve independently at each layer, even if the source ability disappears
- **Dependency (613.8)**: Only exists when effects are in the **same layer**

## Turn Structure

```
Beginning → Precombat Main → Combat → Postcombat Main → Ending
```

APNAP (CR 101.4):
- Active player decides first, non-active player decides second
- When multiple triggered abilities trigger simultaneously, they go on the stack in APNAP order
- Result: non-active player's triggers **resolve last (LIFO within APNAP)**

## Response Standards

1. **Prioritize Wiki citations**: Check `wiki/concepts/` for relevant concept pages first
2. **Precise rule citations**: Cite CR/MTR rule numbers, do not answer from memory
3. **Bilingual labeling**: Card names use `Chinese (English)` format
4. **Cross-links**: Include `[[slug|display]]` references in answers

## Complete Rules Files

| File | Content |
|------|---------|
| `raw/cr/1.md` | Game concepts, priority, costs |
| `raw/cr/6.md` | **Spells, abilities, layer system (613)** |
| `raw/cr/7.md` | **Keyword abilities (702), keyword actions (701)** |
| `raw/cr/glossarycn.md` | Chinese terminology glossary |

## Judge-Specific

Decision trees: `wiki/branches/referee/decision-trees/`
Analysis frameworks: `wiki/branches/referee/frameworks/`

For judge rules questions:
1. Break down by both timeline and mechanic dimensions
2. Mandatory deep search for keyword actions involved (check CR 702)
3. Four-step rule text reading: full copy → circle qualifiers → word-by-word confirmation → reverse verification
4. Output execution compliance report

## Notes

- **Always verify specific cards** — use `card_search.py` or API, never from memory
- **Chinese card names must be confirmed via mtgch** — user input may have errors or nicknames
- **Mind the layer system and timestamp** — for complex interactions, determine layer first
- **Commander rules are in CR 903** — sideboard limits, color identity, command tax
