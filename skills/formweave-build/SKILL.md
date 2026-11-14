---
name: formweave-build
description: 新建、修改、优化或打包 Windows 10/11 桌面程序，用于桌面工程实现、既有应用增量改造及交付故障排查。仅要技术方案、设计预览或审查意见时不使用本入口；不用于通用网站或手机应用开发。
license: MIT
metadata:
  version: "1.0.0"
---

# Windows 应用开发

包内相对路径以本 SKILL.md 所在目录为基准。按当前框架和交付阶段读取资料。

## 环境

需项目文件与命令执行能力；原生运行和打包验收需要 Windows 及目标框架工具链。随包样例按 references/examples.md 配置环境。

## 执行

**首次写入应用前核对批准范围。** 查看项目指引、代码、依赖、构建入口和聊天记录，按[范围确认](references/agreement.md)检查。缺少明确批准时，完成调查并给出可确认方案，停在写入前；技能名、功能愿望或已有源码不能代替批准。已有批准沿用，在范围内连续推进。

新建项目按[框架选型](references/frameworks.md)选择满足约束的最小方案。改造项目先运行正常入口，记录数据行为、原生集成及可重复的回归基线。按[桌面设计](references/desktop.md)实现主任务和异常状态，以[性能与可靠性](references/performance.md)约定测量方法，再按[交付与维护](references/delivery.md)构建、试运行和交付。

## 按需参考

| 当前需要 | 读取资料与用途 |
|---|---|
| 引入外部工程、依赖或素材 | [采用记录](references/adoption.md)：核对版本、许可与适配成本。 |
| 借鉴手机系统 | [移动方法转化](references/mobile.md)：保留桌面键鼠、窗口和原生能力。 |
| 实现动效或借鉴动效网站 | [动效决策](references/motion.md)确定触发、中断与降级；[界面与动效转化](references/interface-motion.md)用于布局、主题和参数控制。具体效果再查[来源导航](references/motion-index.md)，沿用当前框架实现。 |
| 需要适合当前项目的起点 | [样例说明](references/examples.md)：包含 Qt Widgets、WPF、Electron 的资源入口、环境与验证命令，只复制选定的完整样例。 |

## 交付

说明改动范围、源码或构建入口、运行条件、实际验证结果和未覆盖项。缺少 SDK、权限或运行库时，记录失败命令与原因，完成仍可执行的检查；源码生成不等于可运行交付，也不以换框架绕过故障。仅在平台、框架、数据行为或交付范围改变时重新确认。
