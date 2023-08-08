import discord
from discord.ext import commands
import sys
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class grab(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def grab(self, ctx):
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        AIRDROP_LOOT = random.randint(500,1200)
        user = str(ctx.message.author.id)

        if user in mainbot.balances:
            embed = discord.Embed(description = f'{ctx.message.author} just grabbed an airdrop for ¢{AIRDROP_LOOT}', color = random.choice(mainbot.random_colors))
            mainbot.balances[user] += AIRDROP_LOOT
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'{mainbot.NO_BANK_ACC}')
            self.grab.reset_cooldown(ctx)
            
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @grab.error
    async def grab_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to grab another airdrop')
            return

async def setup(bot):
    await bot.add_cog(grab(bot)) 
