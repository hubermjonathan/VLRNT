package com.hubermjonathan.vlrnt;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.Message;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.entities.MessageEmbed;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;

public class Arrows extends Feature {
    public Arrows(MessageReceivedEvent event) {
        super(event);
    }

    public void sendArrowMessage(String map) {
        MessageChannel channel = getEvent().getChannel();
        Message message = getEvent().getMessage();

        if (map == null) {
            EmbedBuilder embedBuilder = new EmbedBuilder();
            embedBuilder.setTitle("Which map?");
            embedBuilder.setDescription("Use `val! arrows [map_name]` to choose a map from the following.");
            embedBuilder.addField("**Maps**", "Bind, Haven, Split, Ascent", false);
            embedBuilder.setColor(Constants.EMBED_COLOR);
            channel.sendMessage(embedBuilder.build()).queue();
            return;
        }

        switch (map.toLowerCase()) {
            case ("bind"):
                channel.sendMessage(getBindEmbed()).queue();
                break;
            case ("haven"):
                channel.sendMessage(getHavenEmbed()).queue();
                break;
            case ("split"):
                channel.sendMessage(getSplitEmbed()).queue();
                break;
            case ("ascent"):
                channel.sendMessage(getAscentEmbed()).queue();
                break;
            default:
                message.addReaction(Constants.DENY).queue();
        }
    }

    public MessageEmbed getBindEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Sova Arrows for Bind");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/sova");
        embedBuilder.addField(
                "**Coming Soon**",
                "The bot owner is currently gathering arrow locations and will update this feature soon.",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getHavenEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Sova Arrows for Haven");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/sova");
        embedBuilder.addField(
                "**Coming Soon**",
                "The bot owner is currently gathering arrow locations and will update this feature soon.",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getSplitEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Sova Arrows for Split");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/sova");
        embedBuilder.addField(
                "**Coming Soon**",
                "The bot owner is currently gathering arrow locations and will update this feature soon.",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }

    public MessageEmbed getAscentEmbed() {
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Sova Arrows for Ascent");
        embedBuilder.setThumbnail("http://vlrnt.hubermjonathan.com/sova");
        embedBuilder.addField(
                "**Coming Soon**",
                "The bot owner is currently gathering arrow locations and will update this feature soon.",
                false
        );
        embedBuilder.setColor(Constants.EMBED_COLOR);
        return embedBuilder.build();
    }
}
