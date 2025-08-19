import docker
import time
import sys
import os
from datetime import datetime

client = docker.DockerClient(base_url='unix://var/run/docker.sock')

def log_restart(container_name):
    os.makedirs('/logs', exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('/logs/restarts.log', 'a') as f:
        f.write(f"{timestamp} - Restarted container: {container_name}\n")

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
                log_restart(container.name)
        time.sleep(300) #5 minutes

if __name__ == "__main__":
    main()
