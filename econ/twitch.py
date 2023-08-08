from discord.ext import commands
import sys
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def twitch(self, ctx):
        user = str(ctx.message.author.id)

        mainbot.pc = mainbot.openfile(mainbot.PC_FILE)

        mainbot.pc[user] = mainbot.pc[user] if user in mainbot.pc else 0
        CHANCE = random.randint(1, 100)
        random_coins = random.randint(500, 1000)

        if mainbot.pc[user] > 0:
            await ctx.send('what do you want to stream today?\n`fortnite`, `minecraft`, `pubg`, or `valorant`')
            msg = await self.bot.wait_for('message', check = lambda m: m.author == ctx.author)
            
            if msg.content.lower() == 'fortnite':
                if CHANCE <= 75:
                    await ctx.send(f'you streamed fortnite and turns out people actually liked it\nyou earned **{random_coins}** coins')
                    mainbot.balances[user] += random_coins
                elif CHANCE > 75 and CHANCE < 80:
                    mainbot.pc[user] -= 1
                    await ctx.send(f'your stream was so ass your pc fucking exploded\nyou now have {mainbot.pc[user]} pc(s) left')
                else:
                    await ctx.send('nobody watched your stream giving you **0** coins lol')

            elif msg.content.lower() == 'minecraft':
                if CHANCE <= 75:
                    await ctx.send(f'you streamed mc and turns out people actually liked it\nyou earned **{random_coins}** coins')
                    mainbot.balances[user] += random_coins
                elif CHANCE > 75 and CHANCE < 80:
                    mainbot.pc[user] -= 1
                    await ctx.send(f'your stream was so ass your pc fucking exploded\nyou now have {mainbot.pc[user]} pc(s) left')
                else:
                    await ctx.send('nobody watched your stream giving you **0** coins lol')

            elif msg.content.lower() == 'pubg':
                if CHANCE <= 75:
                    await ctx.send(f'you streamed pubg and turns out people actually liked it\nyou earned **{random_coins}** coins')
                    mainbot.balances[user] += random_coins
                elif CHANCE > 75 and CHANCE < 80:
                    mainbot.pc[user] -= 1
                    await ctx.send(f'your stream was so ass your pc fucking exploded\nyou now have {mainbot.pc[user]} pc(s) left')
                else:
                    await ctx.send('nobody watched your stream giving you **0** coins lol')

            elif msg.content.lower() == 'valorant':
                if CHANCE <= 75:
                    await ctx.send(f'you streamed valorant and turns out people actually liked it\nyou earned **{random_coins}** coins')
                    mainbot.balances[user] += random_coins
                elif CHANCE > 75 and CHANCE < 80:
                    mainbot.pc[user] -= 1
                    await ctx.send(f'your stream was so ass your pc fucking exploded\nyou now have {mainbot.pc[user]} pc(s) left')
                else:
                    await ctx.send('nobody watched your stream giving you **0** coins lol')

            else:
                await ctx.send('not an option')
                self.twitch.reset_cooldown(ctx)
        else:
            await ctx.send('you don\'t have a pc')
            self.twitch.reset_cooldown(ctx)

    @twitch.error
    async def twitch_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to stream again ')
            return

async def setup(bot):
    await bot.add_cog(twitch(bot)) 
