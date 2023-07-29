from discord.ext import commands
import sys
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class rob(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def rob(self, ctx, member: discord.Member = None):
        mainbot.balances = mainbot.openfile(mainbot.BALANCES_FILE)

        user = str(ctx.message.author.id)

        if member is None:
            await ctx.send('you need to rob someone')
            self.rob.reset_cooldown(ctx)
        elif str(member.id) == user:
            await ctx.send("?")
            self.rob.reset_cooldown(ctx)
        else:
            if user in mainbot.balances:
                if mainbot.balances[user] >= 5000:
                    if str(member.id) in mainbot.balances:
                        await ctx.send(f"you have a 25% chance of successfully robbing 15-30% of **{member.name}'s** account. you fail you pay 5000\ntype `y` to continue and `n` to not")
                        msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)
                        if msg.content.lower() == 'y':
                            CHANCE_OF_ROB = random.randint(1, 100)
                            AMOUNT_ROBBED_PERCENTAGE = random.randint(15, 30) 
                            if CHANCE_OF_ROB <= 25:
                                amount_robbed = round((AMOUNT_ROBBED_PERCENTAGE/100) * mainbot.balances[str(member.id)])
                                mainbot.balances[str(member.id)] -= amount_robbed
                                mainbot.balances[user] += amount_robbed
                                await ctx.send(f'nice {ctx.message.author.mention}, you robbed **{AMOUNT_ROBBED_PERCENTAGE}%** of **{member.name}\'s** bank account (${amount_robbed:,d})')
                            else:
                                mainbot.balances[user] -= 5000
                                await ctx.send('the robbery failed and you lost **$5000**')
                        elif msg.content.lower() == 'n':
                            await ctx.send('ok')
                            self.rob.reset_cooldown(ctx)
                        else:
                            await ctx.send('not an option')
                            self.rob.reset_cooldown(ctx)
                    else:
                        await ctx.send('mentioned user doesn\'t have a bank account')
                        self.rob.reset_cooldown(ctx)
                else:
                    await ctx.send('you need 5000 to rob someone')
                    self.rob.reset_cooldown(ctx)
            else:
                await ctx.send('you don\'t have a bank acc. use the `plead` command to get one')
                self.rob.reset_cooldown(ctx)
            
        mainbot.savefile(mainbot.balances, mainbot.BALANCES_FILE)

    @rob.error
    async def rob_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to rob again')
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send('user isn\'t in the server')
            self.rob.reset_cooldown(ctx)

async def setup(bot):
    await bot.add_cog(rob(bot)) 
