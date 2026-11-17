# YouNavi Proposal Deck 

生成 YouNavi 产品视觉语言的单文件 HTML 横向翻页 PPT。它适合产品分享、发布会演示、路线图、团队叙事和克制的 SaaS 风 proposal deck。

## 定位

这不是杂志风、瑞士海报风或装饰型 landing page。它把 YouNavi 产品 UI 语言翻译成演讲稿：

- 默认白底 / 浅灰底，保留少量 Action Blue；另有纯黑白灰对比模板。
- 系统无衬线字体。
- 发丝线、12px 卡片、16px 截图框。
- 内容页紧凑，hero 页有演讲表现力。
- 动效只做 opacity 渐显。

## 目录

```text
younavi-proposal-deck/
├── SKILL.md
├── assets/
│   ├── template.html
│   └── template-mono.html
├── examples/
│   └── sample.html
├── references/
│   ├── checklist.md
│   ├── components.md
│   ├── enhancement-logic.md
│   ├── layouts.md
│   ├── structure.md
│   └── theme.md
└── scripts/
    ├── export-pdf.py
    └── validate-proposal-deck.mjs
```

## 使用流程

1. 先确认主题、素材、页数或让 skill 草拟大纲。
2. 从 `assets/template.html` 复制一份到目标项目目录；如果用户要纯黑白灰，则用 `assets/template-mono.html`。
3. 按 `references/structure.md` 规划页面角色。
4. 从 `references/layouts.md` 复制版式到 `SLIDES_HERE` 与 `SLIDES_HERE_END` 之间。
5. 用用户内容替换方括号占位符。
6. 运行校验：

```bash
node scripts/validate-proposal-deck.mjs path/to/index.html
```

7. 浏览器打开 HTML 逐页视觉检查。

## PDF 导出

HTML 确认后再导出 PDF：

```bash
python scripts/export-pdf.py --html path/to/index.html --out path/to/slides.pdf
```

前置依赖：

```bash
pip install playwright
playwright install chromium
```

PDF 只是 HTML 的导出快照，不单独维护版式。

## 示例

`examples/sample.html` 是模板效果样例。它用于看视觉和交互，不要直接当交付母版。示例默认封面是白底；蓝底封面只作为备选版式保留。

## 设计边界

- 默认模板主强调色只有 Action Blue，但封面默认不使用整页蓝底。
- `template-mono.html` 不使用蓝色，只有黑白灰。
- 紫色只用于 AI / 文档语义。
- 状态色必须有真实业务语义。
- 不使用装饰性渐变、光斑、玻璃拟态、重阴影。
- 不引入报刊衬线、Didone 数字或瑞士海报式极端排版。

## 和其它 deck skill 的关系

- `guizang-ppt-skill`：更适合杂志风 / 瑞士风的强视觉演讲。
- `editorial-deck`：更适合严肃刊物式 HTML/PDF/PPTX 交付。
- `younavi-proposal-deck`：更适合产品 UI 风、路线图、功能展示、团队/产品叙事。
