import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


# Define logger
logger = logging.getLogger(__name__)


def send_slack_message(
    bot_token: str, channel_id: str, message_body: str
) -> tuple[bool, SlackApiError | None]:
    client = WebClient(token=bot_token)
    try:
        client.chat_postMessage(channel=channel_id, text=message_body)
        return True, None
    except SlackApiError as err:
        return False, err
