import discord
from discord.ext import commands

from config.secrets import discord_token


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
    await bot.load_extension("commands.validation.map_bundle")


if __name__ == "__main__":
    bot.run(discord_token)
