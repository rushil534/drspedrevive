from discord.ext import commands
import discord
from discord.ext.commands import has_permissions
from discord import ChannelType

class new(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def new(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send('Proper Usage: `new [category/channel/role/thread]`')
        elif ctx.invoked_subcommand is None:
            await ctx.send('not an option')
    
    @new.command(name = 'category')
    @commands.guild_only()
    @has_permissions(manage_guild = True)
    async def new_category_subcommand(self, ctx, *, name: str = None):
        if name == None:
            await ctx.send('i need a name for the category')
            return
        
        try:
            category = await ctx.guild.create_category(name = name)
            await ctx.send(f'Category: `{category.name}` created!')
        except Exception:
            await ctx.send('you made an error somewhere')
    
    @new.command(name = 'channel')
    @commands.guild_only()
    @has_permissions(manage_channels = True)
    async def new_channel_subcommand(self, ctx, category: discord.CategoryChannel = None, *, name: str = None):
        if category == None:
            await ctx.send('give me a category to create the channel in')
            return

        if name == None:
            await ctx.send('i need a name for the channel')
            return

        try:
            channel = await ctx.guild.create_text_channel(name = name, category = category)
            await ctx.send(f'Channel: `{channel.name}` created!')
        except Exception:
            await ctx.send('you made an error somewhere')

    @new.command(name = 'role')
    @commands.guild_only()
    @has_permissions(manage_roles = True)
    async def new_role_subcommand(self, ctx, *, name: str = None):
        if name == None:
            await ctx.send('i need a name for this role')
            return

        try:
            await ctx.guild.create_role(name = name)
            await ctx.send(f'Role `{name}` created!')
        except Exception:
            await ctx.send('you made an error somewhere')

    @new.command(name = 'thread')
    @commands.guild_only()
    @has_permissions(create_public_threads = True, create_private_threads = True)
    async def new_thread_subcommand(self, ctx, channel: discord.TextChannel = None, *, name: str = None):
        if channel == None:
            await ctx.send('i need a channel to create a thread in')
            return
        
        if name == None:
            await ctx.send('i need a name for this thread')
            return
        
        await ctx.send('do you want a `private` or a `public` thread?')
        msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)

        if msg.content.lower() == 'public':
            try:
                await channel.create_thread(name = name, type = ChannelType.public_thread)
                await ctx.send(f'Thread `{name}` Created!')
            except Exception:
                await ctx.send('you made an error somewhere')
        elif msg.content.lower() == 'private':
            try:
                await channel.create_thread(name = name, type = ChannelType.private_thread)
                await ctx.send(f'Thread `{name}` Created!')
            except Exception:
                await ctx.send('you made an error somewhere')
        else:
            await ctx.send('that\'s not an option')

    @new_category_subcommand.error
    async def new_category_subcommand_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Manage Server`!')
        
    @new_channel_subcommand.error
    async def new_channel_subcommand_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Manage Channels`!')
        if isinstance(error, commands.BadArgument):
            await ctx.send('that category is invalid')

    @new_role_subcommand.error
    async def new_role_subcommand_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the perm: `Manage Roles`!')

    @new_thread_subcommand.error
    async def new_thread_subcommand_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have either the `Create Public Threads` or `Create Private Threads` Perm!')
        if isinstance(error, commands.BadArgument):
            await ctx.send('that channel is invalid')
        

async def setup(bot):
    await bot.add_cog(new(bot))
