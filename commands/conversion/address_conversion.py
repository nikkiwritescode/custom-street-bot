from utils.address_section_mapper import AddressSectionMapper
from discord.ext import commands


class AddressTranslation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Fortune Street Virtual -> File Offset
    @commands.command(aliases=['fsv2fsf', 'fsvtofsf'])
    async def ConvertFSVirtualAddressToFSFileOffset(self, ctx, arg):
        FSVirtToFSFile = []
        FSVirtToFSFile.append(
            AddressSectionMapper(
                offsetBegin=0x80004000,
                offsetEnd=0x80006720,
                delta=0x80003F00
            )
        )
        FSVirtToFSFile.append(
            AddressSectionMapper(
                offsetBegin=0x80006720,
                offsetEnd=0x80006C80,
                delta=0x7FBFDA40
            )
        )
        FSVirtToFSFile.append(
            AddressSectionMapper(
                offsetBegin=0x80006C80,
                offsetEnd=0x80007480,
                delta=0x7FBFDA40
            )
        )
        FSVirtToFSFile.append(
            AddressSectionMapper(
                offsetBegin=0x80007480,
                offsetEnd=0x8040D940,
                delta=0x80004C60
            )
        )
        FSVirtToFSFile.append(
            AddressSectionMapper(
                offsetBegin=0x8040D940,
                offsetEnd=0x8040DE80,
                delta=0x80003F00
            )
        )
        FSVirtToFSFile.append(
            AddressSectionMapper(
                offsetBegin=0x8040DE80,
                offsetEnd=0x8040DEA0,
                delta=0x80003F00
            )
        )
        FSVirtToFSFile.append(
            AddressSectionMapper(
                offsetBegin=0x8040DEC0,
                offsetEnd=0x8044EA60,
                delta=0x80003F20
            )
        )
        FSVirtToFSFile.append(
            AddressSectionMapper(
                offsetBegin=0x8044EA60,
                offsetEnd=0x804AC680,
                delta=0x80003F20
            )
        )
        FSVirtToFSFile.append(
            AddressSectionMapper(
                offsetBegin=0x80814A80,
                offsetEnd=0x808171C0,
                delta=0x8036C320
            )
        )
        FSVirtToFSFile.append(
            AddressSectionMapper(
                offsetBegin=0x80818DA0,
                offsetEnd=0x8081EDE0,
                delta=0x8036DF00
            )
        )

        address = int(arg, base=16)
        newAddress = 0
        for section in FSVirtToFSFile:
            if section.offsetBegin <= address and address <= section.offsetEnd:
                newAddress = address - section.delta
        if newAddress == 0 or newAddress == address:
            await ctx.send(
                "The specified Fortune Street Virtual Address " +
                "is invalid."
            )
        else:
            newAddressString = f"{newAddress:02X}"
            await ctx.send(
                "The equivalent Fortune Street File Offset " +
                f"is: **{newAddressString}**"
            )

    # Boom Street Virtual -> File Offset
    @commands.command(aliases=['bsv2bsf', 'bsvtobsf'])
    async def ConvertBSVirtualAddressToBSFileOffset(self, ctx, arg):
        BSVirtToBSFile = []
        BSVirtToBSFile.append(
            AddressSectionMapper(
                offsetBegin=0x80004000,
                offsetEnd=0x80006720,
                delta=0x80003F00
            )
        ),
        BSVirtToBSFile.append(
            AddressSectionMapper(
                offsetBegin=0x80006720,
                offsetEnd=0x80006C80,
                delta=0x7FBFDA00
            )
        ),
        BSVirtToBSFile.append(
            AddressSectionMapper(
                offsetBegin=0x80006C80,
                offsetEnd=0x80007480,
                delta=0x7FBFDA00
            )
        ),
        BSVirtToBSFile.append(
            AddressSectionMapper(
                offsetBegin=0x80007480,
                offsetEnd=0x8040D980,
                delta=0x80004C60
            )
        ),
        BSVirtToBSFile.append(
            AddressSectionMapper(
                offsetBegin=0x8040D980,
                offsetEnd=0x8040DEC0,
                delta=0x80003F00
            )
        ),
        BSVirtToBSFile.append(
            AddressSectionMapper(
                offsetBegin=0x8040DEC0,
                offsetEnd=0x8040DEE0,
                delta=0x80003F00
            )
        ),
        BSVirtToBSFile.append(
            AddressSectionMapper(
                offsetBegin=0x8040DF00,
                offsetEnd=0x8044EC00,
                delta=0x80003F20
            )
        ),
        BSVirtToBSFile.append(
            AddressSectionMapper(
                offsetBegin=0x8044EC00,
                offsetEnd=0x804AC820,
                delta=0x80003F20
            )
        ),
        BSVirtToBSFile.append(
            AddressSectionMapper(
                offsetBegin=0x80814C80,
                offsetEnd=0x808173C0,
                delta=0x8036C380
            )
        ),
        BSVirtToBSFile.append(
            AddressSectionMapper(
                offsetBegin=0x80818FA0,
                offsetEnd=0x8081EFE0,
                delta=0x8036DF60
            )
        )

        address = int(arg, base=16)
        newAddress = 0
        for section in BSVirtToBSFile:
            if section.offsetBegin <= address and address <= section.offsetEnd:
                newAddress = address - section.delta
        if newAddress == 0 or newAddress == address:
            await ctx.send(
                "The specified Boom Street Virtual Address "
                + "is invalid."
            )
        else:
            newAddressString = f"{newAddress:02X}"
            await ctx.send(
                "The equivalent Boom Street File Offset " +
                f"is: **{newAddressString}**"
            )

    @commands.command(aliases=['fsv2bsv', 'fsvtobsv'])
    async def ConvertFSVirtualAddressToBSVirtualAddress(self, ctx, arg):
        FSVirtToBSVirt = []
        FSVirtToBSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x80000100,
                offsetEnd=0x8007A283,
                delta=0x0
            )
        ),
        FSVirtToBSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x8007A2F4,
                offsetEnd=0x80268717,
                delta=0x54
            )
        ),
        FSVirtToBSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x80268720,
                offsetEnd=0x8040D97B,
                delta=0x50
            )
        ),
        FSVirtToBSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x8040D980,
                offsetEnd=0x8041027F,
                delta=0x40
            )
        ),
        FSVirtToBSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x804105F0,
                offsetEnd=0x8044EBE7,
                delta=0x188
            )
        ),
        FSVirtToBSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x8044EC00,
                offsetEnd=0x804AC804,
                delta=0x1A0
            )
        ),
        FSVirtToBSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x804AC880,
                offsetEnd=0x8081F013,
                delta=0x200
            )
        )

        address = int(arg, base=16)
        newAddress = 0
        for section in FSVirtToBSVirt:
            if section.offsetBegin <= address and address <= section.offsetEnd:
                newAddress = address + section.delta
        if newAddress == 0:
            await ctx.send(
                "The specified Fortune Street Virtual Address is invalid."
            )
        elif address == newAddress:
            newAddressString = f"{newAddress:02X}"
            await ctx.send(
                f"The address {newAddressString} is the same in Boom Street "
                + "as it is in Fortune Street."
            )
        else:
            newAddressString = f"{newAddress:02X}"
            await ctx.send(
                "The equivalent Boom Street Virtual Address is: " +
                f"**{newAddressString}**"
            )

    @commands.command(aliases=['bsv2fsv', 'bsvtofsv'])
    async def ConvertBSVirtualAddressToFSVirtualAddress(self, ctx, arg):
        BSVirtToFSVirt = []
        BSVirtToFSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x80000100,
                offsetEnd=0x8007A283,
                delta=0x0
            )
        ),
        BSVirtToFSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x8007A2F4,
                offsetEnd=0x80268717,
                delta=0x54
            )
        ),
        BSVirtToFSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x80268720,
                offsetEnd=0x8040D97B,
                delta=0x50
            )
        ),
        BSVirtToFSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x8040D980,
                offsetEnd=0x8041027F,
                delta=0x40
            )
        ),
        BSVirtToFSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x804105F0,
                offsetEnd=0x8044EBE7,
                delta=0x188
            )
        ),
        BSVirtToFSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x8044EC00,
                offsetEnd=0x804AC804,
                delta=0x1A0
            )
        ),
        BSVirtToFSVirt.append(
            AddressSectionMapper(
                offsetBegin=0x804AC880,
                offsetEnd=0x8081F013,
                delta=0x200
            )
        )

        address = int(arg, base=16)
        newAddress = 0
        for section in BSVirtToFSVirt:
            if section.offsetBegin <= address and address <= section.offsetEnd:
                newAddress = address - section.delta
        if newAddress == 0:
            await ctx.send(
                "The specified Boom Street Virtual Address is invalid."
            )
        elif address == newAddress:
            newAddressString = f"{newAddress:02X}"
            await ctx.send(
                f"The address {newAddressString} is the same " +
                "in Fortune Street as it is in Boom Street."
            )
        else:
            newAddressString = f"{newAddress:02X}"
            await ctx.send(
                "The equivalent Fortune Street Virtual Address is: " +
                f"**{newAddressString}**"
            )


def setup(bot):
    bot.add_cog(AddressTranslation(bot))
