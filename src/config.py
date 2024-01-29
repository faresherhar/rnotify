from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str = Field(validation_alias="UPME_DATABASE_URI")
    REPOS_FILE: str = Field(validation_alias="UPME_REPOS_FILE")

    GITHUB_API: str = "https://api.github.com/repos/"
    GITLAB_API: str = "https://gitlab.com/api/v4/projects/"

settings = Settings()
