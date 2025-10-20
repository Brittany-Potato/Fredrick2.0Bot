# Discord/cogs/general.py

from discord.ext import commands
from prompts import TATO_INFO

class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="tato", help="Learn about my awesome creator!")
    async def tato_command(self, ctx):
        """Sends a pre-written message with info about the creator."""
        await ctx.send(TATO_INFO)
        
async def setup(bot):
    await bot.add_cog(GeneralCog(bot))