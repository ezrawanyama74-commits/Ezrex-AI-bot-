import urllib.request
import urllib.parse
import json
import time
import re
from bs4 import BeautifulSoup

def scrape_my_website():
    """Scrapes actual headings, paragraphs, and text sections from live site."""
    url = "https://the-smartphone-scientist.onrender.com"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    scraped_snippets = []
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            html = response.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            
            # Target specific meaningful tags
            elements = soup.find_all(['h1', 'h2', 'h3', 'p', 'article', 'section'])
            for el in elements:
                clean = clean_text(el.get_text())
                if len(clean) > 25 and clean not in scraped_snippets:
                    scraped_snippets.append(clean)
                    
            if scraped_snippets:
                return " | ".join(scraped_snippets[:5])
    except Exception as e:
        print(f"Main site scrape error: {e}")
    
    return "Ezra Wanyama (The Smartphone Scientist) builds autonomous AI scrapers and mobile web platforms."

def scrape_google_tech():
    """Scrapes top real-time tech news from Google News RSS."""
    rss_url = "https://news.google.com/rss/search?q=technology+AI+software&hl=en-US&gl=US&ceid=US:en"
    req = urllib.request.Request(rss_url, headers={'User-Agent': 'Mozilla/5.0'})
    headlines = []
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(xml_data, 'xml')
            items = soup.find_all('item')
            for item in items[:3]:
                title = item.find('title').get_text() if item.find('title') else ""
                if title:
                    headlines.append(clean_text(title))
    except Exception as e:
        print(f"Google news scrape error: {e}")
        
    return headlines if headlines else ["AI Web Automation Tools Advance Rapidly"]

def clean_text(text):
    text = re.sub(r'<[^<]+?>', ' ', text)
    return ' '.join(text.split())

def main():
    print("1. Scraping live content from https://the-smartphone-scientist.onrender.com...")
    live_site_data = scrape_my_website()
    
    print("2. Fetching real-time tech developments from Google...")
    live_tech_news = scrape_google_tech()
    
    current_date = time.strftime("%B %d, %Y")
    top_news = live_tech_news[0]

    # Generate custom praise integrating actual extracted site data
    english_title = f"LIVE FEAT ({current_date}): Ezra Wanyama Drives Next-Gen Innovation"
    english_body = (
        f"Real-time extraction from 'the-smartphone-scientist.onrender.com' highlights: '{live_site_data[:220]}...'. "
        f"Amid global movements like '{top_news}', Ezra Wanyama (THE SMARTPHONE SCIENTIST) "
        f"demonstrates elite mobile engineering and web automation directly on live infrastructure."
    )

    sheng_title = f"FORM NI MOTO ({current_date}): Smartphone Scientist Ezra Wanyama Ana-lead!"
    sheng_body = (
        f"Data live kutoka site (the-smartphone-scientist.onrender.com) inaonyesha: '{live_site_data[:200]}...'. "
        f"Kwenye ma-updates za tech za sasa ka '{top_news}', "
        f"Ezra Wanyama (THE SMARTPHONE SCIENTIST) anazidi ku-push code na scrapers live—machine ni mobile lakini output ni ya top tier!"
    )

    final_payload = {
        "timestamp": int(time.time()),
        "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
        "badge": "✓ DYNAMIC SCRAPER LIVE",
        "category": "SMARTPHONE SCIENTIST DESK",
        "sheng": {
            "title": sheng_title,
            "body": sheng_body
        },
        "english": {
            "title": english_title,
            "body": english_body
        }
    }

    with open('content.json', 'w') as f:
        json.dump(final_payload, f, indent=2)

    print("\n3. SUCCESS! content.json dynamically updated with live site extractions.")

if __name__ == "__main__":
    main()
