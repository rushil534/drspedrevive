from discord.ext import commands
import sys
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class pig(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def pig(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.healths = mainbot.openfile(mainbot.HEALTH_FILE)
        mainbot.pigs = mainbot.openfile(mainbot.PIG_FILE)  
        mainbot.meats = mainbot.openfile(mainbot.MEAT_FILE)

        mainbot.healths[user] = mainbot.healths[user] if user in mainbot.healths else 100
        mainbot.pigs[user] = mainbot.pigs[user] if user in mainbot.pigs else 0
        mainbot.meats[user] = mainbot.meats[user] if user in mainbot.meats else 0 
        
        if mainbot.healths[user] >= 5:
            if mainbot.pigs[user] > 0:
                meat = mainbot.pigs[user] * 6
                mainbot.meats[user] += meat
                mainbot.pigs[user] = 0
                mainbot.healths[user] -= 5
                embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :cut_of_meat: {meat} from his :pig2: pigs", color = random.choice(mainbot.random_colors))
                await ctx.send(embed = embed)   
            else:
                await ctx.send('you don\'t have any pigs!')
                self.pig.reset_cooldown(ctx)
        else:
            await ctx.send('you don\'t have enough health for this action!')
            self.pig.reset_cooldown(ctx)

        mainbot.savefile(mainbot.healths, mainbot.HEALTH_FILE)
        mainbot.savefile(mainbot.pigs, mainbot.PIG_FILE)
        mainbot.savefile(mainbot.meats, mainbot.MEAT_FILE)

    @pig.error
    async def pig_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to get more goods')


async def setup(bot):
    await bot.add_cog(pig(bot)) 
