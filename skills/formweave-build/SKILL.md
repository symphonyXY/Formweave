---
name: formweave-build
description: 新建、修改、优化或打包 Windows 10/11 桌面程序，用于桌面工程实现、既有应用增量改造及交付故障排查。仅要技术方案、设计预览或审查意见时不使用本入口；不用于通用网站或手机应用开发。
license: MIT
compatibility: 需项目文件与命令执行能力；原生运行和打包验收需要 Windows 及目标框架工具链。随包样例按 references/examples.md 配置环境。
metadata:
  version: "1.0.0"
---

# Windows 应用开发

包内相对路径均以本 SKILL.md 所在目录为基准。按当前框架和交付阶段读取参考；不预先遍历全部样例或动效索引。

**第一次写入应用前检查确认状态。** 读取项目指引、代码、依赖、构建入口和当前聊天中已批准的范围。按[确认单](references/agreement.md)核对；缺失明确批准时只做调查并给出可确认方案，停止在写入前。不能从技能名、功能愿望或既有源码推定批准。确认后在范围内连续推进。

新建时用[框架指南](references/frameworks.md)选择最小架构；改造时先运行正常入口、记录原生集成与数据行为、准备可重复回归场景。修改前记录基线。外部依赖或素材按[复用记录](references/adoption.md)核查。

按[桌面设计](references/desktop.md)实现主任务及异常状态。借鉴移动界面时查[版本和转化依据](references/mobile.md)。用[性能与可靠性](references/performance.md)约定测量口径，再依[交付与维护](references/delivery.md)构建、试运行、清理和交付。

三个可复制的小型起点分别是 [Qt 工作台](assets/qt/workbench.py)、[WPF 项目](assets/wpf/Workbench.csproj)、[Electron 项目](assets/electron/package.json)。只在适合已确认项目时采用；构建和验证命令见[样例说明](references/examples.md)。

实现动效前用[桌面动效决策](references/motion.md)确定任务状态和回退，再从[双站索引](references/motion-index.md)选对应条目。沿用当前框架实现；在真实输入路径测试快速重复操作、取消与资源释放。

交付包含改动范围、源码或构建入口、运行条件、实际验证结果及未覆盖项。SDK、权限或运行库缺失时，记录失败命令和原因，完成仍可执行的检查；不得把源码生成当作可运行交付，也不为绕过故障擅自换框架。已有批准沿用，仅对改变范围的决定重新确认。
