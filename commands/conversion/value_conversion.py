from discord.ext import commands
import struct


class ValueConversion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # From Hex
    @commands.command(name="hex2int")
    async def hexToInt(self, ctx, arg):
        try:
            await ctx.send(int(arg, base=16))
        except ValueError:
            await ctx.send("Please enter a valid hexidecimal value!")

    @commands.command(name="hex2float")
    async def hexToFloat(self, ctx, arg):
        try:
            await ctx.send(struct.unpack('!f', bytes.fromhex(arg))[0])
        except ValueError:
            await ctx.send("Please enter a valid hexidecimal value!")

    # To Hex
    @commands.command(name="int2hex")
    async def intToHex(self, ctx, arg):
        try:
            num = int(arg)
            assert type(num) == int, await ctx.send(
                "Please enter a valid integer value."
            )
            await ctx.send(hex(num))
        except ValueError:
            await ctx.send("Please enter a valid integer value.")

    @commands.command(name="float2hex")
    async def floatToHex(self, ctx, arg):
        try:
            num = float(arg)
            assert type(num) == float, await ctx.send(
                "Please enter a valid floating-point value."
            )
            await ctx.send(hex(struct.unpack('<I', struct.pack('<f', num))[0]))
        except ValueError:
            await ctx.send("Please enter a valid floating-point value.")


def setup(bot):
    bot.add_cog(ValueConversion(bot))
