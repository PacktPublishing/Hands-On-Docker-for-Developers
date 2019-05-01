# Using the Docker Engine Python client

## Prerequisites

- Python 3 intalled locally
- Docker running locally
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) installed:

```bash
pip install docker
```

## Run the sample

This samples start an `httpd` container and prints its ID and exposed port to stdout.

```bash
$ python3 docker-ps.py
Container ID: c4f5b10ef51bcbcd8f326e0d3d44cad03b012177c705038bd8ed79b99cc7756e
Exposed port: 32776
$ curl localhost:32776
<html><body><h1>It works!</h1></body></html>
```
