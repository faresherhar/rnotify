<h1 align="center">Rnotify</h1>

<h2 align="center">The Repository Releases Tracker</h2>

<p align="center">
  <a href="https://www.python.org/"><img alt="Supported Python Versions: 3.12" src="https://img.shields.io/badge/python-3.12-blue?logo=python"></a>
  <a href="https://pypi.org/project/pip/"><img alt="Pip Version: v24.0" src="https://img.shields.io/pypi/v/pip?logo=Pypi"></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

> Up-to-date to the latest release of your favorite opensource tools.”

**Rnotify**, is a Python tool for tracking releases. By using it, you are notified of the latest release of your configured repositories. It uses the Github, and Gitlab APIs to scrape the data of the releases related to your repositories, and sends you a message to notify you of the latest release, by Email, Slack, Telegram... .

For more details, installation instrucions, and configuration, please refer to the documentation below.

## Code Overview

```bash
.
├── data                            # Example data
│   └── release
│       ├── github_release_body.json
│       └── gitlab_release_body.json
├── doc                             # Documentation files
│   ├── CONTRIBUTING.md
│   ├── DEPLOYMENT.md
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
│   ├── asgi.py                     # API App
│   ├── config.py                   # Config files
│   ├── cruds                       # Cruds for each model
│   │   ├── __init__.py
│   │   ├── platform
│   │   │   ├── __init__.py
│   │   │   ├── slack.py
│   │   │   └── telegram.py
│   │   ├── release.py
│   │   └── repo.py
│   ├── database.py                 # SQLAlchemy config
│   ├── init_db.py                  # Create Tables
│   ├── __init__.py
│   ├── logging_config.py           # Logging config
│   ├── main.py                     # Main functions
│   ├── models                      # SQLAlchemy models
│   │   ├── base.py
│   │   ├── __init__.py
│   │   ├── platform
│   │   │   ├── __init__.py
│   │   │   ├── slack.py
│   │   │   └── telegram.py
│   │   ├── release.py
│   │   └── repo.py
│   ├── platforms                   # Notification platforms
│   │   ├── email.py
│   │   ├── __init__.py
│   │   ├── slack.py
│   │   └── telegram.py
│   ├── providers                   # Github, Gitlab API requests
│   │   ├── github.py
│   │   ├── gitlab.py
│   │   └── __init__.py
│   ├── routers                     # FastAPI routers
│   │   ├── __init__.py
│   │   ├── platform
│   │   │   ├── __init__.py
│   │   │   ├── slack.py
│   │   │   └── telegram.py
│   │   ├── release.py
│   │   └── repo.py
│   └── utils.py                    # Utility code
├── templates                       # Notification message templaes
│   ├── notification.md.j2
│   └── notification.txt.j2
├── tests                           # Tests
│   ├── test_platforms_slack.py
│   ├── test_platforms_telegram.py
│   ├── test_providers_github.py
│   ├── test_providers_gitlab.py
│   └── test_utils.py
├── README.md                       # README
├── Makefile                        # Makefile
├── pytest.ini                      # Pytest config
├── .gitignore                      # Git ignore                             
├── docker-compose.yaml             # Docker compose setup
├── .dockerignore                   # Docker ignore                                 
├── Dockerfile                      # Dockerfile
└── .env.example                    # .env file example
```

## API Reference

## Documentation

- [Contributing](./doc/CONTRIBUTING.md)
- [Installation](./doc/INSTALLATION.md)
- [Deployment](./doc/DEPLOYMENT.md)

## FAQ

## Features
