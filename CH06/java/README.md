# Using the Docker Engine Java client

## Prerequisites

- JDK and maven installed locally
- Docker running locally

## Run the sample

This samples uses the [Spotify Docker client for the JVM](https://github.com/spotify/docker-client). It waits for **one** Docker Engine event, prints its details to stdout and exits. To test it start it using maven:

```bash
mvn -q clean install exec:java
```

and trigger a Docker Engine event from another shell:

```bash
$ docker run -d -P httpd
9f5589f2664bcb756bb70d243a8ef3652aae93719138469e35ac4689dc2af035
```

The following informations is printed to stdout in the first shell:

```bash
EVENT TIME: Wed May 01 18:34:41 CEST 2019
EVENT ACTION: create
EVENT TYPE: CONTAINER
EVENT ACTOR ID: 9f5589f2664bcb756bb70d243a8ef3652aae93719138469e35ac4689dc2af035
```
