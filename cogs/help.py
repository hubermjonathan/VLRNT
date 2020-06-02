import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(Help(bot))


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.version_number = 'v0.0.0'
        self.embed_color = 0xff4654
        self.valorant_icon_url = 'https://hubermjonathan-valorant-bot.herokuapp.com/icon'

    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            # create the embed
            embed=discord.Embed(title='Valorant Bot Help', description='Use `help command_name` for more information about a specific command', color=self.embed_color)
            embed.set_thumbnail(url=self.valorant_icon_url)
            embed.add_field(name='Available Commands',
                            value='command [optional]',
                            inline=True
                            )
            embed.set_footer(text=self.version_number)

            # send the message
            await ctx.send(embed=embed)
