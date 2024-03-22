from utils.renderer import render_notification
from utils.platforms.slack import send_slack_message
from utils.platforms.telegram import send_telegram_message
from utils.platforms.email import send_email


message_body = render_notification(
    provider="gitlab",
    repo="AuroraOSS/AuroraStore",
    release_name="3.2.8",
    tag_name="3.2.8",
    type="txt",
)
