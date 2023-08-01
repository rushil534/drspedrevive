from discord.ext import commands
import sys 
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')

import bot as mainbot

class farm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def farm(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.locations = mainbot.openfile(mainbot.LOCATIONS_FILE)
        mainbot.morris = mainbot.openfile(mainbot.MORRIS_FILE)
        mainbot.douglas = mainbot.openfile(mainbot.DOUGLAS_FILE)
        mainbot.salads = mainbot.openfile(mainbot.SALADS_FILE)
        mainbot.cooked_chickens = mainbot.openfile(mainbot.COOKED_CHICKENS_FILE)
        mainbot.uncooked_chickens = mainbot.openfile(mainbot.UNCOOKED_CHICKENS_FILE)
        mainbot.stoves = mainbot.openfile(mainbot.STOVES_FILE)
        mainbot.buffalos = mainbot.openfile(mainbot.BUFFALOS_FILE)
        mainbot.wools = mainbot.openfile(mainbot.WOOL_FILE)
        mainbot.rices = mainbot.openfile(mainbot.RICE_FILE)
        mainbot.wheats = mainbot.openfile(mainbot.WHEAT_FILE)
        mainbot.pigs = mainbot.openfile(mainbot.PIG_FILE)
        mainbot.meats = mainbot.openfile(mainbot.MEAT_FILE)
        mainbot.ambulances = mainbot.openfile(mainbot.AMBULANCES_FILE)
        mainbot.pc = mainbot.openfile(mainbot.PC_FILE)
        mainbot.bread = mainbot.openfile(mainbot.BREAD_FILE)
        mainbot.mooshroom_cows = mainbot.openfile(mainbot.MOOSHROOM_COW_FILE)
        mainbot.bowls = mainbot.openfile(mainbot.BOWLS_FILE)
        mainbot.mushroom_stew = mainbot.openfile(mainbot.MUSHROOM_STEW_FILE)
        mainbot.commands2 = mainbot.openfile(mainbot.COMMANDS_FILE)

        mainbot.locations[user] = mainbot.locations[user] if user in mainbot.locations else 0
        mainbot.morris[user] = mainbot.morris[user] if user in mainbot.morris else 0
        mainbot.douglas[user] = mainbot.douglas[user] if user in mainbot.douglas else 0
        mainbot.salads[user] = mainbot.salads[user] if user in mainbot.salads else 0
        mainbot.cooked_chickens[user] = mainbot.cooked_chickens[user] if user in mainbot.cooked_chickens else 0
        mainbot.uncooked_chickens[user] = mainbot.uncooked_chickens[user] if user in mainbot.uncooked_chickens else 0
        mainbot.stoves[user] = mainbot.stoves[user] if user in mainbot.stoves else 0
        mainbot.sheeps[user] = mainbot.sheeps[user] if user in mainbot.sheeps else 0
        mainbot.buffalos[user] = mainbot.buffalos[user] if user in mainbot.buffalos else 0
        mainbot.wools[user] = mainbot.wools[user] if user in mainbot.wools else 0
        mainbot.rices[user] = mainbot.rices[user] if user in mainbot.rices else 0
        mainbot.wheats[user] = mainbot.wheats[user] if user in mainbot.wheats else 0
        mainbot.pigs[user] = mainbot.pigs[user] if user in mainbot.pigs else 0
        mainbot.meats[user] = mainbot.meats[user] if user in mainbot.meats else 0
        mainbot.ambulances[user] = mainbot.ambulances[user] if user in mainbot.ambulances else 0
        mainbot.pc[user] = mainbot.pc[user] if user in mainbot.pc else 0
        mainbot.bread[user] = mainbot.bread[user] if user in mainbot.bread else 0
        mainbot.mooshroom_cows[user] = mainbot.mooshroom_cows[user] if user in mainbot.mooshroom_cows else 0
        mainbot.bowls[user] = mainbot.bowls[user] if user in mainbot.bowls else 0
        mainbot.mushroom_stew[user] = mainbot.mushroom_stew[user] if user in mainbot.mushroom_stew else 0
        mainbot.commands2[user] = mainbot.commands2[user] if user in mainbot.commands2 else 0


        if mainbot.locations[user] == 0:
            embed = discord.Embed(title = f"{ctx.message.author.name}'s California Farm", description = f"`le <crop/animal>` to harvest the animals or crops\n `le shop` for more", color = random.choice(mainbot.random_colors))
            embed.add_field(name = "Animals [NOT SELLABLE]\n", value = f":sheep: Sheep | {mainbot.sheeps[user]}\n :pig2: Pigs | {mainbot.pigs[user]}\n :water_buffalo: Buffalos | {mainbot.buffalos[user]}\n :hatched_chick: Uncooked Chickens | {mainbot.uncooked_chickens[user]}\n <:mooshroom:716492779391418440> Mooshroom Cows | {mainbot.mooshroom_cows[user]}\n", inline = True)
            embed.add_field(name = "\nCrops [NOT SELLABLE]\n", value = f":rice: Rice | {mainbot.rices[user]}\n", inline = False)
            embed.add_field(name = "\nGoods [SELLABLE]\n", value = f":scroll:  Wool | {mainbot.wools[user]}\n :tanabata_tree: Wheat | {mainbot.wheats[user]}\n :cut_of_meat: Meat | {mainbot.meats[user]}\n :chicken: Chickens | {mainbot.cooked_chickens[user]}\n", inline = False)
            embed.add_field(name = "\nMeds [NOT SELLABLE]\n", value = f":ambulance: Ambulances | {mainbot.ambulances[user]}\n:french_bread: Bread | {mainbot.bread[user]}", inline = False)
            embed.add_field(name = "\nMaterials [NOT SELLABLE]\n", value = f':cooking: Stoves | {mainbot.stoves[user]}\n :desktop: PC | {mainbot.pc[user]}', inline = False)
            embed.add_field(name = "\nDishes [NOT SELLABLE]\n", value = f':salad: Salads | {mainbot.salads[user]}\n <:mushstew:716492699879997530> Mushroom Stew | {mainbot.mushroom_stew[user]}', inline = False)
            embed.add_field(name = "\nJets [NOT SELLABLE]\n", value = f':airplane_small: Morris | {mainbot.morris[user]}\n:airplane: Douglas | {mainbot.douglas[user]}', inline = False)
            embed.add_field(name = "\nLocation [MISCELLANEOUS]", value = f':man_running: Location | California', inline = False)
            embed.add_field(name = '\nItems [MISCELLANEOUS]', value = f':bowl_with_spoon: Bowl | {mainbot.bowls[user]}', inline = False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title = f"{ctx.message.author.name}'s California Farm", description = f"`le <crop/animal>` to harvest the animals or crops\n `le shop` for more", color = random.choice(mainbot.random_colors))
            embed.add_field(name = "Animals [NOT SELLABLE]\n", value = f":sheep: Sheep | {mainbot.sheeps[user]}\n :pig2: Pigs | {mainbot.pigs[user]}\n :water_buffalo: Buffalos | {mainbot.buffalos[user]}\n :hatched_chick: Uncooked Chickens | {mainbot.uncooked_chickens[user]}\n <:mooshroom:716492779391418440> Mooshroom Cows | {mainbot.mooshroom_cows[user]}\n", inline = True)
            embed.add_field(name = "\nCrops [NOT SELLABLE]\n", value = f":rice: Rice | {mainbot.rices[user]}\n", inline = False)
            embed.add_field(name = "\nGoods [SELLABLE]\n", value = f":scroll:  Wool | {mainbot.wools[user]}\n :tanabata_tree: Wheat | {mainbot.wheats[user]}\n :cut_of_meat: Meat | {mainbot.meats[user]}\n :chicken: Chickens | {mainbot.cooked_chickens[user]}\n", inline = False)
            embed.add_field(name = "\nMeds [NOT SELLABLE]\n", value = f":ambulance: Ambulances | {mainbot.ambulances[user]}\n:french_bread: Bread | {mainbot.bread[user]}", inline = False)
            embed.add_field(name = "\nMaterials [NOT SELLABLE]\n", value = f':cooking: Stoves | {mainbot.stoves[user]}\n :desktop: PC | {mainbot.pc[user]}', inline = False)
            embed.add_field(name = "\nDishes [NOT SELLABLE]\n", value = f':salad: Salads | {mainbot.salads[user]}\n <:mushstew:716492699879997530> Mushroom Stew | {mainbot.mushroom_stew[user]}', inline = False)
            embed.add_field(name = "\nJets [NOT SELLABLE]\n", value = f':airplane_small: Morris | {mainbot.morris[user]}\n:airplane: Douglas | {mainbot.douglas[user]}', inline = False)
            embed.add_field(name = "\nLocation [MISCELLANEOUS]", value = f':man_running: Location | Texas', inline = False)
            embed.add_field(name = '\nItems [MISCELLANEOUS]', value = f':bowl_with_spoon: Bowl | {mainbot.bowls[user]}', inline = False)
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(farm(bot))
