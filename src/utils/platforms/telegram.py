import requests

from config import settings


def send_telegram_message(
    bot_token: str, chat_id: str, message_body: str
) -> tuple[bool, Exception | None]:
    try:
        requests.get(
            settings.TELEGRAM_API.format(
                bot_token=bot_token, chat_id=chat_id, message_body=message_body
            )
        )
        return True, None
    except Exception as err:
        return False, err
