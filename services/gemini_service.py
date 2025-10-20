# Services/gemini_service.py

import google.generativeai as genai
from config import GEMINI_API_KEY
from prompts import BOT_PERSONALITY_PROMPT

genai.configure(api_key=GEMINI_API_KEY)

#* ~~ Simple text generation function ~~

async def generate_text(user_question: str) -> str:
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        full_prompt = f"{BOT_PERSONALITY_PROMPT}\n\n--- HUMAN QUESTION ---\n{user_question}"
        
        response = await model.generate_content_async(full_prompt)
        return response.text
    except Exception as e:
        print(f"An error occured with Gemini AI: {e}")
        return "Sorry, I'm having trouble thinking right now."
    