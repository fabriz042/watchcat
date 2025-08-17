import click
import docker

client = docker.DockerClient(base_url='unix://var/run/docker.sock')

@click.group()
def cli():
    pass

@click.command()
def list_containers():
    for container in client.containers.list(all=True):
        print(container.name)

cli.add_command(list_containers)

if __name__ == "__main__":
    cli()
