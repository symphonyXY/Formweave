# 按主任务选择桌面布局

先写出用户连续两三次操作的对象、动作和可见结果。已有工程沿用用户熟悉的导航。下面列出的是设计借鉴，按当前场景取用。核对日期为 2026-11-18，依据为上游文档及版本源码。

| 用户在做什么 | 值得看的界面 | 设计取舍与复验 |
|---|---|---|
| 浏览、查找一条记录 | Files 的 Details 视图支持调整列宽，信息面板可按需显示。[布局](https://files.community/docs/features/layout) · [v4.3](https://files.community/blog/posts/v4-3-0) | 让编号、名称和当前任务所需字段先进入视野。普通窗口原位更新详情，窄窗收起次要信息，仍能找到当前记录和操作。 |
| 连续复核差异 | GitHub Desktop 的 Changes 清单随当前文件显示差异，可切换统一或并排视图。[Windows 操作](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop?platform=windows) · [3.6.11](https://github.com/desktop/desktop/releases/tag/release-3.6.11) | 把前值、后值及变化量放在便于对照的位置。用方向键连续看三项，再检查详情、焦点和已勾选范围。 |
| 在宽表中定位和筛选 | DB Browser for SQLite 的 Qt 表格处理冻结列、筛选表头及滚动同步。[v3.13.1 表格源码](https://github.com/sqlitebrowser/sqlitebrowser/blob/v3.13.1/src/ExtendedTableWidget.cpp) | 仅当横向滚动会失去记录身份时考虑冻结编号。给表格一个键盘入口，导航记录与退出表格均应可预测。用长名称和窄窗试读。 |
| 预览批量变更 | PowerRename 就地对照原文件名与预计结果。[官方演示](https://learn.microsoft.com/en-us/windows/powertoys/powerrename) · [v0.102.3101](https://github.com/microsoft/PowerToys/releases/tag/v0.102.3101) | 把批量入口靠近选择摘要。开始时固定处理范围，任务途中改变筛选，回执仍按开始时的记录计算。 |
| 跟踪耗时任务 | HandBrake 可逐项查看队列并启动处理。[队列说明](https://handbrake.fr/docs/en/1.11.0/advanced/queue.html) · [1.11.2 WPF 界面](https://github.com/HandBrake/HandBrake/blob/1.11.2/win/CS/HandBrakeWPF/Views/QueueView.xaml) | 多个独立任务各有状态。一次批处理用状态栏即可显示进度、取消和终态。试取消后立即开始下一次，核对计数归属。 |
| 只执行一个动作 | 文件名查看器可直接并置选择按钮与结果。控件层级与间距可查 [WinUI Gallery v3.0.4](https://github.com/microsoft/WinUI-Gallery/releases/tag/v3.0.4) 和 [Windows 内容布局](https://learn.microsoft.com/en-us/windows/apps/design/basics/content-basics)。 | 让首次打开、取消、成功都有明确落点。一个文件入口通常只需一个主按钮，打开与返回的焦点可实测。 |

评估一个密集工作台时，固定数据、窗口和缩放，观察首屏完整行数、到达目标的按键数、焦点和任务反馈。保留字号可读性，结合截图判断压缩空间的代价。单动作工具则检查首次操作和返回结果是否容易找到。引入第三方实现时单独核对该版本涉及文件的许可及署名。
