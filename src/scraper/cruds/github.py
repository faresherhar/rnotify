from sqlalchemy.orm import Session

from models.github import Github


def add_release(
    repo_name: str,
    release_id: int,
    release_body: dict[str, str | dict[str, str]],
    db_session: Session,
):
    pass
