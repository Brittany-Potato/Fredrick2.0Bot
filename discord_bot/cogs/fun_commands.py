import discord
from discord.ext import commands
import random

# --- Import the AI service and new prompt ---
from services.gemini_service import generate_themed_response
from prompts import VILLAGER_PROMPT

# --- Import our hardcoded image list ---
from command_assets import VILLAGER_IMAGES

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="vill", help="Summons a villager with a profound, AI-generated statement.")
    async def villager_command(self, ctx):
        """Sends a random villager image and an AI-generated phrase."""
        # Let users know the bot is thinking
        async with ctx.typing():
            try:
                # --- DYNAMIC TEXT ---
                # Call the AI to generate a fresh quote using our specific prompt
                ai_phrase = await generate_themed_response(VILLAGER_PROMPT)
                
                # --- HARDCODED IMAGE ---
                random_image_url = random.choice(VILLAGER_IMAGES)
                
                # Create the embed with the AI's response
                embed = discord.Embed(
                    description=f"**\"{ai_phrase}\"**",
                    color=discord.Color.green()
                )
                embed.set_image(url=random_image_url)
                
                await ctx.send(embed=embed)
                
            except Exception as e:
                print(f"--- [FAILURE] The !vill command failed: {e} ---")
                await ctx.send("Hrmph. I seem to have misplaced my emeralds... and my thoughts.")

async def setup(bot):
    await bot.add_cog(FunCog(bot))