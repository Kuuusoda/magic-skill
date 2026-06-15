#!/usr/bin/env python3
"""
Download Scryfall Oracle Cards bulk data and convert to oracle-cards-lite.json.

Only keeps fields needed by build_indices.py and the mtg-wiki skill.
Uses HTTP proxy for download (default: http://127.0.0.1:1083).
"""
import json
import os
import sys
import time
from pathlib import Path
from urllib import request, error

# ── Config ──────────────────────────────────────────────────────────
PROXY = os.environ.get("MTG_PROXY", "http://127.0.0.1:1083")
SCRYFALL_BULK_API = "https://api.scryfall.com/bulk-data"
PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROJECT_ROOT / "raw" / "data"
OUTPUT_PATH = DATA_DIR / "oracle-cards-lite.json"

# Fields to keep in the lite version
KEEP_FIELDS = {
    "name", "oracle_id", "type_line", "oracle_text", "mana_cost",
    "cmc", "colors", "color_identity", "keywords",
    "power", "toughness", "loyalty",
    "legalities", "rarity", "set_name", "set", "released_at",
}

# ── Helpers ─────────────────────────────────────────────────────────
def http_get(url: str, timeout: int = 120) -> dict | None:
    """GET with proxy. Returns parsed JSON or None on failure."""
    proxy_handler = request.ProxyHandler({"http": PROXY, "https": PROXY})
    opener = request.build_opener(proxy_handler)
    req = request.Request(url, headers={
        "User-Agent": "mtg-wiki-cron/1.0 (github.com/mtg-judge)",
        "Accept": "application/json",
    })
    try:
        with opener.open(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore") if hasattr(e, "read") else ""
        print(f"  HTTP {e.code}: {body[:200]}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  Error: {e}", file=sys.stderr)
        return None


def download_file(url: str, dest: Path, timeout: int = 600) -> bool:
    """Download a file with progress indication. Returns True on success."""
    proxy_handler = request.ProxyHandler({"http": PROXY, "https": PROXY})
    opener = request.build_opener(proxy_handler)
    req = request.Request(url, headers={
        "User-Agent": "mtg-wiki-cron/1.0 (github.com/mtg-judge)",
    })
    try:
        with opener.open(req, timeout=timeout) as resp:
            total = int(resp.headers.get("Content-Length", 0))
            downloaded = 0
            chunk_size = 1024 * 1024  # 1MB
            dest.parent.mkdir(parents=True, exist_ok=True)
            with open(dest, "wb") as f:
                while True:
                    chunk = resp.read(chunk_size)
                    if not chunk:
                        break
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total:
                        pct = downloaded * 100 // total
                        print(f"\r  下载中... {downloaded // (1024*1024)}MB / {total // (1024*1024)}MB ({pct}%)", end="", flush=True)
            print()
            return True
    except Exception as e:
        print(f"\n  下载失败: {e}", file=sys.stderr)
        return False


def lite_card(card: dict) -> dict:
    """Extract only KEEP_FIELDS from a full card dict."""
    result = {}
    for field in KEEP_FIELDS:
        if field in card:
            result[field] = card[field]
    # Ensure legalities is always a dict
    if "legalities" not in result:
        result["legalities"] = {}
    return result


# ── Main ────────────────────────────────────────────────────────────
def main():
    print("Step 1: 获取 Scryfall bulk-data 元信息...")
    bulk = http_get(SCRYFALL_BULK_API)
    if not bulk:
        print("❌ 无法获取 bulk-data 列表", file=sys.stderr)
        sys.exit(1)

    # Find oracle_cards entry
    oracle_entry = None
    for item in bulk.get("data", []):
        if item.get("type") == "oracle_cards":
            oracle_entry = item
            break

    if not oracle_entry:
        print("❌ 未找到 oracle_cards 条目", file=sys.stderr)
        sys.exit(1)

    remote_updated = oracle_entry.get("updated_at", "unknown")
    download_url = oracle_entry.get("download_uri")
    uncomp_size = oracle_entry.get("size", 0)
    print(f"  远程更新时间: {remote_updated}")
    print(f"  文件大小: {uncomp_size // (1024*1024)}MB")
    print(f"  下载URL: {download_url}")

    # Check if already up-to-date
    version_file = DATA_DIR / ".oracle_version"
    if version_file.exists():
        local_version = version_file.read_text().strip()
        if local_version == remote_updated and OUTPUT_PATH.exists():
            print(f"\n  本地已是最新 ({local_version})，跳过下载。")
            return

    # Download
    print(f"\nStep 2: 下载 Oracle Cards ({uncomp_size // (1024*1024)}MB)...")
    tmp_path = DATA_DIR / "oracle-cards-full.tmp.json"
    if not download_file(download_url, tmp_path):
        tmp_path.unlink(missing_ok=True)
        sys.exit(1)
    print("  下载完成。")

    # Convert to lite
    print("\nStep 3: 转换为 oracle-cards-lite.json...")
    try:
        with open(tmp_path, "r", encoding="utf-8") as f:
            full_cards = json.load(f)
    except Exception as e:
        print(f"❌ 读取下载文件失败: {e}", file=sys.stderr)
        tmp_path.unlink(missing_ok=True)
        sys.exit(1)

    lite_cards = []
    for card in full_cards:
        lite_cards.append(lite_card(card))

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(lite_cards, f, ensure_ascii=False, separators=(",", ":"))

    # Cleanup temp file
    tmp_path.unlink()

    # Save version stamp
    version_file.write_text(remote_updated)

    print(f"  转换完成: {len(lite_cards)} 张牌")
    print(f"  输出: {OUTPUT_PATH}")
    size_mb = OUTPUT_PATH.stat().st_size / (1024 * 1024)
    print(f"  文件大小: {size_mb:.1f}MB")


if __name__ == "__main__":
    main()
