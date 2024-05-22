import requests

from config import settings


def get_gitlab_releases(owner: str, repo: str) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(settings.GITLAB_API + f"{owner}%2F{repo}/releases")
    return response.json() if response.status_code == 200 else None


def get_gitlab_latest_release(owner: str, repo: str) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(settings.GITLAB_API + f"{owner}%2F{repo}/releases/permalink/latest")
    return response.json() if response.status_code == 200 else None


def get_gitlab_release_by_tag_name(owner: str, repo: str, tag_name: str) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(settings.GITLAB_API + f"{owner}%2F{repo}/releases/{tag_name}")
    return response.json() if response.status_code == 200 else None
