import discord
from discord.ext import commands
import globals

def setup(bot):
    bot.add_cog(Vote(bot))


class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['v'])
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def vote(self, ctx):
        if ctx.invoked_subcommand is None:
            # create the embed
            embed = discord.Embed(title='Vote Here!',
                description='Use the link above to vote for me on Discord Bot list and help me become more popular!',
                url='https://top.gg/bot/717125416858550322',
                color=globals.embed_color
            )
            embed.set_thumbnail(url='http://vlrnt.hubermjonathan.com/icon')

            # send the message
            await ctx.send(embed=embed)
