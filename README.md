# Rnotify Logo

<h2 align="center">The Repository Releases Tracker</h2>

<p align="center">
<a href="https://www.python.org/"><img alt="Supported Python Versions: 3.10 | 3.11 | 3.12" src="https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12-blue"></a>
<a href="https://pypi.org/project/pip/"><img alt="Pip Version: v24.0" src="https://img.shields.io/pypi/v/pip"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://mit-license.org/"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://docs.github.com/en/rest"><img alt="Github API" src="https://img.shields.io/badge/api-github-blue?logo=github"></a>
<a href="https://docs.gitlab.com/ee/api/rest/"><img alt="Gitlab API" src="https://img.shields.io/badge/api-gitlab-blue?logo=gitlab"></a>
<a href="https://api.slack.com/apis"><img alt="Slack API" src="https://img.shields.io/badge/api-slack-blue?logo=slack"></a>
<a href="https://core.telegram.org/"><img alt="Telegram API" src="https://img.shields.io/badge/api-telegram-blue?logo=telegram"></a>
</p>

> Up-to-date to the latest release of your favorite opensource tools.”

RNOTIFY is a Python tool for tracking releases. By using it, you are notified of the latest release of your configured repositories. It uses the Github, and Gitlab APIs to scrape the data of the releases related to your repositories, and sends you a notification about it, by Email, Slack, Telegram...


<p align="center">
  <img alt="Diagram" src="diagram/diagram.svg">
</p>


For more details, installation instrucions, and configuration, please refer to the documentation below.

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

> Setup configuration files

```sh
mkdir ${RNOTIFY_CONFIG_DIR}
cat >> ${RNOTIFY_PROVIDERS_FILE}<< EOF
github:
  - grafana/grafana
  - derailed/k9s

gitlab:
  - AuroraOSS/AuroraStore
EOF

cat >> ${RNOTIFY_PLATFORMS_FILE}<< EOF
email:
    receiver_email: some.user@gmail.com
    smtp_server: smtp.gmail.com
    user_email: user@gmail.com
    user_password: passwd
    port: 465
    message_type: html
EOF
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

#### Rnotify App Image

> Please make sure to update the variables in the Makefile before building the image.
>> ***ARTIFACTORY_URL***, ***SRC_IMAGE_NAME***, ***SRC_IMAGE_TAG***

```sh
# Build 'src/' directory for the rnotify app Docker image
make build_src
```

> Please make sure to login into your image artifactory before pushing the image.

```sh
# Push the rnotify app Docker image
make push_src
```

#### Rnotify Dahsboard Image

> Please make sure to update the variables in the Makefile before building the image.
>> ***ARTIFACTORY_URL***, ***DASHBOARD_IMAGE_NAME***, ***DASHBOARD_IMAGE_TAG***

```sh
# Build 'dashboard/' directory for the rnotify app Docker image
make build_dashboard
```

> Please make sure to login into your image artifactory before pushing the image.

```sh
# Push the rnotify dashboard Docker image
make push_dashboard
```