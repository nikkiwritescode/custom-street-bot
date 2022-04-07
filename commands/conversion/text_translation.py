from discord.ext import commands
from app import deepl_key
import deepl

translator = deepl.Translator(deepl_key)


class TextTranslation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['japanese', 'jp'])
    async def TranslateToJapanese(self, ctx, *, arg):
        result = translator.translate_text(
            arg,
            target_lang="JA"
        )
        await ctx.send(result.text)

    @commands.command(aliases=['english', 'en'])
    async def TranslateToEnglish(self, ctx, *, arg):
        result = translator.translate_text(
            arg,
            target_lang="EN-US"
        )
        await ctx.send(result.text)


def setup(bot):
    bot.add_cog(TextTranslation(bot))
