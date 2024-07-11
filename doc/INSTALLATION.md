# Installation

## Helm

## Docker Compose

> Please make sure to build your image first.

```sh
# Update the values for your config.toml
cp example.config.toml config.toml

# Build 'src/' directory for the rnotify app Docker image
make build_src

# Run docker-compose
docker-compose up
```