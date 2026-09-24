"""Graphical user interface for the scraper using tkinter."""

from __future__ import annotations

import threading
import tkinter as tk
from tkinter import messagebox, ttk

from src.scraper.orchestrator import generate_index, scrape_all
from src.scraper.catalog import get_catalog_tree, flatten_catalog


class ScraperGUI:
    """Main application window for the scraper GUI."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("原神千星奇域·综合指南抓取工具")
        self.root.geometry("680x520")
        self.root.minsize(560, 420)

        self._scraping = False
        self._build_ui()

    def _build_ui(self) -> None:
        # Main frame
        main = ttk.Frame(self.root, padding=16)
        main.pack(fill=tk.BOTH, expand=True)

        # Title
        title = ttk.Label(
            main,
            text="原神千星奇域·综合指南 文档抓取工具",
            font=("Microsoft YaHei UI", 14, "bold"),
        )
        title.pack(pady=(0, 12))

        # Options frame
        opt_frame = ttk.LabelFrame(main, text="选项", padding=12)
        opt_frame.pack(fill=tk.X, pady=(0, 12))

        self.force_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            opt_frame,
            text="强制重新抓取所有页面（忽略更新检测）",
            variable=self.force_var,
        ).pack(anchor=tk.W)

        self.index_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            opt_frame,
            text="抓取完成后生成索引文件 (index.md)",
            variable=self.index_var,
        ).pack(anchor=tk.W)

        # Stats frame
        self.stats_frame = ttk.LabelFrame(main, text="统计", padding=12)
        self.stats_frame.pack(fill=tk.X, pady=(0, 12))

        self.stats_labels: dict[str, ttk.Label] = {}
        stats_row = ttk.Frame(self.stats_frame)
        stats_row.pack(fill=tk.X)
        for i, key in enumerate(["更新", "新增", "删除", "跳过", "错误"]):
            ttk.Label(stats_row, text=f"{key}:").grid(row=0, column=i * 2, padx=(0, 4))
            lbl = ttk.Label(stats_row, text="0", font=("Consolas", 10, "bold"))
            lbl.grid(row=0, column=i * 2 + 1, padx=(0, 12))
            self.stats_labels[key] = lbl

        # Progress frame
        prog_frame = ttk.LabelFrame(main, text="进度", padding=12)
        prog_frame.pack(fill=tk.X, pady=(0, 12))

        self.progress = ttk.Progressbar(
            prog_frame, orient=tk.HORIZONTAL, mode="determinate"
        )
        self.progress.pack(fill=tk.X, pady=(0, 8))

        self.status_var = tk.StringVar(value="就绪")
        self.status_label = ttk.Label(
            prog_frame, textvariable=self.status_var, foreground="#555"
        )
        self.status_label.pack(anchor=tk.W)

        # Buttons
        btn_frame = ttk.Frame(main)
        btn_frame.pack(fill=tk.X, pady=(0, 12))

        self.start_btn = ttk.Button(
            btn_frame, text="开始抓取", command=self._on_start
        )
        self.start_btn.pack(side=tk.LEFT, padx=(0, 8))

        ttk.Button(btn_frame, text="列出页面", command=self._on_list).pack(
            side=tk.LEFT
        )

        # Log area
        log_frame = ttk.LabelFrame(main, text="日志", padding=8)
        log_frame.pack(fill=tk.BOTH, expand=True)

        self.log_text = tk.Text(
            log_frame, height=8, wrap=tk.WORD, state=tk.DISABLED
        )
        scrollbar = ttk.Scrollbar(
            log_frame, orient=tk.VERTICAL, command=self.log_text.yview
        )
        self.log_text.configure(yscrollcommand=scrollbar.set)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def _log(self, msg: str) -> None:
        """Append a message to the log area (thread-safe)."""
        def _append():
            self.log_text.configure(state=tk.NORMAL)
            self.log_text.insert(tk.END, msg + "\n")
            self.log_text.see(tk.END)
            self.log_text.configure(state=tk.DISABLED)

        self.root.after(0, _append)

    def _set_progress(self, current: int, total: int, message: str) -> None:
        """Update the progress bar (thread-safe)."""
        def _update():
            if total > 0:
                self.progress["maximum"] = total
                self.progress["value"] = current
            self.status_var.set(f"{current}/{total} - {message}")

        self.root.after(0, _update)

    def _update_stats(self, stats: dict[str, int]) -> None:
        """Update the statistics labels (thread-safe)."""
        def _do():
            mapping = {
                "更新": stats.get("updated", 0),
                "新增": stats.get("added", 0),
                "删除": stats.get("removed", 0),
                "跳过": stats.get("skipped", 0),
                "错误": stats.get("errors", 0),
            }
            for key, val in mapping.items():
                self.stats_labels[key].configure(text=str(val))

        self.root.after(0, _do)

    def _set_scraping(self, scraping: bool) -> None:
        self._scraping = scraping
        self.start_btn.configure(
            text="抓取中..." if scraping else "开始抓取",
            state=tk.DISABLED if scraping else tk.NORMAL,
        )

    def _on_start(self) -> None:
        if self._scraping:
            return
        self._set_scraping(True)
        self._log("开始抓取...")
        force = self.force_var.get()
        build_index = self.index_var.get()

        # Reset stats
        self._update_stats({})

        thread = threading.Thread(
            target=self._run_scrape, args=(force, build_index), daemon=True
        )
        thread.start()

    def _run_scrape(self, force: bool, build_index: bool) -> None:
        try:
            stats = scrape_all(
                force=force, progress=self._set_progress
            )
            self._update_stats(stats)
            self._log(
                f"完成: 更新={stats.get('updated', 0)}, "
                f"新增={stats.get('added', 0)}, "
                f"删除={stats.get('removed', 0)}, "
                f"跳过={stats.get('skipped', 0)}, "
                f"错误={stats.get('errors', 0)}"
            )
            if build_index:
                self._log("生成索引文件...")
                idx = generate_index()
                self._log(f"索引已生成: {idx}")
            self._log("全部完成。")
        except Exception as exc:
            self._log(f"[错误] {exc}")
            messagebox.showerror("错误", str(exc))
        finally:
            self.root.after(0, lambda: self._set_scraping(False))

    def _on_list(self) -> None:
        self._log("获取页面列表...")
        try:
            tree = get_catalog_tree()
            pages = flatten_catalog(tree)
            self._log(f"共 {len(pages)} 个页面")
            for p in pages[:20]:
                self._log(f"  [{p.path_id}] {p.title}")
            if len(pages) > 20:
                self._log(f"  ... 还有 {len(pages) - 20} 个页面")
        except Exception as exc:
            self._log(f"[错误] {exc}")


def main() -> None:
    """Launch the GUI application."""
    root = tk.Tk()
    # Use default ttk theme
    try:
        style = ttk.Style()
        # Use a clean default theme; avoid platform-specific custom themes
        if "vista" in style.theme_names():
            style.theme_use("vista")
        elif "clam" in style.theme_names():
            style.theme_use("clam")
    except tk.TclError:
        pass
    app = ScraperGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
