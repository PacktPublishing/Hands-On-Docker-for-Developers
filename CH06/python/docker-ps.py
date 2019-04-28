#!/usr/bin/env python3

import docker
client = docker.from_env()

containers = client.containers.list()
for container in containers:
    print(container.short_id, container.attrs['Config']['Image'])