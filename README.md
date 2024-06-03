<h1 align="center">Rnotify</h1>

<h2 align="center">The Repository Releases Tracker</h2>

<p align="center">
  <a href="https://www.python.org/"><img alt="Supported Python Versions: 3.12" src="https://img.shields.io/badge/python-3.12-blue?logo=python"></a>
  <a href="https://pypi.org/project/pip/"><img alt="Pip Version: v24.0" src="https://img.shields.io/pypi/v/pip?logo=Pypi"></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

> Up-to-date to the latest release of your favorite opensource tools.”

RNOTIFY is a Python tool for tracking releases. By using it, you are notified of the latest release of your configured repositories. It uses the Github, and Gitlab APIs to scrape the data of the releases related to your repositories, and sends you a notification about it, by Email, Slack, Telegram...

For more details, installation instrucions, and configuration, please refer to the documentation below.

## Installation

### Helm

### Docker Compose

> Please make sure to build your image first.

```sh
# Build 'src/' directory for the rnotify app Docker image
make build_src

# Run docker-compose
docker-compose up
```

Open your browser, and go to <http://localhost:8080>.

## Contributing

### Setup Development Enviroment

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

### Local development

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

### Run Tests

```sh
# Run tests
make run_tests
```

### Docker Images

> Please make sure to update the variables in the Makefile before building the image, and to login into your image artifactory before pushing it.

```sh
# Build 'src/' directory for the rnotify app Docker image
make build_src

# Push the rnotify app Docker image
make push_src

# Access the rnotify app Docker image
make debug_src
```
