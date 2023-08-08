from discord.ext import commands
from discord.ext.commands import has_permissions
import discord

class unlock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() 
    @commands.guild_only()
    @has_permissions(manage_channels = True)
    async def unlock(self, ctx, channel: discord.TextChannel = None):
        if channel == None:
            channel = ctx.channel

        overwrites = channel.overwrites[ctx.guild.default_role]
        overwrites.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite = overwrites)
        embed = discord.Embed(title = ':unlock: This channel has been unlocked', description = 'This channel has been unlocked', color = discord.Color.green())
        await channel.send(embed=embed)
                
    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Manage Channels`!')

async def setup(bot):
    await bot.add_cog(unlock(bot))   
