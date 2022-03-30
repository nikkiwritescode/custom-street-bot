from discord.ext import commands
import discord
import os

# Environment Variables
deepl_key = os.environ.get("DEEPL_AUTH_KEY")
discord_token = os.environ.get("DISCORD_TOKEN")

# Bot Setup
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot.remove_command("help")
bot.load_extension("commands.conversion.address_conversion")
bot.load_extension("commands.conversion.value_conversion")
bot.load_extension("commands.conversion.text_translation")
bot.load_extension("commands.help.embeds")
bot.load_extension("commands.help.links")
bot.load_extension("commands.venture.fetcher")

bot.run(discord_token)
