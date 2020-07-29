package com.hubermjonathan.vlrnt;

import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;

import javax.security.auth.login.LoginException;

public class VLRNT {
    public static void main(String[] args) throws LoginException, InterruptedException {
        JDA jda = JDABuilder.createDefault(System.getenv("TOKEN")).build();
        jda.awaitReady();
        jda.addEventListener(new Dispatcher());
    }
}
