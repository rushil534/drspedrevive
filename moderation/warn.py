from discord.ext import commands
from discord.ext.commands import has_permissions
import discord

class warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(manage_roles = True)
    async def warn(self, ctx, member: discord.Member = None, *, reason: str = None):
        server = ctx.message.guild
        if member == ctx.message.author:
            await ctx.send('?')
            return
        
        if member == None:
            await ctx.send('i need someone to warn')
            return
        
        if member == self.bot.user:
            await ctx.send('??')
            return

        if reason == None:
            reason = "No reason given"

        await ctx.send(f'```{member} was warned\nReason: {reason}```')
        channel = await member.create_dm()
        await channel.send(f"You were warned in {server}\nReason: {reason}")

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send('that person isn\'t here buddy')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Manage Roles`!')

async def setup(bot):
    await bot.add_cog(warn(bot))   
