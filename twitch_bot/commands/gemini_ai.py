# Twitch/commands/gemini_ai.py

from twitchio.ext import commands
from services.gemini_service import generate_text

@commands.command(name="ask")
async def ask(ctx: commands.Context, *, question: str):
    """Asks Gemini a question"""
    # --- MODIFIED: Pass the author's ID and platform ---
    response = await generate_text(question, str(ctx.author.id), "twitch")
    await ctx.send(response)