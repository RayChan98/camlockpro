#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T-41 CamlockPro 产品页批量生成（材质×类型×尺寸矩阵，参数=竞对公开值 competitor-reference）"""
import os

OUT = r"F:/kravzik建站信息/Hermes全自动网站运营/快速建站实验/camlockpro-site/src/content/products"
os.makedirs(OUT, exist_ok=True)

# 每个产品：slug, title, seoTitle, seoDesc, kw, category, summary, 参数表行, FAQ
P = [
 dict(slug="aluminum-camlock-couplings", title="Aluminum Camlock Couplings",
  seoTitle="Aluminum Camlock Couplings | Type A-F, 1/2\"-6\" | CamlockPro",
  seoDesc="Cast aluminum cam and groove couplings (types A-F, DC, DP) in 1/2\" to 6\". A-A-59326D standard, EPDM/NBR/Viton gaskets. Factory direct pricing.",
  kw="aluminum camlock coupling", category="aluminum",
  summary="Cast aluminum camlock couplings for water, fuel, agriculture and general transfer. Types A-F, DC and DP in 1/2\" to 6\", A-A-59326D compliant.",
  spec="""| Size | Working pressure | Temperature range |
|:--|:--|:--|
| 1/2\" – 2\" | 200 psi | -25°C to +80°C (EPDM) |
| 3\" | 125 psi | -25°C to +80°C (EPDM) |
| 4\" | 110 psi | -25°C to +80°C (EPDM) |
| 6\" | 60 psi | -25°C to +80°C (EPDM) |""",
  faq=[("What sizes are available?", "Aluminum camlocks are stocked from 1/2\" to 6\" nominal hose/pipe bore, with 3/4\" and 1-1/4\" also common. Type A through F plus DC and DP are all available in each size."),
       ("Which gaskets come standard?", "Standard fitment is EPDM. NBR (oil/fuel), Viton (chemicals) and PTFE (aggressive acids) options are available for the same coupling body."),
       ("Can aluminum camlocks handle potable water?", "Yes — aluminum couplings are widely used in agriculture and water transfer. For continuous potable water duty, specify food-grade gaskets.")]),
 dict(slug="stainless-steel-camlock-couplings", title="Stainless Steel Camlock Couplings",
  seoTitle="Stainless Steel Camlock Couplings | 304/316 | CamlockPro",
  seoDesc="304 and 316 stainless steel camlock couplings for food, chemical and marine duty. Types A-F in 1/2\" to 6\", 250 psi rated, A-A-59326D.",
  kw="stainless steel camlock coupling", category="stainless-steel",
  summary="304/316 stainless cam and groove couplings for food, beverage, chemical and marine applications. 1/2\" to 6\", 250 psi working pressure.",
  spec="""| Size | Working pressure | Temperature range |
|:--|:--|:--|
| 1/2\" – 2\" | 250 psi | -30°C to +150°C (EPDM) |
| 3\" | 150 psi | -30°C to +150°C (EPDM) |
| 4\" | 130 psi | -30°C to +150°C (EPDM) |
| 6\" | 70 psi | -30°C to +150°C (EPDM) |""",
  faq=[("304 or 316?", "304 covers most food, water and mild chemical duty. 316 adds molybdenum for chloride and marine environments, acids and saltwater — specify 316 for coastal or aggressive media."),
       ("Is stainless food-safe?", "Yes. 304/316 stainless with food-grade EPDM or Viton gaskets is the standard choice for dairy, beverage and edible oil lines."),
       ("Do stainless camlocks cost much more?", "Roughly 2.5-4x aluminum per piece, but the corrosion life and reusability in food/chemical plants usually pay it back quickly.")]),
 dict(slug="brass-camlock-couplings", title="Brass Camlock Couplings",
  seoTitle="Brass Camlock Couplings | Fuel & Gas Rated | CamlockPro",
  seoDesc="Machined brass cam and groove couplings for fuel, gas and high-pressure lines. Types A-F, 1/2\" to 4\", NPT and BSPT threads.",
  kw="brass camlock coupling", category="brass",
  summary="Machined brass camlock couplings for fuel transfer, gas lines and high-pressure hydraulic use. Types A-F in 1/2\" to 4\".",
  spec="""| Size | Working pressure | Temperature range |
|:--|:--|:--|
| 1/2\" – 2\" | 250 psi | -30°C to +120°C |
| 3\" | 150 psi | -30°C to +120°C |
| 4\" | 120 psi | -30°C to +120°C |""",
  faq=[("Why choose brass over aluminum?", "Brass handles higher thread strength, better spark resistance in fuel/gas environments, and repeated connect-disconnect cycles without galling."),
       ("Which threads?", "NPT (US) and BSPT (UK/EU) are both stocked. Confirm your standard before ordering — they are not interchangeable."),
       ("Can brass camlocks handle gasoline?", "Yes. Brass with NBR gaskets is the standard combination for gasoline, diesel and lube oil transfer.")]),
 dict(slug="polypropylene-camlock-couplings", title="Polypropylene Camlock Couplings",
  seoTitle="Polypropylene Camlock Couplings | Chemical Rated | CamlockPro",
  seoDesc="Lightweight polypropylene cam and groove couplings for acids, solvents and deionized water. Types A-F in 1/2\" to 4\", 150 psi.",
  kw="polypropylene camlock coupling", category="polypropylene",
  summary="Polypropylene camlock couplings for aggressive chemical transfer, DI water and food handling. 1/2\" to 4\", corrosion-proof and lightweight.",
  spec="""| Size | Working pressure | Temperature range |
|:--|:--|:--|
| 1/2\" – 2\" | 150 psi | -20°C to +70°C |
| 3\" – 4\" | 100 psi | -20°C to +70°C |""",
  faq=[("What chemicals can PP camlocks handle?", "PP resists most acids, alkalis, solvents and deionized water at ambient temperature. For hot or concentrated chemicals, check the compatibility chart or specify PTFE gaskets."),
       ("Are PP camlocks food safe?", "Yes, PP with food-grade EPDM gaskets is used in food plants, breweries and potable water systems."),
       ("Why choose PP over metal?", "Half the weight of aluminum, zero corrosion, no galvanic issues, and lower cost — ideal for chemical plants and mobile transfer.")]),
 dict(slug="camlock-fittings-adapters", title="Camlock Fittings & Adapters",
  seoTitle="Camlock Fittings & Adapters | Threaded, Reducer, Flange | CamlockPro",
  seoDesc="Camlock threaded adapters, reducers, hose shanks, elbows and flanges — connect camlocks to pipes, hoses, tanks and IBC totes.",
  kw="camlock adapter", category="fittings-adapters",
  summary="Threaded adapters, reducers, hose shanks, elbows and flanges that connect camlock couplings to pipes, hoses, tanks and IBC totes.",
  spec="""| Fitting type | Connection ends | Typical use |
|:--|:--|:--|
| Threaded adapter (A/B) | Camlock × NPT/BSPT | Pipe, pump and equipment connections |
| Hose shank (C/E) | Camlock × barbed hose | Hose-end connections with clamps |
| Reducer | Two camlock sizes | Stepping between hose/pipe sizes |
| Flange adapter | Camlock × ANSI flange | Tank and manifold connections |
| Elbow (45°/90°) | Camlock × camlock | Tight-space routing |""",
  faq=[("Which adapter do I need?", "Check what's on the other end: threaded pipe needs type A (male) or B (female) with NPT/BSPT threads; hose needs type C/E hose shank; flanges need a flange adapter."),
       ("Can adapters change camlock size?", "Yes — reducers connect a larger coupling to a smaller hose or pipe. Always size the camlock to the LARGER bore."),
       ("Are adapters compatible across brands?", "Yes. Cam and groove fittings follow the A-A-59326D profile, so CamlockPro adapters mate with Dixon, Banjo, PT and other standard camlocks.")]),
 dict(slug="camlock-gaskets-seals", title="Camlock Gaskets & Seals",
  seoTitle="Camlock Gaskets | EPDM, NBR, Viton, PTFE | CamlockPro",
  seoDesc="Camlock replacement gaskets in EPDM, NBR, Viton and PTFE for every size 1/2\" to 6\". The part that actually makes the seal.",
  kw="camlock gasket", category="gaskets-seals",
  summary="Replacement camlock gaskets in EPDM, NBR, Viton and PTFE — the sealing element behind every leak-free cam and groove connection.",
  spec="""| Material | Temp range | Best for |
|:--|:--|:--|
| EPDM | -30°C to +150°C | Water, weather, mild chemicals (standard) |
| NBR | -30°C to +100°C | Oil, fuel, hydraulic fluids |
| Viton (FKM) | -20°C to +200°C | Aggressive chemicals, aromatics |
| PTFE | -50°C to +230°C | Strong acids, solvents, purity |""",
  faq=[("How often should gaskets be replaced?", "Inspect at every disconnect. Soft, cracked or flattened gaskets leak — replace before a spill, not after."),
       ("Are gaskets size-specific?", "Yes. A 2\" camlock gasket fits only 2\" camlocks. Order by coupling size and material compatibility."),
       ("Can I upgrade my gasket material?", "Yes — any standard camlock accepts any of the four gasket materials. Swapping in Viton or PTFE upgrades chemical resistance without changing the coupling.")]),
 dict(slug="camlock-dust-caps-plugs", title="Camlock Dust Caps & Plugs",
  seoTitle="Camlock Dust Caps & Plugs | Type DC & DP | CamlockPro",
  seoDesc="Type DC camlock dust caps and DP dust plugs keep open coupling ends clean, safe and drip-free. All materials, 1/2\" to 6\".",
  kw="camlock dust cap", category="dust-caps-plugs",
  summary="Type DC dust caps and DP dust plugs for every camlock size — keep hose ends clean, capped and safe between connections.",
  spec="""| Type | Connects to | Purpose |
|:--|:--|:--|
| DC (dust cap) | Female coupler (B/D/F) | Caps the female end |
| DP (dust plug) | Male adapter (A/C/E) | Plugs the male end |""",
  faq=[("Do I need both caps and plugs?", "One DC caps a female end, one DP plugs a male end. If both halves of a hose assembly stay connected, you need one of each."),
       ("Are dust caps leak-proof?", "They seal against drips and dust when the coupling is not in use — they are not rated for working pressure."),
       ("What materials?", "Aluminum, stainless steel, brass and polypropylene to match your coupling body and duty.")]),
 dict(slug="camlock-parts-accessories", title="Camlock Parts & Accessories",
  seoTitle="Camlock Parts: Lever Arms, Safety Pins, Chains | CamlockPro",
  seoDesc="Replacement camlock lever arms, safety pins, chains and wrenches. Keep couplings in service — same A-A-59326D profile.",
  kw="camlock replacement parts", category="accessories",
  summary="Replacement lever arms, safety pins, chains and service parts for cam and groove couplings of every standard brand.",
  spec="""| Part | Fits | Note |
|:--|:--|:--|
| Lever arm assembly | Types B/D/F couplers | Includes cams + pins |
| Safety pin + chain | All types | Prevents accidental release |
| Cam arm spring | B/D/F couplers | Restores arm tension |
| Coupling wrench | 1/2\"-6\" | For stubborn connections |""",
  faq=[("Can I rebuild a worn coupling?", "Yes — lever arm assemblies and cams are replaceable. If the body or groove is scored, replace the whole coupling."),
       ("Do spare parts fit Dixon/Banjo camlocks?", "Standard A-A-59326D profile parts are interchangeable across brands, but always confirm with a sample or drawing."),
       ("What causes camlocks to fail?", "Worn gaskets (most common), bent lever arms from over-tightening, and damaged grooves from dragging on the ground. Inspect both halves each use.")]),
]

