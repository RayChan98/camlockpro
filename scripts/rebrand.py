#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PureFlow 品牌替换：bj- -> pf-，BoreJet/borejet -> PureFlow/pureflow，全站 src/ 批量"""
import os, re

ROOT = r'D:\kravzik-work\pureflow-hose-site\src'
SKIP_DIRS = {'node_modules', 'dist', '.git', '.astro'}

def walk():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(('.astro', '.ts', '.tsx', '.js', '.mjs', '.json', '.css', '.md', '.svg')):
                yield os.path.join(dirpath, fn)

# 替换映射：先长后短
REPL = [
    ('BoreJet', 'PureFlow'),
    ('borejet', 'pureflow'),
    ('BOREJET', 'PUREFLOW'),
    ('bj-accent', 'pf-accent'),
    ('bj-', 'pf-'),
]

changed = []
for fp in walk():
    try:
        with open(fp, encoding='utf-8') as f:
            t = f.read()
    except Exception:
        continue
    orig = t
    for a, b in REPL:
        t = t.replace(a, b)
    if t != orig:
        with open(fp, 'w', encoding='utf-8', newline='') as f:
            f.write(t)
        changed.append(fp)

print(f'替换完成: {len(changed)} 文件')
for c in changed:
    print(' ', c.replace(ROOT, 'src'))
