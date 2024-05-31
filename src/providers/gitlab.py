from requests import Response, get
import logging

from config import scraper_settings


# Define logger
logger = logging.getLogger(__name__)


def get_gitlab_releases(owner: str, repo: str) -> Response:
    return get(scraper_settings.GITLAB_API + f"{owner}%2F{repo}/releases")


def get_gitlab_latest_release(owner: str, repo: str) -> Response:
    return get(scraper_settings.GITLAB_API + f"{owner}%2F{repo}/releases/permalink/latest")


def get_gitlab_release_by_tag_name(owner: str, repo: str, tag: str) -> Response:
    return get(scraper_settings.GITLAB_API + f"{owner}%2F{repo}/releases/{tag}")
