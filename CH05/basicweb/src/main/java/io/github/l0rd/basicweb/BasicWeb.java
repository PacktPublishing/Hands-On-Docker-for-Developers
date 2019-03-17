package io.github.l0rd.basicweb;

public class BasicWeb {

    private final long id;
    private final String content;

    public BasicWeb(long id, String content) {
        this.id = id;
        this.content = content;
    }

    public long getId() {
        return id;
    }

    public String getContent() {
        return content;
    }
}