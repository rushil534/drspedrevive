from discord.ext import commands
import sys
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class buffalo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def buffalo(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.healths = mainbot.openfile(mainbot.HEALTH_FILE)
        mainbot.wheats = mainbot.openfile(mainbot.WHEAT_FILE)  
        mainbot.meats = mainbot.openfile(mainbot.MEAT_FILE)
        mainbot.buffalos = mainbot.openfile(mainbot.BUFFALOS_FILE)

        mainbot.healths[user] = mainbot.healths[user] if user in mainbot.healths else 100
        mainbot.wheats[user] = mainbot.wheats[user] if user in mainbot.wheats else 0
        mainbot.meats[user] = mainbot.meats[user] if user in mainbot.meats else 0 
        mainbot.buffalos[user] = mainbot.buffalos[user] if user in mainbot.buffalos else 0

        if mainbot.healths[user] >= 20:
            if mainbot.buffalos[user] > 0:
                mainbot.wheats[user] = mainbot.wheats[user] if user in mainbot.wheats else 0
                mainbot.meats[user] = mainbot.meats[user] if user in mainbot.meats else 0
                wheat2 = mainbot.buffalos[user] * 10000
                mainbot.wheats[user] += wheat2
                meat2 = mainbot.buffalos[user] * 10000
                mainbot.meats[user] += meat2
                mainbot.healths[user] -= 20
                mainbot.buffalos[user] = 0
                embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :cut_of_meat: {meat2} meat and :ear_of_rice: {wheat2} wheat from his :water_buffalo: Buffalos", color = random.choice(mainbot.random_colors))
                await ctx.send(embed = embed)   
            else:
                await ctx.send('you don\'t have any buffalos!')
                self.buffalo.reset_cooldown(ctx)
        else:
            await ctx.send('you don\'t have enough health for this action!')
            self.buffalo.reset_cooldown(ctx)

        mainbot.savefile(mainbot.buffalos, mainbot.BUFFALOS_FILE)
        mainbot.savefile(mainbot.wheats, mainbot.WHEAT_FILE)
        mainbot.savefile(mainbot.healths, mainbot.HEALTH_FILE)
        mainbot.savefile(mainbot.meats, mainbot.MEAT_FILE)

    @buffalo.error
    async def buffalo_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to get more goods ')


async def setup(bot):
    await bot.add_cog(buffalo(bot)) 
