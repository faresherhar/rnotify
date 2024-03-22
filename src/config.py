from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str = Field(validation_alias="RNOTIFY_DATABASE_URI")
    PROVIDERS_FILE: str = Field(validation_alias="RNOTIFY_PROVIDERS_FILE")
    PLATFORMS_FILE: str = Field(validation_alias="RNOTIFY_PLATFORMS_FILE")
    NOTIFICATION_TEMPLATES: str = Field(
        validation_alias="RNOTIFY_NOTIFICATION_TEMPLATES"
    )

    GITHUB_API: str = "https://api.github.com/repos/"
    GITHUB_RELEASE: str = "https://github.com/{repo}/releases/tag/{tag_name}"

    GITLAB_API: str = "https://gitlab.com/api/v4/projects/"
    GITLAB_RELEASE: str = "https://gitlab.com/{repo}/-/releases/{tag_name}"

    TELEGRAM_API: str = (
        "https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message_body}"
    )


settings = Settings()
