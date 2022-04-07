from discord.ext import commands
import discord

from app import bot
from commands.help.content.aliases import (
    address_converter_aliases,
    card_aliases,
    help_aliases,
    text_translation_aliases,
    value_converter_aliases,
    url_aliases
)
from commands.help.content.descriptions import (
    address_converters_help,
    help_help,
    text_translation_help,
    urls_help,
    value_converters_help,
    venture_cards_help
)

prefix = bot.command_prefix


class DisplayHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rules")
    async def rules(self, ctx):
        embed = discord.Embed(color=0x000000)
        embed.add_field(
            name="Don't be a jerk",
            value="This means no bullying. Call people what they want " +
                  "to be called. Offer constructive criticism instead of " +
                  "simply telling someone their work sucks. Stuff like " +
                  "that. I don't think everything under this category " +
                  "needs to be explicitly stated, so use your common sense." +
                  "It's not hard to be nice to people.",
            inline=False,
        )
        embed.add_field(
            name="Don't spam",
            value="Talking a lot and being active here is okay and " +
                  "highly encouraged! This rule is for spamming " +
                  "nonsense links and the like. If it makes the staff " +
                  "have to put on the Discord Mod hat it's probably " +
                  "over the line, we don't like doing that.",
            inline=False,
        )
        embed.add_field(
            name="Try to keep channels on-topic",
            value="...as much as possible anyway. This rule will " +
                  "be bent a lot by conversations being active and " +
                  "vibrant and that's totally fine! Just try to at " +
                  "least be mindful of it and move to the correct " +
                  "channel when you notice.",
            inline=False,
        )
        embed.add_field(
            name="No piracy / illegal content",
            value="If you link directly to an ISO or something " +
                  "like that we would be at a very low, but still " +
                  "nonzero, risk of Nintendo trying to nuke our " +
                  "server and that would be an extremely sad day " +
                  "for all of us.",
            inline=False,
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['commands'])
    async def help(self, ctx):
        embed = discord.Embed(
            title="Overview of Available Commands",
            color=0x000000
        )
        embed.add_field(
            name="Address Converters",
            value="".join(address_converters_help),
            inline=False,
        )
        embed.add_field(
            name="Value Converters",
            value="".join(value_converters_help),
            inline=False,
        )
        embed.add_field(
            name="Text Translation (powered by DeepL)",
            value="".join(text_translation_help),
            inline=False,
        )
        embed.add_field(
            name="Venture Cards",
            value="".join(venture_cards_help),
            inline=False
        )
        embed.add_field(
            name="URLs",
            value="".join(urls_help),
            inline=False
        )
        embed.add_field(
            name="Help",
            value="".join(help_help),
            inline=False
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['alias', 'alt'])
    async def aliases(self, ctx):
        embed = discord.Embed(
            title="Aliases for Available Commands",
            color=0x000000
        )
        embed.add_field(
            name="Address Converters",
            value="".join(address_converter_aliases),
            inline=False,
        )
        embed.add_field(
            name="Value Converters",
            value="".join(value_converter_aliases),
            inline=False,
        )
        embed.add_field(
            name="Text Translation (powered by DeepL)",
            value="".join(text_translation_aliases),
            inline=False,
        )
        embed.add_field(
            name="Venture Cards",
            value="".join(card_aliases),
            inline=False
        )
        embed.add_field(
            name="URLs",
            value="".join(url_aliases),
            inline=False
        )
        embed.add_field(
            name="Help Commands",
            value="".join(help_aliases),
            inline=False
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(DisplayHelp(bot))
