# main.py

import asyncio
from discord_bot.bot import bot as discord_bot
from twitch_bot.bot import bot as twitch_bot
from config import DISCORD_TOKEN

async def main():
    await asyncio.gather(
        discord_bot.start(DISCORD_TOKEN),
        twitch_bot.start()
    )
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bots are shutting down.")