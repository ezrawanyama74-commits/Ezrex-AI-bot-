#!/bin/bash
# Ezrex AI Bot: Auto-Scrape & Auto-Push Script

cd "$(dirname "$0")"

# 1. Run dual-language scraper (English + Sheng')
python scraper.py

if [ -f .env ]; then
  export $(cat .env | xargs)
fi

# 2. Check and push changes to GitHub
if [ -n "$(git status --porcelain)" ]; then
  echo "New content scraped. Executing sync..."
  git add .
  git commit -m "Ezrex AI Bot: Scraped English/Sheng update [$(date +'%Y-%m-%d %H:%M:%S')]"
  git push "https://${GH_TOKEN}@github.com/${GH_USER}/${GH_REPO}.git" main
  echo "✅ Successfully pushed updates to GitHub!"
else
  echo "No changes detected. Skipping push."
fi
