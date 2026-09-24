"""Command-line interface for the scraper."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from tqdm import tqdm

from src.core.config import Language, set_language
from src.scraper.orchestrator import (
    generate_index,
    list_categories,
    scrape_all,
    scrape_page,
)
from src.scraper.catalog import get_catalog_tree, flatten_catalog


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="genshin-scraper",
        description="抓取原神千星奇域·综合指南网站内容并转换为 Markdown 文档。",
    )
    parser.add_argument(
        "--lang",
        choices=[lang.value for lang in Language],
        default=Language.ZH_CN.value,
        help="抓取的语言版本 (zh-cn 或 en-us)，默认 zh-cn",
    )
    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    # scrape command
    scrape_p = subparsers.add_parser(
        "scrape", help="抓取文档（默认仅抓取有更新的页面）"
    )
    scrape_p.add_argument(
        "--force", action="store_true", help="强制重新抓取所有页面"
    )
    scrape_p.add_argument(
        "--no-index", action="store_true", help="不生成索引文件"
    )

    # update command (alias for scrape without force)
    subparsers.add_parser("update", help="检查更新并仅抓取变化的页面")

    # list command
    list_p = subparsers.add_parser("list", help="列出所有页面或分类")
    list_p.add_argument(
        "--categories", action="store_true", help="仅列出顶级分类"
    )

    # single command
    single_p = subparsers.add_parser("single", help="抓取单个页面")
    single_p.add_argument("path_id", help="页面的 path_id")

    return parser


def cmd_scrape(args: argparse.Namespace) -> int:
    """Execute the scrape/update command."""
    force = getattr(args, "force", False)

    print(f"{'强制抓取所有页面' if force else '检查更新...'}")
    stats = {"total": 0, "errors": 0}

    pbar = None

    def progress(current: int, total: int, message: str) -> None:
        nonlocal pbar
        if pbar is None or pbar.total != total:
            if pbar:
                pbar.close()
            pbar = tqdm(total=total, desc="抓取进度", unit="页")
        pbar.update(1)
        pbar.set_postfix_str(message[:40])

    try:
        stats = scrape_all(force=force, progress=progress)
    finally:
        if pbar:
            pbar.close()

    print("\n抓取完成:")
    print(f"  更新: {stats.get('updated', 0)} 页")
    print(f"  新增: {stats.get('added', 0)} 页")
    print(f"  删除: {stats.get('removed', 0)} 页")
    print(f"  跳过: {stats.get('skipped', 0)} 页")
    print(f"  错误: {stats.get('errors', 0)} 页")

    if not getattr(args, "no_index", False):
        print("生成索引文件...")
        index_path = generate_index()
        print(f"  索引: {index_path}")

    return 0 if stats.get("errors", 0) == 0 else 1


def cmd_list(args: argparse.Namespace) -> int:
    """Execute the list command."""
    if args.categories:
        cats = list_categories()
        print("顶级分类:")
        for cat in cats:
            print(f"  - {cat}")
    else:
        tree = get_catalog_tree()
        pages = flatten_catalog(tree)
        print(f"共 {len(pages)} 个页面:")
        for p in pages:
            print(f"  [{p.path_id}] {p.title}  ({p.category_path})")
    return 0


def cmd_single(args: argparse.Namespace) -> int:
    """Execute the single page scrape command."""
    path_id = args.path_id
    print(f"抓取页面: {path_id}")
    # Find the node in the catalog (match by content path_id or catalog path_id)
    tree = get_catalog_tree()
    pages = flatten_catalog(tree)
    node = next(
        (p for p in pages if p.path_id == path_id or p.catalog_path_id == path_id),
        None,
    )
    if node is None:
        print(f"[错误] 未找到 path_id={path_id} 的页面")
        return 1
    filepath = scrape_page(node)
    print(f"已保存: {filepath}")
    return 0


def main(argv: list[str] | None = None) -> int:
    """Main CLI entry point."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    # Set the active language before doing anything else
    set_language(args.lang)

    if args.command is None:
        parser.print_help()
        return 0

    handlers = {
        "scrape": cmd_scrape,
        "update": lambda a: cmd_scrape(
            argparse.Namespace(force=False, no_index=False)
        ),
        "list": cmd_list,
        "single": cmd_single,
    }

    handler = handlers.get(args.command)
    if handler is None:
        parser.print_help()
        return 1

    try:
        return handler(args)
    except KeyboardInterrupt:
        print("\n已取消。")
        return 130
    except Exception as exc:
        print(f"[错误] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
