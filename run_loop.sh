#!/bin/bash
if [ -f .env ]; then export $(cat .env | xargs); fi

while true; do
  echo "🚀 Running scraper update..."
  python scraper.py

  echo "📤 Pushing updated content.json to GitHub..."
  git add content.json
  git commit -m "Auto-update news content [cron]"
  git push https://${GH_TOKEN}@github.com/ezrawanyama74-commits/Ezrex-AI-bot-.git main

  echo "⏳ Sleeping for 10 minutes..."
  sleep 600
done
