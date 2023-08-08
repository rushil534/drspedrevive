import discord
from discord.ext import commands

class userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['ui'])
    async def userinfo(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author

        roles = [role for role in member.roles]

        embed = discord.Embed(colour = member.color, timestamp = ctx.message.created_at)

        embed.set_author(name = f"User Info - {member}")
        embed.set_thumbnail(url = member.avatar)
        embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar)

        embed.add_field(name = "ID:", value = member.id)
        embed.add_field(name = "Server name:", value = member.display_name)
        embed.add_field(name = "Created at:", value = member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
        embed.add_field(name = "Joined at:", value = member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))

        embed.add_field(name = f"Roles ({len(roles)})", value = " ".join([role.mention for role in roles]))
        embed.add_field(name = "Top role:", value = member.top_role.mention)

        embed.add_field(name="Bot?", value = member.bot)

        await ctx.send(embed=embed) 

async def setup(bot):
    await bot.add_cog(userinfo(bot))   
