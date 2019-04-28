package DockerPs;
import com.spotify.docker.client.DockerClient;
import com.spotify.docker.client.DockerClient.ListContainersParam;
import com.spotify.docker.client.exceptions.DockerCertificateException;
import com.spotify.docker.client.exceptions.DockerException;
import com.spotify.docker.client.messages.Container;

import java.util.List;

import com.spotify.docker.client.DefaultDockerClient;

/**
 * Hello world!
 */
public final class App {
    private App() {
    }

    /**
     * Says hello to the world.
     * 
     * @param args The arguments of the program.
     * @throws DockerCertificateException
     * @throws InterruptedException
     * @throws DockerException
     */
    public static void main(String[] args) throws DockerCertificateException, DockerException, InterruptedException {
        final DockerClient docker = DefaultDockerClient.fromEnv().build();

        List<Container> listContainers = docker.listContainers(ListContainersParam.allContainers());
        for (Container container : listContainers) {
            System.out.println(container.id() + " " + container.image());
        }
        docker.close();
    }
}
