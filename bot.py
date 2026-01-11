import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online come {bot.user}")
    await bot.load_extension("cogs.setup")
    await bot.load_extension("cogs.welcome")
    await bot.load_extension("cogs.live_notify")
    await bot.load_extension("cogs.commands")
    await bot.load_extension("cogs.tickets")

bot.run(os.getenv("TOKEN"))
{
    "announce_channel": 0,
    "role_to_ping": 0,
    "tiktok_url": "",
    "discord_url": ""
}
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
        from discord.ext import commands

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

async def setup(bot):
    await bot.add_cog(Tickets(bot))
    discord.py