from jinja2 import Environment, FileSystemLoader

from config import settings


# Notification message rendering
def render_notification_message(provider: str, owner: str, repo: str, tag: str) -> str:
    template = Environment(loader=FileSystemLoader(settings.NOTIFICATION_TEMPLATES)).get_template("notification.txt.j2")
    return template.render(provider=provider.title(), owner=owner, repo=repo, tag=tag)


def render_notification_message_markdown(provider: str, owner: str, repo: str, tag: str) -> str:
    template = Environment(loader=FileSystemLoader(settings.NOTIFICATION_TEMPLATES)).get_template("notification.md.j2")
    return template.render(provider=provider.title(), owner=owner, repo=repo, tag=tag)
