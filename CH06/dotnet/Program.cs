using System;
using System.Collections;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

using Docker.DotNet;
using Docker.DotNet.Models;

namespace dockerPs
{
    class Program
    {
        static async Task Main(string[] args)
        {
            DockerClient client = new DockerClientConfiguration(
                new Uri("unix:///var/run/docker.sock"))
                .CreateClient();

            IList<ContainerListResponse> containers = await GetContainers(client);
            foreach (var container in containers)
            {
                Console.WriteLine("{0} {1} {2}", container.ID, container.Image, container.Status);
            }
        }

        private static async Task<IList<ContainerListResponse>> GetContainers(DockerClient client)
        {
            return await client.Containers.ListContainersAsync(
                            new ContainersListParameters()
                            {
                                Limit = 10,
                            });
        }
    }
}
