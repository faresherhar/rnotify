from requests import Response

import platforms.telegram


def test_send_telegram_message_success(mocker):
    response = Response()
    response.status_code = 200

    mocker.patch("platforms.telegram.send_telegram_message", return_value=response)
    send_telegram_response = platforms.telegram.send_telegram_message(
        bot_token="bot_token", chat_id=12345678, message="message"
    )

    assert send_telegram_response.status_code == response.status_code


def test_send_telegram_message_fail(mocker):
    response = Response()
    response.status_code = 404

    mocker.patch("platforms.telegram.send_telegram_message", return_value=response)
    send_telegram_response = platforms.telegram.send_telegram_message(
        bot_token="bot_token", chat_id=12345678, message="message"
    )

    assert send_telegram_response.status_code == response.status_code
