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
        Agents agents = new Agents(event);
        Arrows arrows = new Arrows(event);

        switch (tokens[1]) {
            case ("stats"):
                admin.sendStatsMessage();
                break;
            case ("agents"):
                agents.sendAgentMessage(tokens.length > 2 ? tokens[2] : null);
                break;
            case ("arrows"):
                arrows.sendArrowMessage(tokens.length > 2 ? tokens[2] : null);
                break;
            default:
                message.addReaction(Constants.NO_COMMAND).queue();
        }
    }
}
