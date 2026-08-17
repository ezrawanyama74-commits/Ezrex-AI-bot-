import requests
from bs4 import BeautifulSoup
import json
import random

def get_tech_news():
    """Scrapes external news/RSS feeds"""
    try:
        # Example target: Fetching tech/academic updates from an open feed
        url = "https://news.ycombinator.com/"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Grab top story title
        top_story = soup.find('span', class_='titleline').find('a').text
        return top_story
    except Exception as e:
        return "New Artificial Intelligence and Web Technologies updates released."

def get_my_web_story():
    """Scrapes personal bio/updates from your live Render site"""
    try:
        url = "https://the-smartphone-scientist.onrender.com"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract main header or paragraph text from your site
        heading = soup.find('h1') or soup.find('h2')
        story = heading.text.strip() if heading else "Ezra's Tech Innovations"
        return story
    except Exception as e:
        return "Ezra's Smartphone Development Studio & Projects"

def build_dual_payload():
    news_item = get_tech_news()
    personal_story = get_my_web_story()
    
    # 1. English Content Version
    english_data = {
        "title": f"Tech Insight: {news_item[:45]}...",
        "body": f"Global Update: {news_item}. Meanwhile, on my main platform ({personal_story}), continuous deployment scripts are active."
    }
    
    # 2. Sheng' Content Version
    sheng_data = {
        "title": f"Ma-News: {news_item[:35]}...",
        "body": f"Form ni hii: {news_item}. Nayo kwa site yangu-base ({personal_story}), ma-code ziko auto-pushed na cron jobs bila stress!"
    }
    
    payload = {
        "english": english_data,
        "sheng": sheng_data
    }
    
    with open("content.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        
    print(" Successfully scraped news + web story into English and Sheng'!")

if __name__ == "__main__":
    build_dual_payload()
