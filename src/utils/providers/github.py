import requests
import logging

import utils.logging_config as logging_config
from config import settings


# Define logger
logger = logging.getLogger(__name__)

def get_github_releases(repo_name: str) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(settings.GITHUB_API + f"{repo_name}/releases")
    return response.json() if response.status_code == 200 else None


def get_github_latest_release(repo_name: str) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(settings.GITHUB_API + f"{repo_name}/releases/latest")
    return response.json() if response.status_code == 200 else None


def get_github_release_by_tag_name(
    repo_name: str, tag_name: str
) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(settings.GITHUB_API + f"{repo_name}/releases/tags/{tag_name}")
    return response.json() if response.status_code == 200 else None
