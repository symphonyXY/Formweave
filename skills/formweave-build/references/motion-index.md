# 桌面动效来源索引

按来源和原始 ID 查找，一行对应一个公开目录条目。策略列为织形针对 Windows 桌面应用的选择；操作时序、降级方法与验收条件见[动效决策指南](motion.md)。同一方法在两个来源可能重复，同名 ID 保留各自含义。可离线查阅，打开上游原例时才需要联网。

2026-11-04 核对。LuckyMaomi 的页面链接与 [57 条定义](https://github.com/luckymaomi/ui/blob/2efa31f91bda58f4766e1c9166134ea20eab944a/src/content/data/animations.json)逐项对齐。Motion.Lab 的 160 张公开卡片与[同版本效果定义](https://github.com/yangxu128/Motion.Lab/blob/fbfda036aadbc1b46547bce8a7a57ec12bf73485/data/effects.ts)逐项对齐。记录标识、分类和参数元数据；不复制示例实现、素材或提示词。网站示例并未逐个移植或在 Windows 原生框架上测帧。

## LuckyMaomi · 57 项

原站的触发方式与时长用于识别演示。continuous 代表持续响应；各项目应根据任务决定是否安排过渡。

### 入场

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

### 悬停

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [悬浮抬升](https://luckymaomi.github.io/ui/animations/hover-lift/) | `hover-lift` | on-hover / 200ms | 控件反馈 |
| [悬浮发光](https://luckymaomi.github.io/ui/animations/hover-glow/) | `hover-glow` | on-hover / 300ms | 控件反馈 |
| [3D 卡片翻转](https://luckymaomi.github.io/ui/animations/flip-card/) | `flip-card` | on-hover / 600ms | 专项展示 |
| [边框描边](https://luckymaomi.github.io/ui/animations/border-trace/) | `border-trace` | on-hover / 600ms | 控件反馈 |
| [下划线绘制](https://luckymaomi.github.io/ui/animations/underline-draw/) | `underline-draw` | on-hover / 300ms | 控件反馈 |

### 文字

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [打字机效果](https://luckymaomi.github.io/ui/animations/typewriter/) | `typewriter` | on-mount / 3s | 装饰留档 |
| [文字渐变流动](https://luckymaomi.github.io/ui/animations/text-gradient-flow/) | `text-gradient-flow` | continuous / 3s | 装饰留档 |
| [数字滚动](https://luckymaomi.github.io/ui/animations/counter-roll/) | `counter-roll` | on-scroll / 2s | 数值进度 |
| [跑马灯滚动](https://luckymaomi.github.io/ui/animations/marquee-scroll/) | `marquee-scroll` | continuous / 20s | 装饰留档 |
| [故障文字](https://luckymaomi.github.io/ui/animations/glitch-text/) | `glitch-text` | continuous / 3s | 装饰留档 |
| [文字揭示](https://luckymaomi.github.io/ui/animations/text-reveal/) | `text-reveal` | on-scroll / 800ms | 专项展示 |
| [文字解密](https://luckymaomi.github.io/ui/animations/text-scramble/) | `text-scramble` | on-mount / 1.5s | 装饰留档 |

### 加载

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [骨架屏脉冲](https://luckymaomi.github.io/ui/animations/skeleton-pulse/) | `skeleton-pulse` | continuous / 2s | 任务等待 |
| [三点弹跳加载](https://luckymaomi.github.io/ui/animations/spinner-dots/) | `spinner-dots` | continuous / 1.4s | 任务等待 |
| [微光扫过](https://luckymaomi.github.io/ui/animations/shimmer/) | `shimmer` | continuous / 2s | 任务等待 |
| [进度条加载](https://luckymaomi.github.io/ui/animations/progress-bar/) | `progress-bar` | continuous / 2s | 数值进度 |

### 滚动

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [滚动显现](https://luckymaomi.github.io/ui/animations/scroll-reveal/) | `scroll-reveal` | on-scroll / 600ms | 分组呈现 |
| [视差浮动](https://luckymaomi.github.io/ui/animations/parallax-float/) | `parallax-float` | on-scroll / continuous | 专项展示 |
| [滚动翻页](https://luckymaomi.github.io/ui/animations/scroll-page-turn/) | `scroll-page-turn` | on-scroll / continuous | 专项展示 |
| [滚动剥离](https://luckymaomi.github.io/ui/animations/scroll-peel-away/) | `scroll-peel-away` | on-scroll / continuous | 专项展示 |

### 背景

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [背景渐变流动](https://luckymaomi.github.io/ui/animations/background-gradient-shift/) | `background-gradient-shift` | continuous / 8s | 装饰留档 |
| [形状变形](https://luckymaomi.github.io/ui/animations/morph-shape/) | `morph-shape` | continuous / 8s | 专项展示 |

### 微交互

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [子元素错开动画](https://luckymaomi.github.io/ui/animations/stagger-children/) | `stagger-children` | on-mount / 500ms | 分组呈现 |
| [抖动提示](https://luckymaomi.github.io/ui/animations/shake/) | `shake` | on-click / 500ms | 操作回执 |
| [脉搏跳动](https://luckymaomi.github.io/ui/animations/pulse/) | `pulse` | continuous / 2s | 装饰留档 |
| [弹性回弹](https://luckymaomi.github.io/ui/animations/elastic-snap/) | `elastic-snap` | on-click / 800ms | 装饰留档 |
| [脉冲光环](https://luckymaomi.github.io/ui/animations/pulse-ring/) | `pulse-ring` | continuous / 2s | 装饰留档 |
| [彩纸爆炸](https://luckymaomi.github.io/ui/animations/confetti-burst/) | `confetti-burst` | on-click / 1.2s | 专项展示 |

### 转场

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [模糊到清晰](https://luckymaomi.github.io/ui/animations/blur-in/) | `blur-in` | on-mount / 500ms | 内容切换 |
| [交叉淡化](https://luckymaomi.github.io/ui/animations/crossfade/) | `crossfade` | manual / 500ms | 内容切换 |
| [滑动切换](https://luckymaomi.github.io/ui/animations/slide-swap/) | `slide-swap` | manual / 400ms | 层级开合 |
| [形态过渡](https://luckymaomi.github.io/ui/animations/morph-transition/) | `morph-transition` | continuous / 600ms | 层级开合 |

### 微交互

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [聚光灯卡片](https://luckymaomi.github.io/ui/animations/spotlight-card/) | `spotlight-card` | on-hover / continuous | 装饰留档 |
| [磁吸悬浮](https://luckymaomi.github.io/ui/animations/magnetic-hover/) | `magnetic-hover` | on-hover / continuous | 装饰留档 |
| [涟漪点击](https://luckymaomi.github.io/ui/animations/ripple-click/) | `ripple-click` | on-click / 600ms | 控件反馈 |

### 指针

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

### 悬停

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [3D 透视倾斜](https://luckymaomi.github.io/ui/animations/tilt-3d/) | `tilt-3d` | on-hover / continuous | 专项展示 |

### 离场

| 原例 | ID | 网站触发 / 时长 | 桌面策略 |
|---|---|---|---|
| [淡出下滑](https://luckymaomi.github.io/ui/animations/fade-out-down/) | `fade-out-down` | manual / 400ms | 层级开合 |
| [缩放消失](https://luckymaomi.github.io/ui/animations/scale-out/) | `scale-out` | on-click / 300ms | 层级开合 |
| [右侧滑出](https://luckymaomi.github.io/ui/animations/slide-out-right/) | `slide-out-right` | on-click / 400ms | 层级开合 |
| [折叠收起](https://luckymaomi.github.io/ui/animations/collapse/) | `collapse` | on-click / 350ms | 层级开合 |

## Motion.Lab · 160 项

参数列是每张卡公开的可调字段；单位、范围和默认值见对应原例。是否需要 JS、GPU 或新依赖由目标实现决定。例如 lottie-checkmark 的来源定义采用 SVG 表达完成反馈。

### 基础 · 42

| 原例 | ID | 可调字段 | 桌面策略 |
|---|---|---|---|
| [淡入](https://motionlab.uanx.online/lab/fade-in) | `fade-in` | duration, delay | 内容切换 |
| [上滑淡入](https://motionlab.uanx.online/lab/fade-in-up) | `fade-in-up` | duration, distance | 内容切换 |
| [左侧滑入](https://motionlab.uanx.online/lab/slide-in-left) | `slide-in-left` | duration | 层级开合 |
| [右侧滑入](https://motionlab.uanx.online/lab/slide-in-right) | `slide-in-right` | duration | 层级开合 |
| [缩放弹跳](https://motionlab.uanx.online/lab/zoom-bounce) | `zoom-bounce` | duration | 专项展示 |
| [水平翻转](https://motionlab.uanx.online/lab/flip-x) | `flip-x` | duration | 专项展示 |
| [旋转入场](https://motionlab.uanx.online/lab/rotate-in) | `rotate-in` | duration | 专项展示 |
| [脉冲](https://motionlab.uanx.online/lab/pulse) | `pulse` | duration, intensity | 装饰留档 |
| [摇晃](https://motionlab.uanx.online/lab/shake) | `shake` | duration | 操作回执 |
| [心跳](https://motionlab.uanx.online/lab/heartbeat) | `heartbeat` | duration | 装饰留档 |
| [跑马灯](https://motionlab.uanx.online/lab/marquee) | `marquee` | duration, direction | 装饰留档 |
| [加载旋转](https://motionlab.uanx.online/lab/spinner) | `spinner` | duration | 任务等待 |
| [上滑入场](https://motionlab.uanx.online/lab/slide-up) | `slide-up` | duration, distance | 内容切换 |
| [下滑入场](https://motionlab.uanx.online/lab/slide-down) | `slide-down` | duration, distance | 内容切换 |
| [弹跳入场](https://motionlab.uanx.online/lab/bounce-in) | `bounce-in` | duration | 专项展示 |
| [弹性入场](https://motionlab.uanx.online/lab/elastic-in) | `elastic-in` | duration | 专项展示 |
| [淡出消失](https://motionlab.uanx.online/lab/fade-out) | `fade-out` | duration | 层级开合 |
| [缩放呼吸](https://motionlab.uanx.online/lab/scale-pulse) | `scale-pulse` | duration, min, max | 装饰留档 |
| [持续旋转](https://motionlab.uanx.online/lab/rotate-360) | `rotate-360` | duration | 装饰留档 |
| [钟摆](https://motionlab.uanx.online/lab/swing) | `swing` | duration | 装饰留档 |
| [果冻](https://motionlab.uanx.online/lab/jello) | `jello` | duration | 装饰留档 |
| [闪烁](https://motionlab.uanx.online/lab/flash) | `flash` | duration, color | 装饰留档 |
| [上方淡入](https://motionlab.uanx.online/lab/fade-in-down) | `fade-in-down` | duration, distance | 内容切换 |
| [左侧淡入](https://motionlab.uanx.online/lab/fade-in-left) | `fade-in-left` | duration, distance | 内容切换 |
| [右侧淡入](https://motionlab.uanx.online/lab/fade-in-right) | `fade-in-right` | duration, distance | 内容切换 |
| [缩放入场](https://motionlab.uanx.online/lab/scale-in) | `scale-in` | duration, from | 内容切换 |
| [缩小归位](https://motionlab.uanx.online/lab/scale-out) | `scale-out` | duration, from | 内容切换 |
| [垂直翻转](https://motionlab.uanx.online/lab/flip-y) | `flip-y` | duration | 专项展示 |
| [3D 翻转](https://motionlab.uanx.online/lab/flip-in-3d) | `flip-in-3d` | duration | 专项展示 |
| [摇摆](https://motionlab.uanx.online/lab/wobble) | `wobble` | duration | 装饰留档 |
| [庆祝抖动](https://motionlab.uanx.online/lab/tada) | `tada` | duration | 装饰留档 |
| [向下弹跳](https://motionlab.uanx.online/lab/bounce-down) | `bounce-down` | duration, distance | 专项展示 |
| [角落滑入](https://motionlab.uanx.online/lab/slide-fade-corner) | `slide-fade-corner` | duration | 专项展示 |
| [倾斜入场](https://motionlab.uanx.online/lab/skew-in) | `skew-in` | duration, angle | 专项展示 |
| [模糊入场](https://motionlab.uanx.online/lab/blur-in) | `blur-in` | duration, blur | 内容切换 |
| [模糊呼吸](https://motionlab.uanx.online/lab/blur-out) | `blur-out` | duration, blur | 装饰留档 |
| [灰度入场](https://motionlab.uanx.online/lab/grayscale-in) | `grayscale-in` | duration | 专项展示 |
| [色彩循环](https://motionlab.uanx.online/lab/color-cycle) | `color-cycle` | duration | 装饰留档 |
| [边框画出](https://motionlab.uanx.online/lab/border-draw) | `border-draw` | duration | 控件反馈 |
| [阴影生长](https://motionlab.uanx.online/lab/shadow-grow) | `shadow-grow` | duration | 装饰留档 |
| [渐变流动](https://motionlab.uanx.online/lab/gradient-shift) | `gradient-shift` | duration | 装饰留档 |
| [光标打字](https://motionlab.uanx.online/lab/typewriter-cursor) | `typewriter-cursor` | speed | 装饰留档 |

### 文字 · 40

| 原例 | ID | 可调字段 | 桌面策略 |
|---|---|---|---|
| [打字机](https://motionlab.uanx.online/lab/typewriter) | `typewriter` | speed | 装饰留档 |
| [波浪文字](https://motionlab.uanx.online/lab/wave-text) | `wave-text` | duration | 装饰留档 |
| [遮罩揭示](https://motionlab.uanx.online/lab/mask-reveal) | `mask-reveal` | duration | 专项展示 |
| [字符分裂](https://motionlab.uanx.online/lab/split-char) | `split-char` | duration | 专项展示 |
| [渐变文字](https://motionlab.uanx.online/lab/gradient-text) | `gradient-text` | duration | 装饰留档 |
| [故障文字](https://motionlab.uanx.online/lab/glitch-text) | `glitch-text` | duration | 装饰留档 |
| [乱码解码](https://motionlab.uanx.online/lab/scramble) | `scramble` | duration | 装饰留档 |
| [数字滚动](https://motionlab.uanx.online/lab/count-up) | `count-up` | target | 数值进度 |
| [错落淡入](https://motionlab.uanx.online/lab/stagger-fade) | `stagger-fade` | duration, stagger | 分组呈现 |
| [垂直跑马灯](https://motionlab.uanx.online/lab/vertical-marquee) | `vertical-marquee` | duration | 装饰留档 |
| [阴影偏移](https://motionlab.uanx.online/lab/text-shadow-shift) | `text-shadow-shift` | duration, intensity | 装饰留档 |
| [3D 文字](https://motionlab.uanx.online/lab/text-3d) | `text-3d` | layers, depth | 装饰留档 |
| [字符旋转](https://motionlab.uanx.online/lab/text-rotate-in) | `text-rotate-in` | duration, stagger | 装饰留档 |
| [字距呼吸](https://motionlab.uanx.online/lab/letter-spacing-wave) | `letter-spacing-wave` | duration, max | 装饰留档 |
| [下划线](https://motionlab.uanx.online/lab/underline-draw) | `underline-draw` | duration | 控件反馈 |
| [高亮扫过](https://motionlab.uanx.online/lab/highlight-sweep) | `highlight-sweep` | duration | 操作回执 |
| [闪烁光标](https://motionlab.uanx.online/lab/text-blink-cursor) | `text-blink-cursor` | speed | 装饰留档 |
| [彩虹文字](https://motionlab.uanx.online/lab/rainbow-text) | `rainbow-text` | duration | 装饰留档 |
| [3D 翻面](https://motionlab.uanx.online/lab/text-flip-3d) | `text-flip-3d` | duration | 装饰留档 |
| [数字翻牌](https://motionlab.uanx.online/lab/number-marquee) | `number-marquee` | speed | 数值进度 |
| [文字上滑](https://motionlab.uanx.online/lab/text-fade-up) | `text-fade-up` | duration, distance | 专项展示 |
| [文字左滑](https://motionlab.uanx.online/lab/text-slide-left) | `text-slide-left` | duration, distance | 专项展示 |
| [文字缩放](https://motionlab.uanx.online/lab/text-zoom-in) | `text-zoom-in` | duration | 专项展示 |
| [模糊揭示](https://motionlab.uanx.online/lab/text-blur-reveal) | `text-blur-reveal` | duration | 专项展示 |
| [RGB 故障](https://motionlab.uanx.online/lab/text-glitch-rgb) | `text-glitch-rgb` | duration | 装饰留档 |
| [霓虹发光](https://motionlab.uanx.online/lab/text-neon) | `text-neon` | duration | 装饰留档 |
| [火焰文字](https://motionlab.uanx.online/lab/text-fire) | `text-fire` | duration | 装饰留档 |
| [冰霜文字](https://motionlab.uanx.online/lab/text-ice) | `text-ice` | duration | 装饰留档 |
| [金属质感](https://motionlab.uanx.online/lab/text-metallic) | `text-metallic` | duration | 装饰留档 |
| [描边文字](https://motionlab.uanx.online/lab/text-outline) | `text-outline` | duration | 装饰留档 |
| [多行打字](https://motionlab.uanx.online/lab/text-typewriter-multi) | `text-typewriter-multi` | speed | 装饰留档 |
| [删除重打](https://motionlab.uanx.online/lab/text-delete-retype) | `text-delete-retype` | speed | 装饰留档 |
| [3D 波浪](https://motionlab.uanx.online/lab/text-wave-3d) | `text-wave-3d` | duration | 装饰留档 |
| [弹跳文字](https://motionlab.uanx.online/lab/text-bounce) | `text-bounce` | duration | 装饰留档 |
| [彩虹偏移](https://motionlab.uanx.online/lab/text-rainbow-shift) | `text-rainbow-shift` | duration | 装饰留档 |
| [长投影](https://motionlab.uanx.online/lab/text-shadow-long) | `text-shadow-long` | depth | 装饰留档 |
| [描边动画](https://motionlab.uanx.online/lab/text-stroke-animate) | `text-stroke-animate` | duration | 装饰留档 |
| [分裂揭示](https://motionlab.uanx.online/lab/text-split-reveal) | `text-split-reveal` | duration | 专项展示 |
| [字符下落](https://motionlab.uanx.online/lab/text-char-fall) | `text-char-fall` | duration | 装饰留档 |
| [词语飞入](https://motionlab.uanx.online/lab/text-word-fly) | `text-word-fly` | duration, stagger | 装饰留档 |

### 交互 · 40

| 原例 | ID | 可调字段 | 桌面策略 |
|---|---|---|---|
| [磁吸光标](https://motionlab.uanx.online/lab/magnetic-cursor) | `magnetic-cursor` | strength | 装饰留档 |
| [3D 倾斜](https://motionlab.uanx.online/lab/three-d-tilt) | `three-d-tilt` | max | 专项展示 |
| [点击波纹](https://motionlab.uanx.online/lab/ripple-click) | `ripple-click` | duration | 控件反馈 |
| [鼠标视差](https://motionlab.uanx.online/lab/parallax-mouse) | `parallax-mouse` | intensity | 装饰留档 |
| [粘性光标](https://motionlab.uanx.online/lab/blob-cursor) | `blob-cursor` | size | 装饰留档 |
| [悬停图像畸变](https://motionlab.uanx.online/lab/hover-image-distort) | `hover-image-distort` | amount | 专项展示 |
| [磁吸按钮](https://motionlab.uanx.online/lab/magnetic-button) | `magnetic-button` | radius | 装饰留档 |
| [堆叠翻页](https://motionlab.uanx.online/lab/sticky-stack) | `sticky-stack` | count | 专项展示 |
| [拖动滚动](https://motionlab.uanx.online/lab/drag-scroll) | `drag-scroll` | duration | 定点操控 |
| [随悬停变色](https://motionlab.uanx.online/lab/color-picker-hover) | `color-picker-hover` | size | 装饰留档 |
| [按钮按下](https://motionlab.uanx.online/lab/button-press) | `button-press` | scale | 控件反馈 |
| [悬停上浮](https://motionlab.uanx.online/lab/hover-lift) | `hover-lift` | lift | 控件反馈 |
| [强倾斜](https://motionlab.uanx.online/lab/tilt-card-strong) | `tilt-card-strong` | max | 装饰留档 |
| [跟随聚光](https://motionlab.uanx.online/lab/spotlight-follow) | `spotlight-follow` | size | 装饰留档 |
| [鼠标拖尾](https://motionlab.uanx.online/lab/mouse-trail) | `mouse-trail` | count, size | 装饰留档 |
| [点击爆开](https://motionlab.uanx.online/lab/click-burst) | `click-burst` | count | 装饰留档 |
| [悬停旋转](https://motionlab.uanx.online/lab/hover-icon-spin) | `hover-icon-spin` | duration | 装饰留档 |
| [滑动开关](https://motionlab.uanx.online/lab/toggle-flip) | `toggle-flip` | duration | 控件反馈 |
| [手风琴](https://motionlab.uanx.online/lab/accordion-smooth) | `accordion-smooth` | duration | 层级开合 |
| [滑块拖动](https://motionlab.uanx.online/lab/range-drag) | `range-drag` | max | 数值进度 |
| [悬停缩放](https://motionlab.uanx.online/lab/hover-scale) | `hover-scale` | scale | 控件反馈 |
| [悬停旋转](https://motionlab.uanx.online/lab/hover-rotate) | `hover-rotate` | angle | 装饰留档 |
| [悬停倾斜](https://motionlab.uanx.online/lab/hover-skew) | `hover-skew` | angle | 装饰留档 |
| [悬停模糊](https://motionlab.uanx.online/lab/hover-blur) | `hover-blur` | blur | 装饰留档 |
| [悬停变色](https://motionlab.uanx.online/lab/hover-color-change) | `hover-color-change` | duration | 控件反馈 |
| [边框扩展](https://motionlab.uanx.online/lab/hover-border-expand) | `hover-border-expand` | duration | 控件反馈 |
| [文字揭示](https://motionlab.uanx.online/lab/hover-text-reveal) | `hover-text-reveal` | duration | 定点操控 |
| [图片放大](https://motionlab.uanx.online/lab/hover-image-zoom) | `hover-image-zoom` | scale | 定点操控 |
| [翻转卡片](https://motionlab.uanx.online/lab/hover-flip-card) | `hover-flip-card` | duration | 装饰留档 |
| [悬停发光](https://motionlab.uanx.online/lab/hover-glow) | `hover-glow` | intensity | 控件反馈 |
| [Material 波纹](https://motionlab.uanx.online/lab/click-ripple-material) | `click-ripple-material` | duration | 控件反馈 |
| [点击冲击波](https://motionlab.uanx.online/lab/click-shockwave) | `click-shockwave` | duration | 装饰留档 |
| [Emoji 爆开](https://motionlab.uanx.online/lab/click-emoji-burst) | `click-emoji-burst` | count | 装饰留档 |
| [拖动揭示](https://motionlab.uanx.online/lab/drag-to-reveal) | `drag-to-reveal` | duration | 定点操控 |
| [拖动旋转](https://motionlab.uanx.online/lab/drag-rotate) | `drag-rotate` | sensitivity | 定点操控 |
| [滚动进度](https://motionlab.uanx.online/lab/scroll-progress) | `scroll-progress` | height | 数值进度 |
| [滚动揭示](https://motionlab.uanx.online/lab/scroll-reveal) | `scroll-reveal` | distance | 分组呈现 |
| [滚动视差](https://motionlab.uanx.online/lab/scroll-parallax) | `scroll-parallax` | speed | 专项展示 |
| [磁吸文字](https://motionlab.uanx.online/lab/hover-magnetic-text) | `hover-magnetic-text` | strength | 装饰留档 |
| [跟随光标](https://motionlab.uanx.online/lab/hover-follow-cursor) | `hover-follow-cursor` | speed | 装饰留档 |

### 高级 · 38

| 原例 | ID | 可调字段 | 桌面策略 |
|---|---|---|---|
| [滚动驱动](https://motionlab.uanx.online/lab/gsap-scrollTrigger) | `gsap-scrollTrigger` | distance | 专项展示 |
| [粒子系统](https://motionlab.uanx.online/lab/three-particles) | `three-particles` | count | 专项展示 |
| [着色器](https://motionlab.uanx.online/lab/webgl-shader) | `webgl-shader` | speed | 专项展示 |
| [五彩纸屑](https://motionlab.uanx.online/lab/canvas-confetti) | `canvas-confetti` | count | 专项展示 |
| [Lottie 加载](https://motionlab.uanx.online/lab/lottie-loader) | `lottie-loader` | style | 任务等待 |
| [SVG 形变](https://motionlab.uanx.online/lab/morph-svg) | `morph-svg` | duration | 专项展示 |
| [网格磁吸](https://motionlab.uanx.online/lab/grid-magnetic) | `grid-magnetic` | radius | 装饰留档 |
| [正弦波](https://motionlab.uanx.online/lab/sine-wave) | `sine-wave` | frequency, amplitude | 专项展示 |
| [音频条](https://motionlab.uanx.online/lab/audio-wave) | `audio-wave` | bars, speed | 专项展示 |
| [分形树](https://motionlab.uanx.online/lab/fractal-tree) | `fractal-tree` | depth, angle | 专项展示 |
| [噪声流动](https://motionlab.uanx.online/lab/noise-flow) | `noise-flow` | speed, scale | 专项展示 |
| [粘性球](https://motionlab.uanx.online/lab/metaball) | `metaball` | count, blur | 专项展示 |
| [弹簧物理](https://motionlab.uanx.online/lab/physics-spring) | `physics-spring` | stiffness, damping | 定点操控 |
| [路径运动](https://motionlab.uanx.online/lab/trajectory-path) | `trajectory-path` | duration | 专项展示 |
| [立方体](https://motionlab.uanx.online/lab/3d-cube-rotate) | `3d-cube-rotate` | duration | 专项展示 |
| [数字雨](https://motionlab.uanx.online/lab/matrix-rain) | `matrix-rain` | speed, density | 装饰留档 |
| [水波涟漪](https://motionlab.uanx.online/lab/ripple-water) | `ripple-water` | duration, count | 专项展示 |
| [流体畸变](https://motionlab.uanx.online/lab/fluid-distort) | `fluid-distort` | amount, speed | 专项展示 |
| [粒子喷泉](https://motionlab.uanx.online/lab/particle-fountain) | `particle-fountain` | count | 专项展示 |
| [粒子星系](https://motionlab.uanx.online/lab/particle-galaxy) | `particle-galaxy` | count | 专项展示 |
| [等离子着色器](https://motionlab.uanx.online/lab/shader-plasma) | `shader-plasma` | speed | 专项展示 |
| [火球着色器](https://motionlab.uanx.online/lab/shader-fireball) | `shader-fireball` | speed | 专项展示 |
| [雪花飘落](https://motionlab.uanx.online/lab/canvas-snow) | `canvas-snow` | count | 专项展示 |
| [烟花](https://motionlab.uanx.online/lab/canvas-fireworks) | `canvas-fireworks` | count | 专项展示 |
| [星空](https://motionlab.uanx.online/lab/canvas-starfield) | `canvas-starfield` | count | 专项展示 |
| [海浪](https://motionlab.uanx.online/lab/canvas-ocean) | `canvas-ocean` | speed | 专项展示 |
| [路径绘制](https://motionlab.uanx.online/lab/svg-draw-path) | `svg-draw-path` | duration | 专项展示 |
| [虚线动画](https://motionlab.uanx.online/lab/svg-dash-animate) | `svg-dash-animate` | duration | 专项展示 |
| [3D 球体](https://motionlab.uanx.online/lab/3d-sphere) | `3d-sphere` | detail | 专项展示 |
| [3D 圆环](https://motionlab.uanx.online/lab/3d-torus) | `3d-torus` | duration | 专项展示 |
| [GSAP 时间线](https://motionlab.uanx.online/lab/gsap-timeline) | `gsap-timeline` | duration | 专项展示 |
| [GSAP 错落](https://motionlab.uanx.online/lab/gsap-stagger) | `gsap-stagger` | stagger | 分组呈现 |
| [Lottie 打勾](https://motionlab.uanx.online/lab/lottie-checkmark) | `lottie-checkmark` | duration | 操作回执 |
| [重力物理](https://motionlab.uanx.online/lab/physics-gravity) | `physics-gravity` | gravity | 专项展示 |
| [布料模拟](https://motionlab.uanx.online/lab/physics-cloth) | `physics-cloth` | resolution | 专项展示 |
| [曼德博集合](https://motionlab.uanx.online/lab/fractal-mandelbrot) | `fractal-mandelbrot` | iterations | 专项展示 |
| [流场粒子](https://motionlab.uanx.online/lab/flow-field) | `flow-field` | count | 专项展示 |
| [Voronoi 艺术](https://motionlab.uanx.online/lab/voronoi-art) | `voronoi-art` | count | 专项展示 |

## 两个配套入口

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

Motion.Lab 的[项目 README](https://github.com/yangxu128/Motion.Lab/blob/fbfda036aadbc1b46547bce8a7a57ec12bf73485/README.md)标注 MIT；此次核对的仓库树未见独立 LICENSE。若项目需直接引入其演示代码、第三方依赖或素材，另行核实对应版本、权利人与署名。

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
