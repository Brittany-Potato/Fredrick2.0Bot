from twitchio.ext import commands
import random

# --- Import the AI service and new prompt ---
from services.gemini_service import generate_themed_response
from prompts import VILLAGER_PROMPT

# --- Import our hardcoded image list ---
from command_assets import VILLAGER_IMAGES

@commands.command(name="vill")
async def villager_command(ctx: commands.Context):
    """Sends an AI-generated villager phrase and a link to an image."""
    try:
        # --- DYNAMIC TEXT ---
        ai_phrase = await generate_themed_response(VILLAGER_PROMPT)
        
        # --- HARDCODED IMAGE ---
        random_image_url = random.choice(VILLAGER_IMAGES)
        
        # Send them as separate messages
        await ctx.send(ai_phrase)
        await ctx.send(random_image_url)

    except Exception as e:
        print(f"--- [FAILURE] The Twitch !vill command failed: {e} ---")
        await ctx.send("Hrmph. Something went wrong with my brain.")