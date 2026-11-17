# 组件

在所选母版内使用这些组件模式。默认母版是 `assets/template.html`；纯黑白灰母版是 `assets/template-mono.html`。优先复用现有 class，不要临时发明样式。

## 顶部 Chrome

普通 slide 使用：

```html
<header class="chrome">
  <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
  <span>[页面标签]</span>
</header>
```

规则：

- 左侧是身份信息，但可复用模板里保持 `[品牌名]`。
- 右侧保持短标签，例如 `SECTION`、`POINTS`、`METRICS`、`[页面标签]`。
- 不要把长标题放进 chrome。
- 如果用户选择“不要四周标注”，可删除品牌文字和右侧标签，但不要自行编造。

## 页脚

```html
<footer class="foot"><span>[Deck 名称]</span><span class="meta">03</span></footer>
```

规则：

- 右侧放页码。
- 只有封面/收尾等需要身份表达的页面，才使用 `[作者 / 团队] · [品牌名]`。
- 可复用示例必须对占位符友好。
- 如果用户选择“不要四周标注”，页脚左侧可留空或删除，只保留页码/folio。

## 卡片

```html
<div class="card" data-anim>
  <h3 class="h3">[标题]</h3>
  <p class="body-sm" style="margin-top:var(--sp-8)">[说明]</p>
</div>
```

规则：

- 卡片用于重复信息项，不用于包裹整个页面区块。
- 卡片使用 `border:1px solid var(--c-hairline)` 和 `border-radius:12px`。
- 不要把卡片嵌套在卡片里。
- 从工作流模板复制来的 `.step .n` 圆点编号只能用于真实顺序步骤。并列概念、访谈原则、抽象循环、能力拆解等页面不要保留这些编号，改用 `.meta` 短标签。

## KPI

```html
<div class="card" data-anim>
  <div class="num-mega em">98<span style="font-size:.4em">%</span></div>
  <div class="kpi-label">[指标名]</div>
</div>
```

规则：

- 只给最重要的一个数字使用 `em`。
- 单位放在更小的 inline span 中。
- 除非数字很短，否则一页不要放超过三个 KPI 卡片。

## Rows

```html
<div class="rows">
  <div class="row" data-anim>
    <span class="idx">01</span>
    <div>
      <div class="row-title">[要点标题]</div>
      <div class="body-sm">[一句说明]</div>
    </div>
  </div>
</div>
```

规则：

- rows 适合问题列表、原则、风险和决策。
- 每一行只保留一个标题和一句短说明。

## Chips

```html
<span class="chip">[标签]</span>
```

规则：

- chip 表达状态、分类或功能类型。
- 不要把 chip 当装饰物。

## 按钮

```html
<span class="btn btn--brand">[主要行动]</span>
<span class="btn btn--ghost">[次要行动]</span>
```

规则：

- 只在 CTA 或工作流页面中使用。
- 静态 slide 里的按钮表达行动，不用于解释导航方式。

## 图片框

```html
<div class="frame r-16x10" data-anim>
  <img src="images/[screenshot].png" alt="[截图说明]">
</div>
```

规则：

- 优先使用真实产品截图，不使用泛泛的 stock 图。
- 如果截图暂缺，草稿阶段保留可见的路径占位。
- App 截图用 `r-16x10`；视频/hero 媒体用 `r-16x9`；图示用 `r-4x3`；头像或方形资产用 `r-1x1`。

## 表格

只有经过工作流中的表格确认步骤后，才使用表格。

```html
<div class="card" data-anim>
  <table class="table">
    <thead>
      <tr><th>[列 A]</th><th>[列 B]</th><th>[列 C]</th></tr>
    </thead>
    <tbody>
      <tr><td>[内容]</td><td>[内容]</td><td>[内容]</td></tr>
      <tr><td>[内容]</td><td>[内容]</td><td>[内容]</td></tr>
      <tr><td>[内容]</td><td>[内容]</td><td>[内容]</td></tr>
    </tbody>
  </table>
</div>
```

规则：

- 优先 3-4 列、3-6 行。
- 列名必须短。
- 表格只用于对比/矩阵数据。如果只是简单列表，用 rows。
- 如果当前模板还没有 `.table` CSS，就加到 token 化 CSS 区：发丝线边框、`14px` 文字、无装饰性单元格填色。默认模板可用 Action Blue 文本强调；黑白灰模板只能用灰阶强调。

## 校验脚本

交付前运行：

```bash
node scripts/validate-proposal-deck.mjs path/to/index.html
```

空母版自检使用：

```bash
node scripts/validate-proposal-deck.mjs assets/template.html --allow-template
```

脚本会检查：

- `<title>` 是否仍是模板占位。
- 是否存在 slide，且每页有 `data-title`。
- 每页是否使用 `slide--canvas / surface / brand / ink`。
- 普通页是否包含 `.chrome`、`.stage`、`.foot`。
- 是否有卡片嵌套、过多 `.em` 强调、非 token hex、渐变/重阴影等风险。

脚本不能替代视觉检查。通过脚本后仍要打开 HTML 逐页看是否溢出、是否撞底部导航、截图是否清晰。
