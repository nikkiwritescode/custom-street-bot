from utils.address_section_mapper import AddressSectionMapper
from discord.ext import commands
import json

offset_json_path = "commands/conversion/offsets/offsets.json"

BSVirtToISVirt = []
BSVirtToFSVirt = []
BSVirtToBSFile = []
FSVirtToFSFile = []


def initialize_lists():
    with open(offset_json_path, "r") as read_offset_file:
        offset_dict = json.load(read_offset_file)

    for row in offset_dict["BoomVirtualToItadakiVirtual"]:
        BSVirtToISVirt.append(
            AddressSectionMapper(
                offsetBegin=row[0],
                offsetEnd=row[1],
                delta=row[2]
            )
        )

    for row in offset_dict["BoomVirtualToFortuneVirtual"]:
        BSVirtToFSVirt.append(
            AddressSectionMapper(
                offsetBegin=row[0],
                offsetEnd=row[1],
                delta=row[2]
            )
        )

    for row in offset_dict["BoomVirtualToBoomFile"]:
        BSVirtToBSFile.append(
            AddressSectionMapper(
                offsetBegin=row[0],
                offsetEnd=row[1],
                delta=row[2]
            )
        )

    for row in offset_dict["FortuneVirtualToFortuneFile"]:
        FSVirtToFSFile.append(
            AddressSectionMapper(
                offsetBegin=row[0],
                offsetEnd=row[1],
                delta=row[2]
            )
        )


def convert_address(input, list_of_offsets, operator, destination_game, type):
    address = int(input, base=16)
    newAddress = 0
    for section in list_of_offsets:
        begin = int(section.offsetBegin, base=16)
        end = int(section.offsetEnd, base=16)
        delta = int(section.delta, base=16)

        if begin <= address and address <= end:
            if(operator == "add"):
                newAddress = address + delta
            elif(operator == "subtract"):
                newAddress = address - delta
            else:
                return ("Invalid request.")
    if newAddress == 0 or newAddress == address:
        return ("The specified address is invalid.")
    else:
        return (
            f"The equivalent {type} address in "
            f"{destination_game} is **{newAddress:02X}**"
        )


class AddressTranslation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # populate the lists once
        initialize_lists()

    # Boom Street Virtual -> Boom Street File Offset
    @commands.command(aliases=['bsv2bsf', 'bsvtobsf'])
    async def ConvertBSVirtualAddressToBSFileOffset(self, ctx, arg):
        await ctx.send(
            convert_address(
                arg,
                BSVirtToBSFile,
                "subtract",
                "Boom Street",
                "file"
            )
        )

    # Boom Street Virtual -> Fortune Street Virtual
    @commands.command(aliases=['bsv2fsv', 'bsvtofsv'])
    async def ConvertBSVirtualAddressToFSVirtualAddress(self, ctx, arg):
        await ctx.send(
            convert_address(
                arg,
                BSVirtToFSVirt,
                "subtract",
                "Fortune Street",
                "virtual"
            )
        )

    # Boom Street Virtual -> Itadaki Street Wii Virtual
    @commands.command(aliases=['bsv2isv', 'bsvtoisv'])
    async def ConvertBSVirtualAddressToISVirtualAddress(self, ctx, arg):
        await ctx.send(
            convert_address(
                arg,
                BSVirtToISVirt,
                "subtract",
                "Itadaki Street Wii",
                "virtual"
            )
        )

    # Fortune Street Virtual -> Boom Street Virtual
    @commands.command(aliases=['fsv2bsv', 'fsvtobsv'])
    async def ConvertFSVirtualAddressToBSVirtualAddress(self, ctx, arg):
        await ctx.send(
            convert_address(
                arg,
                BSVirtToFSVirt,
                "add",
                "Boom Street",
                "virtual"
            )
        )

    # Fortune Street Virtual -> Fortune Street File Offset
    @commands.command(aliases=['fsv2fsf', 'fsvtofsf'])
    async def ConvertFSVirtualAddressToFSFileOffset(self, ctx, arg):
        await ctx.send(
            convert_address(
                arg,
                FSVirtToFSFile,
                "subtract",
                "Fortune Street",
                "file"
            )
        )

    # Itadaki Street Virtual -> Boom Street Virtual
    @commands.command(aliases=['isv2bsv', 'isvtobsv'])
    async def ConvertISVirtualAddressToBSVirtualAddress(self, ctx, arg):
        await ctx.send(
            convert_address(
                arg,
                BSVirtToISVirt,
                "add",
                "Boom Street",
                "virtual"
            )
        )


def setup(bot):
    bot.add_cog(AddressTranslation(bot))
