from discord.ext import commands
import sys

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.cities = mainbot.openfile(mainbot.CITIES_FILE)
        mainbot.locations = mainbot.openfile(mainbot.LOCATIONS_FILE)
        mainbot.citypop = mainbot.openfile(mainbot.CITYPOP_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.cities[user] = mainbot.cities[user] if user in mainbot.cities else 0
        mainbot.locations[user] = mainbot.locations[user] if user in mainbot.locations else 0
        mainbot.citypop[user] = mainbot.citypop[user] if user in mainbot.citypop else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0

        if mainbot.locations[user] == 1:
            if mainbot.cities[user] == 0:
                await ctx.send('This will cost you `350000` coins. And it will cost a lot to maintain it.\nyou up for it? `y` or `n`')
                msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)
                if msg.content.lower() == 'y' or msg.content.lower() == 'Y':
                    if mainbot.balances[user] >= 350000:
                        await ctx.send(f'Congratulations {ctx.message.author.mention}! you started off with a **basic city**')
                        mainbot.balances[user] -= 350000
                        mainbot.cities[user] += 1
                        mainbot.citypop[user] = 0
                    else:
                        await ctx.send('get more money')
                elif msg.content.lower() == 'n' or msg.content.lower() == 'N':
                    await ctx.send('alr no city for u')
                else:
                    await ctx.send('not an option')
            else:
                await ctx.send('you already have a city')
        else:
            await ctx.send('you must be in Texas to create a city!')

        mainbot.savefile(mainbot.cities, mainbot.CITIES_FILE)
        mainbot.savefile(mainbot.locations, mainbot.LOCATIONS_FILE)
        mainbot.savefile(mainbot.citypop, mainbot.CITYPOP_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

async def setup(bot):
    await bot.add_cog(create(bot)) 
