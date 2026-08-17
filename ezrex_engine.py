import os
import json
import requests
from google import genai
from google.genai import types

# API Credentials
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")
SCHOOL_OF_TECH_API = "https://the-smartphone-scientist.onrender.com/school-of-tech/ingest"
API_KEY = "YOUR_SCHOOL_OF_TECH_KEY"

client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """
You are Ezrex AI Bot, the primary intelligence engine for 'THE SCHOOL OF TECH' under 'THE SMARTPHONE SCIENTIST'.

Task 1: CREDIBILITY FILTER
Check if the input has verifiable tech facts (benchmarks, official manufacturer releases, confirmed specs).
If it is unverified rumor or clickbait without evidence, set "is_credible": false and reject it.

Task 2: MAGAZINE CONTENT GENERATION
Generate structured JSON if credible:
- "is_credible": true/false
- "rejection_reason": "Reason if rejected"
- "magazine_title": "Clean, high-impact headline"
- "evidence_tag": "e.g., 'Official Launch', 'Geekbench Spec', 'FCC Certified'"
- "sheng_summary": "Descriptive, authentic urban Sheng' breakdown using technical terms accurately."
- "english_summary": "Professional International English editorial breakdown."

Output strictly raw JSON without markdown code fences.
"""

def process_and_post(raw_title, raw_body, source_image_url=None):
    prompt = f"Source Title: {raw_title}\n\nArticle Body: {raw_body}"

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.2,
                response_mime_type="application/json"
            ),
            contents=prompt
        )

        data = json.loads(response.text)

        if not data.get("is_credible"):
            print(f"🚫 Ezrex AI Bot Rejected: {raw_title}")
            return

        final_image = source_image_url or "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=1000&auto=format&fit=crop"

        payload = {
            "apiKey": API_KEY,
            "type": "story",
            "data": {
                "title": data["magazine_title"],
                "evidence_badge": data["evidence_tag"],
                "image_url": final_image,
                "sheng_content": data["sheng_summary"],
                "english_content": data["english_summary"],
                "author": "Ezrex AI Bot",
                "status": "PUBLISHED"
            }
        }

        res = requests.post(SCHOOL_OF_TECH_API, json=payload, timeout=10)
        if res.status_code == 200:
            print(f"✅ Ezrex AI Bot Published: {data['magazine_title']}")

    except Exception as e:
        print(f"❌ Ezrex AI Bot Error: {e}")

if __name__ == "__main__":
    print("Ezrex AI Bot Engine Ready.")
