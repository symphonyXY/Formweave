---
name: formweave-build
description: 按已确认范围实现、修改、测试或打包 Windows 10/11 桌面应用。也用于此类工程的只读交付检查、文档整理和发布准备；GitHub 写入须单独授权。不用于仅需方案、独立预览或界面审查的任务。
license: MIT
metadata:
  version: "1.0.0"
---

# Windows 应用开发

包内相对路径以本 SKILL.md 所在目录为基准。按当前框架和交付阶段读取资料。

## 环境

需项目文件与命令执行能力；原生运行和打包验收需要 Windows 及相应 SDK 或运行库。见[样例说明](references/examples.md)。

## 执行

**首次写入应用前核对批准范围。** 查看项目指引、代码、依赖、构建入口和聊天记录，按[范围确认](references/agreement.md)检查。缺少明确批准时，完成调查并给出可确认方案，停在写入前；技能名、功能愿望或已有源码不能代替批准。已有批准沿用，在范围内连续推进。

新建项目按[框架选型](references/frameworks.md)选择满足约束的最小方案。改造项目先运行正常入口，记录数据行为、原生集成及可重复的回归基线。按[桌面设计](references/desktop.md)实现主任务和异常状态，以[性能与可靠性](references/performance.md)约定测量方法，再按[交付与维护](references/delivery.md)构建、试运行和交付。

只要交付就绪报告时，按[项目盘点与安全清理](references/project-hygiene.md)只读调查，不生成或修改目标项目文件，也不运行不在范围内的应用或构建。若用户批准整理，按工程实际入口、构建和数据行为增量处理。清理核对具体清单；推送、创建 PR、写标签或 Release 等远端操作只按明确授权执行，不因「可以发布」或报告无阻塞而自动执行。

## 按需参考

| 当前需要 | 读取资料与用途 |
|---|---|
| 选择或复核工作台、对照、批量任务或单动作布局 | [桌面案例](references/desktop-patterns.md)：将当前记录、批量选中范围与运行中任务绑定到真实数据。 |
| 引入外部工程、依赖或素材 | [采用记录](references/adoption.md)：核对版本、许可与适配成本。 |
| 借鉴手机系统 | [移动方法转化](references/mobile.md)：保留桌面键鼠、窗口和原生能力。 |
| 实现动效或借鉴动效网站 | [动效决策](references/motion.md)确定触发、中断与降级；[界面与动效转化](references/interface-motion.md)用于布局、主题和参数控制。具体效果再查[来源导航](references/motion-index.md)，沿用当前框架实现。 |
| 需要适合当前项目的起点 | [样例说明](references/examples.md)：包含 Qt Widgets、WPF、Electron 的资源入口、环境与验证命令，只复制选定的完整样例。 |
| 整理或补写目标工程文档 | [仓库文档](references/repository-docs.md)：按受众选择 README、变更日志及社区文件，从干净副本复验命令。 |
| 准备向 GitHub 提交或发布 | [发布流程](references/github-publishing.md)：遵循用户的分支与可见性约定，先报告待发布范围，再按逐项授权执行。 |
| 实现桌面玻璃材质、对象预览或可反向的卡片重排 | [视觉材质与过渡](references/visual-motion-patterns.md)：从当前画面接续，不让业务或命中区依赖动效结束。 |

## 交付

说明改动范围、源码或构建入口、运行条件、实际验证结果和未覆盖项。已有验收编号时逐项回报；把结构盘点、真实运行、清理及远端操作的结果分开记。缺少 SDK、权限或运行库时记录原因并完成仍可执行的检查；源码生成不等于可运行交付，也不以换框架绕过故障。仅在平台、框架、数据行为或交付范围改变时重新确认应用实施范围。
