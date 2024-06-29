from urllib.parse import quote
from requests import Response, get

from config import settings


def get_auth(api_token: str) -> dict[str]:
    return {"Authorization": f"Bearer {api_token}"} if api_token != "" else {}


def get_github_latest_release(repo_name: str, api_token: str) -> Response:
    return get(
        settings.github_api_url + f"{repo_name}/releases/latest",
        headers=get_auth(api_token=api_token),
    )


def get_gitlab_latest_release(repo_name: str, api_token: str) -> Response:
    return get(
        settings.gitlab_api_url
        + f"{quote(repo_name, safe='')}/releases/permalink/latest",
        headers=get_auth(api_token=api_token),
    )
