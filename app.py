import click
import docker
import time
import sys
import os

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
    print("Watchcat enabled, monitoring unhealthy containers every 1 minute")
    
    pid = os.fork()
    if pid == 0:
        while True:
            for container in client.containers.list(all=True):
                health = container.attrs.get('State', {}).get('Health', {}).get('Status')
                if health == 'unhealthy':
                    print(f"{container.name} is unhealthy. Restarting...")
                    container.restart()
            time.sleep(60)
    else:
        sys.exit(0)

@click.command()
def disable():
    try:
        watchcat_container = client.containers.get('watchcat')
        watchcat_container.stop()
        print("Watchcat stopped")
    except docker.errors.NotFound:
        print("Watchcat container not found")

#Comands
cli.add_command(list_unhealthy)
cli.add_command(list_containers)
cli.add_command(enable)
cli.add_command(disable)

if __name__ == "__main__":
    cli()
