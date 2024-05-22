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
python3 -m venv .venv/
source .venv/bin/activate
pip install --upgrade pip
make setup
```

> Setup enviroment variables

```sh
cp .env.example .env
set -a && source .env && set +a
```

> Database

For development we're using `SQLite DB`. If you want to use another RDBMS, please update the `RNOTIFY_DATABASE_URI` in the enviroment variable, and reload the new values `set -a && source .env && set +a`.

To explore the `SQLite DB`, we recommend using the [SQLite Browser](https://sqlitebrowser.org/).

### Run Tests

```sh
# Run tests
make run_tests
```

### Docker Images

> Please make sure to update the variables in the Makefile before building the image, and to login into your image artifactory before pushing the image.

```sh
# Build 'src/' directory for the rnotify app Docker image
make build_src

# Push the rnotify app Docker image
make push_src
```
