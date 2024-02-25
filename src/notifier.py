from utils.renderer import render_notification
from utils.platforms.email import send_email
from utils.platforms.slack import send_slack_message


message_body = render_notification(
    provider="gitlab",
    repo="AuroraOSS/AuroraStore",
    release_name="3.2.8",
    tag_name="3.2.8",
    type="html",
)
