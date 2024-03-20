from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def send_slack_message(message: str, channel_id: str, bot_token: str):
    client = WebClient(token=bot_token)
    try:
        response = client.chat_postMessage(channel=channel_id, text=message)
        assert response["message"]["text"] == message
    except SlackApiError as e:
        print(
            f"Slack Error {e.response['error']}, status_code {e.response.status_code}"
        )
