import discord
from discord.ext import commands
import os

class KaelBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True 
        
        super().__init__(
            command_prefix='!', 
            intents=intents,
            status=discord.Status.dnd,
            activity=discord.CustomActivity(name="@ kael for help")
        )

    async def on_ready(self):
        print("--- SYSTEM ONLINE ---")
        print(f"Operative: {self.user.name}")
        print(f"ID: {self.user.id}")
        print(f"Latency: {round(self.latency * 1000)}ms")
        print("---------------------")

    async def setup_hook(self):
        # This is where we will eventually load 'Cogs' (modules)
        print("Initializing tactical modules...")

bot = KaelBot()

@bot.command()
async def ping(ctx):
    await ctx.send(f"**PONG.** System latency is {round(bot.latency * 1000)}ms.")

token = os.getenv('TOKEN')
if token:
    bot.run(token)
else:
    print("ERROR: No 'TOKEN' found in environment variables.")
