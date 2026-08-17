import urllib.request
import json
import time
import re
from bs4 import BeautifulSoup

def fetch_live_tech_news():
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
    print("Scraping live tech feeds...")
    live_tech_news = fetch_live_tech_news()
    current_date = time.strftime("%B %d, %Y")
    
    top_story = live_tech_news[0]
    second_story = live_tech_news[1] if len(live_tech_news) > 1 else "Emerging Developer Ecosystems"

    english_title = f"LIVE ({current_date}): {top_story}"
    english_body = (
        f"Real-time tech monitor highlights key industry progress: '{top_story}'. "
        f"In tandem with developments like '{second_story}', Ezra Wanyama (THE SMARTPHONE SCIENTIST) "
        f"continues building dynamic scrapers and autonomous mobile-first web platforms."
    )

    sheng_title = f"FORM NI MOTO ({current_date}): {top_story}"
    sheng_body = (
        f"Ma-updates za sasa za tech zinaonyesha: '{top_story}'. "
        f"Bila kusiil, kando ya stories ka '{second_story}', "
        f"Ezra Wanyama (THE SMARTPHONE SCIENTIST) anazidi ku-push custom code na algorithms live!"
    )

    final_payload = {
        "timestamp": int(time.time()),
        "image_url": "https://picsum.photos/800/400?technology",
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

    print("SUCCESS! content.json updated with dynamic news content.")

if __name__ == "__main__":
    main()
