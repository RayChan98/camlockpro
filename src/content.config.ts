import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// APKB 铁律：产品/博客走 Content Collections + TS schema 校验，
// 禁手写散 frontmatter（istamping 栽过的坑）。

const products = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/products' }),
  schema: z.object({
    title: z.string(),
    seoTitle: z.string(),
    seoDesc: z.string(),
    // 主关键词：必须来自 KEYWORDS.md 真值词表（Semrush 导出），禁自造
    primaryKeyword: z.string(),
    volume: z.number().optional(),
    kd: z.number().optional(),
    category: z.enum([
      'aluminum',
      'stainless-steel',
      'brass',
      'polypropylene',
      'fittings-adapters',
      'gaskets-seals',
      'dust-caps-plugs',
      'accessories',
    ]),
    summary: z.string(),
    // 参数来源：抄竞对引流阶段一律 'competitor-reference'，
    // 拿到母厂真参数后改 'factory-verified'
    specSource: z.enum(['competitor-reference', 'factory-verified']),
    specSourceNote: z.string().default('Reference data compiled from public industry sources — pending factory verification.'),
    // 参数未验证时不进 sitemap，避免空壳/未核页面拖累站点质量
    noindex: z.boolean().default(false),
    order: z.number().default(99),
    updated: z.coerce.date(),
  }),
});

const guides = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/guides' }),
  schema: z.object({
    title: z.string(),
    seoTitle: z.string(),
    seoDesc: z.string(),
    primaryKeyword: z.string(),
    volume: z.number().optional(),
    kd: z.number().optional(),
    cluster: z.string(),
    summary: z.string(),
    // pubDate 缺省时回落到 updated，避免必填字段卡住内容产出
    pubDate: z.coerce.date().optional(),
    updated: z.coerce.date().optional(),
    noindex: z.boolean().default(false),
  }),
});

export const collections = { products, guides };
