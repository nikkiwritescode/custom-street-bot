import os
import discord
import shutil
from cs_board_tools.io import read_zip
from cs_board_tools.validation import validate_bundle
from discord import app_commands
from discord.ext import commands

from config.secrets import gdrive_api_key


def get_emoji(status):
    match (status):
        case "OK":
            emoji = ":green_circle:"
        case "WARNING":
            emoji = ":yellow_circle:"
        case "ERROR":
            emoji = ":red_circle:"
        case "SKIPPED":
            emoji = ":black_circle:"
    return emoji


def remove_temp_directory(path):
    shutil.rmtree(path)


class ValidateBundle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    name = "validate_board_bundle"

    description = "Validate that a board bundle is "
    "configured correctly, that values are consistent "
    "between the .frb and .yaml file, and that it doesn't "
    "contain any of the common problems that cause boards "
    "to fail."


    @app_commands.command(name=name, description=description)
    async def validate(
        self,
        interaction: discord.Interaction,
        attachment: discord.Attachment
    ):
        if not attachment:
            return

        errors_were_found_message = "{error_count} error(s) were found."
        warnings_were_found_message = "{warning_count} warning(s) were found."
        both_were_found_message = "{error_count} error(s) and {warning_count} warning(s) were found."

        # Currently, Discord does not allow
        # multiple attachments to functions
        # like this one, so we can safely
        # assume there will be only one.

        # Regardless, we'll be a good
        # citizen and do a quick check to
        # confirm it isn't a list, so the
        # code doesn't blow up if this aspect
        # changes.

        if isinstance(attachment, list):
            return

        base_path = "./upload/"

        file_path = base_path + attachment.filename

        we_created_dir = False
        if not os.path.exists(base_path):
            we_created_dir = True
            os.mkdir(base_path)
        await attachment.save(file_path)

        await interaction.response.defer()

        bundles = read_zip(file_path)
        # remove the file now that we've extracted and examined it
        if os.path.exists(file_path):
            os.remove(file_path)

        output = validate_bundle(bundles, gdrive_api_key=gdrive_api_key)

        embeds = []

        error_icon = "https://cdn0.iconfinder.com/data/icons/shift-interfaces/32/Error-512.png"
        success_icon = "https://static-00.iconduck.com/assets.00/success-icon-512x512-qdg1isa0.png"
        warning_icon = "https://www.iconsdb.com/icons/preview/orange/warning-xxl.png"

        icon = success_icon
        for r in output.boards:
            if r.issue_count == 0:
                description = "All tests passed!"
                icon = success_icon

            elif r.warning_count > 0 and r.error_count > 0:
                description = both_were_found_message.format(
                    error_count=r.error_count,
                    warning_count=r.warning_count
                )
                icon = error_icon

            elif r.warning_count > 0:
                description = warnings_were_found_message.format(warning_count=r.warning_count)
                icon = warning_icon

            elif r.error_count > 0:
                description = errors_were_found_message.format(error_count=r.error_count)
                icon = error_icon


            embed=discord.Embed(title=f"{r.board_name}", description="", color=0x62a0ea)

            if(r.error_count > 0):
                bulleted_errors=[]
                for e in r.error_messages:
                    bulleted_errors.append(f"* {e}")

                errors="\n".join(bulleted_errors)
                value = (errors[:1020] + '..') if len(errors) > 1020 else errors

                embed.add_field(name="Errors:", value=value, inline=False)

            if(r.warning_count > 0):
                bulleted_warnings=[]
                for w in r.warning_messages:
                    bulleted_warnings.append(f"* {w}")

                warnings="\n".join(bulleted_warnings)
                value = (warnings[:1020] + '..') if len(warnings) > 1020 else warnings

                embed.add_field(name="Warnings:", value=value, inline=False)

            if(r.informational_messages):
                bulleted_messages=[]
                for i in r.informational_messages:
                    bulleted_messages.append(f"* {i}")

                messages="\n".join(bulleted_messages)
                value = (messages[:1020] + '..') if len(messages) > 1020 else messages

                embed.add_field(name="Other Notes:", value=value, inline=False)

            embed.set_author(name="Board Validation Results", icon_url=icon)
            embed.add_field(name=f"{get_emoji(r.board_configuration.status)} Board Configuration", value="", inline=True)
            embed.add_field(name=f"{get_emoji(r.consistency.status)} Board Consistency", value="", inline=True)
            embed.add_field(name=f"{get_emoji(r.icon.status)} Icon", value="", inline=True)
            embed.add_field(name=f"{get_emoji(r.max_paths.status)} Max Paths", value="", inline=True)
            embed.add_field(name=f"{get_emoji(r.music_download.status)} Music Download", value="", inline=True)
            embed.add_field(name=f"{get_emoji(r.naming.status)} Naming Convention", value="", inline=True)
            embed.add_field(name=f"{get_emoji(r.screenshots.status)} Screenshots", value="", inline=True)
            embed.add_field(name=f"{get_emoji(r.venture.status)} Venture Cards", value="", inline=True)
            embed.add_field(name=f"{get_emoji(r.yaml.status)} YAML Validation", value="", inline=True)
            embed.add_field(name=f"", value="", inline=True)

            embed.set_footer(text=description)

            embeds.append(embed)

        if we_created_dir:
            remove_temp_directory(base_path)

        await interaction.followup.send(embeds=embeds)


async def setup(bot):
    await bot.add_cog(ValidateBundle(bot))
