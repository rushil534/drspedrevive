from discord.ext import commands
import sys
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

# 0 IS CALIFORNIA
# 1 IS TEXAS

class fly(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def fly(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send('Proper Usage: `fly [morris/douglas]`')
        elif ctx.invoked_subcommand is None:
            await ctx.send(f"that plane doesn't exist buddy")

    @fly.command(name = 'morris')
    async def fly_morris_subcommand(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.locations = mainbot.openfile(mainbot.LOCATIONS_FILE)
        mainbot.morris = mainbot.openfile(mainbot.MORRIS_FILE)
        mainbot.healths = mainbot.openfile(mainbot.HEALTH_FILE)

        mainbot.locations[user] = mainbot.locations[user] if user in mainbot.locations else 0
        mainbot.morris[user] = mainbot.morris[user] if user in mainbot.morris else 0
        mainbot.healths[user] = mainbot.healths[user] if user in mainbot.healths else 0

        if mainbot.morris[user] >= 1:
            await ctx.send('you have a 25% chance of getting air sick, causing you to lose about 5-9 health.\nStill want to fly on this plane? `y` or `n`')
            msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)
            
            if msg.content.lower() == 'y':

                if mainbot.healths[user] < 9:
                    await ctx.send('you do not have enough health to risk for this flight')
                    return
                
                await ctx.send('Where do you want to travel? `Texas` or `California`?')
                msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)

                if msg.content.lower() == 'california':

                    if mainbot.locations[user] == 0:
                        await ctx.send('you are already in california')
                        return
                    
                    CHANCE_OF_GETTING_AIR_SICK = random.randint(1, 100)
                    HEALTH_LOSS = random.randint(5, 9)
                    await ctx.send('travelling back to California!')

                    if CHANCE_OF_GETTING_AIR_SICK <= 25:
                        mainbot.healths[user] -= HEALTH_LOSS
                        await ctx.send(f'you got air sick, causing you to lose {HEALTH_LOSS} health')
                        mainbot.locations[user] = 0
                        await ctx.send(f'you are in California now. commands you can run are `farm`')
                    else:
                        mainbot.locations[user] = 0
                        await ctx.send(f'luckily, you didn\'t get airsick\nyou are in California now. commands you can run are `farm`')

                elif msg.content.lower() == 'texas':

                    if mainbot.locations[user] == 1:
                        await ctx.send('you are already in Texas')
                        return
                    
                    CHANCE_OF_GETTING_AIR_SICK = random.randint(1, 100)
                    HEALTH_LOSS = random.randint(5, 9)
                    await ctx.send('Travelling to Texas!')
                    
                    if CHANCE_OF_GETTING_AIR_SICK > 25:
                        await ctx.send(f'you got air sick, causing you to lose {HEALTH_LOSS} health')
                        mainbot.healths[user] -= HEALTH_LOSS
                        mainbot.locations[user] = 1
                        await ctx.send(f'you are in Texas now. commands you can run are `city`')
                    else:
                        mainbot.locations[user] = 1
                        await ctx.send(f'luckily you didn\'t get airsick\nyou are in Texas now. commands you can run are `city`')
                
                else:
                    await ctx.send('not an option; rerun the command')

            elif msg.content.lower() == 'n':
                await ctx.send('flight cancelled')

        else:
            await ctx.send('you don\'t have the Morris jet!')

        mainbot.savefile(mainbot.locations, mainbot.LOCATIONS_FILE)
        mainbot.savefile(mainbot.morris, mainbot.MORRIS_FILE)
        mainbot.savefile(mainbot.healths, mainbot.HEALTH_FILE)


    @fly.command(name = 'douglas')
    async def fly_douglas_subcommand(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.locations = mainbot.openfile(mainbot.LOCATIONS_FILE)
        mainbot.douglas = mainbot.openfile(mainbot.DOUGLAS_FILE)

        mainbot.locations[user] = mainbot.locations[user] if user in mainbot.locations else 0
        mainbot.douglas[user] = mainbot.douglas[user] if user in mainbot.douglas else 0

        if mainbot.douglas[user] >= 1:
            await ctx.send('Where do you want to travel? `Texas` or `California`?')
            msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)

            if msg.content.lower() == 'california':

                if mainbot.locations[user] == 0:
                    await ctx.send('you are already in California')
                    return
                
                await ctx.send('Travelling back to california!')
                mainbot.locations[user] = 0
                await ctx.send(f'you are in California now. commands you can run are `farm`')
                
            elif msg.content.lower() == 'texas':

                if mainbot.locations[user] == 1:
                    await ctx.send('you are already in Texas')
                    return
                
                await ctx.send('Travelling to Texas!')
                mainbot.locations[user] = 1
                await ctx.send(f'you are in Texas now. commands you can run are `city`')

            else:
                await ctx.send('not an option; rerun the command')

        else:
            await ctx.send('you don\'t have the Douglas jet!')

        mainbot.savefile(mainbot.locations, mainbot.LOCATIONS_FILE)

async def setup(bot):
    await bot.add_cog(fly(bot)) 
