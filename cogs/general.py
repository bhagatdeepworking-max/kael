import discord
from discord.ext import commands
from discord import app_commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_base_embed(self, title, description):
        """Helper to keep all Kael embeds consistent (White Color)"""
        embed = discord.Embed(
            title=f"KAEL // {title}",
            description=description,
            color=0xFFFFFF  # Pure White
        )
        embed.set_footer(text="Precision Operative • @ kael for help")
        return embed

    @app_commands.command(name="ping", description="Check Kael's tactical response time.")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        embed = self.get_base_embed("LATENCY", f"System response time: `{latency}ms`")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="info", description="View Kael's system specifications.")
    async def info(self, interaction: discord.Interaction):
        embed = self.get_base_embed("SYSTEM OVERVIEW", "Elite Integrated Server Management Operative.")
        
        embed.add_field(name="Status", value="🟢 Operational", inline=True)
        embed.add_field(name="Latency", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.add_field(name="Version", value="v1.0.0", inline=True)
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="userinfo", description="Scan a user's profile data.")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user
        
        embed = self.get_base_embed("USER DATA", f"Displaying profile for {member.mention}")
        embed.set_thumbnail(url=member.display_avatar.url)
        
        embed.add_field(name="Joined Discord", value=member.created_at.strftime("%b %d, %Y"), inline=True)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%b %d, %Y"), inline=True)
        embed.add_field(name="Top Role", value=member.top_role.mention, inline=True)
        
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))
