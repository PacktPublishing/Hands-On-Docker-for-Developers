package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"os"

	"github.com/docker/docker/api/types"
	"github.com/docker/docker/client"
)

func main() {
	cli, err := client.NewClientWithOpts(client.FromEnv)
	if err != nil {
		panic(err)
	}

	img := "traefik"
	ctx := context.Background()

	reader, err := cli.ImagePull(ctx, img, types.ImagePullOptions{})
	if err != nil {
		panic(err)
	}
	io.Copy(os.Stdout, reader)

	data, _, err := cli.ImageInspectWithRaw(ctx, img)
	if err != nil {
		panic(err)
	}

	s, err := json.MarshalIndent(data, "", "    ")
	if err != nil {
		panic(err)
	}

	fmt.Printf("%s", s)
}