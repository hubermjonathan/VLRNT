import random
import discord
from discord.ext import commands
import globals

def setup(bot):
    bot.add_cog(History(bot))


class History(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['h', 'hist'])
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def history(self, ctx, *args):
        async with ctx.typing():
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

            # send full match history
            if len(args) == 1:
                # create the embed
                embed = discord.Embed(title=args[0], description='Match History', color=globals.embed_color)
                for i in range(3):
                    map = random.choice(["Bind", "Haven", "Split", "Ascent"])
                    embed.add_field(name=f'**Game {i+1}**',
                        value=f'**{map} - {random.choice(["Victory", "Defeat"])}**\n'
                            f'{random.choice(["13-12", "7-13", "13-10", "13-4", "9-13"])}\n'
                            f'Combat Score: {random.randrange(200, 400)}\n'
                            f'Score: {random.randrange(7, 30)}/{random.randrange(7, 20)}/{random.randrange(0, 10)}\n',
                        inline=False
                    )
                embed.set_footer(text='Because the VALORANT API is still in development, no real data is used for this command.')

                # send the message
                await ctx.send(embed=embed)

            # send single game information
            else:
                # create the embed
                embed = discord.Embed(title=args[0], color=globals.embed_color)
                map = random.choice(["Bind", "Haven", "Split", "Ascent"])
                embed.set_thumbnail(url=f'https://hubermjonathan-vlrnt.herokuapp.com/{map}')
                embed.add_field(name=f'**{map} - {random.choice(["Victory", "Defeat"])}**\n',
                    value=f'{random.choice(["13-12", "7-13", "13-10", "13-4", "9-13"])}\n'
                        f'Combat Score: {random.randrange(200, 400)}\n'
                        f'Score: {random.randrange(7, 30)}/{random.randrange(7, 20)}/{random.randrange(0, 10)}\n',
                    inline=False
                )
                embed.set_footer(text='Because the VALORANT API is still in development, no real data is used for this command.')

                # send the message
                await ctx.send(embed=embed)

