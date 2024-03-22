from utils.platforms.email import send_email

from smtplib import SMTP

def test_send_email_success(smtpd):
    from_addr = "from.addr@example.org"
    to_addrs = "to.addr@example.org"
    msg = (f"From: {from_addr}\r\n"
            f"To: {to_addrs}\r\n"
            f"Subject: Foo\r\n\r\n"
            f"Foo bar")

    with SMTP(smtpd.hostname, smtpd.port) as client:
        client.sendmail(from_addr, to_addrs, msg)

    assert len(smtpd.messages) == 1


def test_send_email_fail(mocker):
    mocker.patch("utils.platforms.email.send_email", return_value=(False, Exception))
    status, _ = send_email(
        receiver_email="",
        message_body="",
        subject="",
        smtp_server="",
        user_email="",
        user_password="",
    )

    assert status is False
