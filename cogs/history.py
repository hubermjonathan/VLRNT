import discord
from discord.ext import commands
import globals

def setup(bot):
    bot.add_cog(History(bot))


class History(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_match_history(self, ctx, riot_id, games):
        # create the embed
        embed = discord.Embed(title=riot_id, description='Match History', color=globals.embed_color)
        for i, game in enumerate(games):
            embed.add_field(name=f'**Game {i+1}**',
                value=f'**{game["map"]} - {game["result"]}**\n' \
                    f'{game["score"]}\n' \
                    f'Combat Score: {game["avg_combat_score"]}\n' \
                    f'Score: {game["kills"]}/{game["deaths"]}\n',
                inline=False
            )

        # send the message
        await ctx.send(embed=embed)

    async def get_single_game(self, ctx, riot_id, game):
        # create the embed
        embed = discord.Embed(title=riot_id, color=globals.embed_color)
        embed.add_field(name=f'**{game["map"]} - {game["result"]}**\n',
            value=f'{game["score"]}\n' \
                f'Combat Score: {game["avg_combat_score"]}\n' \
                f'Score: {game["kills"]}/{game["deaths"]}\n',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @commands.command(aliases=['h', 'hist'])
    async def history(self, ctx, *args):
        # verify args
        if len(args) == 0:
            raise commands.ArgumentParsingError()
        elif len(args) > 2:
            raise commands.TooManyArguments()
        elif len(args) == 2:
            try:
                if int(args[1]) < 1 or int(args[1]) > 3:
                    raise commands.BadArgument('Provide a valid match number')
            except ValueError:
                raise commands.BadArgument('Provide a valid match number')

        # TODO verify riot id
        if False:
            raise commands.BadArgument('Provide a valid Riot ID')

        # TODO gather the data
        games = [
            {
                'map': 'Bind',
                'score': '13-12',
                'result': 'Victory',
                'kills': 24,
                'deaths': 11,
                'avg_combat_score': 365
            },
            {
                'map': 'Split',
                'score': '11-13',
                'result': 'Defeat',
                'kills': 17,
                'deaths': 19,
                'avg_combat_score': 243
            },
            {
                'map': 'Haven',
                'score': '13-6',
                'result': 'Victory',
                'kills': 28,
                'deaths': 9,
                'avg_combat_score': 413
            }
        ]

        if len(args) == 1:
            # send full match history
            await self.get_match_history(ctx, args[0], games)
        else:
            # send single game information
            await self.get_single_game(ctx, args[0], games[int(args[1])-1])

