import docker
import time
import sys

client = docker.DockerClient(base_url='unix://var/run/docker.sock')

def main():
    print("Watchcat enabled, monitoring unhealthy containers every 5 minute")

    while True:
        for container in client.containers.list(all=True):
            if container.name == 'watchcat':
                continue
            health = container.attrs.get('State', {}).get('Health', {}).get('Status')
            if health == 'unhealthy':
                print(f"{container.name} is unhealthy. Restarting...")
                container.restart()
        time.sleep(300) #5 minutes

if __name__ == "__main__":
    main()
