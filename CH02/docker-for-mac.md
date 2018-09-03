# The Docker for Mac example

## Build the image

```bash
linuxkit build -format iso-efi docker-for-mac.yml
```

## Specify docker configuration

Create the file `./metadata.json`:

```json
{
    "docker": {
        "entries": {
            "daemon.json": {
                "content": "{\n \"debug\" : true,\n \"experimental\" : true\n}\n"
             }
         }
     }
}
```

## Run the image

```bash
linuxkit run hyperkit \
          -networking=vpnkit \
          -vsock-ports=2376 \
          -disk size=4096M \
          -data-file ./metadata.json \
          -iso -uefi docker-for-mac-efi
```

## Configure the docker macOS CLI

To access the docker daemon that is running in this Docker for Mac host use the Unix socket unix://docker-for-mac-efi-state/guest.00000948:

```bash
docker -H unix://docker-for-mac-efi-state/guest.00000948 ps
```