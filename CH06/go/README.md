# Using the Docker Engine Go client

## Prerequisites

- Go intalled locally and GOPATH env variable set
- Docker running locally
- Official [Docker Engine Go SDK](https://gowalker.org/docker.io/go-docker) installed:

```bash
go get github.com/docker/docker/client
```

## Run the sample

This samples pull the docker image `traefik` and then print to stdout the image attributes:

```bash
$ DOCKER_API_VERSION=1.39 go run main.go
{"status":"Pulling from library/traefik","id":"latest"}
(...)
{
    "Id": "sha256:0d2f1c7902c773164cfa4afba0af881fe47b399b930f6ae92b5eea3cb7ee81cc",
    "RepoTags": [
        "traefik:latest"
    ],
(...)
    "Metadata": {
        "LastTagTime": "0001-01-01T00:00:00Z"
    }
}
```
