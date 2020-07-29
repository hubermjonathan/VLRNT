package com.hubermjonathan.vlrnt;

import net.dv8tion.jda.api.entities.Message;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import javax.annotation.Nonnull;

public class Dispatcher extends ListenerAdapter {
    @Override
    public void onMessageReceived(@Nonnull MessageReceivedEvent event) {
        Message message = event.getMessage();
        String content = message.getContentRaw();
        String[] tokens = content.split(" ");

        if (event.getAuthor().isBot() || message.getMentions().size() > 1) return;
        if (!tokens[0].equals("!val")) return;

        Admin admin = new Admin(event);

        switch (tokens[1]) {
            case ("stats"):
                admin.sendStatsMessage();
                break;
            default:
                message.addReaction(Constants.NO_COMMAND).queue();
        }
    }
}
