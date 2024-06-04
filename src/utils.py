from jinja2 import Environment, FileSystemLoader

from config import settings
from platforms.telegram import send_telegram_message
from platforms.slack import send_slack_message


# Notification message rendering
def render_notification(provider: str, owner: str, repo: str, tag: str) -> str:
    template = Environment(loader=FileSystemLoader(settings.NOTIFICATION_TEMPLATES)).get_template("notification.txt.j2")
    return template.render(provider=provider.title(), owner=owner, repo=repo, tag=tag)


def render_notification_markdown(provider: str, owner: str, repo: str, tag: str) -> str:
    template = Environment(loader=FileSystemLoader(settings.NOTIFICATION_TEMPLATES)).get_template("notification.md.j2")
    return template.render(provider=provider.title(), owner=owner, repo=repo, tag=tag)


# Send notification
def send_notification(provider: str, owner: str, repo: str, tag: str, notification_methods: list[str]) -> None:
    for item in notification_methods:
        if item == "telegram":
            message = render_notification(provider=provider, owner=owner, repo=repo, tag=tag)
            send_telegram_message(bot_token=settings.TELEGRAM_BOT_TOKEN, chat_id=settings.TELEGRAM_CHAT_ID, message=message)
        elif item == "slack":
            message = render_notification(provider=provider, owner=owner, repo=repo, tag=tag)
            send_slack_message(webhook_token=settings.SLACK_WEBHOOK_TOKEN, message=message)
