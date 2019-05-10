# Build a SpringBoot image with Jib

## Build it with Docker (maven dependency plugin version) - fabric8

```bash
$ mvn -f pom.xml install

$ (docker rm -f springboot-mdp || echo "container not found") && \
mvn package dockerfile:build && \
docker run -d -p 8080:8080 --name springboot-mdp mariolet/gs-spring-boot:mdp && \
sleep 10 && curl localhost:8080
(...)
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  8.163 s
[INFO] Finished at: 2019-05-03T23:24:13+02:00
[INFO] ------------------------------------------------------------------------
```

## Build it with Jib

```bash
$ (docker rm -f springboot-jib || echo "container not found") && \
mvn -f pom.jib.xml compile jib:dockerBuild -Dimage=mariolet/gs-spring-boot-jib && \
docker run -d -p 8080:8080 --name springboot-jib mariolet/gs-spring-boot-jib && \
sleep 10 && curl localhost:8080
(...)
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  4.802 s
[INFO] Finished at: 2019-05-03T23:26:19+02:00
[INFO] ------------------------------------------------------------------------
```