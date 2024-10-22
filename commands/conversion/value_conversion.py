import discord
from discord import app_commands
from discord.ext import commands
import struct


def check_if_string_is_hex(value: str):
    try:
        int(value, 16)
        return True
    except ValueError:
        return False


class ValueConversion(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="convert_value_to_hex",
        description="Convert a value to Hexadecimal",
    )
    async def convert_value_to_hex(
        self,
        interaction: discord.Interaction,
        value: str
    ):
        send = interaction.response.send_message
        response = f"You entered: {value}\nValue converted to hex: "

        if "." in value:  # if float
            error_msg = response + "ERROR converting float to hex"
            num = float(value)
            assert type(num) is float, await send(error_msg)
            try:
                await send(hex(struct.unpack("<I", struct.pack("<f", num))[0]))
            except ValueError:
                await send(response + error_msg)
        else:  # if int
            error_msg = response + "ERROR converting int to hex"
            num = int(value)
            assert type(num) is int, await send(error_msg)
            try:
                await send(hex(num))
            except ValueError:
                await send(error_msg)

    @app_commands.command(
        name="convert_value_to_int",
        description="Convert a value to integer",
    )
    async def convert_value_to_int(
        self,
        interaction: discord.Interaction,
        value: str,
    ):
        send = interaction.response.send_message
        response = f"You entered: {value}\nValue converted to int: "

        if check_if_string_is_hex(value):  # if hex
            error_msg = response + "ERROR converting hex to int"
            if value[:2] == "0x":
                value = value[2:]
            try:
                await send(int(value, base=16))
            except ValueError:
                await send(error_msg)
        else:  # if float
            error_msg = response + "ERROR converting float to int"
            num = float(value)
            assert type(num) is float, await send(error_msg)
            try:
                await send(round(num))
            except ValueError:
                await send(error_msg)

    @app_commands.command(
        name="convert_value_to_float",
        description="Convert a value to float",
    )
    async def convert_value_to_float(
        self, interaction: discord.Interaction, value: str
    ):
        send = interaction.response.send_message
        response = f"You entered: {value}\nValue converted to float: "

        try:  # if int
            num = int(value)
            await send(float(num))
        except ValueError:  # if hex
            if check_if_string_is_hex(value):
                error_msg = response + "ERROR converting hex to float"
                if value[:2] == "0x":
                    value = value[2:]
                try:
                    await send(struct.unpack("!f", bytes.fromhex(value))[0])
                except ValueError:
                    await send(error_msg)
            else:
                await send(response + "ERROR. Unknown input type.")


async def setup(bot):
    await bot.add_cog(ValueConversion(bot))
