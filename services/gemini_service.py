# Services/gemini_service.py

import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

#* ~~ Simple text generation function ~~

async def generate_text(prompt: str) -> str:
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        print(f"An error occured with Gemini AI: {e}")
        return "Sorry, I'm having trouble thinking right now."
    