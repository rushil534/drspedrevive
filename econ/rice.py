from discord.ext import commands
import sys
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class rice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def rice(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.healths = mainbot.openfile(mainbot.HEALTH_FILE)
        mainbot.wheats = mainbot.openfile(mainbot.WHEAT_FILE)
        mainbot.rices = mainbot.openfile(mainbot.RICE_FILE)

        mainbot.healths[user] = mainbot.healths[user] if user in mainbot.healths else 100
        mainbot.wheats[user] = mainbot.wheats[user] if user in mainbot.wheats else 0
        mainbot.rices[user] = mainbot.rices[user] if user in mainbot.rices else 0 
        
        
        if mainbot.healths[user] >= 5:
            if mainbot.rices[user] > 0:
                wheat = mainbot.rices[user] * 4
                mainbot.wheats[user] += wheat
                mainbot.healths[user] -= 5  
                mainbot.rices[user] = 0
                embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :tanabata_tree: {wheat} wheat from his :rice: rice", color = random.choice(mainbot.random_colors))
                await ctx.send(embed = embed)   
            else:
                await ctx.send('you don\'t have any rice')
                self.rice.reset_cooldown(ctx)
        else:
            await ctx.send('you don\'t have enough health for this action!')
            self.rice.reset_cooldown(ctx)

        mainbot.savefile(mainbot.healths, mainbot.HEALTH_FILE)
        mainbot.savefile(mainbot.wheats, mainbot.WHEAT_FILE)
        mainbot.savefile(mainbot.rices, mainbot.RICE_FILE)

    @rice.error
    async def rice_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to get more goods  ')


async def setup(bot):
    await bot.add_cog(rice(bot)) 
