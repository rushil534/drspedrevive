from discord.ext import commands
from discord.ext.commands import has_permissions

class purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(manage_channels = True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit = amount + 1)
        await ctx.send('done', delete_after = 2)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `purge [# of messages you want deleted]`')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Manage Channels`!')

async def setup(bot):
    await bot.add_cog(purge(bot))   
