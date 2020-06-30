import discord
from discord.ext import commands
import globals


def setup(bot):
    bot.add_cog(Agents(bot))


class Agents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(case_insensitive=True)
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def agents(self, ctx):
        if ctx.invoked_subcommand is None:
            # create the embed
            embed = discord.Embed(
                title='Which agent would you like to learn about?',
                description='Use `val?agents [agent_name]` to choose an agent from the following.\n',
                color=globals.embed_color
            )
            embed.add_field(name='**Agents**',
                value='Jett, Raze, Breach, Omen, Brimstone, Phoenix, Sage, Sova, Viper, Cypher, Reyna',
                inline=False
            )

            # send the message
            await ctx.send(embed=embed)

    @agents.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def jett(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Jett',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://vlrnt.hubermjonathan.com/jett')
        embed.add_field(name='**Q - Updraft**',
            value='INSTANTLY propel Jett high into the air.',
            inline=False
        )
        embed.add_field(name='**E - Tailwind**',
            value='INSTANTLY propel Jett in the direction she is moving. If Jett is standing still, she will propel forward.',
            inline=False
        )
        embed.add_field(name='**C - Cloudburst**',
            value='INSTANTLY throw a projectile that expands into a brief vision-blocking cloud on impact with a surface. HOLD the ability key to curve the smoke in the direction of your crosshair.',
            inline=False
        )
        embed.add_field(name='**X - Blade Storm**',
            value='EQUIP a set of highly accurate knives that recharge on killing an opponent. FIRE to throw a single knife at your target. ALTERNATE FIRE to throw all remaining daggers at your target.',
            inline=False
        )
        embed.add_field(name='**Ability Videos**',
            value='To view videos of Jett\'s abilities visit https://playvalorant.com/en-us/agents/jett/',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @agents.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def raze(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Raze',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://vlrnt.hubermjonathan.com/raze')
        embed.add_field(name='**Q - Blast Pack**',
            value='INSTANTLY throw a Blast Pack that will stick to surfaces. RE-USE the ability after deployment to detonate, damaging and moving anything hit. Raze isn\'t damaged by this ability, but will still take fall damage if launched up far enough.',
            inline=False
        )
        embed.add_field(name='**E - Paint Shells**',
            value='EQUIP a cluster grenade. FIRE to throw the grenade, which does damage and creates sub-munitions, each doing damage to anyone in their range.',
            inline=False
        )
        embed.add_field(name='**C - Boom Bot**',
            value='EQUIP a Boom Bot. FIRE will deploy the bot, causing it to travel in a straight line on the ground, bouncing off walls. The Boom Bot will lock on to any enemies in its frontal cone and chase them, exploding for heavy damage if it reaches them.',
            inline=False
        )
        embed.add_field(name='**X - Showstopper**',
            value='EQUIP a rocket launcher. FIRE shoots a rocket that does massive area damage on contact with anything.',
            inline=False
        )
        embed.add_field(name='**Ability Videos**',
            value='To view videos of Raze\'s abilities visit https://playvalorant.com/en-us/agents/raze/',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @agents.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def breach(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Breach',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://vlrnt.hubermjonathan.com/breach')
        embed.add_field(name='**Q - Flashpoint**',
            value='EQUIP a blinding charge. FIRE the charge to set fast-acting burst through the wall. The charge detonates to blind all players looking at it.',
            inline=False
        )
        embed.add_field(name='**E - Fault Line**',
            value='EQUIP a seismic blast. HOLD FIRE to increase the distance. RELEASE to set off the quake, danzing all players in its zone and in a line up to the zone.',
            inline=False
        )
        embed.add_field(name='**C - Aftershock**',
            value='EQUIP a fusion charge. FIRE the charge to set a slow-acting burst through the wall. The burst does heavy damage to anyone caught in its area.',
            inline=False
        )
        embed.add_field(name='**X - Rolling Thunder**',
            value='EQUIP a seismic charge. FIRE to send a cascading quake through all terrain in a large cone. The quake dazes and knocks up anyone caught in it.',
            inline=False
        )
        embed.add_field(name='**Ability Videos**',
            value='To view videos of Breach\'s abilities visit https://playvalorant.com/en-us/agents/breach/',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @agents.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def omen(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Omen',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://vlrnt.hubermjonathan.com/omen')
        embed.add_field(name='**Q - Paranoia**',
            value='INSTANTLY fire a shadow projectile forward, briefly reducing the vision range of all players it touches. This projectile can pass straight through walls.',
            inline=False
        )
        embed.add_field(name='**E - Dark Cover**',
            value='EQUIP a shadow orb and see its range indicator. FIRE to throw the shadow orb to the marked location, creating a long-lasting shadow sphere that blocks vision. HOLD ALTERNATE FIRE while targeting to move the marker further away. HOLD the ability key with targeting to move the market closer.',
            inline=False
        )
        embed.add_field(name='**C - Shrouded Step**',
            value='EQUIP a shadow walk ability and see its range indicator. FIRE to begin a brief channel, then teleport to the marked location.',
            inline=False
        )
        embed.add_field(name='**X - From The Shadows**',
            value='EQUIP a tactical map. FIRE to begin teleporting to the selected location. While teleporting, Omen will appear as a Shade that can be destroyed by an enemy to cancel his teleport.',
            inline=False
        )
        embed.add_field(name='**Ability Videos**',
            value='To view videos of Omen\'s abilities visit https://playvalorant.com/en-us/agents/omen/',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @agents.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def brimstone(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Brimstone',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://vlrnt.hubermjonathan.com/brimstone')
        embed.add_field(name='**Q - Incendiary**',
            value='EQUIP an incendiary grenade launcher. FIRE to launch a grenade that detonates as it comes to a rest on the floor, creating a lingering fire zone that damages players within the zone.',
            inline=False
        )
        embed.add_field(name='**E - Sky Smoke**',
            value='EQUIP a tactical map. FIRE to set locations where Brimstone’s smoke clouds will land. ALTERNATE FIRE to confirm, launching long-lasting smoke clouds that block vision in the selected area.',
            inline=False
        )
        embed.add_field(name='**C - Stim Beacon**',
            value='EQUIP a stim beacon. FIRE to toss the stim beacon in front of Brimstone. Upon landing, the stim beacon will create a field that grants players RapidFire.',
            inline=False
        )
        embed.add_field(name='**X - Orbital Strike**',
            value='EQUIP a tactical map. FIRE to launch a lingering orbital strike laser at the selected location, dealing high damage-over-time to players caught in the selected area.',
            inline=False
        )
        embed.add_field(name='**Ability Videos**',
            value='To view videos of Brimstone\'s abilities visit https://playvalorant.com/en-us/agents/brimstone/',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @agents.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def phoenix(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Phoenix',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://vlrnt.hubermjonathan.com/phoenix')
        embed.add_field(name='**Q - Curveball**',
            value='EQUIP a flare orb that takes a curving path and detonates shortly after throwing. FIRE to curve the flare orb to the left, detonating and blinding any player who sees the orb. ALTERNATE FIRE to curve the flare orb to the right.',
            inline=False
        )
        embed.add_field(name='**E - Hot Hands**',
            value='EQUIP a fireball. FIRE to throw a fireball that explodes after a set amount of time or upon hitting the ground, creating a lingering fire zone that damages enemies.',
            inline=False
        )
        embed.add_field(name='**C - Blaze**',
            value='EQUIP a flame wall. FIRE to create a line of flame that moves forward, creating a wall of fire that blocks vision and damages players passing through it. HOLD FIRE to bend the wall in the direction of your crosshair.',
            inline=False
        )
        embed.add_field(name='**X - Run It Back**',
            value='INSTANTLY place a marker at Phoenix’s location. While this ability is active, dying or allowing the timer to expire will end this ability and bring Phoenix back to this location with full health.',
            inline=False
        )
        embed.add_field(name='**Ability Videos**',
            value='To view videos of Phoenix\'s abilities visit https://playvalorant.com/en-us/agents/phoenix/',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @agents.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def sage(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Sage',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://vlrnt.hubermjonathan.com/sage')
        embed.add_field(name='**Q - Slow Orb**',
            value='EQUIP a slowing orb. FIRE to throw a slowing orb forward that detonates upon landing, creating a lingering field that slows players caught inside of it.',
            inline=False
        )
        embed.add_field(name='**E - Healing Orb**',
            value='EQUIP a healing orb. FIRE with your crosshairs over a damaged ally to activate a heal-over-time on them. ALT FIRE while Sage is damaged to activate a self heal-over-time.',
            inline=False
        )
        embed.add_field(name='**C - Barrier Orb**',
            value='EQUIP a barrier orb. FIRE places a solid wall. ALT FIRE rotates the targeter.',
            inline=False
        )
        embed.add_field(name='**X - Ressurection**',
            value='EQUIP a resurrection ability. FIRE with your crosshairs placed over a dead ally to begin resurrecting them. After a brief channel, the ally will be brought back to life with full health.',
            inline=False
        )
        embed.add_field(name='**Ability Videos**',
            value='To view videos of Sage\'s abilities visit https://playvalorant.com/en-us/agents/sage/',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @agents.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def sova(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Sova',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://vlrnt.hubermjonathan.com/sova')
        embed.add_field(name='**Q - Shock Bolt**',
            value='EQUIP a bow with a shock bolt. FIRE to send the explosive forward, detonating upon collision and damaging players nearby. HOLD FIRE to extend the range of the projectile. ALTERNATE FIRE to add up to two bounces to this arrow.',
            inline=False
        )
        embed.add_field(name='**E - Recon Bolt**',
            value='EQUIP a bow with a recon bolt. FIRE to send the recon bolt forward, activating upon collision and revealing the location of nearby enemies caught in the line of sight of the bolt. HOLD FIRE to extend the range of the projectile. ALTERNATE FIRE to add up to two bounces to this arrow.',
            inline=False
        )
        embed.add_field(name='**C - Owl Drone**',
            value='EQUIP an owl drone. FIRE to deploy and take control of movement of the drone. While in control of the drone, FIRE to shoot a marking dart. This dart will reveal the location of any player struck by the dart.',
            inline=False
        )
        embed.add_field(name='**X - Hunter\'s Fury**',
            value='EQUIP a bow with three long-range wall-piercing energy blasts. FIRE to release an energy blast in a line in front of Sova, dealing damage and revealing the location of enemies caught in the line. This ability can be RE-USED up to two more times while the ability timer is active.',
            inline=False
        )
        embed.add_field(name='**Ability Videos**',
            value='To view videos of Sova\'s abilities visit https://playvalorant.com/en-us/agents/sova/',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @agents.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def viper(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Viper',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://vlrnt.hubermjonathan.com/viper')
        embed.add_field(name='**Q - Poison Cloud**',
            value='EQUIP a gas emitter. FIRE to throw the emitter that perpetually remains throughout the round. RE-USE the ability to create a toxic gas cloud at the cost of fuel. This ability can be RE-USED more than once and can be picked up to be REDEPLOYED.',
            inline=False
        )
        embed.add_field(name='**E - Toxic Screen**',
            value='EQUIP a gas emitter launcher. FIRE to deploy a long line of gas emitters. RE-USE the ability to create a tall wall of toxic gas at the cost of fuel. This ability can be RE-USED more than once.',
            inline=False
        )
        embed.add_field(name='**C - Snake Bite**',
            value='EQUIP a chemical launcher. FIRE to launch a canister that shatters upon hitting the floor, creating a lingering chemical zone that damages and slows enemies.',
            inline=False
        )
        embed.add_field(name='**X - Viper\'s Pit**',
            value='EQUIP a chemical sprayer. FIRE to spray a chemical cloud in all directions around Viper, creating a large cloud that reduces the vision range and maximum health of players inside of it.',
            inline=False
        )
        embed.add_field(name='**Ability Videos**',
            value='To view videos of Viper\'s abilities visit https://playvalorant.com/en-us/agents/viper/',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @agents.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def cypher(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Cypher',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://vlrnt.hubermjonathan.com/cypher')
        embed.add_field(name='**Q - Cyber Cage**',
            value='INSTANTLY toss the cyber cage in front of Cypher. Activate to create a zone that blocks vision and slows enemies who pass through it.',
            inline=False
        )
        embed.add_field(name='**E - Spycam**',
            value='EQUIP a spycam. FIRE to place the spycam at the targeted location. RE-USE this ability to take control of the camera’s view. While in control of the camera, FIRE to shoot a marking dart. This dart will reveal the location of any player struck by the dart.',
            inline=False
        )
        embed.add_field(name='**C - Trapwire**',
            value='EQUIP a trapwire. FIRE to place a destructible and covert tripwire at the targeted location creating a line that spans between the placed location and the wall opposite. Enemy players who cross a tripwire will be tethered, revealed, and dazed after a short period if they do not destroy the device in time. This ability can be picked up to be REDEPLOYED.',
            inline=False
        )
        embed.add_field(name='**X - Nueral Theft**',
            value='INSTANTLY use on a dead enemy player in your crosshairs to reveal the location of all living enemy players.',
            inline=False
        )
        embed.add_field(name='**Ability Videos**',
            value='To view videos of Cypher\'s abilities visit https://playvalorant.com/en-us/agents/cypher/',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)

    @agents.command()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def reyna(self, ctx):
        # create the embed
        embed = discord.Embed(
            title='Reyna',
            color=globals.embed_color
        )
        embed.set_thumbnail(url='http://vlrnt.hubermjonathan.com/reyna')
        embed.add_field(name='**Q - Devour**',
            value='Enemies killed by Reyna leave behind Soul Orbs that last 3 seconds. INSTANTLY consume a nearby soul orb, rapidly healing for a short duration. Health gained through this skill exceeding 100 will decay over time. If EMPRESS is active, this skill will automatically cast and not consume the orb.',
            inline=False
        )
        embed.add_field(name='**E - Dismiss**',
            value='INSTANTLY consume a nearby soul orb, becoming intangible for a short duration. If EMPRESS is active, also become invisible.',
            inline=False
        )
        embed.add_field(name='**C - Leer**',
            value='EQUIP an ethereal destructible eye. ACTIVATE to cast the eye a short distance forward. The eye will Nearsight all enemies who look at it.',
            inline=False
        )
        embed.add_field(name='**X - Empress**',
            value='INSTANTLY enter a frenzy, increasing firing speed, equip and reload speed dramatically. Scoring a kill renews the duration.',
            inline=False
        )
        embed.add_field(name='**Ability Videos**',
            value='To view videos of Reyna\'s abilities visit https://playvalorant.com/en-us/agents/reyna/',
            inline=False
        )

        # send the message
        await ctx.send(embed=embed)
