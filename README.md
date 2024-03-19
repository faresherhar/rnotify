# Update Me

A Python Application to track repositories releases

## Application Diagram

![Diagram](diagram/diagram.svg "Diagram")

##  Upcomming Features

- [ ] Support Coderberg
- [ ] Support notification platforms
  - ~~Email~~
  - ~~Slack~~
  - Teams
  - Mattermost
  - Telegram
  - Discord~~
  - Signal

## Contributing

### Setup Development Enviroment

```shell
# Create development enviroment
python3 -m venv .venv/
source .venv/bin/activate

# Install dependencies
make setup

# Create .env file
cp .env.dev.example .env

# Create local Database
touch sqlite.db

# Load enviroment variables
export $(grep -v '^#' .env | xargs)
```

### DataBase

For development we're using `SQLite DB`. If you want to use another DB, please update the `UPME_DATABASE_URI` in the enviroment variable, and reload the new values `export $(grep -v '^#' .env | xargs)`.

To explore the `SQLite DB`, we recommend using the [SQLite Browser](https://sqlitebrowser.org/).