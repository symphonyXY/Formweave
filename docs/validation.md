# Formweave 1.0.0 验证记录

定版日期：2026-11-11。定版时静态与安装检查使用仓库 .venv 的 Python 3.13，在 Windows 上运行。样例测量按其真实采集时间单独记录，不能视为定版当天重新执行。

## Unreleased · 2026-11-14

### 本轮问题修复与复验

以下为本轮最新结果，后面的早期失败与待执行状态保留为历史记录，不能替代本表。

| 对象 | 实际方法与结果 |
|---|---|
| 通用校验差异 | 将四包原 compatibility 内容完整移入正文“环境”，保留名称、description、调用策略和版本。逐包运行宿主 skill-creator 的 quick_validate.py（Python -X utf8），四包均退出 0；未修改外部工具。环境要求未丢失。 |
| 独立校验漏检 | 先用测试复现独立包接受 CRLF、孤立参考文件的问题，再修复。现在 SKILL、UI YAML、其他文本均检查格式，references 必须可从入口到达，合法循环引用可通过。非法 YAML、重复字段、类型与长度边界继续覆盖。 |
| 安装收据 | 先复现 format:true 及重复 format 被误接受，再修复 JSON 解析与字段类型检查。异常收据清单同样拒绝，验证失败前后文件清单和哈希不变。保留格式号 1、完整哈希及原安装命令。 |
| 自动化与恢复 | unittest discover 共 18 项通过，包含四个真实包的安装、更新、交换失败还原及重试。额外验证回滚重命名也失败时 previous/new 恢复目录保留，未知文件保留。全部在隔离目标运行，未写用户技能目录。 |
| 旧包升级 | 从提交 8d5d68fdb59ad2f845a4e478ae1400c28ff3955f 提取完整四包并安装，再用本轮源码 update/verify；收据、格式、引用可达性均通过。恢复说明已区分“旧包与新源码不同”和“恢复损坏”，不再要求对旧包直接得到新源码的 verify 一致。 |
| Qt 样例探针 | 去除弃用的 QApplication.setActiveWindow 调用；以 QT_QPA_PLATFORM=offscreen 运行 tests/qt_probe.py，8 万行、筛选、连续选中、批量校验、取消、窗口布局及关闭路径通过。5 次筛选耗时中位约 22.56 ms，结果仅描述该离屏样例，不证明原生输入或性能预算达标。原始样本见下方证据。 |
| 独立模型行为 | 九例逐一在无父历史的独立代理中执行，八例符合观察判据，一例预览受环境限制；手机网页首次读取协议偏差已改用只含名称/描述的夹具并独立复核路由。已批准 Qt 副本有真实 windows 平台 7 项事件检查；预览的 5 项静态及 13 项模拟状态检查不算真实 UI 通过。详见[逐例结果](../evals/results-2026-11-14.md)与[原始结构化证据](evidence/behavior-2026-11-14.json)。 |
| 静态与清理 | 仓库 validate.py、git diff --check 通过；scripts/clean.py 只预览，候选 0 项，未删除仓库内容。 |

仍未覆盖：动效预览的真实浏览器交互被协议策略阻止，未尝试绕过；本机 dotnet --list-sdks 无输出，未重跑 WPF/.NET 10 构建；未重跑 Electron 打包、Windows 10、其他架构、混合 DPI、真实中文输入法、辅助技术或生产项目。以上属于未具备的验收证据，不能通过改文案记成已解决，也没有证据据此断言模板存在缺陷。

### 前期动效与结构整理（历史记录）

对象为四个技能的界面/动效参考、按需读取入口、来源索引与相关说明；VERSION 和原生样例未改动。环境为本仓库 Windows 工作区、.venv Python 3.13，网站操作使用应用内浏览器。以下结果仅适用于本次未定版改动。

