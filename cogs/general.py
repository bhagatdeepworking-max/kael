import discord
from discord.ext import commands
from discord import app_commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check Kael's tactical response time.")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"**PONG.** Response time: `{latency}ms`")

    @app_commands.command(name="info", description="View Kael's system specifications.")
    async def info(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Kael // System Overview",
            description="Elite Integrated Server Management Operative.",
            color=0x00fbff
        )
        embed.add_field(name="Status", value="🟢 Operational", inline=True)
        embed.add_field(name="Latency", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.set_footer(text="Precision in every packet.")
        
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))
