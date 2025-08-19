import docker
import time
import sys
from datetime import datetime

client = docker.DockerClient(base_url='unix://var/run/docker.sock')
minutes = 5

def log_restart(container_name):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('/logs/restarts.log', 'a') as f:
        f.write(f"{timestamp} - Restarted container: {container_name}\n")

def main():
    print(f"Watchcat enabled, monitoring unhealthy containers every {minutes} minutes")

    while True:
        for container in client.containers.list(all=True):
            if container.name == 'watchcat':
                continue
            health = container.attrs.get('State', {}).get('Health', {}).get('Status')
            if health == 'unhealthy':
                print(f"{container.name} is unhealthy. Restarting...")
                container.restart()
                log_restart(container.name)
        time.sleep(minutes*60)

if __name__ == "__main__":
    main()
