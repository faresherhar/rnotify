from requests import Response, post
import logging

from config import notifier_settings


# Define logger
logger = logging.getLogger(__name__)


def send_slack_message(webhook_token: str, message: str) -> Response:
    return post(notifier_settings.SLACK_WEBHOOK_API + webhook_token, json={"text": message})
