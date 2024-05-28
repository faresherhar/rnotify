from requests import Request, get
import logging

from config import scraper_settings


# Define logger
logger = logging.getLogger(__name__)


def get_github_releases(owner: str, repo: str) -> Request:
    return get(scraper_settings.GITHUB_API + f"{owner}/{repo}/releases")


def get_github_latest_release(owner: str, repo: str) -> Request:
    return get(scraper_settings.GITHUB_API + f"{owner}/{repo}/releases/latest")


def get_github_release_by_tag_name(owner: str, repo: str, tag: str) -> Request:
    return get(scraper_settings.GITHUB_API + f"{owner}/{repo}/releases/tags/{tag}")
