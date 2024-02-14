from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str = Field(validation_alias="UPME_DATABASE_URI")
    REPOS_FILE: str = Field(validation_alias="UPME_REPOS_FILE")
    NOTIFICATION_TEMPLATES: str = Field(validation_alias="UPME_NOTIFICATION_TEMPLATES")

    GITHUB_API: str = "https://api.github.com/repos/"
    GITHUB_RELEASE: str = "https://github.com/{repo}/releases/tag/{tag_name}"

    GITLAB_API: str = "https://gitlab.com/api/v4/projects/"
    GITLAB_RELEASE: str = "https://gitlab.com/{repo}/-/releases/{tag_name}"


settings = Settings()
