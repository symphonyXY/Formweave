# LuckyMaomi 动效索引 · 57 项

用户指定 LuckyMaomi 或其具体效果时读取。返回[来源导航](motion-index.md)；策略含义与验收见[动效决策](motion.md)。

2026-11-04 核对页面与 [animations.json](https://github.com/luckymaomi/ui/blob/2efa31f91bda58f4766e1c9166134ea20eab944a/src/content/data/animations.json)，提交 `2efa31f91bda58f4766e1c9166134ea20eab944a`。这里保留名称、原始 ID、触发和时长，桌面策略为 Formweave 建议；不代表全部效果已移植或完成原生验收。

按中文名、ID 或策略搜索下表；需要词汇与鼠标案例时再读文末“配套入口”。

原站的触发方式与时长用于识别演示。continuous 代表持续响应；各项目应根据任务决定是否安排过渡。

## 入场 · 9

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [淡入上滑](https://luckymaomi.github.io/ui/animations/fade-in-up/) | `fade-in-up` | on-mount / 600ms | 内容切换 |
| [缩放淡入](https://luckymaomi.github.io/ui/animations/scale-in/) | `scale-in` | on-mount / 400ms | 层级开合 |
| [淡入下滑](https://luckymaomi.github.io/ui/animations/fade-in-down/) | `fade-in-down` | on-mount / 600ms | 内容切换 |
| [左侧滑入](https://luckymaomi.github.io/ui/animations/slide-in-left/) | `slide-in-left` | on-mount / 500ms | 层级开合 |
| [弹性入场](https://luckymaomi.github.io/ui/animations/bounce-in/) | `bounce-in` | on-mount / 600ms | 专项展示 |
| [右侧滑入](https://luckymaomi.github.io/ui/animations/slide-in-right/) | `slide-in-right` | on-mount / 500ms | 层级开合 |
| [旋转入场](https://luckymaomi.github.io/ui/animations/rotate-in/) | `rotate-in` | on-mount / 500ms | 专项展示 |
| [远景拉近](https://luckymaomi.github.io/ui/animations/zoom-in/) | `zoom-in` | on-mount / 500ms | 专项展示 |
| [弹簧缩放](https://luckymaomi.github.io/ui/animations/elastic-scale/) | `elastic-scale` | on-mount / 800ms | 专项展示 |

## 悬停 · 6

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [悬浮抬升](https://luckymaomi.github.io/ui/animations/hover-lift/) | `hover-lift` | on-hover / 200ms | 控件反馈 |
| [悬浮发光](https://luckymaomi.github.io/ui/animations/hover-glow/) | `hover-glow` | on-hover / 300ms | 控件反馈 |
| [3D 卡片翻转](https://luckymaomi.github.io/ui/animations/flip-card/) | `flip-card` | on-hover / 600ms | 专项展示 |
| [边框描边](https://luckymaomi.github.io/ui/animations/border-trace/) | `border-trace` | on-hover / 600ms | 控件反馈 |
| [下划线绘制](https://luckymaomi.github.io/ui/animations/underline-draw/) | `underline-draw` | on-hover / 300ms | 控件反馈 |
| [3D 透视倾斜](https://luckymaomi.github.io/ui/animations/tilt-3d/) | `tilt-3d` | on-hover / continuous | 专项展示 |

## 文字 · 7

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [打字机效果](https://luckymaomi.github.io/ui/animations/typewriter/) | `typewriter` | on-mount / 3s | 装饰留档 |
| [文字渐变流动](https://luckymaomi.github.io/ui/animations/text-gradient-flow/) | `text-gradient-flow` | continuous / 3s | 装饰留档 |
| [数字滚动](https://luckymaomi.github.io/ui/animations/counter-roll/) | `counter-roll` | on-scroll / 2s | 数值进度 |
| [跑马灯滚动](https://luckymaomi.github.io/ui/animations/marquee-scroll/) | `marquee-scroll` | continuous / 20s | 装饰留档 |
| [故障文字](https://luckymaomi.github.io/ui/animations/glitch-text/) | `glitch-text` | continuous / 3s | 装饰留档 |
| [文字揭示](https://luckymaomi.github.io/ui/animations/text-reveal/) | `text-reveal` | on-scroll / 800ms | 专项展示 |
| [文字解密](https://luckymaomi.github.io/ui/animations/text-scramble/) | `text-scramble` | on-mount / 1.5s | 装饰留档 |

## 加载 · 4

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [骨架屏脉冲](https://luckymaomi.github.io/ui/animations/skeleton-pulse/) | `skeleton-pulse` | continuous / 2s | 任务等待 |
| [三点弹跳加载](https://luckymaomi.github.io/ui/animations/spinner-dots/) | `spinner-dots` | continuous / 1.4s | 任务等待 |
| [微光扫过](https://luckymaomi.github.io/ui/animations/shimmer/) | `shimmer` | continuous / 2s | 任务等待 |
| [进度条加载](https://luckymaomi.github.io/ui/animations/progress-bar/) | `progress-bar` | continuous / 2s | 数值进度 |

## 滚动 · 4

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [滚动显现](https://luckymaomi.github.io/ui/animations/scroll-reveal/) | `scroll-reveal` | on-scroll / 600ms | 分组呈现 |
| [视差浮动](https://luckymaomi.github.io/ui/animations/parallax-float/) | `parallax-float` | on-scroll / continuous | 专项展示 |
| [滚动翻页](https://luckymaomi.github.io/ui/animations/scroll-page-turn/) | `scroll-page-turn` | on-scroll / continuous | 专项展示 |
| [滚动剥离](https://luckymaomi.github.io/ui/animations/scroll-peel-away/) | `scroll-peel-away` | on-scroll / continuous | 专项展示 |

## 背景 · 2

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [背景渐变流动](https://luckymaomi.github.io/ui/animations/background-gradient-shift/) | `background-gradient-shift` | continuous / 8s | 装饰留档 |
| [形状变形](https://luckymaomi.github.io/ui/animations/morph-shape/) | `morph-shape` | continuous / 8s | 专项展示 |

## 微交互 · 9

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [子元素错开动画](https://luckymaomi.github.io/ui/animations/stagger-children/) | `stagger-children` | on-mount / 500ms | 分组呈现 |
| [抖动提示](https://luckymaomi.github.io/ui/animations/shake/) | `shake` | on-click / 500ms | 操作回执 |
| [脉搏跳动](https://luckymaomi.github.io/ui/animations/pulse/) | `pulse` | continuous / 2s | 装饰留档 |
| [弹性回弹](https://luckymaomi.github.io/ui/animations/elastic-snap/) | `elastic-snap` | on-click / 800ms | 装饰留档 |
| [脉冲光环](https://luckymaomi.github.io/ui/animations/pulse-ring/) | `pulse-ring` | continuous / 2s | 装饰留档 |
| [彩纸爆炸](https://luckymaomi.github.io/ui/animations/confetti-burst/) | `confetti-burst` | on-click / 1.2s | 专项展示 |
| [聚光灯卡片](https://luckymaomi.github.io/ui/animations/spotlight-card/) | `spotlight-card` | on-hover / continuous | 装饰留档 |
| [磁吸悬浮](https://luckymaomi.github.io/ui/animations/magnetic-hover/) | `magnetic-hover` | on-hover / continuous | 装饰留档 |
| [涟漪点击](https://luckymaomi.github.io/ui/animations/ripple-click/) | `ripple-click` | on-click / 600ms | 控件反馈 |

## 转场 · 4

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [模糊到清晰](https://luckymaomi.github.io/ui/animations/blur-in/) | `blur-in` | on-mount / 500ms | 内容切换 |
| [交叉淡化](https://luckymaomi.github.io/ui/animations/crossfade/) | `crossfade` | manual / 500ms | 内容切换 |
| [滑动切换](https://luckymaomi.github.io/ui/animations/slide-swap/) | `slide-swap` | manual / 400ms | 层级开合 |
| [形态过渡](https://luckymaomi.github.io/ui/animations/morph-transition/) | `morph-transition` | continuous / 600ms | 层级开合 |

## 指针 · 8

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [光晕指针](https://luckymaomi.github.io/ui/animations/cursor-aura/) | `cursor-aura` | continuous / continuous | 装饰留档 |
| [指针轨迹](https://luckymaomi.github.io/ui/animations/cursor-trail/) | `cursor-trail` | continuous / continuous | 装饰留档 |
| [靠近显现](https://luckymaomi.github.io/ui/animations/proximity-reveal/) | `proximity-reveal` | on-hover / 180ms | 定点操控 |
| [文字排斥](https://luckymaomi.github.io/ui/animations/text-repulsion/) | `text-repulsion` | continuous / continuous | 装饰留档 |
| [图像扭曲](https://luckymaomi.github.io/ui/animations/image-distortion/) | `image-distortion` | continuous / continuous | 专项展示 |
| [鼠标视差层](https://luckymaomi.github.io/ui/animations/parallax-layers/) | `parallax-layers` | continuous / continuous | 专项展示 |
| [拖拽物理](https://luckymaomi.github.io/ui/animations/drag-physics/) | `drag-physics` | manual / continuous | 定点操控 |
| [上下文光标](https://luckymaomi.github.io/ui/animations/context-cursor/) | `context-cursor` | on-hover / continuous | 定点操控 |

## 离场 · 4

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [淡出下滑](https://luckymaomi.github.io/ui/animations/fade-out-down/) | `fade-out-down` | manual / 400ms | 层级开合 |
| [缩放消失](https://luckymaomi.github.io/ui/animations/scale-out/) | `scale-out` | on-click / 300ms | 层级开合 |
| [右侧滑出](https://luckymaomi.github.io/ui/animations/slide-out-right/) | `slide-out-right` | on-click / 400ms | 层级开合 |
| [折叠收起](https://luckymaomi.github.io/ui/animations/collapse/) | `collapse` | on-click / 350ms | 层级开合 |

## 配套入口

[动效词汇表](https://luckymaomi.github.io/ui/animations/vocabulary/)含 12 组、48 个术语。沟通需求时可以用以下原始术语定位时间、对象与退场；它们不计入 57 个效果。

- **entrances-exits**　fade-in, slide-in, scale-in, pop-in, reveal, fade-out
- **sequencing-timing**　keyframes, stagger, delay, duration
- **movement-transforms**　translate, scale, rotate, tilt-3d
- **transitions**　crossfade, morph, layout, accordion
- **scroll**　scroll-reveal, scroll-driven, parallax, marquee
- **feedback-interaction**　hover, press, shake, ripple
- **easing**　ease-out, ease-in, ease-in-out, cubic-bezier
- **spring**　spring, stiffness, damping, bounce
- **looping-ambient**　loop, pulse, shimmer, float
- **polish-effects**　blur, clip-path, line-drawing, typewriter
- **performance**　frame-rate, compositor, gpu-accelerated
- **principles**　purposeful, anticipation, perceived-performance

[鼠标交互实验室](https://luckymaomi.github.io/ui/mouse-interactions/)的 17 个房间展示了 47 个交互标签。用房间编号查原例。定点拖放与靠近显现可参考「定点操控」；磁吸、追踪和表面折射通常按「装饰留档」处理。房间用于观察输入与反馈，不改变桌面应用类型。

- **01 · 新野兽派**　双向磁吸 CTA、惯性拖拽卡片、区域状态光标
- **02 · 玻璃拟态**　环境光晕跟随、视差深度层、玻璃聚光灯 + 区域切换
- **03 · 杂志编辑**　衬线逐字排斥、墨点轨迹、靠近浮现操作
- **04 · 赛博朋克霓虹**　RGB 通道分离、扫描线跟随、霓虹点轨迹
- **05 · 新拟态**　压凹表面、磁吸软按钮、环境柔光
- **06 · 包豪斯**　磁吸原色按钮、3D 倾斜方块
- **07 · 装饰艺术**　镜像金光晕、金色环境光、金粉轨迹
- **08 · 蒸汽波**　粉色扫描线跟随、RGB 分裂光标、品红粉尘轨迹
- **09 · 液态玻璃**　液态形变光斑、折射光晕、玻璃聚光灯
- **10 · 黏土拟态**　黏土挤压、柔压凹、磁吸圆按钮
- **11 · 粗野主义**　红色涟漪波、磁吸文字链接、红色聚光灯
- **12 · 反设计**　彩纸喷射、RGB 故障分裂、酸绿轨迹
- **13 · 构成主义**　旋转红徽章、几何碎片星座
- **14 · 瑞士海报**　透视网格、微妙 3D 倾斜
- **15 · 漫画风**　放射速度线、粗壮 3D 倾斜、半调点轨迹
- **16 · 拼贴艺术**　多层纸片视差、撕纸深度
- **17 · 酸性图形**　液态铬光斑、酸性 RGB 分裂、扫描线溢出

## 来源与许可

LuckyMaomi 的[许可原文](https://github.com/luckymaomi/ui/blob/2efa31f91bda58f4766e1c9166134ea20eab944a/LICENSE)随本包所列目录元数据保留如下。

```text
MIT License

Copyright (c) 2026 luckymaomi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
