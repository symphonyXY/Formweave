# Windows 工程文档怎么写

先读现有说明和真实运行入口。只增补使用者需要且有依据的文档；保持现有语言、命名和章节习惯。不为统一格式大改旧文件，不把空模板提交成已完成内容。README 优先帮首次使用者完成一个可见任务，开发细节移到贡献文档或能找到的子页面。

从[桌面 README 骨架](../assets/templates/desktop-readme.md)起步，替换真实名称、版本、命令和结果，删去不适用的小节。没有的安装版、便携版、截图、兼容环境或发布地址不要虚构。区分目标系统和实测系统、最终用户运行库和开发 SDK、安装包和源码；有用户持久数据时写明真实位置、升级迁移和卸载保留范围。用户只要文档时不要改代码来迎合例子。

| 文件 | 先回答什么 |
|---|---|
| `README.md` | 谁用、解决什么、怎样安装或解压、第一次怎么操作与看到什么、源码如何运行／构建、去哪求助；给必要的系统和架构条件。 |
| `CONTRIBUTING.md` | 开发工具链、环境准备、验证命令、问题复现材料、变更和 PR 要附的证据。若只内部使用，按团队约定保留精简入口。 |
| `CHANGELOG.md` | 面向用户，写改动、影响和升级动作，未发布内容列入 `Unreleased`；真实版本和定版日期留到定版时写。沿用项目版本规则，不生成提交日志转储。 |
| `LICENSE`、第三方声明 | 用用户同意的许可和适用的原文；不能自行替项目选许可，不能把被捆绑依赖、图标和字体一概写成项目许可证。 |
| `SECURITY.md`、Issue／PR 模板 | 有接收外部反馈的实际渠道时再补。写受支持版本与私下报告方法；问题模板收集实际与预期行为、系统、版本和复现步骤；PR 收集改动范围与证据。不要编造联系人或承诺。 |

## 格式和验收

- Markdown 保持标题层级清楚，站内路径使用相对链接，截图有说明和替代文本。代码围栏对应实际 Shell；命令和输出分开，说明工作目录、前置条件及预期结果，避免复制时连提示符或凭据一起带上。编码和换行遵循目标项目已有配置；新工程无约定时可采用 UTF-8 无 BOM、LF、末尾一换行。
- 从干净的隔离副本运行适用的命令，做一次典型操作，记录前提、实际输出与步骤；未获执行许可或缺工具时标记未验证。检查双语里的版本、系统和命令相同；没有受众需求不强制双语。不要把校验文档格式当作应用验收。
- 可选用 [Lychee v0.24.2](https://github.com/lycheeverse/lychee/blob/lychee-v0.24.2/README.md) 分开检查本地链接和外链，例如在目标根运行 `lychee --offline README.md`；网络限流单独记录。已有 Node.js 22+ 的工程可运行 [markdownlint-cli2 v0.24.1](https://raw.githubusercontent.com/DavidAnson/markdownlint-cli2/v0.24.1/README.md) 只检查适用规则。无外部工具时人工点击本地链接并记录范围，不声称已做自动化检查。

依据：[GitHub 中文 README 指南](https://docs.github.com/zh/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)及[格式语法](https://docs.github.com/zh/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)用于平台行为；[Standard Readme v1.3.0](https://github.com/RichardLitt/standard-readme/blob/v1.3.0/spec.md)、[Keep a Changelog 1.1.0](https://keepachangelog.com/zh-CN/1.1.0/)是写作参考，不是 GitHub 强制格式。[Microsoft 操作说明指南](https://learn.microsoft.com/en-us/style-guide/procedures-instructions/)与 [Flow Launcher v2.1.4 README](https://github.com/Flow-Launcher/Flow.Launcher/blob/v2.1.4/README.md)用于参考 Windows 安装和首次操作的写法，不复制第三方文字或图片。
