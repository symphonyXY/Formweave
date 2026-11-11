# 能力、兼容性与证据等级

适用版本：Formweave 1.0.0。核对日期：2026-11-11。

项目说明提供[简体中文](../README.md)与[英文](../README.en.md)版本；技能正文、包内参考及主要验证记录以简体中文为主。英文 README 不代表技能内容已全面英文化，也不改变下列平台与客户端的验证范围。

LuckyMaomi 与 Motion.Lab 作为动效设计与技术参考，元数据可离线查找；具体项目沿用目标框架实现。动效索引覆盖与框架运行验证分别登记，桌面验收仍按下表分列。[桌面转化与验证方法](../skills/formweave-build/references/motion.md)

目标为 Windows 10 22H2 x64（构建 19045 系列）及 Windows 11 x64。本次实机为 Windows 11 家庭版 25H2 26200.8037。记录测试构建能避免把系统大版本相同误当成运行条件相同。

界面实例与同机测量见 [Qt 工作台](evidence/qt-workbench.png)、[WPF 库存表](evidence/wpf-inventory.png)、[Electron 文件选择](evidence/electron-files.png)和[验证记录](validation.md)。交互场景各有侧重，不能按这三个样例推算同一产品在各框架上的性能。

| 对象 | 资料与适配 | Windows 11 本地证据 | Windows 10 |
|---|---|---|---|
| Qt Widgets / PySide6-Essentials 6.10.2 | 模型视图、可取消任务、PyInstaller 6.22.3 文件夹构建。[Qt 6.10 平台表](https://doc.qt.io/qt-6.10/supported-platforms.html) | 源码、QtTest、截图、文件夹 EXE、进程采样 | 目标，未实机验收 |
| WPF / .NET 10 | 数据绑定、窗口适配、框架依赖版。SDK 10.0.403，Windows Desktop Runtime 10.0.14。安装前分别核对 OS 生命周期和运行库。[微软运行条件](https://learn.microsoft.com/en-us/dotnet/core/install/windows) | 发布目录 EXE、筛选/焦点探针和启动采样 | 目标，未实机验收 |
| Electron 45.2.2 x64 | 原生文件选择、窄 IPC、离线页面、官方运行时文件夹分发。[官方构建](https://github.com/electron/electron/releases/tag/v45.2.2) | 页面/进程隔离烟测、打包启动及进程树；原生操作见验证记录 | 目标，未实机验收 |
| WinUI 3、WinForms、既有 Win32/MFC、Qt Quick/QML、C++ Qt Widgets | 专项选型、现有工程增量改造与验证路线 | 资料参考 | 资料参考 |
| Tauri 2、WebView2 宿主、Avalonia、.NET MAUI、Flutter Desktop、Tkinter/ttk、wxPython/wxWidgets | 约束、工具链和最小验证场景 | 资料参考 | 资料参考 |

[框架选型指南](../skills/formweave-plan/references/frameworks.md) 内有每条路线的决策条件。成熟项目复用、具体最低 OS、处理器、WebView2、VC++ 运行库、系统特效与离线分发须在应用自己的依赖锁定后核对。Windows 10 与 11 均须可读可操作；系统不支持可选特效时降级为不透明表面。

主要执行 Agent 为 Codex，本机 codex-cli 0.166.0-alpha.6 可用，行为评测使用 Codex 独立评测代理。安装的路径与完整性、技能路由的模拟请求和当前桌面客户端实际选择器是三个检查项。其他 Agent、ARM64、x86、其他操作系统、真实客户生产项目分别待验证。

## 技能格式与客户端

四个入口使用标准 license、compatibility 字段。校验器检查重复 YAML 字段、字段类型和长度，以及仓库 UTF-8/LF 文本格式。安装仅使用当前 formweave-* 名称，按收据和完整哈希检查目标；不识别或改动其他名称的目录。

| 客户端 | 安装与调用 | 当前证据 |
|---|---|---|
| Codex | 用户或项目的 .agents/skills；$formweave-plan 等 | 具有技能发现记录；定版复验包格式与隔离安装，未重跑客户端选择器。 |
| Claude Code | 用户或项目的 .claude/skills；/formweave-plan 等 | 对照官方文档的静态适配，尚未实测发现、自动触发和任务执行。 |

通用正文不使用 Claude 专属变量、hooks 或工具预授权；Codex 的 UI 默认提示词仍使用其自身语法。客户端兼容性不代表原生 Windows 样例已经在新环境运行。[依据与具体取舍](skill-design.md)
