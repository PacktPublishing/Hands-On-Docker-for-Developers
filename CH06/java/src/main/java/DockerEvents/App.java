package DockerEvents;
import com.google.common.collect.ImmutableMap;
import com.spotify.docker.client.DockerClient;
import com.spotify.docker.client.DockerClient.ListContainersParam;
import com.spotify.docker.client.messages.Event;
import com.spotify.docker.client.EventStream;
import com.spotify.docker.client.exceptions.DockerCertificateException;
import com.spotify.docker.client.exceptions.DockerException;
import com.spotify.docker.client.messages.Container;

import com.spotify.docker.client.messages.Event.Actor;
import java.util.List;

import com.spotify.docker.client.DefaultDockerClient;

public final class App {
    private App() {
    }

    /**
     * @throws DockerCertificateException
     * @throws InterruptedException
     * @throws DockerException
     */
    public static void main(String[] args) throws DockerCertificateException, DockerException, InterruptedException {
        final DockerClient docker = DefaultDockerClient.fromEnv().build();
        final EventStream eventStream = docker.events();

        Event event = eventStream.next();
        System.out.printf("EVENT TIME: %s\n", event.time());
        System.out.printf("EVENT ACTION: %s\n", event.action());
        System.out.printf("EVENT TYPE: %s\n", event.type());
        Actor actor = event.actor();
        ImmutableMap<String, String> attributes = actor.attributes();
        System.out.printf("EVENT ACTOR ID: %s\n", actor.id());

        eventStream.close();
        docker.close();
    }
}
