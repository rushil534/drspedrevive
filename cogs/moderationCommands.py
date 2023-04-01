import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import has_permissions

class moderationCommands(commands.Cog):
	def __init__(self, bot):
			self.bot = bot
	
	autoPurge = False

	@commands.command(aliases = ['ui'])
	async def userinfo(self, ctx, member: discord.Member):
		roles = [role for role in member.roles]

		embed=discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

		embed.set_author(name=f"User Info - {member}")
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)

		embed.add_field(name="ID:", value=member.id)
		embed.add_field(name="Guild name:", value=member.display_name)
		embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
		embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))

		embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
		embed.add_field(name="Top role:", value=member.top_role.mention)

		embed.add_field(name="Bot?", value=member.bot)
		embed.add_field(name="Idiot?", value="True")

		await ctx.send(embed=embed) 


	@commands.command()
	@has_permissions(manage_channels = True)
	async def autopurge(self, ctx, amount: int, seconds: float):
		await ctx.send(f'`{amount}` messages will delete every `{seconds}` seconds\nTo stop this, do `le stoppurge`')
		global autoPurge
		autoPurge = True
		while autoPurge == True:
			await asyncio.sleep(seconds)
			await ctx.channel.purge(limit = amount)
			
	@commands.group(invoke_without_command = True)
	async def new(self, ctx):
		await ctx.send('Proper Usage: `le new [category/channel]`')

	@new.command() 
	@commands.guild_only()
	@has_permissions(manage_guild = True)
	async def category(self, ctx, *, name: str):
		category = await ctx.guild.create_category(name = name)
		await ctx.send(f'Category: `{category.name}` created!')

	@new.command() 
	@commands.guild_only()
	@has_permissions(manage_channels = True)
	async def channel(self, ctx, categoryid : int, *, name):
		channel = await ctx.guild.create_text_channel(name = name, category = self.bot.get_channel(categoryid))
		await ctx.send(f'Channel: `{channel.name}` created!')

	@commands.group(invoke_without_command = True)
	async def delete(self, ctx):
		await ctx.send('Proper Usage: `le delete [thecategory/thechannel]`')

	@delete.command() 
	@commands.guild_only()
	@has_permissions(manage_guild = True)
	async def thecategory(self, ctx, category: discord.CategoryChannel):
		await category.delete()
		await ctx.send(f'Category: `{category.name}` deleted!')

	@delete.command() 
	@commands.guild_only()
	@has_permissions(manage_channels = True)
	async def thechannel(self, ctx, channel: discord.TextChannel = None):
		channel = channel or ctx.channel
		await channel.delete()
		await ctx.send(f'Channel: `{channel.name}` deleted!')

	@commands.command()
	@has_permissions(manage_channels = True)
	async def purge(self, ctx, amount: int):
		await ctx.channel.purge(limit = amount + 1)
		await ctx.send('Purged!', delete_after = 2)

	@commands.command() 
	@commands.guild_only()
	@has_permissions(manage_channels = True)
	async def lock(self, ctx, channel: discord.TextChannel = None):
		channel = channel or ctx.channel

		if ctx.guild.default_role not in channel.overwrites:
			overwrites = {
				ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
			}
			await channel.edit(overwrites= overwrites)
			await channel.send(f'This channel has been locked :lock:')
		elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
			overwrites = channel.overwrites[ctx.guild.default_role]
			overwrites.send_messages = False
			await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
			embed = discord.Embed(title = ':lock: This channel has been locked', description = 'This channel has been locked', color = discord.Color.red())
			await channel.send(embed=embed)

	@commands.command() 
	@commands.guild_only()
	@has_permissions(manage_channels = True)
	async def unlock(self, ctx, channel: discord.TextChannel = None):
		channel = channel or ctx.channel

		overwrites = channel.overwrites[ctx.guild.default_role]
		overwrites.send_messages = True
		await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
		embed = discord.Embed(title = ':unlock: This channel has been unlocked', description = 'This channel has been unlocked', color = discord.Color.green())
		await channel.send(embed=embed)

	@commands.command()
	async def stoppurge(self, ctx):
		global autoPurge
		autoPurge = False
		await ctx.send('done')


	@commands.command()
	@has_permissions(ban_members = True)
	async def ban(self, ctx, member: discord.Member, *, reason=None):
		server = ctx.message.guild
		if member == ctx.message.author:
				await ctx.send("are you **REALLY** going to try to ban **YOURSELF**")
				return
		elif member == None:
				await ctx.send('whatchu think ima do without a user to ban')
		elif reason == None:
				reason = "No reason given"
				await member.ban(reason=reason)
				await ctx.send(f"```{member} was banned\nReason: {reason}```")
				message = f"You were banned from {server}\nReason: {reason}"
				await member.send(message)
		else:
				await member.ban(reason=reason)
				await ctx.send(f"```{member} was banned\nReason: {reason}```")
				message = f"You were banned from {server}\nReason: {reason}"
				await member.send(message)



	@commands.command()
	@has_permissions(ban_members = True)
	async def unban(self, ctx, member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')
		
		for ban_entry in banned_users:
				user = ban_entry.user

				if (user.name, user.discriminator) == (member_name, member_discriminator):
						await ctx.guild.unban(user)
						await ctx.send(f'Unbanned {user.mention}')
						return

	@commands.command()
	async def ping(self, ctx):
			await ctx.send(f'`{round(self.bot.latency * 1000)}ms`')

	@commands.command()
	@has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member, *, reason = None):
			if member == ctx.message.author:
					await ctx.send('are you **REALLY** going to try to kick **YOURSELF**')
			elif member == None:
					await ctx.send('whatchu think ima do without a user to kick')
			elif reason == None:
					server = ctx.message.guild
					reason = "No reason given"
					await member.kick(reason=reason)
					await ctx.send(f'```{member} was kicked\nReason: {reason}```')
					message = f"You were kicked from {server}\nReason: {reason}"
					await member.send(message)
			else:
					server = ctx.message.guild
					await member.kick(reason = reason)
					await ctx.send(f'```{member} was kicked\nReason: {reason}```')
					message = f"You were kicked from {server}\nReason: {reason}"
					await member.send(message)





	@commands.command()
	@has_permissions(manage_roles=True)
	async def warn(self, ctx, member: discord.Member = None, *, reason = None):
			server = ctx.message.guild
			if member == ctx.message.author:
					await ctx.send('are you **REALLY** going to try to warn **YOURSELF**')
			elif member == None:
					await ctx.send('whatchu think ima do without a user to warn')
			elif reason == None:
					reason = "No reason given"
					await ctx.send(f'```{member} was warned\nReason: {reason}```')
					message = f"You were warned in {server}\nReason: {reason}"
					await member.send(message)
			else:
					await ctx.send(f'```{member} was warned\nReason: {reason}```')
					message = f"You were warned from {server}\nReason: {reason}"
					await member.send(message)

	@commands.command(aliases = ['cr'])
	@has_permissions(manage_roles = True)
	async def createrole(self, ctx, *, message: str):
			guild = ctx.guild
			await guild.create_role(name=message)
			await ctx.send(f'Role: `{message}` created!')

	#--------------
	# Errors
	#--------------

	@purge.error
	async def purge_error(self, ctx, error):
			if isinstance(error, commands.MissingRequiredArgument):
					await ctx.send('Proper Usage: `le purge [amount of msgs u wana delete]`')
			elif isinstance(error, commands.MissingPermissions):
					await ctx.send('You don\'t have the perm: `Manage Channels`!')
	
	@category.error
	async def category_error(self, ctx, error):
			if isinstance(error, commands.MissingRequiredArgument):
					await ctx.send('Proper Usage: `le new category [name]`')
			elif isinstance(error, commands.MissingPermissions):
					await ctx.send('You don\'t have the perm: `Manage Server`!')

	@thecategory.error
	async def thecategory_error(self, ctx, error):
			if isinstance(error, commands.MissingRequiredArgument):
					await ctx.send('Proper Usage: `le delete thecategory [category id]`')
			elif isinstance(error, commands.MissingPermissions):
					await ctx.send('You don\'t have the perm: `Manage Server`!')

	@channel.error
	async def channel_error(self, ctx, error):
			if isinstance(error, commands.MissingRequiredArgument):
					await ctx.send('Proper Usage: `le new channel [category id] [name]`')
			elif isinstance(error, commands.MissingPermissions):
					await ctx.send('You don\'t have the perm: `Manage channels`!')


	@autopurge.error
	async def autopurge_error(self, ctx, error):
			if isinstance(error, commands.MissingRequiredArgument):
					await ctx.send('Proper Usage: `le autopurge [amount of messages you want to delete] [every x seconds]`')
			elif isinstance(error, commands.MissingPermissions):
					await ctx.send('You don\'t have the perm: `Manage Channels`!')

	@ban.error
	async def ban_error(self, ctx, error):
			if isinstance(error, commands.MissingRequiredArgument):
					await ctx.send('Proper Usage: `le ban [user] [reason]`')
			elif isinstance(error, commands.MissingPermissions):
					await ctx.send('You don\'t have the perm: `Ban Members`!')

	@kick.error
	async def kick_error(self, ctx, error):
			if isinstance(error, commands.MissingRequiredArgument):
					await ctx.send('Proper Usage: `le kick [user] [reason]`')
			elif isinstance(error, commands.MissingPermissions):
					await ctx.send('You don\'t have the perm: `Kick Members`!')

	@unban.error
	async def unban_error(self, ctx, error):
			if isinstance(error, commands.MissingRequiredArgument):
					await ctx.send('Proper Usage: `le unban [user name#user discriminator]`\n`EX: le unban loser#0000`')
			elif isinstance(error, commands.MissingPermissions):
					await ctx.send('You don\'t have the perm: `Ban Members`!')

	@warn.error
	async def warn_error(self, ctx, error):
			if isinstance(error, commands.MissingRequiredArgument):
					await ctx.send('Proper Usage: `le warn [user] [reason]`')
			elif isinstance(error, commands.MissingPermissions):
					await ctx.send('You don\'t have the perm: `Manage Roles`!')
	
	@createrole.error
	async def cr_error(self, ctx, error):
			if isinstance(error, commands.MissingRequiredArgument):
					await ctx.send('Proper Usage: `le createrole [name]`')
			elif isinstance(error, commands.MissingPermissions):
					await ctx.send('You don\'t have the perm: `Manage Roles`!')


	@userinfo.error
	async def userinfo_error(self, ctx, error):
			member = ctx.message.author
			roles = [role for role in member.roles]

			embed=discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

			embed.set_author(name=f"User Info - {member}")
			embed.set_thumbnail(url=member.avatar_url)
			embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)

			embed.add_field(name="ID:", value=member.id)
			embed.add_field(name="Guild name:", value=member.display_name)
			embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
			embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))

			embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
			embed.add_field(name="Top role:", value=member.top_role.mention)

			embed.add_field(name="Bot?", value=member.bot)
			embed.add_field(name="Idiot?", value="True")

			await ctx.send(embed=embed) 

async def setup(bot):
	await bot.add_cog(moderationCommands(bot))
