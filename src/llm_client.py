# src/llm_client.py
import os
from dotenv import load_dotenv
from google import genai

# Load .env from project root
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "No API key found. Set GOOGLE_API_KEY or GEMINI_API_KEY in your .env or system env."
    )

# Pass the key explicitly to the client
client = genai.Client(api_key=api_key)

def get_gemini_response(prompt: str) -> str:
    resp = client.models.generate_content(
        model="gemini-2.5-flash",   # or "gemini-1.5-pro"
        contents=prompt
    )
    return resp.text
