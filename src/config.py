from os import getenv
from pydantic_settings import (
    BaseSettings,
    CliSettingsSource,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)


class Settings(BaseSettings):
    # Broker, Backend URI
    broker_uri: str
    backend_uri: str

    # Github Repositories, API Url, API Token
    github_repos: list[str]
    github_api_url: str
    github_api_token: str

    # Gitlab Repositories, API Url, API Token
    gitlab_repos: list[str]
    gitlab_api_url: str
    gitlab_api_token: str

    # Notification Template
    notification_template: str

    # Email Settings
    recipient: str
    smtp_username: str
    smtp_password: str
    smtp_server: str
    smtp_port: int

    model_config = SettingsConfigDict(toml_file=getenv("RNOTIFY_CONFIG_FILE"))

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: BaseSettings,
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls),)


settings = Settings()

