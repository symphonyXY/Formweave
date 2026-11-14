# 技能格式与设计依据

适用版本：Formweave 1.0.0。核对日期：2026-11-11。四个技能版本以 VERSION 为准。

## 未定版的结构与语言整理 · 2026-11-14

本次按 skill-creator 的原则整理入口与参考资料：入口保留执行方式、必要约束和交付条件；按需参考说明“何时读取、用于什么决策”。四个入口分别服务规划、预览、开发、审查，保留原有任务边界和应用写入前的确认要求。目录名、清单名称及安装命令保持兼容。

| 内容 | 维护位置 | 读取条件 |
|---|---|---|
| 任务范围与交付 | 各包 SKILL.md | 进入相应工作流时读取。 |
| 决策与实施方法 | references 中的范围、选型、桌面设计、动效、性能和交付资料 | 只读取当前阶段所需的部分。 |
| 动效来源选择 | references/motion-index.md | 需要具体来源时读取，导航本身不承载完整目录。 |
| 三站事实索引及许可 | motion-luckymaomi-index.md、motion-lab-index.md、motion-hub-index.md | 按来源分别读取或搜索；各目录保留提交、元数据及许可说明。 |
| 可复用产物与运行工具 | assets、scripts | 仅在需要相应样例或确定性操作时使用。 |
| 历史检查、安装说明和维护依据 | 仓库 docs、README、CONTRIBUTING | 维护仓库时读取，安装后的独立技能不依赖这些文件。 |

中文正文使用直接的动作和可观察结果。保留 API、命令、参数与英文标识符；术语出现时说明其对当前决策的意义。区分事实、建议起点与待验证项，减少重复的禁止句和固定数量要求：无需为了形式凑候选、让用户填写所有字段或生成多种预览载体。会影响授权、数据和交付的约束仍保留明确条件。

共享资料在独立包中保留相同副本，不建立跨包路径。拆分长目录时保留原导航路径、条目、来源与许可，并检查新资料能够从入口发现。目录覆盖、静态格式和模型行为分别验证，不以文字整理推断触发或执行效果已改善。

## 来源与取舍

以下是 2026-11-11 留存的格式与写作依据，链接固定到当时阅读的提交。保留与本仓库有关的取舍，不以仓库关注度判断技能质量。

| 来源 | 快照与阅读入口 | 在本项目的采用方式 |
|---|---|---|
| Agent Skills | [格式规范](https://agentskills.io/specification) | 使用标准 frontmatter；验证字段类型、名称及长度，metadata 保持字符串映射。 |
| OpenAI | [官方技能文档](https://learn.chatgpt.com/docs/build-skills) | 入口与按需参考分离；Codex UI 配置保留在 agents/openai.yaml。 |
| Claude Code | [官方技能文档](https://code.claude.com/docs/en/skills) | 说明 .claude/skills 安装位置和 /skill-name 调用方式；客户端专属调用控制不混入通用清单。 |
| anthropics/skills | [skill-creator](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/skill-creator/SKILL.md) | 借鉴分层读取与评测迭代；明确触发场景，补充可观察的交付判据。 |
| obra/superpowers | [writing-skills](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-skills/SKILL.md) | 将能机械判断的格式错误交给校验器；用行为案例检查授权沿用和模式边界。 |
| openai/skills | [skill-creator](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/SKILL.md) | 保持入口简短、资源自包含，按任务风险决定流程约束。 |

以上属于设计与技术参考，没有复制第三方代码、模板或素材。上游各目录可能有不同许可，今后复制具体文件时须单独核对其提交中的许可；仓库整体的许可摘要不能代替逐文件判断。

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

仓库校验器接受通用 frontmatter 字段集合：name、description、license、compatibility、metadata、allowed-tools。当前四包仅使用 name、description、license、metadata，将环境要求保留在正文，以兼容 skill-creator 较窄的校验白名单；这不是把合法的 compatibility 字段判为无效。当前技能不预授权工具，allowed-tools 的客户端语义仍需单独核对。Claude 专属字段及动态命令注入不会自动加入本包。

校验器拒绝重复 YAML 键、非映射头部、超长描述、非字符串 metadata、错误的 UI 字段与伪布尔值；名称允许最多 64 字符。UTF-8 无 BOM、LF、末尾一个换行和无行尾空白是本仓库格式约定，仓库与独立包均检查；这些并非所有客户端都强制的标准。references 中的 Markdown 资料须能沿包内链接从 SKILL.md 到达，允许循环引用但不允许无入口的参考文件。

静态校验能发现结构问题，无法证明 Agent 会正确选用技能。行为评测使用[案例集与执行方法](../evals/README.md)；安装完整性、实际模型行为、原生应用运行和客户端技能选择分别记录，证据见[验证记录](validation.md)。
