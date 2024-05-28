import logging

import logging_config
from database import get_db_session
from providers.github import get_github_latest_release
from providers.gitlab import get_gitlab_latest_release
from cruds.release import add_release
from cruds.repo import get_repos


def scrap():
    repositories = [item.as_dict() for item in get_repos(db_session=get_db_session())]

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


if __name__ == "__main__":
    # Define logger
    logger = logging.getLogger(__name__)
    
    scrap()
