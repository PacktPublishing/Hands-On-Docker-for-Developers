# Build a SpringBoot image with Jib

## Build it with Docker (maven dependency plugin version)

```bash
$ mvn package dockerfile:build
(...)
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  8.163 s
[INFO] Finished at: 2019-05-03T23:24:13+02:00
[INFO] ------------------------------------------------------------------------
$ docker run -d -p 8080:8080 --name springboot-mdp mariolet/gs-spring-boot:mdp
9edb3ad4a8cc4965d5ab6c9c4287c872d3a56aaafb7f53c7b6f44b235c79d3d
$ curl localhost:8080
Greetings from Sbrodj!%
```

## Build it with Jib

```bash
$ mvn -f pom.jib.xml compile jib:dockerBuild -Dimage=mariolet/gs-spring-boot-jib
(...)
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  4.802 s
[INFO] Finished at: 2019-05-03T23:26:19+02:00
[INFO] ------------------------------------------------------------------------
$ docker run -d -p 8080:8080 --name springboot-jib mariolet/gs-spring-boot-jib
fc43325f414cd137c06fa3ee235302e8bf0d1a97e6de9c918f5580ec8713a941
$ curl localhost:8080
Greetings from Moulinsart!%
```
