import os
import redis
import discord
from discord.ext import commands
import globals

def setup(bot):
    bot.add_cog(Tiers(bot))


class Tiers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.redis = redis.from_url(os.environ.get('REDIS_URL'))

    @commands.group(aliases=['tl'])
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def tiers(self, ctx):
        if ctx.invoked_subcommand is None:
            async with ctx.typing():
                # get the agents
                agents = [
                    ('Jett', int(self.redis.get('jett'))),
                    ('Raze', int(self.redis.get('raze'))),
                    ('Breach', int(self.redis.get('breach'))),
                    ('Omen', int(self.redis.get('omen'))),
                    ('Brimstone', int(self.redis.get('brimstone'))),
                    ('Phoenix', int(self.redis.get('phoenix'))),
                    ('Sage', int(self.redis.get('sage'))),
                    ('Sova', int(self.redis.get('sova'))),
                    ('Viper', int(self.redis.get('viper'))),
                    ('Cypher', int(self.redis.get('cypher'))),
                    ('Reyna', int(self.redis.get('reyna'))),
                ]

                # sort the agents
                agents.sort(key=lambda t: t[1], reverse=True)

                # create the rankings
                rankings = ''
                for i, agent in enumerate(agents):
                    rankings = rankings + f'**{i+1}:** {agent[0]} ({agent[1]})\n'

                # create the embed
                embed = discord.Embed(title='Community Tier List', description='To submit your vote, use `val?tiers vote`.', color=globals.embed_color)
                embed.set_thumbnail(url=f'http://assets.hubermjonathan.com/vlrnt/{agents[0][0].lower()}')
                embed.add_field(name='**Agents**',
                    value=rankings,
                    inline=True
                )

                # send the message
                await ctx.send(embed=embed)

    @tiers.command()
    @commands.is_owner()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def reset(self, ctx):
        async with ctx.typing():
            # reset agent scores
            self.redis.set('jett', 0)
            self.redis.set('raze', 0)
            self.redis.set('breach', 0)
            self.redis.set('omen', 0)
            self.redis.set('brimstone', 0)
            self.redis.set('phoenix', 0)
            self.redis.set('sage', 0)
            self.redis.set('sova', 0)
            self.redis.set('viper', 0)
            self.redis.set('cypher', 0)
            self.redis.set('reyna', 0)

            # send the message
            await ctx.send(embed=discord.Embed(title='Community Tier List', description='The community tier list has been reset.', color=globals.embed_color))

    @tiers.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def vote(self, ctx, *args):
        # verify args
        if len(args) == 1 or len(args) == 2:
            raise commands.ArgumentParsingError()
        elif len(args) > 3:
            raise commands.TooManyArguments()
        elif len(args) == 3:
            valid_agents = ['jett', 'raze', 'breach', 'omen', 'brimstone', 'phoenix', 'sage', 'sova', 'viper', 'cypher', 'reyna']
            if str(args[0]).lower() not in valid_agents or str(args[1]).lower() not in valid_agents or str(args[2]).lower() not in valid_agents:
                raise commands.BadArgument('Provide valid agent names.')

        # send help message
        if len(args) == 0:
            # create the embed
            embed = discord.Embed(
                title='Community Tier List',
                description='Vote for the 3 agents who you think are the **strongest** using the following format:\n'
                    '`val?tiers vote [agent_name] [agent_name] [agent_name]`\n'
                    '\nDo not include the [] in your command. The first agent listed is your first place and the last one is third place.\n'
                    '\nExample: `val?tiers vote Sova Reyna Raze`',
                color=globals.embed_color
            )

            # send the message
            await ctx.send(embed=embed)
            return

        async with ctx.typing():
            # remove old votes
            if self.redis.get(ctx.author.id) is not None:
                old_votes = tuple(map(str, self.redis.get(ctx.author.id).decode('utf-8').split(' ')))
                new_votes = int(self.redis.get(str(old_votes[0]).lower()))-7
                self.redis.set(str(old_votes[0]).lower(), new_votes if new_votes > 0 else 0)
                new_votes = int(self.redis.get(str(old_votes[1]).lower()))-3
                self.redis.set(str(old_votes[1]).lower(), new_votes if new_votes > 0 else 0)
                new_votes = int(self.redis.get(str(old_votes[2]).lower()))-1
                self.redis.set(str(old_votes[2]).lower(), new_votes if new_votes > 0 else 0)

            # submit votes
            self.redis.set(str(args[0]).lower(), int(self.redis.get(str(args[0]).lower()))+7)
            self.redis.set(str(args[1]).lower(), int(self.redis.get(str(args[1]).lower()))+3)
            self.redis.set(str(args[2]).lower(), int(self.redis.get(str(args[2]).lower()))+1)
            self.redis.set(ctx.author.id, ' '.join(args))

            # send the message
            await ctx.send(embed=discord.Embed(title='Community Tier List', description='Your vote has been submitted.', color=globals.embed_color))
