#!/usr/bin/env python3
"""
万智牌原创卡牌生成器
根据用户输入的需求，结合 wiki 中的规则知识，构建优化后的 LLM Prompt 或直接调用 API 生成卡牌。
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from typing import List, Tuple

# Project root: this file is at output/card-generator/generate_card.py
PROJECT_ROOT = Path(__file__).resolve().parents[2]

WIKI_CONCEPTS_DIR = PROJECT_ROOT / "wiki" / "concepts"
TEMPLATES_DIR = Path(__file__).parent / "templates"
GENERATED_DIR = Path(__file__).parent / "generated"

MAX_CONCEPT_CHARS = 1200
MAX_MATCHED_CONCEPTS = 6


def load_concept_index() -> List[Tuple[str, Path, str]]:
    """扫描 wiki/concepts，返回 [(clean_title, file_path, full_title), ...]"""
    concepts = []
    if not WIKI_CONCEPTS_DIR.exists():
        print(f"错误：找不到 wiki 概念目录 {WIKI_CONCEPTS_DIR}", file=sys.stderr)
        sys.exit(1)

    for md_file in sorted(WIKI_CONCEPTS_DIR.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        title = None
        for line in content.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break
        if not title:
            continue
        clean = re.sub(r"[（(].*?[）)]", "", title).strip()
        concepts.append((clean, md_file, title, content))
    return concepts


def extract_relevant_concepts(user_input: str, concepts: List[Tuple[str, Path, str, str]]) -> List[Tuple[str, str, str]]:
    """根据用户输入匹配最相关的概念，返回 [(clean_title, full_title, snippet), ...]"""
    scored = []
    for clean, md_file, full_title, content in concepts:
        score = 0
        # 如果 clean title 出现在用户输入中，加分
        if clean.lower() in user_input.lower():
            score += len(clean) * 2
        # 分词匹配（简单按字/词）
        for char in clean:
            if char in user_input:
                score += 1
        if score > 0:
            # 提取正文内容（去掉 frontmatter）
            body = re.sub(r"^---\n.*?---\n", "", content, flags=re.DOTALL).strip()
            snippet = body[:MAX_CONCEPT_CHARS]
            if len(body) > MAX_CONCEPT_CHARS:
                snippet += "\n...（内容已截断）"
            scored.append((score, clean, full_title, snippet))

    scored.sort(key=lambda x: -x[0])
    results = []
    seen = set()
    for score, clean, full_title, snippet in scored[:MAX_MATCHED_CONCEPTS]:
        if clean not in seen:
            results.append((clean, full_title, snippet))
            seen.add(clean)
    return results


def build_prompt(user_input: str, concepts: List[Tuple[str, Path, str, str]]) -> str:
    relevant = extract_relevant_concepts(user_input, concepts)

    concept_blocks = []
    for clean, full_title, snippet in relevant:
        concept_blocks.append(f"### {full_title}\n{snippet}\n")
    concept_section = "\n".join(concept_blocks) if concept_blocks else "（无直接匹配的规则概念）"

    template_path = TEMPLATES_DIR / "prompt_template.md"
    if template_path.exists():
        template = template_path.read_text(encoding="utf-8")
    else:
        template = DEFAULT_PROMPT_TEMPLATE

    prompt = template.replace("{{USER_INPUT}}", user_input)
    prompt = prompt.replace("{{CONCEPTS}}", concept_section)
    return prompt


def call_claude_api(prompt: str) -> dict:
    """如果环境变量中有 ANTHROPIC_API_KEY，则调用 Claude API。"""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("未设置 ANTHROPIC_API_KEY 环境变量")

    try:
        from anthropic import Anthropic
    except ImportError:
        raise RuntimeError("请先安装 anthropic SDK: pip install anthropic")

    client = Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system="你是一位资深的万智牌卡牌设计师，精通万智牌完整规则（CR）和卡牌设计哲学。请严格按要求的 JSON 格式输出。",
        messages=[{"role": "user", "content": prompt}],
    )
    text = response.content[0].text
    # 尝试提取 JSON
    try:
        # 先找 markdown code block
        match = re.search(r"```json\n(.*?)\n```", text, re.DOTALL)
        if match:
            return json.loads(match.group(1))
        # 再找纯 JSON
        return json.loads(text)
    except json.JSONDecodeError:
        return {"raw_text": text}


def render_card_markdown(card: dict) -> str:
    """将卡牌 JSON 渲染为美观的 Markdown。"""
    zh_name = card.get("name", {}).get("zh", "未知")
    en_name = card.get("name", {}).get("en", "")
    mana = card.get("manaCost", "")
    ctype = card.get("type", "")
    text = card.get("text", {}).get("zh", "")
    flavor = card.get("flavorText", {}).get("zh", "")
    rarity = card.get("rarity", "")
    pt = ""
    if "power" in card and "toughness" in card:
        pt = f"{card['power']}/{card['toughness']}"
    if "loyalty" in card:
        pt = f"忠诚：{card['loyalty']}"

    lines = [
        f"# {zh_name}",
        f"*{en_name}*" if en_name else "",
        "",
        f"**法术力费用：** {mana}",
        f"**类型：** {ctype}",
        f"**稀有度：** {rarity}",
        "",
        "## 规则叙述",
        text,
        "",
    ]
    if flavor:
        lines.extend(["## 风味叙述", f"*{flavor}*", ""])
    if pt:
        lines.append(f"**P/T / 忠诚：** {pt}")
    if "designNotes" in card:
        lines.extend(["", "## 设计笔记", card["designNotes"]])
    return "\n".join(lines)


DEFAULT_PROMPT_TEMPLATE = """你是一位资深的万智牌设计师，精通完整规则（CR）和卡牌设计哲学。

