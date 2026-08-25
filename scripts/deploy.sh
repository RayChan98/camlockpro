#!/usr/bin/env bash
# camlockpro-site 一键部署（CF Pages 个人号，项目名 camlockpro，分支 main）
# 用法: bash scripts/deploy.sh
# 坑: ① npx wrangler 会联网拉最新版卡死 → 用本地 node_modules/.bin/wrangler
#      ② 直连上传被墙 → 必须 export HTTPS_PROXY=7897（README 已记录）
#      ③ token 读 %LOCALAPPDATA%/hermes/.env 的 CF_PERSONAL_TOKEN
set -e
cd "$(dirname "$0")/.."

TOKEN=$(python -c "
import os,re
txt=open(os.path.expandvars(r'%LOCALAPPDATA%/hermes/.env'),encoding='utf-8',errors='replace').read()
print(re.search(r'CF_PERSONAL_TOKEN=(.+)',txt).group(1).strip().strip('\"'))
")
export CLOUDFLARE_API_TOKEN="$TOKEN"
export CLOUDFLARE_ACCOUNT_ID=93eb74c606d4eb51f1e2eb0cad15bd36
export HTTPS_PROXY=http://127.0.0.1:7897 HTTP_PROXY=http://127.0.0.1:7897

node node_modules/wrangler/bin/wrangler.js pages deploy dist --project-name=camlockpro --branch=main
