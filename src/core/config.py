"""Configuration constants for the scraper."""

from __future__ import annotations

from enum import Enum
from pathlib import Path


class Language(str, Enum):
    """Supported website languages."""

    ZH_CN = "zh-cn"
    EN_US = "en-us"

    @property
    def label(self) -> str:
        """Human-readable label for the language."""
        return "简体中文" if self is Language.ZH_CN else "English"

    @property
    def subdir(self) -> str:
        """Output subdirectory name for this language."""
        return "" if self is Language.ZH_CN else "en"

    @property
    def state_suffix(self) -> str:
        """Suffix for the state file of this language."""
        return "" if self is Language.ZH_CN else "_en"


# Project root (relative paths are based on project root)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Current language (mutable via set_language)
_current_language = Language.ZH_CN


def set_language(lang: Language | str) -> None:
    """Set the active scraping language.

    Args:
        lang: A Language enum or its string value (e.g. "zh-cn", "en-us").
    """
    global _current_language
    if isinstance(lang, str):
        lang = Language(lang)
    _current_language = lang


def get_language() -> Language:
    """Return the currently active scraping language."""
    return _current_language


# ---- Output directories (language-aware) ----

def get_docs_dir() -> Path:
    """Return the docs output directory for the active language."""
    sub = _current_language.subdir
    return PROJECT_ROOT / "docs" / sub if sub else PROJECT_ROOT / "docs"


def get_images_dir() -> Path:
    """Return the images output directory for the active language."""
    return get_docs_dir() / "images"


def get_state_file() -> Path:
    """Return the state file path for the active language."""
    suffix = _current_language.state_suffix
    return PROJECT_ROOT / f".scraper_state{suffix}.json"


# Backward-compatible constants (default to Chinese)
DOCS_DIR = get_docs_dir()
IMAGES_DIR = get_images_dir()
STATE_FILE = get_state_file()


# ---- Website API endpoints (language-aware) ----

_KNOWLEDGE_BASE = "https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn"


def _lang_code() -> str:
    return _current_language.value  # "zh-cn" or "en-us"


def get_base_api_url() -> str:
    """Return the base API URL for the active language."""
    return f"{_KNOWLEDGE_BASE}/{_lang_code()}"


def get_catalog_url() -> str:
    """Return the catalog JSON URL for the active language."""
    return f"{get_base_api_url()}/catalog.json?game_biz=hk4eugc_cn&lang={_lang_code()}"


def get_content_url_template() -> str:
    """Return the content HTML URL template for the active language."""
    return (
        f"{get_base_api_url()}/{{path_id}}/content.html"
        f"?v=1016&game_biz=hk4eugc_cn&lang={_lang_code()}"
    )


def get_text_map_url() -> str:
    """Return the textMap JSON URL for the active language."""
    return f"{get_base_api_url()}/textMap.json?game_biz=hk4eugc_cn&lang={_lang_code()}"


# Backward-compatible constants (default to Chinese)
BASE_API_URL = get_base_api_url()
CATALOG_URL = get_catalog_url()
CONTENT_URL_TEMPLATE = get_content_url_template()
TEXT_MAP_URL = get_text_map_url()


# Website page URL (for reference links in markdown)
PAGE_URL_TEMPLATE = "https://act.mihoyo.com/ys/ugc/tutorial/detail/{path_id}"


def get_page_url_template() -> str:
    """Return the page URL template (unchanged across languages)."""
    return PAGE_URL_TEMPLATE


# Request settings
REQUEST_TIMEOUT = 30


def get_request_headers() -> dict[str, str]:
    """Return request headers adapted to the active language."""
    lang_code = _lang_code()
    if _current_language is Language.ZH_CN:
        accept_lang = "zh-CN,zh;q=0.9,en;q=0.8"
    else:
        accept_lang = "en-US,en;q=0.9,zh-CN;q=0.8"
    return {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/html, */*",
        "Accept-Language": accept_lang,
        "Cookie": f"mi18nLang={lang_code}",
    }


# Backward-compatible constant (default to Chinese headers)
REQUEST_HEADERS = get_request_headers()


# Maximum retries for failed requests
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

# Concurrency settings
MAX_WORKERS = 5
