from utils.platforms.telegram import send_telegram_message


def test_send_telegram_message_success(mocker):
    mocker.patch(
        "utils.platforms.telegram.send_telegram_message", return_value=(True, None)
    )

    status, _ = send_telegram_message(
        bot_token="bot_token", chat_id="chat_id", message_body="message_body"
    )
    assert status is True


def test_send_telegram_message_fail(requests_mock):
    requests_mock.get(
        "https://api.telegram.org/bot{bot_token}/sendMessage", status_code=404
    )

    status, _ = send_telegram_message(
        bot_token="bot_token", chat_id="chat_id", message_body="message_body"
    )
    assert status is False
