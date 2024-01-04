from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.github import Github


def get_github_releases(db_session: Session) -> list[Github]:
    return db_session.query(Github).all()


def get_github_release(
    repo_name: str,
    release_id: int,
    db_session: Session,
) -> Github | None:
    return (
        db_session.query(Github)
        .filter(Github.repo_name == repo_name, Github.release_id == release_id)
        .one_or_none()
    )


def add_github_release(
    repo_name: str,
    release_id: int,
    release_body: dict[str, str | dict[str, str]],
    db_session: Session,
) -> None:
    db_session.add(
        Github(
            repo_name=repo_name,
            release_id=release_id,
            release_body=release_body,
            notified=False,
        )
    )

    try:
        db_session.commit()
    except IntegrityError:
        pass


def update_github_release(
    repo_name: str,
    release_id: int,
    release_body: dict[str, str | dict[str, str]],
    db_session: Session,
) -> None:
    release = get_github_release(
        repo_name=repo_name, release_id=release_id, db_session=db_session
    )
    release.release_id = release_id
    release.release_body = release_body

    db_session.commit()
