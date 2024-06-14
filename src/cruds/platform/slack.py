from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.platform.slack import Slack


def get_slack_webhooks(db_session: Session) -> list[Slack]:
    return db_session.query(Slack).all()


def get_slack_webhook(webhook_token: str, db_session: Session) -> Slack | None:
    return db_session.query(Slack).filter(Slack.webhook_token==webhook_token).one_or_none()


def add_slack_webhook(webhook_token: str, db_session: Session) -> None:
    db_session.add(Slack(webhook_token=webhook_token))

    try:
        db_session.commit()
        return
    except IntegrityError:
        pass


def delete_slack_webhook(webhook_token: str, db_session: Session) -> None:
    effected_rows = db_session.query(Slack).filter(Slack.webhook_token==webhook_token).delete()

    if effected_rows != 0:
        db_session.commit()
