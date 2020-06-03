import discord
from discord.ext import commands
import globals

def setup(bot):
    bot.add_cog(Ranked(bot))


class Ranked(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['r'])
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def ranked(self, ctx, riot_id):
        async with ctx.typing():
            # TODO verify riot id

            # create the embed
            embed = discord.Embed(title=riot_id, description='Ranked Stats', color=globals.embed_color)
            embed.set_thumbnail(url='https://hubermjonathan-vlrnt.herokuapp.com/plat3')
            embed.add_field(name='**Games**',
                value=f'**Games Played:** {35+31}\n'
                    f'**Games Won:** {35}\n'
                    f'**Games Lost:** {31}\n'
                    f'**Win Rate:** {round(35/(35+31)*100)}%\n',
                inline=True
            )
            embed.add_field(name='**Performance**',
                value=f'**Kills:** {430}\n'
                    f'**Deaths:** {389}\n'
                    f'**Assists:** {257}\n'
                    f'**K/D Ratio:** {round(430/389, 2)}\n'
                    f'**Headshot %:** {round(225/420*100)}%\n'
                    f'**Combat Score:** {289}\n',
                inline=True
            )
            embed.set_footer(text='Because the VALORANT API is still in development, no real data is used for this command.')

            # send the message
            await ctx.send(embed=embed)
