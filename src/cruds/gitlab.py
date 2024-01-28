from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
import logging

import utils.logging_config as logging_config
from models.gitlab import Gitlab


# Define logger
logger = logging.getLogger(__name__)

def get_gitlab_releases(db_session: Session) -> list[Gitlab]:
    logger.info("Searching for Gitlab releases")
    return db_session.query(Gitlab).all()


def get_gitlab_release(
    repo_name: str,
    tag_name: str,
    db_session: Session,
) -> Gitlab | None:
    logger.info(f"Seraching fot Gitlab release '{tag_name}'")
    return (
        db_session.query(Gitlab)
        .filter(Gitlab.repo_name == repo_name, Gitlab.tag_name == tag_name)
        .one_or_none()
    )


def add_gitlab_release(
    repo_name: str,
    tag_name: str,
    release_body: dict[str, str | dict[str, str]],
    db_session: Session,
) -> None:
    db_session.add(
        Gitlab(
            repo_name=repo_name,
            tag_name=tag_name,
            release_body=release_body,
            notified=False,
        )
    )

    try:
        db_session.commit()
        logger.info(f"Adding Gitlab release '{tag_name}'")
    except IntegrityError:
        logger.warning(f"Gitlab release '{tag_name}' already exists")

def update_gitlab_release(
    repo_name: str,
    tag_name: str,
    release_body: dict[str, str | dict[str, str]],
    db_session: Session,
) -> None:
    release = get_gitlab_release(
        repo_name=repo_name, tag_name=tag_name, db_session=db_session
    )
    release.tag_name = tag_name
    release.release_body = release_body

    logger.info(f"Updating Gitlab release '{tag_name}'")
    db_session.commit()
