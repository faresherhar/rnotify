from os import getenv
from pydantic_settings import (
    BaseSettings,
    CliSettingsSource,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)


class Settings(BaseSettings):
    # Database URI
    database_uri: str

    # GitHub Configuration
    github_api_url: str
    github_repos: list[str]
    github_api_token: str

    # GitLab Configuration
    gitlab_api_url: str
    gitlab_repos: list[str]
    gitlab_api_token: str

    # HTML Notification Template
    notification_template: str

    # Email Configuration
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
