import os
from datetime import datetime
import discord
from discord.ext import commands
import globals


def setup(bot):
    bot.add_cog(Admin(bot))


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        # get the number of guilds
        num_guilds = len(self.bot.guilds) - 2

        # get the number of users
        members = []
        for g in self.bot.guilds:
            if g.id == 110373943822540800 or g.id == 264445053596991498:
                continue
            for m in g.members:
                if not m.bot and m.id not in members:
                    members.append(m.id)
        num_members = len(members)

        # send the message
        await self.bot.get_user(196141424318611457).send(embed=discord.Embed(title='New Guild', description=f'**New guild name:** {guild.name}\n**Number of guilds:** {num_guilds}\n**Number of members:** {num_members}\n', color=globals.embed_color))

    @commands.command()
    @commands.is_owner()
    @commands.dm_only()
    async def stats(self, ctx):
        # get the number of guilds
        num_guilds = len(self.bot.guilds) - 2

        # get the number of users
        members = []
        for g in self.bot.guilds:
            if g.id == 110373943822540800 or g.id == 264445053596991498:
                continue
            for m in g.members:
                if not m.bot and m.id not in members:
                    members.append(m.id)
        num_members = len(members)

        # send the message
        await ctx.author.send(embed=discord.Embed(title='Stats', description=f'**Number of guilds:** {num_guilds}\n**Number of members:** {num_members}\n', color=globals.embed_color))

    @commands.command()
    @commands.is_owner()
    @commands.dm_only()
    async def cogs(self, ctx):
        # send the message
        await ctx.author.send(embed=discord.Embed(title='Cogs', description=', '.join(self.bot.cogs), color=globals.embed_color))

    @commands.command()
    @commands.is_owner()
    @commands.dm_only()
    async def load(self, ctx, cog):
        # reload the extension
        try:
            self.bot.load_extension(f'cogs.{cog}')
        except Exception:
            await ctx.message.add_reaction('👎')
            return

        # acknowledge the command
        await ctx.message.add_reaction('👍')

    @commands.command()
    @commands.is_owner()
    @commands.dm_only()
    async def unload(self, ctx, cog):
        # reload the extension
        try:
            self.bot.unload_extension(f'cogs.{cog}')
        except Exception:
            await ctx.message.add_reaction('👎')
            return

        # acknowledge the command
        await ctx.message.add_reaction('👍')

    @commands.command(aliases=['rl'])
    @commands.is_owner()
    @commands.dm_only()
    async def reload(self, ctx, cog):
        # reload the extension
        try:
            self.bot.reload_extension(f'cogs.{cog}')
        except Exception:
            await ctx.message.add_reaction('👎')
            return

        # acknowledge the command
        await ctx.message.add_reaction('👍')
