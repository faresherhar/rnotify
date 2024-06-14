from pydantic import Field
from pydantic_settings import BaseSettings


#TODO: Add APIs documentation, and detail references
class Settings(BaseSettings):
    # Database URI
    DATABASE_URI: str = Field(validation_alias="RNOTIFY_DATABASE_URI")

    # Github API, Github API Token
    GITHUB_API: str = "https://api.github.com/repos/"
    GITHUB_RELEASE_URL: str = "https://github.com/{owner}/{repo}/releases/tag/{tag}"
    GITHUB_API_TOKEN: str = Field(validation_alias="RNOTIFY_GITHUB_API_TOKEN", default="")

    # Gitlab API, Gitlab API Token
    GITLAB_API: str = "https://gitlab.com/api/v4/projects/"
    GITLAB_RELEASE_URL: str = "https://gitlab.com/{owner}/{repo}/-/releases/{tag_name}"
    GITLAB_API_TOKEN: str = Field(validation_alias="RNOTIFY_GITLAB_API_TOKEN", default="")

    # Notifications templates.
    NOTIFICATION_TEMPLATES: str = Field(validation_alias="RNOTIFY_NOTIFICATION_TEMPLATES", default="")

    # What service to use to send notifications
    # Multiple methods can be chosen using a list[str].
    # email, slack, telegram
    NOTIFICATION_METHODS: str = Field(validation_alias="RNOTIFY_NOTIFICATION_METHODS", default="")

    # Notification Platforms API
    TELEGRAM_API: str = "https://api.telegram.org/"
    SLACK_WEBHOOK_API: str = "https://hooks.slack.com/services/"


settings = Settings()
