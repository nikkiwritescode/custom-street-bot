import discord
from discord import app_commands
from discord.ext import commands
from textwrap import dedent

from commands.help.content.rules import rules


class DisplayRules(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="rules", description="Show the Custom Street server rules"
    )
    async def show_rules(self, interaction: discord.Interaction):
        embed = discord.Embed(color=0x000000)
        for k, v in rules.items():
            embed.add_field(
                name=k,
                value=dedent(v).strip("\n"),
                inline=False,
            )
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(DisplayRules(bot))
