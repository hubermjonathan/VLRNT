import discord

version_number = 'v0.0.1'
embed_color = 0xff4654

def create_error_message(message):
    # create the embed
    embed=discord.Embed(title='Error', description=message, color=embed_color)

    # return the embed
    return embed
