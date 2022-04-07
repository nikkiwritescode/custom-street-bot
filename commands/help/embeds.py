from discord.ext import commands
import discord

from app import bot

prefix = bot.command_prefix

commands_address_converters_help = [
    f"`{prefix}bsv2fsv` Boom Street Virtual Address to FS.\n",
    f"`{prefix}fsv2bsv` Fortune Street Virtual Address to BS.\n",
    f"`{prefix}bsv2bsf` BS Virtual Address to File Offset.\n",
    f"`{prefix}fsv2fsf` FS Virtual Address to File Offset.\n",
]
commands_text_translation_help = [
    f"`{prefix}en` Convert text to English.\n",
    f"`{prefix}jp` Convert text to Japanese.\n",
]
commands_urls_help = [
    f"`{prefix}calc` Display the Address Calculator URL.\n",
    f"`{prefix}contribute` Display a link to this bot's GitHub repo.\n",
    f"`{prefix}github` Display the Github URL.\n",
    f"`{prefix}invite` Display the server invite link.\n",
    f"`{prefix}twitch` Display the Twitch channel URL.\n",
    f"`{prefix}wiki` Display the Wiki URL.\n",
    f"`{prefix}youtube` Display the YouTube channel URL.",
]
commands_value_converters_help = [
    f"`{prefix}hex2int` Convert Hex to Decimal.\n",
    f"`{prefix}hex2float` Convert Hex to Float.\n",
    f"`{prefix}int2hex` Convert Decimal to Hex.\n",
    f"`{prefix}float2hex` Convert Float to Hex.",
]
commands_venture_cards_help = [
    f"`{prefix}card` Pull a random Venture Card.\n",
    f"`{prefix}card <number>` Pull a specific Venture Card.\n",
]


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
            value="".join(commands_address_converters_help),
            inline=False,
        )
        embed.add_field(
            name="Value Converters",
            value="".join(commands_value_converters_help),
            inline=False,
        )
        embed.add_field(
            name="Text Translation (powered by DeepL)",
            value="".join(commands_text_translation_help),
            inline=False,
        )
        embed.add_field(
            name="Venture Cards",
            value="".join(commands_venture_cards_help),
            inline=False
        )
        embed.add_field(
            name="URLs",
            value="".join(commands_urls_help),
            inline=False
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(DisplayHelp(bot))
