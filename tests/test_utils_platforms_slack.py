from slack_sdk import WebClient

from utils.platforms.slack import send_slack_message


def test_send_slack_message_success(requests_mock):
    client = WebClient()
    resp = client.api_test()
    assert resp.status_code == 200


def test_send_slack_message_fail(requests_mock):
    status, _ = send_slack_message(
        bot_token="bot_token", channel_id="chat_id", message_body="message_body"
    )
    assert status is False
