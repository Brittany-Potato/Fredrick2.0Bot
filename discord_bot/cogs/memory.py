from discord.ext import commands
from services.memory_service import save_memory
# discord_bot/cogs/memory.py

# --- Make sure to import the new function at the top ---
from services.memory_service import save_memory, set_nickname

class MemoryCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="remember", help="Tells Fred to remember something about you.")
    async def remember(self, ctx, *, text_to_remember: str):
        # ... (this command stays the same)
        user_id = str(ctx.author.id)
        await save_memory(user_id, "discord", text_to_remember)
        await ctx.send("You got it, tater tot! I'll file that away in my spud-brain.")

    # --- ADD THIS NEW COMMAND ---
    @commands.command(name="setname", help="Sets your nickname for Fred to use.")
    async def set_user_nickname(self, ctx, *, nickname: str):
        """Sets a nickname for the user."""
        user_id = str(ctx.author.id)
        await set_nickname(user_id, "discord", nickname)
        await ctx.send(f"I'll call you **{nickname}** from now on, my fry-end!")

async def setup(bot):
    await bot.add_cog(MemoryCog(bot))