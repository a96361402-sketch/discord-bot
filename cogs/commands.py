import discord
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def regole(self, ctx):
        embed = discord.Embed(
            title="📜 Regole del server",
            description="1. Rispetta tutti\n2. Niente spam\n3. Segui le linee guida\n4. Divertiti!",
            color=0x3498db
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(
            title="ℹ️ Info del server",
            description="Questo è il bot ufficiale del server!",
            color=0x7289da
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Commands(bot))