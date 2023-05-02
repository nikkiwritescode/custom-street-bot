import discord
from discord import app_commands
from discord.ext import commands
import json

from data.paths import links_help_path

with open(links_help_path, "r") as read_file_en:
    link_choices = json.load(read_file_en)


class DisplayLinks(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    url_choices = []
    for k, v in link_choices.items():
        url_choices.append(app_commands.Choice(name=v[0], value=k))

    @app_commands.command(
        name="links", description="Show various Custom Street-related URLs"
    )
    @app_commands.describe(url_to_show="Which URL to show")
    @app_commands.choices(url_to_show=url_choices)
    async def show_link(
        self,
        interaction: discord.Interaction,
        url_to_show: app_commands.Choice[str]
    ):
        send = interaction.response.send_message
        for k, v in link_choices.items():
            if url_to_show.value == k:
                await send(v[1])


async def setup(bot):
    await bot.add_cog(DisplayLinks(bot))
