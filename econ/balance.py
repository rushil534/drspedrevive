from discord.ext import commands
import sys
import json
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

balances = mainbot.balances
BALANCES_FILE = mainbot.BALANCES_FILE
random_colors = mainbot.random_colors

class balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['bal'])
    async def balance(self, ctx, member: discord.Member = None): 
        try:
            with open(BALANCES_FILE, 'r') as fp: 
                balances = json.load(fp) 
        except FileNotFoundError:
            print(f'In on_ready(): File {BALANCES_FILE} not found. Starting off with an empty balances dictionary.') 
            balances = {}

        user = str(ctx.message.author.id)
        if member is None:
            if user in balances:
                embed = discord.Embed(title=f":moneybag: {ctx.message.author.name}'s balance", description=f"**Bank Account**: {balances[user]:,d}/ꝏ", color = random.choice(random_colors))
                await ctx.send(embed=embed)
            else:
                balances[user] = 100
                await ctx.send('You didnt have an account so i made you one with a start of 100 coins')
        else:
            if str(member.id) in balances:
                embed = discord.Embed(title=f":moneybag: {member.name}'s balance", description=f"**Bank Account**: {balances[str(member.id)]:,d}/ꝏ", color = random.choice(random_colors))
                await ctx.send(embed=embed)
            else:
                await ctx.send('user doesn\'t have an acc')

async def setup(bot):
    await bot.add_cog(balance(bot)) 
