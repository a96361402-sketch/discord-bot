import discord
from discord.ext import commands

WELCOME_CHANNEL = 1455609585955111075

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(WELCOME_CHANNEL)
        if channel:
            embed = discord.Embed(
                title="👋 Benvenuto!",
                description=f"{member.mention} è entrato nel server!",
                color=0x00ff99
            )
            await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Welcome(bot))