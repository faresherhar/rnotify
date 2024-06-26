from smtplib import SMTP

from platforms.email import send_email


def test_send_email_success(smtpd):
    from_addr = "from.addr@example.org"
    to_addrs = "to.addr@example.org"
    msg = (
        f"From: {from_addr}\r\n"
        f"To: {to_addrs}\r\n"
        f"Subject: Foo\r\n\r\n"
        f"Foo bar"
    )

    with SMTP(smtpd.hostname, smtpd.port) as client:
        client.sendmail(from_addr, to_addrs, msg)

    assert len(smtpd.messages) == 1


def test_send_email_fail():
    status, _ = send_email(
        receiver_email="",
        message_body="",
        subject="",
        smtp_server="",
        user_email="",
        user_password="",
    )

    assert status is False
