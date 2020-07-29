package com.hubermjonathan.vlrnt;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.Message;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.entities.MessageEmbed;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;

public class Agents extends Feature {
    public Agents(MessageReceivedEvent event) {
        super(event);
    }

    public void sendAgentMessage(String agent) {
        MessageChannel channel = getEvent().getChannel();
        Message message = getEvent().getMessage();

        if (agent == null) {
            EmbedBuilder embedBuilder = new EmbedBuilder();
            embedBuilder.setTitle("Which agent would you like to learn about?");
            embedBuilder.setDescription("Use `!val agents [agent_name]` to choose an agent from the following.");
            embedBuilder.addField("**Agents**", "Jett, Raze, Breach, Omen, Brimstone, Phoenix, Sage, Sova, Viper, Cypher, Reyna", false);
            embedBuilder.setColor(Constants.EMBED_COLOR);
            channel.sendMessage(embedBuilder.build()).queue();
            return;
        }

        switch (agent.toLowerCase()) {
            case ("jett"):
                channel.sendMessage(getJettEmbed()).queue();
                break;
            case ("raze"):
                channel.sendMessage(getRazeEmbed()).queue();
                break;
            case ("breach"):
                channel.sendMessage(getBreachEmbed()).queue();
                break;
            case ("omen"):
                channel.sendMessage(getOmenEmbed()).queue();
                break;
            case ("brimstone"):
                channel.sendMessage(getBrimstoneEmbed()).queue();
                break;
            case ("phoenix"):
                channel.sendMessage(getPhoenixEmbed()).queue();
                break;
            case ("sage"):
                channel.sendMessage(getSageEmbed()).queue();
                break;
            case ("sova"):
                channel.sendMessage(getSovaEmbed()).queue();
                break;
            case ("viper"):
                channel.sendMessage(getViperEmbed()).queue();
                break;
            case ("cypher"):
                channel.sendMessage(getCypherEmbed()).queue();
                break;
            case ("reyna"):
                channel.sendMessage(getReynaEmbed()).queue();
                break;
            default:
                message.addReaction(Constants.DENY).queue();
        }
    }

