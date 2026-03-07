import discord
from discord.ext import commands
from discord import app_commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_base_embed(self, header, content):
        """Custom Kael layout with separator and specific footer"""
        # Using \n to create the line break and the dashed separator
        description = f"----------------------------------------------\n{content}"
        
        embed = discord.Embed(
            title=header,
            description=description,
            color=0xFFFFFF  # Pure White
        )
        embed.set_footer(text="Made by AI Development!")
        return embed

    @app_commands.command(name="ping", description="Check Kael's tactical response time.")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        # Matches your requested format
        embed = self.get_base_embed("Pong!", f"Latency: {latency}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="info", description="View Kael's system specifications.")
    async def info(self, interaction: discord.Interaction):
        content = (
            f"Status: Operational\n"
            f"Latency: {round(self.bot.latency * 1000)}ms\n"
            f"Version: 1.0.0"
        )
        embed = self.get_base_embed("System Overview", content)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))
