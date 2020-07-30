package com.hubermjonathan.vlrnt;

import net.dv8tion.jda.api.entities.Message;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import javax.annotation.Nonnull;
import java.util.Arrays;

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
        Help help = new Help(event);
        Tiers tiers = new Tiers(event);
        Notes notes = new Notes(event);

        switch (tokens[1]) {
            case ("stats"):
                if (!event.getAuthor().getId().equals("196141424318611457")) return;
                admin.sendStatsMessage();
                break;
            case ("agents"):
                agents.sendAgentMessage(tokens.length > 2 ? tokens[2] : null);
                break;
            case ("arrows"):
            case ("arw"):
                arrows.sendArrowMessage(tokens.length > 2 ? tokens[2] : null);
                break;
            case ("help"):
                help.sendHelpMessage(tokens.length > 2 ? tokens[2] : null);
                break;
            case ("tiers"):
            case ("tl"):
                tiers.handleTiersCommand(tokens.length > 2 ? tokens[2] : null, tokens.length > 3 ? Arrays.copyOfRange(tokens, 3, tokens.length) : null);
                break;
            case ("notes"):
            case ("n"):
            case ("pn"):
                notes.sendNotesMessage();
                break;
            default:
                message.addReaction(Constants.NO_COMMAND).queue();
        }
    }
}
