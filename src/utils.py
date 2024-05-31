from jinja2 import Environment, FileSystemLoader

from config import notifier_settings
from platforms.telegram import send_telegram_message


# Notification message rendering
def render_notification(provider: str, owner: str, repo: str, tag: str) -> str:
    template = Environment(loader=FileSystemLoader(notifier_settings.NOTIFICATION_TEMPLATES)).get_template("notification.txt.j2")
    return template.render(provider=provider.title(), owner=owner, repo=repo, tag=tag)


def render_notification_markdown(provider: str, owner: str, repo: str, tag: str) -> str:
    template = Environment(loader=FileSystemLoader(notifier_settings.NOTIFICATION_TEMPLATES)).get_template("notification.md.j2")
    return template.render(provider=provider.title(), owner=owner, repo=repo, tag=tag)


# Send notification
def send_notification(provider: str, owner: str, repo: str, tag: str, notification_methods: list[str]) -> None:
    for item in notification_methods:
        if item == "telegram":
            message = render_notification(provider=provider, owner=owner, repo=repo, tag=tag)
            send_telegram_message(bot_token=notifier_settings.TELEGRAM_BOT_TOKEN, chat_id=notifier_settings.TELEGRAM_CHAT_ID, message=message)
