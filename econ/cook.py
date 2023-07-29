from discord.ext import commands
import sys
import json
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class cook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context = True)
    async def cook(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send('Proper Usage: `cook [item]`')
        elif ctx.invoked_subcommand is None:
            await ctx.send(f"you can only cook **chicken**")

    @cook.command(name = 'chicken', aliases = ['chickens'])
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def cook_chicken_subcommand(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.healths = mainbot.openfile(mainbot.HEALTH_FILE)
        mainbot.stoves = mainbot.openfile(mainbot.STOVES_FILE)
        mainbot.cooked_chickens = mainbot.openfile(mainbot.COOKED_CHICKENS_FILE)
        mainbot.uncooked_chickens = mainbot.openfile(mainbot.UNCOOKED_CHICKENS_FILE)

        mainbot.healths[user] = mainbot.healths[user] if user in mainbot.healths else 100
        mainbot.stoves[user] = mainbot.stoves[user] if user in mainbot.stoves else 0
        mainbot.cooked_chickens[user] = mainbot.cooked_chickens[user] if user in mainbot.cooked_chickens else 0
        mainbot.uncooked_chickens[user] = mainbot.uncooked_chickens[user] if user in mainbot.uncooked_chickens else 0 

        if mainbot.healths[user] >= 10:
            if mainbot.stoves[user] > 0:
                if mainbot.uncooked_chickens[user] > 0:
                    chicken = mainbot.uncooked_chickens[user] * 3
                    mainbot.cooked_chickens[user] += chicken
                    mainbot.healths[user] -= 10
                    mainbot.stoves[user] -= 1 
                    embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :chicken: {chicken} chickens from his :hatched_chick: Uncooked Chickens!", color = random.choice(mainbot.random_colors))
                    await ctx.send(embed = embed)   
                else:
                    await ctx.send('You don\'t have any uncooked chicken!')  
                    self.cook_chicken_subcommand.reset_cooldown(ctx)
            else:
                await ctx.send('You don\'t have any stoves!')
                self.cook_chicken_subcommand.reset_cooldown(ctx)
        else:
            await ctx.send('You don\'t have enough health for this action!')

        mainbot.savefile(mainbot.healths, mainbot.HEALTH_FILE)
        mainbot.savefile(mainbot.stoves, mainbot.STOVES_FILE)
        mainbot.savefile(mainbot.cooked_chickens, mainbot.COOKED_CHICKENS_FILE)
        mainbot.savefile(mainbot.uncooked_chickens, mainbot.UNCOOKED_CHICKENS_FILE)

    @cook_chicken_subcommand.error
    async def cook_chicken_subcommand_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to cook chicken again')
            return

async def setup(bot):
    await bot.add_cog(cook(bot)) 
