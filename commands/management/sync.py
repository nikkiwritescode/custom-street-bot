import discord
from typing import Literal, Optional
from discord.ext import commands
from discord.ext.commands import Greedy, Context

# Command for syncing the bot's commands to the guild. It works as follows:
# !sync -> global sync
# !sync ~ -> sync current guild
# !sync * -> copies all global app commands to current guild and syncs
# !sync ^ -> clears all commands from the current guild target and syncs
# !sync id_1 id_2 -> syncs guilds with id 1 and 2

# this is a normal, typed command since
# slash commands are what we're needing to sync


class SyncBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_role("⚠ Staff")  # only staff can use this command
    async def sync(
        self,
        ctx: Context,
        guilds: Greedy[discord.Object],
        spec: Optional[Literal["~", "*", "^"]] = None,
    ) -> None:
        if not guilds:
            if spec == "~":
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "*":
                ctx.bot.tree.copy_global_to(guild=ctx.guild)
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "^":
                ctx.bot.tree.clear_commands(guild=ctx.guild)
                await ctx.bot.tree.sync(guild=ctx.guild)
                synced = []
            else:
                synced = await ctx.bot.tree.sync()

            response = (
                f"Synced {len(synced)} commands ",
                f"{'globally' if spec is None else 'to the current guild.'}",
            )
            await ctx.send("".join(response))
            return

        ret = 0
        for guild in guilds:
            try:
                await ctx.bot.tree.sync(guild=guild)
            except discord.HTTPException:
                pass
            else:
                ret += 1

        await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")


async def setup(bot):
    await bot.add_cog(SyncBot(bot))
