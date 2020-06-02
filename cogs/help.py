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
            embed = discord.Embed(title='Valorant Bot Help',
                description='Use **val help {command}** for more information about a specific command.\n' \
                    '[] indicates a required argument and {} indicates an optional one. Do not include these in the commands.\n',
                color=globals.embed_color
            )
            embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/icon')
            embed.add_field(name='**Available Commands**',
                value='**help {command}** - Help messages\n' \
                    '**unrated [riot_id]** - Unrated stats\n' \
                    '**ranked [riot_id]** - Ranked stats\n' \
                    '**scout [riot_id]** - Current game\n' \
                    '**history [riot_id] {number}** - Match history\n' \
                    '**notes** - Latest patch notes\n' \
                    '**agents [agent_name]** - Agent information\n' \
                    '**arrows [map_name]** - Sova arrows\n',
                inline=False
            )
            embed.add_field(name='**Owner**',
                value='Add **Huberrrr#2959** on Discord to get help with the bot, ask questions, or request features!',
                inline=False
            )
            embed.set_footer(text=globals.version_number)

            # send the message
            await ctx.send(embed=embed)

    @help.command(aliases=['u', 'ur'])
    async def unrated(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='**unrated [riot_id]**',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/icon')
        embed.add_field(name='**Aliases**',
            value='u, ur\n',
            inline=False
        )
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

    @help.command(aliases=['r'])
    async def ranked(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='**ranked [riot_id]**',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/icon')
        embed.add_field(name='**Aliases**',
            value='r\n',
            inline=False
        )
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

    @help.command(aliases=['s'])
    async def scout(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='**scout [riot_id]**',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/icon')
        embed.add_field(name='**Aliases**',
            value='s\n',
            inline=False
        )
        embed.add_field(name='**Arguments**',
            value='**scout** - [Required] Command group\n' \
                '**riot_id** - [Required] The Riot ID of the user to return stats for\n',
            inline=False
        )
        embed.add_field(name='**Description**',
            value='Get a quick overview of your teammates and enemies for a match.',
            inline=False
        )
        embed.set_footer(text=globals.version_number)

        # send the message
        await ctx.send(embed=embed)

    @help.command(aliases=['h', 'hist'])
    async def history(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='**history [riot_id] {number}**',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/icon')
        embed.add_field(name='**Aliases**',
            value='h, hist\n',
            inline=False
        )
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

    @help.command(aliases=['n', 'pn'])
    async def notes(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='**notes**',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/icon')
        embed.add_field(name='**Aliases**',
            value='n, pn\n',
            inline=False
        )
        embed.add_field(name='**Arguments**',
            value='**notes** - [Required] Command group\n',
            inline=False
        )
        embed.add_field(name='**Description**',
            value='Get the latest patch notes for VALORANT.',
            inline=False
        )
        embed.set_footer(text=globals.version_number)

        # send the message
        await ctx.send(embed=embed)

    @help.command()
    async def agents(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='**agents [agent_name]**',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/icon')
        embed.add_field(name='**Aliases**',
            value='None\n',
            inline=False
        )
        embed.add_field(name='**Arguments**',
            value='**agents** - [Required] Command group\n' \
                '**agent_name** - [Required] The agent to get information for\n',
            inline=False
        )
        embed.add_field(name='**Description**',
            value='Learn about the agents of VALORANT.',
            inline=False
        )
        embed.set_footer(text=globals.version_number)

        # send the message
        await ctx.send(embed=embed)

    @help.command(aliases=['arw'])
    async def arrows(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='**arrows [map_name]**',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='https://hubermjonathan-valorant-bot.herokuapp.com/icon')
        embed.add_field(name='**Aliases**',
            value='arw\n',
            inline=False
        )
        embed.add_field(name='**Arguments**',
            value='**arrows** - [Required] Command group\n' \
                '**map_name** - [Required] The map name to get Sova arrows for\n',
            inline=False
        )
        embed.add_field(name='**Description**',
            value='Get locations and lineups for Sova arrows.',
            inline=False
        )
        embed.set_footer(text=globals.version_number)

        # send the message
        await ctx.send(embed=embed)
