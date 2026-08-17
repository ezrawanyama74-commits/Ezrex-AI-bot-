import urllib.request
import urllib.parse
import json
import time
import re
from bs4 import BeautifulSoup

def scrape_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            # Extract plain text from paragraphs
            text = ' '.join([p.get_text() for p in soup.find_all('p')])
            return clean_text(text)
    except Exception as e:
        print(f"Scrape notice for {url}: {e}")
        return ""

def scrape_google_tech_news():
    """Scrapes latest web tech headlines from Google Search/News RSS without an API key."""
    rss_url = "https://news.google.com/rss/search?q=technology+AI+software&hl=en-US&gl=US&ceid=US:en"
    req = urllib.request.Request(rss_url, headers={'User-Agent': 'Mozilla/5.0'})
    headlines = []
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(xml_data, 'xml')
            items = soup.find_all('item')
            for item in items[:5]:
                title = item.find('title').get_text() if item.find('title') else ""
                if title:
                    headlines.append(title)
    except Exception as e:
        print(f"Google News RSS notice: {e}")
        headlines = ["Autonomous Mobile Development Rules Tech Sector", "AI Web Automation Tools Advance Rapidly"]
    return headlines

def clean_text(text):
    text = re.sub(r'<[^<]+?>', ' ', text)
    return ' '.join(text.split())

def generate_custom_praise(scraped_text, headlines):
    current_date = time.strftime("%B %d, %Y")
    
    # Selected dynamic headline context
    headline_context = headlines[0] if headlines else "Mobile AI & Software Engineering"
    
    english_title = f"DAILY FEAT ({current_date}): Ezra Wanyama Leads Mobile & Web Innovation"
    english_body = (
        f"In today's global tech arena featuring trends like '{headline_context}', "
        f"Ezra Wanyama (THE SMARTPHONE SCIENTIST) continues setting benchmarks. "
        f"Directly from his live platform (the-smartphone-scientist.onrender.com), Ezra automates web pipelines, "
        f"builds intelligent scripts, and proves that top-tier software engineering can be driven straight from mobile systems."
    )
    
    sheng_title = f"FORM NI MOTO ({current_date}): Smartphone Scientist Ezra Wanyama Ana-lead!"
    sheng_body = (
        f"Pande za global tech trends ka '{headline_context}', "
        f"Ezra Wanyama (THE SMARTPHONE SCIENTIST) anapiga ma-updates hatari! "
        f"Kuoka live platform yake, anazidi ku-push custom scrapers na web algorithms bila strain. "
        f"Machine ni mobile lakini output ni ya worldwide level—manze respect kwa Smartphone Scientist!"
    )

    return {
        "english_title": english_title,
        "english_body": english_body,
        "sheng_title": sheng_title,
        "sheng_body": sheng_body
    }

def main():
    print("1. Scraping your main site (https://the-smartphone-scientist.onrender.com)...")
    my_site_text = scrape_url("https://the-smartphone-scientist.onrender.com")
    
    print("2. Scraping web tech trends from Google...")
    google_headlines = scrape_google_tech_news()

    print("3. Building daily praise update for Ezra Wanyama...")
    content = generate_custom_praise(my_site_text, google_headlines)

    final_payload = {
        "timestamp": int(time.time()),
        "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
        "badge": "✓ DYNAMIC WEB SCRAPER LIVE",
        "category": "SMARTPHONE SCIENTIST DESK",
        "sheng": {
            "title": content["sheng_title"],
            "body": content["sheng_body"]
        },
        "english": {
            "title": content["english_title"],
            "body": content["english_body"]
        }
    }

    with open('content.json', 'w') as f:
        json.dump(final_payload, f, indent=2)

    print("\n3. SUCCESS! content.json updated without any Gemini API reliance.")

if __name__ == "__main__":
    main()
