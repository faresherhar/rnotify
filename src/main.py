from config import settings
from database import engine, get_db_session
from models import Base

from models import Release
from utils import (
    get_github_latest_release,
    get_gitlab_latest_release,
    generate_release_url,
    render_notification_message,
    send_email,
)


if __name__ == "__main__":
    # Create release table if not exists
    Base.metadata.create_all(bind=engine)

    # Save new scraped releases
    scraped_releases = set()

    # Get the list of the stored releases
    db_session = get_db_session()
    stored_releases = set(
        db_session.query(Release.provider, Release.repo_name, Release.tag_name).all()
    )

    # Scrap github repositories for new releases
    for repo_name in settings.github_repos:
        response = get_github_latest_release(
            repo_name=repo_name, api_token=settings.github_api_token
        )
        if response.status_code == 200:
            scraped_releases.add(("github", repo_name, response.json()["tag_name"]))

    # Scrap gitlab repositories for new releases
    for repo_name in settings.gitlab_repos:
        response = get_gitlab_latest_release(
            repo_name=repo_name, api_token=settings.gitlab_api_token
        )
        if response.status_code == 200:
            scraped_releases.add(("gitlab", repo_name, response.json()["tag_name"]))

    # Create list of releases
    new_releases = []
    for item in scraped_releases.difference(stored_releases):
        new_releases.append(
            Release(
                provider=item[0],
                repo_name=item[1],
                tag_name=item[2],
                release_url=generate_release_url(*item),
            )
        )

    # Add the new releases into the database
    db_session.add_all(new_releases)
    db_session.commit()

    # Send notification email
    if len(new_releases) != 0:
        send_email(
            subject="Rnotify Releases Notification",
            message_body=render_notification_message(new_releases),
            recipient=settings.recipient,
            smtp_server=settings.smtp_server,
            smtp_username=settings.smtp_username,
            smtp_password=settings.smtp_password,
            smtp_port=settings.smtp_port,
        )
