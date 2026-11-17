#!/usr/bin/env node
import { readFileSync } from 'node:fs';

const file = process.argv[2];
const allowTemplate = process.argv.includes('--allow-template');

if (!file) {
  console.error('Usage: node scripts/validate-proposal-deck.mjs <index.html> [--allow-template]');
  process.exit(2);
}

const html = readFileSync(file, 'utf8');
const htmlNoComments = html.replace(/<!--[\s\S]*?-->/g, '');
const errors = [];
const warnings = [];

const titleMatch = html.match(/<title>([\s\S]*?)<\/title>/i);
const title = titleMatch?.[1]?.trim() ?? '';

if (!allowTemplate && (!title || /\[必填\]|替换为 PPT 标题|Deck Title/.test(title))) {
  errors.push('Document <title> still contains the template placeholder.');
}

const deckMatch = htmlNoComments.match(/<div\b[^>]*id="deck"[^>]*>([\s\S]*?)<\/div>\s*<div\b[^>]*id="nav"/i);
const deckHtml = deckMatch?.[1] ?? htmlNoComments;
const slideRe = /<section\b[^>]*class="[^"]*\bslide\b[^"]*"[^>]*>[\s\S]*?<\/section>/g;
const slides = [...deckHtml.matchAll(slideRe)].map((m, idx) => ({
  idx: idx + 1,
  html: m[0],
  tag: m[0].match(/<section\b[^>]*>/)?.[0] ?? '',
}));

if (!slides.length && !allowTemplate) {
  errors.push('No <section class="slide ..."> pages found between SLIDES_HERE markers.');
}

if (!allowTemplate && /SLIDES_HERE[\s\S]*SLIDES_HERE_END/.test(deckHtml) && !slides.length) {
  errors.push('Template markers are still empty. Insert generated slides before delivery.');
}

const forbiddenVisuals = [
  ['linear-gradient', /linear-gradient\s*\(/i],
  ['radial-gradient', /radial-gradient\s*\(/i],
  ['backdrop-filter', /backdrop-filter\s*:/i],
  ['large shadow', /box-shadow\s*:\s*(?!var\(--shadow-card(?:-hover)?\))/i],
];

for (const [label, re] of forbiddenVisuals) {
  if (re.test(deckHtml)) warnings.push(`Potential non-product visual treatment found: ${label}.`);
}

const customHexRe = /#[0-9a-fA-F]{3,8}\b/g;
const cssTokenBlock = html.match(/<style>[\s\S]*?<\/style>/i)?.[0] ?? '';
const bodyWithoutStyle = htmlNoComments.replace(cssTokenBlock, '');
const customHexes = [...bodyWithoutStyle.matchAll(customHexRe)]
  .map((m) => m[0])
  .filter((value) => !/^#(?:fff|ffffff)$/i.test(value));
if (customHexes.length) {
  warnings.push(`Custom hex values outside token CSS: ${[...new Set(customHexes)].join(', ')}. Prefer theme tokens.`);
}

slides.forEach((slide) => {
  const title = slide.tag.match(/\bdata-title="([^"]*)"/)?.[1]?.trim();
  if (!title) errors.push(`Slide ${slide.idx}: missing data-title for ESC index.`);

  const className = slide.tag.match(/\bclass="([^"]*)"/)?.[1] ?? '';
  if (!/\bslide--(?:canvas|surface|brand|ink)\b/.test(className)) {
    errors.push(`Slide ${slide.idx}: missing product theme class slide--canvas/surface/brand/ink.`);
  }

  const isFullBleedException = /\bdata-full-bleed="true"\b/.test(slide.tag);
  if (!isFullBleedException) {
    for (const part of ['chrome', 'stage', 'foot']) {
      if (!new RegExp(`class="[^"]*\\b${part}\\b`).test(slide.html)) {
        errors.push(`Slide ${slide.idx}: missing .${part}. Use data-full-bleed="true" only for intentional exceptions.`);
      }
    }
  }

  const emCount = (slide.html.match(/\bclass="[^"]*\bem\b/g) ?? []).length;
  if (emCount > 1) warnings.push(`Slide ${slide.idx}: more than one .em highlight. Product deck should usually emphasize one thing.`);

  if (/\bclass="[^"]*\bframe\b[^"]*"/.test(slide.html) && !/\br-(?:16x10|16x9|4x3|1x1)\b/.test(slide.html)) {
    warnings.push(`Slide ${slide.idx}: .frame without a standard ratio class.`);
  }

  if (!allowTemplate && /如何使用本模板|SLIDES_HERE|示范页/.test(slide.html)) {
    errors.push(`Slide ${slide.idx}: visible template instruction text appears in a slide.`);
  }
});

if (warnings.length) {
  console.warn('Warnings:');
  for (const warning of warnings) console.warn(`- ${warning}`);
}

if (errors.length) {
  console.error('YouNavi proposal deck validation failed:');
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log(`YouNavi proposal deck validation passed: ${slides.length} slide(s).`);
