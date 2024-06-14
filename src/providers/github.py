from requests import Response, get
import logging

from config import settings


# Define logger
logger = logging.getLogger(__name__)


def get_github_headers() -> dict[str, str]:
    if settings.GITHUB_API_TOKEN == "":
        return {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {settings.GITHUB_API_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def get_github_releases(owner: str, repo: str) -> Response:
    return get(
        settings.GITHUB_API + f"{owner}/{repo}/releases", headers=get_github_headers()
    )


def get_github_latest_release(owner: str, repo: str) -> Response:
    return get(
        settings.GITHUB_API + f"{owner}/{repo}/releases/latest",
        headers=get_github_headers(),
    )


def get_github_release_by_tag_name(owner: str, repo: str, tag: str) -> Response:
    return get(
        settings.GITHUB_API + f"{owner}/{repo}/releases/tags/{tag}",
        headers=get_github_headers(),
    )
