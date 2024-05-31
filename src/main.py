import logging

import logging_config
from database import get_db_session
from config import notifier_settings

from utils import send_notification

from providers.github import get_github_latest_release
from providers.gitlab import get_gitlab_latest_release

from cruds.release import add_release, get_unnotified_releases, update_release_notification_status, delete_notified_release
from cruds.repo import get_repos


def scrap():
    repositories = [item.as_dict() for item in get_repos(db_session=get_db_session())]
    if repositories == []:
        exit(0)
    
    for item in repositories:
        if item['provider'] == "github":
            response = get_github_latest_release(owner=item["owner"], repo=item["repo"])
            if response.status_code == 200:
                release_body = response.json()
                add_release(provider=item['provider'], owner=item['owner'], repo=item['repo'], tag=release_body["tag_name"], db_session=get_db_session())

        elif item['provider'] == "gitlab":
            response = get_gitlab_latest_release(owner=item["owner"], repo=item["repo"])
            if response.status_code == 200:
                release_body = response.json()
                add_release(provider=item['provider'], owner=item['owner'], repo=item['repo'], tag=release_body["tag_name"], db_session=get_db_session())


def notify():
    notification_methods = [item.strip() for item in notifier_settings.NOTIFICATION_METHODS.split(",")]
    if notification_methods == []:
        exit(0)
    
    releases = [item.as_dict() for item in get_unnotified_releases(db_session=get_db_session())]
    for item in releases:
        send_notification(provider=item['provider'], owner=item['owner'], repo=item['repo'], tag=item["tag"], notification_methods=notification_methods)
        update_release_notification_status(provider=item['provider'], owner=item['owner'], repo=item['repo'], tag=item["tag"], db_session=get_db_session())


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
