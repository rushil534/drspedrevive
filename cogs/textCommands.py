from discord.ext import commands

class textCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    

    @commands.command()
    async def bold(self, ctx, *, message: str):
        await ctx.send(f'**{message}**')





    @commands.command()
    async def underline(self, ctx, *, message: str):
        await ctx.send(f'__{message}__')





    @commands.command()
    async def strikethrough(self, ctx, *, message: str):
        await ctx.send(f'~~{message}~~')





    @commands.command()
    async def italics(self, ctx, *, message: str):
        await ctx.send(f'*{message}*')





    @commands.command()
    async def bolditalics(self, ctx, *, message: str):
        await ctx.send(f'***{message}***')





    @commands.command()
    async def underlineitalics(self, ctx, *, message: str):
        await ctx.send(f'__*{message}*__')





    @commands.command()
    async def underlinebold(self, ctx, *, message: str):
        await ctx.send(f'__**{message}**__')





    @commands.command()
    async def ubi(self, ctx, *, message: str):
        await ctx.send(f'__***{message}***__')





    @commands.command()
    async def codeblock(self, ctx, *, message: str):
        await ctx.send(f'`{message}`')





    @commands.command()
    async def echo(self, ctx, *, message: str):
        await ctx.send(f'{message}')





    @commands.command()
    async def bify(self, ctx, *, text: str):
        NUMBERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        VOWELS = ["a", "e", "i", "o", "u"]
        bified = ""

        for word in text.split(" "):

            bified += ":b:" + word[1:] + " " if word[0].lower() not in VOWELS else word + " "

        await ctx.send(bified)





    @commands.command()
    async def greenify(self, ctx, *, message : str):
        await ctx.send(f'```css\n{message}```')
    
    #--------
    # Errors
    #--------

    @echo.error
    async def echo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `le echo [words]`')





    @bify.error
    async def bify_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `le bify [word that starts with a consonant]`')





    @greenify.error
    async def greenify_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `le greenify [words]`')

    

    @bold.error
    async def bold_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `le bold [words]`')





    @bolditalics.error
    async def boldi_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `le bolditalics [words]`')





    @underline.error
    async def underline_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `le underline [words]`')





    @underlinebold.error
    async def underlinebold_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `le underlinebold [words]`')





    @underlineitalics.error
    async def underlineitalics_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `le underlineitalics [words]`')





    @strikethrough.error
    async def strikethrough_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `le strikethrough [words]`')





    @ubi.error
    async def ubi_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `le ubi [words]`')





    @codeblock.error
    async def codeblock_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `le codeblock [words]`')





    @italics.error
    async def italics_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Proper Usage: `le italics [words]`')

async def setup(bot):
    await bot.add_cog(textCommands(bot))
