from discord.ext import commands
import sys
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['bal'])
    async def balance(self, ctx, member: discord.Member = None): 
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        user = str(ctx.message.author.id)
        if member is None:
            if user in mainbot.balances:
                embed = discord.Embed(title=f":moneybag: {ctx.message.author.name}'s balance", description=f"**Bank Account**: {mainbot.balances[user]:,d}/ꝏ", color = random.choice(mainbot.random_colors))
                await ctx.send(embed=embed)
            else:
                await ctx.send(f'{mainbot.NO_BANK_ACC}')
        else:
            if str(member.id) in mainbot.balances:
                embed = discord.Embed(title=f":moneybag: {member.name}'s balance", description=f"**Bank Account**: {mainbot.balances[str(member.id)]:,d}/ꝏ", color = random.choice(mainbot.random_colors))
                await ctx.send(embed=embed)
            else:
                await ctx.send('user doesn\'t have an acc')

async def setup(bot):
    await bot.add_cog(balance(bot)) 
