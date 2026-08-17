import json
import time

def fetch_and_synthesize():
    print("🤖 Ezrex Bot updating content and images...")

    # Reliable direct image URLs from Unsplash
    tech_images = [
        "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1531297484001-80022131f5a1?auto=format&fit=crop&w=800&q=80"
    ]

    selected_img = tech_images[int(time.time()) % len(tech_images)]

    payload = {
        "timestamp": int(time.time()),
        "image_url": selected_img,
        "badge": "✓ LIVE UPDATE",
        "category": "TECH INSIGHTS",
        "sheng": {
            "title": "MA-NEWS: AI;DR (AI; DIDN'T READ)...",
            "body": "Form ni hii: AI;DR (AI; Didn't Read). Nayo kwa site yangu-base (Ezra Wanyama), ma-code ziko auto-pushed na cron jobs bila stress!"
        },
        "english": {
            "title": "TECH INSIGHT: AI;DR (AI; DIDN'T READ)...",
            "body": "Global Update: AI;DR (AI; Didn't Read). Meanwhile, on my main platform (Ezra Wanyama), continuous deployment scripts and automated cron jobs are active."
        }
    }

    with open('content.json', 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)

    print("✅ content.json written successfully with active image_url!")

if __name__ == '__main__':
    fetch_and_synthesize()
