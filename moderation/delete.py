from discord.ext import commands
import discord
from discord.ext.commands import has_permissions

class delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def delete(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send('Proper Usage: `delete [category/channel/role]`')
        elif ctx.invoked_subcommand is None:
            await ctx.send('not an option')
    
    @delete.command(name = 'category')
    @commands.guild_only()
    @has_permissions(manage_guild = True)
    async def delete_category_subcommand(self, ctx, category: discord.CategoryChannel = None):
        if category == None:
            await ctx.send('give me a category to delete')
            return

        try:
            await category.delete()
            await ctx.send(f'Category: `{category.name}` deleted!')
        except Exception:
            await ctx.send('an error occurred')
    
    @delete.command(name = 'channel')
    @commands.guild_only()
    @has_permissions(manage_channels = True)
    async def delete_channel_subcommand(self, ctx, channel: discord.TextChannel = None):
        if channel == None:
            await ctx.send('give me a channel to delete')
            return
        
        try:
            await channel.delete()
            await ctx.send(f'Channel: `{channel.name}` deleted!')
        except Exception:
            await ctx.send('an error occurred')

    @delete.command(name = 'role')
    @commands.guild_only()
    @has_permissions(manage_roles = True)
    async def delete_role_subcommand(self, ctx, role: discord.Role = None):
        if role == None:
            await ctx.send('give me a role to delete')
            return

        try:
            await role.delete()
            await ctx.send(f'Role: `{role.name}` deleted!')
        except Exception:
            await ctx.send('an error occured')

    @delete_category_subcommand.error
    async def delete_category_subcommand_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Manage Server`!')
        if isinstance(error, commands.BadArgument):
            await ctx.send('that category is invalid')

    @delete_channel_subcommand.error
    async def delete_channel_subcommand_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Manage Channels`!')
        if isinstance(error, commands.BadArgument):
            await ctx.send('that channel is invalid')

    @delete_role_subcommand.error
    async def delete_role_subcommand_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Manage Roles`!')
        if isinstance(error, commands.BadArgument):
            await ctx.send('that role is invalid')

async def setup(bot):
    await bot.add_cog(delete(bot))
