from utils.address_section_mapper import AddressSectionMapper
from discord.ext import commands
import json

offset_json_path = "commands/conversion/offsets/offsets.json"

BSVirtToISVirt = []
BSVirtToFSVirt = []
BSVirtToBSFile = []
FSVirtToBSVirt = []
FSVirtToFSFile = []
ISVirtToBSVirt = []
ISVirtToFSVirt = []
ISVirtToISFile = []

def initialize_lists():
    with open(offset_json_path, "r") as read_offset_file:
        offset_dict = json.load(read_offset_file)

    for row in offset_dict["BoomVirtualToItadakiVirtual"]:
        BSVirtToISVirt.append(
            AddressSectionMapper(
                offsetBegin=int(row[0], base=16),
                offsetEnd=int(row[1], base=16),
                delta=int(row[2], base=16)
            )
        )

    for row in offset_dict["BoomVirtualToFortuneVirtual"]:
        BSVirtToFSVirt.append(
            AddressSectionMapper(
                offsetBegin=int(row[0], base=16),
                offsetEnd=int(row[1], base=16),
                delta=int(row[2], base=16)
            )
        )

    for row in offset_dict["BoomVirtualToBoomFile"]:
        BSVirtToBSFile.append(
            AddressSectionMapper(
                offsetBegin=int(row[0], base=16),
                offsetEnd=int(row[1], base=16),
                delta=int(row[2], base=16)
            )
        )

    for row in offset_dict["BoomVirtualToFortuneVirtual"]:
        begin = int(row[0], base=16)
        end = int(row[1], base=16)
        delta = int(row[2], base=16)

        FSVirtToBSVirt.append(
            AddressSectionMapper(
                offsetBegin=begin-delta,
                offsetEnd=end-delta,
                delta=delta
            )
        )

    for row in offset_dict["FortuneVirtualToFortuneFile"]:
        FSVirtToFSFile.append(
            AddressSectionMapper(
                offsetBegin=int(row[0], base=16),
                offsetEnd=int(row[1], base=16),
                delta=int(row[2], base=16)
            )
        )

    for row in offset_dict["BoomVirtualToItadakiVirtual"]:
        begin = int(row[0], base=16)
        end = int(row[1], base=16)
        delta = int(row[2], base=16)

        ISVirtToBSVirt.append(
            AddressSectionMapper(
                offsetBegin=begin-delta,
                offsetEnd=end-delta,
                delta=delta
            )
        )
    
    for row in offset_dict["ItadakiVirtualToItadakiFile"]:
        ISVirtToISFile.append(
            AddressSectionMapper(
                offsetBegin=int(row[0], base=16),
                offsetEnd=int(row[1], base=16),
                delta=int(row[2], base=16)
            )
        )

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

        ISVirtToFSVirt.append(
            AddressSectionMapper(
                offsetBegin=begin,
                offsetEnd=end,
                delta=delta
            )
        )

    # Fortune Street to Itadaki Street

    # A similar concept works here, but I enumerate through
    # FSVirtToBSVirt instead to ensure all the offsetBegins
    # and offsetEnds line up as they should.

    for i, data in enumerate(FSVirtToBSVirt):
        begin = data.offsetBegin
        end = data.offsetEnd
        delta = BSVirtToISVirt[i].delta - data.delta

        print(f"{hex(begin)}, {hex(end)}, {hex(delta)}")

        ISVirtToFSVirt.append(
            AddressSectionMapper(
                offsetBegin=begin,
                offsetEnd=end,
                delta=delta
            )
        )


def convert_address(input, list_of_offsets, operator, destination_game, type):
    address = int(input, base=16)
    newAddress = 0
    for section in list_of_offsets:
        if section.offsetBegin <= address and address <= section.offsetEnd:
            if(operator == "add"):
                newAddress = address + section.delta
            elif(operator == "subtract"):
                newAddress = address - section.delta
            else:
                return ("Invalid request.")
    if newAddress == 0:
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
                FSVirtToBSVirt,
                "add",
                "Boom Street",
                "virtual"
            )
        )

    # Fortune Street Virtual -> Itadaki Street Wii Virtual
    @commands.command(aliases=['fsv2isv', 'fsvtoisv'])
    async def ConvertFSVirtualAddressToISVirtualAddress(self, ctx, arg):
        await ctx.send(
            convert_address(
                arg,
                ISVirtToFSVirt,
                "subtract",
                "Itadaki Street Wii",
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
                ISVirtToBSVirt,
                "add",
                "Boom Street",
                "virtual"
            )
        )

    # Itadaki Street Virtual -> Fortune Street Virtual
    @commands.command(aliases=['isv2fsv', 'isvtofsv'])
    async def ConvertISVirtualAddressToFSVirtualAddress(self, ctx, arg):
        await ctx.send(
            convert_address(
                arg,
                ISVirtToFSVirt,
                "add",
                "Fortune Street",
                "virtual"
            )
        )
    
    # Itadaki Street Virtual -> Itadaki Street File Offset
    @commands.command(aliases=['isv2isf', 'isvtoisf'])
    async def ConvertISVirtualAddressToISFileOffset(self, ctx, arg):
        await ctx.send(
            convert_address(
                arg,
                ISVirtToISFile,
                "subtract",
                "Itadaki Street",
                "file"
            )
        )


def setup(bot):
    bot.add_cog(AddressTranslation(bot))
