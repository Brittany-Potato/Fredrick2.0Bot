from twitchio.ext import commands
from services.memory_service import save_memory
from services.memory_service import save_memory, set_nickname

@commands.command(name="remember")
async def remember(ctx: commands.Context, *, text_to_remember: str):
    """Tells Fred to remember something about the user."""
    user_id = str(ctx.author.id)
    await save_memory(user_id, "twitch", text_to_remember)
    await ctx.send("You got it, tater tot! I'll file that away in my spud-brain.")
    
@commands.command(name="setname")
async def set_user_nickname(ctx: commands.Context, *, nickname: str):
    """Sets a nickname for the user."""
    user_id = str(ctx.author.id)
    await set_nickname(user_id, "twitch", nickname)
    await ctx.send(f"I'll call you {nickname} from now on, my fry-end!")