# Contributing

## Code Overview

```bash
.
├── data                            # Example data
│   └── release
│       ├── github_release_body.json
│       └── gitlab_release_body.json
├── doc                             # Documentation files
│   ├── CONTRIBUTING.md
│   └── INSTALLATION.md
├── helm                            # Helm Chart manifests
│   ├── Chart.yaml
│   ├── templates
│   │   ├── configmap.yaml
│   │   ├── _helpers.tpl
│   │   └── rnotify.yaml
│   └── values.yaml
├── requirements                    # Requirements files
│   ├── common.txt
│   └── dev.txt
├── src                             # Source Code
│   ├── __init__.py
│   ├── config.py                   # Config files
│   ├── logging_config.py           # Logging config
│   ├── notifier.py                 # Celery app for sending notifications
│   ├── scraper.py                  # Scrap for releases
│   └── utils.py                    # Utility code
├── templates                       # Notification message templaes
│   ├── notification.txt.j2
│   └── notification.txt.j2
├── tests                           # Tests
│   └── test_utils.py
├── README.md                       # README
├── Makefile                        # Makefile
├── pytest.ini                      # Pytest config
├── example.config.toml             # Config file example
├── .gitignore                      # Git ignore                             
├── docker-compose.yaml             # Docker compose setup
├── .dockerignore                   # Docker ignore                                 
└── Dockerfile                      # Dockerfile
```

## Environment Variables

To run this project, you will need the `RNOTIFY_CONFIG_FILE` environment variable (Mandatory), that indicates to the configuration file full name.

## Setup Development Enviroment

> Setup development enviroment

```sh
# Create virtual enviroment
python3 -m venv .venv/
source .venv/bin/activate
pip install --upgrade pip

# Install dependencies
make setup
```

> Setup enviroment variables

```sh
export RNOTIFY_CONFIG_FILE="./config.toml"
```

> Database

For development, we're using `Redis` as a backend and a brocker at the sametime. In case an alternative is being used, please make sure to update the values in the configuration.

## Local development

Each functionality is run seperatly, despite having the code within the same project. For development, it's better to use 3 different terminals, each part run seperatly.

### Setup redis

Copy the following code into a file nameded `docker-compose.redis.yaml`.

```yaml
version: 3.7
services:
  redis:
    image: docker.io/bitnami/redis:7.2.5
    volumes:
      - redis:/bitnami/redis/data
    environment:
      ALLOW_EMPTY_PASSWORD=yes
    ports:
      - "6379:6379"
volumes:
  redis: null
```

### Run applications

Use 3 different terminals.

> Terminal 1

```sh
# Start Redis
docker-compose -f docker-compose.redis.yaml up
```

> Terminal 2

```sh
# Start Celery app for sending notifications
make run_notifier
```

> Terminal 3

```sh
# Start Scraper
make run_scraper
```

## Docker Images

I believe that each person should build his own project, having his own image, therefore I didn't provide any url to a hosted image. 

> Please make sure to update the variables in the Makefile before building the image, and to login into your image artifactory before pushing it.

```sh
# Build 'src/' directory for the rnotify app Docker image
make build_src

# Push the rnotify app Docker image
make push_src

# Access the rnotify app Docker image
make debug_src
```
