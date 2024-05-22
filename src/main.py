from utils import render_notification
from database import get_db_session
from config import settings

from providers.github import get_github_latest_release
from providers.gitlab import get_gitlab_latest_release

from cruds.release import add_release, get_unnotified_releases, delete_notified_release
from cruds.repo import get_repos

from platforms.telegram import send_telegram_message


def scrap():
    repositories = [item.as_dict() for item in get_repos(db_session=get_db_session())]

    for item in repositories:
        if item['provider'] == "github":
            release_body = get_github_latest_release(owner=item["owner"], repo=item["repo"])
            add_release(provider=item['provider'], owner=item['owner'], repo=item['repo'], tag=release_body["tag_name"], changelog=release_body["body"], db_session=get_db_session())

        elif item['provider'] == "gitlab":
            release_body = get_gitlab_latest_release(owner=item["owner"], repo=item["repo"])
            add_release(provider=item['provider'], owner=item['owner'], repo=item['repo'], tag=release_body["tag_name"], changelog=release_body["description"], db_session=get_db_session())

        
def notify():
    releases = get_unnotified_releases(db_session=get_db_session())

    for release in releases:
        message_body = render_notification( provider=release.provider, owner=release.owner, repo=release.repo, tag=release.tag)
        send_telegram_message(bot_token=settings.TELEGRAM_BOT_TOKEN, chat_id=settings.TELEGRAM_CHAT_ID, message_body=message_body)


def clean():
    delete_notified_release(db_session=get_db_session())


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        sys.exit(0)

    if sys.argv[1] == "scrap":
        scrap()
    elif sys.argv[1] == "notify":
        notify()
    elif sys.argv[1] == "clean":
        clean()
