# 主题

改 deck 模板里的视觉数值前读取本文档。

## 核心 Token

| 角色 | 数值 | 用途 |
|---|---:|---|
| 画布白 | `#ffffff` | 默认 slide 背景 |
| 呼吸灰 | `#f8f8f8` | 用于交替节奏的浅灰页 |
| muted 块底 | `#f3f3f3` | 截图占位、轻量容器 |
| ink | `#0d0d0d` | 主文字、深色 hero 背景 |
| 次级文字 | `#5d5d5d` | 正文 |
| 三级文字 | `#8f8f8f` | meta、页脚、标签 |
| 发丝线 | `#e9eaeb` | 主要分割线 |
| 边框 | `#e8e8e8` | 更明确的卡片/截图边框 |
| Action Blue | `#0285ff` | 唯一主品牌强调色 |
| Action Blue hover | `#408ff5` | 仅用于交互 hover |
| Action Blue 浅底 | `#e7f0fe` | chip、轻强调 |
| 紫色 | `#5e5ce6` | 仅用于 AI / 文档语义 |

## 字体

- 字体栈：`-apple-system`, `BlinkMacSystemFont`, `PingFang SC`, `SF Pro SC`, `HarmonyOS Sans SC`, `Microsoft YaHei UI`, `Noto Sans SC`, `Inter`, sans-serif。
- 只使用 `400`、`500`、`600` 字重。
- 正文字号使用固定档位：`14`、`16`、`18`、`20`、`24`。
- Hero / display 标题可以用 `min(vw,vh)`，因为它属于演示场景豁免。
- 字距只用于 mono/meta 标签。不要使用负字距。

## 圆角与表面

- 组件/卡片圆角：`12px`。
- 截图/frame 圆角：`16px`。
- 壳层/hero 容器如需使用：`20px` 或 `24px`。
- 胶囊/chip：`999px`。
- 普通内容卡片不漂浮；用发丝线边框，不用大阴影。

## 动效

- 文本只做 opacity 渐显，约 `800ms`。
- 不做滑入、弹跳、旋转、模糊或视差。
- 保留 `prefers-reduced-motion` 支持。

## 允许的背景

- `slide--canvas`：白底，默认内容页。
- `slide--surface`：浅灰底，用于节奏和内容分组。
- `slide--brand`：Action Blue，仅作为封面/章节/CTA 的备选强冲击版本；默认封面先用白底。
- `slide--ink`：深色 ink，仅用于收尾或强 thesis。

## 模板变体

- `assets/template.html`：默认 YouNavi 产品风。保留 Action Blue，但封面默认使用白底版式。
- `assets/template-mono.html`：纯黑白灰对比模板。所有品牌强调、进度条、圆点、chip、指标强调都改成灰阶，不使用蓝色。

## 禁止使用

- 装饰性渐变球、径向光斑、bokeh、玻璃拟态。
- 米色纸感、报刊衬线、Didone 数字。
- 随机第二强调色或多彩 palette。
- slide markup 内的自定义 hex 色值；草稿期真实图片占位除外。
