# Discord/bot.py

import discord 
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Discord bot {bot.user} has connected to Discord!")
    # Load cogs
    for filename in os.listdir('./discord_bot.cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f"discord_bot.cogs.{filename[:3]}")