## 用户需求
{{USER_INPUT}}

## 相关规则知识
{{CONCEPTS}}

## 任务
请设计一张完全原创的万智牌卡牌。要求：
1. 卡牌必须严格遵守万智牌的规则和术语规范。
2. 法术力费用和效应应当合理平衡（可以参考标准赛或限制赛的强度）。
3. 如果是生物，请给出合理的 P/T。
4. 如果是鹏洛客，请给出合理的起始忠诚度，并设计符合 CR 606 的忠诚异能格式（如 +1: ...，-2: ...）。
5. 规则叙述必须清晰、无歧义，使用标准万智牌术语。
6. 提供中文和英文双语名称、规则叙述、风味叙述。
7. 风味叙述（flavor text）要有故事感，契合卡牌的颜色和主题。

## 输出格式
请严格按以下 JSON 格式输出（不要加 markdown 代码块标记之外的额外解释）：

```json
{
  "name": {
    "zh": "中文名称",
    "en": "English Name"
  },
  "manaCost": "{2}{R}{R}",
  "type": "传奇生物 ~ 龙",
  "text": {
    "zh": "飞行，敏捷\\n当 ~ 进战场时，它对每位对手各造成 2 点伤害。",
    "en": "Flying, haste\\nWhen ~ enters the battlefield, it deals 2 damage to each opponent."
  },
  "flavorText": {
    "zh": "天空在它面前燃烧，大地在它脚下颤抖。",
    "en": "The sky burns before it, and the earth trembles beneath its claws."
  },
  "rarity": "rare",
  "power": "4",
  "toughness": "4",
  "designNotes": "设计思路简要说明"
}
```
"""


def main():
    parser = argparse.ArgumentParser(description="万智牌原创卡牌生成器")
    parser.add_argument("-p", "--prompt", required=True, help="用户对卡牌的设计需求描述")
    parser.add_argument("--generate", action="store_true", help="直接调用 Claude API 生成卡牌（需要 ANTHROPIC_API_KEY）")
    parser.add_argument("-o", "--output", help="输出文件路径（默认打印到终端）")
    args = parser.parse_args()

    concepts = load_concept_index()
    prompt = build_prompt(args.prompt, concepts)

    if not args.generate:
        print("=" * 60)
        print("已构建优化 Prompt，请复制到 Claude/ChatGPT 中使用：")
        print("=" * 60)
        print(prompt)
        return

    try:
        card = call_claude_api(prompt)
    except RuntimeError as e:
        print(f"API 调用失败: {e}", file=sys.stderr)
        sys.exit(1)

    md = render_card_markdown(card)

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(md, encoding="utf-8")
        json_path = out_path.with_suffix(".json")
        json_path.write_text(json.dumps(card, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"卡牌已保存到: {out_path}")
        print(f"JSON 已保存到: {json_path}")
    else:
        print(md)


if __name__ == "__main__":
    main()
