# Build a SpringBoot container with Jib

## Build it with Docker

```bash
$ mvn install dockerfile:build && \
(docker rm -f springboot-normal || echo "container not found") && \
docker run -d -p 8080:8080 --name springboot-normal mariolet/gs-spring-boot
(...)
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 17.138 s
[INFO] Finished at: 2019-05-01T01:36:39+02:00
[INFO] Final Memory: 52M/399M
[INFO] ------------------------------------------------------------------------
```

## Build it with Jib

```bash
mvn compile jib:dockerBuild -Dimage=mariolet/gs-spring-boot-jib && \
(docker rm -f springboot-jib || echo "container not found") && \
docker run -d -p 8081:8080 --name springboot-jib mariolet/gs-spring-boot-jib
(...)
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 8.114 s
[INFO] Finished at: 2019-05-01T01:37:08+02:00
[INFO] Final Memory: 32M/284M
[INFO] ------------------------------------------------------------------------
```