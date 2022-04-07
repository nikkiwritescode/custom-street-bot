from discord.ext import commands


class DisplayLinks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['calculator'])
    async def calc(self, ctx):
        await ctx.send(
            "Fortune Street Address Calculator => "
            "https://fortunestreetmodding.github.io/calculator"
        )

    @commands.command()
    async def contribute(self, ctx):
        await ctx.send(
            "This bot is open source! If you'd like to contribute, "
            "you can find the source code, here => "
            "https://github.com/nikkiwritescode/custom-street-bot"
        )

    @commands.command(aliases=['git', 'repo'])
    async def github(self, ctx):
        await ctx.send(
            "Fortune Street Modding on Github => "
            "https://github.com/FortuneStreetModding/"
        )

    @commands.command(aliases=['discord', 'invite', 'serverlink'])
    async def invitation(self, ctx):
        await ctx.send(
            "Custom Street on Discord => "
            "https://discord.gg/DE9Hn7T"
        )

    @commands.command(aliases=['ttv'])
    async def twitch(self, ctx):
        await ctx.send(
            "Custom Street on Twitch => "
            "https://www.twitch.tv/customstreet"
        )

    @commands.command()
    async def wiki(self, ctx):
        await ctx.send(
            "Fortune Street Modding Wiki => "
            "https://github.com/FortuneStreetModding/fortune-avenue-qt/wiki"
        )

    @commands.command(aliases=['channel', 'tube', 'yt'])
    async def youtube(self, ctx):
        await ctx.send(
            "Custom Street on YouTube => "
            "https://www.youtube.com/channel/UCYe4nHqb0HcWZ0pnoDP0Ijw"
        )


def setup(bot):
    bot.add_cog(DisplayLinks(bot))
