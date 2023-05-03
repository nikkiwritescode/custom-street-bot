import deepl
import discord
from discord import app_commands
from discord.ext import commands

from config.secrets import deepl_key

translator = deepl.Translator(deepl_key)


class TextTranslation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="translate", description="Translate text between languages"
    )
    @app_commands.describe(
        text="Text to translate", language="Language to translate to"
    )
    @app_commands.choices(
        language=[
            app_commands.Choice(name="English (American)", value="EN-GB"),
            app_commands.Choice(name="English (British)", value="EN-US"),
            app_commands.Choice(name="French", value="FR"),
            app_commands.Choice(name="German", value="DE"),
            app_commands.Choice(name="Italian", value="IT"),
            app_commands.Choice(name="Japanese", value="JA"),
            app_commands.Choice(name="Spanish", value="ES"),
        ]
    )
    async def translate(
        self, interaction: discord.Interaction, text: str, language: str
    ):
        response = f"Input text: {text}\nTranslated: "
        result = translator.translate_text(text, target_lang=language)
        await interaction.response.send_message(response + result.text)


async def setup(bot):
    await bot.add_cog(TextTranslation(bot))
