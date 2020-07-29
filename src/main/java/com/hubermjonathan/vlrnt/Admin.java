package com.hubermjonathan.vlrnt;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.Guild;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;

public class Admin extends Feature {
    public Admin(MessageReceivedEvent event) {
        super(event);
    }

    public void sendStatsMessage() {
        int numberOfGuilds = getEvent().getJDA().getGuilds().size();
        int numberOfUsers = 0;
        for (Guild g : getEvent().getJDA().getGuilds()) {
            numberOfUsers += g.getMemberCount();
        }

        MessageChannel channel = getEvent().getChannel();
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Stats");
        embedBuilder.setDescription(String.format("**Number of guilds:** %d\n**Number of members:** %d", numberOfGuilds, numberOfUsers));
        embedBuilder.setColor(Constants.EMBED_COLOR);
        channel.sendMessage(embedBuilder.build()).queue();
    }
}
