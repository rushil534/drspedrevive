from discord.ext import commands
import sys

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class use(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def use(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send('Proper Usage: `use [item]`')
        elif ctx.invoked_subcommand is None:
            await ctx.send(f"you can only use **ambulances** or **bread**")

    @use.command(name = 'ambulance', aliases = ['ambulances'])
    async def use_ambulance_subcommand(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.ambulances = mainbot.openfile(mainbot.AMBULANCES_FILE)
        mainbot.healths = mainbot.openfile(mainbot.HEALTH_FILE) 

        mainbot.ambulances[user] = mainbot.ambulances[user] if user in mainbot.ambulances else 0
        mainbot.healths[user] = mainbot.healths[user] if user in mainbot.healths else 0

        if mainbot.ambulances[user] >= 1:
            if mainbot.healths[user] < 100:
                mainbot.healths[user] = 100
                mainbot.ambulances[user] -= 1
                await ctx.send(f'{ctx.message.author.mention} has just healed themselves to 100 health!')
            else:
                await ctx.send('you can\'t dose that, you have full health!')
        else:
            await ctx.send('you don\'t have any ambulances')

        mainbot.savefile(mainbot.ambulances, mainbot.AMBULANCES_FILE)
        mainbot.savefile(mainbot.healths, mainbot.HEALTH_FILE)

    @use.command(name = 'bread', aliases = ['breads'])
    async def use_bread_subcommand(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.bread = mainbot.openfile(mainbot.BREAD_FILE)
        mainbot.healths = mainbot.openfile(mainbot.HEALTH_FILE)

        mainbot.bread[user] = mainbot.bread[user] if user in mainbot.bread else 0
        mainbot.healths[user] = mainbot.healths[user] if user in mainbot.healths else 0

        if mainbot.bread[user] >= 1:
            if mainbot.healths[user] < 60:
                mainbot.healths[user] = 60
                mainbot.bread[user] -= 1
                await ctx.send(f'{ctx.message.author.mention} has just healed themselves to 60 health!')
            else:
                await ctx.send('you have more than 60 health')
        else:
            await ctx.send('you have no bread')

        mainbot.savefile(mainbot.bread, mainbot.BREAD_FILE)
        mainbot.savefile(mainbot.healths, mainbot.HEALTH_FILE)

async def setup(bot):
    await bot.add_cog(use(bot)) 
