from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str = Field(validation_alias="DATABASE_URI")
    GITHUB_API: str = "https://api.github.com/repos/"
    GITHUB_HEADERS: dict[str, str] = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


settings = Settings()
