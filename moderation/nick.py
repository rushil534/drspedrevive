import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class nick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(manage_nicknames = True)
    async def nick(self, ctx, member: discord.Member = None, *, newnick: str = None):
        if member == None:
            await ctx.send('i need someone\'s nickname to change')
            return
        
        if member.nick == newnick:
            await ctx.send('that user already has that nickname')
            return

        if newnick == None:
            newnick = str(member.name)

        oldnick = member.nick

        try:
            await member.edit(nick = newnick)
            await ctx.send(f'changed {member.mention}\'s nickname from {oldnick} to {newnick}')
        except discord.errors.Forbidden:
            await ctx.send('i can\'t do that')

    @nick.error
    async def nick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Manage Nicknames`!')
        if isinstance(error, commands.MemberNotFound):
            await ctx.send('that person isn\'t here buddy')

async def setup(bot):
    await bot.add_cog(nick(bot))   
