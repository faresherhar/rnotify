from sqlalchemy.exc import IntegrityError
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
        .filter(Repo.repo_name == repo_name, Repo.tag_name == tag_name)
        .one_or_none()
    )


def add_release(
    provider: str,
    repo_name: str,
    tag_name: str,
    release_body: dict[str, str | dict[str, str]],
    db_session: Session,
) -> None:
    db_session.add(
        Repo(
            provider=provider,
            repo_name=repo_name,
            tag_name=tag_name,
            release_body=release_body,
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
