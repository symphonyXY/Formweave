# Formweave 验证记录

当前基线：1.0.0（2026-11-19）。下列检查按对象区分；历史截图、测量及行为记录只适用于当时的环境和技能快照。

## 2026-11-19

### CI 布局与运行时修复

- [失败运行](https://github.com/symphonyXY/Formweave/actions/runs/44535276235)定位到 Qt 探针的窄窗断言。本地 `offscreen` 复现时，动态计数令布局最小宽度达到 772，610 宽的缩窗请求被限制，详情栏保持显示。
- 修复后，Python 3.13.17、PySide6-Essentials 6.10.2 下的桌面会话、`offscreen` 与 `offscreen` 加 `QT_SCALE_FACTOR=1.5` 三种探针均通过。检查 8 万行筛选、多选、校验、取消，610×420 实际窗口宽度、详情折叠及工具栏完整可见性。
- 静态校验和 24 项 unittest 通过，包含四包隔离安装、更新与失败恢复。隔离临时目录的 Qt 文件夹构建与 `offscreen` EXE 烟测通过。
- 工作流使用 Node.js 24 的官方 Action，运行条件见[兼容性说明](compatibility.md)。远端执行结果由 [GitHub Actions 工作流记录](https://github.com/symphonyXY/Formweave/actions/workflows/check.yml)提供。真实生产项目、Windows 10 真机及人工输入法和多屏验收仍为待验证项。

### README 文档复验

- 静态检查通过，包含双语版本与日期、语言切换的居中标记、本地链接与章节锚点、代码块、设计展示和程序示例先于安装教程的顺序。两种语言的命令和图片路径一致，覆盖两份 HTML 设计预览、三个程序示例与六张截图。设计展示按视觉、布局与交互内容介绍，程序示例按工程能力介绍。
- Python 3.13.17 下，README 的全量安装与单包安装命令分别在隔离临时目录通过 `install`、`update`、`verify`。24 项 unittest 通过，包含四个完整技能包的更新、失败恢复与重试。
- 样例运行与截图沿用下文已有证据。真实生产项目、Windows 10 真机和新增人工交互验收属于待验证项，README 排版检查采用源码与图片审阅。

### 基线复验

- Python 3.13.17：依赖检查、仓库校验和 24 项 unittest 通过，包含安装失败恢复、冲突保护和重试。四包在隔离目录全新安装通过；由旧托管安装更新到当前 1.0.0 也通过，四包分别通过独立校验和 skill-creator 通用校验。
- 两个浏览器探针及 Qt 的 8 万行探针均重跑通过。WPF 和 Electron 没有重新打包。证据文件均有文档引用，清理预览没有候选。
- 三个独立的描述级路由试验分别将已有 WPF 应用的可点击预览选为 `formweave-preview`，将只读交付检查选为 `formweave-build`，将移动网页任务选为「无」。仅提供技能名称、描述及该例请求；未执行任务，也未测试客户端自动触发。

### 浏览器预览

[层光素材总览](../skills/formweave-preview/assets/visual-motion-preview.html)使用原创几何图和合成数据，不分发 M HUB 的视频、壁纸、产品图、品牌或实现。[深色](evidence/2026-11-19/visual-motion-dark.png)和[浅色](evidence/2026-11-19/visual-motion-light.png)在 1180×780、第二张卡已选中、开启减少动效时采集。

在 Windows 11 的 Chrome 158.0.8127.37、Playwright 1.62.1 验证：

- 离线打开无网络请求。鼠标或 Tab 临时预览，点击或 Enter 确认；Esc 恢复已选。标签用键盘切换，不移动外壳。
- 动画在 85 ms 和反向后的 110 ms 改向；同一卡片位置和尺寸四个分量的偏差均不超过 1 CSS px。旧动画取消，工具栏位置、焦点、选中和卡片数保持。这是样例测量，不是 M HUB 参数。
- 手动减少动效取消进行中的卡片动画；模拟系统减少动效时无活动动画。590 和 390 CSS px 下直接切换，无横向溢出。浏览器强制颜色隐藏背景光影，保留选择语义。
- 既有差异复核预览的筛选、键盘查看与多选、任务取消、范围快照和窄窗探针通过。浏览器结果不覆写原生验收边界。

### 交付流程

- 对新复制和既有的两个 Qt 样例副本，按 README 骨架用已有依赖的 Python 运行 `python -B workbench.py --smoke`，均在含空格和中文的路径出现窗口并通过单记录筛选。新副本另通过 PyInstaller 6.22.3 文件夹版烟测；未从无开发依赖的目标机验证。
- 三个独立代理的[行为检查](../evals/results-2026-11-19.md)覆盖详细设计、已有工程只读盘点和未授权的发布准备。均为显式调用，不能替代客户端自然触发测试。

## 2026-11-18

- 浏览器盘点测试：72 条中 54 条有差异、18 条相符；核对了清空恢复焦点、选中范围快照和任务取消。[HTML 截图](evidence/2026-11-18/inventory-preview.png)
- Windows 11 Qt 6.10.2：8 万条数据，复验筛选、键盘多选、批量校验与取消。610×420 可见主操作，另在模拟 150% 缩放时运行探针。[Qt 截图](evidence/2026-11-18/qt-workbench.png)
- [A/B 生成对照](../evals/results-2026-11-18.md)保留双方宽窄窗口截图。每组仅一次生成，不能推断整体模型或技能质量。

## 2026-11-14

[九例独立行为评测](../evals/results-2026-11-14.md)中八例符合判据、一例预览因环境限制仅部分通过；自然请求路由首次读取协议偏差与修正也有记录。[结构化证据](evidence/behavior-2026-11-14.json)

动效目录对照了 Motion.Lab 与 Motion Hub 的固定提交，核对唯一 ID、分类及许可声明差异；只抽查了部分页面交互。包内[界面与动效转化](../skills/formweave-build/references/interface-motion.md)保留来源与许可，不把索引覆盖当作实际移植或性能结果。

## 原生历史测量

采集于 2026-11-04，Windows 11 家庭版 25H2 x64（26200.8037），Ryzen 9 7945HX，约 15.7 GiB 内存。不是本次重整后的新测量。

| 样例 | 历史验证 | 文件夹大小 | 首窗中位数 | 私有提交中位数 |
|---|---|---:|---:|---:|
| Qt Widgets | 启动关闭、模型筛选、多选、校验及取消。[实际窗口](evidence/qt-workbench.png) | 94,011,880 字节 | 563.5 ms | 55.4 MiB |
| WPF | 一万条记录的筛选、选中、空结果、焦点与缩放。[实际窗口](evidence/wpf-inventory.png) | 194,359 字节，另需运行库 | 563.1 ms | 71.6 MiB |
| Electron | 隔离桥烟测、三轮原生文件选择与取消。[实际窗口](evidence/electron-files.png) | 373,778,074 字节，含运行时 | 162.3 ms | 150.3 MiB |

每个样例连续启动三次；计时至首个可见有标题窗口，然后采样进程树。未清空系统缓存，不用此表直接比较框架性能。[原始测量](evidence/window-samples.jsonl) · [历史 HTML 截图](evidence/inventory-preview.png)

## 复验入口与限制

- 仓库格式、版本、独立包和安装恢复：见[贡献指南](../CONTRIBUTING.md#验证)。
- 预览：在仓库根目录运行 `node tests/visual_preview_probe.cjs "<Chrome 可执行文件>"` 或 `node tests/preview_probe.cjs "<Chrome 可执行文件>"`；Node 须能解析 Playwright。层光探针可追加截图文件前缀。
- 原生：按[样例说明](../skills/formweave-build/references/examples.md)准备框架。Qt 交互用 [qt_probe.py](../tests/qt_probe.py)，Electron 文件对话框用 [electron_probe.cjs](../tests/electron_probe.cjs)，进程采样用 [window_probe.py](../tests/window_probe.py)。
- 本基线未验证 Windows 10 真机、混合 DPI 多屏、真实中文输入法、Claude Code 实际运行、长时间性能、真实生产项目或远端发布。
