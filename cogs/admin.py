import os
from datetime import datetime
from discord.ext import commands


def setup(bot):
    bot.add_cog(Admin(bot))


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # message owner
        if os.getenv('DEV') is None:
            print('BOT STATUS: ready')
            user = await self.bot.fetch_user(self.bot.owner_id)
            await user.send(f'Bot ready at {datetime.now().time()}')

    @commands.command(aliases=['l'])
    @commands.is_owner()
    async def load(self, ctx, cog):
        # reload the extension
        try:
            self.bot.load_extension(f'cogs.{cog}')
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
            await ctx.message.add_reaction('👎')
            return

        # acknowledge the command
        await ctx.message.add_reaction('👍')
