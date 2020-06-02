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
            embed=discord.Embed(title='Valorant Bot Help',
                description='[] indicates a required argument and {} indicates and optional one.\n' \
                    'Do not include these in the commands.\n' \
                    'Use **help {command}** for more information about a specific command.\n',
                color=globals.embed_color
            )
            embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/icon')
            embed.add_field(name='**Available Commands**',
                value='**help {command}** - Help messages\n' \
                    '**unrated [riot_id]** - Unrated stats\n' \
                    '**ranked [riot_id]** - Ranked stats\n' \
                    '**history [riot_id] {number}** - Match history\n',
                inline=False
            )
            embed.add_field(name='**Owner**',
                value='Add **Huberrrr#2959** on Discord to get help with the bot, ask questions, or request features!',
                inline=False
            )
            embed.set_footer(text=globals.version_number)

            # send the message
            await ctx.send(embed=embed)

    @help.command()
    async def unrated(self, ctx):
        # create the embed
        embed=discord.Embed(title='Valorant Bot Help',
            description='**unrated [riot_id]**',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/icon')
        embed.add_field(name='**Arguments**',
            value='**unrated** - [Required] Command group\n' \
                '**riot_id** - [Required] The Riot ID of the user to return stats for\n',
            inline=False
        )
        embed.add_field(name='**Description**',
            value='Returns an overview of stats for a user for the unrated gamemode.',
            inline=False
        )
        embed.set_footer(text=globals.version_number)

        # send the message
        await ctx.send(embed=embed)

    @help.command()
    async def ranked(self, ctx):
        # create the embed
        embed=discord.Embed(title='Valorant Bot Help',
            description='**ranked [riot_id]**',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/icon')
        embed.add_field(name='**Arguments**',
            value='**ranked** - [Required] Command group\n' \
                '**riot_id** - [Required] The Riot ID of the user to return stats for\n',
            inline=False
        )
        embed.add_field(name='**Description**',
            value='Returns an overview of stats for a user for the ranked gamemode.',
            inline=False
        )
        embed.set_footer(text=globals.version_number)

        # send the message
        await ctx.send(embed=embed)

    @help.command()
    async def history(self, ctx):
        # create the embed
        embed=discord.Embed(title='Valorant Bot Help',
            description='**history [riot_id] {number}**',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/icon')
        embed.add_field(name='**Arguments**',
            value='**history** - [Required] Command group\n' \
                '**riot_id** - [Required] The Riot ID of the user to return stats for\n' \
                '**number** - {Optional} The match number to get more details for\n',
            inline=False
        )
        embed.add_field(name='**Description**',
            value='Look up match history for a given Riot ID or specify a number to get more details about a specific match.',
            inline=False
        )
        embed.set_footer(text=globals.version_number)

        # send the message
        await ctx.send(embed=embed)
