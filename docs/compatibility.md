# 兼容性与能力边界

适用版本：Formweave 1.0.0（2026-11-19）。中英文见[简体中文 README](../README.md)和[英文 README](../README.en.md)；包内正文及参考资料以简体中文为主。

## 工作流与技术栈

四个技能面向 Windows 桌面应用的规划、预览、开发与审查，可按目标项目的技术栈使用。选型资料覆盖 Qt Widgets、Qt Quick/QML、WPF、WinForms、WinUI 3、Electron、Tauri/WebView2、Avalonia、Flutter Desktop 等路线。当前随包可运行的桌面工程为 Qt Widgets、WPF 和 Electron。

HTML 用于独立展示界面设计和演示交互，正式应用可按目标框架实现相应布局与操作。框架覆盖和样例运行证据分别按下文记录，实际应用仍需在目标环境验收。

## 技能安装与客户端

安装与更新工具只需要 Python 3.13 标准库。四个技能可独立运行，包内引用不跨包。安装器按收据、目录清单和文件哈希核对内容，不以版本号大小拒绝更新；用户须使用原安装目标。本基线不改变包名、安装位置或收据格式。[安装冲突与恢复](../CONTRIBUTING.md#安装冲突与恢复)

| 客户端 | 安装目标 | 证据 |
|---|---|---|
| Codex | 用户或项目的技能目录，参照 [README](../README.md#安装和更新) | 有历史技能发现记录；本基线验证了隔离安装、更新与校验，不视作客户端自动触发复验。 |
| Claude Code | 可试用用户或项目的 `.claude/skills` 目录 | 静态适配；未实际验证技能发现、自动触发或执行。 |

## 浏览器预览

[层光](../skills/formweave-preview/assets/visual-motion-preview.html)和[差异复核](../skills/formweave-preview/assets/inventory-preview.html)用合成数据，在 Windows 11 的 Chrome 上运行。深浅材质、布局改向、减少动效和强制颜色的浏览器证据见[验证记录](validation.md#浏览器预览)。浏览器模拟不能证明 Windows 高对比度、混合 DPI、输入法或原生可访问性。

## Windows 原生样例

目标为 Windows 10 22H2 x64 及 Windows 11 x64；Windows 10 未实机验收。以下是 Windows 11 上的样例证据，不构成平台或框架的完整支持保证。实际应用以其 SDK、依赖和目标机测试为准。

| 样例 | 依赖与分发 | 已有证据 |
|---|---|---|
| Qt Widgets | PySide6-Essentials 6.10.2；PyInstaller 6.22.3 文件夹版。参见 [Qt 6.10 平台表](https://doc.qt.io/qt-6.10/supported-platforms.html)。 | QtTest、桌面截图、文件夹 EXE、进程采样。 |
| WPF | .NET 10 SDK 10.0.403；框架依赖版需要 Windows Desktop Runtime 10.0.14。[运行条件](https://learn.microsoft.com/en-us/dotnet/core/install/windows) | 发布目录 EXE、筛选、焦点与启动采样历史证据。 |
| Electron | [Electron 45.2.2 x64](https://github.com/electron/electron/releases/tag/v45.2.2)；官方运行时文件夹分发。 | 隔离桥烟测、原生文件对话框及进程树历史证据。 |

其他 Windows 框架见[选型参考](../skills/formweave-plan/references/frameworks.md)，不表示本仓库已实测。ARM64、x86、其他操作系统、生产项目和安装包升级／卸载未在本基线验证。外部文档和凭据检查工具可选；部署技能不要求安装这些工具。

Qt 样例的最小窗口为 610×420，宽度小于 760 时折叠详情栏。CI 使用 `QT_QPA_PLATFORM=offscreen` 检查交互与文件夹版启动，桌面会话另验原生窗口表现。GitHub Actions 使用 checkout v7、setup-python v7、setup-dotnet v6，其运行时均为 Node.js 24。[checkout 清单](https://github.com/actions/checkout/blob/v7/action.yml) · [setup-python 清单](https://github.com/actions/setup-python/blob/v7/action.yml) · [setup-dotnet 清单](https://github.com/actions/setup-dotnet/blob/v6/action.yml)

开发技能提供发布准备和授权检查，不承诺远端发布成功。远端写入须按指定仓库、分支和操作另行授权。
