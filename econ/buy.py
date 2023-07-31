from discord.ext import commands
import sys
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class buy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def buy(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send('Proper Usage: `buy [item] [amount]`')
        elif ctx.invoked_subcommand is None:
            await ctx.send(f"that doesn't exist bud")
        
    @buy.command(name = 'morris')
    async def buy_morris_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.morris = mainbot.openfile(mainbot.MORRIS_FILE)
        mainbot.meats = mainbot.openfile(mainbot.MEAT_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)
        mainbot.wheats = mainbot.openfile(mainbot.WHEAT_FILE)
        mainbot.salads = mainbot.openfile(mainbot.SALADS_FILE)

        mainbot.morris[user] = mainbot.morris[user] if user in mainbot.morris else 0
        mainbot.meats[user] = mainbot.meats[user] if user in mainbot.meats else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0
        mainbot.wheats[user] = mainbot.wheats[user] if user in mainbot.wheats else 0
        mainbot.salads[user] = mainbot.salads[user] if user in mainbot.salads else 0

        if amount is None:
            amount = 1
        
        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return
        
        if mainbot.balances[user] >= 10000:
            if mainbot.meats[user] >= 1500:
                if mainbot.salads[user] >= 3:
                    if mainbot.wheats[user] >= 5000:
                        mainbot.wheats[user] -= 5000
                        mainbot.salads[user] -= 3
                        mainbot.meats[user] -= 1500
                        mainbot.balances[user] -= 10000
                        mainbot.morris[user] += 1
                        await ctx.send(f'Congratulations {ctx.message.author.mention}! you bought a Morris X8200 jet!')
                    else: 
                        await ctx.send('you don\'t have enough wheat for this')
                else:
                    await ctx.send('you don\'t have enough salads for this')
            else:
                await ctx.send('you don\'t have enough meat for this')
        else:
            await ctx.send('you don\'t have enough money for this')

        mainbot.savefile(mainbot.morris, mainbot.MORRIS_FILE)
        mainbot.savefile(mainbot.meats, mainbot.MEAT_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)
        mainbot.savefile(mainbot.wheats, mainbot.WHEAT_FILE)
        mainbot.savefile(mainbot.salads, mainbot.SALADS_FILE)

    @buy.command(name = 'douglas')
    async def buy_douglas_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.douglas = mainbot.openfile(mainbot.DOUGLAS_FILE)
        mainbot.stoves = mainbot.openfile(mainbot.STOVES_FILE)
        mainbot.meats = mainbot.openfile(mainbot.MEAT_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)
        mainbot.salads = mainbot.openfile(mainbot.SALADS_FILE)

        mainbot.douglas[user] = mainbot.douglas[user] if user in mainbot.douglas else 0
        mainbot.stoves[user] = mainbot.stoves[user] if user in mainbot.stoves else 0
        mainbot.meats[user] = mainbot.meats[user] if user in mainbot.meats else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0
        mainbot.salads[user] = mainbot.salads[user] if user in mainbot.salads else 0

        if amount is None:
            amount = 1
        
        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return

        if mainbot.balances[user] >= 75000:
            if mainbot.meats[user] >= 5000:
                if mainbot.salads[user] >= 20:
                    if mainbot.stoves[user] >= 10:
                        mainbot.meats[user] -= 5000
                        mainbot.salads[user] -= 20
                        mainbot.stoves[user] -= 10
                        mainbot.balances[user] -= 75000
                        mainbot.douglas[user] += 1
                        await ctx.send(f'Congratulations {ctx.message.author.mention}! you bought a Douglas 900ER jet!')
                    else:
                        await ctx.send('you don\'t have enough stoves for this')
                else:
                    await ctx.send('you don\'t have enough salads for this')
            else:
                await ctx.send('you don\'t have enough meat for this')
        else:
            await ctx.send('you don\'t have enough money for this')

        mainbot.savefile(mainbot.douglas, mainbot.DOUGLAS_FILE)
        mainbot.savefile(mainbot.stoves, mainbot.STOVES_FILE)
        mainbot.savefile(mainbot.meats, mainbot.MEAT_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)
        mainbot.savefile(mainbot.salads, mainbot.SALADS_FILE)

    @buy.command(name = 'sheep', aliases = ['sheeps'])
    async def buy_sheep_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.sheeps = mainbot.openfile(mainbot.SHEEPS_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.sheeps[user] = mainbot.sheeps[user] if user in mainbot.sheeps else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0
        
        if amount is None:
            amount = 1
        
        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return
        
        pfs = amount * 100
        if mainbot.balances[user] >= pfs:
            mainbot.sheeps[user] += amount
            mainbot.balances[user] -= pfs
            embed = discord.Embed(title = 'Purchase Complete', description = f'you bought **{amount}** sheep for `{pfs} coins`', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send(f'you don\'t have enough to buy {amount} sheeps')

        mainbot.savefile(mainbot.sheeps, mainbot.SHEEPS_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @buy.command(name = 'bread', aliases = ['breads'])
    async def buy_bread_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.bread = mainbot.openfile(mainbot.BREAD_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.bread[user] = mainbot.bread[user] if user in mainbot.bread else 0 
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0

        if amount is None:
            amount = 1

        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return
        
        pfb = amount * 1200
        if mainbot.balances[user] >= pfb:
            mainbot.bread[user] += amount
            mainbot.balances[user] -=  pfb
            embed = discord.Embed(title = 'Purchase Complete', description = f'you bought **{amount}** bread for `{pfb} coins`', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send(f'you don\'t have enough to buy {amount} bread!')

        mainbot.savefile(mainbot.bread, mainbot.BREAD_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @buy.command(name = 'bowl', aliases = ['bowls'])
    async def buy_bowl_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.bowls = mainbot.openfile(mainbot.BOWLS_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.bowls[user] = mainbot.bowls[user] if user in mainbot.bowls else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0

        if amount is None:
            amount = 1
        
        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return
        
        pfb = amount * 50
        if mainbot.balances[user] >= pfb:
            mainbot.bowls[user] += amount
            mainbot.balances[user] -= pfb
            embed = discord.Embed(title = 'Purchase Complete', description = f'you bought **{amount}** bowls for `{pfb} coins`', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send(f'you don\'t have enough to buy {amount} bowls')

        mainbot.savefile(mainbot.bowls, mainbot.BOWLS_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)
    
    @buy.command(name = 'rice', aliases = ['rices'])
    async def buy_rice_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.rices = mainbot.openfile(mainbot.RICE_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.rices[user] = mainbot.rices[user] if user in mainbot.rices else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0

        if amount is None:
            amount = 1
        
        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return
        
        pfr = amount * 30
        if mainbot.balances[user] >= pfr:
            mainbot.rices[user] += amount
            mainbot.balances[user] -= pfr
            embed = discord.Embed(title = 'Purchase Complete', description = f'you bought **{amount}** rice for `{pfr} coins`', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send(f'you don\'t have enough to buy {amount} rice')

        mainbot.savefile(mainbot.rices, mainbot.RICE_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @buy.command(name = 'pig', aliases = ['pigs'])
    async def buy_pig_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.pigs = mainbot.openfile(mainbot.PIG_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.pigs[user] = mainbot.pigs[user] if user in mainbot.pigs else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0

        if amount is None:
            amount = 1

        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return

       
        pfp = amount * 200
        if mainbot.balances[user] >= pfp:
            mainbot.pigs[user] += amount
            mainbot.balances[user] -= pfp
            embed = discord.Embed(title = 'Purchase Complete', description = f'you bought **{amount}** pigs for `{pfp} coins`', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send(f'you don\'t have enough to buy {amount} pig(s)')

        mainbot.savefile(mainbot.pigs, mainbot.PIG_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    
    @buy.command(name = 'ambulance', aliases = ['ambulances'])
    async def buy_ambulance_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)
        
        mainbot.ambulances = mainbot.openfile(mainbot.AMBULANCES_FILE)
        mainbot.meats = mainbot.openfile(mainbot.MEAT_FILE)

        mainbot.ambulances[user] = mainbot.ambulances[user] if user in mainbot.ambulances else 0
        mainbot.meats[user] = mainbot.meats[user] if user in mainbot.meats else 0

        if amount is None:
            amount = 1

        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return

        pfa = amount * 15200
        if mainbot.meats[user] >= pfa:
            mainbot.ambulances[user] += amount
            mainbot.meats[user] -= pfa
            embed = discord.Embed(title = 'Purchase Complete', description = f'you bought **{amount}** ambulances for `{pfa} meat`', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send(f'you don\'t have enough to buy {amount} ambulances!')

        mainbot.savefile(mainbot.ambulances, mainbot.AMBULANCES_FILE)
        mainbot.savefile(mainbot.meats, mainbot.MEAT_FILE)
        
    @buy.command(name = 'buffalo', aliases = ['buffalos'])
    async def buy_buffalo_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.buffalos = mainbot.openfile(mainbot.BUFFALOS_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.buffalos[user] = mainbot.buffalos[user] if user in mainbot.buffalos else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0

        if amount is None:
            amount = 1

        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return
        
        pfb = amount * 10000000
        if mainbot.balances[user] >= pfb:
            mainbot.buffalos[user] += amount
            mainbot.balances[user] -= pfb
            embed = discord.Embed(title = 'Purchase Complete', description = f'you bought **{amount}** buffalo for `{pfb} coins`', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send(f'you don\'t have enough to buy {amount} buffalos!')
    
        mainbot.savefile(mainbot.buffalos, mainbot.BUFFALOS_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @buy.command(name = 'stove', aliases = ['stoves'])
    async def buy_stove_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.stoves = mainbot.openfile(mainbot.STOVES_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.stoves[user] = mainbot.stoves[user] if user in mainbot.stoves else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0

        if amount is None:
            amount = 1

        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return
        
        pfs = amount * 19500
        if mainbot.balances[user] >= pfs:
            mainbot.stoves[user] += amount
            mainbot.balances[user] -= pfs
            embed = discord.Embed(title = 'Purchase Complete', description = f'you bought **{amount}** stoves for `{pfs} coins`', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send(f'you don\'t have enough to buy {amount} stoves!')

        mainbot.savefile(mainbot.stoves, mainbot.STOVES_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @buy.command(name = 'chicken', aliases = ['chickens'])
    async def buy_chicken_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.uncooked_chickens = mainbot.openfile(mainbot.UNCOOKED_CHICKENS_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.uncooked_chickens[user] = mainbot.uncooked_chickens[user] if user in mainbot.uncooked_chickens else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0

        if amount is None:
            amount = 1

        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return

        pfuc = amount * 10000
        if mainbot.balances[user] >= pfuc:
            mainbot.uncooked_chickens[user] += amount
            mainbot.balances[user] -= pfuc
            embed = discord.Embed(title = 'Purchase Complete', description = f'you bought **{amount}** uncooked chickens for `{pfuc} coins`', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send(f'you don\'t have enough to buy {amount} uncooked chicken(s)!')

        mainbot.savefile(mainbot.uncooked_chickens, mainbot.UNCOOKED_CHICKENS_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @buy.command(name = 'pc', aliases = ['pcs'])
    async def buy_pc_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.pc = mainbot.openfile(mainbot.PC_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.pc[user] = mainbot.pc[user] if user in mainbot.pc else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0

        if amount is None:
            amount = 1

        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return

        pfl = amount * 1500
        if mainbot.alances[user] >= pfl:
            mainbot.pc[user] += amount
            mainbot.balances[user] -= pfl
            embed = discord.Embed(title = 'Purchase Complete', description = f'you bought **{amount}** laptop(s) for `{pfl} coins`', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send(f'you don\'t have enough to buy {amount} pc(s)!')

        mainbot.savefile(mainbot.pc, mainbot.PC_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @buy.command(name = 'mooshroom', aliases = ['mooshrooms'])
    async def buy_mooshroom_subcommand(self, ctx, amount: int = None):
        user = str(ctx.message.author.id)

        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)
        mainbot.mooshroom_cows = mainbot.openfile(mainbot.MOOSHROOM_COW_FILE)

        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0
        mainbot.mooshroom_cows[user] = mainbot.mooshroom_cows[user] if user in mainbot.mooshroom_cows else 0

        if amount is None:
            amount = 1

        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return

        pfmc = 14400 * amount
        if mainbot.balances[user] >= pfmc:
            mainbot.mooshroom_cows[user] += amount
            mainbot.balances[user] -= pfmc
            embed = discord.Embed(title = 'Purchase Complete', description = f'you bought **{amount}** mooshroom cows for `{pfmc} coins`', color = random.choice(mainbot.random_colors))
            await ctx.send(embed = embed)
        else:
            await ctx.send(f'you don\'t have enough to buy {amount} mooshroom cows!')

        mainbot.savefile(mainbot.mooshroom_cows, mainbot.MOOSHROOM_COW_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

async def setup(bot):
    await bot.add_cog(buy(bot)) 
