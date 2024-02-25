from utils.renderer import render_notification
from utils.platforms.email import send_email


message_body = render_notification(
    provider="gitlab",
    repo="AuroraOSS/AuroraStore",
    release_name="3.2.8",
    tag_name="3.2.8",
    type="html",
)

send_email(
    receiver_email="",
    message_body=message_body,
    subject="Release Notification",
    smtp_server="",
    user_email="",
    user_password="",
)
