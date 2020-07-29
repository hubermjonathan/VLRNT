package com.hubermjonathan.vlrnt;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.Message;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import redis.clients.jedis.Jedis;

import java.util.Arrays;
import java.util.List;

public class Tiers extends Feature {
    Jedis jedis;

    public Tiers(MessageReceivedEvent event) {
        super(event);
        this.jedis = new Jedis(Constants.REDIS_URL);
    }

    public void handleTiersCommand(String command, String[] agents) {
        Message message = getEvent().getMessage();

        if (command == null) {
            sendTierList();
            return;
        }

        switch (command.toLowerCase()) {
            case ("reset"):
                if (!getEvent().getAuthor().getId().equals("196141424318611457")) return;
                resetTierList();
                break;
            case ("vote"):
                if (agents == null) {
                    sendVoteMessage();
                    return;
                }

                castVote(agents);
                break;
            default:
                message.addReaction(Constants.DENY).queue();
        }
    }

    public void resetTierList() {
        jedis.set("jett", "0");
        jedis.set("raze", "0");
        jedis.set("breach", "0");
        jedis.set("omen", "0");
        jedis.set("brimstone", "0");
        jedis.set("phoenix", "0");
        jedis.set("sage", "0");
        jedis.set("sova", "0");
        jedis.set("viper", "0");
        jedis.set("cypher", "0");
        jedis.set("reyna", "0");

        MessageChannel channel = getEvent().getChannel();
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Community Tier List");
        embedBuilder.setDescription("The community tier list has been reset.");
        embedBuilder.setColor(Constants.EMBED_COLOR);
        channel.sendMessage(embedBuilder.build()).queue();
    }

    public void sendTierList() {
        String[] agents = { "Jett", "Raze", "Breach", "Omen", "Brimstone", "Phoenix", "Sage", "Sova", "Viper", "Cypher", "Reyna" };
        int[] votes = {
                Integer.parseInt(jedis.get("jett")),
                Integer.parseInt(jedis.get("raze")),
                Integer.parseInt(jedis.get("breach")),
                Integer.parseInt(jedis.get("omen")),
                Integer.parseInt(jedis.get("brimstone")),
                Integer.parseInt(jedis.get("phoenix")),
                Integer.parseInt(jedis.get("sage")),
                Integer.parseInt(jedis.get("sova")),
                Integer.parseInt(jedis.get("viper")),
                Integer.parseInt(jedis.get("cypher")),
                Integer.parseInt(jedis.get("reyna"))
        };

        for (int i = 0; i < votes.length; i++) {
            for (int j = i + 1; j < votes.length; j++) {
                if (votes[i] < votes[j]) {
                    int tempVote = votes[i];
                    votes[i] = votes[j];
                    votes[j] = tempVote;

                    String tempAgent = agents[i];
                    agents[i] = agents[j];
                    agents[j] = tempAgent;
                }
            }
        }

        String rankings = "";
        for (int i = 0; i < agents.length; i++) {
            rankings = rankings.concat(String.format("**%d:** %s (%d)\n", i + 1, agents[i], votes[i]));
        }

        MessageChannel channel = getEvent().getChannel();
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Community Tier List");
        embedBuilder.setDescription("To submit your vote, use `!val tiers vote`.");
        embedBuilder.setThumbnail(String.format("http://vlrnt.hubermjonathan.com/%s", agents[0].toLowerCase()));
        embedBuilder.addField("**Agents**", rankings,false);
        embedBuilder.setColor(Constants.EMBED_COLOR);
        channel.sendMessage(embedBuilder.build()).queue();
    }

    public void sendVoteMessage() {
        MessageChannel channel = getEvent().getChannel();
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Community Tier List");
        embedBuilder.setDescription("Vote for the 3 agents who you think are the **strongest** using the following format:\n`!val tiers vote [agent_name] [agent_name] [agent_name]`\nDo not include the [] in your command. The first agent listed is your first place and the last one is third place.\nExample: `!val tiers vote Sova Reyna Raze`");
        embedBuilder.setColor(Constants.EMBED_COLOR);
        channel.sendMessage(embedBuilder.build()).queue();
    }

    public void castVote(String[] agents) {
        if (agents.length != 3) {
            Message message = getEvent().getMessage();
            message.addReaction(Constants.DENY).queue();
            return;
        }

        String[] validAgents = { "jett", "raze", "breach", "omen", "brimstone", "phoenix", "sage", "sova", "viper", "cypher", "reyna" };
        List<String> validAgentsList = Arrays.asList(validAgents);
        for (String agent : agents) {
            if (!validAgentsList.contains(agent)) {
                Message message = getEvent().getMessage();
                message.addReaction(Constants.DENY).queue();
                return;
            }
        }

        if (jedis.get(getEvent().getAuthor().getId()) != null) {
            String[] oldVotes = jedis.get(getEvent().getAuthor().getId()).split(" ");
            int newVotes = Integer.parseInt(jedis.get(oldVotes[0].toLowerCase())) - 7;
            jedis.set(oldVotes[0].toLowerCase(), newVotes > 0 ? String.valueOf(newVotes) : "0");
            newVotes = Integer.parseInt(jedis.get(oldVotes[1].toLowerCase())) - 3;
            jedis.set(oldVotes[1].toLowerCase(), newVotes > 0 ? String.valueOf(newVotes) : "0");
            newVotes = Integer.parseInt(jedis.get(oldVotes[2].toLowerCase())) - 1;
            jedis.set(oldVotes[2].toLowerCase(), newVotes > 0 ? String.valueOf(newVotes) : "0");
        }

        jedis.set(agents[0].toLowerCase(), String.valueOf(Integer.parseInt(jedis.get(agents[0].toLowerCase())) + 7));
        jedis.set(agents[1].toLowerCase(), String.valueOf(Integer.parseInt(jedis.get(agents[1].toLowerCase())) + 3));
        jedis.set(agents[2].toLowerCase(), String.valueOf(Integer.parseInt(jedis.get(agents[2].toLowerCase())) + 1));
        String agentsString = String.format("%s %s %s", agents[0], agents[1], agents[2]);
        jedis.set(getEvent().getAuthor().getId(), agentsString);

        MessageChannel channel = getEvent().getChannel();
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Community Tier List");
        embedBuilder.setDescription("Your vote has been cast.");
        embedBuilder.setColor(Constants.EMBED_COLOR);
        channel.sendMessage(embedBuilder.build()).queue();
    }
}
