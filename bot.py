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