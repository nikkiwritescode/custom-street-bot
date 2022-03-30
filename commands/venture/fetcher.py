from discord.ext import commands
import random

from utils.card_embed import CardEmbed


class VentureCards(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="card")
    async def pull_card(self, ctx, arg=None):
        if not arg:
            arg = random.randint(1, 128)
        try:
            num = int(arg)
            assert (
                type(num) == int and num >= 1 and num <= 128
            ), await ctx.send(
                "Please enter a valid integer value between 1 and 128."
            )
        except ValueError:
            await ctx.send(
                "Please enter a valid integer value between 1 and 128."
            )

        card = CardEmbed.create_card_embed(arg, ctx.author.mention)
        await ctx.send(file=card.file, embed=card.embed)


def setup(bot):
    bot.add_cog(VentureCards(bot))
