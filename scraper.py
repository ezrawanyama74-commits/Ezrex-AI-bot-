import json

def scrape_dual_content():
    # 1. Fetch English source content
    english_data = {
        "title": "Academic Updates & Notes",
        "body": "Detailed summary of upcoming study materials and exam review notes."
    }
    
    # 2. Fetch/Format Sheng' translation content
    sheng_data = {
        "title": "Ma-Info na Notes za Chuo",
        "body": "Summary mob ya masomo na ma-notes za kucrack izi exams vizuri."
    }
    
    # 3. Store both sections for the web frontend dual tabs
    payload = {
        "english": english_data,
        "sheng": sheng_data
    }
    
    with open("content.json", "w") as f:
        json.dump(payload, f, indent=2)
    print("Dual-language content scraped successfully!")

if __name__ == "__main__":
    scrape_dual_content()
