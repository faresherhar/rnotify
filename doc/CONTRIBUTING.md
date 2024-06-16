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

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

### Common

> `RNOTIFY_DATABASE_URI`
 
Database URI (Mandatory Enviroment Variable). Check the supported SQLAlchemy dialects.

### Scraper

> `RNOTIFY_GITHUB_API_TOKEN`

Github Authentication Token (Optional Enviroment Variable). When not provided, the code still works but with a limited number of queries per hour. 

> `RNOTIFY_GITLAB_API_TOKEN`

Gitlab Authentication Token (Optional Enviroment Variable). When not provided, the code still works but with a limited number of queries per hour.

### Notifier

> `RNOTIFY_NOTIFICATION_TEMPLATES`

Notification Templates Directory (Mandatory Enviroment Variable). This variable points to the directory of the templates for the notifications.

> `RNOTIFY_NOTIFICATION_METHODS`

Notification Methods (Mandatory Enviroment Variable). A list of platfroms (separated by comma), to be used to send notifications. Please check our supported notification platforms.

Examples:

- "email"
- "email,telegram"
- "slack,telegram"

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
# Update the value if necessary
cp .env.example .env

# Load the enviroment variables
# Execute it whenever you update the values
set -a && source .env && set +a
```

> Database

For development, we're using `SQLite DB`. If you want to use another RDBMS, please update the `RNOTIFY_DATABASE_URI` in the enviroment variables file `.env`, and reload the new values `set -a && source .env && set +a`.

To explore the `SQLite DB`, we recommend using the [SQLite Browser](https://sqlitebrowser.org/).

## Local development

Each functionality is run seperatly, despite having the code within the same project.

```sh
# Init the Database
make init_db

# Lunch the API
# Navigate to http://localhost:8080, to access it
make run_asgi

# Fetch data for new releases
make run_scraper

# Send notifications for the new releases
make run_notifier
```

> Init Script

Use the following code in `src/init_db.py`, if you want to auto fill the database with examples for the development.

```python
if __name__ == "__main__":
    from database import engine, get_db_session

    from cruds.repo import add_repo

    from models.release import Release
    from models.repo import Repo
    from models.base import Base

    Base.metadata.create_all(bind=engine)

    repo_data = [
        {"provider": "github", "owner": "derailed", "repo": "k9s"},
        {"provider": "gitlab", "owner": "AuroraOSS", "repo": "AuroraStore"},
    ]

    for row in repo_data:
        add_repo(**row, db_session=get_db_session())
```

> Run Tests

```sh
# Run tests
make run_tests
```

## Docker Images

> Please make sure to update the variables in the Makefile before building the image, and to login into your image artifactory before pushing it.

```sh
# Build 'src/' directory for the rnotify app Docker image
make build_src

# Push the rnotify app Docker image
make push_src

# Access the rnotify app Docker image
make debug_src
```
