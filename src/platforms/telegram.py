from requests import get, Response
import logging

from config import notifier_settings


# Define logger
logger = logging.getLogger(__name__)


def send_telegram_message(bot_token: str, chat_id: int, message: str) -> Response:
    params = {"chat_id": chat_id, "text": message}
    return get(notifier_settings.TELEGRAM_API + f"bot{bot_token}/sendMessage", params=params)
