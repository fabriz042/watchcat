import click
import docker
import time

client = docker.DockerClient(base_url='unix://var/run/docker.sock')

@click.group()
def cli():
    pass

@click.command()
def list_containers():
    for container in client.containers.list(all=True):
        print(container.name)

@click.command()
def list_unhealthy():
    for container in client.containers.list(all=True):
        if container.attrs.get('State', {}).get('Health', {}).get('Status') == 'unhealthy':
            print(f"{container.name} - {container.status}")

@click.command()
def enable():
    while True:
        for container in client.containers.list(all=True):
            health = container.attrs.get('State', {}).get('Health', {}).get('Status')
            if health == 'unhealthy':
                print(f"{container.name} is unhealthy. Restarting...")
                container.restart()
        time.sleep(60)  # wait 60 secods to next check

    print("Watchat enabled, every 1 minute will restart unhealthy containers")

cli.add_command(list_unhealthy)
cli.add_command(list_containers)
cli.add_command(enable)

if __name__ == "__main__":
    cli()
