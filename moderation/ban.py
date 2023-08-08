from discord.ext import commands
from discord.ext.commands import has_permissions
import discord

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member = None, *, reason: str = None):
        server = ctx.message.guild
        if member == ctx.message.author:
            await ctx.send("?")
            return
        
        if member == None:
            await ctx.send('i need someone to ban')
            return
        
        if reason == None:
            reason = "No reason given"

        if member == self.bot.user:
            await ctx.send('??')
            return

        try:
            await member.ban(reason = reason)
            await ctx.send(f"```{member} was banned\nReason: {reason}```")
        except discord.errors.Forbidden:
            await ctx.send(f'i can\'t do that, **{member.name}** probably has more perms than me')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Ban Members`!')
        if isinstance(error, commands.MemberNotFound):
            await ctx.send('that person isn\'t here buddy')
        

async def setup(bot):
    await bot.add_cog(ban(bot))   
