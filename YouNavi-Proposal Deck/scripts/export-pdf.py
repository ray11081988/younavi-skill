#!/usr/bin/env python3
"""
YouNavi Proposal Deck · HTML to PDF exporter

用 Playwright 打开横向 HTML deck，注入打印样式，把每个 `.slide` 导出为
一页 16:9 PDF。PDF 是 HTML 的快照，不是单独维护的版式源。

用法：
    python scripts/export-pdf.py --html path/to/index.html
    python scripts/export-pdf.py --html path/to/index.html --out path/to/slides.pdf --wait 4000
"""

import argparse
import asyncio
import tempfile
from pathlib import Path


PRINT_STYLE = """
@page {
  size: 13.333in 7.5in;
  margin: 0;
}

html,
body {
  width: 13.333in !important;
  min-height: 7.5in !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow: visible !important;
  background: #fff !important;
}

#deck {
  position: static !important;
  inset: auto !important;
  display: block !important;
  width: 13.333in !important;
  height: auto !important;
  transform: none !important;
  transition: none !important;
}

.slide {
  position: relative !important;
  display: flex !important;
  flex: none !important;
  width: 13.333in !important;
  height: 7.5in !important;
  min-height: 7.5in !important;
  max-height: 7.5in !important;
  overflow: hidden !important;
  break-after: page !important;
  page-break-after: always !important;
  break-inside: avoid !important;
  page-break-inside: avoid !important;
}

.slide:last-child {
  break-after: auto !important;
  page-break-after: auto !important;
}

#progress,
#nav,
#folio,
#index {
  display: none !important;
}

[data-anim] {
  opacity: 1 !important;
  transition: none !important;
  transition-delay: 0ms !important;
}
"""


SINGLE_SLIDE_STYLE = """
html,
body {
  width: 13.333in !important;
  height: 7.5in !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow: hidden !important;
}

#deck {
  position: static !important;
  display: block !important;
  width: 13.333in !important;
  height: 7.5in !important;
  transform: none !important;
  transition: none !important;
}

.slide {
  display: none !important;
  position: relative !important;
  flex: none !important;
  width: 13.333in !important;
  height: 7.5in !important;
  min-height: 7.5in !important;
  max-height: 7.5in !important;
  overflow: hidden !important;
}

.slide.__export_current {
  display: flex !important;
}

#progress,
#nav,
#folio,
#index {
  display: none !important;
}

[data-anim] {
  opacity: 1 !important;
  transition: none !important;
  transition-delay: 0ms !important;
}
"""


def parse_args():
    parser = argparse.ArgumentParser(description="Export a YouNavi product HTML deck to PDF")
    parser.add_argument("--html", required=True, help="Input HTML deck path")
    parser.add_argument(
        "--out",
        default=None,
        help="Output PDF path. Defaults to the input HTML path with .pdf suffix.",
    )
    parser.add_argument("--wait", type=int, default=4000, help="Extra wait time in ms")
    return parser.parse_args()


def resolve_path(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = Path.cwd() / path
    return path.resolve()


async def main(args):
    try:
        from playwright.async_api import async_playwright
    except ImportError as exc:
        raise SystemExit(
            "缺少 Playwright。请先安装：pip install playwright && playwright install chromium"
        ) from exc
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError as exc:
        raise SystemExit("缺少 pypdf。请先安装：pip install pypdf") from exc

    html_path = resolve_path(args.html)
    out_path = resolve_path(args.out) if args.out else html_path.with_suffix(".pdf")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not html_path.exists():
        raise FileNotFoundError(f"HTML 文件不存在：{html_path}")

    print(f"Loading {html_path.as_uri()}")

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        await page.goto(html_path.as_uri(), wait_until="networkidle")
        await page.emulate_media(media="screen")
        await page.evaluate("document.fonts ? document.fonts.ready : Promise.resolve()")
        await page.wait_for_timeout(args.wait)
        await page.add_style_tag(content=PRINT_STYLE + SINGLE_SLIDE_STYLE)

        slide_count = await page.locator(".slide").count()
        if slide_count == 0:
            raise RuntimeError("没有找到 `.slide` 页面，无法导出 PDF。")

        writer = PdfWriter()
        with tempfile.TemporaryDirectory(prefix="younavi-proposal-deck-pdf-") as temp_dir:
            temp_root = Path(temp_dir)
            for index in range(slide_count):
                await page.evaluate(
                    """
                    (index) => {
                      const slides = Array.from(document.querySelectorAll('.slide'));
                      slides.forEach((slide, i) => {
                        slide.classList.toggle('__export_current', i === index);
                      });
                    }
                    """,
                    index,
                )
                part_path = temp_root / f"slide-{index + 1:02d}.pdf"
                await page.pdf(
                    path=str(part_path),
                    print_background=True,
                    prefer_css_page_size=True,
                    width="13.333in",
                    height="7.5in",
                    margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
                )
                reader = PdfReader(str(part_path))
                if len(reader.pages) != 1:
                    raise RuntimeError(
                        f"第 {index + 1} 页导出异常：期望 1 页，实际 {len(reader.pages)} 页。"
                    )
                writer.add_page(reader.pages[0])

        with out_path.open("wb") as file:
            writer.write(file)
        await browser.close()

    print(f"Done · {slide_count} slides exported to {out_path}")


if __name__ == "__main__":
    asyncio.run(main(parse_args()))
