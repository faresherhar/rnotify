import logging

import logging_config
from database import get_db_session
from config import settings

from utils import render_notification_message
from providers.github import get_github_latest_release
from providers.gitlab import get_gitlab_latest_release
from platforms.telegram import send_telegram_message
from platforms.slack import send_slack_message
from cruds.release import (
    add_release,
    get_unnotified_releases,
    update_release_notification_status,
    delete_notified_release,
)
from cruds.repo import get_repos
from cruds.platform.telegram import get_telegram_bots
from cruds.platform.slack import get_slack_webhooks


# Scraping new releases
def scrap():
    repositories = [item.as_dict() for item in get_repos(db_session=get_db_session())]
    if repositories == []:
        logger.warning("No repositories found. Exiting...")
        exit(0)

    for item in repositories:
        if item["provider"] == "github":
            response = get_github_latest_release(owner=item["owner"], repo=item["repo"])
            if response.status_code == 200:
                release_body = response.json()
                add_release(
                    provider=item["provider"],
                    owner=item["owner"],
                    repo=item["repo"],
                    tag=release_body["tag_name"],
                    db_session=get_db_session(),
                )

        elif item["provider"] == "gitlab":
            response = get_gitlab_latest_release(owner=item["owner"], repo=item["repo"])
            if response.status_code == 200:
                release_body = response.json()
                add_release(
                    provider=item["provider"],
                    owner=item["owner"],
                    repo=item["repo"],
                    tag=release_body["tag_name"],
                    db_session=get_db_session(),
                )


# Notification Sending
def get_platforms_config():
    return {
        "telegram": get_telegram_bots(db_session=get_db_session())[0].as_dict(),
        "slack": get_slack_webhooks(db_session=get_db_session())[0].as_dict(),
    }


def send_notification(
    provider: str,
    owner: str,
    repo: str,
    tag: str,
    notification_methods: list[str],
    platforms_config: dict[str, dict[str, str]],
) -> None:
    for item in notification_methods:
        message = render_notification_message(
            provider=provider, owner=owner, repo=repo, tag=tag
        )
        if item == "telegram":
            if platforms_config[item] != None:
                send_telegram_message(
                    bot_token=platforms_config[item]["bot_token"],
                    chat_id=platforms_config[item]["chat_id"],
                    message=message,
                )
        elif item == "slack":
            if platforms_config[item] != None:
                send_slack_message(
                    webhook_token=platforms_config[item]["webhook_token"],
                    message=message,
                )


def notify():
    if settings.NOTIFICATION_METHODS == "":
        logger.warning("Nottifications configuration not found. Exiting...")
        exit(0)
    elif settings.NOTIFICATION_TEMPLATES == "":
        logger.warning("Nottifications templates not found. Exiting...")
        exit(0)

    notification_methods = [
        item.strip() for item in settings.NOTIFICATION_METHODS.split(",")
    ]
    releases = [
        item.as_dict() for item in get_unnotified_releases(db_session=get_db_session())
    ]

    for item in releases:
        send_notification(
            provider=item["provider"],
            owner=item["owner"],
            repo=item["repo"],
            tag=item["tag"],
            notification_methods=notification_methods,
            platforms_config=get_platforms_config(),
        )
        # update_release_notification_status(provider=item['provider'], owner=item['owner'], repo=item['repo'], tag=item["tag"], db_session=get_db_session())


def clean():
    delete_notified_release(db_session=get_db_session())


if __name__ == "__main__":
    import sys

    # Define logger
    logger = logging.getLogger(__name__)

    # Define different commands
    if len(sys.argv) > 1:
        if sys.argv[1] == "scrap":
            scrap()
        elif sys.argv[1] == "notify":
            notify()
        elif sys.argv[1] == "clean":
            clean()
