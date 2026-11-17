# 版式

把下面的区块复制到所选母版的 `SLIDES_HERE` 与 `SLIDES_HERE_END` 之间。默认母版是 `assets/template.html`；纯黑白灰对比母版是 `assets/template-mono.html`。用用户提供的内容替换方括号占位符。

## 封面（默认白底）

```html
<section class="slide slide--canvas" data-title="[封面标题]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
    <span>[DECK 标识] · [年份]</span>
  </header>
  <div class="stage stage--cover">
    <span class="kicker" data-anim>[演讲类型] / [Talk Type]</span>
    <h1 class="display cover-title" data-anim>[主标题第一行]<br>[主标题第二行]</h1>
    <p class="lead cover-lead" data-anim style="margin-top:var(--sp-24)">[一句话副标题]</p>
  </div>
  <footer class="foot">
    <span>[作者 / 团队] · [品牌名]</span>
    <span class="meta">[日期]</span>
  </footer>
</section>
```

## 封面（长标题）

标题超过 18 个中文字符、包含长英文短语，或预计换行超过 3 行时，必须使用这个版本。不要把长标题塞进默认封面，否则会只占左半屏。

```html
<section class="slide slide--canvas" data-title="[封面标题]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
    <span>[DECK 标识] · [年份]</span>
  </header>
  <div class="stage stage--cover-long">
    <span class="kicker" data-anim>[演讲类型] / [Talk Type]</span>
    <h1 class="display display--long cover-title--long" data-anim>[较长主标题第一行]<br>[较长主标题第二行]<br>[可选第三行]</h1>
    <p class="lead cover-lead" data-anim style="margin-top:var(--sp-24)">[一句话副标题]</p>
  </div>
  <footer class="foot">
    <span>[作者 / 团队] · [品牌名]</span>
    <span class="meta">[日期]</span>
  </footer>
</section>
```

## 封面（蓝底备选）

蓝底封面只用于需要强品牌冲击的开场。默认先用白底封面，避免首页整页蓝色太重。

```html
<section class="slide slide--brand" data-title="[封面标题]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot" style="background:#fff"></span>[品牌名]</span>
    <span>[DECK 标识] · [年份]</span>
  </header>
  <div class="stage stage--cover">
    <span class="kicker" data-anim>[演讲类型] / [Talk Type]</span>
    <h1 class="display cover-title" data-anim>[主标题第一行]<br>[主标题第二行]</h1>
    <p class="lead cover-lead" data-anim style="margin-top:var(--sp-24)">[一句话副标题]</p>
  </div>
  <footer class="foot">
    <span>[作者 / 团队] · [品牌名]</span>
    <span class="meta">[日期]</span>
  </footer>
</section>
```

## 章节页

```html
<section class="slide slide--canvas" data-title="[章节名]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
    <span>[章节标签]</span>
  </header>
  <div class="stage">
    <span class="num-mid em" data-anim>01</span>
    <hr class="rule" data-anim style="max-width:120px;margin:var(--sp-24) 0">
    <h2 class="h-hero" data-anim>[章节标题]</h2>
    <p class="lead" data-anim style="margin-top:var(--sp-20)">[章节说明]</p>
  </div>
  <footer class="foot"><span>[Deck 名称]</span><span class="meta">02</span></footer>
</section>
```

## 要点行

```html
<section class="slide slide--surface" data-title="[页面标题]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
    <span>[页面标签]</span>
  </header>
  <div class="stage">
    <h2 class="h1" data-anim style="margin-bottom:var(--sp-32)">[主标题]</h2>
    <div class="rows">
      <div class="row" data-anim>
        <span class="idx">01</span>
        <div><div class="row-title">[要点一]</div><div class="body-sm">[说明一]</div></div>
      </div>
      <div class="row" data-anim>
        <span class="idx">02</span>
        <div><div class="row-title">[要点二]</div><div class="body-sm">[说明二]</div></div>
      </div>
      <div class="row" data-anim>
        <span class="idx">03</span>
        <div><div class="row-title">[要点三]</div><div class="body-sm">[说明三]</div></div>
      </div>
    </div>
  </div>
  <footer class="foot"><span>[Deck 名称]</span><span class="meta">03</span></footer>
</section>
```

## 指标

