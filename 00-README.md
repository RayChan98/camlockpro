# CAMLOCKPRO — Camlock 快速接头 B2B 独立站

> 域名：**camlockpro.com**（2026-08-23 拟定，待主人/总控注册，当前 **https://camlockpro.pages.dev** 顶着）
> 品牌：CamlockPro — Cam and Groove Couplings（凸轮锁紧快速接头）
> 技术栈：Astro 7 + Tailwind v4（照 fullcolorcam 原生模式，**不 clone molditquick**）
> 状态：✅ 已上线（25→31 页全 200）/ 表单 Zoho ok:true / sitemap 24 条 / 死链 0
> 归属：**个人兼职线**（git 仓 RayChan98/camlockpro，禁 grohoprecision-hub）

## 决策记录

| 日期 | 决策 |
|:--|:--|
| 2026-08-23 | T-41 候选池开群（7 维重估 86 分），M1 三查完成（303 词池/主词+45%/+104%），建议做 |
| 2026-08-23 | 夜间预跑①②③④完成（竞对清单 25+ 域名三分类/内容策略 8 页面类型/8 词簇提炼/范本自审 19/20） |
| 2026-08-23 | 建站：clone pureflow-hose-site 换肤 CamlockPro（30 文件零残留），CF 个人号部署 |
| 2026-08-23 | 建站边界：材质（铝/SS/黄铜/PP）×类型（A-F/DC/DP）×尺寸（1/2"-6"）选型矩阵站 |

## 关键资产

- 竞对清单：`F:/kravzik建站信息/Hermes全自动网站运营/选品研究/候选产品池/T-41-Camlock快接/02-竞对主域名清单.md`
- 内容策略：同目录 `03-竞对内容策略分析.md` + `04-页面内容提炼.md`（8 词簇×8 骨架）
- 范本自审：同目录 `05-范本自审记录.md` + `范本/camlock-coupling-types-guide.md`
- 选品报告：同目录 `01-选品报告-Camlock快接-M1.md`

## 技术要点（换肤坑，防复踩）

- clone 兄弟站后 **astro.config.mjs site:** + **robots.txt Sitemap:** + public 孤儿品牌文件三处必改，否则 sitemap 域名错
- content.config.ts 产品 `category` enum 必须先行改（产品 md 才跟得上）
- frontmatter 值含 `"`（如 1/2"）→ 用单引号包裹或转义，否则 js-yaml 崩
- pf-* 类前缀是品牌专属（scoped 组件样式），换肤时定义与用法一起改
- CF Pages 个人号：`CF_PERSONAL_TOKEN`/`CF_PERSONAL_ACCOUNT_ID`（.env），wrangler 需 export HTTPS_PROXY=7897

## 待办

- [ ] 主人/总控注册 camlockpro.com（走 CF Registrar）→ canonical 自动生效
- [ ] git push（github.com 被墙瞬态，api 通主站不通，恢复后推 RayChan98/camlockpro）
- [ ] 内容增量：剩余词簇指南（燃料/食品级/水/消防/IBC 应用 + Top10 listicle 外链饵）
- [ ] 核心词 ≥3000 字深度指南扩充（类型指南扩到 3000+）
- [ ] 飞书网站记录表（seo-page-tracker 批量录入）
- [ ] on-page/technical SEO 终检（title/desc/canonical 已过，补 structured data 复核）
- [ ] 产品图管线（素材后置，色板/LOGO 随时可换）
