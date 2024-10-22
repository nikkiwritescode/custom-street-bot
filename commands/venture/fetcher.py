import discord
from discord import app_commands
from discord.ext import commands
import random

from utils.card_embed import CardEmbed


class VentureCards(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="pull_random_card", description="Pull a random venture card"
    )
    async def pull_random_card(self, interaction: discord.Interaction):
        send = interaction.response.send_message
        num = random.randint(1, 128)
        card = CardEmbed.create_card_embed(num, interaction.user.mention)
        await send(file=card.file, embed=card.embed)

    @app_commands.command(name="pull_card", description="Pull a venture card")
    @app_commands.describe(number="Card number to pull")
    async def pull_card(self, interaction: discord.Interaction, number: str):
        send = interaction.response.send_message
        try:
            num = int(number)
            assert type(num) is int and num >= 1 and num <= 128, await send(
                "Please enter a valid integer value between 1 and 128."
            )
        except ValueError:
            await send("Please enter a valid integer value between 1 and 128.")

        card = CardEmbed.create_card_embed(number, interaction.user.mention)
        await send(file=card.file, embed=card.embed)


async def setup(bot):
    await bot.add_cog(VentureCards(bot))
