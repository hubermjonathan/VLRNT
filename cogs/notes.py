import requests
from bs4 import BeautifulSoup
from discord.ext import commands


def setup(bot):
    bot.add_cog(Notes(bot))


class Notes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def notes(self, ctx):
        # get the patch notes
        r = requests.get('https://playvalorant.com/en-us/news/')
        soup = BeautifulSoup(r.content, 'html.parser')
        for a in soup.find_all('a', href=True):
            if 'game-updates/valorant-patch-notes' in a["href"]:
                notes = f'https://playvalorant.com{a["href"]}'
                break

        # get the highlights
        r = requests.get(notes)
        soup = BeautifulSoup(r.content, 'html.parser')
        for a in soup.find_all('a', href=True):
            if 'patchnotes' in a["href"]:
                highlights = a["href"]
                break

        # send the message
        await ctx.send(f'Here are the latest patch notes!\n{notes}\n{highlights}\n')
