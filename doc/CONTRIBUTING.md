# Contributing

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

## Run Tests

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
