# Discord/cogs/gemini_ai.py

from discord.ext import commands 
from services.gemini_service import generate_text

class GeminiAICog(commands.Cog):
    def __init__(self, bot):
        self.bot
        
    @commands.command(name="ask")
    async def ask_gemini(self, ctx, *, question:str):
        """Asks a question to Gemini"""
        async with ctx.typing():
            response = await generate_text(question)
            await ctx.send(response)
            
async def setup(bot):
    await bot.add_cog(GeminiAICog(bot))