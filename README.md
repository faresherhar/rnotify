<h1 align="center">Rnotify</h1>

<h2 align="center">The Repository Releases Tracker</h2>

<p align="center">
  <a href="https://www.python.org/"><img alt="Supported Python Versions: 3.12" src="https://img.shields.io/badge/python-3.12-blue?logo=python"></a>
  <a href="https://pypi.org/project/pip/"><img alt="Pip Version: v24.0" src="https://img.shields.io/pypi/v/pip?logo=Pypi"></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

> Up-to-date to the latest release of your favorite opensource tools.”

**Rnotify**, is a Python tool for tracking releases. By using it, you are notified of the latest release of your configured repositories. It uses the Github, and Gitlab APIs to scrape the data of the releases related to your repositories, and sends you a message to notify you of the latest release, by Email.

For more details, installation instructions, and configuration, please refer to the documentation below.

## FAQ

> Why building Rnotify ?

At the time, I worked within a team, in which our technical environment heavily depends on open source projects, and we had many tools that were outdated. Being unable to track the new releases of each single opensource application, was the reason for it.

Thus, I created Rnotify, to do the job for us. A backend application, that keeps us updated with the new releases.

> What are the supported developer platforms ?

At the moment, the application supports only the Github, and the Gitlab APIs. However, if there's the need to support another platform, please open an issue for it, or add it yourself, and open a pull request.

> Do I need API keys for using Rnotify ?

It is not mandatory to provide any API keys. Still, both the Github, and Gitlab APIs, have some limitations without the API keys. The short answer is, unless you have too many repositories listed, or doing checks on a hourly basis, the application still works fine, without the API keys.

Please take a deeper look at the documentation [Github Rate Limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28), [Gitlab Rate Limits](https://docs.gitlab.com/ee/user/gitlab_com/index.html#gitlabcom-specific-rate-limits).

> What are the notification services supported ?

The application was designed to send notifications via emails only. This doesn't eliminate the chance to adding more services in the future.

> Can I change the HTML template for the notification ?

Yes totally. Create your own HTML template, whilst respecting the data fields, and the Jinja syntax.

> What are the supported RDBMS ?

At the current moment only `SQLite` and `PostgreSQL` are supported.

> How can I run Rnotify ?

Rnotify, was designed to be run on as `Function as a Service` tool, however a `Dockerfile` is provided, so the application can be run on a container based system.

## Installation

> Please make sure to build your image first.

```sh
# Update the values for your config.toml
# Update values
cp example.config.toml config.toml

# Run docker-compose
docker-compose up
```

## Development

### Code Overview

```bash
.
├── requirements                    # Requirements files
│   ├── common.txt
│   └── dev.txt
├── src                             # Source Code
│   ├── __init__.py
│   ├── config.py                   # Config files
│   ├── database.py                 # Database config
│   ├── models.py                   # Release db model
│   ├── main.py                     # main code
│   └── utils.py                    # Utility code
├── templates                       # Notification email templates
│   ├── notification.html.j2
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

### Environment Variables

To run this project, you will need the `RNOTIFY_CONFIG_FILE` environment variable (mandatory), it refers to the configuration file.

## Setup Development Environment

> Setup development environment

```sh
# Create virtual environment
python3 -m venv .venv/
source .venv/bin/activate
pip install --upgrade pip

# Install dependencies
make setup

# Copy configuration file
# Update the values
cp example.config.toml config.toml
```

> Setup environment variables

```sh
export RNOTIFY_CONFIG_FILE="./config.toml"
```

> Database

For development, we're using `SQLite` as a RDBMS. In case of an alternative is being used, please make sure to update the values in the configuration.

> Docker Image

I believe that each person should build his own project, having his own image, therefore I didn't provide any url to a hosted image.
