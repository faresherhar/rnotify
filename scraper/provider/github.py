import requests

# from scraper.config import settings
from scraper.config import settings


def get_releases(repo_name: str):
	response = requests.get(
		settings.GITHUB_API + f"{repo_name}/releases", headers=settings.GITHUB_HEADERS
	)
	return response.json() if response.status_code == 200 else None


def get_latest_release(repo_name: str):
	response = requests.get(
		settings.GITHUB_API + f"{repo_name}/releases/latest",
		headers=settings.GITHUB_HEADERS,
	)
	return response.json() if response.status_code == 200 else None


def get_release(repo_name: str, release_id: str):
	response = requests.get(
		settings.GITHUB_API + f"{repo_name}/releases/{release_id}",
		headers=settings.GITHUB_HEADERS,
	)
	return response.json() if response.status_code == 200 else None
