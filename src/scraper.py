from redis import Redis

from config import settings
from utils import render_notification_message, get_old_releases, generate_release_url
from providers import get_github_latest_release, get_gitlab_latest_release
from notifier import send_email


if __name__ == "__main__":
    # with Redis.from_url(settings.backend_uri, decode_responses=True) as db_seassion:
    #     old_releases = get_old_releases(db_seassion=db_seassion)

    # new_releases = set()

    # for repo_name in settings.github_repos:
    #     response = get_github_latest_release(repo_name=repo_name, api_token=settings.github_api_token)
    #     if response.status_code == 200:
    #         new_releases.add(("github", repo_name, response.json()["tag_name"]))

    # for repo_name in settings.gitlab_repos:
    #     response = get_gitlab_latest_release(repo_name=repo_name, api_token=settings.gitlab_api_token)
    #     if response.status_code == 200:
    #         new_releases.add(("gitlab", repo_name, response.json()["tag_name"]))

    # for release in new_releases - old_releases:
    #     send_email_notification.delay(render_notification_message(*release))

    # releases = {('gitlab', 'AuroraOSS/AuroraStore', '4.5.1')}
    release = ("gitlab", "AuroraOSS/AuroraStore", "4.5.1")
    message_body = render_notification_message(*release)

    send_email_notification.delay(message_body)
