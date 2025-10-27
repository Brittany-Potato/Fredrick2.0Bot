# Services/gemini_service.py

import google.generativeai as genai
from config import GEMINI_API_KEY
from prompts import BOT_PERSONALITY_PROMPT
from services.memory_service import get_user_memories, get_nickname

genai.configure(api_key=GEMINI_API_KEY)

async def generate_text(user_question: str, user_id: str = None, platform: str = None) -> str:
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        context_facts = ""
        if user_id and platform:
            # 1. Get the user's nickname
            nickname = await get_nickname(user_id, platform)
            if nickname:
                context_facts += f"This user's name is {nickname}. Address them by this name when appropriate.\n"

            # 2. Get the user's general memories
            memories = await get_user_memories(user_id, platform)
            if memories:
                formatted_memories = "\n- ".join(memories)
                context_facts += f"--- REMEMBER THE FOLLOWING FACTS ABOUT THIS USER ---\n- {formatted_memories}\n"

        full_prompt = f"{BOT_PERSONALITY_PROMPT}\n\n{context_facts}--- HUMAN QUESTION ---\n{user_question}"
        
        print("--- [AI] Generating response... ---")
        response = await model.generate_content_async(full_prompt)
        return response.text
    except Exception as e:
        print(f"An error occured with Gemini AI: {e}")
        return "Sorry, I'm having a-peel-ing technical difficulties right now!"
    
async def generate_themed_response(prompt: str) -> str:
    """A simple generator for creative, one-off text snippets"""
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        print(f"---[AI] Generating themed response... ---")
        response = await model.generate_content_async(prompt)
        return response.text.strip()
    except Exception as e:
        prit(f"An error occured with Gemini AI (Themed): {e}")
        return "Hrmm... I forgot what I was going to say."