for p in P:
    body = f"""# {p['title']}

{p['summary']}

## Specifications

{p['spec']}

**Standard:** A-A-59326D (formerly MIL-C-27487) profile — interchangeable with Dixon, Banjo, PT and other standard cam and groove couplings.

## Why choose CamlockPro

- Factory-direct pricing on matched material × type × size combinations
- Every size stocked with EPDM gaskets standard; NBR, Viton and PTFE on request
- OEM branding and custom machining available from 500 pcs
- Technical support confirms type, size and gasket before you commit

## Applications

- {p.get('apps', 'Water, fuel, chemical, food and general transfer lines')}

## FAQ

"""
    for q, a in p['faq']:
        body += f"**{q}**\n\n{a}\n\n"
    body += """---
*Specifications are reference values compiled from public industry sources and pending factory verification. Confirm ratings with our team before final specification.*
"""
    fm = f"""---
title: "{p['title']}"
seoTitle: "{p['seoTitle']}"
seoDesc: "{p['seoDesc']}"
primaryKeyword: "{p['kw']}"
category: "{p['category']}"
summary: "{p['summary']}"
specSource: "competitor-reference"
specSourceNote: "Reference data compiled from public industry sources — pending factory verification."
noindex: false
order: 1
updated: 2026-08-23
---
{body}"""
    with open(os.path.join(OUT, p['slug'] + ".md"), "w", encoding="utf-8", newline="") as f:
        f.write(fm)
    print("OK", p['slug'])
print("total:", len(P))
