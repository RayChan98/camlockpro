// 站点单一配置源：域名/导航/联系方式只在这里改一次
// T-41 Camlock 快接 2026-08-23 定：品牌=CamlockPro（camlockpro.com 待注册，先 pages.dev 顶着）
// 旗舰：Aluminum Camlock（应用最广）+ 次旗舰：Stainless Steel / Polypropylene（差异化）
// 建站边界（README）：材质×口径×类型选型矩阵
export const SITE = {
  name: 'CamlockPro',
  tagline: 'Cam and Groove Couplings — Aluminum, Stainless Steel, Brass and Polypropylene for Quick, Leak-Free Transfer',
  url: 'https://camlockpro.pages.dev',
  plannedDomain: 'camlockpro.com',
  inquiryEmail: 'cj226144@gmail.com',
  // 表单走 CF function /api/contact（Zoho OAuth2），Web3Forms 废弃
  web3formsKey: '',
};

// 导航：聚焦欧美 B2B（6 项导航），弃竞对 30+ 分类堆料
export const NAV = [
  { label: 'Products', href: '/products/' },
  { label: 'Applications', href: '/applications/' },
  { label: 'Guides', href: '/guides/' },
  { label: 'OEM', href: '/oem/' },
  { label: 'About', href: '/about/' },
  { label: 'Contact', href: '/contact/' },
];

// 产品分类：材质×类型选型矩阵（03 页面内容提炼主词汇总排序，铝旗舰打头）
export const CATEGORIES = [
  {
    slug: 'aluminum',
    icon: 'alu',
    label: 'Aluminum Camlock Couplings',
    blurb: 'Cast aluminum couplings (types A–F, DC, DP) for water, fuel and general transfer — the most widely used camlock material.',
    milestone: 'M1',
  },
  {
    slug: 'stainless-steel',
    icon: 'ss',
    label: 'Stainless Steel Camlock Couplings',
    blurb: '304/316 stainless couplings for food, chemical and marine duties where corrosion resistance matters.',
    milestone: 'M2',
  },
  {
    slug: 'brass',
    icon: 'brass',
    label: 'Brass Camlock Couplings',
    blurb: 'Machined brass couplings for fuel, gas and high-pressure lines where thread strength and spark risk matter.',
    milestone: 'M3',
  },
  {
    slug: 'polypropylene',
    icon: 'pp',
    label: 'Polypropylene Camlock Couplings',
    blurb: 'Lightweight PP couplings for aggressive chemicals, acids and deionized water.',
    milestone: 'M4',
  },
  {
    slug: 'fittings-adapters',
    icon: 'fit',
    label: 'Camlock Fittings & Adapters',
    blurb: 'Threaded adapters, reducers, hose shanks and flanges to connect camlocks to pipes, hoses and equipment.',
    milestone: 'M5',
  },
  {
    slug: 'gaskets-seals',
    icon: 'gask',
    label: 'Camlock Gaskets & Seals',
    blurb: 'EPDM, NBR, Viton and PTFE gaskets for every size and duty — the part that actually makes the seal.',
    milestone: 'M6',
  },
  {
    slug: 'dust-caps-plugs',
    icon: 'dc',
    label: 'Camlock Dust Caps & Plugs',
    blurb: 'Type DC caps and DP plugs keep open ends clean, safe and drip-free between connections.',
    milestone: 'M7',
  },
  {
    slug: 'accessories',
    icon: 'acc',
    label: 'Camlock Parts & Accessories',
    blurb: 'Replacement lever arms, safety pins, chains and wrenches to keep couplings in service.',
    milestone: 'M8',
  },
];

// 首页应用场景入口：按买家工况组织
export const SCENARIOS = [
  {
    slug: 'agriculture-irrigation',
    label: 'Agriculture & Irrigation',
    blurb: 'Water and liquid fertilizer transfer for pivots, drip and flood irrigation systems.',
    href: '/products/aluminum/',
    guide: '/guides/camlock-irrigation-guide/',
    icon: 'alu',
  },
  {
    slug: 'chemical-transfer',
    label: 'Chemical Transfer',
    blurb: 'Acid, solvent and chemical loading with PP, PTFE-gasketed and stainless couplings.',
    href: '/products/polypropylene/',
    guide: '/guides/camlock-chemical-guide/',
    icon: 'chem',
  },
  {
    slug: 'fuel-oil',
    label: 'Fuel & Oil Transfer',
    blurb: 'Gasoline, diesel, lube and hydraulic oil transfer with brass and aluminum couplings.',
    href: '/products/brass/',
    guide: '/guides/camlock-fuel-guide/',
    icon: 'hydro',
  },
  {
    slug: 'food-beverage',
    label: 'Food & Beverage',
    blurb: 'Sanitary transfer of milk, juice, beer and edible oils with 304/316 stainless and food-grade gaskets.',
    href: '/products/stainless-steel/',
    guide: '/guides/camlock-food-grade-guide/',
    icon: 'food',
  },
  {
    slug: 'water-dewatering',
    label: 'Water & Dewatering',
    blurb: 'Site water, dewatering, fire and municipal hookups with quick, tool-free connections.',
    href: '/products/aluminum/',
    guide: '/guides/camlock-water-guide/',
    icon: 'suct',
  },
  {
    slug: 'ibc-bulk',
    label: 'IBC & Bulk Handling',
    blurb: 'IBC tote, tanker and drum connections for bulk chemical and food transfer.',
    href: '/products/fittings-adapters/',
    guide: '/guides/camlock-ibc-guide/',
    icon: 'assy',
  },
];
