import discord
from discord.ext import commands
import globals

def setup(bot):
    bot.add_cog(Scout(bot))


class Scout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['s'])
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def scout(self, ctx, riot_id):
        # TODO verify riot id, verify in game

        # create the embed
        embed = discord.Embed(title=riot_id, description='Scout Data', color=globals.embed_color)
        embed.set_thumbnail(url='https://hubermjonathan-vlrnt.herokuapp.com/haven')
        embed.add_field(name='**Your Team**',
            value=f'**Player 1 - Sage (Iron 3):** 53% W/L - 0.87 K/D\n' \
                f'**Player 2 - Sova (Iron 2):**  56% W/L - 1.05 K/D\n' \
                f'**Player 3 - Breach (Bronze 3):**  48% W/L - 0.63 K/D\n' \
                f'**Player 4 - Phoenix (Iron 1):**  51% W/L - 0.95 K/D\n' \
                f'**Player 5 - Brimstone (Silver 2):**  52% W/L - 1.12 K/D\n',
            inline=False
        )
        embed.add_field(name='**Enemy Team**',
            value=f'**Player 1 - Sova (Iron 3):** 53% W/L - 0.87 K/D\n' \
                f'**Player 2 - Breach (Iron 2):**  56% W/L - 1.05 K/D\n' \
                f'**Player 3 - Cypher (Bronze 3):**  48% W/L - 0.63 K/D\n' \
                f'**Player 4 - Reyna (Iron 1):**  51% W/L - 0.95 K/D\n' \
                f'**Player 5 - Sage (Silver 2):**  52% W/L - 1.12 K/D\n',
            inline=False
        )
        embed.set_footer(text='Because the VALORANT API is still in development, no real data is used for this command.')

        # send the message
        await ctx.send(embed=embed)
