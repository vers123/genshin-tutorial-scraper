# Genshin Impact Qianxing Qiyu Guide Scraper

> Scrape all content from the [Genshin Impact Qianxing Qiyu Comprehensive Guide](https://act.mihoyo.com/ys/ugc/tutorial/detail/) website and convert it to Markdown documents, organized by directory.

## Features

- **Full Scraping**: Scrapes all 188+ guide documents, organized by the website's directory structure
- **Incremental Updates**: Automatically detects changes via the update log and `updated_at` timestamps, only re-scraping modified pages
- **Local Images**: Downloads images locally and references them with relative paths in Markdown
- **CLI + GUI**: Command-line mode with tqdm progress bar; GUI uses tkinter default style
- **YAML Front Matter**: Each document includes metadata (title, path_id, updated_at, category, source URL)
- **Index Generation**: Auto-generates `docs/index.md` with links to all documents organized by directory tree
- **Auto Release**: Pushing a `v*` tag triggers an automated GitHub Release build; release notes come from `CHANGELOG.md`

## Requirements

- Python 3.10 or higher
- Recommended to run in a virtual environment

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/vers123/genshin-tutorial-scraper.git
cd genshin-tutorial-scraper
```

### 2. Create and activate a virtual environment

```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Windows (CMD)
python -m venv .venv
.\.venv\Scripts\activate.bat

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run

**CLI mode:**

```bash
# Check for updates and scrape only changed pages (recommended for daily use)
python main.py update

# Force re-scrape all pages
python main.py scrape --force

# List all pages
python main.py list

# List only top-level categories
python main.py list --categories

# Scrape a single page by path_id
python main.py single <path_id>
```

**GUI mode:**

```bash
python main.py --gui
```

## Project Structure

```
genshin-tutorial-scraper/
├── docs/                    # Scraped Markdown documents (organized by category)
│   ├── index.md             # Document index
│   ├── 更新日志/
│   ├── 读前须知/
│   ├── 界面介绍/
│   ├── 概念介绍/
│   ├── 节点介绍/
│   ├── 辅助功能/
│   └── 附录/
├── doc/
│   └── ai/                  # Documentation for AI tools
├── src/
│   ├── scraper/             # Core scraping modules
│   │   ├── catalog.py       # Catalog tree fetching & parsing
│   │   ├── content.py       # Page content fetching
│   │   ├── converter.py     # HTML to Markdown conversion
│   │   ├── images.py        # Image downloading
│   │   └── orchestrator.py  # Scraping orchestration
│   ├── core/
│   │   ├── config.py        # Configuration constants
│   │   └── updater.py       # Update detection
│   ├── cli.py               # CLI entry point
│   └── gui.py               # GUI entry point
├── tests/                   # Unit tests
├── .github/workflows/       # GitHub Actions workflows
├── CHANGELOG.md             # Changelog
├── LICENSE                  # MIT License
├── README.md                # Chinese README
├── README_EN.md             # English README
├── requirements.txt         # Python dependencies
├── pyproject.toml           # Project configuration
└── main.py                  # Program entry point
```

## Update Detection Mechanism

The tool creates a `.scraper_state.json` state file in the project root, recording the `updated_at` timestamp of each page.

Each time you run `update` (or `scrape` without `--force`):

1. Fetch the latest `catalog.json`
2. Compare each page's `updated_at` against the stored state
3. Scrape only pages whose timestamp changed (updates) and new pages (additions)
4. Remove Markdown files for pages that no longer exist in the catalog
5. Update the state file

This ensures daily updates only fetch a small number of changed pages, greatly improving efficiency.

## GitHub Actions Auto Release

The project includes a GitHub Actions workflow (`.github/workflows/release.yml`):

- Triggered when a `v*` tag is pushed
- Automatically runs tests
- Scrapes the latest documents
- Creates a GitHub Release with notes from the corresponding version in `CHANGELOG.md`

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v
```

## License

MIT License © 2026 vers123
