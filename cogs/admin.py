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
    async def on_ready(self):
        # message owner
        if os.getenv('DEV') is not None:
            print('BOT STATUS: ready')
            user = await self.bot.fetch_user(self.bot.owner_id)
            await user.send(embed=discord.Embed(title='Bot ready', description=datetime.now().strftime("%H:%M:%S"), color=globals.embed_color))

    @commands.command()
    @commands.is_owner()
    async def stats(self, ctx):
        # get the number of guilds
        num_guilds = len(self.bot.guilds)

        # get the number of users
        members = []
        for g in self.bot.guilds:
            for m in g.members:
                if not m.bot and m.id not in members:
                    members.append(m.id)
        num_members = len(members)

        # send the message
        await ctx.author.send(embed=discord.Embed(title='Stats', description=f'**Number of guilds:** {num_guilds}\n**Number of members:** {num_members}\n', color=globals.embed_color))

    @commands.command(aliases=['c'])
    @commands.is_owner()
    async def cogs(self, ctx):
        # send the message
        await ctx.author.send(embed=discord.Embed(title='Cogs', description=', '.join(self.bot.cogs), color=globals.embed_color))

    @commands.command(aliases=['l'])
    @commands.is_owner()
    async def load(self, ctx, cog):
        # reload the extension
        try:
            self.bot.load_extension(f'cogs.{cog}')
        except Exception:
            await ctx.message.add_reaction('👎')
            return

        # acknowledge the command
        await ctx.message.add_reaction('👍')

    @commands.command(aliases=['ul'])
    @commands.is_owner()
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
    async def reload(self, ctx, cog):
        # reload the extension
        try:
            self.bot.reload_extension(f'cogs.{cog}')
        except Exception:
            await ctx.message.add_reaction('👎')
            return

        # acknowledge the command
        await ctx.message.add_reaction('👍')
