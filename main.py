import os, re, discord
from discord.ext import commands

DISCORD_TOKEN = os.getenv("(redacted for HiddenDevs APP)")

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(f"{bot.user} has spawnd (you did a thing)")

bot.run(DISCORD_TOKEN)
