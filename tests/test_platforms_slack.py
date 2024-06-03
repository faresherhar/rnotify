from requests import Response

import platforms.slack


def test_send_slack_message_success(mocker):
    response = Response()
    response.status_code = 200

    mocker.patch("platforms.slack.send_slack_message", return_value=response)
    send_slack_response = platforms.slack.send_slack_message(webhook_token="webhook_token", message="message")

    assert send_slack_response.status_code == response.status_code


def test_send_slack_message_fail(mocker):
    response = Response()
    response.status_code = 404

    mocker.patch("platforms.slack.send_slack_message", return_value=response)
    send_slack_response = platforms.slack.send_slack_message(webhook_token="webhook_token", message="message")

    assert send_slack_response.status_code == response.status_code
