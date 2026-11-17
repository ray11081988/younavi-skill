---
name: younavi-proposal-deck
description: 制作精美的横向翻页宣讲演示Slides。适合产品分享、发布会演示、路线图展示和团队叙事。内置多种版式和组件，支持 html 展示和PDF 导出。
exposure: on-trigger
---

# YouNavi Proposal Deck

把一个粗略主题、标题、大纲或素材，转成一份可本地预览的单文件 HTML 横向翻页 PPT。视觉上像 YouNavi 产品 UI 被翻译成演讲稿：中性白底、Action Blue、系统无衬线字体、发丝线、紧凑信息密度，以及少量有分量的 hero 页。

这个 skill 的核心不是“立刻生成”，而是先把用户意图、页数、大纲、四周小标注和表格需求确认清楚，再产出 HTML，并自动打开本地预览。PDF、打印版或其他格式只在用户需要时继续生成。

## 交付契约

- 默认交付一个自包含 `.html` 文件。
- 默认从 `assets/template.html` 开始，把生成的 slide 粘贴到 `SLIDES_HERE` 与 `SLIDES_HERE_END` 之间。
- 如果用户要纯黑白灰、不使用蓝色，改用 `assets/template-mono.html`。
- `assets/template.html` 是空母版；可打开 `examples/sample.html` 查看示范页，但不要直接把 sample 当交付母版。
- 保留横向翻页、进度条、ESC 索引、底部圆点导航和 token 区，除非有明确理由改动。
- 用户没有给出具体身份信息前，使用占位符：`[品牌名]`、`[作者 / 团队]`、`[Deck 名称]`、`[日期]`、`[网址 / 联系方式]`。
- 可复用示例里不要硬编码 YouNavi、人名、日期或网址；只有用户明确提供时才填真实值。

## 工作流

严格按下面的决策流走。除非用户已经给足素材，否则不要跳过确认直接生成 PPT。

### 第一步：判断输入完整度

先检查用户是否提供了：

- 主题或标题
- 大纲或内容素材
- 页数要求或大致长度
- 受众 / 使用场景（如有）

如果用户给了标题/主题、大纲/内容和页数，进入第二步。

如果用户连主题都没有给，只问主题或标题。不要一次性追问所有缺失信息。

如果用户给了标题/主题，但没有大纲或内容，先草拟一份简洁大纲并停下来确认：

> 我先按这个主题草拟一份大纲，你看方向是否对；如果你有自己的大纲，也可以直接发我。

草拟时按页列出每页目的和页数。发完后等待用户确认。

如果用户给了内容但没给页数，根据素材选择一个合理页数，并在生成前说明这个假设。

### 第二步：确认风格

MVP 主风格是 YouNavi Proposal Deck。因此现在不要让用户多选复杂风格。必要时只说明默认选择：

> 我先按 YouNavi 产品风：白底/浅灰、Action Blue、发丝线、产品界面式信息密度来做。

如果用户明确要求对比或纯黑白灰，则使用 `assets/template-mono.html`。不要临时发明其他视觉主题。

### 第三步：整理信息架构

用户确认大纲后，读取 `references/structure.md`，把内容映射到页面角色。随后只读取必要的视觉参考：

- 改颜色、字体、间距、动效前读 `references/theme.md`。
- 组合页面版式时读 `references/layouts.md`。
- 使用卡片、按钮、chip、截图、指标、流程行、对比行或表格时读 `references/components.md`。

### 第四步：确认四周小标注

风格和主题大纲确认后，生成前检查用户是否给了 PPT 四周的小标注信息：

- 品牌 / 项目标识：如 `[品牌名]`
- 团队 / 作者：如 `[作者 / 团队]`
- Deck 名称：如 `[Deck 名称]`
- 年份 / 日期：如 `[年份]`、`[日期]`
- 右上角页面标签策略：如 `BACKGROUND`、`METRICS`、`ROADMAP`
- 是否需要页脚左侧文字、页脚右侧页码、顶部 running head

如果这些信息都已给出，按用户信息填写。

如果缺失，必须先询问用户，而不是自行编造。询问时给用户两个明确选择：

> 四周小标注还缺一些信息，比如品牌名、团队/作者、年份/日期、Deck 名称。你希望我怎么处理？  
> 1. 先用占位符：`[品牌名]`、`[作者 / 团队]`、`[日期]`  
> 2. 这版先不要这些四周标注，只保留页码/必要导航  
> 也可以直接把要显示的内容发我。

问完后停下来等待确认。用户选择“占位”时保留方括号占位符；用户选择“不要”时，生成 slide 时删除对应可见标注，但保留必要页码/导航功能。

### 第五步：判断是否需要表格

生成 HTML 前，模型自行判断是否需要表格。

只有当内容涉及对比、功能矩阵、路线图、价格/套餐、里程碑、before/after 映射、责任分工或结构化数值时，才考虑表格。

如果不需要表格，直接继续，不要额外打扰用户。

如果判断表格有价值，必须先问用户确认，并给出具体参数：

> 这里我判断第 X 页适合用表格来呈现。建议用 `[表格目的]`，`[列数]` 列 × `[行数]` 行，列为 `[列名...]`。这样可以吗？

问完后停下来等待确认。如果用户拒绝，就把同样内容改成 rows 或 cards。

### 第六步：生成并给出 HTML 预览

