# Using the Docker Engine .NET client

## Prerequisites

- [.NET Core SDK](https://dotnet.microsoft.com/download) installed
- Docker running locally
- .NET Client for Docker Remote API installed locally:

```bash
dotnet add package Docker.DotNet
```

## Run the sample

This samples uses the [.NET Client for Docker Remote API](https://github.com/Microsoft/Docker.DotNet). It prints to stdout the list of containers running locally. To test it

```bash
$ dotnet run
9f5589f2664bcb756bb70d243a8ef3652aae93719138469e35ac4689dc2af035 httpd
2985c3f8bc123ee112a1e68b30c5942ac1a8d6018d1b3f8b11edc1891454d6a8 httpd
dc4142211d8c1545af8abfb0660066b297b9e52b65294f9241eeb08be1f10d95 httpd
4932d9cf1f844cbdff57e04ea919933f1773a4b4f5aec96aa4672b7aa8cf24a4 httpd
30a892ef7c74020e15981ed00a9592d1ce5a8a6eced1e785bb6e863189c125e6 httpd
276a208c04dfdfad0d9d42c5c826aeb3bed8150531f06ec1fccee630fec61ebf httpd
df507266bac6ba171b316bc642b3c42274b8c24b09877d0211853b382419e4c4 httpd
528dc7a1d8dab613415291f3218dae2789de04847c5bb2672f5d647ee5f759d5 httpd
f65f20b147ecf2e1f795ae38fac3898029b3bb053d7fb2fb31ae8260b14e21b3 httpd
c4f5b10ef51bcbcd8f326e0d3d44cad03b012177c705038bd8ed79b99cc7756e httpd
```