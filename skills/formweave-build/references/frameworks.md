# 从约束筛到候选

先列硬约束（系统最低构建、运行库/离线、原生接口、关键控件、语言和现有代码），再比较维护人力、可访问性、数据规模、资源预算、部署和视觉表达。Windows 的目标分别列为 10 22H2 x64、11 x64；记录每条依赖链的实际版本及上游支持生命周期，产品目标与厂商支持分列。其他架构需单独确认。

| 路线 | 优先试验的场景 | 做决定前的小验证 |
|---|---|---|
| WinUI 3 / Windows App SDK | Windows 优先、XAML、系统外观及窗口能力 | 取最依赖系统的窗口/通知操作，比较有无包标识、运行时分发及 Win10 实色降级。已有 WPF/WinForms 可以单独引入必要的 Windows 能力。 [微软](https://learn.microsoft.com/en-us/windows/apps/get-started) |
| WPF / WinForms | .NET 数据应用、已有控件或业务表单。WPF 适合模板、数据绑定；WinForms 可低成本延续设计器工程 | 用真实数据量试虚拟化、编辑提交、焦点、逐显示器缩放；检查 .NET Desktop Runtime 或自包含发布体积。[WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/overview/) |
| Win32/MFC | 既有消息循环、Shell 扩展或深度原生集成 | 保留消息、句柄和 DPI 语义，先改局部，回归文件拖放与外部程序互操作。 |
| Qt Widgets（PySide6/C++） | 模型视图、密集表格、桌面工具、已有 Python/C++ 核心 | 分离数据模型和视图，试排序/筛选及原生拖放；测 Python 热点，检查平台插件、Qt 模块及许可。[Qt 平台](https://doc.qt.io/qt-6.10/supported-platforms.html) |
| Qt Quick/QML（PySide6/C++） | 强调状态转场、自定义视觉或触控，仍需桌面键鼠 | 原型对比 TableView、输入法候选框、键盘焦点、场景图与软件渲染回退。已有 Widgets 可针对单个表面试嵌入，先测额外渲染成本。[Qt Quick](https://doc.qt.io/qt-6/qtquick-index.html) |
| Electron | 已有 Web 编辑器或前端团队，需要固定 Chromium 行为 | 测完整进程树、离线页面和包体；隔离 renderer，用窄 IPC 接口暴露原生操作。[进程模型](https://www.electronjs.org/docs/latest/tutorial/process-model) |
| Tauri 2 / WebView2 | 可复用前端，能维护 Rust 或已有原生宿主 | 核验目标机 WebView2 的提供/离线更新方式和权限列表。Tauri 的 Windows 构建需要 Rust 与 MSVC；独立 WebView2 控件还需要宿主、生命周期和 IPC。[Tauri](https://v2.tauri.app/start/prerequisites/) |
| Avalonia / .NET MAUI | 已有 C# 工程或明确需要跨平台共享 | Avalonia 对多面板、原生互操作做小样；MAUI 优先验证现有移动项目的菜单、桌面窗口和数据控件。Windows 测试只对 Windows 成立。[Avalonia](https://docs.avaloniaui.net/) · [MAUI](https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui) |
| Flutter Desktop | Dart 团队、定制绘制、一致动效 | 先测 Windows 插件、IME、可访问性树、文件选择和 GPU 降级。[Flutter](https://docs.flutter.dev/platform-integration/windows/setup) |
| Tkinter/ttk、wxPython/wxWidgets | 小型离线工具、已有简单 Python 表单或原生控件工程 | 针对目标语言包、打包依赖、控件密度与高 DPI 试一个完整窗口。[Tkinter](https://docs.python.org/3/library/tkinter.html) · [wxPython](https://docs.wxpython.org/) |

分别做三个决定：①需要单进程、工作线程还是隔离子进程（故障、阻塞、IPC 成本）；②哪个 UI 框架通过硬约束；③代码放在哪里。单窗口工具可以是入口加一个模型；有多个工作流才拆 UI、领域操作、存储适配与任务执行。不按目录数判断架构质量。

迁移必须给出具体瓶颈、可比较的增量修复、重写成本、数据迁移和回滚办法。挑最高风险的真实操作做纵向小样，测过再选择。缺少目标 SDK、系统或硬件时标记资料参考或待验证，记录可复现命令，不伪造样例运行。
