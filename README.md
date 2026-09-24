# 原神千星奇域·综合指南 文档抓取工具

> 抓取 [原神千星奇域·综合指南](https://act.mihoyo.com/ys/ugc/tutorial/detail/) 网站的全部内容，并按目录分类转换为 Markdown 文档。

## 功能特性

- **全量抓取**：抓取综合指南全部 188+ 篇文档，按网站目录结构分类存放
- **增量更新**：通过更新日志和 `updated_at` 时间戳自动检测变化，仅重新抓取有更新的页面
- **图片本地化**：自动下载文档中的图片到本地，Markdown 中使用相对路径引用
- **CLI + GUI 双模式**：命令行模式带 tqdm 进度条，图形界面使用 tkinter 默认风格
- **YAML Front Matter**：每篇文档包含标题、path_id、更新时间、分类、原文链接等元数据
- **索引生成**：自动生成 `docs/index.md` 索引文件，按目录树组织所有文档链接
- **自动发布**：推送 `v*` tag 时自动构建并发布 GitHub Release，更新说明取自 `CHANGELOG.md`

## 环境要求

- Python 3.10 或更高版本
- 建议在虚拟环境中运行

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/vers123/genshin-tutorial-scraper.git
cd genshin-tutorial-scraper
```

### 2. 创建并激活虚拟环境

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

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 运行

**命令行模式：**

```bash
# 检查更新并仅抓取变化的页面（推荐日常使用）
python main.py update

# 强制重新抓取所有页面
python main.py scrape --force

# 列出所有页面
python main.py list

# 仅列出顶级分类
python main.py list --categories

# 抓取单个页面
python main.py single <path_id>
```

**图形界面模式：**

```bash
python main.py --gui
```

## 目录结构

```
genshin-tutorial-scraper/
├── docs/                    # 抓取的 Markdown 文档（按分类组织）
│   ├── index.md             # 文档索引
│   ├── 更新日志/
│   ├── 读前须知/
│   ├── 界面介绍/
│   ├── 概念介绍/
│   ├── 节点介绍/
│   ├── 辅助功能/
│   └── 附录/
├── doc/
│   └── ai/                  # AI 工具使用的文档
├── src/
│   ├── scraper/             # 抓取核心模块
│   │   ├── catalog.py       # 目录树获取与解析
│   │   ├── content.py       # 页面内容获取
│   │   ├── converter.py     # HTML 转 Markdown
│   │   ├── images.py        # 图片下载
│   │   └── orchestrator.py  # 抓取编排
│   ├── core/
│   │   ├── config.py        # 配置常量
│   │   └── updater.py       # 更新检测
│   ├── cli.py               # 命令行入口
│   └── gui.py               # 图形界面入口
├── tests/                   # 单元测试
├── .github/workflows/       # GitHub Actions 工作流
├── CHANGELOG.md             # 更新日志
├── LICENSE                  # MIT 许可证
├── README.md                # 中文说明
├── README_EN.md             # English README
├── requirements.txt         # Python 依赖
├── pyproject.toml           # 项目配置
└── main.py                  # 程序入口
```

## 更新检测机制

工具会在项目根目录生成 `.scraper_state.json` 状态文件，记录每个页面的 `updated_at` 时间戳。

每次运行 `update`（或不带 `--force` 的 `scrape`）时：

1. 获取最新的 `catalog.json`
2. 对比每个页面的 `updated_at` 与状态文件中的记录
3. 仅抓取时间戳发生变化的页面（更新）和新页面（新增）
4. 移除目录中已不存在的页面对应的 Markdown 文件
5. 更新状态文件

这确保了日常更新只需抓取少量变化的页面，大幅提升效率。

## GitHub Actions 自动发布

项目配置了 GitHub Actions 工作流（`.github/workflows/release.yml`）：

- 当推送 `v*` 格式的 tag 时触发
- 自动运行测试
- 抓取最新文档
- 创建 GitHub Release，更新说明取自 `CHANGELOG.md` 中对应版本的内容

## 开发

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest tests/ -v
```

## 许可证

MIT License © 2026 vers123
