import os
import json
import base64
import requests
from bs4 import BeautifulSoup

# GitHub Repository Configurations
GH_TOKEN = os.getenv("GH_TOKEN")
GH_USER = os.getenv("GH_USER", "ezrawanyama74-commits")
GH_REPO = os.getenv("GH_REPO", "Ezrex-AI-bot")
FILE_PATH = "content.json"

def get_tech_news():
    try:
        url = "https://news.ycombinator.com/"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        top_story = soup.find('span', class_='titleline').find('a').text
        return top_story
    except Exception:
        return "New Artificial Intelligence and Web Technologies updates released."

def get_my_web_story():
    try:
        url = "https://the-smartphone-scientist.onrender.com"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        heading = soup.find('h1') or soup.find('h2')
        return heading.text.strip() if heading else "Ezra's Tech Innovations"
    except Exception:
        return "Ezra's Smartphone Development Studio & Projects"

def push_to_github(content_dict):
    """Pushes JSON directly to GitHub via REST API (No local git required)"""
    if not GH_TOKEN:
        print("GH_TOKEN missing. Writing locally instead.")
        with open("content.json", "w", encoding="utf-8") as f:
            json.dump(content_dict, f, indent=2, ensure_ascii=False)
        return

    api_url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{FILE_PATH}"
    headers = {"Authorization": f"Bearer {GH_TOKEN}", "Accept": "application/vnd.github.v3+json"}

    # Get current file SHA (required by GitHub API for updates)
    sha = None
    res = requests.get(api_url, headers=headers)
    if res.status_code == 200:
        sha = res.json().get("sha")

    json_str = json.dumps(content_dict, indent=2, ensure_ascii=False)
    encoded_content = base64.b64encode(json_str.encode("utf-8")).decode("utf-8")

    payload = {
        "message": "Cloud Auto-Scrape: Updated Sheng & English news",
        "content": encoded_content,
        "branch": "main"
    }
    if sha:
        payload["sha"] = sha

    put_res = requests.put(api_url, headers=headers, json=payload)
    if put_res.status_code in [200, 201]:
        print("✅ Cloud Scraper successfully pushed fresh JSON to GitHub!")
    else:
        print(f"❌ Failed to push to GitHub API: {put_res.status_code} - {put_res.text}")

def main():
    news_item = get_tech_news()
    personal_story = get_my_web_story()

    english_data = {
        "title": f"Tech Insight: {news_item[:45]}...",
        "body": f"Global Update: {news_item}. Meanwhile, on my main platform ({personal_story}), continuous deployment scripts are active."
    }
    sheng_data = {
        "title": f"Ma-News: {news_item[:35]}...",
        "body": f"Form ni hii: {news_item}. Nayo kwa site yangu-base ({personal_story}), ma-code ziko auto-pushed na cron jobs bila stress!"
    }

    push_to_github({"english": english_data, "sheng": sheng_data})

if __name__ == "__main__":
    main()
