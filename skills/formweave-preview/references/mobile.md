# 移动方法如何转为桌面行为

下表的桌面方案均为织形建议。厂商开发者资料与产品功能说明分别标注；没有设备实测时不能记为实例观察。项目若用截图或视频作观察，另记设备、系统构建、应用版本、具体画面和复现步骤。只采用能解释当前设计决策的条目。

| 版本与来源 | 资料中可提取的方法 | 桌面转化及验证 |
|---|---|---|
| iOS 26，开发者设计讲解 [WWDC25](https://developer.apple.com/videos/play/wwdc2025/219/) | 以材质区分控件和滚动内容层 | 工具栏与内容层分离；重叠文字、禁用透明和 Win10 实色三种条件均检查可读性。 |
| ColorOS 15，厂商产品说明 [OPPO](https://www.oppo.com/en/newsroom/stories/oppo-coloros-15-launch-smooth/) | 多个动作衔接时保持反馈连续 | 快速切换筛选和侧栏时以最新操作为准；连点和减少动效模式均可完成任务。 |
| HyperOS 2，厂商产品展示 [Xiaomi](https://www.mi.com/global/hyperos?app_version=dev.20051&boardId=39707696) | 关注系统转场的空间连续性；活动页可能随版本改版，引用前核对页面标题 | 列表进入详情时保留上下文；宽窗改成列表/详情分栏，返回恢复焦点。版本不匹配时改记为待核。 |
| HarmonyOS 4，厂商支持说明 [华为实况窗](https://consumer.huawei.com/cn/support/content/zh-cn15978591/) | 让正在进行的活动持续可见 | 将批量任务摘要放在窗口状态栏，提供详情、取消和失败重试，不遮住当前表格。 |
| One UI 7，厂商功能说明 [Samsung](https://www.samsung.com/ca/support/mobile-devices/one-ui-7-on-samsung-galaxy/) | 用 Now Bar 集中呈现进行中的活动 | 多窗口中把状态归属到对应文档，操作可用鼠标和键盘触发；不要求用户执行触屏手势。 |
| OriginOS 5，厂商支持实例 [vivo X200](https://www.vivo.com.cn/service/questions/all?categoryId=158&questionId=1744) | 原子岛以精简信息表达进行中状态，提供拖放入口 | 桌面保留标准拖放和复制语义，并提供右键和菜单等价动作。批量操作显示数量与目的地。 |

只借鉴可解释的方法。图标、字体、截图与品牌素材的复用要单独确认许可。