```html
<section class="slide slide--canvas" data-title="[数据标题]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
    <span>METRICS</span>
  </header>
  <div class="stage">
    <h2 class="h1" data-anim style="margin-bottom:var(--sp-32)">[主标题]</h2>
    <div class="grid grid-3">
      <div class="card" data-anim>
        <div class="num-mega em">[数值]<span style="font-size:.4em">[单位]</span></div>
        <div class="kpi-label">[指标名]</div>
      </div>
      <div class="card" data-anim>
        <div class="num-mega">[数值]<span style="font-size:.4em">[单位]</span></div>
        <div class="kpi-label">[指标名]</div>
      </div>
      <div class="card" data-anim>
        <div class="num-mega">[数值]<span style="font-size:.4em">[单位]</span></div>
        <div class="kpi-label">[指标名]</div>
      </div>
    </div>
  </div>
  <footer class="foot"><span>[Deck 名称]</span><span class="meta">04</span></footer>
</section>
```

## 左文右截图

```html
<section class="slide slide--canvas" data-title="[功能标题]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
    <span>FEATURE</span>
  </header>
  <div class="stage">
    <div class="grid grid-5-7">
      <div data-anim>
        <span class="chip">[标签]</span>
        <h2 class="h1" style="margin:var(--sp-16) 0">[功能标题]</h2>
        <p class="body">[功能说明]</p>
      </div>
      <div class="frame r-16x10" data-anim>
        <img src="images/[screenshot].png" alt="[截图说明]">
      </div>
    </div>
  </div>
  <footer class="foot"><span>[Deck 名称]</span><span class="meta">05</span></footer>
</section>
```

## Before / After 对比

适合状态对比、旧流程/新流程、人工/自动、分散/统一。不要用表格承载情绪判断；两侧各 2-3 行即可。

```html
<section class="slide slide--surface" data-title="[对比标题]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
    <span>COMPARE</span>
  </header>
  <div class="stage">
    <h2 class="h1" data-anim style="margin-bottom:var(--sp-32)">[主标题]</h2>
    <div class="grid grid-2">
      <div class="card" data-anim>
        <div class="meta">BEFORE</div>
        <h3 class="h2" style="margin:var(--sp-16) 0">[旧状态]</h3>
        <div class="rows">
          <div class="row"><span class="idx">01</span><div><div class="row-title">[断点]</div><div class="body-sm">[一句说明]</div></div></div>
          <div class="row"><span class="idx">02</span><div><div class="row-title">[断点]</div><div class="body-sm">[一句说明]</div></div></div>
        </div>
      </div>
      <div class="card" data-anim>
        <div class="meta em">AFTER</div>
        <h3 class="h2" style="margin:var(--sp-16) 0">[新状态]</h3>
        <div class="rows">
          <div class="row"><span class="idx">01</span><div><div class="row-title">[改善]</div><div class="body-sm">[一句说明]</div></div></div>
          <div class="row"><span class="idx">02</span><div><div class="row-title">[改善]</div><div class="body-sm">[一句说明]</div></div></div>
        </div>
      </div>
    </div>
  </div>
  <footer class="foot"><span>[Deck 名称]</span><span class="meta">[页码]</span></footer>
</section>
```

## 工作流步骤

适合 3-4 步产品流程、团队协作流、从输入到结果的系统链路。步骤之间是顺序关系时用它；平行要点继续用 rows/cards。

使用前必须确认圆点数字 `1/2/3/4` 本身就是用户需要看到的顺序语义。如果页面只是表达几个并列概念、方法要素或抽象循环，不要保留 `.step .n` 编号；改用普通 `.card` + `.meta` 标签（如 `ASK`、`LISTEN`、`CONFIRM`），避免模板组件残留造成误读。

```html
<section class="slide slide--canvas" data-title="[工作流标题]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
    <span>WORKFLOW</span>
  </header>
  <div class="stage">
    <h2 class="h1" data-anim style="margin-bottom:var(--sp-32)">[主标题]</h2>
    <div class="grid grid-4">
      <div class="card step" data-anim><span class="n">1</span><h3 class="h3">[步骤一]</h3><p class="body-sm" style="margin-top:var(--sp-8)">[一句说明]</p></div>
      <div class="card step" data-anim><span class="n">2</span><h3 class="h3">[步骤二]</h3><p class="body-sm" style="margin-top:var(--sp-8)">[一句说明]</p></div>
      <div class="card step" data-anim><span class="n">3</span><h3 class="h3">[步骤三]</h3><p class="body-sm" style="margin-top:var(--sp-8)">[一句说明]</p></div>
      <div class="card step" data-anim><span class="n">4</span><h3 class="h3">[步骤四]</h3><p class="body-sm" style="margin-top:var(--sp-8)">[一句说明]</p></div>
    </div>
  </div>
  <footer class="foot"><span>[Deck 名称]</span><span class="meta">[页码]</span></footer>
</section>
```

## 路线图

适合 3 个阶段以内的产品推进，不要超过 4 列。每列一个阶段、两条以内 deliverable。

