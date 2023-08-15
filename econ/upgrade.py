from discord.ext import commands
import discord
import sys
import random
import asyncio

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class upgrade(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def upgrade(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send('Proper Usage: `upgrade [requirements/key/shop/power/water/waste/fire/police/health/entertainment/parks]`')
        elif ctx.invoked_subcommand is None:
            await ctx.send(f"that doesn't exist buddy")
        
    @upgrade.command(name = 'key')
    async def upgrade_key(self, ctx):
        await ctx.send('__**Upgrading in your city**__\n\t- First, spend your money on the URGENT needs for the city such as: Fire, Health, and Police\n\t- Boost population by upgrading Parks and Entertainment\n\t- The more population you get, the more revenue you get!\n\t- Find the requirements to get medium and advanced city with `le requirements [advanced city/medium city]`\n\t- Do `le collect [fire/health/police/entertainment/park]`\n\t- Do `le upgrade [section of city]` to upgrade the section\'s levels for revenue!')

    @upgrade.command(name = 'requirements')
    async def upgrade_requirements(self, ctx, citytype: str = None):
        if citytype == None:
            await ctx.send('Proper usage: `upgrade requirements [medium/advanced]`')
            return
        
        if citytype.lower() == 'medium':
            await ctx.send('__**Requirements for Medium City**__\n\t- LVL 3 Entertainment\n\t- LVL 5 Parks\n\t- LVL 2 Health\n\t- LVL 2 Fire\n\t- LVL 2 Police\n\t- LVL 3 Waste\n\t- LVL 5 Water\n\t- LVL 4 Power')

        if citytype.lower() == 'advanced':
            await ctx.send('__**Requirements for Advanced City**__\n\t- LVL 7 Entertainment\n\t- LVL 6 Parks\n\t- LVL 4 Health\n\t- LVL 4 Fire\n\t- LVL 4 Police\n\t- LVL 5 Waste\n\t- LVL 8 Water\n\t- LVL 5 Power')
    
    @upgrade.command(name = 'shop')
    async def upgrade_shop(self, ctx):
        embed = discord.Embed(title = 'Upgrading costs', description = 'The price of each item multiplies depending what level you are upgrading to\nEX: Upgrading to lvl 3 Entertainment costs 300 Meat, 36000 coins, 30 rice, and 6 salads', color = random.choice(mainbot.random_colors))
        embed.add_field(name = '**Entertainment**', value = 'Price: __100 Meat__, __12,000 coins__, __10 rice__, __2 salads__\nAdds 867 population every level upgrade', inline = True)
        embed.add_field(name = '**Parks**', value = 'Price: __230 Wheat__, __19,000 coins__, __420 wool__, __10 salads__\nAdds 1,001 population every level upgrade', inline = False)
        embed.add_field(name = '**Power**', value = 'Price: __150 Meat__, __10,400 coins__, __20 salads__\nAdds 2,467 population every level upgrade', inline = False)
        embed.add_field(name = '**Water**', value = 'Price: __260 Wheat__, __11,200 coins__, __12 salads__\nAdds 2,227 population every level upgrade', inline = False)
        embed.add_field(name = '**Waste**', value = 'Price: __320 Meat__, __15,600 coins__, __22 salads__\nAdds 3,142 population every level upgrade', inline = False)
        embed.add_field(name = '**Health**', value = 'Price: __720 Meat__, __28,920 coins__, __80 salads__\nAdds 7,819 population every level upgrade', inline = False)
        embed.add_field(name = '**Fire**', value = 'Price: __949 Wheat__, __26,200 coins__, __60 salads__\nAdds 6,231 population every level upgrade', inline = False)
        embed.add_field(name = '**Police**', value = 'Price: __1,001 Meat__, __42,620 coins__, __90 salads__\nAdds 9,331 population every level upgrade', inline = False)
        await ctx.send(embed = embed)

    @upgrade.command(name = 'parks')
    async def upgrade_parks(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.park_lvl = mainbot.openfile(mainbot.PARK_LVL_FILE)
        mainbot.cities = mainbot.openfile(mainbot.CITIES_FILE)
        mainbot.citypop = mainbot.openfile(mainbot.CITYPOP_FILE)
        mainbot.salads = mainbot.openfile(mainbot.SALADS_FILE)
        mainbot.wools = mainbot.openfile(mainbot.WOOL_FILE)
        mainbot.wheats = mainbot.openfile(mainbot.WHEAT_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.park_lvl[user] = mainbot.park_lvl[user] if user in mainbot.park_lvl else 0
        mainbot.cities[user] = mainbot.cities[user] if user in mainbot.cities else 0
        mainbot.citypop[user] = mainbot.citypop[user] if user in mainbot.citypop else 0
        mainbot.salads[user] = mainbot.salads[user] if user in mainbot.salads else 0
        mainbot.wools[user] = mainbot.wools[user] if user in mainbot.wools else 0
        mainbot.wheats[user] = mainbot.wheats[user] if user in mainbot.wheats else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0

        PARK_LEVEL_USER_UPGRADING_TO = mainbot.park_lvl[user] + 1
        WOOL_COST = PARK_LEVEL_USER_UPGRADING_TO * 420
        WHEAT_COST = PARK_LEVEL_USER_UPGRADING_TO * 230
        COINS_COST = PARK_LEVEL_USER_UPGRADING_TO * 19000
        SALADS_COST = PARK_LEVEL_USER_UPGRADING_TO * 10

        if mainbot.cities[user] == 1:
            if mainbot.park_lvl[user] < 6:
                await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{WOOL_COST}__ **wool,** __{WHEAT_COST}__ **wheat,** __{COINS_COST}__ **coins, and** __{SALADS_COST}__ **salads**\n`y` or `n`')
                msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)
                if msg.content.lower() == 'y':
                    if mainbot.salads[user] >= SALADS_COST:
                        if mainbot.balances[user] >= COINS_COST:
                            if mainbot.wools[user] >= WOOL_COST:
                                if mainbot.wheats[user] >= WHEAT_COST:
                                    mainbot.park_lvl[user] = PARK_LEVEL_USER_UPGRADING_TO
                                    mainbot.balances[user] -= COINS_COST
                                    mainbot.salads[user] -= SALADS_COST
                                    mainbot.wheats[user] -= WHEAT_COST
                                    mainbot.wools[user] -= WOOL_COST
                                    mainbot.citypop[user] += 1001
                                    await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Park**__ level is now **{PARK_LEVEL_USER_UPGRADING_TO}**\nGo check with the `city` command!')
                                    await asyncio.sleep(1)
                                    await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Population**__ is now **{mainbot.citypop[user]:,d}**\nGo check with the `city` command!')
                                else:
                                    await ctx.send('you don\'t have enough wheat for this!')
                            else:
                                await ctx.send('you don\'t have enough wool for this!')
                        else:
                            await ctx.send('you don\'t have enough coins for this!')
                    else:
                        await ctx.send('you don\'t have enough salads for this!')
                elif msg.content.lower() == 'n':
                    await ctx.send('ok')
                else:
                    await ctx.send('not an option')
            else:
                await ctx.send('you have reached the maximum level for parks!')
        else:
            await ctx.send('you don\'t have a city')

        mainbot.savefile(mainbot.park_lvl, mainbot.PARK_LVL_FILE)
        mainbot.savefile(mainbot.citypop, mainbot.CITYPOP_FILE)
        mainbot.savefile(mainbot.salads, mainbot.SALADS_FILE)
        mainbot.savefile(mainbot.wools, mainbot.WOOL_FILE)
        mainbot.savefile(mainbot.wheats, mainbot.WHEAT_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @upgrade.command(name = 'police')
    async def upgrade_police(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.police_lvl = mainbot.openfile(mainbot.POLICE_LVL_FILE)
        mainbot.cities = mainbot.openfile(mainbot.CITIES_FILE)
        mainbot.citypop = mainbot.openfile(mainbot.CITYPOP_FILE)
        mainbot.salads = mainbot.openfile(mainbot.SALADS_FILE)
        mainbot.meats = mainbot.openfile(mainbot.MEAT_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.police_lvl[user] = mainbot.police_lvl[user] if user in mainbot.police_lvl else 0
        mainbot.cities[user] = mainbot.cities[user] if user in mainbot.cities else 0
        mainbot.citypop[user] = mainbot.citypop[user] if user in mainbot.citypop else 0
        mainbot.salads[user] = mainbot.salads[user] if user in mainbot.salads else 0
        mainbot.meats[user] = mainbot.meats[user] if user in mainbot.meats else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0

        POLICE_LEVEL_USER_IS_UPGRADE_TO = mainbot.police_lvl[user] + 1
        MEAT_COST = POLICE_LEVEL_USER_IS_UPGRADE_TO * 1001
        COINS_COST = POLICE_LEVEL_USER_IS_UPGRADE_TO * 42620
        SALADS_COST = POLICE_LEVEL_USER_IS_UPGRADE_TO * 90 

        if mainbot.cities[user] == 1:
            if mainbot.police_lvl[user] < 4:
                await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{MEAT_COST}__ **meat**, __{COINS_COST}__ **coins, and** __{SALADS_COST}__ **salads**\n`y` or `n`')
                msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)
                if msg.content.lower() == 'y':
                    if mainbot.salads[user] >= SALADS_COST:
                        if mainbot.balances[user] >= COINS_COST:
                            if mainbot.meats[user] >= MEAT_COST:
                                mainbot.police_lvl[user] = POLICE_LEVEL_USER_IS_UPGRADE_TO
                                mainbot.balances[user] -= COINS_COST
                                mainbot.salads[user] -= SALADS_COST
                                mainbot.meats[user] -= MEAT_COST
                                mainbot.citypop[user] += 9331
                                await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Police**__ level is now **{POLICE_LEVEL_USER_IS_UPGRADE_TO}**\nGo check with the `city` command!')
                                await asyncio.sleep(1)
                                await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Population**__ is now **{mainbot.citypop[user]:,d}**\nGo check with the `city` command!')
                            else:
                                await ctx.send('you don\'t have enough meat for this!')
                        else:
                            await ctx.send('you don\'t have enough coins for this!')
                    else:
                        await ctx.send('you don\'t have enough salads for this!')
                elif msg.content.lower() == 'n':
                    await ctx.send('ok')
                else:
                    await ctx.send('not an option')
            else:
                await ctx.send('you have reached the maximum level for police!')
        else:
            await ctx.send('you don\'t have a city ')

        mainbot.savefile(mainbot.police_lvl, mainbot.POLICE_LVL_FILE)
        mainbot.savefile(mainbot.citypop, mainbot.CITYPOP_FILE)
        mainbot.savefile(mainbot.salads, mainbot.SALADS_FILE)
        mainbot.savefile(mainbot.meats, mainbot.MEAT_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @upgrade.command(name = 'health')
    async def upgrade_health(self, ctx):  
        user = str(ctx.message.author.id)

        mainbot.health_lvl = mainbot.openfile(mainbot.HEALTH_LVL_FILE)
        mainbot.cities = mainbot.openfile(mainbot.CITIES_FILE)
        mainbot.citypop = mainbot.openfile(mainbot.CITYPOP_FILE)
        mainbot.salads = mainbot.openfile(mainbot.SALADS_FILE)
        mainbot.meats = mainbot.openfile(mainbot.MEAT_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.health_lvl[user] = mainbot.health_lvl[user] if user in mainbot.health_lvl else 0
        mainbot.cities[user] = mainbot.cities[user] if user in mainbot.cities else 0
        mainbot.citypop[user] = mainbot.citypop[user] if user in mainbot.citypop else 0
        mainbot.salads[user] = mainbot.salads[user] if user in mainbot.salads else 0
        mainbot.meats[user] = mainbot.meats[user] if user in mainbot.meats else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0
        
        HEALTH_LEVEL_USER_IS_UPGRADE_TO = mainbot.health_lvl[user] + 1
        MEAT_COST = HEALTH_LEVEL_USER_IS_UPGRADE_TO * 720
        COINS_COST = HEALTH_LEVEL_USER_IS_UPGRADE_TO * 28290
        SALADS_COST = HEALTH_LEVEL_USER_IS_UPGRADE_TO * 80  


        if mainbot.cities[user] == 1:
            if mainbot.health_lvl[user] < 4:
                await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{MEAT_COST}__ **meat**, __{COINS_COST}__ **coins, and** __{SALADS_COST}__ **salads**\n`y` or `n`')
                msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)
                if msg.content.lower() == 'y':
                    if mainbot.salads[user] >= SALADS_COST:
                        if mainbot.balances[user] >= COINS_COST:
                            if mainbot.meats[user] >= MEAT_COST:
                                mainbot.health_lvl[user] = HEALTH_LEVEL_USER_IS_UPGRADE_TO
                                mainbot.balances[user] -= COINS_COST
                                mainbot.salads[user] -= SALADS_COST
                                mainbot.meats[user] -= MEAT_COST
                                mainbot.citypop[user] += 7819
                                await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Health**__ level is now **{HEALTH_LEVEL_USER_IS_UPGRADE_TO}**\nGo check with the `city` command!')
                                await asyncio.sleep(1)
                                await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Population**__ is now **{mainbot.citypop[user]:,d}**\nGo check with the `city` command!')
                            else:
                                await ctx.send('you don\'t have enough meat for this!')
                        else:
                            await ctx.send('you don\'t have enough coins for this!')
                    else:
                        await ctx.send('you don\'t have enough salads for this!')
                elif msg.content.lower() == 'n':
                    await ctx.send('ok')
                else:
                    await ctx.send('not an option')
            else:
                await ctx.send('you have reached the maximum level for health!')
        else:
            await ctx.send('you don\'t have a city ')

        mainbot.savefile(mainbot.police_lvl, mainbot.POLICE_LVL_FILE)
        mainbot.savefile(mainbot.citypop, mainbot.CITYPOP_FILE)
        mainbot.savefile(mainbot.salads, mainbot.SALADS_FILE)
        mainbot.savefile(mainbot.meats, mainbot.MEAT_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @upgrade.command(name = 'waste')
    async def upgrade_waste(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.waste_lvl = mainbot.openfile(mainbot.WASTE_LVL_FILE)
        mainbot.cities = mainbot.openfile(mainbot.CITIES_FILE)
        mainbot.citypop = mainbot.openfile(mainbot.CITYPOP_FILE)
        mainbot.salads = mainbot.openfile(mainbot.SALADS_FILE)
        mainbot.meats = mainbot.openfile(mainbot.MEAT_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.waste_lvl[user] = mainbot.waste_lvl[user] if user in mainbot.waste_lvl else 0
        mainbot.cities[user] = mainbot.cities[user] if user in mainbot.cities else 0
        mainbot.citypop[user] = mainbot.citypop[user] if user in mainbot.citypop else 0
        mainbot.salads[user] = mainbot.salads[user] if user in mainbot.salads else 0
        mainbot.meats[user] = mainbot.meats[user] if user in mainbot.meats else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0
        
        WASTE_LEVEL_USER_UPGRADING_TO = mainbot.waste_lvl[user] + 1
        MEAT_COST = WASTE_LEVEL_USER_UPGRADING_TO * 320
        COINS_COST = WASTE_LEVEL_USER_UPGRADING_TO * 15600
        SALADS_COST = WASTE_LEVEL_USER_UPGRADING_TO * 22  

        if mainbot.cities[user] == 1:
            if mainbot.waste_lvl[user] < 5:
                await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{MEAT_COST}__ **meat**, __{COINS_COST}__ **coins, and** __{SALADS_COST}__ **salads**\n`y` or `n`')
                msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)
                if msg.content.lower() == 'y':
                    if mainbot.salads[user] >= SALADS_COST:
                        if mainbot.balances[user] >= COINS_COST:
                            if mainbot.meats[user] >= MEAT_COST:
                                mainbot.waste_lvl[user] = WASTE_LEVEL_USER_UPGRADING_TO
                                mainbot.balances[user] -= COINS_COST
                                mainbot.salads[user] -= SALADS_COST
                                mainbot.meats[user] -= MEAT_COST
                                mainbot.citypop[user] += 3142
                                await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Waste**__ level is now **{WASTE_LEVEL_USER_UPGRADING_TO}**\nGo check with the `city` command!')
                                await asyncio.sleep(1)
                                await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Population**__ is now **{mainbot.citypop[user]:,d}**\nGo check with the `city` command!')
                            else:
                                await ctx.send('you don\'t have enough meat for this!')
                        else:
                            await ctx.send('you don\'t have enough coins for this!')
                    else:
                        await ctx.send('you don\'t have enough salads for this!')
                elif msg.content.lower() == 'n':
                    await ctx.send('ok')
                else:
                    await ctx.send('not an option')
            else:
                await ctx.send('you have reached the maximum level for waste!')
        else:
            await ctx.send('you don\'t have a city')

        mainbot.savefile(mainbot.police_lvl, mainbot.POLICE_LVL_FILE)
        mainbot.savefile(mainbot.citypop, mainbot.CITYPOP_FILE)
        mainbot.savefile(mainbot.salads, mainbot.SALADS_FILE)
        mainbot.savefile(mainbot.meats, mainbot.MEAT_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @upgrade.command(name = 'fire')
    async def upgrade_fire(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.fire_lvl = mainbot.openfile(mainbot.FIRE_LVL_FILE)
        mainbot.cities = mainbot.openfile(mainbot.CITIES_FILE)
        mainbot.citypop = mainbot.openfile(mainbot.CITYPOP_FILE)
        mainbot.salads = mainbot.openfile(mainbot.SALADS_FILE)
        mainbot.wheats = mainbot.openfile(mainbot.WHEAT_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.fire_lvl[user] = mainbot.fire_lvl[user] if user in mainbot.fire_lvl else 0
        mainbot.cities[user] = mainbot.cities[user] if user in mainbot.cities else 0
        mainbot.citypop[user] = mainbot.citypop[user] if user in mainbot.citypop else 0
        mainbot.salads[user] = mainbot.salads[user] if user in mainbot.salads else 0
        mainbot.wheats[user] = mainbot.wheats[user] if user in mainbot.wheats else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0

        FIRE_LEVEL_USER_UPGRADING_TO = mainbot.fire_lvl[user] + 1
        WHEAT_COST = FIRE_LEVEL_USER_UPGRADING_TO * 949
        COINS_COST = FIRE_LEVEL_USER_UPGRADING_TO * 26200
        SALADS_COST = FIRE_LEVEL_USER_UPGRADING_TO * 60

        if mainbot.cities[user] == 1:
            if mainbot.fire_lvl[user] < 4:
                await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{WHEAT_COST}__ **wheat**, __{COINS_COST}__ **coins, and** __{SALADS_COST}__ **salads**\n`y` or `n`')
                msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)
                if msg.content.lower() == 'y':
                    if mainbot.salads[user] >= SALADS_COST:
                        if mainbot.balances[user] >= COINS_COST:
                            if mainbot.wheats[user] >= WHEAT_COST:
                                mainbot.fire_lvl[user] = FIRE_LEVEL_USER_UPGRADING_TO
                                mainbot.balances[user] -= COINS_COST
                                mainbot.salads[user] -= SALADS_COST
                                mainbot.wheats[user] -= WHEAT_COST
                                mainbot.citypop[user] += 6231
                                await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Fire**__ level is now **{FIRE_LEVEL_USER_UPGRADING_TO}**\nGo check with the `city` command!')
                                await asyncio.sleep(1)
                                await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Population**__ is now **{mainbot.citypop[user]:,d}**\nGo check with the `city` command!')
                            else:
                                await ctx.send('you don\'t have enough wheat for this!')
                        else:
                            await ctx.send('you don\'t have enough coins for this!')
                    else:
                        await ctx.send('you don\'t have enough salads for this!')
                elif msg.content.lower() == 'n':
                    await ctx.send('ok')
                else:
                    await ctx.send('not an option')
            else:
                await ctx.send('you have reached the maximum level for fire!')
        else:
            await ctx.send('you don\'t have a city ')

        mainbot.savefile(mainbot.fire_lvl, mainbot.FIRE_LVL_FILE)
        mainbot.savefile(mainbot.citypop, mainbot.CITYPOP_FILE)
        mainbot.savefile(mainbot.salads, mainbot.SALADS_FILE)
        mainbot.savefile(mainbot.wheats, mainbot.WHEAT_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @upgrade.command(name = 'water')
    async def upgrade_water(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.water_lvl = mainbot.openfile(mainbot.WATER_LVL_FILE)
        mainbot.cities = mainbot.openfile(mainbot.CITIES_FILE)
        mainbot.citypop = mainbot.openfile(mainbot.CITYPOP_FILE)
        mainbot.salads = mainbot.openfile(mainbot.SALADS_FILE)
        mainbot.wheats = mainbot.openfile(mainbot.WHEAT_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.water_lvl[user] = mainbot.water_lvl[user] if user in mainbot.water_lvl else 0
        mainbot.cities[user] = mainbot.cities[user] if user in mainbot.cities else 0
        mainbot.citypop[user] = mainbot.citypop[user] if user in mainbot.citypop else 0
        mainbot.salads[user] = mainbot.salads[user] if user in mainbot.salads else 0
        mainbot.wheats[user] = mainbot.wheats[user] if user in mainbot.wheats else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0

        WATER_LEVEL_USER_UPGRADING_TO = mainbot.water_lvl[user] + 1
        WHEAT_COST = WATER_LEVEL_USER_UPGRADING_TO * 260
        COINS_COST = WATER_LEVEL_USER_UPGRADING_TO * 11200
        SALADS_COST = WATER_LEVEL_USER_UPGRADING_TO * 12

        if mainbot.cities[user] == 1:
            if mainbot.water_lvl[user] < 8:
                await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{WHEAT_COST}__ **wheat**, __{COINS_COST}__ **coins, and** __{SALADS_COST}__ **salads**\n`y` or `n`')
                msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)
                if msg.content.lower() == 'y':
                    if mainbot.salads[user] >= SALADS_COST:
                        if mainbot.balances[user] >= COINS_COST:
                            if mainbot.wheats[user] >= WHEAT_COST:
                                mainbot.water_lvl[user] = WATER_LEVEL_USER_UPGRADING_TO
                                mainbot.balances[user] -= COINS_COST
                                mainbot.salads[user] -= SALADS_COST
                                mainbot.wheats[user] -= WHEAT_COST
                                mainbot.citypop[user] += 2227
                                await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Water**__ level is now **{WATER_LEVEL_USER_UPGRADING_TO}**\nGo check with the `city` command!')
                                await asyncio.sleep(1)
                                await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Population**__ is now **{mainbot.citypop[user]:,d}**\nGo check with the `city` command!')
                            else:
                                await ctx.send('you don\'t have enough wheat for this!')
                        else:
                            await ctx.send('you don\'t have enough coins for this!')
                    else:
                        await ctx.send('you don\'t have enough salads for this!')
                elif msg.content.lower() == 'n':
                    await ctx.send('ok')
                else:
                    await ctx.send('not an option')
            else:
                await ctx.send('you have reached the maximum level for water!')
        else:
            await ctx.send('you don\'t have a city ')

        mainbot.savefile(mainbot.water_lvl, mainbot.WATER_LVL_FILE)
        mainbot.savefile(mainbot.citypop, mainbot.CITYPOP_FILE)
        mainbot.savefile(mainbot.salads, mainbot.SALADS_FILE)
        mainbot.savefile(mainbot.wheats, mainbot.WHEAT_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @upgrade.command(name = 'power')
    async def upgrade_power(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.power_lvl = mainbot.openfile(mainbot.POWER_LVL_FILE)
        mainbot.cities = mainbot.openfile(mainbot.CITIES_FILE)
        mainbot.citypop = mainbot.openfile(mainbot.CITYPOP_FILE)
        mainbot.salads = mainbot.openfile(mainbot.SALADS_FILE)
        mainbot.meats = mainbot.openfile(mainbot.MEAT_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.power_lvl[user] = mainbot.power_lvl[user] if user in mainbot.power_lvl else 0
        mainbot.cities[user] = mainbot.cities[user] if user in mainbot.cities else 0
        mainbot.citypop[user] = mainbot.citypop[user] if user in mainbot.citypop else 0
        mainbot.salads[user] = mainbot.salads[user] if user in mainbot.salads else 0
        mainbot.meats[user] = mainbot.meats[user] if user in mainbot.meats else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0
        
        LEVEL_USER_IS_UPGRADING_TO = mainbot.power_lvl[user] + 1
        COST_FOR_MEAT = LEVEL_USER_IS_UPGRADING_TO * 150
        COST_FOR_BALANCES = LEVEL_USER_IS_UPGRADING_TO * 10400
        COST_FOR_SALADS = LEVEL_USER_IS_UPGRADING_TO * 20
        
        if mainbot.cities[user] == 1:
            if mainbot.power_lvl[user] < 5:
                await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{COST_FOR_MEAT}__ **meat,** __{COST_FOR_BALANCES}__ **coins, and** __{COST_FOR_SALADS}__ **salads**\n`y` or `n`')
                msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)
                if msg.content.lower() == 'y':
                    if mainbot.salads[user] >= COST_FOR_SALADS:
                        if mainbot.balances[user] >= COST_FOR_BALANCES:
                            if mainbot.meats[user] >= COST_FOR_MEAT:
                                mainbot.power_lvl[user] = LEVEL_USER_IS_UPGRADING_TO
                                mainbot.balances[user] -= COST_FOR_BALANCES
                                mainbot.meats[user] -= COST_FOR_MEAT
                                mainbot.salads[user] -= COST_FOR_SALADS
                                mainbot.citypop[user] += 2467
                                await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Power**__ level is now **{LEVEL_USER_IS_UPGRADING_TO}**\nGo check with the `city` command!')
                                await asyncio.sleep(1)
                                await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Population**__ is now **{mainbot.citypop[user]:,d}**\nGo check with the `city` command!')
                            else:
                                await ctx.send('you don\'t have enough meat for this!')
                        else:
                            await ctx.send('you don\'t have enough coins for this!')
                    else:
                        await ctx.send('you don\'t have enough salads for this!')
                elif msg.content.lower() == 'n':
                    await ctx.send('ok')
                else:
                    await ctx.send('not an option')
            else:
                await ctx.send('you have reached the maximum level for power!')
        else:
            await ctx.send('you don\'t have a city')

        mainbot.savefile(mainbot.power_lvl, mainbot.POWER_LVL_FILE)
        mainbot.savefile(mainbot.citypop, mainbot.CITYPOP_FILE)
        mainbot.savefile(mainbot.salads, mainbot.SALADS_FILE)
        mainbot.savefile(mainbot.meats, mainbot.MEAT_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @upgrade.command(name = 'entertainment')
    async def upgrade_entertainment(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.entertainment_lvl = mainbot.openfile(mainbot.ENTERTAINMENT_LVL_FILE)
        mainbot.cities = mainbot.openfile(mainbot.CITIES_FILE)
        mainbot.citypop = mainbot.openfile(mainbot.CITYPOP_FILE)
        mainbot.salads = mainbot.openfile(mainbot.SALADS_FILE)
        mainbot.meats = mainbot.openfile(mainbot.MEAT_FILE)
        mainbot.rices = mainbot.openfile(mainbot.RICE_FILE)
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        mainbot.entertainment_lvl[user] = mainbot.entertainment_lvl[user] if user in mainbot.entertainment_lvl else 0
        mainbot.cities[user] = mainbot.cities[user] if user in mainbot.cities else 0
        mainbot.citypop[user] = mainbot.citypop[user] if user in mainbot.citypop else 0
        mainbot.salads[user] = mainbot.salads[user] if user in mainbot.salads else 0
        mainbot.rices[user] = mainbot.rices[user] if user in mainbot.rices else 0
        mainbot.meats[user] = mainbot.meats[user] if user in mainbot.meats else 0
        mainbot.balances[user] = mainbot.balances[user] if user in mainbot.balances else 0
        
        LEVEL_USER_IS_UPGRADING_TO = mainbot.entertainment_lvl[user] + 1
        COST_FOR_LUIUT_MEAT = LEVEL_USER_IS_UPGRADING_TO * 100
        COST_FOR_LUIUT_COINS = LEVEL_USER_IS_UPGRADING_TO * 12000
        COST_FOR_LUIUT_RICE = LEVEL_USER_IS_UPGRADING_TO * 10
        COST_FOR_LUIUT_SALADS = LEVEL_USER_IS_UPGRADING_TO * 2

        if mainbot.cities[user] == 1:
            if mainbot.entertainment_lvl[user] < 7:
                await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{COST_FOR_LUIUT_MEAT}__ **meat,** __{COST_FOR_LUIUT_COINS}__ **coins,** __{COST_FOR_LUIUT_RICE}__ **rice, and** __{COST_FOR_LUIUT_SALADS}__ **salads**\n`y` or `n`')
                msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)
                if msg.content.lower() == 'y':
                    if mainbot.salads[user] >= COST_FOR_LUIUT_SALADS:
                        if mainbot.balances[user] >= COST_FOR_LUIUT_COINS:
                            if mainbot.meats[user] >= COST_FOR_LUIUT_MEAT:
                                if mainbot.rices[user] >= COST_FOR_LUIUT_RICE:
                                    mainbot.entertainment_lvl[user] = LEVEL_USER_IS_UPGRADING_TO
                                    mainbot.balances[user] -= COST_FOR_LUIUT_COINS
                                    mainbot.meats[user] -= COST_FOR_LUIUT_MEAT
                                    mainbot.rices[user] -= COST_FOR_LUIUT_RICE
                                    mainbot.salads[user] -= COST_FOR_LUIUT_SALADS
                                    mainbot.citypop[user] += 867
                                    await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Entertainment**__ level is now **{LEVEL_USER_IS_UPGRADING_TO}**\nGo check with the `city` command!')
                                    await asyncio.sleep(1)
                                    await ctx.send(f'Congratulations {ctx.message.author.mention}! your __**Population**__ is now **{mainbot.citypop[user]:,d}**\nGo check with the `city` command!')
                                else:
                                    await ctx.send('you don\'t have enough rice for this!')
                            else:
                                await ctx.send('you don\'t have enough meat for this!')
                        else:
                            await ctx.send('you don\'t have enough coins for this!')
                    else:
                        await ctx.send('you don\'t have enough salads for this!')
                elif msg.content.lower() == 'n':
                    await ctx.send('ok')
                else:
                    await ctx.send('not an option')
            else:
                await ctx.send('you have reached the maximum level for entertainment!')
        else:
            await ctx.send('you don\'t have a city')

        mainbot.savefile(mainbot.entertainment_lvl, mainbot.ENTERTAINMENT_LVL_FILE)
        mainbot.savefile(mainbot.citypop, mainbot.CITYPOP_FILE)
        mainbot.savefile(mainbot.salads, mainbot.SALADS_FILE)
        mainbot.savefile(mainbot.meats, mainbot.MEAT_FILE)
        mainbot.savefile(mainbot.rices, mainbot.RICE_FILE)
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

async def setup(bot):
    await bot.add_cog(upgrade(bot))
