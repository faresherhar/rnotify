from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session
import logging

import utils.logging_config as logging_config
from models.repo import Repo


# Define logger
logger = logging.getLogger(__name__)


def get_all_releases(db_session: Session) -> list[Repo]:
    logger.info("Searching for releases")
    return db_session.query(Repo).all()


def get_releases(provider: str, db_session: Session) -> list[Repo]:
    logger.info(f"Searching for {provider} releases")
    return db_session.query(Repo).filter(Repo.provider == provider).all()


def get_release(
    provider: str,
    repo_name: str,
    tag_name: str,
    db_session: Session,
) -> Repo | None:
    logger.info(f"Seraching fot {provider} repository {repo_name} release '{tag_name}'")
    return (
        db_session.query(Repo)
        .filter(
            Repo.provider == provider,
            Repo.repo_name == repo_name,
            Repo.tag_name == tag_name,
        )
        .one_or_none()
    )


def get_unnotified_releases(
    db_session: Session,
) -> list[Repo]:
    logger.info(f"Searching for unnotified releases")
    return db_session.query(Repo).filter(Repo.notified == False).all()


def add_release(
    provider: str,
    repo_name: str,
    tag_name: str,
    db_session: Session,
) -> None:
    db_session.add(
        Repo(
            provider=provider,
            repo_name=repo_name,
            tag_name=tag_name,
            notified=False,
        )
    )

    try:
        db_session.commit()
        logger.info(f"Adding {provider} repository {repo_name} release '{tag_name}'")
    except IntegrityError:
        logger.warning(
            f"{provider} repository {repo_name} release '{tag_name}' already exists"
        )


def update_release_notification_status(
    provider: str,
    repo_name: str,
    tag_name: str,
    db_session: Session,
) -> None:
    repo = (
        db_session.query(Repo)
        .filter(
            Repo.provider == provider,
            Repo.repo_name == repo_name,
            Repo.tag_name == tag_name,
        )
        .first()
    )
    try:
        repo.notified = True
        db_session.commit()
        logger.info(
            f"Setting {provider} repository {repo_name} release '{tag_name}' as notified"
        )

    except SQLAlchemyError:
        logger.error(
            f"Unable to update release {provider} repository {repo_name} release '{tag_name}'"
        )


def delete_notified_release(db_session: Session) -> None:
    db_session.query(Repo).filter(Repo.notified == True).delete()
    try:
        db_session.commit()
        logger.info(f"Deleting notified releases")

    except SQLAlchemyError:
        logger.error(f"Unable to delete notified releases")
