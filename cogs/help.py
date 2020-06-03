import discord
from discord.ext import commands
import globals

def setup(bot):
    bot.add_cog(Help(bot))


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            # create the embed
            embed = discord.Embed(title='Valorant Bot Help',
                description='Use `val?help {command}` for more information about a specific command.\n'
                    '[] indicates a required argument and {} indicates an optional one. Do not include these in the commands.\n',
                color=globals.embed_color
            )
            embed.set_thumbnail(url='http://assets.hubermjonathan.com/vlrnt/icon')
            embed.add_field(name='**Available Commands**',
                value='Help messages - `help {command}`\n'
                    'Unrated stats - `unrated [riot_id]`\n'
                    'Ranked stats - `ranked [riot_id]`\n'
                    'Spike rush stats - `spikerush [riot_id]`\n'
                    'Current game - `scout [riot_id]`\n'
                    'Match history - `history [riot_id] {number}`\n'
                    'Latest patch notes - `notes`\n'
                    'Tier list - `tiers {vote [agent] [agent] [agent]}`\n'
                    'Agent information - `agents [agent]`\n'
                    'Sova arrows - `arrows [map]`\n',
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
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def unrated(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='`unrated [riot_id]`',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://assets.hubermjonathan.com/vlrnt/icon')
        embed.add_field(name='**Aliases**',
            value='u, ur\n',
            inline=False
        )
        embed.add_field(name='**Arguments**',
            value='**unrated** [Required] - Command group\n'
                '**riot_id** [Required] - The Riot ID of the user to return stats for\n',
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
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def ranked(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='`ranked [riot_id]`',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://assets.hubermjonathan.com/vlrnt/icon')
        embed.add_field(name='**Aliases**',
            value='r\n',
            inline=False
        )
        embed.add_field(name='**Arguments**',
            value='**ranked** [Required] - Command group\n'
                '**riot_id** [Required] - The Riot ID of the user to return stats for\n',
            inline=False
        )
        embed.add_field(name='**Description**',
            value='Returns an overview of stats for a user for the ranked gamemode.',
            inline=False
        )
        embed.set_footer(text=globals.version_number)

        # send the message
        await ctx.send(embed=embed)

    @help.command(aliases=['sr'])
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def spikerush(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='`spikerush [riot_id]`',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://assets.hubermjonathan.com/vlrnt/icon')
        embed.add_field(name='**Aliases**',
            value='sr\n',
            inline=False
        )
        embed.add_field(name='**Arguments**',
            value='**spikerush** [Required] - Command group\n'
                '**riot_id** [Required] - The Riot ID of the user to return stats for\n',
            inline=False
        )
        embed.add_field(name='**Description**',
            value='Returns an overview of stats for a user for the spike rush gamemode.',
            inline=False
        )
        embed.set_footer(text=globals.version_number)

        # send the message
        await ctx.send(embed=embed)

    @help.command(aliases=['s'])
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def scout(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='`scout [riot_id]`',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://assets.hubermjonathan.com/vlrnt/icon')
        embed.add_field(name='**Aliases**',
            value='s\n',
            inline=False
        )
        embed.add_field(name='**Arguments**',
            value='**scout** [Required] - Command group\n'
                '**riot_id** [Required] - The Riot ID of the user to return stats for\n',
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
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def history(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='`history [riot_id] {number}`',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://assets.hubermjonathan.com/vlrnt/icon')
        embed.add_field(name='**Aliases**',
            value='h, hist\n',
            inline=False
        )
        embed.add_field(name='**Arguments**',
            value='**history** [Required] - Command group\n'
                '**riot_id** [Required] - The Riot ID of the user to return stats for\n'
                '**number** {Optional} - The match number to get more details for\n',
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
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def notes(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='`notes`',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://assets.hubermjonathan.com/vlrnt/icon')
        embed.add_field(name='**Aliases**',
            value='n, pn\n',
            inline=False
        )
        embed.add_field(name='**Arguments**',
            value='**notes** [Required] - Command group\n',
            inline=False
        )
        embed.add_field(name='**Description**',
            value='Get the latest patch notes for VALORANT.',
            inline=False
        )
        embed.set_footer(text=globals.version_number)

        # send the message
        await ctx.send(embed=embed)

    @help.command(aliases=['tl'])
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def tiers(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='`tiers {vote [agent] [agent] [agent]}`',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://assets.hubermjonathan.com/vlrnt/icon')
        embed.add_field(name='**Aliases**',
            value='tl\n',
            inline=False
        )
        embed.add_field(name='**Arguments**',
            value='**tiers** [Required] - Command group\n'
                '**vote** {Optional} - Subcommand group\n'
                '**agent** [Required if **vote** is specified] - Agent name to vote for\n',
            inline=False
        )
        embed.add_field(name='**Description**',
            value='View and vote on a community tier list of agents.',
            inline=False
        )
        embed.set_footer(text=globals.version_number)

        # send the message
        await ctx.send(embed=embed)

    @help.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def agents(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='`agents [agent]`',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://assets.hubermjonathan.com/vlrnt/icon')
        embed.add_field(name='**Aliases**',
            value='None\n',
            inline=False
        )
        embed.add_field(name='**Arguments**',
            value='**agents** [Required] - Command group\n'
                '**agent** [Required] - The agent to get information for\n',
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
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def arrows(self, ctx):
        # create the embed
        embed = discord.Embed(title='Valorant Bot Help',
            description='`arrows [map]`',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://assets.hubermjonathan.com/vlrnt/icon')
        embed.add_field(name='**Aliases**',
            value='arw\n',
            inline=False
        )
        embed.add_field(name='**Arguments**',
            value='**arrows** [Required] - Command group\n'
                '**map** [Required] - The map name to get Sova arrows for\n',
            inline=False
        )
        embed.add_field(name='**Description**',
            value='Get locations and lineups for Sova arrows.',
            inline=False
        )
        embed.set_footer(text=globals.version_number)

        # send the message
        await ctx.send(embed=embed)
