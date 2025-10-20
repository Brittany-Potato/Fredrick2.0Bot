# Twitch/commands/gemini_ai.py

from twitchio.ext import commands
from services.gemini_service import generate_text

@commands.command(name="ask")
async def ask(ctx: commands.Context, *, question: str):
    """Asks Gemini a question"""
    response = await generate_text(question)
    await ctx.send(response)