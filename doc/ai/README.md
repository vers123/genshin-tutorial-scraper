# AI 工具使用文档 / AI Tool Documentation

本文档供 AI 工具和自动化系统了解本项目的结构、接口和使用方式。

## 项目概述

`genshin-tutorial-scraper` 是一个用于抓取原神「千星奇域·综合指南」网站内容并转换为 Markdown 文档的 Python 工具。

- 项目根目录：`genshin-tutorial-scraper/`
- 所有路径均相对于项目根目录
- 抓取的文档输出到 `docs/` 目录，按网站目录结构分类

## 网站 API 接口

网站内容通过以下 JSON/HTML 接口提供（无需登录）：

| 接口 | URL | 说明 |
|------|-----|------|
| 目录树 | `https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/catalog.json?game_biz=hk4eugc_cn&lang=zh-cn` | 返回完整目录树 JSON |
| 页面内容 | `https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/{path_id}/content.html?v=1016&game_biz=hk4eugc_cn&lang=zh-cn` | 返回页面原始 HTML |
| 文本映射 | `https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/textMap.json?game_biz=hk4eugc_cn&lang=zh-cn` | 文本映射表 |

### catalog.json 结构

```json
[
  {
    "title": "界面介绍",
    "path_id": "mhz71urk21nq",
    "real_id": "mhz71urk21nq",
    "updated_at": "2025-09-19 18:47:23",
    "doc_type": "document",
    "children": [
      {
        "title": "整体界面",
        "path_id": "mhn4bsi5lb58",
        "children": [],
        "doc_type": "document"
      }
    ]
  }
]
```

关键字段：
- `path_id`：页面唯一标识，用于拼接 content.html URL
- `updated_at`：页面最后更新时间，用于增量更新检测
- `children`：子页面列表，空数组表示叶子节点

## 核心模块接口

### src/scraper/catalog.py

```python
from src.scraper.catalog import get_catalog_tree, get_all_pages, flatten_catalog

# 获取完整目录树
tree = get_catalog_tree()  # -> list[CatalogNode]

# 获取所有叶子页面（扁平化）
pages = get_all_pages()  # -> list[CatalogNode]

# CatalogNode 属性
node.title        # 页面标题
node.path_id      # 页面 ID
node.updated_at   # 更新时间
node.children     # 子节点列表
node.is_category  # 是否为分类节点
node.category_path # 分类路径（如 "概念介绍/单位"）
node.breadcrumb    # 面包屑路径列表
```

### src/scraper/content.py

```python
from src.scraper.content import fetch_content_html

html = fetch_content_html(path_id)  # -> str (UTF-8 HTML)
```

### src/scraper/converter.py

```python
from src.scraper.converter import html_to_markdown, get_safe_filename

md = html_to_markdown(html, md_file_dir=output_dir)
filename = get_safe_filename(title)  # -> "标题.md"
```

### src/scraper/images.py

```python
from src.scraper.images import download_image, get_relative_image_path

local_path = download_image(url)  # -> Path | None
rel_path = get_relative_image_path(local_path, md_file_dir)  # -> str
```

### src/scraper/orchestrator.py

```python
from src.scraper.orchestrator import scrape_all, scrape_page, generate_index, list_categories

# 抓取全部或仅更新的页面
stats = scrape_all(force=False, progress=callback)
# stats: {updated, added, removed, total, skipped, errors}

# 抓取单个页面
filepath = scrape_page(node)  # -> Path

# 生成索引
index_path = generate_index()  # -> Path

# 列出顶级分类
categories = list_categories()  # -> list[str]
```

### src/core/updater.py

```python
from src.core.updater import UpdateChecker

checker = UpdateChecker()
to_update, to_add, to_remove = checker.check_updates()
checker.record_page(node)
checker.save_state()
```

## 命令行接口

```bash
python main.py update              # 增量更新
python main.py scrape --force      # 全量抓取
python main.py list                # 列出所有页面
python main.py list --categories   # 列出顶级分类
python main.py single <path_id>    # 抓取单个页面
python main.py --gui               # 启动图形界面
```

## 状态文件

`.scraper_state.json` 存储每个页面的 `updated_at` 时间戳，用于增量更新检测。

## 输出目录结构

```
docs/
├── index.md
├── 更新日志/
│   └── 更新日志.md
├── 读前须知/
│   └── 读前须知.md
├── 界面介绍/
│   ├── 整体界面.md
│   ├── 地形编辑.md
│   └── ...
└── ...
```

每个 Markdown 文件包含 YAML Front Matter：

```markdown
---
title: 页面标题
path_id: xxxxx
updated_at: 2026-01-01 00:00:00
category: 分类路径
source_url: https://act.mihoyo.com/ys/ugc/tutorial/detail/xxxxx
---

# 正文标题
...
```

## 测试

```bash
pytest tests/ -v
```

测试覆盖：目录解析、HTML 转 Markdown、更新检测逻辑。
