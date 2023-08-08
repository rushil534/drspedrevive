import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason = None):
        
        if reason == None:
            reason = "no reason given"

        if member == ctx.message.author:
            await ctx.send('?')
            return
        
        if member == None:
            await ctx.send('kick who?')
            return
        
        if member == self.bot.user:
            await ctx.send('??')
            return

        server = ctx.message.guild
        
        try:
            await member.kick(reason = reason)
            await ctx.send(f'```{member} was kicked\nReason: {reason}```')
        except discord.errors.Forbidden as e:
            await ctx.send(f'i can\'t do that, **{member.name}** probably has more perms than me')
        

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Kick Members`!')
        if isinstance(error, commands.MemberNotFound):
            await ctx.send('that person isn\'t here buddy')


async def setup(bot):
    await bot.add_cog(kick(bot))   
