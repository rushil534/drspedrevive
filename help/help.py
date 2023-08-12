from discord.ext import commands
import sys
import json
import discord
import random

sys.path.append('C:/Users/mantr/Desktop/ds-master')  

import bot as mainbot

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command = True)
    async def help(self, ctx):

        with open(r"prefixes.json", 'r') as f:
            prefixes = json.load(f)

        x = prefixes[str(ctx.guild.id)] if str(ctx.guild.id) in prefixes else 'le '

        embed = discord.Embed(title = "Mr. Morale Command Center", description = 'cool bot', color = random.choice(mainbot.random_colors))
        
        embed.add_field(name = ':smile: Random', value = f'`{x}help random`', inline = True)

        embed.add_field(name = ':hammer: Moderation', value = f"`{x}help moderation`", inline = False)

        embed.add_field(name = ':money_with_wings: Economy', value = f"`{x}help economy`", inline = False)

        embed.add_field(name = ':axe: Settings', value = f"`{x}help settings`", inline = False)

        embed.set_footer(text = f'use `{x}` before each command!')

        await ctx.send(embed = embed)

    @help.command(name = 'economy')
    async def economy_subcommand(self, ctx):

        with open(r"prefixes.json", 'r') as f:
            prefixes = json.load(f)
        
        x = prefixes[str(ctx.guild.id)] if str(ctx.guild.id) in prefixes else 'le '

        embed = discord.Embed(title = ":money_with_wings: Economy Commands", description = '`plead`, `bal`, `buy`, `sell`, `notebook`, `combine`, `pharmacy`, `rice`, `sheep`, `buffalo`, `pig`, `farm`, `cook`, `shop`, `popeyes`, `grab`, `use`, `health`, `jetshop`, `fly`, `get`, `city`, `upgrade`, `requirements`, `create`, `work`, `cowmarket`, `twitch`, `profile`, `give`', color = random.choice(mainbot.random_colors))
        embed.set_footer(text = f'use `{x}` before each command!')
        await ctx.send(embed = embed)

    @help.command(name = 'random')
    async def random_subcommand(self, ctx):

        with open(r"prefixes.json", 'r') as f:
            prefixes = json.load(f)
        
        x = prefixes[str(ctx.guild.id)] if str(ctx.guild.id) in prefixes else 'le '

        embed = discord.Embed(title = ":smile: Random Commands", description = '`fat`, `guess`, `status`', color = random.choice(mainbot.random_colors))
        embed.set_footer(text = f'use `{x}` before each command!')
        await ctx.send(embed = embed)

    @help.command(name = 'moderation')
    async def mod_subcommand(self, ctx):

        with open(r"prefixes.json", 'r') as f:
            prefixes = json.load(f)
        
        x = prefixes[str(ctx.guild.id)] if str(ctx.guild.id) in prefixes else 'le '

        embed = discord.Embed(title = ":hammer: Moderation Commands", description = '`kick`, `ban`, `unban`, `purge`, `userinfo`, `warn`, `createrole`, `changenick`, `reactionmessage`, `membermessage`, `setmembermessage`, `setchannelid`, `viewmembermessage`, `autopurge`, `stoppurge`, `new`, `delete`, `lock`, `unlock`', color = random.choice(mainbot.random_colors))
        embed.set_footer(text = f'use `{x}` before each command!')
        await ctx.send(embed = embed)
    
    @help.command(name = 'settings')
    async def settings_subcommand(self, ctx):

        with open(r"prefixes.json", 'r') as f:
            prefixes = json.load(f)
        
        x = prefixes[str(ctx.guild.id)] if str(ctx.guild.id) in prefixes else 'le '

        embed = discord.Embed(title = ':axe: Setting Commands', description = '`setprefix`, `resetprefix`', color = random.choice(mainbot.random_colors))
        embed.set_footer(text = f'use `{x}` before each command!')
        await ctx.send(embed = embed)

async def setup(bot):
    await bot.add_cog(help(bot)) 
