import discord
import os
from discord.ext import commands

# Kael's Core Setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Kael is online. Latency: {round(bot.latency * 1000)}ms')
  
token = os.getenv('TOKEN')
bot.run(token)