```html
<section class="slide slide--surface" data-title="[路线图]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
    <span>ROADMAP</span>
  </header>
  <div class="stage">
    <h2 class="h1" data-anim style="margin-bottom:var(--sp-32)">[主标题]</h2>
    <div class="grid grid-3">
      <div class="card" data-anim><div class="meta">NOW</div><h3 class="h3" style="margin-top:var(--sp-12)">[阶段一]</h3><p class="body-sm" style="margin-top:var(--sp-8)">[交付物 / 结果]</p></div>
      <div class="card" data-anim><div class="meta">NEXT</div><h3 class="h3" style="margin-top:var(--sp-12)">[阶段二]</h3><p class="body-sm" style="margin-top:var(--sp-8)">[交付物 / 结果]</p></div>
      <div class="card" data-anim><div class="meta em">LATER</div><h3 class="h3" style="margin-top:var(--sp-12)">[阶段三]</h3><p class="body-sm" style="margin-top:var(--sp-8)">[交付物 / 结果]</p></div>
    </div>
  </div>
  <footer class="foot"><span>[Deck 名称]</span><span class="meta">[页码]</span></footer>
</section>
```

## 系统架构

适合展示输入、处理、输出或产品模块关系。只做产品级解释，不画复杂技术拓扑。

```html
<section class="slide slide--canvas" data-title="[系统架构]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
    <span>SYSTEM</span>
  </header>
  <div class="stage">
    <h2 class="h1" data-anim style="margin-bottom:var(--sp-32)">[主标题]</h2>
    <div class="grid grid-3" style="align-items:stretch">
      <div class="card" data-anim><div class="meta">INPUT</div><h3 class="h3" style="margin-top:var(--sp-12)">[输入]</h3><p class="body-sm" style="margin-top:var(--sp-8)">[来源 / 触发]</p></div>
      <div class="card" data-anim><div class="meta em">SYSTEM</div><h3 class="h3" style="margin-top:var(--sp-12)">[处理]</h3><p class="body-sm" style="margin-top:var(--sp-8)">[核心机制]</p></div>
      <div class="card" data-anim><div class="meta">OUTPUT</div><h3 class="h3" style="margin-top:var(--sp-12)">[输出]</h3><p class="body-sm" style="margin-top:var(--sp-8)">[用户可感知结果]</p></div>
    </div>
  </div>
  <footer class="foot"><span>[Deck 名称]</span><span class="meta">[页码]</span></footer>
</section>
```

## 卡片组

```html
<section class="slide slide--surface" data-title="[卡片组]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
    <span>[页面标签]</span>
  </header>
  <div class="stage">
    <h2 class="h1" data-anim style="margin-bottom:var(--sp-32)">[主标题]</h2>
    <div class="grid grid-3">
      <div class="card" data-anim><h3 class="h3">[标题]</h3><p class="body-sm" style="margin-top:var(--sp-8)">[说明]</p></div>
      <div class="card" data-anim><h3 class="h3">[标题]</h3><p class="body-sm" style="margin-top:var(--sp-8)">[说明]</p></div>
      <div class="card" data-anim><h3 class="h3">[标题]</h3><p class="body-sm" style="margin-top:var(--sp-8)">[说明]</p></div>
    </div>
  </div>
  <footer class="foot"><span>[Deck 名称]</span><span class="meta">06</span></footer>
</section>
```

## 表格矩阵

只在 `SKILL.md` 的表格确认步骤完成后使用。

```html
<section class="slide slide--canvas" data-title="[表格标题]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
    <span>[页面标签]</span>
  </header>
  <div class="stage">
    <h2 class="h1" data-anim style="margin-bottom:var(--sp-32)">[主标题]</h2>
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
  </div>
  <footer class="foot"><span>[Deck 名称]</span><span class="meta">07</span></footer>
</section>
```

## 收尾

```html
<section class="slide slide--ink" data-title="[收尾]">
  <header class="chrome">
    <span class="brand-mark"><span class="dot"></span>[品牌名]</span>
    <span>[收尾标签]</span>
  </header>
  <div class="stage">
    <h2 class="h-hero" data-anim>[收尾主张第一行]<br>[收尾主张第二行]</h2>
    <div data-anim style="margin-top:var(--sp-32);display:flex;gap:var(--sp-12)">
      <span class="btn btn--brand">[主要行动]</span>
      <span class="btn btn--ghost">[网址 / 联系方式]</span>
    </div>
  </div>
  <footer class="foot"><span>[作者 / 团队] · [品牌名]</span><span class="meta">[页码]</span></footer>
</section>
```
