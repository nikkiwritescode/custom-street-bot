import discord
from discord import app_commands
from discord.ext import commands
import json

from data.paths import file_offsets_path
from utils.address_section_mapper import AddressSectionMapper


# Address Conversion lists

BSVirtToISVirt = BSVirtToFSVirt = BSVirtToBSFile = []
FSVirtToBSVirt = FSVirtToISVirt = FSVirtToFSFile = []
ISVirtToBSVirt = ISVirtToFSVirt = ISVirtToISFile = []

# Game Names

# This seems silly, but we use these strings
# _all over the place_. We're able to save quite
# a few lines by defining them here.

bs = "Boom Street"
fs = "Fortune Street"
isw = "Itadaki Street Wii"

# Initialization

# This function contains the code to initialize
# a single list. If we're performing this lookup
# in reverse (looking for FS-to-BS data in a
# BS-to_FS dataset, for example), we'll subtract
# the delta from the beginning and ending values.


def init_list(offset_dict: dict, dict_name: str, reverse: bool):
    list = []
    for row in offset_dict[dict_name]:
        if reverse:
            delta = int(row[2], base=16)
            begin = int(row[0], base=16) - delta
            end = int(row[1], base=16) - delta
        else:
            delta = int(row[2], base=16)
            begin = int(row[0], base=16)
            end = int(row[1], base=16)
        list.append(AddressSectionMapper(begin, end, delta))
    return list


# This function is for calling the above one
# to initialize all our lists.


def initialize_lists():
    global BSVirtToISVirt, BSVirtToFSVirt, BSVirtToBSFile
    global FSVirtToBSVirt, FSVirtToFSFile
    global ISVirtToBSVirt, ISVirtToISFile

    with open(file_offsets_path, "r") as read_offset_file:
        offsets = json.load(read_offset_file)

    BSVirtToISVirt = init_list(offsets, "BoomVirtualToItadakiVirtual", False)
    BSVirtToFSVirt = init_list(offsets, "BoomVirtualToFortuneVirtual", False)
    BSVirtToBSFile = init_list(offsets, "BoomVirtualToBoomFile", False)

    FSVirtToBSVirt = init_list(offsets, "BoomVirtualToFortuneVirtual", True)
    FSVirtToFSFile = init_list(offsets, "FortuneVirtualToFortuneFile", False)

    ISVirtToBSVirt = init_list(offsets, "BoomVirtualToItadakiVirtual", True)
    ISVirtToISFile = init_list(offsets, "ItadakiVirtualToItadakiFile", False)

    # Special Cases
    # Itadaki Street Wii to Fortune Street

    # Because Itadaki Street offset deltas are all a little
    # higher than Fortune Street ones, we can basically
    # subtract the Itadaki delta from the Fortune delta
    # and get our correct result, since both conversions
    # are in the same direction from Boom Street.

    for i, data in enumerate(ISVirtToBSVirt):
        begin = data.offsetBegin
        end = data.offsetEnd
        delta = data.delta - BSVirtToFSVirt[i].delta

        ISVirtToFSVirt.append(AddressSectionMapper(begin, end, delta))

    # Fortune Street to Itadaki Street

    # A similar concept works here, but I enumerate through
    # FSVirtToBSVirt instead to ensure all the offsetBegins
    # and offsetEnds line up as they should.

    for i, data in enumerate(FSVirtToBSVirt):
        begin = data.offsetBegin
        end = data.offsetEnd
        delta = BSVirtToISVirt[i].delta - data.delta

        FSVirtToISVirt.append(AddressSectionMapper(begin, end, delta))


# Address Conversion
# As above, this function is about performing a single conversion...


def convert(input, list_of_offsets, operator, destination_game, type):
    address = int(input, base=16)
    newAddress = 0
    response = f"You entered: **{address:02X}**\n"
    for section in list_of_offsets:
        if section.offsetBegin <= address and address <= section.offsetEnd:
            if operator == "add":
                newAddress = address + section.delta
            elif operator == "subtract":
                newAddress = address - section.delta
            else:
                return "Invalid request."
    if newAddress == 0:
        response += "The specified address is invalid."
        return response
    else:
        response += (
            f"The equivalent {type} address in "
            f"{destination_game} is **{newAddress:02X}**"
        )
        return response


# ...wheras the ones in this class below
# call the above to perform more complex
# conversions.


class AddressConversion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # populate the lists once
        initialize_lists()

    @app_commands.command(
        name="convert_address_to_file_offset",
        description="Convert a virtual address to file offset",
    )
    @app_commands.describe(address="The virtual address to convert")
    @app_commands.choices(
        game=[
            app_commands.Choice(name=bs, value="boom"),
            app_commands.Choice(name=fs, value="fortune"),
            app_commands.Choice(name=isw, value="itadaki"),
        ]
    )
    async def convert_to_file_offset(
        self,
        interaction: discord.Interaction,
        address: str,
        game: app_commands.Choice[str],
    ):
        # line shortening maneuvers
        a = address
        f = "file"
        send = interaction.response.send_message
        sub = "subtract"

        match game.value:
            case "boom":
                await send(convert(a, BSVirtToBSFile, sub, bs, f))
            case "fortune":
                await send(convert(a, FSVirtToFSFile, sub, fs, f))
            case "itadaki":
                await send(convert(a, ISVirtToISFile, sub, isw, f))

    @app_commands.command(
        name="convert_address_to_other_region",
        description="Convert a virtual address to another game"
    )
    @app_commands.describe(address="The address to convert")
    @app_commands.choices(
        source_game=[
            app_commands.Choice(name=bs, value="boom"),
            app_commands.Choice(name=fs, value="fortune"),
            app_commands.Choice(name=isw, value="itadaki"),
        ]
    )
    @app_commands.choices(
        destination_game=[
            app_commands.Choice(name=bs, value="boom"),
            app_commands.Choice(name=fs, value="fortune"),
            app_commands.Choice(name=isw, value="itadaki"),
        ]
    )
    async def convert_to_other_version(
        self,
        interaction: discord.Interaction,
        address: str,
        source_game: app_commands.Choice[str],
        destination_game: app_commands.Choice[str],
    ):
        # line shortening maneuvers
        a = address
        send = interaction.response.send_message
        sub = "subtract"
        v = "virtual"

        if source_game.value == destination_game.value:
            await send("Please choose different games!")

        match source_game.value:
            case "boom":
                match destination_game.value:
                    case "fortune":
                        await send(convert(a, BSVirtToFSVirt, sub, fs, v))
                    case "itadaki":
                        await send(convert(a, BSVirtToISVirt, sub, isw, v))
            case "fortune":
                match destination_game.value:
                    case "boom":
                        await send(convert(a, FSVirtToBSVirt, "add", bs, v))
                    case "itadaki":
                        await send(convert(a, FSVirtToISVirt, sub, isw, v))
            case "itadaki":
                match destination_game.value:
                    case "boom":
                        await send(convert(a, ISVirtToBSVirt, "add", bs, v))
                    case "fortune":
                        await send(convert(a, ISVirtToFSVirt, "add", fs, v))


async def setup(bot):
    await bot.add_cog(AddressConversion(bot))
