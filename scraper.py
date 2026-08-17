import urllib.request
import xml.etree.ElementTree as ET
import json
import time

def fetch_live_news():
    url = "https://news.google.com/rss/search?q=technology+ai&hl=en-US&gl=US&ceid=US:en"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            # Get the first live headline
            item = root.find('.//item')
            if item is not None:
                title = item.find('title').text if item.find('title') is not None else "Latest Tech Update"
                link = item.find('link').text if item.find('link') is not None else ""
                
                # Format into JSON payload
                data = {
                    "timestamp": int(time.time()),
                    "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
                    "badge": "✓ LIVE NEWS",
                    "category": "TECH BREAKING",
                    "sheng": {
                        "title": f"MA-NEWS: {title[:50]}...",
                        "body": f"Form ni hii: {title}. Cheki full details hapa link-i kwa web!"
                    },
                    "english": {
                        "title": title,
                        "body": f"Breaking Tech Update: {title}. Scraped directly from live global feeds."
                    }
                }
                
                with open('content.json', 'w') as f:
                    json.dump(data, f, indent=2)
                print("Successfully updated content.json with live web news!")
            else:
                print("No news items found.")
    except Exception as e:
        print(f"Error scraping live news: {e}")

if __name__ == "__main__":
    fetch_live_news()
