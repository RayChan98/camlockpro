#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PureFlow guides 批量生成：软管主题 guides（替换 nozzle 71 篇）"""
import json, os, re

OUT = r'D:\kravzik-work\pureflow-hose-site\src\content\guides'

GUIDES = [
  {
    'file': 'food-grade-hose-selection.md',
    'title': 'How to Choose a Food Grade Hose',
    'seoTitle': 'How to Choose a Food Grade Hose — Materials, Standards and Cleaning',
    'seoDesc': 'Food grade hose selection guide: FDA and 3-A standards, NBR vs EPDM vs UHMWPE vs silicone, temperature limits, and CIP cleaning considerations.',
    'primaryKeyword': 'food grade hose selection',
    'volume': 90,
    'kd': 3,
    'cluster': 'food-grade',
    'summary': 'How to choose a food grade hose: standards, materials, temperatures, cleaning regimes and the questions to ask before you buy.',
    'pubDate': '2026-08-20',
    'updated': '2026-08-24',
    'body': '''Choosing a food grade hose is a material decision first and a price decision second. The wrong compound taints the product or fails in the cleaning cycle — both expensive outcomes that a specification sheet prevents.

## Start With the Standards

The product you transfer decides the standard you must meet:

- **FDA 21 CFR 177.2600** — rubber compounds for repeated food contact (US)
- **FDA 21 CFR 177.1550** — PTFE for food contact
- **EU 1935/2004** — EU framework for food contact materials
- **3-A Sanitary Standards** — dairy and processing equipment (US)

Ask your supplier for the certificate. If they cannot produce one, the hose is not food grade.

## Match the Material to the Product

| Product | Recommended tube |
|:--|:--|
| Milk, juice, beer, soft drinks | EPDM |
| Edible oils, fats, shortening | NBR (nitrile) |
| Tomato paste, sauces, concentrate | UHMWPE lining |
| Wine, spirits | Clear PVC or EPDM |
| Aggressive CIP chemicals | UHMWPE or PTFE |
| Hot products / repeated autoclave | Platinum-cured silicone |

## Check the Temperature Range

Every compound has a window: EPDM roughly -30°C to 120°C, NBR similar, UHMWPE to about 80-90°C continuous, silicone -60°C to 200°C, PTFE to 260°C. Hot-fill products and steam cleaning both push the upper limit — size the hose for the cleaning cycle, not just the product temperature.

## Think About Cleaning

Food hoses must survive CIP (clean-in-place) cycles — caustic and acid washes, hot water, sometimes steam. A compound that is perfect for the product but fails in the washdown is the wrong choice. UHMWPE and PTFE linings win here because they resist the cleaning chemicals and stay smooth, so nothing holds on.

## The Questions to Ask Before Buying

1. What product, at what temperature?
2. What cleaning regime (chemicals, cycles, steam)?
3. What working pressure, what size?
4. Are assemblies needed, or bare hose?

Send us those four answers and we come back with a specification — not a catalogue page. See our [food grade hose range](/products/food-grade/).''',
  },
  {
    'file': 'ptfe-hose-guide.md',
    'title': 'PTFE Hose: The Complete Guide',
    'seoTitle': 'PTFE Hose Guide — Construction, Standards, Applications and Selection',
    'seoDesc': 'The complete PTFE hose guide: smooth bore vs convoluted, SAE 100R14, temperature and pressure limits, fittings, and which applications need PTFE.',
    'primaryKeyword': 'ptfe hose',
    'volume': 480,
    'kd': 8,
    'cluster': 'ptfe',
    'summary': 'Everything about PTFE hose: how it is constructed, smooth bore vs convoluted, SAE 100R14, limits, fittings and the applications that need it.',
    'pubDate': '2026-08-18',
    'updated': '2026-08-24',
    'body': '''PTFE hose is the answer when rubber cannot cope: aggressive chemicals, steam, high temperatures, or a product that must not be contaminated by its hose. It is also more expensive and less forgiving to handle than rubber — so the decision to use it should be deliberate.

## What PTFE Brings

Polytetrafluoroethylene is chemically inert to almost everything. It resists acids, bases, solvents and oxidisers across nearly the entire pH range, runs from cryogenic temperatures to 260°C continuous, and its non-stick bore means nothing adheres — the hose drains clean and stays clean.

## Construction Basics

Bare PTFE is limp, so every hose reinforces it. The standard construction: an extruded PTFE tube, one or two stainless steel braids, and optional rubber or steel cover. Terminations need specially designed fittings — the PTFE is too slick for a standard crimp to hold by friction alone, so fittings swage, clamp or use a collared design.

## Smooth Bore vs Convoluted

- **Smooth bore**: continuous tube, low pressure drop, easy to clean, best for hygienic and high-purity duties. More rigid.
- **Convoluted (corrugated)**: shaped tube that flexes with a tighter bend radius. Slightly rougher bore — fine for chemicals, not for hygienic duties.

## SAE 100R14

SAE 100R14 defines PTFE hose with stainless steel braid: bore sizes, pressure ratings and bend radii, so different makers' hoses interchange. Specify R14-compliant hose unless you have a reason not to.

## When PTFE Is the Right Call

- Saturated steam to 200°C+
- Concentrated acids and oxidisers
- Solvents that attack rubber
- Food and pharma lines needing steam-cleanable, non-reactive bores
- Hot-melt adhesives (non-stick bore)
- Fuel lines (conductive PTFE drains static)

## Selection Questions

Fluid, concentration, temperature, pressure, bore, end fittings, and whether you need conductive bore or abrasion cover. Answer those and the spec writes itself. Browse our [PTFE hose range](/products/ptfe/) or send the duty to us.''',
  },
  {
    'file': 'chemical-hose-selection.md',
    'title': 'Chemical Hose Selection: Lining, Construction and Compatibility',
    'seoTitle': 'Chemical Hose Selection — UHMWPE, PTFE and XLPE Linings Explained',
    'seoDesc': 'How to select a chemical transfer hose: UHMWPE vs PTFE vs XLPE linings, construction and reinforcement, and why compatibility data matters.',
    'primaryKeyword': 'chemical hose selection',
    'volume': 70,
    'kd': 2,
    'cluster': 'chemical-transfer',
    'summary': 'Chemical hose selection: how the lining is chosen for the fluid, construction for the pressure, and why compatibility data beats guesswork.',
    'pubDate': '2026-08-16',
    'updated': '2026-08-24',
    'body': '''Chemical hose fails one of two ways: the lining is attacked by the fluid, or the construction is wrong for the pressure. Both are preventable with a specification process that starts with the fluid, not the catalogue.

## The Lining Is the Decision

The lining touches the chemical, so it carries most of the compatibility burden:

- **UHMWPE** — broad resistance to acids, alkalis and solvents up to ~80°C. The workhorse lining: tough, non-reactive, cost-effective.
- **PTFE** — inert to virtually everything, higher temperature ceiling, steam-cleanable. The premium choice for the worst duties.
- **XLPE** — cross-linked polyethylene, a targeted option for a defined chemical range at moderate temperatures.

## Read the Compatibility Chart Properly

Compatibility data is quoted at a temperature — resistance changes with it. A chemical that is "compatible" at 20°C can attack the lining at 60°C. Always check the chart at your actual service temperature, and be suspicious of charts that quote no temperature at all.

## Construction Follows Pressure

Textile braid for 10 bar duties; spiral wire for higher pressure and full vacuum. The cover is chosen for the environment: EPDM for weather, CR for oil and abrasion. Anti-static (conductive) constructions are mandatory for many flammable solvents.

## Practical Checks

1. Chemical name, concentration and temperature
2. Working pressure and whether vacuum occurs (pump suction side)
3. Couplings — camlock, flange, threaded, or factory assemblies
4. Certification needed (ATEX, marine, food contact)

Get these four right and the hose will outlast the pump. See our [chemical transfer hose range](/products/chemical-transfer/).''',
  },
  {
    'file': 'hydraulic-hose-selection.md',
    'title': 'Hydraulic Hose Selection: R1 vs R2, Sizes and Pressure Ratings',
    'seoTitle': 'Hydraulic Hose Selection — SAE 100R1 vs 100R2, Sizes and Ratings',
    'seoDesc': 'Hydraulic hose selection guide: SAE 100R1 vs 100R2, working pressures by size, temperature limits and assembly considerations.',
    'primaryKeyword': 'hydraulic hose selection',
    'volume': 60,
    'kd': 2,
    'cluster': 'hydraulic',
    'summary': 'Hydraulic hose selection: what R1 and R2 mean, how to size by pressure and bore, and why assemblies should be factory made.',
    'pubDate': '2026-08-15',
    'updated': '2026-08-24',
    'body': '''A hydraulic hose failure is not a maintenance event — it is a safety event. High-pressure fluid releases with enough force to injure, so the selection process exists to keep the hose within its rating under every condition the machine sees.

## R1 vs R2 in Plain Terms

**SAE 100R1** is one wire braid. Working pressures from roughly 25 bar (2" bore) to 225 bar (1/4" bore). **SAE 100R2** is two wire braids — about 35% more pressure in the same size. Rule of thumb: R1 for return and medium lines, R2 for high-pressure circuits and where shock loads exist.

## Match Pressure to the System

The hose rating must exceed the system's maximum pressure — including spikes. A relief valve set at 150 bar does not protect a hose rated 130 bar, because the spike before the valve opens still counts. Size the hose to the spike, not the steady state.

## Sizes and Bends

Bore size decides flow and pressure drop; the bend radius decides where the hose can physically route. Forcing a hose below its bend radius is the fastest way to kill it — the reinforcement work-hardens and the tube fatigues.

## Assemblies: Make Them Factory Side

Field-assembled fittings are the weak link. Factory crimped assemblies on calibrated machines, pressure tested to 100%, remove the human error. If a machine shop in the field can crimp as well as the factory, great — otherwise buy tested assemblies.

## Quick Selection Checklist

1. System pressure, including spikes
2. Flow rate → bore size
3. Fluid and temperature range
4. Routing → bend radius and length
5. End fittings: JIC, BSP, NPT, flange
6. Factory crimped and tested

See our [hydraulic hose range](/products/hydraulic/) for R1/R2 in the full size range.''',
  },
  {
    'file': 'silicone-hose-selection.md',
    'title': 'Silicone Hose Selection: Food, Pharma and High-Temperature Duty',
    'seoTitle': 'Silicone Hose Selection — Platinum vs Peroxide Cure, Grades and Limits',
    'seoDesc': 'Silicone hose selection: platinum vs peroxide cure, food and pharma grades, temperature range, reinforcement options and when silicone beats rubber.',
    'primaryKeyword': 'silicone hose',
    'volume': 1400,
    'kd': 5,
    'cluster': 'silicone',
    'summary': 'Silicone hose selection: platinum vs peroxide cure, food and pharma grades, temperature and vacuum limits, and when silicone beats rubber.',
    'pubDate': '2026-08-14',
    'updated': '2026-08-24',
    'body': '''Silicone is the specialist's hose: it costs more than rubber, but it survives temperatures and cleaning cycles that rubber cannot. The selection question is when the premium is worth it.

## Platinum vs Peroxide Cure

The cure system decides purity. **Platinum (addition) cure** produces no by-products — cleaner, more consistent, first choice for food and pharma contact. **Peroxide cure** is cheaper but can leave residues that matter in closed systems. If the product touches the hose, specify platinum.

## Grades

- **Food grade**: FDA 21 CFR 177.2600, EU 1935/2004
- **Pharma grade**: USP Class VI, low extractables, autoclavable
- **Medical grade**: additional biocompatibility testing

## The Temperature Argument

Silicone runs -60°C to 200°C continuous — beyond EPDM's ceiling. That alone justifies it for steam vents, hot-air lines and process heat. Add repeated autoclaving (which kills most rubber) and the case closes.

## Reinforcement Options

Bare silicone handles gravity and low pressure. **Polyester braid** lifts working pressure for food transfer lines. **Stainless steel spiral** adds full-vacuum capability — the braided spiral silicone hose is the standard for sanitary vacuum duty.

## When Silicone Beats Rubber

- Continuous heat above 120°C
- Autoclave / SIP cycles
- Food or pharma contact requiring purity
- Odour- or taste-free transfer
- Peristaltic pump tubes needing flex life

## Selection Inputs

Product, temperature, pressure or vacuum, cleaning regime, bore size. Send them and we spec the grade and construction. Browse [silicone hoses](/products/silicone/).''',
  },
  {
    'file': 'suction-hose-selection.md',
    'title': 'Suction Hose Selection: Layflat, Wire-Reinforced and Heavy Duty',
    'seoTitle': 'Suction Hose Selection — Layflat vs Wire-Reinforced vs Heavy Duty',
    'seoDesc': 'How to choose a suction or discharge hose: layflat for light water duty, wire-reinforced for vacuum, heavy-duty for slurry and dredging.',
    'primaryKeyword': 'suction hose',
    'volume': 720,
    'kd': 4,
    'cluster': 'suction-discharge',
    'summary': 'Suction and discharge hose selection: layflat, wire-reinforced and heavy-duty constructions, vacuum capability and sizes.',
    'pubDate': '2026-08-13',
    'updated': '2026-08-24',
    'body': '''Suction and discharge hoses look similar but are engineered differently: suction hose resists collapse under vacuum, discharge hose resists burst under pressure. Many duties need both in one hose — the construction decides whether it survives.

## Layflat: Light and Cheap

Layflat discharge hose is the budget workhorse: light, collapsible, flat-packing, perfect for irrigation, dewatering and temporary lines. Working pressures typically 4-8 bar. Not for vacuum, not for abrasives — the walls are too thin.

## Wire-Reinforced: the Vacuum Answer

A PVC or rubber tube with an embedded helix wire holds the bore open under vacuum — the standard for pump suction lines, tanker loading and general industrial use. Choose PVC for economy, rubber for oil and abrasion resistance. Full vacuum capability with pressures to 10-20 bar.

## Heavy Duty: Slurry and Dredging

Abrasion-resistant tube (often wear-grade rubber), multiple reinforcement plies and a thick cover for sand, gravel, sludge and dredge spoil. The wear life is in the tube compound — specify by the abrasive and the velocity, not by price.

## Sizes

From 25 mm to 300 mm bore. Fittings: camlock (fast), flanged (permanent), threaded, or plain ends for clamp-on couplings.

## Selection Checklist

1. Duty: suction, discharge, or both
2. Fluid: water, slurry, abrasive, chemical
3. Vacuum or pressure rating needed
4. Temperature (hot water kills PVC)
5. Size and end fittings

See our [suction and discharge range](/products/suction-discharge/).''',
  },
  {
    'file': 'hose-assembly-guide.md',
    'title': 'Hose Assemblies: Crimping, Fittings and Test Certificates',
    'seoTitle': 'Hose Assembly Guide — Crimping, Fittings, Testing and Certification',
    'seoDesc': 'Hose assembly guide: how factory crimping works, fitting types, why pressure testing matters, and what a test certificate proves.',
    'primaryKeyword': 'hose assembly',
    'volume': 260,
    'kd': 4,
    'cluster': 'hose-assemblies',
    'summary': 'Hose assemblies explained: why factory crimping beats field fitting, fitting types, pressure testing, and what certificates you should expect.',
    'pubDate': '2026-08-12',
    'updated': '2026-08-24',
    'body': '''A hose assembly is a pressure vessel in miniature — and like any pressure vessel, it is only as safe as its weakest joint. In practice that joint is the fitting, which is why factory crimping and testing matter.

## Why Crimp, Not Just Push On

Push-on and clamp fittings work at low pressure. Above that, the fitting must be mechanically locked to the hose — the crimp compresses the ferrule into the hose reinforcement so the two become one. A correct crimp holds at the hose's full rating; a bad crimp fails at a fraction of it.

## The Factory Advantage

Factory crimping uses calibrated machines with documented settings per hose/fitting combination, controlled skiving (removal of the cover where required), and trained operators. Field crimping with a hand tool and a guess is how assemblies fail. There is no substitute for the controlled process.

## Fitting Types

- **JIC / BSP / NPT** — threaded hydraulic ends
- **Flange** — SAE flange ends for large bores and high pressure
- **Tri-clamp** — sanitary connections for food and pharma
- **Barb / hose tail** — push-on low-pressure ends
- **Camlock** — fast connect/disconnect for transfer lines

## What the Test Certificate Proves

Every assembly we ship is pressure tested to 100% of working pressure. The certificate records the test pressure, the date, the operator and the hose/fitting spec — traceability that protects you in an audit and in the field.

## When to Specify Assemblies

- Safety-critical lines (hydraulic, steam, chemical)
- Food and pharma lines where traceability is audited
- Any line where a field failure means downtime

See our [hose assemblies](/products/hose-assemblies/) or send your duty for a build-and-test quote.''',
  },
]

# 清理旧 guides
for f in os.listdir(OUT):
    if f.endswith('.md'):
        os.remove(os.path.join(OUT, f))

for g in GUIDES:
    body = g.pop('body')
    front = '---\n'
    for k, v in g.items():
        if isinstance(v, str):
            front += f'{k}: "{v}"\n'
        else:
            front += f'{k}: {v}\n'
    front += '---\n\n'
    with open(os.path.join(OUT, g['file']), 'w', encoding='utf-8', newline='\n') as f:
        f.write(front + body)
    print('written:', g['file'])
