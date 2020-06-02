import discord
from discord.ext import commands
import globals

def setup(bot):
    bot.add_cog(Scout(bot))


class Scout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['s'])
    async def scout(self, ctx, riot_id):
        # TODO verify riot id
        if False:
            raise commands.BadArgument('Provide a valid Riot ID')

        # create the embed
        embed = discord.Embed(title=riot_id, description='Scout Data', color=globals.embed_color)
        embed.add_field(name='**Your Team**',
            value=f'**Sage (Iron 3):** 53% W/L 0.87 K/D\n' \
                f'**Sova (Iron 2):**  56% W/L 1.05 K/D\n' \
                f'**Breach (Bronze 3):**  48% W/L 0.63 K/D\n' \
                f'**Phoenix (Iron 1):**  51% W/L 0.95 K/D\n' \
                f'**Brimstone (Silver 2):**  52% W/L 1.12 K/D\n',
            inline=True
        )
        embed.add_field(name='**Enemy Team**',
            value=f'**Sova (Iron 3):** 53% W/L 0.87 K/D\n' \
                f'**Breach (Iron 2):**  56% W/L 1.05 K/D\n' \
                f'**Cypher (Bronze 3):**  48% W/L 0.63 K/D\n' \
                f'**Reyna (Iron 1):**  51% W/L 0.95 K/D\n' \
                f'**Sage (Silver 2):**  52% W/L 1.12 K/D\n',
            inline=True
        )

        # send the message
        await ctx.send(embed=embed)
