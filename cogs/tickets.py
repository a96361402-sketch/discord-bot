import discord
from discord.ext import commands

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ticket(self, ctx):
        guild = ctx.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }

        channel = await guild.create_text_channel(
            f"ticket-{ctx.author.name}",
            overwrites=overwrites
        )

        embed = discord.Embed(
            title="🎫 Ticket creato",
            description=f"{ctx.author.mention} il tuo ticket è stato aperto!",
            color=0x00aaff
        )

        await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Tickets(bot))