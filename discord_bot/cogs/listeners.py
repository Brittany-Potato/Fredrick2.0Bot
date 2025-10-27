# discord_bot/cogs/listeners.py (CORRECTED VERSION)

import discord
from discord.ext import commands
from config import WELCOME_CHANNEL_ID
from prompts import WELCOME_PROMPT

# --- NEW: Import the tool that lets the bot think! ---
from services.gemini_service import generate_text

class ListenersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        # Good practice to add a breadcrumb to see the event fire
        print(f"--- [EVENT TRIGGERED] Member Join: {member.name} ---")

        # 1. Get the channel and store it in a variable
        channel = self.bot.get_channel(int(WELCOME_CHANNEL_ID))

        # 2. Make sure the channel was found
        if channel is not None:
            
            # --- THIS IS THE MAGIC ---
            # 3. Instead of sending the prompt, send it to the AI for a response.
            print("--- [AI] Generating a creative welcome message... ---")
            ai_welcome_message = await generate_text(WELCOME_PROMPT)

            # 4. Send the AI's creative response, along with the member mention!
            await channel.send(f"{member.mention} {ai_welcome_message}")

        else:
            print(f"--- [FAILURE] Could not find channel with ID {WELCOME_CHANNEL_ID} ---")


async def setup(bot):
    await bot.add_cog(ListenersCog(bot))