# Motion.Lab 动效索引 · 160 项

用户指定 Motion.Lab 或其具体效果时读取。返回[来源导航](motion-index.md)；策略含义与验收见[动效决策](motion.md)。

目录于 2026-11-04 核对，2026-11-14 复核提交仍为 `fbfda036aadbc1b46547bce8a7a57ec12bf73485`，160 个 ID 集合未变。来源为[实验室](https://motionlab.uanx.online/lab)与 [data/effects.ts](https://github.com/yangxu128/Motion.Lab/blob/fbfda036aadbc1b46547bce8a7a57ec12bf73485/data/effects.ts)。桌面策略为 Formweave 建议；未逐项移植或原生测帧。

可搜索中文名、原始 ID、可调字段或策略。下表按基础 42、文字 40、交互 40、高级 38 分组。

参数列是每张卡公开的可调字段；单位、范围和默认值见对应原例。是否需要 JS、GPU 或新依赖由目标实现决定。例如 lottie-checkmark 的来源定义采用 SVG 表达完成反馈。

## 基础 · 42

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

## 文字 · 40

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

## 交互 · 40

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

## 高级 · 38

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

## 来源与许可

Motion.Lab 的[项目 README](https://github.com/yangxu128/Motion.Lab/blob/fbfda036aadbc1b46547bce8a7a57ec12bf73485/README.md)标注 MIT；此次核对的仓库树未见独立 LICENSE。若项目需直接引入其演示代码、第三方依赖或素材，另行核实对应版本、权利人与署名。
