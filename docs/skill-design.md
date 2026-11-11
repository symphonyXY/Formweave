# 技能格式与设计依据

适用版本：Formweave 1.0.0。核对日期：2026-11-11。四个技能版本以 VERSION 为准。

## 来源与取舍

先核对官方格式，再阅读高星仓库的实际技能。下列星数来自当日 GitHub REST API 快照，仅用于说明样本关注度，不表示质量排名。链接固定到阅读时的提交，后续复核应重新取样。

| 来源 | 快照与阅读入口 | 在本项目的采用方式 |
|---|---|---|
| Agent Skills | [格式规范](https://agentskills.io/specification) | 使用标准 frontmatter；验证字段类型、名称及长度，metadata 保持字符串映射。 |
| OpenAI | [官方技能文档](https://learn.chatgpt.com/docs/build-skills) | 入口与按需参考分离；Codex UI 配置保留在 agents/openai.yaml。 |
| Claude Code | [官方技能文档](https://code.claude.com/docs/en/skills) | 说明 .claude/skills 安装位置和 /skill-name 调用方式；客户端专属调用控制不混入通用清单。 |
| anthropics/skills | 192,658 stars；[skill-creator](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/skill-creator/SKILL.md) | 借鉴分层读取与评测迭代；明确触发场景，补充可观察的交付判据。 |
| obra/superpowers | 315,906 stars；[writing-skills](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-skills/SKILL.md) | 将能机械判断的格式错误交给校验器；用行为案例检查授权沿用和模式边界。 |
| openai/skills | 28,679 stars；[skill-creator](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/SKILL.md) | 保持入口简短、资源自包含，按任务风险决定流程约束。 |

以上属于设计与技术参考，没有复制第三方代码、模板或素材。上游各目录可能有不同许可，今后复制具体文件时须单独核对其提交中的许可；仓库整体星数或许可摘要不能代替逐文件判断。

未采用上游的跨技能依赖、强制子代理流程和扩大触发范围的写法：四个工作流仍可单独安装，用户的桌面任务和既有确认决定工作范围。无需为四个小型入口再增加插件清单、空目录或包内安装文档。

## 包结构与读取

```text
skills/formweave-<mode>/
├── SKILL.md             标准清单、主要约束、按需参考入口
├── LICENSE              独立分发许可
├── agents/openai.yaml   Codex 展示名称与默认提示词
├── references/          按任务读取的中文资料
├── scripts/             有实际执行需要时提供
└── assets/              有预览或样例需要时提供
```

最后两个目录按实际需要存在，规划和审查不必创建。安装说明、更新日志和维护记录留在仓库根目录及 docs；应用模板放在 assets。技能本身不依赖这些仓库级说明才能执行。所有参考链接从包内解析，共享同名参考保留完全相同的副本。

SKILL.md 的 description 说明任务、触发场景与容易混淆的边界；正文说明授权、资料选择和交付结果。动效索引仅在查具体来源或效果时读取。500 行是官方建议的入口规模上限，不是本项目应写满的目标，也不作为拒绝合法技能的格式规则。

## 校验边界

本项目采用通用 frontmatter 字段集合：name、description、license、compatibility、metadata、allowed-tools。当前技能不预授权任何工具；allowed-tools 的客户端语义仍需单独核对。Claude 专属字段及动态命令注入不会自动加入本包。若未来确有需要，应先调整兼容性约定和校验，再引入适配。

校验器拒绝重复 YAML 键、非映射头部、超长描述、非字符串 metadata、错误的 UI 字段与伪布尔值；名称允许最多 64 字符。UTF-8 无 BOM、LF、末尾一个换行和无行尾空白是本仓库格式约定，并非所有客户端都强制的标准。

静态校验能发现结构问题，无法证明 Agent 会正确选用技能。行为评测使用[案例集与执行方法](../evals/README.md)；安装完整性、实际模型行为、原生应用运行和客户端技能选择分别记录，证据见[验证记录](validation.md)。
