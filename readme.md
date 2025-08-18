# Watchcat

Docker container monitoring tool

## Setup

Add alias for easy usage:

```bash
echo "alias watchcat='docker compose run --rm watchcat'" >> ~/.bashrc
source ~/.bashrc
```

## Usage

```bash
watchcat list-containers
```

```bash
watchcat list_unhealthy
```

```bash
watchcat enable
```
