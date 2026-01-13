import discord
import json
from discord.ext import commands

CONFIG_FILE = "config.json"

class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setup(self, ctx):
        embed = discord.Embed(
            title="⚙️ Configurazione Bot",
            description="Rispondi ai messaggi per configurare il bot.",
            color=0x00aaff
        )

        embed.add_field(name="1️⃣ ID canale annunci", value="Scrivilo quando richiesto", inline=False)
        embed.add_field(name="2️⃣ ID ruolo da pingare", value="Scrivilo quando richiesto", inline=False)
        embed.add_field(name="3️⃣ Link TikTok", value="Scrivilo quando richiesto", inline=False)
        embed.add_field(name="4️⃣ Link Discord", value="Scrivilo quando richiesto", inline=False)

        await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send("🔹 **Inserisci l'ID del canale annunci:**")
        announce = await self.bot.wait_for("message", check=check)

        await ctx.send("🔹 **Inserisci l'ID del ruolo da pingare:**")
        role = await self.bot.wait_for("message", check=check)

        await ctx.send("🔹 **Inserisci il link TikTok:**")
        tiktok = await self.bot.wait_for("message", check=check)

        await ctx.send("🔹 **Inserisci il link Discord:**")
        discord_link = await self.bot.wait_for("message", check=check)

        data = {
            "announce_channel": int(announce.content),
            "role_to_ping": int(role.content),
            "tiktok_url": tiktok.content,
            "discord_url": discord_link.content
        }

        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=4)

        await ctx.send("✅ **Configurazione salvata con successo!**")

async def setup(bot):
    await bot.add_cog(Setup(bot))