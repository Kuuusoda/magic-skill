"""Shared local test bootstrap for qq-bot scripts."""

from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv


BOT_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = BOT_ROOT.parent


def setup_test_env() -> None:
    """Load local .env and point tests at the current workspace."""
    load_dotenv(BOT_ROOT / ".env", override=False)

    plugins_path = str(BOT_ROOT / "plugins")
    if plugins_path not in sys.path:
        sys.path.insert(0, plugins_path)

    os.environ.setdefault("WIKI_PATH", str(PROJECT_ROOT / "wiki"))
    os.environ.setdefault("RAW_PATH", str(PROJECT_ROOT / "raw"))
    os.environ.setdefault("SKILL_PATH", str(PROJECT_ROOT / "skill"))
    os.environ.setdefault("AGENT_PATH", str(PROJECT_ROOT / "agent"))
    os.environ.setdefault("LLM_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")
    os.environ.setdefault("DASHSCOPE_MODEL", "glm-5.1")
    os.environ.setdefault("LLM_TIMEOUT_SECONDS", "120")
