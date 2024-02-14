from urllib.parse import quote
import requests
import logging

import utils.logging_config as logging_config
from config import settings


# Define logger
logger = logging.getLogger(__name__)


def get_gitlab_releases(repo_name: str) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(
        settings.GITLAB_API + f"{quote(repo_name, safe='')}/releases"
    )
    return response.json() if response.status_code == 200 else None


def get_gitlab_latest_release(repo_name: str) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(
        settings.GITLAB_API + f"{quote(repo_name, safe='')}/releases/permalink/latest"
    )
    return response.json() if response.status_code == 200 else None


def get_gitlab_release_by_tag_name(
    repo_name: str, tag_name: str
) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(
        settings.GITLAB_API + f"{quote(repo_name, safe='')}/releases/{tag_name}"
    )
    return response.json() if response.status_code == 200 else None
