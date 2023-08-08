from discord.ext import commands
from discord.ext.commands import has_permissions
import discord

class unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(ban_members = True)
    async def unban(self, ctx, user: discord.User = None):
        if user == None:
            await ctx.send('i need someone to unban')
        try:
            await ctx.guild.unban(user)
            await ctx.send('done')
        except discord.errors.NotFound:
            await ctx.send(f'i can\'t do that, **{user.name}** probably has more perms than me')
        
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Ban Members`!')
        if isinstance(error, commands.UserNotFound):
            await ctx.send('that person isn\'t in this server\'s bans')

async def setup(bot):
    await bot.add_cog(unban(bot))   
