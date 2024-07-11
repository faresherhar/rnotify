from redis import Redis
import logging

from config import settings
import logging_config
from notifier import send_email_notification
from utils import get_old_releases, get_github_latest_release, get_gitlab_latest_release


# Define logger
logger = logging.getLogger("Scraper")


if __name__ == "__main__":
    logger.info("Scraping new releases...")

    # Get releases that were already notified, from the backend database
    with Redis.from_url(settings.backend_uri, decode_responses=True) as db_seassion:
        old_releases = get_old_releases(db_seassion=db_seassion)

    # Save new scraped releases
    new_releases = set()

    # Scrap github repositories for new releases
    if len(settings.github_repos) != 0:
        for repo_name in settings.github_repos:
            response = get_github_latest_release(repo_name=repo_name, api_token=settings.github_api_token)
            if response.status_code == 200:
                new_releases.add(("github", repo_name, response.json()["tag_name"]))
    else:
        logger.warning("Github repositories not found")

    # Scrap gitlab repositories for new releases
    if len(settings.gitlab_repos) != 0:
        for repo_name in settings.gitlab_repos:
            response = get_gitlab_latest_release(repo_name=repo_name, api_token=settings.gitlab_api_token)
            if response.status_code == 200:
                new_releases.add(("gitlab", repo_name, response.json()["tag_name"]))
    else:
        logger.warning("Gitlab repositories not found")

    # Send notification for the new releases, that were not notified yet
    releases = new_releases - old_releases
    if len(releases) != 0:
        logger.info("Sending email notifications...")
        for release in releases:
            send_email_notification.delay(*release)
    else:
        logger.info("No new releases found...")
