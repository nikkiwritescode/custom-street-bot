import discord
from discord.ext import commands
import os

# Environment Variables
deepl_key = os.environ.get("DEEPL_AUTH_KEY")
discord_token = os.environ.get("DISCORD_TOKEN")

# Bot Setup
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    bot.remove_command("help")
    await bot.load_extension("commands.conversion.address_conversion")
    await bot.load_extension("commands.conversion.value_conversion")
    await bot.load_extension("commands.conversion.text_translation")
    await bot.load_extension("commands.help.commands")
    await bot.load_extension("commands.help.links")
    await bot.load_extension("commands.help.rules")
    await bot.load_extension("commands.management.sync")
    await bot.load_extension("commands.venture.fetcher")

bot.run(discord_token)
