import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import globals

# load environment variables
if os.getenv('DEV') is not None:
    load_dotenv('.env')

# create the bot
bot = commands.Bot(owner_id=int(os.getenv('OWNER_ID')),
                   command_prefix=commands.when_mentioned_or('val '),
                   activity=discord.Activity(type=discord.ActivityType.listening, name=f'val help | {globals.version_number}'))
bot.remove_command('help')

# add all the cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# run the bot
bot.run(os.getenv('TOKEN'))
