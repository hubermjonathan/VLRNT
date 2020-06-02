import discord
from discord.ext import commands
import globals

def setup(bot):
    bot.add_cog(Help(bot))


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            # create the embed
            embed=discord.Embed(title='Valorant Bot Help', description='Use `help command_name` for more information about a specific command', color=globals.embed_color)
            embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/icon')
            embed.add_field(name='Available Commands',
                            value='command [optional]',
                            inline=True
                            )
            embed.set_footer(text=globals.version_number)

            # send the message
            await ctx.send(embed=embed)
