from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio

class autopurge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    autoPurge = False

    @commands.command()
    @has_permissions(manage_channels = True)
    async def autopurge(self, ctx, amount: int, seconds: float):
        if seconds < 3:
            await ctx.send('interval must be 3 or more seconds')
            return
        
        await ctx.send(f'`{amount}` messages will delete every `{seconds}` seconds\nTo stop this, use the command `stoppurge`')
        global autoPurge
        autoPurge = True
        while autoPurge == True:
            await asyncio.sleep(seconds)
            await ctx.channel.purge(limit = amount)
        
    @commands.command()
    async def stoppurge(self, ctx):
        global autoPurge
        autoPurge = False
        await ctx.send('done')

    @autopurge.error
    async def autopurge_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `autopurge [# of messages you want deleted] [every x seconds]`')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Manage Channels`!')

async def setup(bot):
    await bot.add_cog(autopurge(bot))   