| 证据类别 | 执行范围与结果 |
|---|---|
| 网站操作抽查 | Motion.Lab 目录显示 160 项；上滑淡入调参从 0.8 s 改为 0.2 s 后读数更新；查询 formweave-no-match 显示 0 个及清除筛选。Motion Hub 目录显示 60 项；淡入详情可切换提示词/实现示例；分段标签切到 Performance，重播恢复 Overview。通过可见状态核对，未测帧或逐项检查全部演示。 |
| 上游源码核对 | Motion.Lab 当前提交仍为 fbfda036aadbc1b46547bce8a7a57ec12bf73485，data/effects.ts 提取 160 个唯一 ID，指纹与旧索引一致；Motion Hub 提交 30de78c09594edc72cef28dfe165777a67fd8452，data/motions.js 提取 60 个唯一 ID，六类数量为进入 12、悬停 12、反馈 19、布局 5、滚动 8、图片 4。核对详情控制、主题变量及 README/package.json 许可差异，链接见[包内转化指南](../skills/formweave-plan/references/interface-motion.md)。 |
| 仓库静态与自动化 | scripts/validate.py 通过：四包引用自包含、同名共享参考逐字一致、元数据、版本及文本格式有效。unittest discover 共 12 项通过；扩展的索引测试核对三来源 277 项的数量、唯一性、ID 指纹、查询型详情 URL 及策略。git diff --check 通过。 |
| 完整包隔离安装 | TemporaryDirectory 的 formweave-full-packages-* 内复制四个真实包，并重定向 manage.SKILLS；逐包 install、verify、修改隔离参考后的 update 与独立校验通过。逐包注入暂存交换失败，确认目录和收据完全还原，再重试 update/verify 成功；未知 user-notes.txt 保留。未写用户技能安装目录。 |
| 补充通用校验 | skill-creator 自带 quick_validate.py 对四包均退出 1，原因是其字段白名单不含仓库原有的 compatibility；未为绕过该差异删除环境说明或修改外部校验器。仓库校验器按本项目规范支持该字段且通过，此项不记为通过。 |
| 文档复核与清理 | 核对网站观察与 Formweave 建议的区别、来源命名空间、未定版标记、中英文使用说明及独立包链接。scripts/clean.py 仅预览，候选 0 项，未执行仓库清理。 |
| 样例、真实项目及人工验收 | 本次未改应用样例，未重跑 GUI、打包或真实生产项目；两站全量键盘、减少动效、GPU 性能及原生 Windows 行为仍需对应环境验证。没有新增人工验收结论。 |

新增 motion-hub-source-routing、motion-preview-replay、motion-audit-screenshot-limit 三个模型行为案例，尚未运行与评分。它们的预期观察不作为行为通过证据；已有待评测案例状态保持不变。

#### 结构与语言复验

同日按 skill-creator 整理四个入口及参考资料。应用样例、触发描述、调用策略、清单版本和安装器未改动；未重新访问上游网站。将动效目录按来源拆分，保留全部条目、来源与许可，motion-index.md 继续作为导航入口。

| 检查 | 结果与边界 |
|---|---|
| 包结构与语言复核 | 四个入口区分执行、按需参考与交付；移除固定候选数量和逐项问卷式表述，保留应用写入前确认。方法资料以中文说明任务与结果，英文保留用于 API、命令和标识符；历史浏览器操作细节保留在本记录，不重复占用方法入口。 |
| 来源与静态回归 | 来源导航为 13 行；原 LuckyMaomi、Motion.Lab 目录分别放入新文件，重复分类合并后仍保留 57/160/60 项的 ID 集合。仓库 validate.py、12 项 unittest 及 git diff --check 通过，共享参考保持逐字一致。 |
| 从提交版本升级 | 隔离目录中从提交 8d5d68fdb59ad2f845a4e478ae1400c28ff3955f 提取四个真实包并安装，再以当前工作区快照 update/verify，全部通过。每包注入暂存交换失败，目录及收据完整还原，随后重试成功，未知文件保留。 |
| 独立读取 | 对安装副本逐包校验，并从各 SKILL.md 沿 Markdown 链接遍历；plan、preview、build、audit 的 9/9/14/9 个参考文件均可达，无跨包路径。该检查证明资料可发现，不证明模型实际选择了恰当资料。 |
| skill-creator 通用校验 | 对四个包再次运行 quick_validate.py，均因既有 compatibility 字段不在该工具白名单中退出 1。保留有效的环境说明与仓库字段约定，未修改外部工具或以删除字段绕过检查。 |
| 未执行项 | 未重跑模型行为、客户端选择器、原生样例、打包或人工验收；新增 plan-sufficient-constraints 案例待运行，不能以结构整理推断行为改善。 |

