import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import globals


def setup(bot):
    bot.add_cog(Notes(bot))


class Notes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['n', 'pn'])
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def notes(self, ctx):
        # get the patch notes
        r = requests.get('https://playvalorant.com/en-us/news/')
        soup = BeautifulSoup(r.content, 'html.parser')
        for a in soup.find_all('a', href=True):
            if 'game-updates/valorant-patch-notes' in a.get('href') and 'news-card' not in a.parent.get('class'):
                notes = f'https://playvalorant.com{a.get("href")}'
                print(notes)
                break

        # get the highlights
        r = requests.get(notes)
        soup = BeautifulSoup(r.content, 'html.parser')
        for img in soup.find_all('img'):
            if 'Patch_Notes' in img.get('alt'):
                highlights = img.get('src')
                print(highlights)
                break

        # create the embed
        embed = discord.Embed(title='Here are the latest patch notes!',
            description=soup.title.string,
            url=notes,
            color=globals.embed_color
        )
        embed.set_image(url=highlights)

        # send the message
        await ctx.send(embed=embed)
