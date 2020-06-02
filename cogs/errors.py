import discord
from discord.ext import commands
import globals


def setup(bot):
    bot.add_cog(Errors(bot))


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.message.add_reaction('🔒')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.message.add_reaction('❔')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(title='Error', description=f'See `val help {ctx.command}` for correct command usage', color=globals.embed_color))
        elif isinstance(error, commands.ArgumentParsingError):
            await ctx.send(embed=discord.Embed(title='Error', description=f'See `val help {ctx.command}` for correct command usage', color=globals.embed_color))
        elif isinstance(error, commands.TooManyArguments):
            await ctx.send(embed=discord.Embed(title='Error', description=f'See `val help {ctx.command}` for correct command usage', color=globals.embed_color))
        elif isinstance(error, commands.BadArgument):
            await ctx.send(embed=discord.Embed(title='Error', description=f'{error}', color=globals.embed_color))
        else:
            print(f'BOT ERROR: {error}')
            await ctx.message.add_reaction('👎')
