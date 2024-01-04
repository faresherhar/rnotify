import requests

from config import settings


def get_releases(repo_name: str) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(
        settings.GITHUB_API + f"{repo_name}/releases", headers=settings.GITHUB_HEADERS
    )
    return response.json() if response.status_code == 200 else None


def get_latest_release(repo_name: str) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(
        settings.GITHUB_API + f"{repo_name}/releases/latest",
        headers=settings.GITHUB_HEADERS,
    )
    return response.json() if response.status_code == 200 else None


def get_release_by_id(
    repo_name: str, release_id: int
) -> dict[str, str | dict[str, str]] | None:
    response = requests.get(
        settings.GITHUB_API + f"{repo_name}/releases/{release_id}",
        headers=settings.GITHUB_HEADERS,
    )
    return response.json() if response.status_code == 200 else None
