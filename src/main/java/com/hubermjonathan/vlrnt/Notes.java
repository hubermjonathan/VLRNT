package com.hubermjonathan.vlrnt;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;

public class Notes extends Feature {
    public Notes(MessageReceivedEvent event) {
        super(event);
    }

    public void sendNotesMessage() {
        Document doc = null;
        String notesUrl = null;
        String highlightsUrl = null;
        try {
            doc = Jsoup.connect("https://playvalorant.com/en-us/news").get();
            Elements headlines = doc.select("a");
            for (Element headline : headlines) {
                if (headline.absUrl("href").contains("game-updates/valorant-patch-note") && !headline.parent().hasClass("news-card")) {
                    notesUrl = headline.absUrl("href");
                    break;
                }
            }

            doc = Jsoup.connect(notesUrl).get();
            Elements images = doc.select("img");
            for (Element image : images) {
                if (image.absUrl("src").contains("Patch_Notes")) {
                    highlightsUrl = image.absUrl("src");
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        MessageChannel channel = getEvent().getChannel();
        EmbedBuilder embedBuilder = new EmbedBuilder();
        embedBuilder.setTitle("Here are the latest patch notes!", notesUrl);
        embedBuilder.setDescription(doc.title());
        if (highlightsUrl != null) embedBuilder.setImage(highlightsUrl);
        embedBuilder.setColor(Constants.EMBED_COLOR);
        channel.sendMessage(embedBuilder.build()).queue();
    }
}
