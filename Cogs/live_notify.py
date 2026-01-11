import discord
import json
from discord.ext import commands

CONFIG_FILE = "config.json"

class LiveNotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def load_config(self):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)

    @commands.command()
    async def live(self, ctx):
        cfg = self.load_config()

        channel = self.bot.get_channel(cfg["announce_channel"])
        role = cfg["role_to_ping"]
        tiktok = cfg["tiktok_url"]
        discord_url = cfg["discord_url"]

        if channel:
            embed = discord.Embed(
                title="🔴 LIVE ORA!",
                description="Sto trasmettendo in diretta!",
                color=0xff0000
            )

            embed.add_field(name="📱 TikTok", value=tiktok, inline=False)
            embed.add_field(name="🌐 Discord", value=discord_url, inline=False)

            ping = f"<@&{role}>"

            await channel.send(ping, embed=embed)

async def setup(bot):
    await bot.add_cog(LiveNotify(bot))