## 当前定版检查

| 证据类别 | 执行范围与结果 |
|---|---|
| 静态 | scripts/validate.py 检查四包清单、UI、引用、共享副本、版本与文本格式，通过；git diff --check 通过。 |
| 自动化回归 | unittest discover 共 12 项通过，覆盖清单类型、重复字段、长度边界、独立包、安装与更新、目标冲突、本地修改、链接、失败还原、清理及动效索引。 |
| 完整包隔离运行 | TemporaryDirectory 内复制四个真实技能并重定向 manage.SKILLS；执行 install、update、verify 和逐包校验；修改隔离来源模拟更新内容，并注入交换失败检查目录与收据恢复，全部通过。未写用户技能目录。 |
| 清理预览 | scripts/clean.py 预览候选 0 项，仓库未执行删除；测试生成的字节码在隔离目录按清单处理。 |
| 人工文档复核 | 核对目录职责、触发边界、包内路径、来源和兼容性表述；README 的命令、图片及页内导航与当前内容一致。 |

检查命令见[贡献指南](../CONTRIBUTING.md)，格式与来源依据见[技能设计说明](skill-design.md)。

## 原生样例证据

样例证据采集于 2026-11-04。测试主机为 Windows 11 家庭版 25H2 x64（26200.8037），Ryzen 9 7945HX，约 15.7 GiB 内存；框架与运行库版本见[兼容性矩阵](compatibility.md)。应用样例在本次整理中没有修改。

| 交付样例 | 从交付目录验证的行为 | 文件夹大小 | 首窗中位 ms | 私有提交中位 MiB |
|---|---|---:|---:|---:|
| Qt Widgets | 文件夹版启动与关闭，模型筛选、多选、校验和取消探针。[实际窗口](evidence/qt-workbench.png) | 94,011,880 字节 | 563.5 | 55.4 |
| WPF | 1 万条数据筛选、选中摘要、空结果、焦点与缩放。[实际窗口](evidence/wpf-inventory.png) | 194,359 字节，另需 .NET 10 Desktop Runtime | 563.1 | 71.6 |
| Electron | 隔离桥烟测、Windows 文件对话框三轮选择与取消。[实际窗口](evidence/electron-files.png) | 373,778,074 字节，含运行时 | 162.3 | 150.3 |

每个样例在同一主机连续启动三次，从创建进程至首个可见有标题窗口出现计时，约两秒后采样进程树。未清空系统缓存，工作负载各异，数据仅描述对应样例。[原始九次采样](evidence/window-samples.jsonl)

HTML 预览具有键盘选择、清除后焦点、窄窗、紧凑视图和减少动效的检查记录。[预览截图](evidence/inventory-preview.png)

## Agent 行为与未覆盖项

Codex CLI 0.166.0-alpha.6 具有四个技能的发现记录。已记录的独立行为评测涵盖确认不足时停在写入前、按现有 WPF 工程提出方案、独立预览、缺失材料、保留 Qt 快捷键及如实报告缺少 SDK。当前定版未重跑客户端选择器或模型行为评测。

1.0.0 定版时，motion-source-collision、motion-real-progress、negative-web-prototype、approved-scope-reuse、audit-no-material 五例尚待运行；本轮已完成这些案例的独立复验，最新结果与协议偏差见[逐例结果](../evals/results-2026-11-14.md)。其他旧案例没有在本轮重跑。[评测方法](../evals/README.md)

Claude Code 客户端、Windows 10 真机、混合 DPI 多屏、真实中文输入法、长时间运行、应用安装升级卸载和真实生产项目尚待验收。当前定版未重跑 GUI 或打包，不以静态检查推断这些行为通过；本地结果不包含远端 GitHub Actions 记录。

## 复验入口

原生运行与构建命令见[样例说明](../skills/formweave-build/references/examples.md)。Qt 探针为 tests/qt_probe.py；HTML 预览为 tests/preview_probe.cjs（需 Node、Playwright 和 Chrome）；Electron 原生文件对话框为 tests/electron_probe.cjs，参数为构建 EXE 的绝对路径。
