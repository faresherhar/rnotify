from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.release import Release


def get_all_releases(db_session: Session) -> list[Release]:
    return db_session.query(Release).all()


def get_unnotified_releases(db_session: Session) -> list[Release]:
    return db_session.query(Release).filter(Release.notified == False).all()


def get_releases_by_provider(provider: str, db_session: Session) -> list[Release]:
    return db_session.query(Release).filter(Release.provider == provider).all()


def get_release(provider: str, owner: str, repo: str, tag: str, db_session: Session) -> Release | None:
    return db_session.query(Release).filter(Release.provider == provider, Release.owner == owner, Release.repo == repo, Release.tag == tag).one_or_none()


def add_release(provider: str, owner: str, repo: str, tag: str, db_session: Session) -> None:
    db_session.add(Release(provider=provider, owner=owner, repo=repo, tag=tag, notified=False))

    try:
        db_session.commit()
    except IntegrityError:
        pass


def update_release_notification_status(provider: str, owner: str, repo: str, tag: str, db_session: Session) -> None:
    release = db_session.query(Release).filter(Release.provider == provider, Release.owner == owner, Release.repo == repo, Release.tag == tag).one_or_none()
    
    if release:
        release.notified = True
        db_session.commit()


def delete_notified_release(db_session: Session) -> None:
    effected_rows = db_session.query(Release).filter(Release.notified == True).delete()
    
    if effected_rows != 0:
        db_session.commit()
