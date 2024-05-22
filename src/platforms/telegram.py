import requests

from config import settings


def send_telegram_message(bot_token: str, chat_id: int, message_body: str) -> requests.Request:
    params = {"chat_id": chat_id, "text": message_body}
    return requests.get(settings.TELEGRAM_API + f"bot{bot_token}/sendMessage", params=params)
