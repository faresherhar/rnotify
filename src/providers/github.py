import requests

from config import settings


def get_github_releases(owner: str, repo: str) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(settings.GITHUB_API + f"{owner}/{repo}/releases")
    return response.json() if response.status_code == 200 else None


def get_github_latest_release(owner: str, repo: str) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(settings.GITHUB_API + f"{owner}/{repo}/releases/latest")
    return response.json() if response.status_code == 200 else None


def get_github_release_by_tag_name(owner: str, repo: str, tag_name: str) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(settings.GITHUB_API + f"{owner}/{repo}/releases/tags/{tag_name}")
    return response.json() if response.status_code == 200 else None
