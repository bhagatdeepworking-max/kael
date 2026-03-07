import discord
from discord.ext import commands
import os

class KaelBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True 
        
        super().__init__(
            command_prefix='!', # Still needed for internal logic
            intents=intents,
            status=discord.Status.dnd,
            activity=discord.CustomActivity(name="@ kael for help")
        )

    async def setup_hook(self):
        # Load the General Cog
        await self.load_extension('cogs.general')
        print("Tactical Module: General [LOADED]")
        
        await self.tree.sync()
        print("Slash Commands: [SYNCED]")

bot = KaelBot()

token = os.getenv('TOKEN')
bot.run(token)
