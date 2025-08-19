# Watchcat

Simple Docker container monitoring tool that automatically restarts unhealthy containers and records logs.

## Features

- Monitors all running Docker containers every 5 minutes
- Automatically restarts containers with `unhealthy` health status
- Excludes itself from monitoring to prevent infinite loops

## Prerequisites

- Docker and Docker Compose installed
- Docker daemon running
- Containers must have health checks configured to benefit from monitoring

## Setup

1. Clone the repository:

```bash
git clone https://github.com/fabriz042/watchcat.git
cd watchcat
```

2. Start the monitoring service:

```bash
docker compose up -d
```

## How it works

Watchcat connects to the Docker socket and continuously monitors container health status. When it detects a container with `unhealthy` status, it automatically restarts that container.

## Configuration

The monitoring interval is set to 5 minutes by default. To change this, modify the `minutes = 5` value in `app.py`.

## Logs

### Watch restart events log

Restart events are saved to a host folder for easy viewing:

```bash
# View all restart events
cat ./logs/restarts.log
```

Example output:

```
2025-01-18 14:30:15 - Restarted container: webapp
2025-01-18 15:45:22 - Restarted container: database
2025-01-18 16:12:08 - Restarted container: redis
```
