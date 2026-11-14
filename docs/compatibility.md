# 能力、兼容性与证据等级

适用版本：Formweave 1.0.0。核对日期：2026-11-11。

项目说明提供[简体中文](../README.md)与[英文](../README.en.md)版本；技能正文、包内参考及主要验证记录以简体中文为主。英文 README 不代表技能内容已全面英文化，也不改变下列平台与客户端的验证范围。

未定版补充核对：2026-11-14。LuckyMaomi、Motion.Lab 与 Web Motion Showcase（页面品牌 Motion Hub）作为界面和动效设计参考，277 个来源条目的元数据可离线查找；Motion Hub 与 LuckyMaomi 分属不同站点。四个包均附[界面与动效转化](../skills/formweave-build/references/interface-motion.md)和独立的 Motion Hub 索引；新增资料不引入运行依赖或改变安装路径，已安装包按 README 的 update 命令同步。

同日结构整理保留四个技能名、description 与调用策略。为兼容 skill-creator 通用校验器，将原 compatibility 环境要求完整迁入各 SKILL.md 的“环境”正文；不再依赖该工具不接受的头部字段，也未修改外部工具。motion-index.md 保留原路径并改为来源导航，三站目录保存在包内。使用原有 update 命令即可升级；安装位置、依赖、收据格式号不变。

具体项目沿用目标框架实现。两站页面抽查、索引静态覆盖与原生运行验证分别登记，新增方法没有扩大以下平台的实测范围。网页主题与 prefers-reduced-motion 不能代替原生系统设置、辅助技术和输入法验证。[桌面转化与验证方法](../skills/formweave-build/references/motion.md)

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

主要执行 Agent 为 Codex。历史技能发现记录来自 codex-cli 0.166.0-alpha.6；本轮 codex --version 实际返回 0.167.0-alpha.4.1，模型行为复验使用当前桌面会话的独立代理，不冒充该 CLI 版本的选择器实测。安装完整性、自然请求路由和桌面客户端选择器分开检查。其他客户端、ARM64、x86、其他操作系统及真实生产项目分别待验证。

## 技能格式与客户端

四个入口头部使用 name、description、license、metadata；运行环境放在正文，skill-creator 通用校验与仓库校验均通过。仓库校验器仍接受旧包合法的可选 compatibility 字段，但不以它作为当前四包的运行前提。独立包也检查 UTF-8/LF 格式与参考可达性。安装仅使用当前 formweave-* 名称，按收据和完整哈希检查目标；异常 JSON 重复字段、布尔格式号与非法清单会被拒绝，不覆盖现场。

| 客户端 | 安装与调用 | 当前证据 |
|---|---|---|
| Codex | 用户或项目的 .agents/skills；$formweave-plan 等 | 具有技能发现记录；本轮复验包格式、隔离升级及九个独立行为案例，结果与限制见验证记录；未重跑客户端选择器。 |
| Claude Code | 用户或项目的 .claude/skills；/formweave-plan 等 | 对照官方文档的静态适配，尚未实测发现、自动触发和任务执行。 |

通用正文不使用 Claude 专属变量、hooks 或工具预授权；Codex 的 UI 默认提示词仍使用其自身语法。客户端兼容性不代表原生 Windows 样例已经在新环境运行。[依据与具体取舍](skill-design.md)
