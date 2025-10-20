# Twitch/bot.py
from twitchio.ext import commands
# Correct the import path to be absolute from the project root
from twitch_bot.commands import gemini_ai as gemini_commands 
from config import TWITCH_TOKEN, TWITCH_CHANNEL, TWITCH_CLIENT_ID, TWITCH_NICK

class TwitchBot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=TWITCH_TOKEN,
            client_id=TWITCH_CLIENT_ID,
            nick=TWITCH_NICK,
            prefix="!",
            initial_channels=[TWITCH_CHANNEL]
        )
        
    async def event_ready(self):
        print(f"Twitch bot {self.nick} is online!")
        print(f"User id is: {self.user_id}")
        
    async def event_message(self, message):
        if message.echo:
            return 
        
        await self.handle_commands(message)
        
    @commands.command(name="Hello")
    async def hello_command(self, ctx):
        await ctx.send(f"Hello {ctx.author.name}!")
        
        
bot = TwitchBot()

# Adding commands from other files
bot.add_command(gemini_commands.ask)
bot.add_command(bot.hello_command)