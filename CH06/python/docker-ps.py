#!/usr/bin/env python3

import docker
client = docker.from_env()

img = 'httpd'

container = client.containers.run(img, detach=True, publish_all_ports=True)
print('Container ID: ' + container.id)
container.reload()
print('Exposed port: ' + container.attrs['NetworkSettings']['Ports']['80/tcp'][0]['HostPort'])
