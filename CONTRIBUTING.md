# 贡献指南

## 目录与文件格式

- `skills/<skill-name>/` 是独立安装单元。名称使用英文小写和连字符，目录名与 SKILL.md 的 name 相同。运行所需的脚本、模板、许可和参考资料放在包内。多个包共用的同名参考保持字节一致。
- `scripts/` 放仓库维护工具，`tests/` 放可执行检查，`evals/` 放行为请求与判据，`docs/evidence/` 放验证记录实际引用的图片和原始测量。
- 说明文档以简体中文为主，文件名使用有意义的英文。Markdown 文档通常用小写连字符，Python 模块用下划线；README.md、SKILL.md、WPF 的 XAML 文件等沿用平台惯例。
- 文本统一为 UTF-8 无 BOM、LF、文件末尾一个换行。代码缩进遵循 [.editorconfig](.editorconfig)；Git 通过 [.gitattributes](.gitattributes) 规范检出时的换行并保留二进制图片。文档链接使用仓库相对路径。
- 依赖环境、IDE 状态和临时输出留在本地。新增外部代码、字体或图标前核对来源、版本、许可和署名。

技能编写依据与取舍见[技能格式与设计依据](docs/skill-design.md)。description 写任务与触发边界；SKILL.md 保留必要约束、交付判据及带读取条件的参考链接。不要为统一外观创建无用途目录或复制上游整套流程。通用清单与客户端 UI 配置分开维护；新增客户端专属字段前更新兼容性约定和校验。

## 变更与版本

[VERSION](VERSION) 是四个技能的统一版本号。使用 `主版本.次版本.修订号`：破坏兼容的入口或安装变更升主版本，向后兼容的新能力升次版本，修复升修订号。样例应用自己的包版本和安装收据格式号独立维护。

1. 实际修改时，在 [CHANGELOG.md](CHANGELOG.md) 顶部的 Unreleased 下按实际修改日期（YYYY-MM-DD）记载类别、变化和用户影响。涉及安装路径、依赖或已有数据时附升级办法。
2. 定版时将条目归并到 `## [版本号] - YYYY-MM-DD`，以实际定版日期为准。同步 VERSION、README 和各 SKILL.md 的 `metadata.version`。空的分类或无待发布变更的章节可省略。
3. 运行下面的检查，更新兼容性和验证记录。明确实测对象、环境、方法、结果和未执行项。首次定版的用户可见能力集中写一次，临时下载、清理过程和重复测试输出不进入更新日志。
4. 将通过检查的快照提交并创建同名本地标签，例如 `v1.0.0`。推送和创建 GitHub Release 是另行授权的外部操作。

## 验证与清理

先读 [AGENTS.md](AGENTS.md)。按 [README](README.md) 建立隔离环境，然后从仓库根目录执行：

```powershell
.\.venv\Scripts\python.exe -B scripts\validate.py
.\.venv\Scripts\python.exe -B -m unittest discover -s tests -p "test_*.py" -v
.\.venv\Scripts\python.exe -B scripts\clean.py
```

安装器改动需在隔离目标验证安装、更新、冲突和失败恢复。界面或交付改动按[验证记录](docs/validation.md)复验对应样例。清理先审查绝对路径、链接、引用及候选清单；用途不明的文件保留。

清单或校验器变更需覆盖非法 YAML、重复键、字段类型和长度边界，且复制后的独立包仍可通过校验。修改触发描述时补充容易混淆的正反案例；未实际运行模型的案例只记为待评测，不以单元测试结果代替行为结论。

当前四包将运行环境写入 SKILL.md 正文，头部使用 name、description、license、metadata，以兼容 skill-creator 通用校验器。仓库校验器仍兼容旧包的可选 compatibility 字段。不要删去环境说明或修改宿主工具来获取通过结果。独立包校验同时检查文本格式及 references 的链接可达性；四个真实包的安装、更新和故障恢复已纳入 unittest。

动效资料采用“方法 → 来源导航 → 单站目录”分层：motion.md 负责桌面决策，motion-index.md 只做来源选择，motion-luckymaomi-index.md、motion-lab-index.md、motion-hub-index.md 分别保留各站元数据和许可。调整参考结构时检查调用者和包内可达性，保留已有导航路径；不要仅为缩短行数移动内容。

更新动效快照时，对照 LuckyMaomi 的页面与 animations.json、Motion.Lab 的卡片与 data/effects.ts、Motion Hub（holynova/web-motion-showcase）的目录与 data/motions.js，复核原始 ID、分类、参数、来源提交和许可。Motion Hub 的详情 ID 位于 URL 查询参数，不能按路径末段解析。各来源的 ID 分别排序、以换行连接并取 UTF-8 SHA-256，更新 `tests/test_motion_catalog.py` 的指纹。保留来源命名空间，不按同名 ID 合并；页面抽查、源码核对、目录覆盖和原生运行分别记录。
