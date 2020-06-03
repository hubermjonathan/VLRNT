import discord
from discord.ext import commands
import globals

def setup(bot):
    bot.add_cog(Arrows(bot))


class Arrows(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['arw'], case_insensitive=True)
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def arrows(self, ctx):
        if ctx.invoked_subcommand is None:
            # create the embed
            embed = discord.Embed(
                title='Which map?',
                description='Use `val arrows [map_name]` to choose a map from the following.\n',
                color=globals.embed_color
            )
            embed.set_thumbnail(url='https://hubermjonathan-vlrnt.herokuapp.com/sova')
            embed.add_field(name='**Maps**',
                value='Bind, Haven, Split, Ascent',
                inline=False
            )

            # send the message
            await ctx.send(embed=embed)

    @arrows.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def bind(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Sova Arrows for Bind',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-vlrnt.herokuapp.com/sova')
        embed.add_field(name='**Coming Soon**',
            value='The bot owner is currently gathering arrow locations and will update this feature soon.',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @arrows.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def haven(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Sova Arrows for Haven',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-vlrnt.herokuapp.com/sova')
        embed.add_field(name='**Coming Soon**',
            value='The bot owner is currently gathering arrow locations and will update this feature soon.',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @arrows.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def split(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Sova Arrows for Split',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-vlrnt.herokuapp.com/sova')
        embed.add_field(name='**Coming Soon**',
            value='The bot owner is currently gathering arrow locations and will update this feature soon.',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @arrows.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def ascent(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Sova Arrows for Ascent',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-vlrnt.herokuapp.com/sova')
        embed.add_field(name='**Coming Soon**',
            value='The bot owner is currently gathering arrow locations and will update this feature soon.',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)
