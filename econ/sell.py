from discord.ext import commands
import sys
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class sell(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def sell(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send('Proper Usage: `sell [item] [amount]`')
        elif ctx.invoked_subcommand is None:
            await ctx.send(f"you can only sell **wheat**, **wool**, or **meat**")

    @sell.command(name = 'wheat', aliases = ['wheats'])
    async def sell_wheat_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.wheats = mainbot.openfile(mainbot.WHEAT_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.wheats[user] = mainbot.wheats[user] if user in mainbot.wheats else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0
        
        if amount is None:
            amount = 1
        
        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return

        if mainbot.wheats[user] >= amount:
            money = amount * 10
            mainbot.wheats[user] -= amount
            mainbot.balances[user] += money
            embed = discord.Embed(title = 'Sale Complete', description = f'you gained `{money} coins` for selling **{amount}** wheat', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send('you don\'t have enough wheat for that')

        mainbot.savefile(mainbot.wheats, mainbot.WHEAT_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @sell.command(name = 'wool', aliases = ['wools'])
    async def sell_wool_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.wools = mainbot.openfile(mainbot.WOOL_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.wools[user] = mainbot.wools[user] if user in mainbot.wools else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0
        
        if amount is None:
            amount = 1
        
        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return
        
        if mainbot.wools[user] >= amount:
            money = amount * 15
            mainbot.wools[user] -= amount
            mainbot.balances[user] += money
            embed = discord.Embed(title = 'Sale Complete', description = f'you gained `{money} coins` for selling **{amount}** wool', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send('you don\'t have enough wool for that')

        mainbot.savefile(mainbot.wools, mainbot.WOOL_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @sell.command(name = 'meat', aliases = ['meats'])
    async def sell_meat_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.meats = mainbot.openfile(mainbot.MEAT_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.meats[user] = mainbot.meats[user] if user in mainbot.meats else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0
        
        if amount is None:
            amount = 1
        
        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return
        
        if mainbot.meats[user] >= amount:
            money = amount * 25
            mainbot.meats[user] -= amount
            mainbot.balances[user] += money
            embed = discord.Embed(title = 'Sale Complete', description = f'you gained `{money} coins` for selling **{amount}** meat', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send('you don\'t have enough meat for that') 

        mainbot.savefile(mainbot.meats, mainbot.MEAT_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

async def setup(bot):
    await bot.add_cog(sell(bot)) 
