from discord.ext import commands
from discord.ext.commands import has_permissions
import discord

class lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() 
    @commands.guild_only()
    @has_permissions(manage_channels = True)
    async def lock(self, ctx, channel: discord.TextChannel = None):
        if channel == None:
            channel = ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites = overwrites)
            await channel.send(f'This channel has been locked :lock:')
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            embed = discord.Embed(title = ':lock: This channel has been locked', description = 'This channel has been locked', color = discord.Color.red())
            await channel.send(embed=embed)

    @lock.error
    async def lock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Manage Channels`!')

async def setup(bot):
    await bot.add_cog(lock(bot))   
