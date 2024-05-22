from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from models.repo import Repo


def get_repos(db_session: Session) -> list[Repo]:
    return db_session.query(Repo).all()


def get_repos_by_provider(provider: str, db_session: Session) -> list[Repo]:
    return db_session.query(Repo).filter(Repo.provider == provider).all()


def get_repos_by_owner(provider: str, owner: str, db_session: Session) -> list[Repo]:
    return db_session.query(Repo).filter(Repo.provider == provider, Repo.owner == owner).all()


def add_repo(provider: str, owner: str, repo: str, db_session: Session) -> None:
    db_session.add(Repo(provider=provider, owner=owner, repo=repo))

    try:
        db_session.commit()
        return
    except IntegrityError:
        pass


def delete_repo(provider: str, owner: str, repo: str, db_session: Session) -> None:
    effected_rows = db_session.query(Repo).filter(Repo.provider == provider, Repo.owner == owner, Repo.repo == repo).delete()

    if effected_rows > 0:
        db_session.commit()