当大纲、风格、四周小标注和表格决策都确认后：

1. 复制选定母版到目标输出路径：默认用 `assets/template.html`；纯黑白灰需求用 `assets/template-mono.html`。
2. 把生成的 slide 写入 `SLIDES_HERE` 与 `SLIDES_HERE_END` 之间。
3. 填写可见文案、媒体占位、页码和 `data-title`。
4. 如果有真实产品截图，优先使用；没有则保留清晰的图片路径占位。
5. 读取 `references/checklist.md` 做最终检查：身份占位、溢出风险、页脚一致性、页数、产品风纪律。
6. 运行 `node scripts/validate-proposal-deck.mjs path/to/index.html`，P0 错误必须修掉；warning 需要人工判断。
7. HTML 生成并校验通过后，自动打开本地文件预览。
   - 在 Codex 桌面环境中，优先使用可用的浏览器/打开能力打开 `file://` 或本地 HTML 路径。
   - 如果环境不支持自动打开，明确告诉用户未能自动打开，并给出 HTML 路径。
8. 把 HTML 路径发给用户，并说明已打开预览。
9. 告诉用户：如果需要 PDF、打印版或其他格式，可以继续生成；但不要主动生成这些格式。

### 第七步：按需导出 PDF

只有在用户明确要求 PDF，或用户已确认 HTML 预览可以导出后，才执行这一步。

使用内置脚本：

```bash
python scripts/export-pdf.py --html path/to/index.html --out path/to/slides.pdf
```

规则：

- PDF 是 HTML 的快照，不能作为新的版式源单独修改。
- 导出前必须先确保 HTML 已通过 `scripts/validate-proposal-deck.mjs`。
- 如果 Playwright / Chromium 缺失，说明依赖缺失，不要改用截图拼接等临时方案。
- 导出完成后，把 PDF 路径发给用户。

## 视觉原则

这套 deck 要在“产品纪律”和“演讲表现力”之间取平衡。

- 正文/内容页遵守产品 UI 规则：白底或浅灰底、左对齐、发丝线、12px 卡片、克制排版、无装饰。
- 封面默认使用白底克制版本；章节页、收尾页和大数字页可以有演讲豁免：更大的字、Action Blue 或 ink 背景、更强留白。
- 封面标题较长时必须使用长标题封面规则：`stage--cover-long`、`display--long`、`cover-title--long`。不要让长标题只占左半屏。
- 主强调色只有 Action Blue。紫色只用于 AI / 文档语义。状态色必须有真实状态含义。
- 禁止装饰性渐变、光斑、玻璃拟态、漂浮大区块、重阴影和随机 SVG 装饰。
- 使用系统无衬线字体和 400/500/600 字重。除非用户明确要求，不引入 Didone、衬线杂志风或瑞士海报风。
- 借鉴 `guizang-ppt-skill` 的校验思路，但不复制它的瑞士锁版式；本 skill 保持产品 UI 语法和轻量版式库。
- 借鉴 `editorial-deck` 的“先结构后渲染”，但不默认生成 PDF / PPTX；HTML 预览是第一交付。

## 推荐页序

普通产品演示优先 8-12 页：

1. 封面
2. 背景 / 为什么现在要讲
3. 痛点 / 断点
4. 核心判断 / thesis
5. 产品或系统解法
6. 工作流 / 架构
7. 指标 / 证据
8. 对比 / before-after
9. 路线图 / 下一步
10. 收尾 CTA

短 deck 保留封面、问题、解法、证据和收尾。长 deck 增加内容页，不要堆更多 hero 页。

详细页面角色和视觉框架见 `references/structure.md`。

## 质量规则

- 每一页必须是带 `data-title` 的 `<section class="slide ...">`。
- 普通页面应包含 `.chrome`、`.stage` 和 `.foot`，除非是有意的全屏例外。
- 页脚左侧必须是占位符友好或用户明确提供的文本。
- 品牌、团队、日期、年份、Deck 名称等四周小标注必须来自用户确认、方括号占位符，或按用户选择删除；不能自行编造。
- 短封面主副标题使用 `stage--cover`、`cover-title` 和 `cover-lead`；长标题使用 `stage--cover-long`、`display--long`、`cover-title--long`，避免内容只占左半屏。
- 最终面向用户的 slide 里不要出现“如何使用本模板”的说明文字。
- 有 token 或现有 class 可用时，不要写自定义 inline 颜色。
- 不要粘贴长段落。拆成 rows、cards 或双栏布局。
- HTML 生成后要自动打开预览；如果无法打开，必须说明原因并给出路径。
- 用户预览 HTML 前，不主动生成 PDF、截图或打印版；用户确认后用 `scripts/export-pdf.py` 导出。
- 交付前必须跑 `scripts/validate-proposal-deck.mjs`。如果是空母版自检，用 `--allow-template`。

## 修改这个 Skill 时

改工作流时更新本文件。改 deck 结构或页面角色规则时更新 `references/structure.md`。改视觉系统时，同时更新 `references/theme.md` 和对应母版的 token 区：默认母版是 `assets/template.html`，黑白灰母版是 `assets/template-mono.html`。新增版式或组件时，分别补到 `references/layouts.md` 和 `references/components.md`。新增 P0 规则时，同步更新 `scripts/validate-proposal-deck.mjs`。
