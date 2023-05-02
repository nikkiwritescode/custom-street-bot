import discord
from discord import app_commands
from discord.ext import commands
import json

from data.paths import rules_help_path

with open(rules_help_path, "r") as read_file_en:
    rules = json.load(read_file_en)


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
                value=v[0],
                inline=False,
            )
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(DisplayRules(bot))
