# 补强逻辑

本文档说明 `younavi-proposal-deck` 从其它 PPT skill 借鉴了什么，以及刻意没有借鉴什么。

## 总原则

`younavi-proposal-deck` 的目标不是成为另一个全能 PPT 引擎，而是稳定生成 YouNavi 产品视觉语言的 HTML proposal deck。

补强方向：

- 工作流向 `editorial-deck` 学：先结构、后页面、再交付。
- 校验向 `guizang-ppt-skill` 学：把 P0 规则脚本化。
- 视觉只向 YouNavi 产品系统收敛：白底、浅灰、少量 Action Blue、系统字体、发丝线、产品截图；如用户要求对比或纯黑白灰，则使用 mono 母版。

## 从 guizang-ppt-skill 借鉴

借鉴：

- 明确 skill 触发边界。
- 使用模板 + references + checklist + validator 的闭环。
- 交付前跑脚本，避免靠模型自觉记住所有 P0。
- 把示例和母版分离，降低误带 demo 内容的概率。

不借鉴：

- 不采用瑞士 locked mode 的 22 个登记版式；产品 deck 需要更轻量的页面语法。
- 不引入 WebGL、ASCII、强视觉动效或海报式巨字系统。
- 不开放多主题。当前只有 YouNavi 产品风。

## 从 editorial-deck 借鉴

借鉴：

- 先确认大纲 / slide map，再生成页面。
- 一页只承载一个判断。
- 版式优先于装饰。
- 使用 layout decision 和 density rule 避免一页塞太多。

不借鉴：

- 不默认导出 PDF / PPTX；本 skill 首交付是 HTML 预览。
- 不使用纸感、衬线、Didone 数字、running head 的刊物系统。
- 不强制 speaker notes；产品 deck 常用于快速演示和迭代。

## 从 younavi-editorial-html-pdf 借鉴

借鉴：

- HTML 是 source of truth。
- 不因输出目标变化而切换视觉系统。
- 明确 scope，避免扩张成泛导出工具。

不借鉴：

- 不使用 editorial 风格提示词。
- 不把 PDF 作为默认最终产物。

## 当前补强后的闭环

1. `SKILL.md` 定义触发、工作流和边界。
2. `references/structure.md` 定义叙事脊柱。
3. `references/layouts.md` 提供可复制版式。
4. `references/components.md` 定义组件语法。
5. `references/theme.md` 锁定视觉 token。
6. `references/checklist.md` 做人工 QA。
7. `scripts/validate-proposal-deck.mjs` 做 P0 静态校验。
8. `examples/sample.html` 保留参考样例。
9. `assets/template.html` 保持默认空母版，避免交付污染；`assets/template-mono.html` 保持纯黑白灰空母版。

## 后续优先级

高优先级：

- 扩展 validator：检查页码连续性、身份占位、表格行列规模、未替换图片路径。
- 增加 screenshot / browser QA 指南。
- 增加真实 YouNavi proposal deck 示例。

中优先级：

- 增加更多产品场景版式，如 release notes、pricing、customer story。
- 提供 `scripts/export-pdf.py` 作为 PDF 导出可选脚本，但仍不作为默认流程。

低优先级：

- 多主题。
- 强动画。
- PPTX 打包。
