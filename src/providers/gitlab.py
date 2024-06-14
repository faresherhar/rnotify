from requests import Response, get
import logging

from config import settings


# Define logger
logger = logging.getLogger(__name__)


def get_gitlab_headers() -> dict[str, str]:
    if settings.GITLAB_API_TOKEN == "":
        return {
            "Content-Type": "application/json",
        }

    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.GITLAB_API_TOKEN}",
    }


def get_gitlab_releases(owner: str, repo: str) -> Response:
    return get(
        settings.GITLAB_API + f"{owner}%2F{repo}/releases", headers=get_gitlab_headers()
    )


def get_gitlab_latest_release(owner: str, repo: str) -> Response:
    return get(
        settings.GITLAB_API + f"{owner}%2F{repo}/releases/permalink/latest",
        headers=get_gitlab_headers(),
    )


def get_gitlab_release_by_tag_name(owner: str, repo: str, tag: str) -> Response:
    return get(
        settings.GITLAB_API + f"{owner}%2F{repo}/releases/{tag}",
        headers=get_gitlab_headers(),
    )
