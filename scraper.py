import json
import urllib.request
import xml.etree.ElementTree as ET
import time

def fetch_live_news():
    print("🌐 Fetching live RSS feed from the web...")
    url = "https://news.ygoogle.com/rss/search?q=technology&hl=en-US&gl=US&ceid=US:en"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
        
        root = ET.fromstring(xml_data)
        item = root.find('.//item')
        
        title = item.find('title').text if item is not None else "Latest AI & Tech Updates"
        link = item.find('link').text if item is not None else "#"
        
        payload = {
            "timestamp": int(time.time()),
            "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
            "badge": "✓ LIVE WEB UPDATE",
            "category": "BREAKING TECH",
            "sheng": {
                "title": f"MA-NEWS: {title[:50]}...",
                "body": f"Form ni hii: {title}. Continuous cloud deployment ina-fetch data live bila ya laptop/phone baseline!"
            },
            "english": {
                "title": f"UPDATE: {title[:50]}...",
                "body": f"{title}. Automatically synced from live web sources."
            }
        }
        
        with open('content.json', 'w', encoding='utf-8') as f:
            json.dump(payload, f, indent=2)
            
        print("✅ Live dynamic content saved to content.json")
    except Exception as e:
        print(f"❌ Error fetching live news: {e}")

if __name__ == '__main__':
    fetch_live_news()
