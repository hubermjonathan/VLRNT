package com.hubermjonathan.vlrnt;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.Message;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.entities.MessageEmbed;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;

public class Help extends Feature {
    public Help(MessageReceivedEvent event) {
        super(event);
    }

    public void sendHelpMessage(String command) {
        MessageChannel channel = getEvent().getChannel();
        Message message = getEvent().getMessage();

        if (command == null) {
            EmbedBuilder embedBuilder = new EmbedBuilder();
            embedBuilder.setTitle("Valorant Bot Help");
            embedBuilder.setDescription("Use `!val help {command}` for more information about a specific command.\n[] indicates a required argument and {} indicates an optional one. Do not include these in the commands.");
            embedBuilder.addField(
                    "**Available Commands**",
                    "Help messages - `help {command}`\nLatest patch notes - `notes`\nTier list - `tiers {vote [agent] [agent] [agent]}`\nAgent information - `agents [agent]`\nSova arrows - `arrows [map]`",
                    false
            );
            embedBuilder.addField(
                    "**Owner**",
                    "Add **Huberrrr#2959** on Discord to get help with the bot, ask questions, or request features!",
                    false
            );
            embedBuilder.setFooter(Constants.VERSION_NUMBER);
            embedBuilder.setColor(Constants.EMBED_COLOR);
            channel.sendMessage(embedBuilder.build()).queue();
            return;
        }

        switch (command.toLowerCase()) {
            case ("notes"):
                channel.sendMessage(getNotesEmbed()).queue();
                break;
            case ("tiers"):
                channel.sendMessage(getTiersEmbed()).queue();
                break;
            case ("agents"):
                channel.sendMessage(getAgentsEmbed()).queue();
                break;
            case ("arrows"):
                channel.sendMessage(getArrowsEmbed()).queue();
                break;
            default:
                message.addReaction(Constants.DENY).queue();
        }
    }

    public MessageEmbed getNotesEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Valorant Bot Help");
        embedBuilder.setDescription("`notes`");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/icon");
        embedBuilder.addField(
                "**Aliases**",
                "n, pn",
                false
        );
        embedBuilder.addField(
                "**Arguments**",
                "**notes** [Required] - Command group",
                false
        );
        embedBuilder.addField(
                "**Description**",
                "Get the latest patch notes for VALORANT.",
                false
        );
        embedBuilder.setFooter(Constants.VERSION_NUMBER);
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getTiersEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Valorant Bot Help");
        embedBuilder.setDescription("`tiers {vote [agent] [agent] [agent]}`");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/icon");
        embedBuilder.addField(
                "**Aliases**",
                "tl",
                false
        );
        embedBuilder.addField(
                "**Arguments**",
                "**tiers** [Required] - Command group\n**vote** {Optional} - Subcommand group\n**agent** [Required if **vote** is specified] - Agent name to vote for",
                false
        );
        embedBuilder.addField(
                "**Description**",
                "View and vote on a community tier list of agents.",
                false
        );
        embedBuilder.setFooter(Constants.VERSION_NUMBER);
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getAgentsEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Valorant Bot Help");
        embedBuilder.setDescription("`agents [agent]`");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/icon");
        embedBuilder.addField(
                "**Aliases**",
                "None",
                false
        );
        embedBuilder.addField(
                "**Arguments**",
                "**agents** [Required] - Command group\n**agent** [Required] - The agent to get information for",
                false
        );
        embedBuilder.addField(
                "**Description**",
                "Learn about the agents of VALORANT.",
                false
        );
        embedBuilder.setFooter(Constants.VERSION_NUMBER);
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getArrowsEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Valorant Bot Help");
        embedBuilder.setDescription("`arrows [map]`");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/icon");
        embedBuilder.addField(
                "**Aliases**",
                "arw",
                false
        );
        embedBuilder.addField(
                "**Arguments**",
                "**arrows** [Required] - Command group\n**map** [Required] - The map name to get Sova arrows for",
                false
        );
        embedBuilder.addField(
                "**Description**",
                "Get locations and lineups for Sova arrows.",
                false
        );
        embedBuilder.setFooter(Constants.VERSION_NUMBER);
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }
}
