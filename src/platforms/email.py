import logging
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Define logger
logger = logging.getLogger(__name__)


def send_email(
    receiver_email: str,
    message_body: str,
    subject: str,
    smtp_server: str,
    user_email: str,
    user_password: str,
    port: int = 465,
) -> tuple[bool, Exception | None]:

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = user_email
    message["To"] = receiver_email

    message.attach(MIMEText(message_body, "html"))
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(user_email, user_password)
            server.sendmail(user_email, receiver_email, message.as_string())
            return True, None
        except Exception as err:
            return False, err
