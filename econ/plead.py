from discord.ext import commands
import sys
import json
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

balances = mainbot.balances
BALANCES_FILE = mainbot.BALANCES_FILE
random_colors = mainbot.random_colors
START_BAL = mainbot.START_BAL

class plead(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def plead(self, ctx):
        try:
            with open(BALANCES_FILE, 'r') as fp: 
                balances = json.load(fp) 
        except FileNotFoundError:
            print(f'In on_ready(): File {BALANCES_FILE} not found. Starting off with an empty balances dictionary.') 
            balances = {}
    
        INCREMENT = random.randint(20, 70)
        user = str(ctx.message.author.id) 

        if user in balances: 
            names = ["**Kanye West**", "**Lindsay Lohan**", "**Azealia Banks**", "**Justin Bieber**", "**Roseanne Barr**", "**Charlie Sheen**", "**Amanda Bynes**", "**Woody Allen**", "**Mel Gibson**", "**R. Kelly**"]
            await ctx.send(random.choice(names) + f' donated {INCREMENT} coins to {ctx.message.author.mention}!')
            balances[user] += INCREMENT
        else: 
            print(f'In plead(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
            balances[user] = START_BAL 
            await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with {START_BAL} coins') 
            self.plead.reset_cooldown(ctx)

        print(f'In plead(): Saving balances = {balances}')
        try: 
            with open(BALANCES_FILE, 'w') as fp: 
                json.dump(balances, fp) 
        except FileNotFoundError: 
            print(f'In beg(): File {BALANCES_FILE} not found! Not sure what to do here!')

    @plead.error
    async def plead_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to plead again ')
            return

async def setup(bot):
    await bot.add_cog(plead(bot)) 
