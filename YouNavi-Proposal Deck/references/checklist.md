# 检查清单

交付生成好的 deck 前读取并执行。

## P0 必须修

- 最终文件是一个可本地打开的 `.html` deck。
- 用户已确认大纲，或用户一开始就提供了完整大纲/素材。
- 四周小标注策略已确认：使用用户提供内容、使用方括号占位符，或删除非必要标注。
- 如果生成了表格，用户已明确确认行列参数。
- 可复用示例没有硬编码人名、网址、日期或品牌身份，除非用户提供。
- 所有可见身份字段要么来自用户，要么是方括号占位符。
- 每一页都是带 `data-title` 的 `<section class="slide ...">`。
- 封面主副标题不是满宽排版；封面使用 `stage--cover`、`cover-title`、`cover-lead`。
- 长标题封面没有被塞进短标题版式；应使用 `stage--cover-long`、`display--long`、`cover-title--long`。
- 文本没有溢出，也没有和页脚、chrome、底部圆点或 folio 撞在一起。
- 没有无意保留的模板组件内容：尤其是工作流卡片里的 `.step .n` 圆点数字、`[步骤一]`、`[一句说明]`、图片路径占位或示例页文案。所有可见编号都必须有明确叙事/顺序含义。
- 没有装饰性渐变、光斑、bokeh、玻璃拟态或重阴影。
- HTML 生成后已自动打开本地预览；如果环境不支持自动打开，已明确说明并给出路径。
- 未经用户要求，不生成 PDF / 导出文件；HTML 预览优先。
- `node scripts/validate-proposal-deck.mjs path/to/index.html` 已通过，没有 P0 error。
- 如果用户要求 PDF，已使用 `python scripts/export-pdf.py --html path/to/index.html --out path/to/slides.pdf`，且没有把 PDF 当作单独版式源修改。

## P1 应该修

- slide 节奏有意图区分 canvas / surface / hero 页。
- 普通内容页的页脚文本一致。
- Action Blue 是唯一主强调色。
- 紫色和状态色都有真实语义。
- 卡片是重复信息项，不是页面大容器。
- 产品截图使用 `.frame` 和合适比例。
- 长段落已拆成 rows、cards 或双栏布局。

## P2 润色

- 章节页留白足够，一页只讲一个想法。
- KPI 页只用 `.em` 强调一个最重要数字。
- meta 标签短，并保持 mono / uppercase 气质。
- 动效仍然是 opacity-only，并尊重 reduced motion。
- `data-title` 对 ESC 索引缩略图有帮助。
- 如果添加了表格 CSS，表格使用发丝线、紧凑文字，没有装饰性填色。
- `examples/sample.html` 只作为参考，不要把 sample 内容混入实际交付。

## P3 可选

- 用真实产品截图替换图片占位。
- 普通产品演示控制在 8-12 页。
- 只有存在真实下一步行动时，才添加最终 CTA。
