# 更新日志 / Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/lang/zh-CN/).

## [Unreleased]

### Fixed / 修复

- 修复 Release 工作流仅抓取中文文档的问题，现同时抓取中英文文档并生成各自索引
- 修复图片文件名可能出现 `.undefined` 等无效扩展名的问题，仅保留已知图片扩展名

## [1.1.0] - 2026-09-25

### Added / 新增

- 支持多语言抓取（简体中文 `zh-cn` / 英语 `en-us`）
- CLI 新增 `--lang` 参数选择语言版本
- GUI 新增语言下拉选择器
- 英文内容通过 `textMap.json` 自动映射正确的 path_id
- 英文文档输出到 `docs/en/` 目录，中文保持 `docs/`
- 各语言使用独立的状态文件（`.scraper_state.json` / `.scraper_state_en.json`）

## [1.0.0] - 2026-09-25

### Added / 新增

- 实现原神千星奇域·综合指南网站全量抓取功能
- 支持按网站目录结构分类存放 Markdown 文档
- 实现基于 `updated_at` 时间戳的增量更新检测
- 自动下载文档图片到本地并使用相对路径引用
- 命令行（CLI）模式，带 tqdm 进度条
- 图形界面（GUI）模式，使用 tkinter 默认风格，带进度条
- YAML Front Matter 元数据（标题、path_id、更新时间、分类、原文链接）
- 自动生成 `docs/index.md` 文档索引
- 中英双语 README
- AI 工具文档（`doc/ai/`）
- GitHub Actions 自动构建与 Release 工作流
- 完整单元测试（17 个测试用例）