    public MessageEmbed getJettEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Jett");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/jett");
        embedBuilder.addField(
                "**Q - Updraft**",
                "INSTANTLY propel Jett high into the air.",
                false
        );
        embedBuilder.addField(
                "**E - Tailwind**",
                "INSTANTLY propel Jett in the direction she is moving. If Jett is standing still, she will propel forward.",
                false
        );
        embedBuilder.addField(
                "**C - Cloudburst**",
                "INSTANTLY throw a projectile that expands into a brief vision-blocking cloud on impact with a surface. HOLD the ability key to curve the smoke in the direction of your crosshair.",
                false
        );
        embedBuilder.addField(
                "**X - Blade Storm**",
                "EQUIP a set of highly accurate knives that recharge on killing an opponent. FIRE to throw a single knife at your target. ALTERNATE FIRE to throw all remaining daggers at your target.",
                false
        );
        embedBuilder.addField(
                "**Ability Videos**",
                "To view videos of Jett's abilities visit https://playvalorant.com/en-us/agents/jett/",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getRazeEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Raze");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/raze");
        embedBuilder.addField(
                "**Q - Blast Pack**",
                "INSTANTLY throw a Blast Pack that will stick to surfaces. RE-USE the ability after deployment to detonate, damaging and moving anything hit. Raze isn\\'t damaged by this ability, but will still take fall damage if launched up far enough.",
                false
        );
        embedBuilder.addField(
                "**E - Paint Shells**",
                "EQUIP a cluster grenade. FIRE to throw the grenade, which does damage and creates sub-munitions, each doing damage to anyone in their range.",
                false
        );
        embedBuilder.addField(
                "**C - Boom Bot**",
                "EQUIP a Boom Bot. FIRE will deploy the bot, causing it to travel in a straight line on the ground, bouncing off walls. The Boom Bot will lock on to any enemies in its frontal cone and chase them, exploding for heavy damage if it reaches them.",
                false
        );
        embedBuilder.addField(
                "**X - Showstopper**",
                "EQUIP a rocket launcher. FIRE shoots a rocket that does massive area damage on contact with anything.",
                false
        );
        embedBuilder.addField(
                "**Ability Videos**",
                "To view videos of Raze's abilities visit https://playvalorant.com/en-us/agents/raze/",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getBreachEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Breach");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/breach");
        embedBuilder.addField(
                "**Q - Flashpoint**",
                "EQUIP a blinding charge. FIRE the charge to set fast-acting burst through the wall. The charge detonates to blind all players looking at it.",
                false
        );
        embedBuilder.addField(
                "**E - Fault Line**",
                "EQUIP a seismic blast. HOLD FIRE to increase the distance. RELEASE to set off the quake, danzing all players in its zone and in a line up to the zone.",
                false
        );
        embedBuilder.addField(
                "**C - Aftershock**",
                "EQUIP a fusion charge. FIRE the charge to set a slow-acting burst through the wall. The burst does heavy damage to anyone caught in its area.",
                false
        );
        embedBuilder.addField(
                "**X - Rolling Thunder**",
                "EQUIP a seismic charge. FIRE to send a cascading quake through all terrain in a large cone. The quake dazes and knocks up anyone caught in it.",
                false
        );
        embedBuilder.addField(
                "**Ability Videos**",
                "To view videos of Breach's abilities visit https://playvalorant.com/en-us/agents/breach/",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getOmenEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Omen");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/omen");
        embedBuilder.addField(
                "**Q - Paranoia**",
                "INSTANTLY fire a shadow projectile forward, briefly reducing the vision range of all players it touches. This projectile can pass straight through walls.",
                false
        );
        embedBuilder.addField(
                "**E - Dark Cover**",
                "EQUIP a shadow orb and see its range indicator. FIRE to throw the shadow orb to the marked location, creating a long-lasting shadow sphere that blocks vision. HOLD ALTERNATE FIRE while targeting to move the marker further away. HOLD the ability key with targeting to move the market closer.",
                false
        );
        embedBuilder.addField(
                "**C - Shrouded Step**",
                "EQUIP a shadow walk ability and see its range indicator. FIRE to begin a brief channel, then teleport to the marked location.",
                false
        );
        embedBuilder.addField(
                "**X - From The Shadows**",
                "EQUIP a tactical map. FIRE to begin teleporting to the selected location. While teleporting, Omen will appear as a Shade that can be destroyed by an enemy to cancel his teleport.",
                false
        );
        embedBuilder.addField(
                "**Ability Videos**",
                "To view videos of Omen's abilities visit https://playvalorant.com/en-us/agents/omen/",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getBrimstoneEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Brimstone");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/brimstone");
        embedBuilder.addField(
                "**Q - Incendiary**",
                "EQUIP an incendiary grenade launcher. FIRE to launch a grenade that detonates as it comes to a rest on the floor, creating a lingering fire zone that damages players within the zone.",
                false
        );
        embedBuilder.addField(
                "**E - Sky Smoke**",
                "EQUIP a tactical map. FIRE to set locations where Brimstone’s smoke clouds will land. ALTERNATE FIRE to confirm, launching long-lasting smoke clouds that block vision in the selected area.",
                false
        );
        embedBuilder.addField(
                "**C - Stim Beacon**",
                "EQUIP a stim beacon. FIRE to toss the stim beacon in front of Brimstone. Upon landing, the stim beacon will create a field that grants players RapidFire.",
                false
        );
        embedBuilder.addField(
                "**X - Orbital Strike**",
                "EQUIP a tactical map. FIRE to launch a lingering orbital strike laser at the selected location, dealing high damage-over-time to players caught in the selected area.",
                false
        );
        embedBuilder.addField(
                "**Ability Videos**",
                "To view videos of Brimstone's abilities visit https://playvalorant.com/en-us/agents/brimstone/",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getPhoenixEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Phoenix");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/phoenix");
        embedBuilder.addField(
                "**Q - Curveball**",
                "EQUIP a flare orb that takes a curving path and detonates shortly after throwing. FIRE to curve the flare orb to the left, detonating and blinding any player who sees the orb. ALTERNATE FIRE to curve the flare orb to the right.",
                false
        );
        embedBuilder.addField(
                "**E - Hot Hands**",
                "EQUIP a fireball. FIRE to throw a fireball that explodes after a set amount of time or upon hitting the ground, creating a lingering fire zone that damages enemies.",
                false
        );
        embedBuilder.addField(
                "**C - Blaze**",
                "EQUIP a flame wall. FIRE to create a line of flame that moves forward, creating a wall of fire that blocks vision and damages players passing through it. HOLD FIRE to bend the wall in the direction of your crosshair.",
                false
        );
        embedBuilder.addField(
                "**X - Run It Back**",
                "INSTANTLY place a marker at Phoenix’s location. While this ability is active, dying or allowing the timer to expire will end this ability and bring Phoenix back to this location with full health.",
                false
        );
        embedBuilder.addField(
                "**Ability Videos**",
                "To view videos of Phoenix's abilities visit https://playvalorant.com/en-us/agents/phoenix/",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getSageEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Sage");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/sage");
        embedBuilder.addField(
                "**Q - Slow Orb**",
                "EQUIP a slowing orb. FIRE to throw a slowing orb forward that detonates upon landing, creating a lingering field that slows players caught inside of it.",
                false
        );
        embedBuilder.addField(
                "**E - Healing Orb**",
                "EQUIP a healing orb. FIRE with your crosshairs over a damaged ally to activate a heal-over-time on them. ALT FIRE while Sage is damaged to activate a self heal-over-time.",
                false
        );
        embedBuilder.addField(
                "**C - Barrier Orb**",
                "EQUIP a barrier orb. FIRE places a solid wall. ALT FIRE rotates the targeter.",
                false
        );
        embedBuilder.addField(
                "**X - Ressurection**",
                "EQUIP a resurrection ability. FIRE with your crosshairs placed over a dead ally to begin resurrecting them. After a brief channel, the ally will be brought back to life with full health.",
                false
        );
        embedBuilder.addField(
                "**Ability Videos**",
                "To view videos of Sage's abilities visit https://playvalorant.com/en-us/agents/sage/",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getSovaEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Sova");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/sova");
        embedBuilder.addField(
                "**Q - Shock Bolt**",
                "EQUIP a bow with a shock bolt. FIRE to send the explosive forward, detonating upon collision and damaging players nearby. HOLD FIRE to extend the range of the projectile. ALTERNATE FIRE to add up to two bounces to this arrow.",
                false
        );
        embedBuilder.addField(
                "**E - Recon Bolt**",
                "EQUIP a bow with a recon bolt. FIRE to send the recon bolt forward, activating upon collision and revealing the location of nearby enemies caught in the line of sight of the bolt. HOLD FIRE to extend the range of the projectile. ALTERNATE FIRE to add up to two bounces to this arrow.",
                false
        );
        embedBuilder.addField(
                "**C - Owl Drone**",
                "EQUIP an owl drone. FIRE to deploy and take control of movement of the drone. While in control of the drone, FIRE to shoot a marking dart. This dart will reveal the location of any player struck by the dart.",
                false
        );
        embedBuilder.addField(
                "**X - Hunter's Fury**",
                "EQUIP a bow with three long-range wall-piercing energy blasts. FIRE to release an energy blast in a line in front of Sova, dealing damage and revealing the location of enemies caught in the line. This ability can be RE-USED up to two more times while the ability timer is active.",
                false
        );
        embedBuilder.addField(
                "**Ability Videos**",
                "To view videos of Sova's abilities visit https://playvalorant.com/en-us/agents/sova/",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getViperEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Viper");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/viper");
        embedBuilder.addField(
                "**Q - Poison Cloud**",
                "EQUIP a gas emitter. FIRE to throw the emitter that perpetually remains throughout the round. RE-USE the ability to create a toxic gas cloud at the cost of fuel. This ability can be RE-USED more than once and can be picked up to be REDEPLOYED.",
                false
        );
        embedBuilder.addField(
                "**E - Toxic Screen**",
                "EQUIP a gas emitter launcher. FIRE to deploy a long line of gas emitters. RE-USE the ability to create a tall wall of toxic gas at the cost of fuel. This ability can be RE-USED more than once.",
                false
        );
        embedBuilder.addField(
                "**C - Snake Bite**",
                "EQUIP a chemical launcher. FIRE to launch a canister that shatters upon hitting the floor, creating a lingering chemical zone that damages and slows enemies.",
                false
        );
        embedBuilder.addField(
                "**X - Viper's Pit**",
                "EQUIP a chemical sprayer. FIRE to spray a chemical cloud in all directions around Viper, creating a large cloud that reduces the vision range and maximum health of players inside of it.",
                false
        );
        embedBuilder.addField(
                "**Ability Videos**",
                "To view videos of Viper's abilities visit https://playvalorant.com/en-us/agents/viper/",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getCypherEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Cypher");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/cypher");
        embedBuilder.addField(
                "**Q - Cyber Cage**",
                "INSTANTLY toss the cyber cage in front of Cypher. Activate to create a zone that blocks vision and slows enemies who pass through it.",
                false
        );
        embedBuilder.addField(
                "**E - Spycam**",
                "EQUIP a spycam. FIRE to place the spycam at the targeted location. RE-USE this ability to take control of the camera’s view. While in control of the camera, FIRE to shoot a marking dart. This dart will reveal the location of any player struck by the dart.",
                false
        );
        embedBuilder.addField(
                "**C - Trapwire**",
                "EQUIP a trapwire. FIRE to place a destructible and covert tripwire at the targeted location creating a line that spans between the placed location and the wall opposite. Enemy players who cross a tripwire will be tethered, revealed, and dazed after a short period if they do not destroy the device in time. This ability can be picked up to be REDEPLOYED.",
                false
        );
        embedBuilder.addField(
                "**X - Nueral Theft**",
                "INSTANTLY use on a dead enemy player in your crosshairs to reveal the location of all living enemy players.",
                false
        );
        embedBuilder.addField(
                "**Ability Videos**",
                "To view videos of Cypher's abilities visit https://playvalorant.com/en-us/agents/cypher/",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getReynaEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Reyna");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/reyna");
        embedBuilder.addField(
                "**Q - Devour**",
                "Enemies killed by Reyna leave behind Soul Orbs that last 3 seconds. INSTANTLY consume a nearby soul orb, rapidly healing for a short duration. Health gained through this skill exceeding 100 will decay over time. If EMPRESS is active, this skill will automatically cast and not consume the orb.",
                false
        );
        embedBuilder.addField(
                "**E - Dismiss**",
                "INSTANTLY consume a nearby soul orb, becoming intangible for a short duration. If EMPRESS is active, also become invisible.",
                false
        );
        embedBuilder.addField(
                "**C - Leer**",
                "EQUIP an ethereal destructible eye. ACTIVATE to cast the eye a short distance forward. The eye will Nearsight all enemies who look at it.",
                false
        );
        embedBuilder.addField(
                "**X - Empress**",
                "INSTANTLY enter a frenzy, increasing firing speed, equip and reload speed dramatically. Scoring a kill renews the duration.",
                false
        );
        embedBuilder.addField(
                "**Ability Videos**",
                "To view videos of Reyna's abilities visit https://playvalorant.com/en-us/agents/reyna/",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }
}
