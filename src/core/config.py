"""Configuration constants for the scraper."""

from pathlib import Path

# Project root (relative paths are based on project root)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Output directories (relative to project root)
DOCS_DIR = PROJECT_ROOT / "docs"
IMAGES_DIR = DOCS_DIR / "images"
STATE_FILE = PROJECT_ROOT / ".scraper_state.json"

# Website API endpoints
BASE_API_URL = "https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn"
CATALOG_URL = f"{BASE_API_URL}/catalog.json?game_biz=hk4eugc_cn&lang=zh-cn"
CONTENT_URL_TEMPLATE = (
    f"{BASE_API_URL}/{{path_id}}/content.html?v=1016&game_biz=hk4eugc_cn&lang=zh-cn"
)
TEXT_MAP_URL = f"{BASE_API_URL}/textMap.json?game_biz=hk4eugc_cn&lang=zh-cn"

# Website page URL (for reference links in markdown)
PAGE_URL_TEMPLATE = "https://act.mihoyo.com/ys/ugc/tutorial/detail/{path_id}"

# Request settings
REQUEST_TIMEOUT = 30
REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/html, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

# Maximum retries for failed requests
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

# Concurrency settings
MAX_WORKERS = 5
