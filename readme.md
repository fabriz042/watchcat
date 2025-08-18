# Watchcat

Simple docker container monitoring tool that automatically restarts unhealthy containers.

## Features

- Monitors all running Docker containers every 5 minutes
- Automatically restarts containers with `unhealthy` health status
- Excludes itself from monitoring to prevent infinite loops
- Lightweight Python-based solution

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

The monitoring interval is set to 5 minutes by default. To change this, modify the `time.sleep(300)` value in `app.py` (300 seconds = 5 minutes).

## Logs

View monitoring logs with:

```bash
docker compose logs -f watchcat
```
