from jinja2 import Environment, FileSystemLoader

from config import settings


def render_notification(provider: str, owner: str, repo: str, tag: str) -> str:
    template = Environment(loader=FileSystemLoader(settings.NOTIFICATION_TEMPLATES)).get_template("notification.txt")
    return template.render(provider=provider.title(), owner=owner, repo=repo, tag=tag)


def render_notification_markdown(provider: str, owner: str, repo: str, tag: str) -> str:
    template = Environment(loader=FileSystemLoader(settings.NOTIFICATION_TEMPLATES)).get_template("notification.md")
    return template.render(provider=provider.title(), owner=owner, repo=repo, tag=tag)
