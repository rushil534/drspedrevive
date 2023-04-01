import discord
from discord.ext import commands
import random

class otherCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    random_colors = [0xFFFFFF, 0x1ABC9C, 0x2ECC71, 0x3498DB, 0x9B59B6, 0xE91E63, 0xF1C40F, 0xE67E22, 0xE74C3C, 0x34495E, 0x11806A, 0x1F8B4C, 0x206694]


    @commands.command()
    async def mainstuff(self, ctx):
        random_colors = [0xFFFFFF, 0x1ABC9C, 0x2ECC71, 0x3498DB, 0x9B59B6, 0xE91E63, 0xF1C40F, 0xE67E22, 0xE74C3C, 0x34495E, 0x11806A, 0x1F8B4C, 0x206694]
        embed = discord.Embed(title = 'links for other stuffz', description = '[Bot Invite](https://discord.com/api/oauth2/authorize?client_id=666867717961285663&permissions=8&scope=bot)', color = random.choice(random_colors))
        await ctx.send(embed = embed)
        
    @commands.command()
    async def dmdev(self, ctx, *, message: str):
        dev = self.bot.get_user(486662307217276948)
        await dev.send(f'**{ctx.message.author}**, also known as **{ctx.message.author.id}** has said **{message}**')
        await ctx.send('ye that man got ur message')

    @commands.command(aliases = ['rs'])
    async def resend(self, ctx, id: int, *, message: str):
        person = self.bot.get_user(id)
        await person.send(f'The bot owner replied with: {message}')
        dev = self.bot.get_user(486662307217276948)
        await dev.send('ye he got it')

async def setup(bot):
    await bot.add_cog(otherCommands(bot))
