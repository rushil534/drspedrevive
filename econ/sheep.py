from discord.ext import commands
import sys
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class sheep(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def sheep(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.healths = mainbot.openfile(mainbot.HEALTH_FILE)
        mainbot.sheeps = mainbot.openfile(mainbot.SHEEPS_FILE)  
        mainbot.wools = mainbot.openfile(mainbot.WOOL_FILE)

        mainbot.healths[user] = mainbot.healths[user] if user in mainbot.healths else 100
        mainbot.sheeps[user] = mainbot.sheeps[user] if user in mainbot.sheeps else 0
        mainbot.wools[user] = mainbot.wools[user] if user in mainbot.wools else 0 
        
        if mainbot.healths[user] >= 5:
            if mainbot.sheeps[user] > 0:
                wool = mainbot.sheeps[user] * 3
                mainbot.wools[user] += wool 
                mainbot.healths[user] -= 5
                embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :scroll: {wool} from his :sheep: sheep", color = random.choice(mainbot.random_colors))
                await ctx.send(embed = embed)   
            else:
                await ctx.send('you don\'t have any pigs!')
                self.pig.reset_cooldown(ctx)
        else:
            await ctx.send('you don\'t have enough health for this action!')
            self.pig.reset_cooldown(ctx)

        mainbot.savefile(mainbot.healths, mainbot.HEALTH_FILE)
        mainbot.savefile(mainbot.sheeps, mainbot.SHEEPS_FILE)
        mainbot.savefile(mainbot.wools, mainbot.WOOL_FILE)

    @sheep.error
    async def sheep_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to get more goods')


async def setup(bot):
    await bot.add_cog(sheep(bot)) 
