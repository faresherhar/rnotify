from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
import logging

import utils.logging_config as logging_config
from models.github import Github


# Define logger
logger = logging.getLogger(__name__)

def get_github_releases(db_session: Session) -> list[Github]:
    logger.info("Searching for Github release '{tag_name}'s")
    return db_session.query(Github).all()


def get_github_release(
    repo_name: str,
    tag_name: str,
    db_session: Session,
) -> Github | None:
    logger.info(f"Seraching fot Github release '{tag_name}'")
    return (
        db_session.query(Github)
        .filter(Github.repo_name == repo_name, Github.tag_name == tag_name)
        .one_or_none()
    )


def add_github_release(
    repo_name: str,
    tag_name: str,
    release_body: dict[str, str | dict[str, str]],
    db_session: Session,
) -> None:
    db_session.add(
        Github(
            repo_name=repo_name,
            tag_name=tag_name,
            release_body=release_body,
            notified=False,
        )
    )

    try:
        db_session.commit()
        logger.info(f"Adding Github release '{tag_name}'")
    except IntegrityError:
        logger.warning(f"Github release '{tag_name}' already exists")


def update_github_release(
    repo_name: str,
    tag_name: str,
    release_body: dict[str, str | dict[str, str]],
    db_session: Session,
) -> None:
    release = get_github_release(
        repo_name=repo_name, tag_name=tag_name, db_session=db_session
    )
    release.tag_name = tag_name
    release.release_body = release_body

    logger.info(f"Updating Github release '{tag_name}'")
    db_session.commit()
