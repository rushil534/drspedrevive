from discord.ext import commands
import sys
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class plead(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def plead(self, ctx):
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)
        mainbot.healths = mainbot.openfile(mainbot.HEALTH_FILE)
        mainbot.locations = mainbot.openfile(mainbot.LOCATIONS_FILE)

        INCREMENT = random.randint(20, 70)
        user = str(ctx.message.author.id) 

        if user in mainbot.balances: 
            names = ["**Kanye West**", "**Lindsay Lohan**", "**Azealia Banks**", "**Justin Bieber**", "**Roseanne Barr**", "**Charlie Sheen**", "**Amanda Bynes**", "**Woody Allen**", "**Mel Gibson**", "**R. Kelly**"]
            await ctx.send(random.choice(names) + f' donated {INCREMENT} coins to {ctx.message.author.mention}!')
            mainbot.balances[user] += INCREMENT
        else: 
            mainbot.balances[user] = mainbot.START_BAL 
            mainbot.healths[user] = 100
            mainbot.locations[user] = 0
            await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with {mainbot.START_BAL} coins') 
            self.plead.reset_cooldown(ctx)

        mainbot.savefile(mainbot.healths, mainbot.HEALTH_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)
        mainbot.savefile(mainbot.locations, mainbot.LOCATIONS_FILE)

    @plead.error
    async def plead_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to plead again ')
            return

async def setup(bot):
    await bot.add_cog(plead(bot)) 
