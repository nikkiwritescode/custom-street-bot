import discord
from discord import app_commands
from discord.ext import commands
from textwrap import dedent

from commands.help.content.commands import help_choices


class LegacyDisplayHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    choices = []
    for k, v in help_choices.items():
        choices.append(app_commands.Choice(name=v[0], value=k))
    choices.append(app_commands.Choice(name="All commands", value="all"))

    @app_commands.command(name="help", description="Describe slash commands")
    @app_commands.describe(command="Which group of commands to get help for")
    @app_commands.choices(command=choices)
    async def help(
        self,
        interaction: discord.Interaction,
        command: app_commands.Choice[str]
    ):
        embed = discord.Embed(color=0x000000)
        for k, v in help_choices.items():
            if command.value == k or command.value == "all":
                embed.add_field(
                    name=v[0],
                    value=dedent("".join(v[1:]).strip("\n")),
                    inline=False,
                )
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(LegacyDisplayHelp(bot))
