# 贡献指南

## 修改流程

1. 阅读 [AGENTS.md](AGENTS.md) 和受影响技能的入口及相关资料。直接修改现有正式文件，不维护并行草稿、不复制整套目录为新版本。
2. 改动涉及共享参考时，同步所有同名副本并保持字节一致。包内引用只能指向本包。第三方资料优先链接固定版本；复制内容时保留对应许可证和署名。
3. 在 [CHANGELOG.md](CHANGELOG.md) 的 `Unreleased` 按实际日期记录用户影响和升级注意事项，同步中英文用法与[兼容性说明](docs/compatibility.md)。仅在待定版条目存在时保留该章节。
4. 复验受影响的流程，记录测试对象、环境、结果和未执行项。任务结束前按[清理规则](#任务收尾)移除不交付的临时产物。

## 目录和文案

| 目录 | 放什么 |
|---|---|
| `skills/` | 四个独立技能：`SKILL.md`、包内资料、可用样例、工具及许可证。 |
| `scripts/`、`tests/` | 仓库维护工具与回归测试。 |
| `evals/`、`docs/evidence/` | 行为案例与证据，以及验证记录引用的原始测量和截图。 |

文本为 UTF-8 无 BOM、LF、末尾一个换行；其他格式按 [.editorconfig](.editorconfig) 和 [.gitattributes](.gitattributes)。说明用简体中文，技能和程序标识符用英文；文档链接用仓库相对路径。README 面向第一次使用者，安装或运行命令必须对应实际入口。用明确的动词区分「只读检查」「实现」「发布」，区分「目标」「实测」「未验证」，不要用界面截图替代运行证据。

## 验证

在仓库根目录运行：

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -B scripts\validate.py
.\.venv\Scripts\python.exe -B -m unittest discover -s tests -p "test_*.py" -v
git diff --check
```

安装器改动在隔离目标验证安装、更新、冲突和失败恢复。界面或交付改动复验对应样例；修改触发描述时用[行为案例](evals/README.md)区分容易混淆的正反任务。没有实际运行的案例记作待评测，不以静态和单元测试代替。交互、原生运行与实测记录见[验证记录](docs/validation.md)。

修改动效索引时保留来源命名空间、精确 ID、版本与许可；Motion Hub 的详情 ID 在查询参数中。对照上游更新 [索引回归测试](tests/test_motion_catalog.py) 的 ID 集合及指纹。页面抽查与原生效果实测分别记录。

## 任务收尾

每次任务先预览 `.\.venv\Scripts\python.exe -B scripts\clean.py`。脚本只识别有对应源码、与当前解释器匹配的字节码；清单无误后才可带 `--apply` 与当次摘要执行。其他临时产物先列绝对路径，核对来源、链接及引用，再清理本次生成、可重建且不交付的文件。不要用通配符清整仓库；用途不明的文件、有效测试、许可证、交付物和证据都保留。

## 安装冲突与恢复

无收据、收据格式错误、已安装包有本地修改或锁仍存在时，不覆盖目录。先核对目标路径和锁记录，确认进程已停止；比较同级 `.formweave-stage-*` 下的 `previous`、`new` 与实际目标。只有目标缺失且 `previous` 完整时才恢复为目标名。恢复后先用对应源码验证，再用拟安装源码执行 `update`、`verify`。不要伪造收据来接受本地差异。

## 定版与远端

[VERSION](VERSION) 是四个技能的统一版本号；样例应用的版本与安装收据格式号独立维护。后续按主版本、次版本、修订号递增。定版时归并 `Unreleased`，按实际日期新增发布条目，并同步 VERSION、双语 README 和四个 SKILL.md 的 `metadata.version`。检查通过后按批准范围提交并建立本地版本标签。

本地定版不自动发布 GitHub。推送分支或标签、创建 PR 或 Release 都须另行授权；遇到远端历史不匹配，不擅自强推。
