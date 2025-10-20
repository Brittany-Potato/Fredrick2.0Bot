# discord_bot/bot.py 

import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Discord bot {bot.user} has connected to Discord!")
    print("--- Loading Discord Cogs ---")

    # The corrected path with a slash '/'
    cogs_directory = './discord_bot/cogs'

    for filename in os.listdir(cogs_directory):
        # We only want to load files that end in .py
        if filename.endswith('.py') and not filename.startswith('__'):
            try:
                # The corrected slicing '[:-3]' to remove '.py'
                await bot.load_extension(f"discord_bot.cogs.{filename[:-3]}")
                print(f"[SUCCESS] Loaded cog: {filename}")
            except Exception as e:
                print(f"[FAILURE] Failed to load cog {filename}: {e}")
    print("--- Finished Loading Cogs ---")