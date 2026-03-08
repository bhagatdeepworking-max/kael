import discord
from discord.ext import commands
import time

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        # Calculate message latency
        start_time = time.monotonic()
        message = await ctx.send("🏓 Pinging...")
        end_time = time.monotonic()
        
        api_latency = round(self.bot.latency * 1000)
        heartbeat = round((end_time - start_time) * 1000)

        embed = discord.Embed(
            title="Pong!",
            color=0x2b2d31 # A sleek, dark "Discord-colored" grey
        )
        embed.add_field(name="📡 API Latency", value=f"`{api_latency}ms`", inline=True)
        embed.add_field(name="⚡ Heartbeat", value=f"`{heartbeat}ms`", inline=True)
        embed.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        
        await message.edit(content=None, embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))
