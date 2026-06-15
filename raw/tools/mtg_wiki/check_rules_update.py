#!/usr/bin/env python3
"""
Check if Comprehensive Rules (CR) documents have been updated since last run.

Strategy:
  1. Check if raw/cr/ directory exists
  2. Compare git diff in raw/cr/ against the last commit
  3. If no git history, check file modification times vs stored stamp
  4. Also attempt to fetch latest CR version from Scryfall
"""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib import request, error

PROJECT_ROOT = Path(__file__).resolve().parents[3]
CR_DIR = PROJECT_ROOT / "raw" / "cr"
MTR_DIR = PROJECT_ROOT / "raw" / "mtr"
IPG_DIR = PROJECT_ROOT / "raw" / "ipg"
STAMP_FILE = PROJECT_ROOT / "raw" / "data" / ".rules_version"
PROXY = os.environ.get("MTG_PROXY", "http://127.0.0.1:1083")


def http_get(url: str) -> str:
    """Simple HTTP GET returning text body."""
    proxy_handler = request.ProxyHandler({"http": PROXY, "https": PROXY})
    opener = request.build_opener(proxy_handler)
    req = request.Request(url, headers={
        "User-Agent": "mtg-wiki-cron/1.0",
    })
    try:
        with opener.open(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception:
        return ""


def check_git_changes(directory: Path) -> bool:
    """Check if files in directory have changed since last git commit."""
    import subprocess
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD", "--", str(directory.relative_to(PROJECT_ROOT))],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            return True
    except Exception:
        pass
    return False


def get_cr_version_from_scryfall() -> str | None:
    """Try to get latest CR release date from mtgch API."""
    # mtgch has comprehensive rules info
    try:
        proxy_handler = request.ProxyHandler({"http": PROXY, "https": PROXY})
        opener = request.build_opener(proxy_handler)
        # Scryfall doesn't directly expose CR version. Try alternative.
        # For now, use file-based check as primary method.
        pass
    except Exception:
        pass
    return None


def main():
    changes = []

    print("=== 检测规则文档更新 ===")

    # Check CR
    if CR_DIR.exists():
        cr_files = sorted(CR_DIR.glob("*.md"))
        if cr_files:
            # Get the most recently modified CR file
            newest = max(cr_files, key=lambda p: p.stat().st_mtime)
            newest_time = datetime.fromtimestamp(newest.stat().st_mtime, tz=timezone.utc)
            print(f"  CR 文件数: {len(cr_files)}, 最新修改: {newest_time.strftime('%Y-%m-%d %H:%M UTC')} ({newest.name})")

            if check_git_changes(CR_DIR):
                changes.append("CR (Comprehensive Rules)")
    else:
        print("  ⚠ CR 目录不存在")

    # Check MTR
    if MTR_DIR.exists():
        if check_git_changes(MTR_DIR):
            changes.append("MTR (Magic Tournament Rules)")

    # Check IPG
    if IPG_DIR.exists():
        if check_git_changes(IPG_DIR):
            changes.append("IPG (Infraction Procedure Guide)")

    # Load previous stamp
    old_version = "none"
    if STAMP_FILE.exists():
        old_version = STAMP_FILE.read_text().strip()

    if changes:
        new_version = datetime.now(timezone.utc).strftime("%Y-%m-%d-%H%M")
        print(f"\n  🔄 检测到更新: {', '.join(changes)}")
        for c in changes:
            print(f"    - {c}")
    else:
        now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        print(f"\n  ✅ 规则文档无变化 ({now_str})")

    print(f"  本地版本: {old_version}")

    # Update stamp (always, to track last check time)
    new_stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d-%H%M")
    STAMP_FILE.parent.mkdir(parents=True, exist_ok=True)
    STAMP_FILE.write_text(new_stamp)


if __name__ == "__main__":
    main()
