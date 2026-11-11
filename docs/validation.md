# Formweave 1.0.0 验证记录

定版日期：2026-11-11。当前静态与安装检查使用仓库 .venv 的 Python 3.13，在 Windows 上运行。样例测量按其真实采集时间单独记录，不能视为定版当天重新执行。

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

motion-source-collision、motion-real-progress、negative-web-prototype、approved-scope-reuse、audit-no-material 五例尚待模型运行与评分。[评测案例与方法](../evals/README.md)

Claude Code 客户端、Windows 10 真机、混合 DPI 多屏、真实中文输入法、长时间运行、应用安装升级卸载和真实生产项目尚待验收。当前定版未重跑 GUI 或打包，不以静态检查推断这些行为通过；本地结果不包含远端 GitHub Actions 记录。

## 复验入口

原生运行与构建命令见[样例说明](../skills/formweave-build/references/examples.md)。Qt 探针为 tests/qt_probe.py；HTML 预览为 tests/preview_probe.cjs（需 Node、Playwright 和 Chrome）；Electron 原生文件对话框为 tests/electron_probe.cjs，参数为构建 EXE 的绝对路径。
