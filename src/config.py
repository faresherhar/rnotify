from pydantic import Field
from pydantic_settings import BaseSettings


#TODO: Add APIs documentation, and detail references
class Settings(BaseSettings):
    # Database URI. Check our RDBMS documentation.
    DATABASE_URI: str = Field(validation_alias="RNOTIFY_DATABASE_URI")


class ScraperSettings(BaseSettings):
    # Github, Gitlab, APIs
    GITHUB_API: str = "https://api.github.com/repos/"
    GITLAB_API: str = "https://gitlab.com/api/v4/projects/"


class NotifierSettings(BaseSettings):
    # Notifications templates.
    NOTIFICATION_TEMPLATES: str = Field(validation_alias="RNOTIFY_NOTIFICATION_TEMPLATES")
    NOTIFICATION_TEMPLATES_TYPES: list[str] = ["txt", "md"]

    # What service to use to send notifications
    # Multiple methods can be chosen using a list[str].
    # email, slack, telegram
    NOTIFICATION_METHODS: str = Field(validation_alias="RNOTIFY_NOTIFICATION_METHODS", default=[])

    # Telegram configuration.
    TELEGRAM_API: str = "https://api.telegram.org/"
    TELEGRAM_BOT_TOKEN: str = Field(validation_alias="RNOTIFY_TELEGRAM_BOT_TOKEN", default="")
    TELEGRAM_CHAT_ID: int = Field(validation_alias="RNOTIFY_TELEGRAM_CHAT_ID", default=0)


settings = Settings()
scraper_settings = ScraperSettings()
notifier_settings = NotifierSettings()
