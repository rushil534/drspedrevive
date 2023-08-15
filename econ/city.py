from discord.ext import commands
import sys
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class city(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def city(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.cities = mainbot.openfile(mainbot.CITIES_FILE)
        mainbot.locations = mainbot.openfile(mainbot.LOCATIONS_FILE)
        mainbot.citypop = mainbot.openfile(mainbot.CITYPOP_FILE)
        mainbot.entertainment_lvl = mainbot.openfile(mainbot.ENTERTAINMENT_LVL_FILE)
        mainbot.park_lvl = mainbot.openfile(mainbot.PARK_LVL_FILE)
        mainbot.power_lvl = mainbot.openfile(mainbot.POWER_LVL_FILE)
        mainbot.water_lvl = mainbot.openfile(mainbot.WATER_LVL_FILE)
        mainbot.waste_lvl = mainbot.openfile(mainbot.WASTE_LVL_FILE)
        mainbot.health_lvl = mainbot.openfile(mainbot.HEALTH_LVL_FILE)
        mainbot.fire_lvl = mainbot.openfile(mainbot.FIRE_LVL_FILE)
        mainbot.police_lvl = mainbot.openfile(mainbot.POLICE_LVL_FILE)

        mainbot.cities[user] = mainbot.cities[user] if user in mainbot.cities else 0
        mainbot.locations[user] = mainbot.locations[user] if user in mainbot.locations else 0
        mainbot.citypop[user] = mainbot.citypop[user] if user in mainbot.citypop else 0
        mainbot.entertainment_lvl[user] = mainbot.entertainment_lvl[user] if user in mainbot.entertainment_lvl else 0
        mainbot.park_lvl[user] = mainbot.park_lvl[user] if user in mainbot.park_lvl else 0
        mainbot.power_lvl[user] = mainbot.power_lvl[user] if user in mainbot.power_lvl else 0
        mainbot.water_lvl[user] = mainbot.water_lvl[user] if user in mainbot.water_lvl else 0
        mainbot.waste_lvl[user] = mainbot.waste_lvl[user] if user in mainbot.waste_lvl else 0
        mainbot.health_lvl[user] = mainbot.health_lvl[user] if user in mainbot.health_lvl else 0
        mainbot.fire_lvl[user] = mainbot.fire_lvl[user] if user in mainbot.fire_lvl else 0 
        mainbot.police_lvl[user] = mainbot.police_lvl[user] if user in mainbot.police_lvl else 0

        epa = mainbot.entertainment_lvl[user] * 867
        pkpa = mainbot.park_lvl[user] * 1001
        pwrpa = mainbot.power_lvl[user] * 2467
        wtpa = mainbot.water_lvl[user] * 2227
        wpa = mainbot.waste_lvl[user] * 3142
        hpa = mainbot.health_lvl[user] * 7819
        fpa = mainbot.fire_lvl[user] * 6231
        ppa = mainbot.police_lvl[user] * 9331

        pop = epa + pkpa + pwrpa + wtpa + wpa + hpa + fpa + ppa
        #medium then advanced then normal

        if mainbot.locations[user] == 1:
            if mainbot.cities[user] == 1:
                if mainbot.power_lvl[user] == 4 and mainbot.water_lvl[user] in [5, 6, 7] and mainbot.waste_lvl[user] in [3, 4] and mainbot.health_lvl[user] in [2, 3] and mainbot.park_lvl[user] == 5 and mainbot.entertainment_lvl[user] in [3, 4, 5, 6] and mainbot.fire_lvl[user] in [2, 3] and mainbot.police_lvl[user] in [2, 3]:
                    embed = discord.Embed(title = f':city_dusk: {ctx.message.author.name}\'s Medium city', description = '`le requirements [medium/advanced city]`\n`le upgrade [Section]`\n`le collect [section]`', color = random.choice(mainbot.random_colors))
                    embed.add_field(name = '__**Overview**__', value = f':man: **Population**: __**{pop:,d}**__', inline = False)
                    embed.add_field(name = '__**Basic City Needs**__', value = f':cloud_lightning: **Power**: Lvl: {mainbot.power_lvl[user]:,d}\n\tPopulation Added: **{pwrpa:,d}**\n:cup_with_straw: **Water**: Lvl: {mainbot.water_lvl[user]:,d}\n\tPopulation Added: **{wtpa:,d}**\n:wastebasket: **Waste**: Lvl: {mainbot.waste_lvl[user]:,d}\n\tPopulation Added: **{wpa:,d}**', inline = True)
                    embed.add_field(name = '__**Urgent Needs**__', value = f':fire_engine: **Fire Station**: Lvl : {mainbot.fire_lvl[user]:,d}\n\tPopulation Added: **{fpa:,d}**\n:police_car: **Police Station**: Lvl: {mainbot.police_lvl[user]:,d}\n\tPopulation Added: **{ppa:,d}**\n:ambulance: **Health**: Lvl: {mainbot.health_lvl[user]:,d}\n\tPopulation Added: **{hpa:,d}**', inline = False)
                    embed.add_field(name = '__**Population Boosters**__', value = f':musical_note: **Entertainment**: Lvl: {mainbot.entertainment_lvl[user]:,d}\n\tPopulation Added: **{epa:,d}**\n:island: **Parks**: Lvl: {mainbot.park_lvl[user]:,d}\n\tPopulation Added: **{pkpa:,d}**', inline = False)
                    await ctx.send(embed = embed)
                elif mainbot.power_lvl[user] == 5 and mainbot.water_lvl[user] == 8 and mainbot.waste_lvl[user] == 5 and mainbot.health_lvl[user] == 4 and mainbot.entertainment_lvl[user] == 7 and mainbot.park_lvl[user] == 6 and mainbot.fire_lvl[user] == 4 and mainbot.police_lvl[user] == 4:
                    embed = discord.Embed(title = f':city_dusk: {ctx.message.author.name}\'s Advanced city', description = '`le requirements [medium/advanced city]`\n`le upgrade [Section]`\n`le collect [section]`', color = random.choice(mainbot.random_colors))
                    embed.add_field(name = '__**Overview**__', value = f':man: **Population**: __**{pop:,d}**__', inline = False)
                    embed.add_field(name = '__**Basic City Needs**__', value = f':cloud_lightning: **Power**: Lvl: {mainbot.power_lvl[user]:,d}\n\tPopulation Added: **{pwrpa:,d}**\n:cup_with_straw: **Water**: Lvl: {mainbot.water_lvl[user]:,d}\n\tPopulation Added: **{wtpa:,d}**\n:wastebasket: **Waste**: Lvl: {mainbot.waste_lvl[user]:,d}\n\tPopulation Added: **{wpa:,d}**', inline = True)
                    embed.add_field(name = '__**Urgent Needs**__', value = f':fire_engine: **Fire Station**: Lvl : {mainbot.fire_lvl[user]:,d}\n\tPopulation Added: **{fpa:,d}**\n:police_car: **Police Station**: Lvl: {mainbot.police_lvl[user]:,d}\n\tPopulation Added: **{ppa:,d}**\n:ambulance: **Health**: Lvl: {mainbot.health_lvl[user]:,d}\n\tPopulation Added: **{hpa:,d}**', inline = False)
                    embed.add_field(name = '__**Population Boosters**__', value = f':musical_note: **Entertainment**: Lvl: {mainbot.entertainment_lvl[user]:,d}\n\tPopulation Added: **{epa:,d}**\n:island: **Parks**: Lvl: {mainbot.park_lvl[user]:,d}\n\tPopulation Added: **{pkpa:,d}**', inline = False)
                    await ctx.send(embed = embed)
                else:
                    embed = discord.Embed(title = f':city_dusk: {ctx.message.author.name}\'s city', description = '`le requirements [medium/advanced city]`\n`le upgrade [Section]`\n`le collect [section]`', color = random.choice(mainbot.random_colors))
                    embed.add_field(name = '__**Overview**__', value = f':man: **Population**: __**{pop:,d}**__', inline = False)
                    embed.add_field(name = '__**Basic City Needs**__', value = f':cloud_lightning: **Power**: Lvl: {mainbot.power_lvl[user]:,d}\n\tPopulation Added: **{pwrpa:,d}**\n:cup_with_straw: **Water**: Lvl: {mainbot.water_lvl[user]:,d}\n\tPopulation Added: **{wtpa:,d}**\n:wastebasket: **Waste**: Lvl: {mainbot.waste_lvl[user]:,d}\n\tPopulation Added: **{wpa:,d}**', inline = True)
                    embed.add_field(name = '__**Urgent Needs**__', value = f':fire_engine: **Fire Station**: Lvl : {mainbot.fire_lvl[user]:,d}\n\tPopulation Added: **{fpa:,d}**\n:police_car: **Police Station**: Lvl: {mainbot.police_lvl[user]:,d}\n\tPopulation Added: **{ppa:,d}**\n:ambulance: **Health**: Lvl: {mainbot.health_lvl[user]:,d}\n\tPopulation Added: **{hpa:,d}**', inline = False)
                    embed.add_field(name = '__**Population Boosters**__', value = f':musical_note: **Entertainment**: Lvl: {mainbot.entertainment_lvl[user]:,d}\n\tPopulation Added: **{epa:,d}**\n:island: **Parks**: Lvl: {mainbot.park_lvl[user]:,d}\n\tPopulation Added: **{pkpa:,d}**', inline = False)
                    await ctx.send(embed = embed)
            else:
                await ctx.send('you don\'t have a city! To get one, use the `create` command')
        else:
            await ctx.send('you must be in Texas in order to view/create your city')


async def setup(bot):
    await bot.add_cog(city(bot)) 
