# CAMLOCKPRO HOSES — 工业软管 B2B 外贸站（T-47）

> 域名：camlockprohose.com（2026-08-24 实测无 DNS 可注册，走 CF Registrar；当前 pages.dev 顶着）
> 品牌：CamlockPro — Food Grade, PTFE and Industrial Hoses（食品级旗舰 + PTFE 次旗舰）
> 技术栈：Astro 7.0.6 + Tailwind v4.3.2（clone nozzle-site-v2 同栈兄弟站骨架）
> 状态：品牌定名 ✅ / 竞对调研 ✅ / 内容骨架 ✅（8 产品 + 7 guides）/ 表单打通 ✅（Zoho OAuth2 ok:true）/ 部署 ✅ https://camlockpro-site.pages.dev（28 页全 200）
> Git 归属：个人兼职 → RayChan98（cj226144）个人号，禁 grohoprecision-hub

## 决策记录

| 日期 | 决策 |
|:--|:--|
| 2026-08-24 | 品牌 = CamlockPro（camlockprohose.com 可注册，零黑历史）|
| 2026-08-24 | 旗舰 = Food Grade Hose（SERP 中国厂空白），次旗舰 = PTFE Hose（+68% 增长）|
| 2026-08-24 | clone nozzle-site-v2 骨架（同栈 Astro7+TWv4 工业流体品类最匹配）|
| 2026-08-24 | 表单 = Zoho OAuth2（复用 PLEATPURE 同套凭据，FROM=raychan@pleatpure.com → TO=cj226144@gmail.com）|
| 2026-08-24 | 色板/LOGO 后置（内容先行，随时可换）|

## 站点结构（28 页）

- 首页 `/`：Hero + 8 产品分类网格 + Why CamlockPro + 最新指南
- 产品页 ×8：`/products/{food-grade,ptfe,chemical-transfer,hydraulic,silicone,suction-discharge,stainless-braided,hose-assemblies}/`
- 指南 ×7：`/guides/{food-grade-hose-selection,ptfe-hose-guide,chemical-hose-selection,hydraulic-hose-selection,silicone-hose-selection,suction-hose-selection,hose-assembly-guide}/`
- 核心页：About / Applications / OEM / Contact / Author / Thank-you
- 信任页：Terms / Privacy / Cookie

## 内容来源

- 产品/指南内容：`夜间预跑/03-页面内容提炼.md`（竞对 Orientflex/Besteflon/Viking 页面骨架提炼改写）
- 关键词：竞对页面提炼（food grade hose / ptfe hose / chemical transfer hose 等 11 簇）
- 口径红线：卖「纯净输送/认证/材质选型」，禁绝对化（软管=耗材）

## 部署

- CF Pages 项目：`camlockpro-site`（个人号账号 93eb74c...，production_branch=main）
- 部署命令：`HTTPS_PROXY=http://127.0.0.1:7897 CLOUDFLARE_API_TOKEN=$CF_PERSONAL_TOKEN CLOUDFLARE_ACCOUNT_ID=93eb74c... npx wrangler pages deploy dist --project-name=camlockpro-site`
- Zoho env 6 件套：PATCH 自 PLEATPURE 同套（ACCOUNT_ID/CLIENT_ID/SECRET/REFRESH_TOKEN/FROM/TO）
- 表单实测：`curl -X POST https://camlockpro-site.pages.dev/api/contact -d "name=..&email=..&message=.."` → `{"ok":true}`

## 待办

- [ ] 主人注册域名 camlockprohose.com（走 CF Registrar）
- [ ] 色板/LOGO 定稿（内容先行已满足，随时可换）
- [ ] 上线前 on-page SEO + technical SEO 检查（大范围）
- [ ] 记录表录入（飞书网站记录表，对齐 fullcolorcam）
- [ ] 内容增量：每产品类补 guide（对标 jeltecn 做法）+ 榜文「Top 10 Food Grade Hose Manufacturers」外链饵
