import discord
from discord.ext import commands
import globals

def setup(bot):
    bot.add_cog(Unrated(bot))


class Unrated(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unrated(self, ctx, riot_id):
        # TODO verify riot id
        if False:
            raise commands.BadArgument('Provide a valid Riot ID')

        # TODO gather the data
        kills = 430
        deaths = 389
        games_won = 35
        games_lost = 31

        # create the embed
        embed=discord.Embed(title=riot_id, description='Unrated Stats', color=globals.embed_color)
        embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/sova')
        embed.add_field(name='**Games**',
                        value=f'**Games Won:** {games_won}\n' \
                            f'**Games Lost:** {games_lost}\n'
                            f'**Win Ratio:** {round(games_won/(games_won+games_lost)*100, 2)}%\n',
                        inline=True
                        )
        embed.add_field(name='**Performance**',
                        value=f'**Kills:** {kills}\n' \
                            f'**Deaths:** {deaths}\n' \
                            f'**K/D Ratio:** {round(kills/deaths, 2)}\n',
                        inline=True
                        )

        # send the message
        await ctx.send(embed=embed)