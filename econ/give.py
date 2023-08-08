from discord.ext import commands
import sys 
import discord

sys.path.append('C:/Users/mantr/Desktop/ds-master')

import bot as mainbot

class give(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def give(self, ctx, member: discord.Member, amount: int = None):
        primary_id = str(ctx.message.author.id)
        other_id = str(member.id)

        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)
        
        mainbot.balances[primary_id] = mainbot.balances[primary_id] if primary_id in mainbot.balances else 0
        mainbot.balances[other_id] = mainbot.balances[other_id] if other_id in mainbot.balances else 0

        if amount is None:
            await ctx.send("rerun the command with a number")
            return

        if amount <= 0:
            await ctx.send("rerun the command with a value above 0")
            return

        if primary_id not in mainbot.balances:
            await ctx.send(f"{mainbot.NO_BANK_ACC}")
            return
        
        if other_id not in mainbot.balances:
            await ctx.send("The other party does not have an account")
            return
        
        if mainbot.balances[primary_id] < amount:
            await ctx.send("you cannot afford this transaction")
            return
        if other_id == primary_id:
            await ctx.send('?')
            return
        
        mainbot.balances[primary_id] -= amount
        mainbot.balances[other_id] += amount
        await ctx.send(f"you gave {member.mention} **{amount:,d}** coins now they have **{mainbot.balances[other_id]:,d}** coins and you have **{mainbot.balances[primary_id]:,d}** coins")
        await member.send(f'{ctx.message.author.name} gave you {amount:,d} coins!')

        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @give.error
    async def give_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `give [user] [amount]`')

async def setup(bot):
    await bot.add_cog(give(bot))
