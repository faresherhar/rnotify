from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.platform.telegram import Telegram


def get_telegram_bots(db_session: Session) -> list[Telegram]:
    return db_session.query(Telegram).all()


def get_telegram_bot(bot_token: str, chat_id: str, db_session: Session) -> Telegram | None:
    return db_session.query(Telegram).filter(Telegram.bot_token==bot_token, Telegram.chat_id==chat_id).one_or_none()


def add_telegram_bot(bot_token: str, chat_id: str, db_session: Session) -> None:
    db_session.add(Telegram(bot_token=bot_token, chat_id=chat_id))

    try:
        db_session.commit()
        return
    except IntegrityError:
        pass


def delete_telegram_bot(bot_token: str, chat_id: str, db_session: Session) -> None:
    effected_rows = db_session.query(Telegram).filter(Telegram.bot_token==bot_token, Telegram.chat_id==chat_id).delete()

    if effected_rows != 0:
        db_session.commit()
